"""Explicit, in-memory Entra authentication for selected existing Azure deployments."""

import os
import re
import shutil
import subprocess
import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from threading import RLock

from contracts import (
    BlockedError, ContractError, JSON, object_value, parse_json, string_value,
)


TOKEN_RESOURCE = "https://cognitiveservices.azure.com"
REFRESH_MARGIN_SECONDS = 300


class CredentialError(BlockedError):
    """Selected authentication failed; no provider request or credential fallback."""


def acquire_token(arguments: list[str], *, auth_env: str) -> JSON:
    """Capture one scoped Azure CLI token response; never log stdout or stderr."""
    if not re.fullmatch(r"DECISION_ROUTING_[A-Z0-9_]+", auth_env):
        raise CredentialError("Entra acquisition requires the selected experiment credential name")
    if (len(arguments) != 6 or arguments[:2] != ["account", "get-access-token"]
            or arguments[2] != "--subscription" or arguments[4:] != ["--resource", TOKEN_RESOURCE]):
        raise CredentialError("Entra acquisition accepts only an explicitly scoped Cognitive Services token command")
    executable = shutil.which("az")
    if executable is None:
        raise CredentialError("Azure CLI is unavailable for selected Entra authentication")
    environment = os.environ.copy()
    environment.pop("TYPESAFE_API_KEY", None)
    environment.pop(auth_env, None)
    try:
        result = subprocess.run(
            [executable, *arguments, "--only-show-errors", "--output", "json"],
            capture_output=True, timeout=60, check=False, env=environment,
        )
    except subprocess.TimeoutExpired as error:
        raise CredentialError("Selected Entra acquisition timed out; no request or login fallback") from error
    except OSError as error:
        raise CredentialError("Selected Entra acquisition could not start Azure CLI") from error
    if result.returncode:
        codes = sorted(set(re.findall(rb"AADSTS[0-9]+", result.stderr)))
        suffix = " (" + ",".join(code.decode("ascii") for code in codes) + ")" if codes else ""
        raise CredentialError("Selected Entra acquisition failed" + suffix +
                              "; refresh the existing scoped login, without keys or security changes")
    try:
        return object_value(parse_json(result.stdout), "selected Entra response")
    except ContractError as error:
        raise CredentialError("Selected Entra response is malformed; raw output is not logged") from error


class EntraBearer:
    """Share a scope-checked, five-minute-margin token across roles and worker clients."""

    def __init__(self, identity: JSON, *, command: Callable[[list[str]], JSON] | None = None,
                 clock: Callable[[], float] = time.time) -> None:
        self.identity: JSON = dict(identity)
        self.subscription_id: str = string_value(identity.get("subscription_id"), "selected Azure subscription_id")
        self.tenant_id: str = string_value(identity.get("tenant_id"), "selected Azure tenant_id")
        for value in (self.subscription_id, self.tenant_id):
            if not re.fullmatch(r"[0-9a-fA-F-]{36}", value):
                raise CredentialError("Selected Azure subscription/tenant identifier is malformed")
        self.auth_env: str = string_value(identity.get("credential_env"), "selected Entra credential name")
        if not re.fullmatch(r"DECISION_ROUTING_[A-Z0-9_]+", self.auth_env):
            raise CredentialError("Entra authentication requires an explicit experiment credential name")
        if identity.get("token_resource") != TOKEN_RESOURCE:
            raise CredentialError("Selected Entra token audience must be Cognitive Services")
        self.command: Callable[[list[str]], JSON] = command if command is not None else (
            lambda arguments: acquire_token(arguments, auth_env=self.auth_env)
        )
        self.clock: Callable[[], float] = clock
        self._value: str = ""
        self._expires_on: int = 0
        self.acquisitions: int = 0
        self._lock: RLock = RLock()

    def validate_target(self, auth_env: str, resource_id: str | None) -> None:
        """Bind the credential to the configured subscription and auth name, without I/O."""
        expected = "/subscriptions/" + self.subscription_id + "/"
        if auth_env != self.auth_env or type(resource_id) is not str or not resource_id.lower().startswith(expected.lower()):
            raise CredentialError("Selected Entra scope does not match the deployment's subscription/auth name")

    def ensure_valid(self) -> None:
        """Refresh atomically before expiry; reject missing, mismatched or unsafe tokens."""
        with self._lock:
            if self._value and self._expires_on - self.clock() > REFRESH_MARGIN_SECONDS:
                return
            document = self.command([
                "account", "get-access-token",
                "--subscription", self.subscription_id,
                "--resource", TOKEN_RESOURCE,
            ])
            if str(document.get("subscription", "")).lower() != self.subscription_id.lower():
                raise CredentialError("Entra token response does not attest the selected subscription")
            if str(document.get("tenant", "")).lower() != self.tenant_id.lower():
                raise CredentialError("Entra token response does not attest the selected tenant; no login switch")
            token = document.get("accessToken")
            expiry = document.get("expires_on")
            if type(expiry) is str and expiry.isdigit():
                expiry = int(expiry)
            if document.get("tokenType") != "Bearer" or type(token) is not str or not re.fullmatch(r"[!-~]+", token):
                raise CredentialError("Selected Entra response has no valid Bearer token; token is never logged")
            if type(expiry) is not int or expiry - self.clock() <= REFRESH_MARGIN_SECONDS:
                raise CredentialError("Selected Entra expiry is missing/too close; no provider request")
            self._value, self._expires_on = token, expiry
            self.acquisitions += 1

    def headers(self) -> dict[str, str]:
        """Return fresh in-memory headers without changing process environment."""
        with self._lock:
            self.ensure_valid()
            return {"Authorization": "Bearer " + self._value}

    @contextmanager
    def injected(self) -> Iterator[None]:
        """Support a bounded local preflight context; the live path uses headers directly."""
        headers = self.headers()
        previous = os.environ.get(self.auth_env)
        os.environ[self.auth_env] = headers["Authorization"].removeprefix("Bearer ")
        try:
            yield
        finally:
            if previous is None:
                os.environ.pop(self.auth_env, None)
            else:
                os.environ[self.auth_env] = previous

    def metadata(self) -> JSON:
        """Expose only scope/expiry checks, never token material or token hashes."""
        with self._lock:
            return {
                "acquired": bool(self._value),
                "expires_on_utc_epoch": self._expires_on if self._value else None,
                "scope": TOKEN_RESOURCE,
                "selected_subscription_and_tenant_matched": bool(self._value),
                "acquisitions": self.acquisitions,
                "refresh_margin_seconds": REFRESH_MARGIN_SECONDS,
                "valid_for_preflight_now": bool(self._value) and self._expires_on - self.clock() > REFRESH_MARGIN_SECONDS,
                "data_plane_rbac_verified": False, "token_persisted": False,
                "long_run_integration": "Selected ModelConfig owns the shared Entra provider; LiveClient obtains fresh headers and registers rotated credentials before every HTTP attempt.",
            }

    def close(self) -> None:
        """Drop this provider's token reference after all dependent calls finish."""
        with self._lock:
            self._value = ""
            self._expires_on = 0
