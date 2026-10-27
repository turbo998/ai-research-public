"""Strict shared contracts for an opt-in, synthetic-only live experiment."""

import hashlib
import json
import math
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import TypeAlias


JSON: TypeAlias = dict[str, object]
EXPERIMENT_DIR = Path(__file__).resolve().parent
ROOT = EXPERIMENT_DIR.parents[1]
LOCAL_DIR = ROOT / ".cache" / "decision-model-routing"
DATA_PATH = EXPERIMENT_DIR / "data" / "cases.jsonl"
CORPUS_PATH = EXPERIMENT_DIR / "data" / "corpus.json"
CONTRACT_PATH = EXPERIMENT_DIR / "contract.json"
MODEL_IDS = {
    "jev": ("jev-1.13.0", "1.13.0"),
    "decision1": ("Microsoft-Decision-1", "1"),
    "small": ("gpt-5.4-mini", "2026-03-17"),
    "strong": ("gpt-6.1-sol", "2026-09-29"),
    "strands": ("strands-decider-2B-qwen3.5-v1-2610", "v1-2610"),
}
PUBLIC_LITERALS = {
    *(model for model, _ in MODEL_IDS.values()), *(model.lower() for model, _ in MODEL_IDS.values()),
    *(model + "-" + version for model, version in MODEL_IDS.values()),
    "billing", "technical", "account", "sales", "unknown", "small", "strong", "human",
    "invoice_lookup", "service_status", "kb_search", "clarify", "choice", "score", "noul",
}
ARMS = ("small-only", "strong-only", "rule", "jev", "decision1", "strands")
NATIVE_ROLES = ("jev", "decision1", "strands")
TASKS = ("classification", "selection", "gating", "scoring")
ADAPTER_VERSION = "2"


class ContractError(ValueError):
    """A local or provider payload violates the frozen experiment contract."""


class BlockedError(RuntimeError):
    """An explicit access, price, identity, or execution gate is unmet."""


def utc_now() -> str:
    """Return a timezone-aware timestamp, without machine or user identifiers."""
    return datetime.now(timezone.utc).isoformat()


def object_value(value: object, context: str) -> JSON:
    """Require a JSON object and reject non-string keys."""
    if type(value) is not dict or any(type(key) is not str for key in value):
        raise ContractError(f"{context}: expected an object with string keys")
    return value


def exact_keys(value: object, expected: set[str], context: str) -> JSON:
    """Require exactly the declared fields, not a success-shaped fallback."""
    document = object_value(value, context)
    if set(document) != expected:
        raise ContractError(f"{context}: unexpected or missing fields")
    return document


def string_value(value: object, context: str) -> str:
    """Require nonempty text without including its contents in errors."""
    if type(value) is not str or not value.strip():
        raise ContractError(f"{context}: expected nonempty text")
    return value


def integer_value(value: object, context: str, *, minimum: int = 0) -> int:
    """Reject bool, floats, and negative token counts."""
    if type(value) is not int or value < minimum:
        raise ContractError(f"{context}: expected an integer >= {minimum}")
    return value


def number_value(value: object, context: str) -> float:
    """Require a finite real number, never bool or a numeric string."""
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ContractError(f"{context}: expected a finite number")
    return float(value)


def probability(value: object, context: str) -> float:
    """Validate, but never clamp or renormalize, a probability."""
    result = number_value(value, context)
    if not 0 <= result <= 1:
        raise ContractError(f"{context}: probability outside [0, 1]")
    return result


def distribution(value: object, keys: tuple[str, ...], context: str, *,
                 rounding_radius: float = 0.0) -> dict[str, float]:
    """Reject missing options and invalid probability mass; preserve valid values."""
    document = exact_keys(value, set(keys), context)
    result = {key: probability(document[key], context) for key in keys}
    if not math.isclose(sum(result.values()), 1.0, rel_tol=0,
                        abs_tol=max(1e-5, len(keys) * rounding_radius) + 1e-12):
        raise ContractError(f"{context}: probabilities must sum to one")
    return result


def _unique_object(pairs: list[tuple[str, object]]) -> JSON:
    result: JSON = {}
    for key, value in pairs:
        if key in result:
            raise ContractError("JSON: duplicate object key")
        result[key] = value
    return result


def _invalid_constant(value: str) -> None:
    raise ContractError("JSON: non-finite constant")


def _finite_float(value: str) -> float:
    result = float(value)
    if not math.isfinite(result):
        raise ContractError("JSON: non-finite numeric value")
    return result


def parse_json(content: str | bytes) -> object:
    """Parse standards-compliant JSON with duplicate-key detection."""
    try:
        return json.loads(content, object_pairs_hook=_unique_object,
                          parse_constant=_invalid_constant, parse_float=_finite_float)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ContractError("JSON: malformed document") from error


def json_bytes(document: object) -> bytes:
    """Serialize deterministic UTF-8 JSON; do not emit NaN/Infinity."""
    return (json.dumps(document, ensure_ascii=False, indent=2,
                       allow_nan=False) + "\n").encode("utf-8")


def sha256(content: bytes) -> str:
    """Hash exact bytes, not normalized text."""
    return hashlib.sha256(content).hexdigest()


def read_object(path: Path) -> JSON:
    """Read a strict JSON object from an explicitly selected file."""
    return object_value(parse_json(path.read_bytes()), "document")


def write_json(path: Path, document: object, *, exclusive: bool = False) -> None:
    """Persist a JSON artifact; exclusive mode protects frozen evidence."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb" if exclusive else "wb") as stream:
        stream.write(json_bytes(document))


def local_path(path: Path) -> Path:
    """Confine private configuration and evidence to the ignored experiment folder."""
    resolved = path.resolve()
    if not resolved.is_relative_to(LOCAL_DIR.resolve()):
        raise BlockedError("Private config/evidence must be inside .cache\\decision-model-routing")
    return resolved


def code_hash() -> str:
    """Bind every experiment Python module to a content hash."""
    content = b"".join(path.name.encode() + b"\0" + path.read_bytes()
                       for path in sorted(EXPERIMENT_DIR.glob("*.py")))
    return sha256(content)


@dataclass(frozen=True)
class Question:
    """One bounded semantic judgment; criteria order is preserved."""

    kind: str
    instructions: str
    criteria: dict[str, str] | list[str]

    def __post_init__(self) -> None:
        string_value(self.instructions, "question.instructions")
        if self.kind == "choice":
            values = object_value(self.criteria, "choice.criteria")
            if not 2 <= len(values) <= 255:
                raise ContractError("Choice requires 2..255 distinct options")
            for key, description in values.items():
                string_value(key, "choice option")
                string_value(description, "choice description")
        elif self.kind == "score":
            if type(self.criteria) is not list or not 2 <= len(self.criteria) <= 10:
                raise ContractError("Score requires 2..10 ordered levels")
            for level in self.criteria:
                string_value(level, "score level")
        elif self.kind == "noul":
            values = exact_keys(self.criteria, {"true", "false"}, "noul.criteria")
            for description in values.values():
                string_value(description, "noul description")
        else:
            raise ContractError("Unsupported question type")

    @property
    def keys(self) -> tuple[str, ...]:
        """Return the exact permitted labels, or the ordered score indexes."""
        if self.kind == "score":
            return tuple(str(index) for index in range(len(self.criteria)))
        return tuple(self.criteria)

    def payload(self) -> JSON:
        """Render the official system-one question shape."""
        return {"type": self.kind, "instructions": self.instructions, "criteria": self.criteria}

    @classmethod
    def from_dict(cls, value: object) -> "Question":
        """Build a question from a frozen dataset object."""
        document = exact_keys(value, {"type", "instructions", "criteria"}, "question")
        return cls(document["type"], document["instructions"], document["criteria"])


@dataclass(frozen=True)
class Answer:
    """Validated result, preserving whether probabilities/confidence are native."""

    kind: str
    value: str | float | bool
    probabilities: dict[str, float] | None
    native_confidence: float | None
    probability_source: str

    @property
    def top_probability(self) -> float | None:
        """A distribution statistic, not independently observed correctness."""
        return max(self.probabilities.values()) if self.probabilities is not None else None

    def record(self) -> JSON:
        """Export only allowlisted numerical and closed-set result fields."""
        return {
            "type": self.kind, "value": self.value,
            "probabilities": self.probabilities, "native_confidence": self.native_confidence,
            "probability_source": self.probability_source,
        }


def _ordinal_confidence(sigma: float, count: int, ordinal_smoothing: float) -> float:
    maximum = (count - 1) / 2
    floor = math.sqrt(ordinal_smoothing)
    if maximum <= floor:
        return 1.0 if sigma <= floor else 0.0
    return max(0.0, min(1.0, (maximum - sigma) / (maximum - floor)))


def score_confidence(probabilities: dict[str, float], *, ordinal_smoothing: float) -> float:
    """Reproduce Strands' ordinal uncertainty, not Jev's different Score statistic."""
    if not 0 <= ordinal_smoothing <= 1:
        raise ContractError("Strands ordinal smoothing must be in [0, 1]")
    count = len(probabilities)
    mean = sum(index * probabilities[str(index)] for index in range(count))
    sigma = math.sqrt(sum(probabilities[str(index)] * (index - mean) ** 2
                          for index in range(count)))
    return _ordinal_confidence(sigma, count, ordinal_smoothing)


def _score_confidence_bounds(probabilities: dict[str, float], ordinal_smoothing: float,
                             radius: float) -> tuple[float, float]:
    """Bound the pre-rounding statistic; never replace or normalize reported probabilities."""
    count = len(probabilities)
    lower = [max(0.0, probabilities[str(index)] - radius) for index in range(count)]
    upper = [min(1.0, probabilities[str(index)] + radius) for index in range(count)]
    mean_low = sum(index * mass for index, mass in enumerate(lower))
    mean_high = sum(index * mass for index, mass in enumerate(upper))
    variance_low = sum(mass * (0.0 if mean_low <= index <= mean_high else
                               min(abs(index - mean_low), abs(index - mean_high)) ** 2)
                       for index, mass in enumerate(lower))
    variance_high = sum(mass * max(abs(index - mean_low), abs(index - mean_high)) ** 2
                        for index, mass in enumerate(upper))
    return (_ordinal_confidence(math.sqrt(variance_high), count, ordinal_smoothing),
            _ordinal_confidence(math.sqrt(variance_low), count, ordinal_smoothing))


def parse_answer(value: object, question: Question, *, provider: str, mode: str,
                 ordinal_smoothing: float = 0.1) -> Answer:
    """Validate native or LLM decisions without inventing missing vendor fields."""
    document = object_value(value, "answer")
    if document.get("type") != question.kind:
        raise ContractError("answer: question/answer type mismatch")
    native = provider in NATIVE_ROLES
    matched = native or mode == "probability"
    if not native:
        if mode not in ("label", "probability"):
            raise ContractError("answer: unapproved LLM output mode")
        result_field = {"choice": "choice", "score": "score",
                        "noul": "noul" if matched else "decision"}[question.kind]
        keys = {"type", result_field}
        if matched and question.kind != "noul":
            keys.add("probabilities")
        exact_keys(document, keys, "LLM answer")
    confidence = document.get("confidence")
    if provider in ("jev", "strands") and question.kind != "noul" and confidence is None:
        raise ContractError("Native answer: missing documented confidence")
    if confidence is not None:
        confidence = probability(confidence, "native confidence")
    if question.kind == "noul":
        if provider == "strands":
            exact_keys(document, {"type", "noul"}, "Strands Noul answer")
        if matched:
            p = probability(document.get("noul"), "noul")
            return Answer("noul", p, {"false": 1 - p, "true": p}, None,
                          "native" if native else "generated-estimate")
        decision = document.get("decision")
        if type(decision) is not bool:
            raise ContractError("label-only Noul requires a boolean decision")
        return Answer("noul", decision, None, None, "not-available")
    # The pinned Strands infer._to_answer rounds each field independently to four decimals.
    radius = 0.00005 if provider == "strands" else 0.0
    probabilities = (distribution(document.get("probabilities"), question.keys, "answer",
                                  rounding_radius=radius)
                     if matched else None)
    if question.kind == "choice":
        if provider == "strands":
            exact_keys(document, {"type", "choice", "probabilities", "confidence"}, "Strands Choice answer")
        selected = document.get("choice")
        if type(selected) is not str or selected not in question.keys:
            raise ContractError("answer: unknown choice")
        if probabilities is not None and probabilities[selected] < max(probabilities.values()) - 1e-5:
            raise ContractError("answer: selected option is not a probability maximum")
        if provider == "strands":
            expected_confidence = (len(question.keys) * max(probabilities.values()) - 1) / (len(question.keys) - 1)
            confidence_error = radius * (1 + len(question.keys) / (len(question.keys) - 1))
            if not math.isclose(confidence, expected_confidence, rel_tol=0, abs_tol=confidence_error + 1e-12):
                raise ContractError("Strands Choice confidence differs from its distribution")
        return Answer("choice", selected, probabilities, confidence if native else None,
                      "native" if native else ("generated-estimate" if matched else "not-available"))
    score = number_value(document.get("score"), "score")
    if not 0 <= score <= len(question.keys) - 1:
        raise ContractError("answer: score outside the requested scale")
    if probabilities is not None:
        expected = sum(index * probabilities[str(index)] for index in range(len(question.keys)))
        score_error = max(1e-4, radius * (1 + sum(range(len(question.keys)))))
        if not math.isclose(score, expected, rel_tol=0, abs_tol=score_error + 1e-12):
            raise ContractError("answer: score is inconsistent with its probability expectation")
    legend = document.get("legend")
    if provider in ("jev", "strands") or legend is not None:
        expected_legend = {str(index): level for index, level in enumerate(question.criteria)}
        if legend != expected_legend:
            raise ContractError("answer: missing or inconsistent score legend")
    if provider == "strands":
        exact_keys(document, {"type", "score", "probabilities", "confidence", "legend"}, "Strands Score answer")
        lower, upper = _score_confidence_bounds(probabilities, ordinal_smoothing, radius)
        if not lower - radius - 1e-12 <= confidence <= upper + radius + 1e-12:
            raise ContractError("Strands Score confidence differs from its ordinal distribution")
    return Answer("score", score, probabilities, confidence if native else None,
                  "native" if native else ("generated-estimate" if matched else "not-available"))


def sanitize(value: object, secrets: tuple[str, ...] = ()) -> object:
    """Redact known injected secrets and private identifiers, including nested strings."""
    if type(value) is dict:
        return {key: sanitize(item, secrets) for key, item in value.items()
                if key.lower() not in {"authorization", "api-key", "api_key", "headers"}}
    if type(value) is list or type(value) is tuple:
        return [sanitize(item, secrets) for item in value]
    if type(value) is str:
        if value in PUBLIC_LITERALS:
            return value
        text = value
        for secret in secrets:
            if secret:
                text = text.replace(secret, "<redacted>")
        text = re.sub(r"https?://[^\s\"<>]*(?:azure\.com|azure\.net)[^\s\"<>]*",
                      "<azure-endpoint-redacted>", text, flags=re.IGNORECASE)
        text = re.sub(r"/subscriptions/[^\s\"<>]+", "<resource-id-redacted>", text,
                      flags=re.IGNORECASE)
        return re.sub(r"\b[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}\b",
                      "<uuid-redacted>", text, flags=re.IGNORECASE)
    return value
