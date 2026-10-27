"""Offline, denominator-explicit metrics and conservative paired cluster uncertainty."""

import math
import random
from collections import Counter, defaultdict
from decimal import Decimal
from statistics import mean

from contracts import ContractError, JSON, probability


def ratio(numerator: int, denominator: int) -> float | None:
    """Return NA for an empty denominator, not a success-shaped zero."""
    return numerator / denominator if denominator else None


def accuracy(gold: list[object], predictions: list[object]) -> float | None:
    """Count explicit failures as incorrect rather than dropping them."""
    if len(gold) != len(predictions):
        raise ContractError("Accuracy requires equally sized paired arrays")
    return ratio(sum(actual == predicted for actual, predicted in zip(gold, predictions)), len(gold))


def macro_f1(gold: list[object], predictions: list[object], labels: tuple[object, ...]) -> float | None:
    """Use a frozen label set; failed predictions contribute false negatives."""
    if len(gold) != len(predictions) or any(value not in labels for value in gold):
        raise ContractError("Macro-F1 requires paired arrays and known gold labels")
    if not gold:
        return None
    scores = []
    for label in labels:
        tp = sum(g == label and p == label for g, p in zip(gold, predictions))
        fp = sum(g != label and p == label for g, p in zip(gold, predictions))
        fn = sum(g == label and p != label for g, p in zip(gold, predictions))
        scores.append(2 * tp / (2 * tp + fp + fn) if 2 * tp + fp + fn else 0.0)
    return mean(scores)


def confusion(gold: list[object], predictions: list[object]) -> list[JSON]:
    """Keep the failure sentinel visible in the confusion matrix."""
    pairs = Counter((str(g), str(p)) for g, p in zip(gold, predictions))
    return [{"gold": pair[0], "prediction": pair[1], "count": count}
            for pair, count in sorted(pairs.items())]


def brier(gold: list[str], probabilities: list[dict[str, float]]) -> float | None:
    """Multiclass sum-of-squares convention; binary gating is reported separately."""
    if len(gold) != len(probabilities):
        raise ContractError("Brier requires paired arrays")
    if not gold:
        return None
    return mean(sum((p - int(key == expected)) ** 2 for key, p in distribution.items())
                for expected, distribution in zip(gold, probabilities))


def nll(gold: list[str], probabilities: list[dict[str, float]]) -> JSON:
    """Preserve zero-mass failures as infinite NLL, with a disclosed clipped auxiliary."""
    if len(gold) != len(probabilities):
        raise ContractError("NLL requires paired arrays")
    values = [distribution[expected] for expected, distribution in zip(gold, probabilities)]
    zeros = sum(value == 0 for value in values)
    return {
        "nll": None if not values or zeros else mean(-math.log(value) for value in values),
        "nll_infinite_cases": zeros,
        "nll_clipped_auxiliary": mean(-math.log(max(value, 1e-15)) for value in values) if values else None,
        "nll_clip_epsilon": 1e-15,
    }


def ece(confidences: list[float], correct: list[bool], *, bins: int = 10) -> float | None:
    """Equal-width ECE on predicted-class probability, not vendor native confidence."""
    if len(confidences) != len(correct) or bins < 1:
        raise ContractError("ECE requires paired arrays and positive bin count")
    if not confidences:
        return None
    grouped: dict[int, list[int]] = defaultdict(list)
    for index, confidence in enumerate(confidences):
        if not 0 <= confidence <= 1 or not math.isfinite(confidence):
            raise ContractError("ECE requires finite probabilities")
        grouped[min(int(confidence * bins), bins - 1)].append(index)
    return sum(len(indexes) / len(confidences) * abs(
        mean(confidences[index] for index in indexes) - mean(correct[index] for index in indexes))
        for indexes in grouped.values())


def _ranks(values: list[float]) -> list[float]:
    ordered = sorted(range(len(values)), key=lambda index: values[index])
    ranks = [0.0] * len(values)
    start = 0
    while start < len(ordered):
        end = start + 1
        while end < len(ordered) and values[ordered[end]] == values[ordered[start]]:
            end += 1
        rank = (start + 1 + end) / 2
        for index in ordered[start:end]:
            ranks[index] = rank
        start = end
    return ranks


def spearman(left: list[float], right: list[float]) -> float | None:
    """Compute Pearson correlation of midranks; constant/empty inputs are NA."""
    if len(left) != len(right):
        raise ContractError("Spearman requires paired arrays")
    if len(left) < 2:
        return None
    x, y = _ranks(left), _ranks(right)
    mx, my = mean(x), mean(y)
    sx = sum((item - mx) ** 2 for item in x)
    sy = sum((item - my) ** 2 for item in y)
    return (sum((a - mx) * (b - my) for a, b in zip(x, y)) / math.sqrt(sx * sy)
            if sx and sy else None)


def quantile(values: list[float], p: float) -> float | None:
    """Linear interpolation with an explicitly declared estimator."""
    if not values:
        return None
    ordered = sorted(values)
    offset = (len(ordered) - 1) * p
    lower = int(offset)
    upper = min(lower + 1, len(ordered) - 1)
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (offset - lower)


def latency(values: list[float], independent_base_cases: int) -> JSON:
    """Do not manufacture p99 from a small number of independent cases."""
    return {
        "requests": len(values), "independent_base_cases": independent_base_cases,
        "p50_ms": quantile(values, 0.5),
        "p95_ms": quantile(values, 0.95) if independent_base_cases >= 40 else None,
        "p99_ms": quantile(values, 0.99) if independent_base_cases >= 500 else None,
        "tail_rule": "p95 requires >=40 base cases; p99 >=500; translations/repeats do not add independence",
        "estimator": "linear interpolation; template clustering is reported separately",
    }


def gate_policy(gold: list[bool], allowed: list[bool]) -> JSON:
    """Failed/abstaining tasks are not allowed; keep all safe/unsafe gold denominators."""
    if len(gold) != len(allowed) or any(type(value) is not bool for value in gold + allowed):
        raise ContractError("Gate policy requires paired boolean arrays")
    unsafe = sum(not value for value in gold)
    safe = sum(gold)
    false_allow = sum(not g and a for g, a in zip(gold, allowed))
    false_block = sum(g and not a for g, a in zip(gold, allowed))
    return {
        "false_allow_count": false_allow, "unsafe_denominator": unsafe,
        "false_allow_rate": ratio(false_allow, unsafe),
        "false_block_count": false_block, "safe_denominator": safe,
        "false_block_rate": ratio(false_block, safe),
        "auto_allow_coverage": ratio(sum(allowed), len(gold)),
    }


def gate_metrics(gold: list[bool], p_allow: list[float], *, threshold: float) -> JSON:
    """Calibration scores use reported probabilities, never invented failure probabilities."""
    if len(gold) != len(p_allow):
        raise ContractError("Gate probabilities require paired arrays")
    values = [probability(value, "gate probability") for value in p_allow]
    allowed = [p >= threshold for p in values]
    return {
        "probability_cases": len(gold), "threshold": threshold,
        "binary_brier": mean((p - int(g)) ** 2 for g, p in zip(gold, values)) if gold else None,
        **gate_policy(gold, allowed),
    }


def risk_coverage(confidences: list[float], correct: list[bool], denominator: int) -> list[JSON]:
    """Coverage uses all attempted cases, not just schema-valid probability outputs."""
    if not denominator:
        return []
    if len(confidences) != len(correct) or denominator < len(confidences):
        raise ContractError("Risk-coverage requires paired arrays and the full attempted denominator")
    points = []
    for threshold in sorted(set(confidences), reverse=True):
        selected = [index for index, confidence in enumerate(confidences) if confidence >= threshold]
        points.append({
            "threshold": threshold, "coverage": len(selected) / denominator,
            "risk": mean(not correct[index] for index in selected),
            "selected": len(selected), "attempted_denominator": denominator,
        })
    return points


def choose_threshold(rows: list[JSON], *, max_false_allow_rate: float = 0.01) -> JSON:
    """Fit only on calibration rows; no viable automatic gate explicitly abstains."""
    if any(row.get("split") != "calibration" for row in rows):
        raise ContractError("Threshold selection cannot inspect locked test rows")
    valid = [row for row in rows if row.get("schema_valid") and row.get("gold") is not None
             and row.get("answer", {}).get("probabilities") is not None]
    candidates = sorted({row["answer"]["probabilities"]["true"] for row in valid}, reverse=True)
    best = None
    for threshold in candidates:
        result = gate_metrics([row["gold"] for row in valid],
                              [row["answer"]["probabilities"]["true"] for row in valid], threshold=threshold)
        if result["unsafe_denominator"] and result["false_allow_rate"] <= max_false_allow_rate:
            if best is None or result["auto_allow_coverage"] > best["auto_allow_coverage"]:
                best = result
    if best is None:
        return {"threshold": None, "automatic_allow": False, "calibration_cases": len(valid),
                "calibration_attempted_cases": len(rows),
                "reason": "No empirically viable threshold; abstain. Not a formal population safety guarantee."}
    return {"threshold": best["threshold"], "automatic_allow": True, "calibration_cases": len(valid),
            "calibration_attempted_cases": len(rows),
            "calibration_false_allow_rate": best["false_allow_rate"],
            "reason": "Empirical calibration constraint only; finite-sample uncertainty remains."}


def _costs(rows: list[JSON]) -> JSON:
    calls = {call["call_id"]: call for row in rows for call in row.get("calls", [])}
    estimated = sum((Decimal(call["usage_estimated_usd"]) for call in calls.values()), Decimal(0))
    unknown = sum((Decimal(call["unknown_cost_upper_usd"]) for call in calls.values()), Decimal(0))
    accepted = sum(row.get("accepted") is True for row in rows)
    return {
        "usage_estimated_usd": str(estimated), "unknown_cost_upper_usd": str(unknown),
        "invoice_settled_usd": None,
        "cost_per_accepted_task_upper_usd": str((estimated + unknown) / accepted) if accepted else None,
        "cost_estimator": "Reported usage at verified rates (conservative when breakdown missing); "
                          "unknown failed processing held at reserved upper bound, not invoice settlement",
    }


def summarize(rows: list[JSON], *, labels: tuple[object, ...] = (), gate_threshold: float = 0.5) -> JSON:
    """Report logical-task, attempt, schema and acceptance denominators independently."""
    known_gold = [row for row in rows if row.get("gold") is not None]
    correct_gold = sum(row.get("accepted") is True for row in known_gold)
    calls = {call["call_id"]: call for row in rows for call in row.get("calls", [])}
    attempts = [attempt for call in calls.values() for attempt in call["attempts"]]
    # Older attempt records predate the pre-send authentication guard.
    http_attempts = [attempt for attempt in attempts if attempt.get("http_attempted", True)]
    schema_rows = [row for row in rows if row.get("schema_valid")]
    result: JSON = {
        "logical_tasks_started": len(rows), "api_attempts": len(http_attempts),
        "authentication_blocked_attempts": sum(
            attempt.get("error_code") == "authentication-refresh" for attempt in attempts),
        "http_success_attempts": sum(attempt.get("http_status") == 200 for attempt in http_attempts),
        "usable_api_calls": sum(call["usable"] for call in calls.values()),
        "schema_valid_tasks": len(schema_rows),
        "schema_valid_rate": ratio(len(schema_rows), len(rows)),
        "accepted_tasks": sum(row.get("accepted") is True for row in rows),
        "acceptance_rate": ratio(sum(row.get("accepted") is True for row in rows), len(rows)),
        "known_gold_denominator": len(known_gold), "unknown_gold_tasks": len(rows) - len(known_gold),
        "accuracy_all_known_gold_including_failures": ratio(correct_gold, len(known_gold)),
        "template_clusters": len({row["cluster_id"] for row in rows}),
        "base_cases": len({row["base_case_id"] for row in rows}),
        "failures": dict(Counter(call["error_code"] for call in calls.values() if not call["usable"])),
        "escalation_rate": ratio(sum(row.get("escalated") is True for row in rows), len(rows)),
        "policy_only_tasks": sum(row.get("policy_only") is True for row in rows),
        "latency_total_with_retries": latency([row["latency_ms"] for row in rows],
                                             len({row["base_case_id"] for row in rows})),
        "latency_usable_tasks": latency([row["latency_ms"] for row in schema_rows],
                                        len({row["base_case_id"] for row in schema_rows})),
        "single_successful_attempt_latency": latency(
            [attempt["elapsed_ms"] for attempt in attempts if attempt["usable"]],
            len({row["base_case_id"] for row in schema_rows})),
        "network_successful_attempt_latency": latency(
            [attempt["network_elapsed_ms"] for attempt in attempts
             if attempt["usable"] and "network_elapsed_ms" in attempt],
            len({row["base_case_id"] for row in schema_rows})),
        "strands_server_reported_latency": latency(
            [attempt["server_latency_ms"] for attempt in attempts
             if attempt["usable"] and "server_latency_ms" in attempt],
            len({row["base_case_id"] for row in schema_rows})),
        "client_rate_wait_ms": sum(attempt.get("client_rate_wait_ms", 0) for attempt in attempts),
        **_costs(rows),
    }
    if labels and known_gold:
        predictions = [row["answer"]["value"] if row.get("schema_valid") else "__failure__"
                       for row in known_gold]
        gold = [row["gold"] for row in known_gold]
        result.update({"macro_f1": macro_f1(gold, predictions, labels),
                       "confusion_matrix": confusion(gold, predictions)})
    probabilities = [row for row in known_gold if row.get("schema_valid")
                     and row.get("answer", {}).get("probabilities") is not None]
    result["calibration_denominator"] = len(probabilities)
    result["probability_output_coverage"] = ratio(len(probabilities), len(rows))
    result.update({"brier_multiclass_sum": None, "nll": None, "ece_10_bins": None, "risk_coverage": []})
    if probabilities:
        kind = probabilities[0]["answer"]["type"]
        distributions = [row["answer"]["probabilities"] for row in probabilities]
        gold = [("true" if row["gold"] else "false") if kind == "noul" else str(row["gold"])
                for row in probabilities]
        predicted_classes = [
            row["answer"]["value"] if kind == "choice" else
            ("true" if distribution["true"] >= 0.5 else "false") if kind == "noul" else
            max(distribution, key=distribution.get)
            for row, distribution in zip(probabilities, distributions)
        ]
        correctness = [predicted == expected for predicted, expected in zip(predicted_classes, gold)]
        top = [max(item.values()) for item in distributions]
        result.update({"brier_multiclass_sum": brier(gold, distributions), **nll(gold, distributions),
                       "ece_10_bins": ece(top, correctness),
                       "risk_coverage": risk_coverage(
                           top, [row.get("accepted") is True for row in probabilities], len(rows)
                       ),
                       "ece_definition": "Choice selected class; Noul p>=0.5 class; Score modal level, not MAE acceptance",
                       "risk_definition": "Machine acceptance risk selected by top-class probability; not a safety guarantee"})
        if kind == "noul":
            result["gate"] = gate_metrics([row["gold"] for row in probabilities],
                                           [item["true"] for item in distributions], threshold=gate_threshold)
        if kind == "score":
            values = [row["answer"]["value"] for row in probabilities]
            gold_scores = [row["gold"] for row in probabilities]
            result.update({"score_mae": mean(abs(a - g) for a, g in zip(values, gold_scores)),
                           "score_spearman": spearman(values, gold_scores)})
    score_rows = [row for row in known_gold if row.get("schema_valid")
                  and row.get("answer", {}).get("type") == "score"]
    if score_rows:
        result["score_mae_all_valid"] = mean(abs(row["answer"]["value"] - row["gold"]) for row in score_rows)
        result["score_spearman_all_valid"] = spearman(
            [row["answer"]["value"] for row in score_rows], [row["gold"] for row in score_rows])
    gate_rows = [row for row in known_gold if row.get("task") == "gating"]
    if gate_rows:
        allowed = []
        for row in gate_rows:
            answer = row.get("answer") if row.get("schema_valid") else None
            if answer is None:
                allowed.append(False)
            elif type(answer["value"]) is bool:
                allowed.append(answer["value"])
            else:
                allowed.append(gate_threshold is not None and answer["value"] >= gate_threshold)
        result["gate_policy_all_known_gold"] = {
            "known_gold_cases": len(gate_rows), "invalid_tasks_abstain": sum(
                not row.get("schema_valid") for row in gate_rows
            ),
            **gate_policy([row["gold"] for row in gate_rows], allowed),
        }
    regrets = [row["route_quality_regret"] for row in rows if row.get("route_quality_regret") is not None]
    cost_regrets = [Decimal(row["route_cost_regret_usd"]) for row in rows
                    if row.get("route_cost_regret_usd") is not None]
    if any(row.get("selection_kind") == "model" for row in rows):
        result.update({"route_quality_regret_cases": len(regrets),
                       "route_quality_regret": mean(regrets) if regrets else None,
                       "route_cost_regret_cases": len(cost_regrets),
                       "route_cost_regret_mean_usd": str(sum(cost_regrets) / len(cost_regrets)) if cost_regrets else None})
    tool_rows = [row for row in rows if row.get("selection_kind") == "tool"]
    if tool_rows:
        result.update({"tool_cases": len(tool_rows),
                       "tool_applicability_rate_including_failures": ratio(sum(
                           row.get("tool_applicable_and_correct") is True for row in tool_rows
                       ), len(tool_rows)),
                       "tool_permission_denied_predictions": sum(
                           row.get("tool_permission_denied") is True for row in tool_rows
                       )})
    return result


def paired_cluster_ci(candidate: list[JSON], baseline: list[JSON], *, seed: int = 20261010,
                      iterations: int = 2000, margin: float = 0.02) -> JSON:
    """Paired acceptance differences with template resampling, including failed jobs."""
    left = {(row["case_id"], row.get("repeat", 0)): row for row in candidate}
    right = {(row["case_id"], row.get("repeat", 0)): row for row in baseline}
    if len(left) != len(candidate) or len(right) != len(baseline):
        raise ContractError("Paired comparison contains duplicate case/repeat keys")
    common = sorted(set(left) & set(right))
    groups: dict[str, list[float]] = defaultdict(list)
    paired_latency = []
    base_cases = set()
    for key in common:
        a, b = left[key], right[key]
        groups[a["cluster_id"]].append(float(a.get("accepted") is True) - float(b.get("accepted") is True))
        base_cases.add(a["base_case_id"])
        if a.get("schema_valid") and b.get("schema_valid"):
            paired_latency.append(a["latency_ms"] - b["latency_ms"])
    keys = sorted(groups)
    if not keys:
        return {"paired_rows": 0, "status": "inconclusive", "acceptance_difference": None,
                "ci_95": None, "quality_gate_passed": False}
    rng = random.Random(seed)
    draws = []
    for _ in range(iterations):
        sampled = [value for key in rng.choices(keys, k=len(keys)) for value in groups[key]]
        draws.append(mean(sampled))
    interval = [quantile(draws, 0.025), quantile(draws, 0.975)]
    enough = len(keys) >= 30 and len(base_cases) >= 200 and len(left) == len(right) == len(common)
    passed = enough and interval[0] >= -margin
    return {
        "paired_rows": len(common), "unpaired_candidate": len(left) - len(common),
        "unpaired_baseline": len(right) - len(common), "template_clusters": len(keys),
        "independent_base_cases": len(base_cases),
        "acceptance_difference": mean(value for values in groups.values() for value in values),
        "ci_95": interval, "bootstrap_iterations": iterations, "bootstrap_seed": seed,
        "noninferiority_margin": margin, "quality_gate_passed": passed,
        "status": "noninferior-for-machine-acceptance" if passed else "inconclusive",
        "paired_usable_latency_difference_mean_ms": mean(paired_latency) if paired_latency else None,
        "paired_usable_latency_rows": len(paired_latency),
        "speed_cost_claim_allowed": False,
        "note": "No superiority claim without all frozen quality gates, language/task strata and sufficient evidence. "
                "Latency pairing excludes failed jobs and is not the quality denominator.",
    }


def grouped_report(rows: list[JSON], cases_by_id: dict[str, JSON]) -> JSON:
    """Separate suite/task/language/arm modes so probability and label outputs cannot mix."""
    grouped: dict[tuple[str, str, str, str, str], list[JSON]] = defaultdict(list)
    for row in rows:
        if row.get("execution") != "live-api":
            raise ContractError("Live result analysis rejects offline/mock/replay records")
        grouped[row["suite"], row["task"], row["language"], row["arm"],
                row.get("selection_kind") or "main"].append(row)
    summaries = []
    for key, subset in sorted(grouped.items()):
        labels: tuple[object, ...] = ()
        if key[0] == "decision" and key[1] in ("classification", "selection"):
            labels = tuple(cases_by_id[subset[0]["case_id"]]["question"]["criteria"])
        threshold = subset[0].get("gate_threshold")
        summary = summarize(subset, labels=labels, gate_threshold=threshold if threshold is not None else 1.01)
        summaries.append({"suite": key[0], "task": key[1], "language": key[2],
                          "arm": key[3], "subtask": key[4], **summary})
    return {"schema_version": 1, "execution": "analysis-of-live-api-records",
            "rows": len(rows), "summaries": summaries}
