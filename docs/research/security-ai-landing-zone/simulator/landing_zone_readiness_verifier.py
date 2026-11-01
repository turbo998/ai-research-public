#!/usr/bin/env python3
"""Deterministic Secure AI Landing Zone & Frontier SOC Readiness Verifier.

Encodes the architectural, licensing, governance, and FTE Sprint gating rules
from the 42-slide "The path to the Frontier: AI for Security x Security for AI"
deck (`Frontier Security Deck-10.26 final.pptx`, 15,233,523 bytes,
SHA-256 `f82c91ebd5e9a3be3c0a95402dfa3fc483089dfb3e4bcd719609f4341d6864df`):
  1. 6 Mandatory Pre-Scale Questions (Slide 7) across Observe, Govern, Secure.
  2. 5 Customer Discovery Opener Questions (Slide 34) triggering Landing Zone
     Assessments when any question is answered "unsure" or "no".
  3. 5 Pillars of Secure AI Landing Zone (Slides 8-21, 20 atomic controls, 4 per pillar)
     governed by Microsoft Agent 365 and unified entry via Copilot as the UI for AI (Slide 6).
  4. Microsoft Agent 365 Prerequisite Licensing & M365 E7 Frontier Suite (Slides 22-23).
  5. 4-6 Week FTE Transformation Sprint Critical Path Gate (Slide 5): Week 3 Secure AI
     Landing Zone + Copilot as UI hard-gates Week 4-5 3-Agent production launch.
  6. Frontier SOC (Slides 24-32): Red/Blue/Green Agent Team, Unified Security & Exposure
     Graph (22 telemetry tables), MDASH (100+ specialized multi-model agents), and
     ISOC in Microsoft Defender (Available Now + November 2026 90-day retention & Perception GA).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple

DECK_METADATA: Dict[str, object] = {
    "file_name": "Frontier Security Deck-10.26 final.pptx",
    "file_size_bytes": 15233523,
    "sha256": "f82c91ebd5e9a3be3c0a95402dfa3fc483089dfb3e4bcd719609f4341d6864df",
    "total_slides": 42,
    "tracks": ["Security for AI (Slides 5-23)", "AI for Security / Frontier SOC (Slides 24-32)", "Partner Playbook & Toolkit (Slides 34-42)"],
    "ai_threat_case_study": {
        "slide": "Slides 3-4",
        "incident": "Monterrey, Mexico Municipal Water & Drainage Utility ICS Intrusion (Jan 2026, Campaign Dec 2025 - Feb 2026)",
        "threat_intel_sources": ["Dragos", "Gambit Security"],
        "ai_generated_loc": 17000,
        "ai_generated_modules": 49,
        "dual_model_division": "Claude (intrusion planning, tool dev, problem-solving) + GPT (victim data processing, structured reporting)",
    },
    "frontier_soc_kpis": {
        "slide": 24,
        "reduced_exposures": {"value": 847, "delta_7d_pct": 18.0},
        "active_investigations": {"value": 41, "delta_7d_pct": 12.0},
        "enriched_indicators": {"value": 124, "delta_7d_pct": 18.0},
        "disrupted_attacks": {"value": 23, "delta_7d_pct": 31.0},
    },
    "mdash_metrics": {
        "slide": 27,
        "stage": "Private Preview",
        "specialized_agents_min": 100,
        "architecture": "Multi-model (Frontier models + Microsoft first-party models) end-to-end vulnerability discovery, validation, and exploitability proof",
    },
    "isoc_defender_roadmap": {
        "slides": "Slides 28-32, 36",
        "eligible_licenses": ["Microsoft Defender Suite", "Microsoft 365 E5", "Microsoft 365 E7 (Frontier Suite)"],
        "available_now": ["Case Management", "SOAR Playbook Builder", "Workbooks", "UEBA", "Autonomous Attack Disruption", "Built-in SIEM"],
        "coming_nov_2026": ["90-Day Data Retention", "Content Hub + CI/CD", "Threat Intelligence Platform", "SOC Optimization", "Project Perception GA"],
    },
}


@dataclass(frozen=True)
class PreScaleQuestion:
    question_id: str
    domain: str  # Observe | Govern | Secure
    pillar_id: str
    question_zh: str
    question_en: str


PRE_SCALE_QUESTIONS: Tuple[PreScaleQuestion, ...] = (
    PreScaleQuestion("Q1", "Observe", "P1_VISIBILITY_GOVERNANCE", "组织里有多少 Agent？风险在哪？", "How many Agents exist in the organization, and where are the risks?"),
    PreScaleQuestion("Q2", "Govern", "P1_VISIBILITY_GOVERNANCE", "每个 Agent 谁负责？何时下线？", "Who is the accountable Owner for each Agent, and when is it retired?"),
    PreScaleQuestion("Q3", "Govern", "P5_COMPLIANCE_AUDIT", "Agent 的行为能否审计、可追溯？", "Are all Agent interactions and actions auditable and traceable?"),
    PreScaleQuestion("Q4", "Secure", "P2_IDENTITY_ACCESS", "Agent 能访问什么？是否过度授权？", "What resources can each Agent access, and is it over-privileged?"),
    PreScaleQuestion("Q5", "Secure", "P3_DATA_SECURITY", "Copilot 和 Agent 会不会泄露敏感数据？", "Will Copilot and Agents expose or leak sensitive corporate data?"),
    PreScaleQuestion("Q6", "Secure", "P4_THREAT_PROTECTION", "被提示注入攻击时，能否发现并阻断？", "Can prompt injection and malicious tool calls be detected and blocked at runtime?"),
)


@dataclass(frozen=True)
class DiscoveryOpenerQuestion:
    opener_id: str
    pillar_tag: str
    product_mapping: str
    question_zh: str
    question_en: str


DISCOVERY_OPENER_QUESTIONS: Tuple[DiscoveryOpenerQuestion, ...] = (
    DiscoveryOpenerQuestion("D1", "Visibility & Governance", "Microsoft Agent 365", "您的组织里现在有多少个 Agent？谁创建的、谁负责？", "How many Agents are in your organization today, who created them, and who owns them?"),
    DiscoveryOpenerQuestion("D2", "Data Security", "Microsoft Purview", "Copilot 能看到的数据，都已经分类和打标签了吗？", "Is all data accessible to Copilot already classified and sensitivity-labeled?"),
    DiscoveryOpenerQuestion("D3", "Identity & Access", "Microsoft Entra Agent ID", "Agent 用的是谁的身份？权限会过期吗？", "Whose identity are Agents using, and do their permissions expire?"),
    DiscoveryOpenerQuestion("D4", "Threat Protection", "Microsoft Defender + ISOC", "如果某个 Agent 被提示注入攻击，SOC 能看到并阻断吗？", "If an Agent is hit by a prompt injection attack, can the SOC see and block it?"),
    DiscoveryOpenerQuestion("D5", "Endpoint & Shadow AI", "Microsoft Defender + Intune", "员工终端上的本地 AI 工具和 Agent，管得住吗？", "Are local AI tools and Agents running on employee endpoints governed and controlled?"),
)


@dataclass(frozen=True)
class LandingZoneControl:
    control_id: str
    pillar_id: str
    pillar_name: str
    slide_ref: str
    name: str
    product: str
    pre_scale_question_id: str
    critical_for_week3_gate: bool = True


LANDING_ZONE_CONTROLS: Tuple[LandingZoneControl, ...] = (
    # Pillar 1: Visibility & Governance (Slides 8, 10-11, 20)
    LandingZoneControl("LZ-P1-01", "P1_VISIBILITY_GOVERNANCE", "① Visibility & Governance", "Slides 8, 10-11", "Agent 365 Unified Registry (Native Foundry / Copilot Studio / M365 Agents)", "Microsoft Agent 365 · M365 Admin Center", "Q1", True),
    LandingZoneControl("LZ-P1-02", "P1_VISIBILITY_GOVERNANCE", "① Visibility & Governance", "Slide 10", "Multi-Framework SDK & Cloud Registry Sync (LangChain, CrewAI, LlamaIndex, Vertex AI, Bedrock)", "Agent 365 SDK · Registry Sync", "Q1", True),
    LandingZoneControl("LZ-P1-03", "P1_VISIBILITY_GOVERNANCE", "① Visibility & Governance", "Slides 8, 10", "Mandatory Agent Owner Assignment & Decommissioning Lifecycle Policy", "Microsoft Agent 365 · M365 Admin Center", "Q2", True),
    LandingZoneControl("LZ-P1-04", "P1_VISIBILITY_GOVERNANCE", "① Visibility & Governance", "Slides 10, 20", "Endpoint & Network Shadow Agent Discovery (Local CLI, Desktop, Agentic IDE, Claw, SaaS)", "Microsoft Defender · Microsoft Intune", "Q1", True),
    # Pillar 2: Identity & Access (Slides 8, 12-13)
    LandingZoneControl("LZ-P2-01", "P2_IDENTITY_ACCESS", "② Identity & Access", "Slide 12", "Unique Entra Agent ID Assignment per Agent (No Shared/User Credentials)", "Microsoft Entra Agent ID", "Q4", True),
    LandingZoneControl("LZ-P2-02", "P2_IDENTITY_ACCESS", "② Identity & Access", "Slide 13", "Entra Access Packages Defining Explicit Least-Privilege Agent Scope & Expiry", "Microsoft Entra ID Governance", "Q4", True),
    LandingZoneControl("LZ-P2-03", "P2_IDENTITY_ACCESS", "② Identity & Access", "Slide 12", "Continuous Agent Risk Evaluation (Anomalous Agent Activity Flagging)", "Microsoft Entra ID Protection", "Q4", True),
    LandingZoneControl("LZ-P2-04", "P2_IDENTITY_ACCESS", "② Identity & Access", "Slide 12", "Real-Time Conditional Access Enforcement for Agents (Allow / Block per Request)", "Microsoft Entra Conditional Access", "Q4", True),
    # Pillar 3: Data Security (Slides 8, 14-15)
    LandingZoneControl("LZ-P3-01", "P3_DATA_SECURITY", "③ Data Security", "Slide 14", "Purview Sensitivity Labels Respected & Inherited by Copilot & Agents", "Microsoft Purview Information Protection", "Q5", True),
    LandingZoneControl("LZ-P3-02", "P3_DATA_SECURITY", "③ Data Security", "Slide 14", "Purview DLP Auto-Masking & Blocking of Sensitive Data in Agent Prompts/Outputs", "Microsoft Purview DLP", "Q5", True),
    LandingZoneControl("LZ-P3-03", "P3_DATA_SECURITY", "③ Data Security", "Slide 15", "DSPM for AI Centralized Visibility into Agent Activity, Sensitive Interactions & Policy Coverage", "Microsoft Purview DSPM for AI", "Q5", True),
    LandingZoneControl("LZ-P3-04", "P3_DATA_SECURITY", "③ Data Security", "Slide 14", "Insider Risk Management Risk Scoring for Risky Agents Correlated with Defender XDR", "Microsoft Purview Insider Risk Management", "Q5", True),
    # Pillar 4: Threat Protection (Slides 8, 16-17, 20-21)
    LandingZoneControl("LZ-P4-01", "P4_THREAT_PROTECTION", "④ Threat Protection", "Slides 16, 21", "Defender Runtime Inspection & Blocking of Prompt Injection, Tool Calls, MCP & APIs", "Microsoft Defender XDR · Defender for Cloud", "Q6", True),
    LandingZoneControl("LZ-P4-02", "P4_THREAT_PROTECTION", "④ Threat Protection", "Slide 17", "Agent Posture Management & Attack Path Graph across Connected Tools/Dependencies", "Microsoft Security Exposure Management", "Q6", True),
    LandingZoneControl("LZ-P4-03", "P4_THREAT_PROTECTION", "④ Threat Protection", "Slides 20-21", "Managed Endpoint Guardrails (Block Unauthorized Local Agents / Enforce Runtime Policy)", "Microsoft Defender for Endpoint · Intune", "Q6", True),
    LandingZoneControl("LZ-P4-04", "P4_THREAT_PROTECTION", "④ Threat Protection", "Slides 8, 16, 29", "Unified AgentSOC Signal Integration into ISOC in Microsoft Defender (XDR + Sentinel)", "ISOC in Microsoft Defender", "Q6", True),
    # Pillar 5: Compliance & Audit (Slides 8, 18-19)
    LandingZoneControl("LZ-P5-01", "P5_COMPLIANCE_AUDIT", "⑤ Compliance & Audit", "Slide 18", "Default Audit Logging of All Agent Interactions (What Agent Said, Did, Accessed)", "Microsoft Purview Audit", "Q3", True),
    LandingZoneControl("LZ-P5-02", "P5_COMPLIANCE_AUDIT", "⑤ Compliance & Audit", "Slides 18-19", "Communication Compliance OOTB Classifiers for Unethical Agent Behavior (e.g., Bribery/Gifts)", "Microsoft Purview Communication Compliance", "Q3", True),
    LandingZoneControl("LZ-P5-03", "P5_COMPLIANCE_AUDIT", "⑤ Compliance & Audit", "Slides 18-19", "Harmful Content, Copyright Infringement & Regulatory Violation Detection", "Microsoft Purview AI Compliance", "Q3", True),
    LandingZoneControl("LZ-P5-04", "P5_COMPLIANCE_AUDIT", "⑤ Compliance & Audit", "Slide 18", "Agent Interaction Retention, Deletion Policies & Defensible eDiscovery for Legal Holds", "Microsoft Purview Data Lifecycle & eDiscovery", "Q3", True),
)

QUALIFYING_AGENT365_LICENSES: Tuple[str, ...] = (
    "M365_E5",
    "M365_A5",
    "M365_Business_Premium",
    "Defender_Suite_plus_Purview_Suite",
    "Defender_Edu_plus_Purview_Edu",
    "Defender_and_Purview_FLW",
    "M365_E7_Frontier_Suite",
)

UNIFIED_SECURITY_GRAPH_TABLES: Tuple[str, ...] = (
    "DeviceInfo",
    "DeviceProcessEvents",
    "DeviceLogonEvents",
    "DeviceNetworkEvents",
    "DeviceRegistryEvents",
    "SignInLogs",
    "IdentityLogonEvents",
    "IdentityDirectoryEvents",
    "IdentityQueryEvents",
    "IdentityInfo",
    "AADServicePrincipalSignIn",
    "AlertInfo",
    "AlertEvidence",
    "SecurityIncident",
    "EmailEvents",
    "EmailAttachmentInfo",
    "ARGResources",
    "ARGResourceContainers",
    "BehaviorAnalytics",
    "ExposureGraphNodes",
    "ExposureGraphEdges",
    "RedTeamOperations",
)


@dataclass(frozen=True)
class LandingZoneReadinessResult:
    scenario_id: str
    license_bundle: str
    agent365_prerequisite_met: bool
    e7_frontier_suite_active: bool
    copilot_as_ui_unified: bool
    pillar_scores: Dict[str, Tuple[int, int, float]]
    satisfied_controls: int
    total_controls: int
    overall_readiness_pct: float
    pre_scale_questions_answered: int
    discovery_assessment_triggered: bool
    week3_fte_gate_passed: bool
    week4_5_agent_launch_allowed: bool
    isoc_eligible: bool
    recommended_partner_phase: str
    action_gate: str  # Act automatically | Confirm | Send to a human
    blocking_reasons: Tuple[str, ...]


def evaluate_landing_zone_readiness(
    scenario_id: str,
    license_bundle: str,
    copilot_as_ui_unified: bool,
    completed_control_ids: Sequence[str],
    discovery_unsure_ids: Sequence[str] = (),
    gate1_exec_sponsorship_met: bool = True,
) -> LandingZoneReadinessResult:
    """Evaluate Secure AI Landing Zone readiness, Week 3 FTE Gate, and Frontier SOC eligibility."""
    done = set(completed_control_ids)
    prereq_met = license_bundle in QUALIFYING_AGENT365_LICENSES
    e7_active = license_bundle == "M365_E7_Frontier_Suite"
    isoc_eligible = license_bundle in (
        "M365_E5",
        "M365_E7_Frontier_Suite",
        "Defender_Suite_plus_Purview_Suite",
        "M365_A5",
    )

    pillar_ids = (
        "P1_VISIBILITY_GOVERNANCE",
        "P2_IDENTITY_ACCESS",
        "P3_DATA_SECURITY",
        "P4_THREAT_PROTECTION",
        "P5_COMPLIANCE_AUDIT",
    )
    pillar_scores: Dict[str, Tuple[int, int, float]] = {}
    for pid in pillar_ids:
        p_controls = [c for c in LANDING_ZONE_CONTROLS if c.pillar_id == pid]
        sat = sum(1 for c in p_controls if c.control_id in done)
        tot = len(p_controls)
        pillar_scores[pid] = (sat, tot, round((sat / tot) * 100.0, 1))

    satisfied = sum(1 for c in LANDING_ZONE_CONTROLS if c.control_id in done)
    total = len(LANDING_ZONE_CONTROLS)
    overall_pct = round((satisfied / total) * 100.0, 1)

    # Check how many of the 6 Pre-Scale Questions have all mapped controls satisfied
    q_answered = 0
    for q in PRE_SCALE_QUESTIONS:
        q_controls = [c for c in LANDING_ZONE_CONTROLS if c.pre_scale_question_id == q.question_id]
        if all(c.control_id in done for c in q_controls):
            q_answered += 1

    discovery_triggered = len(discovery_unsure_ids) > 0 or satisfied < total

    blocking: List[str] = []
    if not prereq_met:
        blocking.append(f"LICENSE_BLOCK: '{license_bundle}' does not satisfy Microsoft Agent 365 prerequisite licensing (Slide 23)")
    if not gate1_exec_sponsorship_met:
        blocking.append("FTE_GATE1_BLOCK: Week 1-2 Gate 1 (5-10 quantifiable outcomes + executive sponsorship) not met (Slide 5)")
    if not copilot_as_ui_unified:
        blocking.append("SHADOW_AI_BLOCK: Copilot as the UI for AI is not unified; fragmented entry points create un-audited Shadow AI (Slide 6)")

    missing_controls = [c.control_id for c in LANDING_ZONE_CONTROLS if c.control_id not in done]
    if missing_controls:
        blocking.append(f"LANDING_ZONE_INCOMPLETE: {len(missing_controls)}/{total} Secure AI Landing Zone controls missing ({', '.join(missing_controls[:5])}{'...' if len(missing_controls) > 5 else ''})")

    # Slide 5 Hard Rule: Week 3 Secure AI Landing Zone + Copilot as UI must pass before Week 4-5 3-Agent launch
    week3_passed = prereq_met and gate1_exec_sponsorship_met and copilot_as_ui_unified and (satisfied == total)
    week4_5_allowed = week3_passed

    if week3_passed and isoc_eligible:
        recommended_phase = "Phase 3: Operate (Managed Frontier SOC + ISOC + Week 4-5 3-Agent Production Launch)"
        action_gate = "Act automatically"
    elif prereq_met and copilot_as_ui_unified and overall_pct >= 80.0:
        recommended_phase = "Phase 2: Build (Complete Remaining Week 3 Landing Zone Controls Before Agent Launch)"
        action_gate = "Confirm"
    else:
        recommended_phase = "Phase 1: Assess (Run 5-Question Discovery & Landing Zone Gap Assessment)"
        action_gate = "Send to a human"

    return LandingZoneReadinessResult(
        scenario_id=scenario_id,
        license_bundle=license_bundle,
        agent365_prerequisite_met=prereq_met,
        e7_frontier_suite_active=e7_active,
        copilot_as_ui_unified=copilot_as_ui_unified,
        pillar_scores=pillar_scores,
        satisfied_controls=satisfied,
        total_controls=total,
        overall_readiness_pct=overall_pct,
        pre_scale_questions_answered=q_answered,
        discovery_assessment_triggered=discovery_triggered,
        week3_fte_gate_passed=week3_passed,
        week4_5_agent_launch_allowed=week4_5_allowed,
        isoc_eligible=isoc_eligible,
        recommended_partner_phase=recommended_phase,
        action_gate=action_gate,
        blocking_reasons=tuple(blocking),
    )


if __name__ == "__main__":
    all_ids = [c.control_id for c in LANDING_ZONE_CONTROLS]
    res = evaluate_landing_zone_readiness(
        scenario_id="DEMO-E7-FRONTIER-READY",
        license_bundle="M365_E7_Frontier_Suite",
        copilot_as_ui_unified=True,
        completed_control_ids=all_ids,
    )
    print(f"Scenario: {res.scenario_id} | Readiness: {res.overall_readiness_pct}% | WK3 Gate: {res.week3_fte_gate_passed} | Action: {res.action_gate}")
