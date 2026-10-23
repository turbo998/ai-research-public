"""Unit tests for sky001_and_19model_verifier.py."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from sky001_and_19model_verifier import (
    NINETEEN_MODELS,
    SKYFALL_SHOWCASE_ASSEMBLIES,
    audit_sky001_benchmarks,
    build_cross_modality_matrix,
    classify_coding_model_action,
    compute_critical_path,
    compute_pareto_frontier,
    export_summary_json,
)


def test_sky001_critical_path_arithmetic() -> None:
    results = {a.key: compute_critical_path(a, steps_per_part=100, parallel_workers=128) for a in SKYFALL_SHOWCASE_ASSEMBLIES}
    jaguar = results["jaguar"]
    assert jaguar.internal_nodes == 36
    assert jaguar.flat_sequential_steps == 10336
    assert jaguar.hierarchical_sequential_steps == 105
    assert jaguar.critical_path_speedup == 98.44

    jet = results["jet"]
    assert jet.flat_sequential_steps == 7026
    assert jet.hierarchical_sequential_steps == 105
    assert jet.critical_path_speedup == 66.91

    arcmate = results["arcmate"]
    assert arcmate.flat_sequential_steps == 3520
    assert arcmate.hierarchical_sequential_steps == 104
    assert arcmate.critical_path_speedup == 33.85

    tractor = results["tractor"]
    assert tractor.flat_sequential_steps == 9238
    assert tractor.hierarchical_sequential_steps == 105
    assert tractor.critical_path_speedup == 87.98


def test_sky001_serial_worker_degenerates_to_flat_work() -> None:
    jaguar_serial = compute_critical_path(SKYFALL_SHOWCASE_ASSEMBLIES[0], steps_per_part=100, parallel_workers=1)
    assert jaguar_serial.hierarchical_batches == 103
    assert jaguar_serial.hierarchical_sequential_steps == 5 + 103 * 100
    assert jaguar_serial.critical_path_speedup == 1.0


def test_sky001_dual_source_benchmark_audit() -> None:
    audit = audit_sky001_benchmarks()
    assert audit["cad"]["sky001_iou_pct"] == 79.7
    assert audit["cad"]["astra_iou_pct"] == 79.1
    assert audit["cad"]["iou_lead_vs_astra_pts"] == 0.6
    assert audit["cad"]["speedup_vs_astra_x"] == 51.0
    assert audit["cad"]["cost_ratio_vs_astra_x"] == 150.0
    assert audit["cad"]["models_only_in_blog"] == ["Gemini 4"]
    assert audit["cad"]["models_only_in_landing"] == ["Gemini 3.8 Flash", "Opus 5.5"]

    assert audit["bim"]["sky001_iou_pct"] == 43.6
    assert audit["bim"]["next_best_model"] == "Gemini 3.8 Flash"
    assert audit["bim"]["iou_lead_vs_next_best_pts"] == 1.3
    assert audit["bim"]["iou_lead_vs_astra_pts"] == 3.0
    assert audit["bim"]["speedup_vs_astra_blog_x"] == 118.5
    assert audit["bim"]["cost_ratio_vs_astra_blog_x"] == 185.8
    assert audit["bim"]["cost_ratio_vs_astra_landing_x"] == 188.4
    assert audit["bim"]["models_only_in_landing"] == ["Opus 5.5"]


def test_19_model_supplement_5_entrants_and_totals() -> None:
    assert len(NINETEEN_MODELS) == 19
    by_slug = {m.slug: m for m in NINETEEN_MODELS}

    haiku55 = by_slug["claude-haiku-5.5"]
    assert haiku55.total_mean == 99.24
    assert haiku55.atomic_mean == 99.15
    assert haiku55.medium_mean == 99.50
    assert haiku55.complex_mean == 99.22
    assert haiku55.hidden_passed == 1308
    assert haiku55.hidden_total == 1310
    assert haiku55.cost_usd == 0.33
    assert haiku55.total_rounds == 94
    assert haiku55.output_tokens == 453116
    assert classify_coding_model_action(haiku55) == "Confirm"

    argon = by_slug["gemini-4-argon"]
    assert argon.total_mean == 98.59
    assert argon.atomic_mean == 99.00
    assert argon.medium_mean == 98.62
    assert argon.complex_mean == 98.06
    assert argon.hidden_passed == 1310
    assert argon.hidden_total == 1310
    assert argon.cost_usd == 2.82
    assert argon.total_rounds == 106
    assert argon.output_tokens == 116755
    assert classify_coding_model_action(argon) == "Act automatically"


def test_19_model_gating_and_pareto_frontier() -> None:
    actions = [classify_coding_model_action(m) for m in NINETEEN_MODELS]
    assert actions.count("Act automatically") == 9
    assert actions.count("Confirm") == 8
    assert actions.count("Send to a human") == 2

    frontier = compute_pareto_frontier()
    for expected in ("Fable 5.1", "Opus 5.5", "Haiku 5.5", "Sonnet 5.5", "GPT-6.1 Sol", "GPT-6 Luna"):
        assert expected in frontier


def test_cross_modality_matrix_and_export(tmp_path: Path | None = None) -> None:
    matrix = build_cross_modality_matrix()
    assert len(matrix) == 6
    astra = next(r for r in matrix if r["coding_model"] == "GPT-6 Astra")
    assert astra["coding_mean_score"] == 98.82
    assert astra["sky_cad_iou_pct"] == 79.1

    if tmp_path is None:
        with tempfile.TemporaryDirectory() as td:
            out_path = Path(td) / "verifier-summary.json"
            payload = export_summary_json(out_path)
            assert out_path.exists()
            assert payload["coding_19_total_runs"] == 209
    else:
        out_path = tmp_path / "verifier-summary.json"
        payload = export_summary_json(out_path)
        assert out_path.exists()
        assert payload["coding_19_total_runs"] == 209


class VerifierTestCase(unittest.TestCase):
    def test_all(self) -> None:
        test_sky001_critical_path_arithmetic()
        test_sky001_serial_worker_degenerates_to_flat_work()
        test_sky001_dual_source_benchmark_audit()
        test_19_model_supplement_5_entrants_and_totals()
        test_19_model_gating_and_pareto_frontier()
        test_cross_modality_matrix_and_export()


if __name__ == "__main__":
    unittest.main(verbosity=2)
