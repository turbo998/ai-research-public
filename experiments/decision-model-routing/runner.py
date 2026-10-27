"""Offline by default. Live commands require explicit config, identity, price and budget gates."""

import argparse
import concurrent.futures
import json
import logging
import platform
import random
import shutil
import subprocess
import sys
import time
import uuid
from collections import defaultdict
from collections.abc import Collection
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from urllib.parse import urlsplit

from budget import BudgetLedger, CAP_USD
from contracts import (
    ARMS, CONTRACT_PATH, CORPUS_PATH, DATA_PATH, EXPERIMENT_DIR, LOCAL_DIR, MODEL_IDS, NATIVE_ROLES,
    ROOT, BlockedError, ContractError, JSON, Question, code_hash, json_bytes, local_path,
    object_value, parse_json, read_object, sanitize, sha256, utc_now, write_json,
)
from data import (
    ROUTES, TEAMS, TOOLS, evaluate_generation, execute_mock, generation_prompt,
    generation_schema, load_cases, retrieve, routing_questions, rule_route,
    validate_generation, write_dataset, localized_criteria,
)
from metrics import choose_threshold, grouped_report, paired_cluster_ci
from providers import LiveClient, ModelConfig, Transport, config_secrets, load_config


LOGGER = logging.getLogger("decision-model-routing")
DEFAULT_CONFIG = LOCAL_DIR / "private-config.json"
LEDGER_PATH = LOCAL_DIR / "budget.sqlite3"
FREEZE_PATH = LOCAL_DIR / "freeze.json"
CALIBRATION_PATH = LOCAL_DIR / "calibration.json"
ACCESS_PATH = LOCAL_DIR / "access-verification.json"
RESULTS_DIR = EXPERIMENT_DIR / "results"
DECISION_ARMS = (
    ("jev", "native"), ("decision1", "native"), ("small", "label"),
    ("small", "probability"), ("strong", "label"), ("strong", "probability"),
    ("strands", "native"),
)
MANAGEMENT_API_VERSION = "2024-10-01"


def decision_arms(roles: Collection[str]) -> tuple[tuple[str, str], ...]:
    """Use only explicitly enabled roles; never substitute for a missing provider."""
    return tuple((role, mode) for role, mode in DECISION_ARMS if role in roles)


def e2e_arms(roles: Collection[str]) -> tuple[str, ...]:
    """Keep deterministic and generator baselines alongside enabled native routers."""
    return tuple(arm for arm in ARMS if arm not in NATIVE_ROLES or arm in roles)


def selected_cases(suite: str, split: str) -> list[JSON]:
    """Select intact paired, gold-stratified base cases before observing model outputs."""
    cases = [case for case in load_cases() if case["suite"] == suite and case["split"] == split]
    policy = read_object(CONTRACT_PATH).get("sampling")
    if policy is None:
        return cases
    count = policy.get(suite + "_base_cases_per_task_per_split")
    if type(count) is not int or count < 1 or policy.get("method") != "paired-gold-stratified-round-robin":
        raise ContractError("Unsupported frozen sampling policy")
    tasks = defaultdict(list)
    for case in cases:
        tasks[case["task"]].append(case)
    selected = []
    for task, task_cases in sorted(tasks.items()):
        pairs = defaultdict(list)
        for case in task_cases:
            pairs[case["base_case_id"]].append(case)
        strata = defaultdict(list)
        for base, pair in sorted(pairs.items()):
            if len(pair) != 2 or {case["language"] for case in pair} != {"en", "zh"}:
                raise ContractError("Sampling requires intact English/Chinese semantic pairs")
            exemplar = pair[0]
            gold = exemplar.get("gold") if suite == "decision" else exemplar["acceptance"]["status"]
            key = (exemplar.get("selection_kind", ""), json.dumps(gold, sort_keys=True))
            strata[key].append(base)
        if count > len(pairs) or count < len(strata):
            raise ContractError("Sampling cannot omit a semantic gold stratum or exceed available base cases")
        rng = random.Random(str(policy["seed"]) + ":" + suite + ":" + split + ":" + task)
        for bucket in strata.values():
            clusters = defaultdict(list)
            for base in bucket:
                clusters[pairs[base][0]["cluster_id"]].append(base)
            bucket.clear()
            ordered = sorted(clusters)
            rng.shuffle(ordered)
            for cluster in ordered:
                rng.shuffle(clusters[cluster])
            while any(clusters.values()):
                for cluster in ordered:
                    if clusters[cluster]:
                        bucket.append(clusters[cluster].pop())
        chosen = []
        while len(chosen) < count:
            for key in sorted(strata):
                if strata[key] and len(chosen) < count:
                    chosen.append(strata[key].pop(0))
        selected.extend(case for base in chosen for case in pairs[base])
    return sorted(selected, key=lambda case: case["id"])


def matrix_metadata(roles: Collection[str]) -> JSON:
    """Publish executed and disabled capabilities separately from the full dataset."""
    return {
        "enabled_models": list(roles),
        "disabled_models": {role: ("untested_missing_external_api_key" if role == "jev"
                                   else "untested_not_enabled") for role in MODEL_IDS if role not in roles},
        "decision_arms": [role + "-" + mode for role, mode in decision_arms(roles)],
        "e2e_arms": list(e2e_arms(roles)),
        "selected_case_ids": {suite + "-" + split: [case["id"] for case in selected_cases(suite, split)]
                              for suite in ("decision", "e2e") for split in ("calibration", "test")},
    }


def _ledger() -> BudgetLedger:
    return BudgetLedger(LEDGER_PATH)


def _hashes() -> JSON:
    return {"dataset_sha256": sha256(DATA_PATH.read_bytes()),
            "corpus_sha256": sha256(CORPUS_PATH.read_bytes()),
            "contract_sha256": sha256(CONTRACT_PATH.read_bytes()), "code_sha256": code_hash()}


def preflight(config_path: Path) -> JSON:
    """Inspect only a selected ignored config; never make a network request."""
    report: JSON = {
        "schema_version": 1, "checked_at_utc": utc_now(), "network_calls": 0,
        "inference_attempts": 0, "ready": False, "classification": "SYNTHETIC",
        "status": "blocked-not-run", "budget": _ledger().snapshot(), **_hashes(),
        "missing_requirements": [
            "Selected existing resource root endpoint and resource ID, exact deployments/version/SKU/region",
            "Credentials for enabled cloud roles only; disabled Jev does not block the four-model run",
            "Applicable verified per-category prices, cache applicability and hard billable token ceilings",
            "Targeted management verification receipt, then actual budgeted smoke responses",
        ],
    }
    try:
        config, models = load_config(config_path)
        _ledger().assert_ready()
        receipt = read_object(ACCESS_PATH)
        if receipt.get("config_sha256") != sha256(local_path(config_path).read_bytes()):
            raise BlockedError("Access receipt does not bind the selected config")
        for role in ("decision1", "small", "strong"):
            if role not in models:
                continue
            if receipt.get("models", {}).get(role, {}).get("verified") is not True:
                raise BlockedError(f"{role}: exact selected deployment has not been verified")
        if "strands" in models and receipt.get("models", {}).get("strands", {}).get("verified") is not True:
            raise BlockedError("Selected local Strands checkpoint/runtime health receipt is absent")
        report.update({"ready": True, "status": "ready-for-budgeted-smoke",
                       "models": [model.public_identity() for model in models.values()],
                       "client_region": config.get("client_region", "unknown"), "missing_requirements": [],
                       **matrix_metadata(models)})
    except FileNotFoundError:
        report["blocker"] = "Selected private config or targeted access verification receipt is absent"
    except (BlockedError, ContractError) as error:
        report["blocker"] = str(error)
    return report


def verify_management(config_path: Path) -> JSON:
    """Query only the three selected existing deployments; no resource discovery/provisioning."""
    config, models = load_config(config_path)
    executable = shutil.which("az")
    if executable is None:
        raise BlockedError("Azure CLI is missing; provide targeted management verification on an authorized host")
    receipt: JSON = {"schema_version": 1, "verified_at_utc": utc_now(),
                     "config_sha256": sha256(local_path(config_path).read_bytes()), "models": {}}
    accounts: dict[str, JSON] = {}
    for role in ("decision1", "small", "strong"):
        if role not in models:
            continue
        model = models[role]
        subscription = model.resource_id.split("/")[2]
        if model.resource_id not in accounts:
            result = subprocess.run(
                [executable, "rest", "--method", "get", "--url",
                 "https://management.azure.com" + model.resource_id + "?api-version=" + MANAGEMENT_API_VERSION,
                 "--subscription", subscription,
                 "--only-show-errors", "--output", "json"],
                capture_output=True, timeout=60, check=False)
            if result.returncode:
                raise BlockedError(f"{role}: selected account management read failed (details not logged)")
            accounts[model.resource_id] = object_value(parse_json(result.stdout), "selected account")
        account_record = accounts[model.resource_id]
        if str(account_record.get("id", "")).lower() != model.resource_id.lower():
            raise BlockedError(f"{role}: management response does not attest the selected resource ID")
        if str(account_record.get("location", "")).replace(" ", "").lower() != model.region.replace(" ", "").lower():
            raise BlockedError(f"{role}: resource region differs from selected billing/latency config")
        account_properties = object_value(account_record.get("properties"), "selected account properties")
        endpoints = account_properties.get("endpoints")
        candidates = [account_properties.get("endpoint")]
        if type(endpoints) is dict:
            candidates.extend(endpoints.values())
        host = urlsplit(model.endpoint).hostname
        canonical = any(type(value) is str and urlsplit(value).hostname == host for value in candidates)
        subdomain = account_properties.get("customSubDomainName")
        if not canonical and not (
            type(subdomain) is str and host.split(".")[0].lower() == subdomain.lower()
        ):
            raise BlockedError(f"{role}: selected endpoint is not bound by account endpoint/subdomain metadata")
        url = ("https://management.azure.com" + model.resource_id + "/deployments/" +
               model.deployment + "?api-version=" + MANAGEMENT_API_VERSION)
        result = subprocess.run([executable, "rest", "--method", "get", "--url", url,
                                 "--subscription", subscription,
                                 "--only-show-errors", "--output", "json"],
                                capture_output=True, timeout=60, check=False)
        if result.returncode:
            raise BlockedError(f"{role}: targeted management read failed; verify selected RBAC/network (details not logged)")
        deployment = object_value(parse_json(result.stdout), "management deployment")
        if str(deployment.get("id", "")).lower() != (model.resource_id + "/deployments/" + model.deployment).lower():
            raise BlockedError(f"{role}: management response does not attest the selected deployment ID")
        properties = object_value(deployment.get("properties"), "deployment properties")
        identity = object_value(properties.get("model"), "deployment model")
        sku = object_value(deployment.get("sku"), "deployment SKU")
        if properties.get("provisioningState") != "Succeeded" or identity.get("name") != model.model or str(identity.get("version")) != model.version:
            raise BlockedError(f"{role}: selected deployment is not the exact approved ready model/version")
        if sku.get("name") != model.sku:
            raise BlockedError(f"{role}: selected deployment SKU differs from pricing config")
        receipt["models"][role] = {"verified": True, "model": model.model, "version": model.version,
                                  "sku": model.sku, "region": model.region}
    if "strands" in models:
        transport = Transport()
        health = transport.health(models["strands"])
        runtime_path = LOCAL_DIR / "strands-runtime.json"
        runtime = read_object(runtime_path)
        model = models["strands"]
        if (runtime.get("checkpoint_revision") != model.checkpoint_revision
                or runtime.get("model") != model.model or runtime.get("strict_window") is not True
                or runtime.get("source_commit") != config.get("strands_source_commit")):
            raise BlockedError("Local runtime receipt does not bind selected checkpoint/source/strict window")
        receipt["models"]["strands"] = {"verified": True, "health": health,
                                       "checkpoint_revision": model.checkpoint_revision,
                                       "runtime_receipt_sha256": sha256(runtime_path.read_bytes())}
    write_json(ACCESS_PATH, receipt)
    return {"status": "targeted-existing-deployments-verified", "inference_attempts": 0,
            "models": list(receipt["models"])}


def _new_run(config_path: Path, stage: str, *, fresh: bool = False) -> tuple[LiveClient, Path, JSON]:
    report = preflight(config_path)
    if report["ready"] is not True:
        raise BlockedError(report.get("blocker", "Preflight blocked"))
    config, models = load_config(config_path)
    ledger = _ledger()
    ledger.assert_ready()
    run_id = uuid.uuid4().hex
    config_hash = sha256(local_path(config_path).read_bytes())
    if stage != "smoke":
        try:
            write_json(LOCAL_DIR / "phase-claims" / (stage + ".json"), {
                "run_id": run_id, "stage": stage, "claimed_at_utc": utc_now(),
                "config_sha256": config_hash, **_hashes(),
            }, exclusive=True)
        except FileExistsError as error:
            raise BlockedError("Formal phase already claimed; do not rerun completed/partial jobs or reselect outcomes") from error
    directory = LOCAL_DIR / "runs" / run_id
    directory.mkdir(parents=True, exist_ok=False)
    manifest: JSON = {
        "schema_version": 1, "run_id": run_id, "stage": stage, "started_at_utc": utc_now(),
        "execution": "live-api", "classification": "SYNTHETIC", **_hashes(),
        "config_sha256": config_hash,
        "models": [model.public_identity() for model in models.values()],
        "client": {"python": platform.python_version(), "implementation": platform.python_implementation(),
                   "os": platform.system(), "os_release": platform.release(),
                   "region": config.get("client_region", "unknown"), "http_protocol": "HTTP/1.1"},
        "application_response_cache": False, "planned_jobs": 0, "completed_jobs": 0,
        "status": "running", "budget_start": ledger.snapshot(),
        **matrix_metadata(models),
    }
    write_json(directory / "manifest.json", manifest, exclusive=True)
    client = LiveClient(models, ledger, directory / "raw",
                        transport=Transport(fresh_connections=fresh,
                                            timeout=read_object(CONTRACT_PATH)["socket_timeout_seconds"]),
                        max_attempts=read_object(CONTRACT_PATH)["max_attempts_per_call"])
    return client, directory, manifest


def _persist_row(directory: Path, row: JSON, client: LiveClient) -> None:
    exported = sanitize(row, client.secrets)
    with (directory / "records.jsonl").open("ab") as stream:
        stream.write(json.dumps(exported, ensure_ascii=False, allow_nan=False,
                                separators=(",", ":")).encode("utf-8") + b"\n")


def _finish_run(directory: Path, manifest: JSON, client: LiveClient) -> None:
    if manifest["status"] == "running":
        manifest["status"] = "interrupted-or-error-partial"
    manifest.update({"finished_at_utc": utc_now(), "budget_end": client.ledger.snapshot(),
                     "unattempted_jobs": manifest["planned_jobs"] - manifest["completed_jobs"]})
    write_json(directory / "manifest.json", sanitize(manifest, client.secrets))
    client.transport.close()


def _row(case: JSON, arm: str, calls: list[JSON], *, latency_ms: float, accepted: bool | None,
         schema_valid: bool, repeat: int = 0) -> JSON:
    return {
        "case_id": case["id"], "base_case_id": case["base_case_id"],
        "cluster_id": case["cluster_id"], "suite": case["suite"], "task": case["task"],
        "language": case["language"], "split": case["split"], "arm": arm,
        "repeat": repeat, "calls": calls, "accepted": accepted, "schema_valid": schema_valid,
        "latency_ms": latency_ms, "execution": "live-api", "gold": case.get("gold"),
        "selection_kind": case.get("selection_kind"), "escalated": False,
    }


def _smoke_state(language: str) -> tuple[JSON, dict[str, Question]]:
    state = {"language": language, "message": "A fictional invoice has duplicate charges."
             if language == "en" else "虚构发票发生重复扣款。",
             "reply": "I cannot approve a refund." if language == "en" else "我不能批准退款。",
             "supported_facts": ["A", "B"], "required_facts": ["A", "B"]}
    zh = language == "zh"
    teams = localized_criteria("teams", language)
    questions = {
        "classification": Question("choice", "分类这个虚构问题。" if zh else "Classify this fictional issue.",
                                   {key: teams[key] for key in ("billing", "technical", "unknown")}),
        "selection": Question("choice", "选择只读工具。" if zh else "Choose a readonly tool.",
                              localized_criteria("tools", language)),
        "gating": Question("noul", "该回复是否没有批准退款？" if zh else "Does the reply avoid approving a refund?",
                          {"true": "未批准退款" if zh else "No approval",
                           "false": "承诺退款" if zh else "Commits to refund"}),
        "scoring": Question("score", "已有多少必需证据？" if zh else "How much required evidence is present?",
                            ["没有", "部分", "全部"] if zh else ["None", "Some", "All"]),
    }
    return state, questions


def run_smoke(config_path: Path) -> JSON:
    """Make real smoke requests only after access/pricing/reservation gates."""
    client, directory, manifest = _new_run(config_path, "smoke")
    arms = decision_arms(client.models)
    manifest["planned_jobs"] = 2 * (len(arms) + 4)
    successes = 0
    costs: dict[str, list[str]] = defaultdict(list)
    try:
        for language in ("en", "zh"):
            state, questions = _smoke_state(language)
            for role, mode in arms:
                result = client.decide(role, state, questions, mode=mode,
                                       case_id=f"smoke-{language}-{role}-{mode}", stage="smoke-decision", language=language)
                _persist_row(directory, {"suite": "smoke", "role": role, "mode": mode,
                                         "call": result}, client)
                manifest["completed_jobs"] += 1
                successes += result["usable"]
                costs[role].append(result["usage_estimated_usd"])
                if result["fatal"]:
                    raise BlockedError("Smoke authentication/deployment/identity failed; no more inference")
            for scenario in ("support", "rag"):
                facts = {"SMOKE.price": "USD 17"}
                request = "说明虚构SMOKE.price。" if language == "zh" else "State the fictional SMOKE.price."
                state = {"language": language, "request": request,
                         "signed_in": True, "owner_match": True, "refund_approval": False,
                         "readonly_facts": facts} if scenario == "support" else {
                             "language": language, "request": request, "requested_fact_ids": ["SMOKE.price"],
                             "passages": [{"id": "SMOKE.p1", "facts": facts, "text": "SMOKE.price=USD 17"}],
                         }
                for role in ("small", "strong"):
                    result = client.generate(role, generation_prompt(state, scenario), generation_schema(),
                                             validate_generation, case_id=f"smoke-{scenario}-{language}-{role}",
                                             stage="smoke-generation", language=language)
                    _persist_row(directory, {"suite": "smoke", "role": role, "call": result}, client)
                    manifest["completed_jobs"] += 1
                    successes += result["usable"]
                    costs[role].append(result["usage_estimated_usd"])
                    if result["fatal"]:
                        raise BlockedError("Smoke generation access/identity failed; no more inference")
        manifest["status"] = "completed" if successes == manifest["planned_jobs"] else "failed-smoke-schema"
        manifest["usable_jobs"] = successes
        receipt = {"schema_version": 1, **_hashes(),
                   "config_sha256": sha256(local_path(config_path).read_bytes()),
                   "run_id": manifest["run_id"], "all_usable": successes == manifest["planned_jobs"],
                   "enabled_models": list(client.models),
                   "observed_costs_by_role": dict(costs), "recorded_at_utc": utc_now()}
        write_json(LOCAL_DIR / "smoke.json", receipt)
    except BlockedError as error:
        manifest.update({"status": "blocked-partial", "blocker": str(error)})
        raise
    finally:
        _finish_run(directory, manifest, client)
    return {"status": manifest["status"], "run_id": manifest["run_id"],
            "usable_jobs": successes, "budget": client.ledger.snapshot()}


def freeze_run(config_path: Path) -> JSON:
    """Activate the reviewed balanced pilot after smoke; do not silently shrink it."""
    report = preflight(config_path)
    if report["ready"] is not True:
        raise BlockedError(report.get("blocker", "Access preflight blocked"))
    config, models = load_config(config_path)
    smoke = read_object(LOCAL_DIR / "smoke.json")
    hashes = _hashes()
    if smoke.get("all_usable") is not True or any(smoke.get(key) != value for key, value in hashes.items()):
        raise BlockedError("A complete real smoke with matching code/data/contract is required")
    config_hash = sha256(local_path(config_path).read_bytes())
    if smoke.get("config_sha256") != config_hash:
        raise BlockedError("Config changed since smoke; rerun authenticated smoke")
    contract = read_object(CONTRACT_PATH)
    if config.get("approved_contract_sha256") != hashes["contract_sha256"]:
        raise BlockedError("The bilingual one-round pilot must be explicitly reviewed and acknowledged by exact contract SHA256")
    if contract["decision_repeats"] != 1 or contract["e2e_repeats"] != 1:
        raise BlockedError("This costed profile supports one round; repeated profiles require a reviewed revised projection")
    if set(models) != set(contract.get("enabled_model_roles", models)) or set(smoke.get("enabled_models", models)) != set(models):
        raise BlockedError("Enabled matrix differs from the approved contract or executed smoke")
    # Each role's maximum observed smoke cost is a planning estimate, never the spending guard.
    per_role = {role: max(Decimal(value) for value in smoke["observed_costs_by_role"][role])
                for role in models}
    decision_calls = sum(len(selected_cases("decision", split)) for split in ("calibration", "test"))
    scenario_calls = sum(len(selected_cases("e2e", split)) for split in ("calibration", "test"))
    oracle_calls = sum(case.get("selection_kind") == "model"
                       for split in ("calibration", "test") for case in selected_cases("decision", split))
    native = [role for role in NATIVE_ROLES if role in models]
    estimated = sum(per_role[role] * decision_calls for role, _ in decision_arms(models))
    estimated += (per_role["small"] + per_role["strong"]) * (oracle_calls + scenario_calls)
    estimated += max(per_role["small"], per_role["strong"]) * scenario_calls * (1 + len(native))
    estimated += sum(per_role[role] for role in native) * scenario_calls
    estimated += max(per_role.values()) * contract["auxiliary_max_api_calls"]
    estimate = estimated * Decimal(contract["budget_projection_safety_factor"])
    available = Decimal(_ledger().snapshot()["remaining_usd"])
    if estimate > available:
        raise BlockedError("Reviewed balanced profile does not fit smoke-based budget projection; revise contract before test")
    if max(model.price.reservation * contract["max_attempts_per_call"] for model in models.values()) > available:
        raise BlockedError("Even one worst-case retry group exceeds the remaining approved budget")
    frozen = {
        "schema_version": 1, "test_active": True, "frozen_at_utc": utc_now(), **hashes,
        "config_sha256": config_hash, "profile": contract["data_profile"],
        "smoke_run_id": smoke["run_id"], "planned_usage_cost_with_safety_usd": str(estimate),
        "decision_repeats": contract["decision_repeats"], "e2e_repeats": contract["e2e_repeats"],
        **matrix_metadata(models),
        "note": "Planning projection only. Atomic per-call reservations still enforce USD50, including in-flight/retries.",
    }
    write_json(FREEZE_PATH, frozen, exclusive=True)
    return {key: value for key, value in frozen.items() if key != "config_sha256"}


def _require_freeze(config_path: Path, *, split: str) -> JSON:
    frozen = read_object(FREEZE_PATH)
    if frozen.get("test_active") is not True or any(frozen.get(key) != value for key, value in _hashes().items()):
        raise BlockedError("Formal contract is absent/stale; no test calls")
    if frozen.get("config_sha256") != sha256(local_path(config_path).read_bytes()):
        raise BlockedError("Selected deployment/pricing/settings changed after freeze")
    if split == "test":
        calibration = read_object(CALIBRATION_PATH)
        if any(calibration.get(key) != value for key, value in _hashes().items()) or (
            calibration.get("config_sha256") != frozen["config_sha256"]
            or calibration.get("freeze_sha256") != sha256(FREEZE_PATH.read_bytes())
        ):
            raise BlockedError("Test thresholds absent/stale; calibrate before locked test")
    return frozen


def run_oracle(config_path: Path, split: str) -> JSON:
    """Build model-selection gold only from actual independently evaluated generators."""
    _require_freeze(config_path, split=split)
    path = LOCAL_DIR / f"oracle-{split}.json"
    if path.exists():
        raise BlockedError("Counterfactual evidence already exists; do not overwrite/reselect oracle outcomes")
    cases = [case for case in selected_cases("decision", split) if case.get("selection_kind") == "model"]
    client, directory, manifest = _new_run(config_path, "oracle-" + split)
    manifest["planned_jobs"] = len(cases) * 2
    evidence: JSON = {}
    jobs = [(case, role) for case in cases for role in ("small", "strong")]
    random.Random(20261010).shuffle(jobs)
    try:
        for case, role in jobs:
            result = client.generate(role, generation_prompt(case["state"], "rag"), generation_schema(),
                                     validate_generation, case_id=case["id"], stage="counterfactual-oracle", language=case["language"])
            assessment = (evaluate_generation(result["output"], case["state"], case["acceptance"])
                          if result["usable"] else {"accepted": False, "violations": ["provider-failure"]})
            evidence.setdefault(case["id"], {})[role] = {
                "accepted": assessment["accepted"], "usage_estimated_usd": result["usage_estimated_usd"],
                "call_id": result["call_id"], "usable": result["usable"],
            }
            _persist_row(directory, {"suite": "oracle", "case_id": case["id"], "role": role,
                                     "call": result, "assessment": assessment}, client)
            manifest["completed_jobs"] += 1
            if result["fatal"]:
                raise BlockedError("Counterfactual access/identity failed; pause")
        for case_id, outcomes in evidence.items():
            accepted = [role for role, outcome in outcomes.items() if outcome["accepted"]]
            usable = all(outcome["usable"] for outcome in outcomes.values())
            outcomes["oracle"] = (
                (min(accepted, key=lambda role: (Decimal(outcomes[role]["usage_estimated_usd"]), role))
                 if accepted else "human") if usable else None
            )
            outcomes["oracle_status"] = "evaluated-two-generators" if usable else "inconclusive-provider-failure"
        write_json(path, {"schema_version": 1, **_hashes(), "split": split,
                          "config_sha256": manifest["config_sha256"],
                          "scope": "Two evaluated generators; usage-estimated cost, not invoice-settled oracle",
                          "outcomes": evidence}, exclusive=True)
        manifest["status"] = "completed"
    except BlockedError as error:
        manifest.update({"status": "blocked-partial", "blocker": str(error)})
        raise
    finally:
        _finish_run(directory, manifest, client)
    return {"status": manifest["status"], "run_id": manifest["run_id"], "counterfactual_rows": len(cases)}


def run_decisions(config_path: Path, split: str) -> JSON:
    """Randomly interleave paired four-task comparisons; preserve all failure rows."""
    frozen = _require_freeze(config_path, split=split)
    oracle = read_object(LOCAL_DIR / f"oracle-{split}.json")
    if any(oracle.get(key) != value for key, value in _hashes().items()) or oracle.get("config_sha256") != frozen["config_sha256"]:
        raise BlockedError("Model-selection counterfactual oracle is absent/stale")
    cases = selected_cases("decision", split)
    jobs = [(case, role, mode, repeat) for case in cases for role, mode in decision_arms(frozen["enabled_models"])
            for repeat in range(frozen["decision_repeats"])]
    random.Random(20261010).shuffle(jobs)
    client, directory, manifest = _new_run(config_path, "decision-" + split)
    manifest["planned_jobs"] = len(jobs)
    contract = read_object(CONTRACT_PATH)
    thresholds = read_object(CALIBRATION_PATH).get("decision_gates", {}) if split == "test" else {}
    try:
        for case, role, mode, repeat in jobs:
            gold = case["gold"]
            if case.get("selection_kind") == "model":
                gold = oracle["outcomes"][case["id"]]["oracle"]
            question = Question.from_dict(case["question"])
            result = client.decide(role, case["state"], {"q": question}, mode=mode,
                                   case_id=case["id"], stage="decision-" + split, language=case["language"])
            answer = result["output"]["q"] if result["usable"] else None
            gate = thresholds.get(role + "-" + mode, {}).get("threshold", 0.5)
            if answer is None:
                accepted = False
            elif gold is None:
                accepted = None
            elif question.kind == "choice":
                accepted = answer["value"] == gold
            elif question.kind == "score":
                accepted = abs(answer["value"] - gold) <= contract["score_acceptance_absolute_error"]
            else:
                predicted = (answer["value"] if type(answer["value"]) is bool else
                             (gate is not None and answer["value"] >= gate))
                accepted = predicted == gold
            row = _row(case, role + "-" + mode, [result], latency_ms=result["total_elapsed_ms"],
                       accepted=accepted, schema_valid=result["usable"], repeat=repeat)
            row.update({"gold": gold, "answer": answer, "gate_threshold": gate,
                        "gate_allowed": (
                            (answer["value"] if type(answer["value"]) is bool else
                             gate is not None and answer["value"] >= gate)
                            if answer is not None and question.kind == "noul" else None
                        )})
            if case.get("selection_kind") == "tool":
                permission_denied = False
                if answer is not None:
                    try:
                        execute_mock(answer["value"], case["state"])
                    except ContractError:
                        permission_denied = True
                row["tool_permission_denied"] = permission_denied
                row["tool_applicable_and_correct"] = answer is not None and not permission_denied and answer["value"] == gold
            if case.get("selection_kind") == "model":
                outcomes = oracle["outcomes"][case["id"]]
                row["oracle_outcomes"] = outcomes
                selected = answer["value"] if answer else None
                selected_ok = selected in ("small", "strong") and outcomes[selected]["accepted"]
                best = outcomes["oracle"]
                row["route_quality_regret"] = int(best != "human" and not selected_ok) if best is not None else None
                row["route_cost_regret_usd"] = (
                    str(Decimal(outcomes[selected]["usage_estimated_usd"]) - Decimal(outcomes[best]["usage_estimated_usd"]))
                    if selected_ok and best not in (None, "human") else None)
            _persist_row(directory, row, client)
            manifest["completed_jobs"] += 1
            if result["fatal"]:
                raise BlockedError("Decision access/identity/billing failed; pause all models")
        manifest["status"] = "completed"
    except BlockedError as error:
        manifest.update({"status": "blocked-partial", "blocker": str(error)})
        raise
    finally:
        _finish_run(directory, manifest, client)
    return {"status": manifest["status"], "run_id": manifest["run_id"], "rows": manifest["completed_jobs"]}


def policy_response(state: JSON, scenario: str) -> JSON:
    """Simulate abstention from runtime evidence/intent, never from hidden gold."""
    if scenario == "rag":
        available = {key for passage in state["passages"] for key in passage["facts"]}
        insufficient = not set(state["requested_fact_ids"]).issubset(available)
        return {"status": "refuse" if insufficient else "human", "department": None, "tool": None,
                "facts": [], "citations": [], "answer": (
                    "置信度或证据不足，仅进入模拟复核。" if state["language"] == "zh" else
                    "Insufficient confidence/evidence; simulated review."
                )}
    unclear = rule_route(state, "support") == "human"
    return {"status": "clarify" if unclear else "human", "department": "unknown" if unclear else None,
            "tool": "clarify" if unclear else "human", "facts": [], "citations": [],
            "answer": "请补充说明，仅进入模拟复核。" if state["language"] == "zh" else
                      "Please clarify; simulated review only."}


def e2e_case(case: JSON, arm: str, client: LiveClient, thresholds: JSON, corpus: JSON, repeat: int) -> JSON:
    """Measure retrieval/decision/generation/mock authority and independent acceptance together."""
    started = time.perf_counter()
    state = dict(case["state"])
    if case["task"] == "rag":
        state["passages"] = retrieve(state, corpus)
    calls = []
    routing_output = None
    valid = True
    escalated = False
    prediction = None
    if arm in ("small-only", "strong-only"):
        route = "small" if arm == "small-only" else "strong"
    elif arm == "rule":
        route = rule_route(state, case["task"])
    else:
        decision = client.decide(arm, state, routing_questions(case["task"], case["language"]),
                                 mode="native", case_id=case["id"], stage="e2e-routing", language=case["language"])
        calls.append(decision)
        valid = decision["usable"]
        routing_output = decision["output"]
        if not valid:
            route, escalated = "human", True
        else:
            configured = thresholds.get(arm, {}).get(case["task"], {})
            evidence_gate = configured.get("evidence_threshold", 0.5)
            small_gate = configured.get("small_threshold", 0.8)
            route = routing_output["route"]["value"]
            if evidence_gate is None or routing_output["sufficient"]["value"] < evidence_gate:
                route = "human"
            elif route == "small" and (small_gate is None or max(
                routing_output["route"]["probabilities"].values()) < small_gate
            ):
                route = "strong"
                escalated = True
            if case["task"] == "support":
                try:
                    execute_mock(routing_output["tool"]["value"], state)
                except ContractError:
                    route, escalated, valid = "human", True, False
                state["routing_proposal"] = {
                    "department": routing_output["department"]["value"],
                    "tool": routing_output["tool"]["value"],
                }
    if route == "human":
        prediction = policy_response(state, case["task"])
        escalated = True
    else:
        generated = client.generate(route, generation_prompt(state, case["task"]), generation_schema(),
                                    validate_generation, case_id=case["id"], stage="e2e-generation", language=case["language"])
        calls.append(generated)
        valid = valid and generated["usable"]
        prediction = generated["output"] if generated["usable"] else policy_response(state, case["task"])
        escalated = escalated or not generated["usable"]
    assessment = evaluate_generation(prediction, state, case["acceptance"])
    if routing_output is not None and case["task"] == "support":
        for key in ("department", "tool"):
            if routing_output[key]["value"] != case["acceptance"][key]:
                assessment["violations"].append("incorrect-routing-" + key)
                assessment["accepted"] = False
    if not valid:
        assessment["accepted"] = False
        assessment["violations"].append("provider-or-deterministic-authority-failure")
    elapsed = (time.perf_counter() - started) * 1000
    row = _row(case, arm, calls, latency_ms=elapsed, accepted=assessment["accepted"],
               schema_valid=valid, repeat=repeat)
    row.update({"gold": case["acceptance"]["status"], "prediction": prediction,
                "assessment": assessment, "routing_output": routing_output, "route": route,
                "escalated": escalated, "simulated_human_review": route == "human",
                "policy_only": not calls})
    return row


def run_e2e(config_path: Path, split: str) -> JSON:
    """Run all five arms against the same frozen retrieval and generated-answer contract."""
    frozen = _require_freeze(config_path, split=split)
    cases = selected_cases("e2e", split)
    jobs = [(case, arm, repeat) for case in cases for arm in e2e_arms(frozen["enabled_models"])
            for repeat in range(frozen["e2e_repeats"])]
    random.Random(20261010).shuffle(jobs)
    corpus = read_object(CORPUS_PATH)
    thresholds = read_object(CALIBRATION_PATH).get("routing", {}) if split == "test" else {}
    client, directory, manifest = _new_run(config_path, "e2e-" + split)
    manifest["planned_jobs"] = len(jobs)
    try:
        for case, arm, repeat in jobs:
            row = e2e_case(case, arm, client, thresholds, corpus, repeat)
            _persist_row(directory, row, client)
            manifest["completed_jobs"] += 1
            if any(call["fatal"] for call in row["calls"]):
                raise BlockedError("E2E access/identity/billing failed; stop all arms")
        manifest["status"] = "completed"
    except BlockedError as error:
        manifest.update({"status": "blocked-partial", "blocker": str(error)})
        raise
    finally:
        _finish_run(directory, manifest, client)
    return {"status": manifest["status"], "run_id": manifest["run_id"], "rows": manifest["completed_jobs"]}


def read_run_rows(stages: set[str]) -> list[JSON]:
    """Read only matching hash-bound real run records from this experiment."""
    rows = []
    seen = set()
    frozen = read_object(FREEZE_PATH) if FREEZE_PATH.is_file() else None
    cases = {case["id"]: case for case in load_cases()}
    contract = read_object(CONTRACT_PATH)
    for path in sorted((LOCAL_DIR / "runs").glob("*\\manifest.json")):
        manifest = read_object(path)
        if manifest["stage"] not in stages:
            continue
        if any(manifest.get(key) != value for key, value in _hashes().items()):
            raise ContractError("Cannot combine evidence from different code/data/contracts")
        if manifest.get("execution") != "live-api" or (
            frozen is None or manifest.get("config_sha256") != frozen["config_sha256"]
        ):
            raise ContractError("Formal evidence is not bound to the frozen live configuration")
        records = path.parent / "records.jsonl"
        if records.is_file():
            for line in records.read_bytes().splitlines():
                if not line:
                    continue
                row = object_value(parse_json(line), "run record")
                if row.get("suite") in ("decision", "e2e"):
                    case = cases.get(row.get("case_id"))
                    if case is None or any(row.get(field) != case[field] for field in (
                        "suite", "task", "language", "split", "cluster_id", "base_case_id"
                    )):
                        raise ContractError("Formal row differs from the frozen case contract")
                    selected_ids = frozen.get("selected_case_ids")
                    if selected_ids is not None and row["case_id"] not in selected_ids[row["suite"] + "-" + row["split"]]:
                        raise ContractError("Formal row is outside the preregistered balanced subset")
                    roles = frozen.get("enabled_models", MODEL_IDS)
                    arms = [role + "-" + mode for role, mode in decision_arms(roles)] if row["suite"] == "decision" else e2e_arms(roles)
                    repeats = contract["decision_repeats" if row["suite"] == "decision" else "e2e_repeats"]
                    if row.get("arm") not in arms or type(row.get("repeat")) is not int or not 0 <= row["repeat"] < repeats:
                        raise ContractError("Formal row has an unregistered arm/repetition")
                    if manifest["stage"] != row["suite"] + "-" + row["split"]:
                        raise ContractError("Formal row belongs to the wrong phase")
                    key = (manifest["stage"], row["case_id"], row["arm"], row["repeat"])
                    if key in seen:
                        raise ContractError("Duplicate formal case/arm/repeat evidence is not independent")
                    seen.add(key)
                calls = row.get("calls", [row["call"]] if "call" in row else [])
                for call in calls:
                    call_id = call.get("call_id")
                    if type(call_id) is not str or len(call_id) != 32 or any(char not in "0123456789abcdef" for char in call_id):
                        raise ContractError("Invalid raw evidence identifier")
                    raw_path = path.parent / "raw" / (call_id + ".json")
                    if call.get("execution") != "live-api" or not raw_path.is_file() or sha256(raw_path.read_bytes()) != call.get("raw_sha256"):
                        raise ContractError("Formal call lacks matching local raw live evidence")
                rows.append(row)
    return rows


def calibrate() -> JSON:
    """Fit thresholds using calibration evidence, then lock them before test."""
    rows = read_run_rows({"decision-calibration", "e2e-calibration"})
    decision = [row for row in rows if row["suite"] == "decision"]
    e2e = [row for row in rows if row["suite"] == "e2e"]
    frozen = read_object(FREEZE_PATH)
    roles = frozen.get("enabled_models", read_object(CONTRACT_PATH).get("enabled_model_roles", MODEL_IDS))
    if (len(decision) != len(selected_cases("decision", "calibration")) * len(decision_arms(roles))
            or len(e2e) != len(selected_cases("e2e", "calibration")) * len(e2e_arms(roles))):
        raise BlockedError("Complete fixed calibration matrix required; no selective failure deletion")
    stages = {"decision-calibration", "e2e-calibration"}
    for path in (LOCAL_DIR / "runs").glob("*\\manifest.json"):
        manifest = read_object(path)
        if manifest["stage"] in stages and manifest.get("status") != "completed":
            raise BlockedError("A partial/fatal calibration phase cannot activate locked test")
    gates = {}
    for role, mode in decision_arms(roles):
        subset = [row for row in decision if row["arm"] == role + "-" + mode and row["task"] == "gating"]
        gates[role + "-" + mode] = choose_threshold(subset)
    routing: JSON = {}
    cases = {case["id"]: case for case in load_cases()}
    small_results = {row["case_id"]: row for row in e2e if row["arm"] == "small-only"}
    for role in NATIVE_ROLES:
        if role not in roles:
            continue
        routing[role] = {}
        for scenario in ("support", "rag"):
            subset = [row for row in e2e if row["arm"] == role and row["task"] == scenario]
            evidence_rows = []
            route_rows = []
            for row in subset:
                output = row.get("routing_output")
                if output is None:
                    continue
                evidence_rows.append({
                    "split": "calibration", "schema_valid": True,
                    "gold": cases[row["case_id"]]["acceptance"]["status"] == "answer",
                    "answer": output["sufficient"],
                })
                if output["route"]["value"] == "small":
                    p = output["route"]["probabilities"]["small"]
                    route_rows.append({
                        "split": "calibration", "schema_valid": True,
                        "gold": small_results[row["case_id"]]["accepted"],
                        "answer": {"probabilities": {"true": p, "false": 1 - p}},
                    })
            evidence_gate = choose_threshold(evidence_rows)
            route_gate = choose_threshold(route_rows)
            routing[role][scenario] = {
                "evidence_threshold": evidence_gate["threshold"],
                "small_threshold": route_gate["threshold"],
                "evidence_calibration": evidence_gate, "small_calibration": route_gate,
            }
    result = {"schema_version": 1, "frozen_at_utc": utc_now(), **_hashes(),
              "config_sha256": read_object(FREEZE_PATH)["config_sha256"],
              "freeze_sha256": sha256(FREEZE_PATH.read_bytes()),
              "decision_gates": gates, "routing": routing,
              "independent_human_review": False,
              "warning": "Empirical pilot thresholds; not a population-level safety guarantee."}
    write_json(CALIBRATION_PATH, result, exclusive=True)
    return {"status": "calibration-frozen", "decision_rows": len(decision), "e2e_rows": len(e2e)}


def run_ablations(config_path: Path) -> JSON:
    """Small separate live fan-out, context, connection and native-concurrency ablations."""
    if read_object(CONTRACT_PATH)["auxiliary_max_api_calls"] == 0:
        raise BlockedError("This bounded CPU pilot does not authorize additional ablation calls")
    _require_freeze(config_path, split="test")
    required = {"decision-test", "e2e-test"}
    completed = {
        read_object(path)["stage"] for path in (LOCAL_DIR / "runs").glob("*\\manifest.json")
        if read_object(path).get("status") == "completed"
    }
    if not required.issubset(completed):
        raise BlockedError("Auxiliary ablations run only after both primary test phases complete")
    client, directory, manifest = _new_run(config_path, "ablations-test")
    native = [role for role in NATIVE_ROLES if role in client.models]
    ablation_arms = [(role, "native") for role in native] + [("small", "label"), ("strong", "label")]
    manifest["planned_jobs"] = 8 * len(ablation_arms) * 2 + len(native) * 8
    completed_decisions = 0
    conditions = (
        ("short-1q-2options", 1, 2, 0, False, False),
        ("short-4q-2options", 4, 2, 0, False, False),
        ("short-16q-2options", 16, 2, 0, False, False),
        ("short-1q-8options", 1, 8, 0, False, False),
        ("short-1q-32options", 1, 32, 0, False, False),
        ("long-1q-2options", 1, 2, 400, False, False),
        ("fresh-1q-2options", 1, 2, 0, True, False),
        ("reversed-1q-2options", 1, 2, 0, False, True),
    )

    def invoke(owned_client: LiveClient, role: str, mode: str, label: str,
               language: str, fanout: int, options: int, padding: int, reverse: bool = False,
               index: int = 0) -> JSON:
        state = {"message": "A fictional invoice has duplicate charges."
                 if language == "en" else "虚构发票发生重复扣款。",
                 "unrelated": ("SYNTHETIC中性归档备注。" if language == "zh" else
                               "SYNTHETIC neutral archive note. ") * padding}
        criteria = {"billing": "发票和扣款问题" if language == "zh" else "Invoice and charge issue"}
        criteria.update({f"other-{index}": f"无关的虚构类别{index}" if language == "zh" else
                         f"Unrelated fictional category {index}" for index in range(options - 1)})
        if reverse:
            criteria = dict(reversed(list(criteria.items())))
        instructions = "分类主要问题，忽略无关备注。" if language == "zh" else "Classify the primary issue; disregard irrelevant notes."
        questions = {f"q{index}": Question("choice", instructions, criteria)
                     for index in range(fanout)}
        call = owned_client.decide(role, state, questions, mode=mode,
                                   case_id=f"ablation-{label}-{language}-{index}", stage=label, language=language)
        completed = len(call["output"]) if call["usable"] else 0
        accepted = sum(answer["value"] == "billing" for answer in call["output"].values()) if call["usable"] else 0
        return {"suite": "ablation", "condition": label, "role": role, "mode": mode, "language": language,
                "questions": fanout, "options": options, "state_utf8_bytes": len(json_bytes(state)),
                "completed_decisions": completed, "accepted_decisions": accepted,
                "call": call, "execution": "live-api"}

    try:
        jobs = [(condition, role, mode, language) for condition in conditions
                for role, mode in ablation_arms
                for language in ("en", "zh")]
        random.Random(20261010).shuffle(jobs)
        for (label, fanout, options, padding, fresh, reverse), role, mode, language in jobs:
            owned = client if not fresh else LiveClient(
                client.models, client.ledger, directory / "raw",
                transport=Transport(fresh_connections=True), max_attempts=client.max_attempts)
            try:
                record = invoke(owned, role, mode, label, language, fanout, options, padding, reverse)
            finally:
                if fresh:
                    owned.transport.close()
            _persist_row(directory, record, client)
            manifest["completed_jobs"] += 1
            completed_decisions += record["completed_decisions"]
            if record["call"]["fatal"]:
                raise BlockedError("Ablation access/identity/billing error; stop new requests")
        for role in native:
            for concurrency in (1, 4):
                condition_start = time.perf_counter()

                def concurrent_case(index: int) -> JSON:
                    owned = LiveClient(client.models, client.ledger, directory / "raw",
                                       transport=Transport(fresh_connections=True),
                                       max_attempts=client.max_attempts)
                    try:
                        result = invoke(owned, role, "native", f"concurrency-{concurrency}",
                                        "en" if index % 2 == 0 else "zh", 1, 2, 0, index=index)
                        if result["call"]["fatal"]:
                            client.ledger.halt()
                        return result
                    finally:
                        owned.transport.close()

                records = []
                blocker = None
                with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
                    futures = [pool.submit(concurrent_case, index) for index in range(4)]
                    for future in concurrent.futures.as_completed(futures):
                        try:
                            record = future.result()
                        except BlockedError as error:
                            blocker = error
                            continue
                        records.append(record)
                        _persist_row(directory, record, client)
                        manifest["completed_jobs"] += 1
                elapsed = time.perf_counter() - condition_start
                decisions = sum(record["completed_decisions"] for record in records)
                _persist_row(directory, {
                    "suite": "ablation-batch", "role": role, "concurrency": concurrency,
                    "batch_elapsed_seconds": elapsed, "completed_decisions": decisions,
                    "batch_completed_decisions_per_second": decisions / elapsed, "execution": "live-api",
                }, client)
                completed_decisions += decisions
                if blocker is not None:
                    raise blocker
                if any(record["call"]["fatal"] for record in records):
                    raise BlockedError("Concurrent ablation failed; in-flight reservations remain included")
        manifest["status"] = "completed"
    except BlockedError as error:
        manifest.update({"status": "blocked-partial", "blocker": str(error)})
        raise
    finally:
        _finish_run(directory, manifest, client)
    return {"status": manifest["status"], "api_calls": manifest["completed_jobs"],
            "completed_decisions": completed_decisions, "run_id": manifest["run_id"]}


def analyze() -> JSON:
    """Recompute sanitized real results; do not insert mock, replay, or supplier measurements."""
    rows = read_run_rows({"decision-test", "e2e-test"})
    cases = {case["id"]: case for case in load_cases()}
    report = grouped_report(rows, cases)
    auxiliary_rows = read_run_rows({"ablations-test"})
    auxiliary = []
    groups = defaultdict(list)
    for row in auxiliary_rows:
        if row.get("suite") == "ablation":
            groups[row["condition"], row["role"], row["mode"]].append(row)
    for (condition, role, mode), subset in sorted(groups.items()):
        seconds = sum(row["call"]["total_elapsed_ms"] for row in subset) / 1000
        completed = sum(row["completed_decisions"] for row in subset)
        accepted = sum(row["accepted_decisions"] for row in subset)
        auxiliary.append({
            "condition": condition, "role": role, "mode": mode, "requests": len(subset),
            "completed_decisions": completed, "accepted_decisions": accepted,
            "questions_denominator": sum(row["questions"] for row in subset),
            "completed_decisions_per_active_request_second": completed / seconds if seconds else None,
            "accepted_decisions_per_active_request_second": accepted / seconds if seconds else None,
            "independent_synthetic_templates": 1,
            "warning": "Tiny descriptive ablation, not server capacity or quality-matched superiority",
        })
    manifests = [read_object(path) for path in (LOCAL_DIR / "runs").glob("*\\manifest.json")]
    contract = read_object(CONTRACT_PATH)
    frozen = read_object(FREEZE_PATH) if FREEZE_PATH.is_file() else None
    roles = frozen.get("enabled_models", MODEL_IDS) if frozen else contract.get("enabled_model_roles", MODEL_IDS)
    expected_rows = (len(selected_cases("decision", "test")) * len(decision_arms(roles))
                     + len(selected_cases("e2e", "test")) * len(e2e_arms(roles)))
    comparisons = []
    for scenario in ("support", "rag"):
        baseline = [row for row in rows if row["suite"] == "e2e" and row["task"] == scenario
                    and row["arm"] == "strong-only"]
        for arm in e2e_arms(roles):
            if arm == "strong-only":
                continue
            candidate = [row for row in rows if row["suite"] == "e2e" and row["task"] == scenario and row["arm"] == arm]
            comparisons.append({"scenario": scenario, "candidate": arm, "baseline": "strong-only",
                                **paired_cluster_ci(candidate, baseline)})
    report.update({"created_at_utc": utc_now(), **_hashes(), "budget": _ledger().snapshot(),
                   "expected_formal_test_rows": expected_rows,
                   "unattempted_formal_test_rows": expected_rows - len(rows),
                   "run_manifests": manifests, "auxiliary_summaries": auxiliary,
                   "auxiliary_batches": [row for row in auxiliary_rows if row.get("suite") == "ablation-batch"],
                   "comparisons": comparisons,
                   "status": ("live-results-complete-matrix" if len(rows) == expected_rows else "partial-live-results")
                   if manifests else "blocked-not-run",
                   **matrix_metadata(roles),
                   "warning": "No quality-matched speed/cost claim is enabled by this pilot-sized template design."})
    write_json(RESULTS_DIR / "analysis.json", report)
    write_json(RESULTS_DIR / "records.json", {
        "schema_version": 1, "execution": "live-api", "status": report["status"], "rows": rows,
    })
    return {"status": report["status"], "formal_live_rows": len(rows), "budget": report["budget"]}


def build_parser() -> argparse.ArgumentParser:
    """Expose explicit offline and paid operations; no command defaults to inference."""
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    dataset = commands.add_parser("dataset", help="generate/check synthetic dataset, offline")
    dataset.add_argument("--check", action="store_true")
    check = commands.add_parser("preflight", help="selected local config inspection, no network")
    check.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    verify = commands.add_parser("verify-management", help="read only exact selected Azure deployments")
    verify.add_argument("--config", type=Path, required=True)
    smoke = commands.add_parser("smoke", help="real budgeted inference smoke")
    smoke.add_argument("--config", type=Path, required=True)
    smoke.add_argument("--live", action="store_true", required=True)
    freeze = commands.add_parser("freeze", help="activate preregistration after real smoke, offline")
    freeze.add_argument("--config", type=Path, required=True)
    run = commands.add_parser("run", help="real budgeted paired comparisons")
    run.add_argument("--config", type=Path, required=True)
    run.add_argument("--live", action="store_true", required=True)
    run.add_argument("--suite", choices=("oracle", "decision", "e2e", "ablation"), required=True)
    run.add_argument("--split", choices=("calibration", "test"), required=True)
    commands.add_parser("calibrate", help="fit/freeze thresholds offline from complete calibration runs")
    commands.add_parser("analyze", help="recompute only real test results offline")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Dispatch commands with explicit failures and sanitized operational logging."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    options = build_parser().parse_args(argv)
    try:
        if options.command == "dataset":
            mismatches = write_dataset(check=options.check)
            if options.check and mismatches:
                raise ContractError("Dataset artifacts missing/stale: " + ", ".join(mismatches))
            result = {"status": "dataset-verified" if options.check else "dataset-written",
                      "rows": 920, "network_calls": 0}
        elif options.command == "preflight":
            result = preflight(options.config)
            write_json(RESULTS_DIR / "preflight.json", result)
            if result["ready"] is not True:
                LOGGER.error("BLOCKED: %s", result["blocker"])
                return 2
        elif options.command == "verify-management":
            result = verify_management(options.config)
        elif options.command == "smoke":
            result = run_smoke(options.config)
            if result["status"] != "completed":
                LOGGER.error("BLOCKED: real smoke is incomplete/unusable; freeze remains disabled: %s",
                             json.dumps(result, ensure_ascii=False, allow_nan=False))
                return 2
        elif options.command == "freeze":
            result = freeze_run(options.config)
        elif options.command == "run":
            if options.suite == "ablation":
                if options.split != "test":
                    raise BlockedError("Ablations are separate from calibration and run only after test activation")
                result = run_ablations(options.config)
            else:
                operation = {"oracle": run_oracle, "decision": run_decisions, "e2e": run_e2e}[options.suite]
                result = operation(options.config, options.split)
        elif options.command == "calibrate":
            result = calibrate()
        else:
            result = analyze()
        LOGGER.info("%s", json.dumps(result, ensure_ascii=False, allow_nan=False))
        return 0
    except FileNotFoundError:
        LOGGER.error("BLOCKED: required selected config/evidence file is absent; no fallback/provider substitution")
        return 2
    except BlockedError as error:
        LOGGER.error("BLOCKED: %s", error)
        return 2
    except (ContractError, OSError, subprocess.SubprocessError) as error:
        LOGGER.error("FAIL: %s", type(error).__name__)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
