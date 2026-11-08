#!/usr/bin/env python3
"""
Unit tests for harness_architecture_verifier.py
Verifies exact source provenance counts, context dilution math, PTC allowance rules,
8-layer architectural scores, and 12 SA evaluation scenarios.
"""

import unittest
from harness_architecture_verifier import (
    EIGHT_LAYER_MATRIX,
    FRAMEWORK_PROVENANCE,
    SCENARIO_EVAL_MATRIX,
    build_full_verification_report,
    simulate_context_attention_and_kv_cache,
    simulate_tool_execution_modes,
)


class TestHarnessArchitectureVerifier(unittest.TestCase):
    def test_framework_provenance_seals(self) -> None:
        by_id = {f.framework_id: f for f in FRAMEWORK_PROVENANCE}
        self.assertEqual(len(by_id), 3)

        dsh = by_id["deepseek-dsh"]
        self.assertEqual(dsh.verified_commit_sha, "fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159")
        self.assertEqual(dsh.key_counts["package_json_manifests"], 411)
        self.assertEqual(dsh.key_counts["top_package_namespaces"], 49)
        self.assertEqual(dsh.key_counts["composition_bundles"], 6)
        self.assertEqual(dsh.key_counts["subagent_providers"], 7)
        self.assertEqual(dsh.key_counts["ptc_default_2min_allowance"], 2048)

        cc = by_id["claude-code"]
        self.assertEqual(cc.verified_commit_sha, "0ed94698aa0aeee471465fc9c867c2e8434c4d68")
        self.assertEqual(cc.key_counts["sdk_core_message_types"], 5)
        self.assertEqual(cc.key_counts["permission_modes"], 6)
        self.assertEqual(cc.key_counts["effort_levels"], 5)

        hve = by_id["microsoft-hve"]
        self.assertEqual(hve.verified_commit_sha, "f425e943bf228052a23e6bc4810b5faef030314f")
        self.assertEqual(hve.key_counts["custom_agents"], 69)
        self.assertEqual(hve.key_counts["instruction_files"], 43)
        self.assertEqual(hve.key_counts["executable_skills"], 93)
        self.assertEqual(hve.key_counts["collection_manifests"], 14)

    def test_context_attention_math(self) -> None:
        sim = simulate_context_attention_and_kv_cache()
        self.assertEqual(sim["hve_doc_anchor_10k_pct"], 30.0)
        self.assertEqual(sim["hve_doc_anchor_200k_pct"], 1.5)
        self.assertEqual(sim["attention_dilution_factor_10k_to_200k"], 20.0)
        self.assertEqual(sim["hve_200k_recovered_system_share_pct"], 15.0)
        self.assertGreater(sim["dsh_in_history_kv_cache_hit_pct"], 90.0)

    def test_tool_execution_ptc_allowance_and_speedup(self) -> None:
        sim = simulate_tool_execution_modes()
        self.assertEqual(sim["ptc_default_call_allowance"], 2048)
        self.assertEqual(sim["ptc_max_call_allowance"], 10240)
        for tier in sim["tiers"]:
            self.assertGreater(tier["serial_ms"], tier["native_parallel_ms"])
            self.assertGreater(tier["native_parallel_ms"], tier["ptc_run_code_ms"])
            self.assertGreater(tier["ptc_speedup_vs_native_x"], 1.2)

    def test_eight_layer_matrix_and_scenarios(self) -> None:
        self.assertEqual(len(EIGHT_LAYER_MATRIX), 8)
        self.assertEqual(len(SCENARIO_EVAL_MATRIX), 12)
        report = build_full_verification_report()
        self.assertEqual(report["scenario_evaluation"]["passed_positive_scenarios"], 11)
        self.assertEqual(report["scenario_evaluation"]["intentional_antipattern_rejections"], 1)
        self.assertEqual(report["scenario_evaluation"]["max_option_reversal_drift_pts"], 0.0)


if __name__ == "__main__":
    unittest.main()
