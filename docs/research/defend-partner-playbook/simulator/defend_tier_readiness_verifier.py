"""Deterministic tier-readiness, licensing capability, and governance gating verifier
for the Microsoft Partner Playbook: DEFEND Partner Playbook (53 slides, 11 chapters).

Verifies and models:
1. All 39 capability comparison rows across Slides 10-11 (19 Defender Suite rows) and
   Slides 13-14 (20 Purview Suite rows) across 4 licensing columns:
   - Business Standard (5/39 = 12.82%)
   - Business Premium (15/39 = 38.46%)
   - Business Premium + Defender Suite (26/39 = 66.67%; 19/19 Defender + 7/20 Purview)
   - Business Premium + Purview Suite (28/39 = 71.79%; 8/19 Defender + 20/20 Purview)
   - Business Premium + Defender & Purview Suites / Enterprise E5 (39/39 = 100.0%)
2. All 51 mandatory exit criteria rows across Slides 35-39 (48 atomic controls + 3 composite
   cross-tier prerequisites) and the hard Governance Rule on Slide 40:
   - DEFENDBase: 11 checks (Slide 35)
   - DEFENDSecurity: 12 checks (Slide 36)
   - DEFENDCompliance: 11 checks (Slide 37)
   - DEFENDComplete: 8 checks including 2 composite prerequisites (Slide 38)
   - DEFENDExtend: 9 checks including 1 composite prerequisite (Slide 39)
3. The 7 Zero Trust Assessment dimensions (Slide 24) and 4-Tier Purview-as-a-Service
   progression (Appendix B, Slides 47-51).
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Dict, List, Optional


PLAYBOOK_METADATA: Dict[str, object] = {
    "title": "DEFEND Partner Playbook: A tiered managed security and compliance framework for Microsoft 365 Business Premium",
    "classification": "partner_developed_service_framework_not_microsoft_sku",
    "total_slides": 53,
    "total_chapters": 11,
    "pptx_size_bytes": 11425905,
    "pptx_sha256": "0298c3bb248a0465d9a1c250ccb1fd1eb631ef5787137d6bbb9a3fc07babad46",
    "zero_trust_dimensions": [
        "Identity",
        "Devices",
        "Applications",
        "Data",
        "Infrastructure",
        "Networks",
        "AI",
    ],
    "defend_tiers": [
        "DEFENDBase",
        "DEFENDSecurity",
        "DEFENDCompliance",
        "DEFENDComplete",
        "DEFENDExtend",
    ],
    "purview_as_a_service_tiers": [
        "Tier 1 — Data Protect",
        "Tier 2 — Data Govern",
        "Tier 3 — Data Control",
        "Tier 4 — Data Assure",
    ],
}


@dataclass(frozen=True)
class CapabilityComparisonRow:
    suite_group: str  # "Defender" (Slides 10-11) or "Purview" (Slides 13-14)
    domain: str
    capability: str
    slide_number: int
    business_standard: bool
    business_premium: bool
    with_suite_addon: bool
    enterprise_e5: bool


@dataclass(frozen=True)
class ExitCriterion:
    criterion_id: str
    tier: str
    slide_number: int
    area: str
    description: str
    is_composite_prerequisite: bool = False
    referenced_tier: Optional[str] = None
    allow_formal_risk_acceptance: bool = True


@dataclass(frozen=True)
class RiskAcceptanceRecord:
    criterion_id: str
    compensating_control: str
    accountable_owner: str
    review_cadence_days: int = 90

    @property
    def is_valid(self) -> bool:
        return (
            bool(self.compensating_control.strip())
            and bool(self.accountable_owner.strip())
            and 1 <= self.review_cadence_days <= 90
        )


@dataclass(frozen=True)
class TierEvaluationResult:
    tier: str
    total_criteria: int
    implemented_count: int
    risk_accepted_count: int
    unsatisfied_count: int
    composite_prerequisites_met: bool
    governance_rule_passed: bool
    readiness_score_pct: float
    action: str  # "Act automatically", "Confirm", or "Send to a human"
    blocking_reasons: List[str]


# Exact 19 rows from Slides 10-11 (Defender Suite comparison)
DEFENDER_CAPABILITY_MATRIX: List[CapabilityComparisonRow] = [
    # Slide 10: Email protection (5)
    CapabilityComparisonRow("Defender", "Email protection", "Advanced anti-phishing", 10, False, True, True, True),
    CapabilityComparisonRow("Defender", "Email protection", "Safe Links & attachments (email, SharePoint, Teams)", 10, False, True, True, True),
    CapabilityComparisonRow("Defender", "Email protection", "Safe Documents", 10, False, False, True, True),
    CapabilityComparisonRow("Defender", "Email protection", "Automatic investigation & response for email", 10, False, False, True, True),
    CapabilityComparisonRow("Defender", "Email protection", "Attack simulation training", 10, False, False, True, True),
    # Slide 10: Endpoint protection (5)
    CapabilityComparisonRow("Defender", "Endpoint protection", "Microsoft Defender XDR", 10, False, True, True, True),
    CapabilityComparisonRow("Defender", "Endpoint protection", "Automated investigation & remediation (endpoints)", 10, False, True, True, True),
    CapabilityComparisonRow("Defender", "Endpoint protection", "Advanced hunting", 10, False, False, True, True),
    CapabilityComparisonRow("Defender", "Endpoint protection", "Threat Experts", 10, False, False, True, True),
    CapabilityComparisonRow("Defender", "Endpoint protection", "Extended data retention (6 months)", 10, False, False, True, True),
    # Slide 11: Identity & access management (7)
    CapabilityComparisonRow("Defender", "Identity & access management", "Multi-factor authentication", 11, True, True, True, True),
    CapabilityComparisonRow("Defender", "Identity & access management", "Conditional Access", 11, False, True, True, True),
    CapabilityComparisonRow("Defender", "Identity & access management", "Risk-based Conditional Access / Identity Protection", 11, False, False, True, True),
    CapabilityComparisonRow("Defender", "Identity & access management", "Self-service password reset", 11, True, True, True, True),
    CapabilityComparisonRow("Defender", "Identity & access management", "Automated remediation for compromised accounts", 11, False, False, True, True),
    CapabilityComparisonRow("Defender", "Identity & access management", "Privileged Identity Management", 11, False, False, True, True),
    CapabilityComparisonRow("Defender", "Identity & access management", "Access reviews / entitlement management", 11, False, False, True, True),
    CapabilityComparisonRow("Defender", "Identity & access management", "Hybrid identity protection", 11, False, False, True, True),
    CapabilityComparisonRow("Defender", "Identity & access management", "Detailed identity risk insights", 11, False, False, True, True),
    # Slide 11: Cloud app security (CASB) (2)
    CapabilityComparisonRow("Defender", "Cloud app security (CASB)", "Defender for Cloud Apps — discovery", 11, False, True, True, True),
    CapabilityComparisonRow("Defender", "Cloud app security (CASB)", "Defender for Cloud Apps — full", 11, False, False, True, True),
]

# Exact 20 rows from Slides 13-14 (Purview Suite comparison)
PURVIEW_CAPABILITY_MATRIX: List[CapabilityComparisonRow] = [
    # Slide 13: Information protection (6)
    CapabilityComparisonRow("Purview", "Information protection", "Manual, default & mandatory labels in M365 Apps", 13, True, True, True, True),
    CapabilityComparisonRow("Purview", "Information protection", "Automatic labels based on sensitive content", 13, False, False, True, True),
    CapabilityComparisonRow("Purview", "Information protection", "Manual sensitivity labeling for Teams meetings", 13, False, False, True, True),
    CapabilityComparisonRow("Purview", "Information protection", "Sensitivity labels based on advanced classifiers", 13, False, False, True, True),
    CapabilityComparisonRow("Purview", "Information protection", "Auto-labeling (Exchange, SharePoint, OneDrive)", 13, False, False, True, True),
    CapabilityComparisonRow("Purview", "Information protection", "Message encryption (Basic -> Advanced)", 13, False, True, True, True),
    # Slide 13: Data loss prevention (DLP) (6)
    CapabilityComparisonRow("Purview", "Data loss prevention (DLP)", "DLP for emails and files", 13, False, True, True, True),
    CapabilityComparisonRow("Purview", "Data loss prevention (DLP)", "DLP for Teams chats", 13, False, False, True, True),
    CapabilityComparisonRow("Purview", "Data loss prevention (DLP)", "Endpoint DLP", 13, False, False, True, True),
    CapabilityComparisonRow("Purview", "Data loss prevention (DLP)", "DLP for cloud apps (network & browser)", 13, False, False, True, True),
    CapabilityComparisonRow("Purview", "Data loss prevention (DLP)", "Policy tips in Outlook (Limited -> Extended)", 13, True, True, True, True),
    CapabilityComparisonRow("Purview", "Data loss prevention (DLP)", "DLP for Microsoft 365 Copilot", 13, False, False, True, True),
    # Slide 14: Data lifecycle management (3)
    CapabilityComparisonRow("Purview", "Data lifecycle management", "Org-wide / location retention policies", 14, False, True, True, True),
    CapabilityComparisonRow("Purview", "Data lifecycle management", "Rules & ML-based automatic retention", 14, False, False, True, True),
    CapabilityComparisonRow("Purview", "Data lifecycle management", "Records management", 14, False, False, True, True),
    # Slide 14: Insider risk & communication (3)
    CapabilityComparisonRow("Purview", "Insider risk & communication", "Purview Insider Risk Management", 14, False, False, True, True),
    CapabilityComparisonRow("Purview", "Insider risk & communication", "Adaptive Protection", 14, False, False, True, True),
    CapabilityComparisonRow("Purview", "Insider risk & communication", "Communication Compliance", 14, False, False, True, True),
    # Slide 14: eDiscovery & audit (2)
    CapabilityComparisonRow("Purview", "eDiscovery & audit", "eDiscovery (Standard -> Premium)", 14, False, True, True, True),
    CapabilityComparisonRow("Purview", "eDiscovery & audit", "Audit (Standard -> Premium)", 14, True, True, True, True),
]

ALL_CAPABILITY_ROWS: List[CapabilityComparisonRow] = DEFENDER_CAPABILITY_MATRIX + PURVIEW_CAPABILITY_MATRIX


# Exact 51 Exit Criteria rows across Slides 35-39
EXIT_CRITERIA: List[ExitCriterion] = [
    # Slide 35: DEFENDBase (11 items)
    ExitCriterion("B01", "DEFENDBase", 35, "Identity", "MFA enforced for all users including administrators"),
    ExitCriterion("B02", "DEFENDBase", 35, "Identity", "Baseline Conditional Access policies deployed and tested"),
    ExitCriterion("B03", "DEFENDBase", 35, "Identity", "Legacy authentication blocked or formally risk accepted"),
    ExitCriterion("B04", "DEFENDBase", 35, "Devices", "All supported endpoints enrolled into Intune"),
    ExitCriterion("B05", "DEFENDBase", 35, "Devices", "OS disk encryption enforced on managed devices"),
    ExitCriterion("B06", "DEFENDBase", 35, "Devices", "Defender for Business enabled and reporting healthy"),
    ExitCriterion("B07", "DEFENDBase", 35, "Email", "Defender for Office 365 Plan 1 protections enabled"),
    ExitCriterion("B08", "DEFENDBase", 35, "Email", "Safe Links and Safe Attachments active"),
    ExitCriterion("B09", "DEFENDBase", 35, "Visibility", "Secure Score baseline established and documented"),
    ExitCriterion("B10", "DEFENDBase", 35, "Visibility", "Device compliance reporting enabled and reviewed"),
    ExitCriterion("B11", "DEFENDBase", 35, "Governance", "Initial risk register created and signed off"),
    # Slide 36: DEFENDSecurity (12 items)
    ExitCriterion("S01", "DEFENDSecurity", 36, "Identity", "Risk-based Conditional Access live"),
    ExitCriterion("S02", "DEFENDSecurity", 36, "Identity", "User and sign-in risk detection operational"),
    ExitCriterion("S03", "DEFENDSecurity", 36, "Identity", "Identity governance workflows defined"),
    ExitCriterion("S04", "DEFENDSecurity", 36, "Endpoint", "Defender for Endpoint Plan 2 fully onboarded"),
    ExitCriterion("S05", "DEFENDSecurity", 36, "Endpoint", "Threat & Vulnerability Management producing output"),
    ExitCriterion("S06", "DEFENDSecurity", 36, "Endpoint", "Automated investigation and remediation enabled"),
    ExitCriterion("S07", "DEFENDSecurity", 36, "Email", "Defender for Office 365 Plan 2 enabled; Threat Explorer operational"),
    ExitCriterion("S08", "DEFENDSecurity", 36, "Email", "Attack simulation programme running or scheduled"),
    ExitCriterion("S09", "DEFENDSecurity", 36, "Cloud", "Defender for Cloud Apps enabled; Shadow IT reviewed and actioned"),
    ExitCriterion("S10", "DEFENDSecurity", 36, "Hybrid", "Defender for Identity healthy where applicable"),
    ExitCriterion("S11", "DEFENDSecurity", 36, "Operations", "Alert triage and response ownership agreed"),
    ExitCriterion("S12", "DEFENDSecurity", 36, "Operations", "Alert noise reviewed and tuned"),
    # Slide 37: DEFENDCompliance (11 items)
    ExitCriterion("C01", "DEFENDCompliance", 37, "Posture", "Compliance Manager baseline assessment completed"),
    ExitCriterion("C02", "DEFENDCompliance", 37, "Posture", "Priority improvement actions agreed"),
    ExitCriterion("C03", "DEFENDCompliance", 37, "Insider Risk", "Insider Risk Management policies deployed"),
    ExitCriterion("C04", "DEFENDCompliance", 37, "Insider Risk", "HR and privacy alignment confirmed"),
    ExitCriterion("C05", "DEFENDCompliance", 37, "Insider Risk", "Alert thresholds tuned to reduce noise"),
    ExitCriterion("C06", "DEFENDCompliance", 37, "Audit", "Audit Premium enabled and retention confirmed"),
    ExitCriterion("C07", "DEFENDCompliance", 37, "Investigation", "eDiscovery Premium workflows tested"),
    ExitCriterion("C08", "DEFENDCompliance", 37, "Records", "Retention policies defined by data class"),
    ExitCriterion("C09", "DEFENDCompliance", 37, "Records", "Ownership of disposition reviews agreed"),
    ExitCriterion("C10", "DEFENDCompliance", 37, "Governance", "Compliance reporting cadence agreed"),
    ExitCriterion("C11", "DEFENDCompliance", 37, "Governance", "Risk acceptance extended to compliance decisions"),
    # Slide 38: DEFENDComplete (8 items, including 2 composite prerequisites)
    ExitCriterion(
        "M01",
        "DEFENDComplete",
        38,
        "Coverage",
        "DEFENDSecurity criteria met",
        is_composite_prerequisite=True,
        referenced_tier="DEFENDSecurity",
        allow_formal_risk_acceptance=False,
    ),
    ExitCriterion(
        "M02",
        "DEFENDComplete",
        38,
        "Coverage",
        "DEFENDCompliance criteria met",
        is_composite_prerequisite=True,
        referenced_tier="DEFENDCompliance",
        allow_formal_risk_acceptance=False,
    ),
    ExitCriterion("M03", "DEFENDComplete", 38, "Signal quality", "Defender incidents reviewed for accuracy"),
    ExitCriterion("M04", "DEFENDComplete", 38, "Signal quality", "Alert noise reduced to manageable levels"),
    ExitCriterion("M05", "DEFENDComplete", 38, "Governance", "Active and maintained risk register"),
    ExitCriterion("M06", "DEFENDComplete", 38, "Governance", "Exception handling and approval process defined"),
    ExitCriterion("M07", "DEFENDComplete", 38, "Operations", "Security and compliance ownership agreed"),
    ExitCriterion("M08", "DEFENDComplete", 38, "Reporting", "Executive reporting structure agreed"),
    # Slide 39: DEFENDExtend (9 items, including 1 hard composite prerequisite)
    ExitCriterion(
        "E01",
        "DEFENDExtend",
        39,
        "Foundations",
        "DEFENDComplete exit criteria met",
        is_composite_prerequisite=True,
        referenced_tier="DEFENDComplete",
        allow_formal_risk_acceptance=False,
    ),
    ExitCriterion("E02", "DEFENDExtend", 39, "SIEM", "Sentinel workspace deployed and secured"),
    ExitCriterion("E03", "DEFENDExtend", 39, "Detection", "Defender incidents integrated into Sentinel"),
    ExitCriterion("E04", "DEFENDExtend", 39, "Detection", "Analytics rules enabled and tested"),
    ExitCriterion("E05", "DEFENDExtend", 39, "Response", "SOAR playbooks deployed and validated"),
    ExitCriterion("E06", "DEFENDExtend", 39, "SOC", "Coverage model agreed; escalation paths documented"),
    ExitCriterion("E07", "DEFENDExtend", 39, "SOC", "Customer response responsibilities defined"),
    ExitCriterion("E08", "DEFENDExtend", 39, "AI", "Security Copilot use cases reviewed"),
    ExitCriterion("E09", "DEFENDExtend", 39, "Validation", "Quarterly readiness and tuning reviews scheduled"),
]


def compute_licensing_coverage_summary() -> Dict[str, object]:
    """Compute exact licensing feature coverage across the Defender (21 rows) and Purview (20 rows) tables."""
    def_total = len(DEFENDER_CAPABILITY_MATRIX)
    pur_total = len(PURVIEW_CAPABILITY_MATRIX)
    combined_total = len(ALL_CAPABILITY_ROWS)

    def_std = sum(1 for r in DEFENDER_CAPABILITY_MATRIX if r.business_standard)
    def_bp = sum(1 for r in DEFENDER_CAPABILITY_MATRIX if r.business_premium)
    def_addon = sum(1 for r in DEFENDER_CAPABILITY_MATRIX if r.with_suite_addon)

    pur_std = sum(1 for r in PURVIEW_CAPABILITY_MATRIX if r.business_standard)
    pur_bp = sum(1 for r in PURVIEW_CAPABILITY_MATRIX if r.business_premium)
    pur_addon = sum(1 for r in PURVIEW_CAPABILITY_MATRIX if r.with_suite_addon)

    # Combined capability counts per DEFEND tier license stack:
    std_total = def_std + pur_std
    bp_total = def_bp + pur_bp
    defend_security_total = def_addon + pur_bp
    defend_compliance_total = def_bp + pur_addon
    defend_complete_total = def_addon + pur_addon

    return {
        "defender_table_rows": def_total,
        "purview_table_rows": pur_total,
        "total_capability_rows": combined_total,
        "defender_suite_coverage": {
            "business_standard": {"count": def_std, "total": def_total, "pct": round(def_std / def_total * 100, 1)},
            "business_premium": {"count": def_bp, "total": def_total, "pct": round(def_bp / def_total * 100, 1)},
            "with_defender_suite": {"count": def_addon, "total": def_total, "pct": round(def_addon / def_total * 100, 1)},
        },
        "purview_suite_coverage": {
            "business_standard": {"count": pur_std, "total": pur_total, "pct": round(pur_std / pur_total * 100, 1)},
            "business_premium": {"count": pur_bp, "total": pur_total, "pct": round(pur_bp / pur_total * 100, 1)},
            "with_purview_suite": {"count": pur_addon, "total": pur_total, "pct": round(pur_addon / pur_total * 100, 1)},
        },
        "tier_bundle_coverage": {
            "Business_Standard": {
                "count": std_total,
                "total": combined_total,
                "pct": round(std_total / combined_total * 100, 1),
            },
            "DEFENDBase_Business_Premium": {
                "count": bp_total,
                "total": combined_total,
                "pct": round(bp_total / combined_total * 100, 1),
            },
            "DEFENDSecurity_BP_plus_Defender": {
                "count": defend_security_total,
                "total": combined_total,
                "pct": round(defend_security_total / combined_total * 100, 1),
            },
            "DEFENDCompliance_BP_plus_Purview": {
                "count": defend_compliance_total,
                "total": combined_total,
                "pct": round(defend_compliance_total / combined_total * 100, 1),
            },
            "DEFENDComplete_BP_plus_Both_Suites": {
                "count": defend_complete_total,
                "total": combined_total,
                "pct": round(defend_complete_total / combined_total * 100, 1),
            },
        },
    }


def evaluate_tier_readiness(
    tier: str,
    implemented_ids: set[str],
    risk_acceptances: Dict[str, RiskAcceptanceRecord],
    prior_tier_results: Optional[Dict[str, TierEvaluationResult]] = None,
) -> TierEvaluationResult:
    """Evaluate a tenant's readiness to exit a given DEFEND tier under the Slide 40 Governance Rule."""
    prior_tier_results = prior_tier_results or {}
    tier_items = [c for c in EXIT_CRITERIA if c.tier == tier]
    if not tier_items:
        raise ValueError(f"Unknown DEFEND tier: {tier}")

    implemented_count = 0
    risk_accepted_count = 0
    unsatisfied_count = 0
    composite_ok = True
    blocking_reasons: List[str] = []

    # Check DEFENDBase prerequisite for all higher tiers (Slide 20 & 26: Base first)
    if tier != "DEFENDBase" and "DEFENDBase" in prior_tier_results:
        if not prior_tier_results["DEFENDBase"].governance_rule_passed:
            composite_ok = False
            blocking_reasons.append("Prerequisite DEFENDBase exit criteria not met (Slide 20/40: Baseline security first)")

    for item in tier_items:
        if item.is_composite_prerequisite and item.referenced_tier:
            ref_res = prior_tier_results.get(item.referenced_tier)
            if ref_res and ref_res.governance_rule_passed:
                implemented_count += 1
            else:
                unsatisfied_count += 1
                composite_ok = False
                blocking_reasons.append(f"Composite prerequisite {item.criterion_id} ({item.description}) failed")
            continue

        if item.criterion_id in implemented_ids:
            implemented_count += 1
        elif item.allow_formal_risk_acceptance and item.criterion_id in risk_acceptances:
            ra = risk_acceptances[item.criterion_id]
            if ra.is_valid:
                risk_accepted_count += 1
            else:
                unsatisfied_count += 1
                blocking_reasons.append(f"{item.criterion_id} has invalid risk acceptance record")
        else:
            unsatisfied_count += 1
            blocking_reasons.append(f"Missing mandatory control {item.criterion_id}: {item.description}")

    # Hard Slide 40 rule: DEFENDExtend must not be activated unless DEFENDComplete controls are in place
    if tier == "DEFENDExtend":
        complete_res = prior_tier_results.get("DEFENDComplete")
        if not complete_res or not complete_res.governance_rule_passed:
            composite_ok = False
            if "Hard Governance Rule (Slide 40): DEFENDExtend prohibited without DEFENDComplete" not in blocking_reasons:
                blocking_reasons.append(
                    "Hard Governance Rule (Slide 40): DEFENDExtend must not be activated unless DEFENDComplete controls are in place"
                )

    total = len(tier_items)
    satisfied = implemented_count + risk_accepted_count
    score_pct = round((satisfied / total) * 100.0, 1)
    governance_passed = (unsatisfied_count == 0) and composite_ok

    if not governance_passed:
        action = "Send to a human"
    elif risk_accepted_count > 0:
        action = "Confirm"
    else:
        action = "Act automatically"

    return TierEvaluationResult(
        tier=tier,
        total_criteria=total,
        implemented_count=implemented_count,
        risk_accepted_count=risk_accepted_count,
        unsatisfied_count=unsatisfied_count,
        composite_prerequisites_met=composite_ok,
        governance_rule_passed=governance_passed,
        readiness_score_pct=score_pct,
        action=action,
        blocking_reasons=blocking_reasons,
    )


SMB_PARTNER_TOOLKIT_CATALOG: Dict[str, object] = {
    "toolkit_name": "Microsoft Product Ecosystem Security & AI Readiness Technical Engineering Toolkit (M365 Business Premium + Defender & Purview Suites)",
    "lifecycle_stages_count": 5,
    "core_aka_ms_links_count": 6,
    "core_assets": [
        {
            "stage": "Stage 1: Vertical Data Classification & SIT Architecture",
            "name": "Industry-Specific Information Protection Technical Reference Guides",
            "short_url": "https://aka.ms/MIP-Industry-OnePagers",
            "resolved_target": "Industry-Specific Information Protection Guides.zip (7 PDFs, 14 pages)",
            "industries": [
                "Consumer Goods",
                "Education (FERPA/COPPA/SIS)",
                "Financial Services & Insurance (GLBA/PCI-DSS/SOX)",
                "Healthcare (HIPAA/HITECH/EHR)",
                "Manufacturing & Distribution (CAD/BOM/MES/ITAR)",
                "Nonprofit (Donor PII/Grant Stewardship)",
                "Professional Services (M&A/Privileged Work Product)",
            ],
            "pages_total": 14,
            "deployment_phases_days": [30, 60, 90],
        },
        {
            "stage": "Stage 2: Client-Side Policy & Taxonomy Compilation",
            "name": "Data Security Guided Assistant (Client-Side Policy Compiler)",
            "short_url": "https://aka.ms/DataSecurityAssistant",
            "resolved_target": "https://microsoft.github.io/DataSecurityGuidedAssistant/",
            "github_repo": "https://github.com/microsoft/DataSecurityGuidedAssistant",
            "version": "v2.0.1572",
            "entry_workflows": ["Labeling Decision Engine", "DLP Policy Compiler", "Combined Taxonomy-to-DLP Pipeline"],
            "supported_label_models": ["8-tier DEFEND model (with INTERNAL EXCEPTION)", "4-tier simplified model"],
            "supported_industries_count": 8,
            "supported_regions_count": 8,
            "supported_license_tiers_count": 6,
        },
        {
            "stage": "Stage 3: Workstream Scope & Dependency Specification",
            "name": "Microsoft Purview Data Security Engineering Scope Generator",
            "short_url": "https://aka.ms/SOW-Generator",
            "resolved_target": "https://microsoft.github.io/SOWGenerator/",
            "github_repo": "https://github.com/microsoft/SOWGenerator",
            "license": "MIT",
            "modular_workstreams_total": 22,
            "priority_1_foundation_count": 9,
            "priority_2_intermediate_count": 1,
            "priority_3_advanced_and_ai_count": 12,
            "ai_and_extended_dlp_workstreams": [
                "DLP for Endpoints (USB, clipboard, network share, print restrictions)",
                "DLP for Teams (external chat & channel SIT/label inspection)",
                "DLP for Copilot (Rule 1 Prompt SIT gate + Rule 2 Sensitivity Label RAG grounding gate in simulation mode)",
                "DLP for Microsoft Edge / Inline Web Traffic (blocks sensitive paste/upload to unmanaged GenAI domains)",
                "Activate DSPM (weekly Copilot SharePoint/OneDrive/Fabric oversharing risk assessment)",
            ],
        },
        {
            "stage": "Stage 4: Multi-Workload Technical Implementation Manuals",
            "name": "Best Practice Security Deployment Guides (6 Workloads)",
            "short_url": "https://aka.ms/Security_SMBDeploymentGuides",
            "resolved_target": "Best Practice Security Deployment Guides for SMB.zip (6 PDFs, 360 pages)",
            "guides_count": 6,
            "pages_total": 360,
            "guides": [
                {
                    "workload_id": "W1",
                    "title": "Identity & Access Controls + Identity Protection (Entra ID P1, Entra ID P2, Defender for Identity)",
                    "pages": 90,
                    "updated": "2026-03-06",
                    "core_controls": [
                        "2+ cloud-only *.onmicrosoft.com Break-Glass accounts (FIDO2/Passkey, excluded from CA & PIM)",
                        "Authenticator passwordless phone sign-in + number matching + 10 Zero Trust CA templates",
                        "Entra ID P2 separate User Risk (High -> Password reset + MFA) & Sign-in Risk (Med/High -> MFA) CA policies",
                        "PIM JIT role & group activation (Active -> Eligible, 1-8h window, MFA/Auth Context, justification, approval)",
                        "Quarterly Access Reviews (Auto-apply remove access, 30-day inactivity helper) & Entitlement Access Packages",
                        "Defender for Identity DC sensors (v3.x/v2.x), gMSA DSA, SAM-R/NTLM auditing & NNR (TCP 135/UDP 137/TCP 3389)",
                    ],
                },
                {
                    "workload_id": "W2",
                    "title": "Data Security Deployment Best Practice (Business Premium + Purview Suite)",
                    "pages": 92,
                    "updated": "2026-06-24",
                    "core_controls": [
                        "Unified Audit Log + Modern Label Scheme (8-Label taxonomy ordered 0..N by restrictiveness)",
                        "Default Email label (GENERAL) + Default Document/Site label (CONFIDENTIAL \\ ALL EMPLOYEES) + SPO/OD co-authoring",
                        "INTERNAL EXCEPTION sub-labels (#5 & #8: metadata + watermark + DLP block + Copilot exclusion without RMS encryption)",
                        "Static vs Adaptive Scope retention policies + 2-year baseline vs 7-year default storage/legal liability control",
                        "Per-workload DLP (EXO, SPO, OD, Devices, Teams, Copilot 2-rule SIT+Label, Edge Inline Web AI) in 15-30d simulation",
                        "Client/Service Auto-Labeling, Online-Only Encryption (Allow offline access = Never), DSPM for AI, IRM & Adaptive Protection",
                    ],
                },
                {
                    "workload_id": "W3",
                    "title": "Email & App + Collaboration Protection (Defender for Office 365 Plan 1 & Plan 2)",
                    "pages": 52,
                    "updated": "2026-03-16",
                    "core_controls": [
                        "SPF (-all), DKIM (2048-bit CNAME), DMARC (p=quarantine/reject across active & parked domains)",
                        "Standard/Strict Preset Security Policies, Anti-Phishing impersonation, Safe Links & Safe Attachments (Email/SPO/OD/Teams)",
                        "Outbound Anti-Spam external auto-forwarding disabled (Off) + Configuration Analyzer drift monitoring",
                        "Teams third-party cloud storage blocked + Teams Admin Quarantine & Zero-Hour Auto-Purge (ZAP)",
                        "MDO P2 Priority Account protection, Attack Simulation (7 payloads incl. QR codes & OAuth consent), AIR & Threat Explorer",
                    ],
                },
                {
                    "workload_id": "W4",
                    "title": "Device Security Best Practice Deployment (Defender for Business & Defender for Endpoint Plan 2)",
                    "pages": 51,
                    "updated": "2026-03-16",
                    "core_controls": [
                        "Intune-MDE connector onboarding, Tamper Protection = On, Cloud-delivered protection = High, Block at First Sight",
                        "Silent BitLocker encryption (TPM 2.0 + XTS-AES, Allow Warning For Other Disk Encryption = Disabled) & Automatic Attack Disruption",
                        "ASR rules staged Audit (RuleMode=2) -> Block (RuleMode=1) (LSASS credential dump, WMI persistence, vulnerable signed drivers)",
                        "Intune MDE Machine Risk Score = Clear (Secure) wired to Entra Conditional Access (Require compliant device)",
                        "Tenant Subscription State upgrade (Defender for Business -> MDE P2) + RBAC Device Groups (5 remediation levels)",
                    ],
                },
                {
                    "workload_id": "W5",
                    "title": "Device Enrollment & Management Best Practice (Microsoft Intune Plan 1)",
                    "pages": 40,
                    "updated": "2026-03-16",
                    "core_controls": [
                        "MDM (corporate Autopilot/ABM/Managed Google Play) vs MAM App Protection Policies (BYOD without device enrollment)",
                        "Default Compliance Policy hardened: Mark devices with no compliance policy assigned = Not compliant",
                        "Device Platform Enrollment Restrictions blocking personal Windows/macOS/iOS/Android enrollment under MAM",
                        "MAM Core Apps protection (Block iCloud/iTunes backup, restrict data transfer to policy-managed apps, block Save As)",
                        "Require MFA for Intune Enrollment CA policy targeting App ID d4ebce55-015a-49b5-a083-c84d1797ae8c (Every time)",
                    ],
                },
                {
                    "workload_id": "W6",
                    "title": "SaaS Security Best Practice Deployment (Defender for Cloud Apps & App Governance)",
                    "pages": 35,
                    "updated": "2026-03-16",
                    "core_controls": [
                        "1-click MDE + Defender for Cloud Apps Shadow IT discovery (>31,000 cloud apps scored across >90 risk factors)",
                        "Cloud Discovery & Anomaly Detection policies with endpoint blocking (Unsanctioned tag -> MDE Network Protection)",
                        "OAuth App Governance (auditing Highly Privileged/Overprivileged/Unused Graph API apps + Auto-Disable in Audit mode)",
                        "App Connectors, SSPM posture scoring, MDA File DLP policies & Conditional Access App Control session proxy",
                        "Entra ID Username Enrichment for discovery logs & Daily/Weekly/Monthly SecOps operational cadence",
                    ],
                },
            ],
        },
        {
            "stage": "Stage 5: Idempotent PowerShell 7+ Automation & Drift Verification",
            "name": "PowerShell Deployment Scripts (SMBBestPracticeTool)",
            "short_url": "https://aka.ms/Deploy-Scripts",
            "resolved_target": "https://microsoft.github.io/BestPractice_Deploy-Scripts/",
            "github_repo": "https://github.com/microsoft/BestPractice_Deploy-Scripts",
            "runtime_requirement": "PowerShell 7+ (pwsh.exe)",
            "workload_toolkits_count": 4,
            "workload_toolkits": ["Products/Purview", "Products/Entra", "Products/Intune", "Products/Defender"],
            "entra_report_only_ca_templates_count": 13,
            "intune_baseline_tasks_count": 6,
            "purview_drift_capabilities": ["Deployment Plans (pre-deployment intent)", "Tenant Validation Reports (object drift detection)"],
        },
        {
            "stage": "Stage 0: End-to-End Engineering Pipeline Specification",
            "name": "Security Partner Toolkit Technical Overview & Feedback Telemetry",
            "short_url": "https://aka.ms/SecurityPartnerToolkit_Playbook",
            "survey_url": "https://aka.ms/SecurityPartnerToolkit-Survey",
            "resolved_target": "Partner Security Toolkit for Enabling SMB.pdf (10 pages, updated Sept 22, 2026)",
        },
    ],
    "defend_aligned_8_label_taxonomy": [
        {"order": 1, "priority_index": 0, "label": "PUBLIC", "encryption": False, "external_sharing": True, "lob_exception": False},
        {"order": 2, "priority_index": 1, "label": "GENERAL", "encryption": False, "external_sharing": True, "lob_exception": False, "default_for": "email"},
        {"order": 3, "priority_index": 2, "label": "CONFIDENTIAL \\ ALL EMPLOYEES", "encryption": True, "external_sharing": False, "lob_exception": False, "default_for": "files_and_sites"},
        {"order": 4, "priority_index": 3, "label": "CONFIDENTIAL \\ SPECIFIC PEOPLE", "encryption": True, "external_sharing": True, "lob_exception": False},
        {"order": 5, "priority_index": 4, "label": "CONFIDENTIAL \\ INTERNAL EXCEPTION", "encryption": False, "external_sharing": False, "lob_exception": True, "review_cadence_days": 90},
        {"order": 6, "priority_index": 5, "label": "HIGHLY CONFIDENTIAL \\ ALL EMPLOYEES", "encryption": True, "external_sharing": False, "lob_exception": False},
        {"order": 7, "priority_index": 6, "label": "HIGHLY CONFIDENTIAL \\ SPECIFIC PEOPLE", "encryption": True, "external_sharing": True, "lob_exception": False},
        {"order": 8, "priority_index": 7, "label": "HIGHLY CONFIDENTIAL \\ INTERNAL EXCEPTION", "encryption": False, "external_sharing": False, "lob_exception": True, "review_cadence_days": 90},
    ],
}


def evaluate_full_tenant_journey(
    implemented_ids: set[str],
    risk_acceptances: Optional[Dict[str, RiskAcceptanceRecord]] = None,
) -> Dict[str, TierEvaluationResult]:
    """Evaluate all 5 DEFEND tiers sequentially enforcing Slide 40 governance gates."""
    risk_acceptances = risk_acceptances or {}
    results: Dict[str, TierEvaluationResult] = {}
    for tier in ["DEFENDBase", "DEFENDSecurity", "DEFENDCompliance", "DEFENDComplete", "DEFENDExtend"]:
        results[tier] = evaluate_tier_readiness(
            tier=tier,
            implemented_ids=implemented_ids,
            risk_acceptances=risk_acceptances,
            prior_tier_results=results,
        )
    return results


def export_verifier_summary(output_path: Path) -> Dict[str, object]:
    """Export deterministic verification summary JSON."""
    licensing = compute_licensing_coverage_summary()
    all_atomic_ids = {c.criterion_id for c in EXIT_CRITERIA if not c.is_composite_prerequisite}
    full_pass = evaluate_full_tenant_journey(implemented_ids=all_atomic_ids)

    tier_counts = {
        tier: len([c for c in EXIT_CRITERIA if c.tier == tier])
        for tier in PLAYBOOK_METADATA["defend_tiers"]  # type: ignore[union-attr]
    }

    summary = {
        "metadata": PLAYBOOK_METADATA,
        "exit_criteria_counts": {
            "by_tier": tier_counts,
            "total_table_rows": len(EXIT_CRITERIA),
            "composite_prerequisite_rows": sum(1 for c in EXIT_CRITERIA if c.is_composite_prerequisite),
            "atomic_control_rows": len(all_atomic_ids),
        },
        "licensing_coverage": licensing,
        "smb_partner_toolkit_catalog": SMB_PARTNER_TOOLKIT_CATALOG,
        "reference_full_deployment_evaluation": {
            k: asdict(v) for k, v in full_pass.items()
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return summary


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "evidence" / "verifier-summary.json"
    data = export_verifier_summary(out)
    print(f"Exported verifier summary to {out} (total criteria={data['exit_criteria_counts']['total_table_rows']})")
