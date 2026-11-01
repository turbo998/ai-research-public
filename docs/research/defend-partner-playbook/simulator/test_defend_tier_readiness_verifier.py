"""Unit tests for the DEFEND Partner Playbook deterministic tier-readiness & gating verifier."""

from __future__ import annotations

import unittest

from defend_tier_readiness_verifier import (
    ALL_CAPABILITY_ROWS,
    DEFENDER_CAPABILITY_MATRIX,
    EXIT_CRITERIA,
    PLAYBOOK_METADATA,
    PURVIEW_CAPABILITY_MATRIX,
    SMB_PARTNER_TOOLKIT_CATALOG,
    RiskAcceptanceRecord,
    compute_licensing_coverage_summary,
    evaluate_full_tenant_journey,
)


class TestDefendTierReadinessVerifier(unittest.TestCase):
    def test_slide_and_criteria_counts(self) -> None:
        self.assertEqual(PLAYBOOK_METADATA["total_slides"], 53)
        self.assertEqual(PLAYBOOK_METADATA["total_chapters"], 11)
        self.assertEqual(len(PLAYBOOK_METADATA["zero_trust_dimensions"]), 7)
        self.assertEqual(len(EXIT_CRITERIA), 51)
        by_tier = {}
        for item in EXIT_CRITERIA:
            by_tier[item.tier] = by_tier.get(item.tier, 0) + 1
        self.assertEqual(
            by_tier,
            {
                "DEFENDBase": 11,
                "DEFENDSecurity": 12,
                "DEFENDCompliance": 11,
                "DEFENDComplete": 8,
                "DEFENDExtend": 9,
            },
        )
        atomic = [c for c in EXIT_CRITERIA if not c.is_composite_prerequisite]
        composite = [c for c in EXIT_CRITERIA if c.is_composite_prerequisite]
        self.assertEqual(len(atomic), 48)
        self.assertEqual(len(composite), 3)

    def test_licensing_capability_matrix_counts(self) -> None:
        self.assertEqual(len(DEFENDER_CAPABILITY_MATRIX), 21)
        self.assertEqual(len(PURVIEW_CAPABILITY_MATRIX), 20)
        self.assertEqual(len(ALL_CAPABILITY_ROWS), 41)

        cov = compute_licensing_coverage_summary()
        self.assertEqual(cov["defender_suite_coverage"]["business_standard"]["count"], 2)
        self.assertEqual(cov["defender_suite_coverage"]["business_premium"]["count"], 8)
        self.assertEqual(cov["defender_suite_coverage"]["with_defender_suite"]["count"], 21)
        self.assertEqual(cov["purview_suite_coverage"]["business_standard"]["count"], 3)
        self.assertEqual(cov["purview_suite_coverage"]["business_premium"]["count"], 7)
        self.assertEqual(cov["purview_suite_coverage"]["with_purview_suite"]["count"], 20)

        bundles = cov["tier_bundle_coverage"]
        self.assertEqual(bundles["Business_Standard"]["count"], 5)
        self.assertEqual(bundles["DEFENDBase_Business_Premium"]["count"], 15)
        self.assertEqual(bundles["DEFENDSecurity_BP_plus_Defender"]["count"], 28)
        self.assertEqual(bundles["DEFENDCompliance_BP_plus_Purview"]["count"], 28)
        self.assertEqual(bundles["DEFENDComplete_BP_plus_Both_Suites"]["count"], 41)

    def test_full_implementation_passes_all_tiers_automatically(self) -> None:
        all_atomic = {c.criterion_id for c in EXIT_CRITERIA if not c.is_composite_prerequisite}
        results = evaluate_full_tenant_journey(implemented_ids=all_atomic)
        for tier, res in results.items():
            self.assertTrue(res.governance_rule_passed, f"{tier} should pass")
            self.assertEqual(res.readiness_score_pct, 100.0)
            self.assertEqual(res.action, "Act automatically")

    def test_formal_risk_acceptance_routes_to_confirm(self) -> None:
        # B03 (Legacy auth blocked or formally risk accepted) satisfied via formal risk acceptance
        base_controls = {f"B{i:02d}" for i in range(1, 12) if i != 3}
        ra = {
            "B03": RiskAcceptanceRecord(
                criterion_id="B03",
                compensating_control="IP-restricted SMTP relay with dedicated monitoring",
                accountable_owner="CISO / IT Director",
                review_cadence_days=90,
            )
        }
        results = evaluate_full_tenant_journey(implemented_ids=base_controls, risk_acceptances=ra)
        base_res = results["DEFENDBase"]
        self.assertTrue(base_res.governance_rule_passed)
        self.assertEqual(base_res.implemented_count, 10)
        self.assertEqual(base_res.risk_accepted_count, 1)
        self.assertEqual(base_res.readiness_score_pct, 100.0)
        self.assertEqual(base_res.action, "Confirm")

    def test_premature_sentinel_activation_blocked_by_slide_40_rule(self) -> None:
        # Suppose a tenant deploys all Base, Security, and Extend controls, but skips Compliance (so Complete fails)
        implemented = (
            {f"B{i:02d}" for i in range(1, 12)}
            | {f"S{i:02d}" for i in range(1, 13)}
            | {f"M{i:02d}" for i in range(3, 9)}
            | {f"E{i:02d}" for i in range(2, 10)}
        )
        results = evaluate_full_tenant_journey(implemented_ids=implemented)
        self.assertTrue(results["DEFENDBase"].governance_rule_passed)
        self.assertTrue(results["DEFENDSecurity"].governance_rule_passed)
        self.assertFalse(results["DEFENDCompliance"].governance_rule_passed)
        self.assertFalse(results["DEFENDComplete"].governance_rule_passed)
        self.assertFalse(results["DEFENDExtend"].governance_rule_passed)
        self.assertEqual(results["DEFENDExtend"].action, "Send to a human")
        self.assertTrue(
            any("DEFENDComplete" in reason for reason in results["DEFENDExtend"].blocking_reasons)
        )

    def test_invalid_risk_acceptance_rejected(self) -> None:
        base_controls = {f"B{i:02d}" for i in range(1, 12) if i != 3}
        ra = {
            "B03": RiskAcceptanceRecord(
                criterion_id="B03",
                compensating_control="",  # missing compensating control
                accountable_owner="IT Lead",
                review_cadence_days=180,  # exceeds 90-day quarterly review
            )
        }
        results = evaluate_full_tenant_journey(implemented_ids=base_controls, risk_acceptances=ra)
        self.assertFalse(results["DEFENDBase"].governance_rule_passed)
        self.assertEqual(results["DEFENDBase"].action, "Send to a human")

    def test_smb_partner_toolkit_catalog_counts(self) -> None:
        self.assertEqual(SMB_PARTNER_TOOLKIT_CATALOG["lifecycle_stages_count"], 5)
        self.assertEqual(SMB_PARTNER_TOOLKIT_CATALOG["core_aka_ms_links_count"], 6)
        assets = SMB_PARTNER_TOOLKIT_CATALOG["core_assets"]
        self.assertEqual(len(assets), 6)
        self.assertEqual(assets[0]["pages_total"], 14)
        self.assertEqual(len(assets[0]["industries"]), 7)
        self.assertEqual(assets[2]["modular_workstreams_total"], 22)
        self.assertEqual(
            assets[2]["priority_1_foundation_count"]
            + assets[2]["priority_2_intermediate_count"]
            + assets[2]["priority_3_advanced_and_ai_count"],
            22,
        )
        self.assertEqual(assets[3]["guides_count"], 6)
        self.assertEqual(assets[3]["pages_total"], 360)
        self.assertEqual(sum(g["pages"] for g in assets[3]["guides"]), 360)
        self.assertEqual(assets[4]["workload_toolkits_count"], 4)
        self.assertEqual(assets[4]["entra_report_only_ca_templates_count"], 13)
        labels = SMB_PARTNER_TOOLKIT_CATALOG["defend_aligned_8_label_taxonomy"]
        self.assertEqual(len(labels), 8)
        self.assertEqual(sum(1 for lbl in labels if lbl["lob_exception"]), 2)

    def test_six_workload_technical_guides_coverage(self) -> None:
        guides = SMB_PARTNER_TOOLKIT_CATALOG["core_assets"][3]["guides"]
        workload_pages = {g["workload_id"]: g["pages"] for g in guides}
        self.assertEqual(
            workload_pages,
            {
                "W1": 90,  # Identity & Access Controls + Identity Protection
                "W2": 92,  # Data Security & AI Guardrails
                "W3": 52,  # Email, App & Collaboration Protection
                "W4": 51,  # Device Security
                "W5": 40,  # Device Enrollment & Management
                "W6": 35,  # SaaS Security
            },
        )
        for guide in guides:
            self.assertGreaterEqual(len(guide["core_controls"]), 5)
        labels = SMB_PARTNER_TOOLKIT_CATALOG["defend_aligned_8_label_taxonomy"]
        self.assertEqual([lbl["priority_index"] for lbl in labels], list(range(8)))



if __name__ == "__main__":
    unittest.main()
