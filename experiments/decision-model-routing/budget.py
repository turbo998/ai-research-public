"""One durable USD50 ledger, with atomic reservations for retries and in-flight calls."""

import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path

from contracts import BlockedError, ContractError, JSON, integer_value, utc_now


CAP_USD = Decimal("50")
MILLION = Decimal(1_000_000)


def usd(value: object, context: str) -> Decimal:
    """Require explicit nonnegative decimal text, never an unknown/free default."""
    if type(value) is not str:
        raise BlockedError(f"{context}: verified decimal USD rate required")
    try:
        result = Decimal(value)
    except InvalidOperation as error:
        raise BlockedError(f"{context}: invalid decimal USD rate") from error
    if not result.is_finite() or result < 0:
        raise BlockedError(f"{context}: finite nonnegative USD rate required")
    return result


@dataclass(frozen=True)
class Usage:
    """Output total includes reasoning; a missing breakdown stays unknown."""

    input_tokens: int
    output_tokens: int
    cached_tokens: int | None
    reasoning_tokens: int | None
    cache_write_tokens: int | None = None

    def __post_init__(self) -> None:
        integer_value(self.input_tokens, "usage.input_tokens")
        integer_value(self.output_tokens, "usage.output_tokens")
        if self.cached_tokens is not None:
            integer_value(self.cached_tokens, "usage.cached_tokens")
            if self.cached_tokens > self.input_tokens:
                raise ContractError("usage: cached input exceeds input total")
        if self.reasoning_tokens is not None:
            integer_value(self.reasoning_tokens, "usage.reasoning_tokens")
            if self.reasoning_tokens > self.output_tokens:
                raise ContractError("usage: reasoning exceeds output total")
        if self.cache_write_tokens is not None:
            integer_value(self.cache_write_tokens, "usage.cache_write_tokens")
            if self.cache_write_tokens + (self.cached_tokens or 0) > self.input_tokens:
                raise ContractError("usage: exclusive input categories exceed input total")

    def record(self) -> JSON:
        """Return actual reported counts; do not invent missing cache/reasoning counts."""
        return {
            "input_tokens": self.input_tokens, "output_tokens": self.output_tokens,
            "cached_tokens": self.cached_tokens, "reasoning_tokens": self.reasoning_tokens,
            "cache_write_tokens": self.cache_write_tokens,
        }


@dataclass(frozen=True)
class Price:
    """Verified rates and hard billable ceilings for one approved deployment."""

    input_rate: Decimal
    cached_rate: Decimal
    output_rate: Decimal
    reasoning_rate: Decimal
    input_ceiling: int
    output_ceiling: int
    cache_write_rate: Decimal = Decimal(0)
    cache_write_policy: str = "not_applicable"

    @classmethod
    def from_dict(cls, value: JSON) -> "Price":
        """Block unknown pricing or billing ceilings before any HTTP request."""
        if value.get("verified") is not True:
            raise BlockedError("Pricing is not verified for the selected deployment")
        for field in ("source", "verified_at", "billing_semantics", "ceiling_evidence"):
            if type(value.get(field)) is not str or not value[field].strip():
                raise BlockedError(f"Pricing requires {field}")
        policy = value.get("cache_write_policy")
        if policy not in ("not_applicable", "exclusive_input_category"):
            raise BlockedError("Pricing requires verified cache-write category applicability")
        if value["billing_semantics"] == "local_self_hosted_zero_api_fee":
            if any(usd(value.get(field), field) != 0 for field in (
                "input_usd_per_million", "cached_usd_per_million", "output_usd_per_million",
                "reasoning_usd_per_million", "cache_write_usd_per_million",
            )):
                raise BlockedError("Local zero-API pricing cannot contain a nonzero API rate")
        return cls(
            *(usd(value.get(field), field) for field in (
                "input_usd_per_million", "cached_usd_per_million",
                "output_usd_per_million", "reasoning_usd_per_million")),
            integer_value(value.get("max_billable_input_tokens"), "input ceiling", minimum=1),
            integer_value(value.get("max_billable_output_tokens"), "output ceiling"),
            usd(value.get("cache_write_usd_per_million"), "cache-write rate"), policy,
        )

    @property
    def reservation(self) -> Decimal:
        """Worst case covers unknown cache use and the entire reasoning/output cap."""
        return (self.input_ceiling * max(self.input_rate, self.cached_rate,
                                        self.cache_write_rate if self.cache_write_policy != "not_applicable" else Decimal(0))
                + self.output_ceiling * max(self.output_rate, self.reasoning_rate)) / MILLION

    def estimate(self, usage: Usage) -> Decimal:
        """Compute usage-based cost without double-counting reasoning tokens."""
        if usage.input_tokens > self.input_ceiling or (
            max(self.output_rate, self.reasoning_rate) > 0 and usage.output_tokens > self.output_ceiling
        ):
            raise BlockedError("Reported usage exceeded a verified billable ceiling; stop all calls")
        return self.observed_cost(usage)

    def observed_cost(self, usage: Usage) -> Decimal:
        """Retain reported charges even when a provider falsifies the verified ceiling."""
        write_rate = self.cache_write_rate if self.cache_write_policy != "not_applicable" else self.input_rate
        if usage.cached_tokens is None:
            input_cost = usage.input_tokens * max(self.input_rate, self.cached_rate, write_rate)
        else:
            writes = usage.cache_write_tokens
            remaining = usage.input_tokens - usage.cached_tokens
            input_cost = usage.cached_tokens * self.cached_rate
            if writes is None:
                input_cost += remaining * max(self.input_rate, write_rate)
            else:
                input_cost += (remaining - writes) * self.input_rate + writes * write_rate
        if usage.reasoning_tokens is None:
            output_cost = usage.output_tokens * max(self.output_rate, self.reasoning_rate)
        else:
            output_cost = ((usage.output_tokens - usage.reasoning_tokens) * self.output_rate
                           + usage.reasoning_tokens * self.reasoning_rate)
        return (input_cost + output_cost) / MILLION


class BudgetLedger:
    """Persist all phases in one SQLite database; crashes never release reservations."""

    def __init__(self, path: Path) -> None:
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as connection:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
            connection.execute(
                "CREATE TABLE IF NOT EXISTS calls (id TEXT PRIMARY KEY, model TEXT NOT NULL, "
                "reserved TEXT NOT NULL, estimated TEXT, unknown_upper TEXT, "
                "status TEXT NOT NULL, created TEXT NOT NULL)")
            connection.execute("INSERT OR IGNORE INTO metadata VALUES ('cap_usd', '50')")
            cap = connection.execute("SELECT value FROM metadata WHERE key='cap_usd'").fetchone()
            if cap != ("50",):
                raise BlockedError("Ledger cap differs from the approved USD50 total")

    @contextmanager
    def _connect(self):
        connection = sqlite3.connect(self.path, timeout=30)
        connection.execute("PRAGMA busy_timeout=30000")
        try:
            with connection:
                yield connection
        finally:
            connection.close()

    @staticmethod
    def _snapshot(connection: sqlite3.Connection) -> JSON:
        rows = connection.execute(
            "SELECT reserved, estimated, unknown_upper, status FROM calls").fetchall()
        reserved = sum((Decimal(row[0]) for row in rows if row[3] == "in-flight"), Decimal(0))
        estimated = sum((Decimal(row[1]) for row in rows if row[1] is not None), Decimal(0))
        unknown = sum((Decimal(row[2]) for row in rows if row[2] is not None), Decimal(0))
        return {
            "cap_usd": str(CAP_USD), "usage_estimated_usd": str(estimated),
            "unknown_cost_upper_usd": str(unknown), "in_flight_reserved_usd": str(reserved),
            "committed_upper_usd": str(estimated + unknown + reserved),
            "remaining_usd": str(CAP_USD - estimated - unknown - reserved),
            "reserved_logical_calls": len(rows), "invoice_settled_usd": None,
        }

    def snapshot(self) -> JSON:
        """Return estimate, unknown bounds, and in-flight amounts separately."""
        with self._connect() as connection:
            return self._snapshot(connection)

    def reserve(self, call_id: str, model: str, per_attempt: Decimal, attempts: int) -> None:
        """Atomically reserve every possible retry before the first billable attempt."""
        integer_value(attempts, "attempt count", minimum=1)
        if not per_attempt.is_finite() or per_attempt < 0:
            raise ContractError("Reservation must be finite and nonnegative")
        amount = per_attempt * attempts
        with self._connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            snapshot = self._snapshot(connection)
            if (connection.execute("SELECT COUNT(*) FROM calls WHERE status='ceiling-breach'").fetchone()[0]
                    or connection.execute("SELECT value FROM metadata WHERE key='halted'").fetchone()):
                raise BlockedError("Ledger locked after a ceiling breach")
            if Decimal(snapshot["remaining_usd"]) < amount:
                raise BlockedError("USD50 total exhausted including retries and in-flight calls")
            connection.execute(
                "INSERT INTO calls VALUES (?, ?, ?, NULL, NULL, 'in-flight', ?)",
                (call_id, model, str(amount), utc_now()))

    def finish(self, call_id: str, estimated: Decimal, unknown_upper: Decimal) -> None:
        """Keep unknown failure charges bounded; release only demonstrably unused retries."""
        for value in (estimated, unknown_upper):
            if not value.is_finite() or value < 0:
                raise ContractError("Finished costs must be finite and nonnegative")
        with self._connect() as connection:
            connection.execute("BEGIN IMMEDIATE")
            row = connection.execute(
                "SELECT reserved, status FROM calls WHERE id=?", (call_id,)).fetchone()
            if row is None or row[1] != "in-flight":
                raise ContractError("Cannot finish an absent or already-finished reservation")
            if estimated + unknown_upper > Decimal(row[0]):
                connection.execute(
                    "UPDATE calls SET status='ceiling-breach', estimated=?, unknown_upper=? WHERE id=?",
                    (str(estimated), str(unknown_upper), call_id))
                connection.commit()
                raise BlockedError("Cost exceeded reservation; ledger locked pending reconciliation")
            connection.execute(
                "UPDATE calls SET status='finished', estimated=?, unknown_upper=? WHERE id=?",
                (str(estimated), str(unknown_upper), call_id))

    def assert_ready(self) -> None:
        """Do not start a new process over unresolved crash or ceiling-breach evidence."""
        with self._connect() as connection:
            halted = connection.execute("SELECT value FROM metadata WHERE key='halted'").fetchone()
            if halted:
                raise BlockedError("Ledger halted after a billing-ceiling failure; manual reconciliation required")
            unresolved = connection.execute(
                "SELECT COUNT(*) FROM calls WHERE status != 'finished'").fetchone()[0]
            if unresolved:
                raise BlockedError("Unresolved in-flight/ceiling-breach ledger entries require reconciliation")

    def halt(self) -> None:
        """Stop future reservations when a verified billing ceiling was falsified."""
        with self._connect() as connection:
            connection.execute("INSERT OR REPLACE INTO metadata VALUES ('halted', 'billing-ceiling')")
