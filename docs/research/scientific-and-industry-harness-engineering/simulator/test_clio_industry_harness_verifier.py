#!/usr/bin/env python3
"""Unit tests for clio_industry_harness_verifier.py."""

import unittest
from pathlib import Path
from clio_industry_harness_verifier import (
    verify_hle_biomed_summary,
    ALE_BENCHMARKS,
    AORFB_MOLECULES,
    BLACK_GREY_BENCHMARK_TABLE_S4,
    evaluate_tool_epistemic_state,
    evaluate_uncertainty_trajectory,
    evaluate_discovery_validator_gate,
    compute_pmo_composite_fitness,
    write_artifacts,
)


class TestClioIndustryHarnessVerifier(unittest.TestCase):
    def test_hle_biomed_metrics(self):
        summary = verify_hle_biomed_summary()
        self.assertEqual(summary["total_questions"], 152)
        self.assertEqual(summary["gpt41_base_correct"], 13)
        self.assertAlmostEqual(summary["gpt41_base_pct"], 8.55, places=2)
        self.assertEqual(summary["o3_high_correct"], 21)
        self.assertAlmostEqual(summary["o3_high_pct"], 13.81, places=2)
        self.assertEqual(summary["gpt41_clio_reported_correct"], 34)
        self.assertAlmostEqual(summary["gpt41_clio_pct"], 22.37, places=2)
        self.assertAlmostEqual(summary["net_gain_vs_gpt41_pts"], 13.82, places=2)
        self.assertAlmostEqual(summary["relative_gain_vs_gpt41_pct"], 161.64, places=2)
        self.assertAlmostEqual(
            summary["ablation_loop_recursion_gain_pts"] + summary["ablation_graph_drift_gain_pts"],
            13.82,
            places=2,
        )

    def test_ale_domain_scores(self):
        phys, health, life = ALE_BENCHMARKS
        self.assertAlmostEqual(phys.discovery_clio_pct - phys.competitor_pct, 8.6, places=1)
        self.assertAlmostEqual(phys.delta_vs_single_model_codex_pts, 18.3, places=1)
        self.assertAlmostEqual(health.discovery_clio_pct - health.competitor_pct, 4.4, places=1)
        self.assertAlmostEqual(life.discovery_clio_pct - life.competitor_pct, 3.8, places=1)

    def test_aorfb_closed_loop_and_exllm_trap(self):
        by_id = {m.compound_id: m for m in AORFB_MOLECULES}
        c1, c3, c20 = by_id["1"], by_id["3"], by_id["20"]
        # Compound 3 achieved ~130 mV (133 mV exact) more negative E_red than 1
        shift_c3_mv = round((c1.e_red_meas_v_she - c3.e_red_meas_v_she) * 1000)
        self.assertEqual(shift_c3_mv, 133)
        # Compound 20 retained ~90 mV (92 mV exact) improvement while more than doubling |i_ox/i_red|
        shift_c20_mv = round((c1.e_red_meas_v_she - c20.e_red_meas_v_she) * 1000)
        self.assertEqual(shift_c20_mv, 92)
        self.assertGreater(c20.peak_current_ratio_iox_ired, c3.peak_current_ratio_iox_ired * 2.0)
        # ExLLM candidates S1-S3 all failed solubility in 1 M KOH (<1 mM) vs CLIO >50 mM
        for ex_id in ("S1", "S2", "S3"):
            self.assertEqual(by_id[ex_id].solubility_koh_meas_mm, "<1")
        self.assertGreater(c3.solubility_koh_numeric_mm, 50.0)
        self.assertGreater(c20.solubility_koh_numeric_mm, 50.0)

    def test_calibrated_deference_state_machine(self):
        r1 = evaluate_tool_epistemic_state(-1.998, 0.700, True, 1)
        r2 = evaluate_tool_epistemic_state(-1.998, 0.700, True, 2)
        r3 = evaluate_tool_epistemic_state(-1.998, 0.700, True, 3)
        self.assertEqual(r1["trust_state"], "UNCRITICAL_ACCEPTANCE")
        self.assertTrue(r1["use_in_hard_gate"])
        self.assertAlmostEqual(r2["discrepancy_v"], 2.698, places=3)
        self.assertEqual(r2["trust_state"], "RANK_ORDER_SALVAGE")
        self.assertFalse(r2["use_in_hard_gate"])
        self.assertTrue(r2["use_for_ranking"])
        self.assertEqual(r3["trust_state"], "GATE_EXCLUDED_CALIBRATION_FIRST")

    def test_uncertainty_gradient_and_validator_gate(self):
        conv = evaluate_uncertainty_trajectory([0.62, 0.48, 0.35, 0.24, 0.16])
        osc = evaluate_uncertainty_trajectory([0.38, 0.72, 0.41, 0.81, 0.52, 0.86])
        self.assertLess(conv["gradient_du_dt"], 0)
        self.assertEqual(conv["action"], "Act automatically")
        self.assertGreater(osc["gradient_du_dt"], 0)
        self.assertEqual(osc["action"], "Send to a human")

        gate_retry = evaluate_discovery_validator_gate(2, 3, 2)
        gate_escalate = evaluate_discovery_validator_gate(2, 3, 3)
        self.assertEqual(gate_retry["status"], "Incomplete")
        self.assertTrue(gate_retry["retry_allowed"])
        self.assertEqual(gate_escalate["status"], "Needs User Attention")
        self.assertFalse(gate_escalate["retry_allowed"])

    def test_pmo_greybox_gain_and_artifact_export(self):
        rows = {(r.condition, r.algorithm): r for r in BLACK_GREY_BENCHMARK_TABLE_S4}
        clio_bb = rows[("Black-box", "CLIO")]
        clio_gb = rows[("Grey-box", "CLIO")]
        ex_gb = rows[("Grey-box", "ExLLM")]
        self.assertGreater(clio_gb.top10_mean, ex_gb.top10_mean)
        rel_gain_top10 = (clio_gb.top10_mean - clio_bb.top10_mean) / clio_bb.top10_mean
        self.assertGreater(rel_gain_top10, 0.14)

        fit = compute_pmo_composite_fitness(log_s=-1.0, e_red=-1.0, sa_score=2.5, tanimoto_sim=0.5, smarts_clean=True)
        self.assertGreater(fit["composite_F"], 0.8)
        fit_bad = compute_pmo_composite_fitness(log_s=-1.0, e_red=-1.0, sa_score=2.5, tanimoto_sim=0.5, smarts_clean=False)
        self.assertEqual(fit_bad["composite_F"], -10.0)

        base_dir = Path(__file__).resolve().parent.parent
        payload = write_artifacts(base_dir)
        self.assertTrue((base_dir / "report.json").exists())
        self.assertEqual(len(payload["evaluation_matrix_12"]), 12)


if __name__ == "__main__":
    unittest.main()
