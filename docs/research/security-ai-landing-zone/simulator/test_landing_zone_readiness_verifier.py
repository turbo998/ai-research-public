#!/usr/bin/env python3
"""Unit tests for the Secure AI Landing Zone & Frontier SOC Readiness Verifier."""

import unittest
from landing_zone_readiness_verifier import (
    DECK_METADATA,
    DISCOVERY_OPENER_QUESTIONS,
    LANDING_ZONE_CONTROLS,
    PRE_SCALE_QUESTIONS,
    QUALIFYING_AGENT365_LICENSES,
    UNIFIED_SECURITY_GRAPH_TABLES,
    evaluate_landing_zone_readiness,
)


class TestLandingZoneReadinessVerifier(unittest.TestCase):
    def test_deck_metadata_and_question_counts(self) -> None:
        self.assertEqual(DECK_METADATA["total_slides"], 42)
        self.assertEqual(DECK_METADATA["file_size_bytes"], 15233523)
        self.assertEqual(len(PRE_SCALE_QUESTIONS), 6)
        self.assertEqual(len(DISCOVERY_OPENER_QUESTIONS), 5)
        self.assertEqual(len(LANDING_ZONE_CONTROLS), 20)
        self.assertEqual(len(UNIFIED_SECURITY_GRAPH_TABLES), 22)

    def test_frontier_soc_and_mdash_metrics(self) -> None:
        kpis = DECK_METADATA["frontier_soc_kpis"]
        self.assertEqual(kpis["reduced_exposures"]["value"], 847)
        self.assertEqual(kpis["active_investigations"]["value"], 41)
        self.assertEqual(kpis["enriched_indicators"]["value"], 124)
        self.assertEqual(kpis["disrupted_attacks"]["value"], 23)
        self.assertEqual(DECK_METADATA["mdash_metrics"]["specialized_agents_min"], 100)
        self.assertEqual(DECK_METADATA["ai_threat_case_study"]["ai_generated_loc"], 17000)
        self.assertEqual(DECK_METADATA["ai_threat_case_study"]["ai_generated_modules"], 49)

    def test_e7_frontier_suite_full_landing_zone_passes_week3_gate(self) -> None:
        all_ids = [c.control_id for c in LANDING_ZONE_CONTROLS]
        res = evaluate_landing_zone_readiness(
            scenario_id="S1-E7-FULL",
            license_bundle="M365_E7_Frontier_Suite",
            copilot_as_ui_unified=True,
            completed_control_ids=all_ids,
        )
        self.assertTrue(res.agent365_prerequisite_met)
        self.assertTrue(res.e7_frontier_suite_active)
        self.assertEqual(res.overall_readiness_pct, 100.0)
        self.assertEqual(res.pre_scale_questions_answered, 6)
        self.assertTrue(res.week3_fte_gate_passed)
        self.assertTrue(res.week4_5_agent_launch_allowed)
        self.assertEqual(res.action_gate, "Act automatically")

    def test_unbuilt_landing_zone_blocks_week4_5_agent_launch(self) -> None:
        # Slide 5 Hard Rule: Without Week 3 Landing Zone, Week 4-5 Agents cannot go to production
        partial_ids = [c.control_id for c in LANDING_ZONE_CONTROLS if c.pillar_id in ("P1_VISIBILITY_GOVERNANCE", "P2_IDENTITY_ACCESS")]
        res = evaluate_landing_zone_readiness(
            scenario_id="S2-PARTIAL-LZ",
            license_bundle="M365_E5",
            copilot_as_ui_unified=True,
            completed_control_ids=partial_ids,
            discovery_unsure_ids=["D2", "D4"],
        )
        self.assertEqual(res.overall_readiness_pct, 40.0)
        self.assertFalse(res.week3_fte_gate_passed)
        self.assertFalse(res.week4_5_agent_launch_allowed)
        self.assertTrue(res.discovery_assessment_triggered)
        self.assertEqual(res.action_gate, "Send to a human")

    def test_fragmented_ui_shadow_ai_blocks_week3_gate_even_with_all_controls(self) -> None:
        # Slide 6: Fragmented entry = Shadow AI
        all_ids = [c.control_id for c in LANDING_ZONE_CONTROLS]
        res = evaluate_landing_zone_readiness(
            scenario_id="S3-FRAGMENTED-UI",
            license_bundle="M365_E7_Frontier_Suite",
            copilot_as_ui_unified=False,
            completed_control_ids=all_ids,
        )
        self.assertFalse(res.week3_fte_gate_passed)
        self.assertFalse(res.week4_5_agent_launch_allowed)
        self.assertTrue(any("SHADOW_AI_BLOCK" in r for r in res.blocking_reasons))

    def test_missing_agent365_prerequisite_license_blocks_deployment(self) -> None:
        # Slide 23: Customer must hold E5/A5/Business Premium or Defender+Purview Suite
        all_ids = [c.control_id for c in LANDING_ZONE_CONTROLS]
        res = evaluate_landing_zone_readiness(
            scenario_id="S4-NO-PREREQ-LICENSE",
            license_bundle="M365_Business_Standard_Only",
            copilot_as_ui_unified=True,
            completed_control_ids=all_ids,
        )
        self.assertFalse(res.agent365_prerequisite_met)
        self.assertFalse(res.week3_fte_gate_passed)
        self.assertEqual(res.action_gate, "Send to a human")
        self.assertIn("M365_Business_Premium", QUALIFYING_AGENT365_LICENSES)


if __name__ == "__main__":
    unittest.main()
