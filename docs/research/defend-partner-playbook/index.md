# Microsoft Product Ecosystem Security & AI Readiness Technical Engineering Practice: 5-Tier DEFEND Architecture, Purview AI Guardrails & 6-Workload (360-Page) Implementation Guide

> **Language / 语言**: [中文 (`README.md`)](./README.md) | **English (Current)**  
> **7-Card 4:5 Visual Benchmark Reports**: [English Report (`test-report.en.md`)](./test-report.en.md) · [中文报告 (`test-report.md`)](./test-report.md) · [Interactive HTML Deck (`test-report-cards.html`)](./test-report-cards.html) ([English Cards (`cards.html`)](./cards.html) | [中文卡片 (`cards.zh.html`)](./cards.zh.html))  
> **Deterministic Verifier & Datasets**: [`simulator/defend_tier_readiness_verifier.py`](./simulator/defend_tier_readiness_verifier.py) · [`simulator/test_defend_tier_readiness_verifier.py`](./simulator/test_defend_tier_readiness_verifier.py) · [`report.json`](./report.json) · [`evidence.json`](./evidence.json) · [`review.md`](./review.md)  
> **Companion Sub-Topic (`Child Study`)**: 🔗 **[Security AI Landing Zone & Frontier SOC Deep Dive (`../security-ai-landing-zone/`)](../security-ai-landing-zone/index.md)** ([中文专著](../security-ai-landing-zone/index.zh.md) | [English 7-Card](../security-ai-landing-zone/cards.html) | [中文 7 卡](../security-ai-landing-zone/cards.zh.html)) — *Security for AI × AI for Security*, Copilot as UI, Microsoft Agent 365 5-Pillar Control Plane, M365 E7 Frontier Suite & Defender ISOC / MDASH  
> **Research Pillar**: Pillar 04 — Zero-Trust Governance, Red Team & Security Engineering

---

## ⚠️ Important Architectural & Governance Boundary Disclaimer

Per Slides 4, 8, 44, and 53 of the *DEFEND Partner Playbook* (`© 2026 Microsoft Corporation`) and *Partner Security Toolkit for Enabling SMB.pdf* (10 pages, updated Sept 22, 2026):
1. **Technical Reference Architecture — Not a Standalone Microsoft SKU**: **The DEFEND 5-tier security architecture (`DEFENDBase`, `DEFENDSecurity`, `DEFENDCompliance`, `DEFENDComplete`, `DEFENDExtend`), the 4-tier Purview-for-AI governance model, and the Microsoft Security Engineering Toolkit are technical reference architectures and implementation building blocks, NOT standalone Microsoft SKUs.**
2. **Licensing & Explicit Policy Configuration**: Security controls and AI guardrails depend on eligible platform licensing (Microsoft 365 Business Premium, Microsoft Defender Suite, Microsoft Purview Suite, Microsoft Sentinel) and explicit policy configuration, simulation testing, and drift validation.
3. **Technical Engineering Scope & Sanitization**: This monograph focuses strictly on **Microsoft product security engineering, control-plane mechanics, client-side policy compilers, 360-page multi-workload deployment specifications, and PowerShell 7+ automation**; all personal names, email addresses, phone numbers, and tracking tokens have been removed.

---

## 1. Executive Summary: From the 5-Tier Control State Machine (`DEFEND`) to 6-Workload Engineering Implementation (`360p Guides + pwsh 7+`)

In production Microsoft 365 tenants (particularly environments built on Microsoft 365 Business Premium and multi-tenant delegated architectures), security engineering teams consistently face three technical failure modes (Slides 3, 6):
- **Silent Configuration Drift & Inactive Baseline Controls**: Tenants frequently hold Microsoft 365 Business Premium licenses without enforcing phishing-resistant MFA, Conditional Access, Intune device compliance, BitLocker encryption, or legacy authentication blocks—leaving native control planes dormant.
- **Copilot RAG Oversharing & Unmanaged Web AI Exfiltration**: Enabling Microsoft 365 Copilot or allowing browser access to third-party generative AI domains (ChatGPT, Gemini, DeepSeek) without a prioritized sensitivity label taxonomy, auto-classification, Endpoint/Teams/Copilot/Edge inline DLP, and Data Security Posture Management (DSPM for AI) exposes sensitive repositories to internal RAG oversharing and external paste/upload leakage.
- **Premature SIEM Telemetry Ingestion & SOC Alert Fatigue**: Routing raw telemetry into Microsoft Sentinel before configuring baseline identity, endpoint ASR, email anti-phishing, and data policies floods SOC queues with low-signal noise and inflates ingestion overhead.

This monograph unifies four complementary Microsoft engineering assets into a single **Control-Plane State Machine + 6-Workload Implementation** technical reference:
1. **5-Tier Security State Machine & Governance Gates — *DEFEND Architecture Playbook* (11 Chapters / 53 Slides, SHA-256: `0298c3bb248a0465...`)**: Defines a **5-tier security & compliance progression model** anchored on Microsoft 365 Business Premium, a **41-row licensing capability matrix**, **51 mandatory tier-exit criteria**, the **Slide 40 Governance Rule**, and the **4-tier Purview-for-AI data governance architecture**.
2. **5-Stage Technical Engineering Pipeline — *Partner Security Toolkit for Enabling SMB.pdf* (10 pages, updated Sept 22, 2026)**: Orchestrates end-to-end engineering across **Stage 1: Vertical SIT & Taxonomy Mapping → Stage 2: Client-Side Policy Compilation (`v2.0.1572`) → Stage 3: 22-Workstream Technical Scope Specification → Stage 4: 6-Workload Portal & PowerShell Runbooks (`360p`) → Stage 5: Idempotent PowerShell 7+ Automation & Drift Validation**.
3. **7 Regulated Vertical Information Protection Specifications — *Industry-Specific Information Protection Guides.zip* (7 PDFs / 14 pages)**: Specifies vertical-specific Sensitive Information Types (SITs), custom regex/EDM identifiers, 30/60/90-day implementation stages, and the **8-Label DEFEND Sensitivity Taxonomy** featuring explicit **`INTERNAL EXCEPTION` sub-labels (#5 and #8)** that preserve metadata, watermarks, DLP blocking, and Copilot RAG exclusion without AES-256 RMS encryption when encryption breaks headless ERP/EHR/SIS/MES batch parsers.
4. **6-Workload Step-by-Step Technical Deployment Guides — *Best Practice Security Deployment Guides for SMB.zip* (6 PDFs / 360 pages) & `SMBBestPracticeTool` (PowerShell 7+)**: Provides exhaustive portal paths, protocol parameters, PowerShell cmdlets, and safety gates across **Identity Protection (90p)**, **Data Security & AI Guardrails (92p)**, **Email & Collaboration Protection (52p)**, **Device Security (51p)**, **Device Enrollment & Management (40p)**, and **SaaS Security (35p)**.

![DEFEND 5-Tier Architecture Overview](./assets/overview.svg)

---

## 2. Structural Breakdown of the *DEFEND Architecture Playbook* (11 Chapters / 53 Slides)

| Chapter | Slides | Chapter Title | Core Technical Deliverables & Control Mechanisms |
| :---: | :---: | :--- | :--- |
| **Ch 01** | Slides 1–7 | **Welcome to the DEFEND Architecture** | Defines the 5 DEFEND tiers (`DEFENDBase` → `DEFENDSecurity` / `DEFENDCompliance` → `DEFENDComplete` → `DEFENDExtend`), 4 engineering objectives (baseline standardization, suite activation, drift elimination, noise reduction), and the architectural boundary |
| **Ch 02** | Slides 8–16 | **Licensing Building Blocks** | Deconstructs **M365 Business Premium**, **Defender Suite** add-on (21-row comparison table, Slides 10–11), **Purview Suite** add-on (20-row comparison table, Slides 13–14), and **Microsoft Sentinel** SIEM/SOAR extension |
| **Ch 03** | Slides 17–20 | **Start with Security Posture (Zero Trust Assessment)** | Mandates running the **Microsoft Zero Trust Assessment** before policy design, evaluating **7 dimensions**: `Identity`, `Devices`, `Applications`, `Data`, `Infrastructure`, `Networks`, and `AI` |
| **Ch 04** | Slides 21–24 | **Core Operating Foundations (Lighthouse & Intune)** | Establishes strict control-plane separation between **M365 Lighthouse** (GDAP-based multi-tenant baseline visibility — **NOT a SOC/SIEM or Intune replacement**) and **Microsoft Intune Plan 1** (the authoritative device compliance enforcement engine) |
| **Ch 05** | Slides 25–31 | **The DEFEND Service Model** | Specifies technical applicability, mandatory controls, telemetry requirements, and step-up triggers for each of the 5 DEFEND tiers |
| **Ch 06** | Slides 32–33 | **Mapping Capabilities Across Tiers** | Maps control-plane progression across Identity, Devices, Email/Collaboration, Data Protection, Governance, and SIEM/SOC |
| **Ch 07** | Slides 34–40 | **Tier Exit Criteria & Governance Rules** | Defines the **51 mandatory exit criteria rows (48 atomic controls + 3 composite cross-tier gates, Slides 35–39)** and the **Slide 40 Governance Rule** (no progression without exit criteria or signed compensating-control risk acceptance; `DEFENDExtend` prohibited without `DEFENDComplete`) |
| **Ch 08** | Slides 41–42 | **Technical & Operational Readiness Checklist** | Covers Governance Readiness (SLAs, risk acceptance, exception review), Technical Readiness (GDAP, Lighthouse, Intune, LLDs), and Operational Readiness (alert routing, posture reviews) |
| **Ch 09** | Slides 43–46 | **Appendix A — Technical Scope Boundary Blueprint** | Explicit **Included Controls** vs **Excluded Controls** per tier to prevent cross-tier configuration drift |
| **Ch 10** | Slides 47–51 | **Appendix B — Purview-for-AI 4-Tier Architecture** | Structures Purview into **4 additive technical layers**: `Tier 1 Data Protect` → `Tier 2 Data Govern` → `Tier 3 Data Control (AI Ready)` → `Tier 4 Data Assure (Continuous Operations)` |
| **Ch 11** | Slides 52–53 | **Summary, Implementation Roadmap & Official References** | Consolidates technical implementation steps and 12 authoritative Microsoft Learn / `aka.ms` reference links |

---

## 3. Licensing Building Blocks & Exact 41-Capability Quantitative Matrix (Chapter 02 · Slides 8–16)

By parsing the underlying XML tables on Slides 10–11 (21 Defender rows) and Slides 13–14 (20 Purview rows) and verifying them via `defend_tier_readiness_verifier.py`, we establish that **Microsoft 365 Business Premium alone covers 15 of the 41 advanced capabilities (`36.6%`)**, whereas adding both the **Defender Suite** and **Purview Suite** reaches **`41 / 41` (`100.0%`)**—delivering full Enterprise E5 security and compliance parity for SMB tenants:

### 3.1 Cross-Tier Licensing Coverage Summary

| Licensing Bundle / DEFEND Tier | Defender Matrix (21 Rows, Slides 10–11) | Purview Matrix (20 Rows, Slides 13–14) | Combined 41-Row Coverage | Net Gain vs Business Premium |
| :--- | :---: | :---: | :---: | :---: |
| **Microsoft 365 Business Standard** *(Reference Baseline)* | `2 / 21` (`9.5%`) | `3 / 20` (`15.0%`) | **`5 / 41` (`12.2%`)** | `-24.4 pts` *(lacks Zero Trust baseline)* |
| **Microsoft 365 Business Premium (`DEFENDBase` / `Data Protect`)** | `8 / 21` (`38.1%`) | `7 / 20` (`35.0%`) | **`15 / 41` (`36.6%`)** | **Baseline (`0.0 pts`)** |
| **Business Premium + Defender Suite (`DEFENDSecurity`)** | **`21 / 21` (`100.0%`)** | `7 / 20` (`35.0%`) | **`28 / 41` (`68.3%`)** | **`+31.7 pts`** *(Security `+61.9 pts`)* |
| **Business Premium + Purview Suite (`DEFENDCompliance` / `Data Control`)** | `8 / 21` (`38.1%`) | **`20 / 20` (`100.0%`)** | **`28 / 41` (`68.3%`)** | **`+31.7 pts`** *(Compliance/AI `+65.0 pts`)* |
| **Business Premium + Both Suites (`DEFENDComplete` / E5 Parity)** | **`21 / 21` (`100.0%`)** | **`20 / 20` (`100.0%`)** | **`41 / 41` (`100.0%`)** | **`+63.4 pts`** *(100% Full Parity)* |

### 3.2 Defender Suite 21-Row Capability Matrix (Slides 10–11)

| Domain | ID | Capability Row | Business Standard | Business Premium (`DEFENDBase`) | + Defender Suite (`DEFENDSecurity`) | Enterprise E5 |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: |
| **Email Protection (5)** | `D01` | Spam and malware protection (Exchange Online Protection) | ● | ● | ● | ● |
| **Email Protection** | `D02` | Advanced phishing, zero-day malware & link protection (MDO Plan 1: Safe Links / Safe Attachments) | ○ | ● | ● | ● |
| **Email Protection** | `D03` | Phishing simulation and end-user security training (Attack Simulation Training — MDO Plan 2) | ○ | ○ | **●** | ● |
| **Email Protection** | `D04` | Automated investigation and remediation for email threats (AIR — MDO Plan 2) | ○ | ○ | **●** | ● |
| **Email Protection** | `D05` | Cross-domain threat hunting across email, links and collaboration (Threat Explorer — MDO Plan 2) | ○ | ○ | **●** | ● |
| **Endpoint Protection (5)** | `D06` | Built-in OS antivirus protection | ● | ● | ● | ● |
| **Endpoint Protection** | `D07` | Next-gen endpoint protection, behavioral EDR & ASR rules (Defender for Business) | ○ | ● | ● | ● |
| **Endpoint Protection** | `D08` | Advanced endpoint threat hunting across devices (MDE Plan 2 Advanced Hunting) | ○ | ○ | **●** | ● |
| **Endpoint Protection** | `D09` | Extended alert retention (6 months) & deeper forensic investigation timelines (MDE Plan 2) | ○ | ○ | **●** | ● |
| **Endpoint Protection** | `D10` | Threat analytics and global threat intelligence insights (Defender Threat Intelligence / MDE P2) | ○ | ○ | **●** | ● |
| **Identity & Access (9)** | `D11` | Multi-factor authentication (MFA) | ○ | ● | ● | ● |
| **Identity & Access** | `D12` | Conditional Access policies (user, device, location, app — Entra ID P1) | ○ | ● | ● | ● |
| **Identity & Access** | `D13` | Risk-based Conditional Access & Identity Protection (sign-in risk & user risk — Entra ID P2) | ○ | ○ | **●** | ● |
| **Identity & Access** | `D14` | Self-service password reset (SSPR) for cloud and hybrid users (Entra ID P1) | ○ | ● | ● | ● |
| **Identity & Access** | `D15` | Automated remediation for compromised user accounts (Entra ID P2) | ○ | ○ | **●** | ● |
| **Identity & Access** | `D16` | Privileged Identity Management (PIM — just-in-time admin elevation & approval — Entra ID P2) | ○ | ○ | **●** | ● |
| **Identity & Access** | `D17` | Access reviews and entitlement management (Entra ID P2 Governance) | ○ | ○ | **●** | ● |
| **Identity & Access** | `D18` | Hybrid / on-premises Active Directory identity threat detection (Defender for Identity — MDI) | ○ | ○ | **●** | ● |
| **Identity & Access** | `D19` | Detailed identity risk investigation and workbook insights (Entra ID P2 + MDI) | ○ | ○ | **●** | ● |
| **Cloud App Security (2)** | `D20` | Basic cloud app visibility and OAuth app discovery | ○ | ● | ● | ● |
| **Cloud App Security** | `D21` | Full CASB: Shadow IT governance, real-time session control & SaaS posture (Defender for Cloud Apps) | ○ | ○ | **●** | ● |

### 3.3 Purview Suite 20-Row Capability Matrix (Slides 13–14)

| Domain | ID | Capability Row | Business Standard | Business Premium (`DEFENDBase`) | + Purview Suite (`DEFENDCompliance`) | Enterprise E5 |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: |
| **Information Protection (6)** | `P01` | Manual sensitivity labels in Office apps | ● | ● | ● | ● |
| **Information Protection** | `P02` | Sensitivity labels with encryption, visual markings & rights management (Azure RMS) | ○ | ● | ● | ● |
| **Information Protection** | `P03` | Automatic sensitivity labeling in Office apps, SharePoint & OneDrive (Client + Service Auto-Labeling) | ○ | ○ | **●** | ● |
| **Information Protection** | `P04` | Classification using sensitive info types, trainable classifiers & fingerprinted templates | ○ | ○ | **●** | ● |
| **Information Protection** | `P05` | Customer-managed encryption keys (Bring Your Own Key — BYOK) | ○ | ○ | **●** | ● |
| **Information Protection** | `P06` | Double Key Encryption (DKE) for highly regulated workloads | ○ | ○ | **●** | ● |
| **Data Loss Prevention (6)** | `P07` | DLP for Exchange Online, SharePoint Online & OneDrive for Business | ○ | ● | ● | ● |
| **Data Loss Prevention** | `P08` | DLP for Teams chat and channel messages | ○ | ○ | **●** | ● |
| **Data Loss Prevention** | `P09` | Endpoint DLP (Windows & macOS file copy, print, USB, upload, browser transfer restrictions) | ○ | ○ | **●** | ● |
| **Data Loss Prevention** | `P10` | DLP for cloud apps and inline SaaS session controls (integrated with Defender for Cloud Apps) | ○ | ○ | **●** | ● |
| **Data Loss Prevention** | `P11` | **DLP for Microsoft 365 Copilot** (sensitivity label & SIT controls for AI prompts/grounding) | ○ | ○ | **●** | ● |
| **Data Loss Prevention** | `P12` | Adaptive DLP enforcement driven by user Insider Risk levels (Adaptive Protection) | ○ | ○ | **●** | ● |
| **Data Lifecycle Mgmt (3)** | `P13` | Manual retention and deletion labels | ● | ● | ● | ● |
| **Data Lifecycle Mgmt** | `P14` | Basic tenant-wide retention policies for Exchange, SharePoint & OneDrive | ○ | ● | ● | ● |
| **Data Lifecycle Mgmt** | `P15` | Automatic retention policies based on events, trainable classifiers & sensitive content (Records Mgmt) | ○ | ○ | **●** | ● |
| **Insider Risk & Comm (3)** | `P16` | Insider Risk Management (data theft, departing employee exfiltration, policy violations) | ○ | ○ | **●** | ● |
| **Insider Risk & Comm** | `P17` | Adaptive Protection (dynamic Conditional Access & DLP tightening based on insider risk score) | ○ | ○ | **●** | ● |
| **Insider Risk & Comm** | `P18` | Communication Compliance (detecting regulatory violations, harassment, sensitive sharing in Teams/Email) | ○ | ○ | **●** | ● |
| **eDiscovery & Audit (2)** | `P19` | Basic eDiscovery (Standard) and 90-day standard audit logs | ● | ● | ● | ● |
| **eDiscovery & Audit** | `P20` | **eDiscovery (Premium) & Audit (Premium)** (1-year+ log retention, legal hold notifications, review sets, AI-relevant high-value audit events) | ○ | ○ | **●** | ● |

---

## 4. Zero Trust Posture Discovery & Dual Operating Foundations (Chapters 03–04 · Slides 17–24)

### 4.1 Phase 0: The 7-Dimension Microsoft Zero Trust Assessment (Slides 17–20)
The Playbook establishes an explicit engagement rule: **Start with Security Posture, Not Licensing**. Before recommending add-on suites, partners run the Microsoft Zero Trust Assessment across **7 dimensions**:
1. **Identity**: MFA coverage, privileged account sprawl, legacy authentication protocols, Conditional Access gaps.
2. **Devices**: Intune enrollment coverage, non-compliant device access, BitLocker encryption state, OS patch hygiene.
3. **Applications**: OAuth third-party app consent risks and Shadow IT cloud app exposure.
4. **Data**: Sensitive data discovery, unlabeled files, anonymous external sharing links, and internal oversharing.
5. **Infrastructure**: Hybrid and administrative control-plane configurations.
6. **Networks**: Named locations, session controls, and boundary protections.
7. **AI**: Copilot and generative AI data access boundaries, DLP readiness, and DSPM for AI posture.

### 4.2 Strict Separation of Duties: M365 Lighthouse vs. Microsoft Intune Plan 1 (Slides 21–24)
- **Microsoft 365 Lighthouse = Multi-Tenant Visibility & Baseline Governance Plane**: Uses **GDAP (Granular Delegated Admin Privileges)** scoped to least-privilege security groups to aggregate baseline compliance, MFA/CA posture, risky users, and Defender for Business status across customer tenants. **Slide 21 explicitly warns: Lighthouse is NOT a SOC/SIEM detection platform, NOT a replacement for Intune device management, and NOT a substitute for Entra ID P2 PIM.**
- **Microsoft Intune Plan 1 = Authoritative Device Enforcement Engine**: All device compliance policies, BitLocker encryption, firewall and ASR rules, MAM App Protection Policies, and device-based Conditional Access enforcement must be authored and enforced in **Intune**.

---

## 5. The 5 DEFEND Tiers, 51 Mandatory Exit Criteria & Slide 40 Governance Rule (Chapters 05–07 · Slides 25–40)

![DEFEND 51-Gate State Machine](./assets/gating-matrix.svg)

### 5.1 Complete 51-Item Mandatory Tier Exit Criteria Checklist (Slides 35–39)

1. **`DEFENDBase` (Slide 35 · 11 Mandatory Exit Checks `B01–B11`)**:
   - `B01–B03` (Identity): MFA enforced for all users (`B01`); baseline Conditional Access policies live (`B02`); **legacy authentication blocked or formally risk accepted (`B03`)**.
   - `B04–B07` (Devices): Managed devices enrolled in Intune (`B04`); device compliance policies active (`B05`); BitLocker, firewall & Secure Boot enforced (`B06`); Defender for Business deployed & reporting (`B07`).
   - `B08–B09` (Email): Defender for Office 365 Plan 1 active (`B08`); mail flow protections validated and risky auto-forwarding blocked (`B09`).
   - `B10–B11` (Visibility & Governance): M365 Lighthouse connected (`B10`); **customer risk register created with residual risks and exceptions signed off (`B11`)**.
2. **`DEFENDSecurity` (Slide 36 · 12 Mandatory Exit Checks `S01–S12`)**:
   - `S01–S03` (Identity): Sign-in/user risk CA policies live (`S01`); **PIM active for all admin roles (`S02`)**; Access Reviews configured (`S03`).
   - `S04–S06` (Endpoint): MDE Plan 2 advanced hunting & AIR enabled (`S04`); TVM remediation workflow established (`S05`); endpoint alert noise tuned (`S06`).
   - `S07–S08` (Email): MDO Plan 2 advanced phishing & AIR live (`S07`); Attack Simulation Training scheduled (`S08`).
   - `S09–S12` (Cloud, Hybrid & Operations): Defender for Cloud Apps OAuth/Shadow IT controls active (`S09`); Defender for Identity deployed where hybrid AD exists (`S10`); alert triage/SLAs defined (`S11`); high-severity incident signal quality validated (`S12`).
3. **`DEFENDCompliance` (Slide 37 · 11 Mandatory Exit Checks `C01–C11`)**:
   - `C01–C02` (Posture): Compliance Manager baseline completed (`C01`); priority regulatory mappings aligned (`C02`).
   - `C03–C05` (Insider Risk): Insider Risk Management configured (`C03`); **review workflows aligned with HR, legal & privacy boundaries (`C04`)**; departing user/exfiltration indicators enabled (`C05`).
   - `C06–C07` (Audit & Investigation): **Audit Premium** retention extended (`C06`); **eDiscovery Premium** workflows tested (`C07`).
   - `C08–C11` (Records & Governance): Retention labels/policies active (`C08`); disposition reviews established (`C09`); compliance RBAC role separation enforced (`C10`); executive compliance reporting cadence agreed (`C11`).
4. **`DEFENDComplete` (Slide 38 · 8 Mandatory Exit Checks `M01–M08`)**:
   - `M01–M02` (Composite Coverage Gates): **All 12 `DEFENDSecurity` exit criteria met (`M01`)** AND **all 11 `DEFENDCompliance` exit criteria met (`M02`)**.
   - `M03–M08` (Signal Quality, Governance, Operations & Reporting): Security & compliance alerts noise-tuned (`M03`); false-positive suppressions documented (`M04`); unified risk register updated (`M05`); QBR cadence active (`M06`); cross-domain security/compliance escalation paths defined (`M07`); customer & Lighthouse dashboards operational (`M08`).
5. **`DEFENDExtend` (Slide 39 · 9 Mandatory Exit Checks `E01–E09`)**:
   - `E01` (Composite Hard Gate): **All `DEFENDComplete` exit criteria met (`E01`)**.
   - `E02–E09` (SIEM, Detection, Response, SOC, AI & Validation): Sentinel workspace & RBAC secured (`E02`); priority connectors ingested (`E03`); analytics rules tuned (`E04`); SOAR Logic Apps playbooks tested (`E05`); SOC escalation/SLAs signed (`E06`); Sentinel ↔ Defender XDR bidirectional sync validated (`E07`); **Security Copilot use cases reviewed where licensed (`E08`)**; end-to-end detection/response validated via tabletop or live test (`E09`).

---

## 6. Appendix B Deep Dive: 4-Tier Purview-as-a-Service & Copilot AI Governance (Chapter 10 · Slides 47–51)

| Service Tier | Licensing Requirement | Sensitivity Labels | DLP Scope | Audit & eDiscovery | Insider Risk & AI Governance (Copilot Readiness) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1 — Data Protect** | Business Premium | Manual, default & mandatory | Email (Exchange) & files (SPO/OneDrive) | Basic (90-day audit, Standard eDiscovery) | Not included; Compliance Manager self-assessed baseline |
| **Tier 2 — Data Govern** | BP + **Purview Suite** | **Automated** (content & classifiers) | **Endpoints**, **Teams chats** & cloud apps | **Premium** (extended retention & legal hold) | **Insider Risk Management** included; automated compliance assessment |
| **Tier 3 — Data Control** | BP + **Purview Suite** | **AI-related** & classifier-driven | **+ AI surfaces (DLP for M365 Copilot)** | Forensic search & AI prompt/response audit | **AI-tuned (DSPM for AI + Adaptive Protection)** for Copilot readiness |
| **Tier 4 — Data Assure** | BP + Purview + **Partner Managed** | Partner-managed lifecycle | + Continuous policy tuning | Managed reporting & legal/HR workflows | Managed triage, monthly posture reporting & quarterly governance reviews |

---

## 7. Microsoft Security Partner Toolkit for SMB — End-to-End 5-Stage Execution & Resolved Link Asset Deep Dive

While the *DEFEND Partner Playbook* defines the strategic 5-tier service architecture (**what and why**), the **Microsoft Security Partner Toolkit for SMB — Accelerate Security and AI Readiness Engagements** provides the complete operational execution kit (**how**) across all 5 stages of a partner engagement.

![SMB Partner Toolkit 5-Stage Lifecycle](./assets/partner-toolkit-lifecycle.svg)

### 7.1 Full Engagement Lifecycle & Resolved 6-Asset Catalog

| Lifecycle Stage | Toolkit Asset | Canonical Short Link | Resolved Target / Official GitHub Repository | Verified Technical Scope |
| :--- | :--- | :--- | :--- | :--- |
| **1. Initial Conversations** | **Industry-Specific Information Protection One-Pagers** | `https://aka.ms/MIP-Industry-OnePagers` | `Industry-Specific Information Protection Guides.zip` (`1.01 MB`) | **7 two-page PDFs (14 pages)**: Consumer Goods, Education (*New*), Financial Services & Insurance, Healthcare, Manufacturing & Distribution, Nonprofit (*New*), Professional Services; 30/60/90-day motion + **8-Label DEFEND Taxonomy** |
| **2. Discovery & Scoping** | **Data Security Guided Assistant** | `https://aka.ms/DataSecurityAssistant` | Live App: `https://microsoft.github.io/DataSecurityGuidedAssistant/`<br>Repo: `https://github.com/microsoft/DataSecurityGuidedAssistant` (`v2.0.1572`) | Client-side interactive decision engine (`index.html`, `570 KB`, strict CSP) with **Labeling Tool**, **DLP Tool**, and **Combined Flow** across 8 industries, 8 regions, 6 license tiers, and 8-tier vs 4-tier label models |
| **3. Proposal Development** | **Microsoft Purview Data Security SOW Generator** | `https://aka.ms/SOW-Generator` | Live App: `https://microsoft.github.io/SOWGenerator/`<br>Repo: `https://github.com/microsoft/SOWGenerator` (MIT License) | Browser-based **Statement of Work (SOW)** builder covering **22 modular workstreams** across Priority 1 (9 Foundation), Priority 2 (1 Intermediate), and Priority 3 (12 Advanced & AI Guardrails) + Managed Services |
| **4. Planning & Implementation** | **Security SMB Deployment Guides** | `https://aka.ms/Security_SMBDeploymentGuides` | `Best Practice Security Deployment Guides for SMB.zip` (`31.82 MB`) | **6 step-by-step PDF deployment manuals totaling 360 pages**: Data Security (92p), Identity Protection (90p), Email & Collaboration (52p), Device Security (51p), Device Management (40p), SaaS Security (35p) |
| **5. Deployment & Configuration** | **PowerShell Deployment Scripts (`SMBBestPracticeTool`)** | `https://aka.ms/Deploy-Scripts` | Docs: `https://microsoft.github.io/BestPractice_Deploy-Scripts/`<br>Repo: `https://github.com/microsoft/BestPractice_Deploy-Scripts` | Idempotent **PowerShell 7+ (`pwsh.exe`)** automation across **4 workload toolkits** (`Products/Purview`, `Products/Entra`, `Products/Intune`, `Products/Defender`) with GDAP, `-WhatIf`, safety gates & HTML/JSON reports |
| **Umbrella Playbook & Feedback** | **Security Partner Toolkit Playbook & Survey** | `https://aka.ms/SecurityPartnerToolkit_Playbook`<br>`https://aka.ms/SecurityPartnerToolkit-Survey` | `Partner Security Toolkit for Enabling SMB.pdf` & Microsoft Customer Voice | Master 5-stage partner orchestration playbook and product feedback channel |

---

### 7.2 Asset 1 Deep Dive: 7 Industry One-Pagers & the 8-Label DEFEND-Aligned Taxonomy (`aka.ms/MIP-Industry-OnePagers`)

The ZIP archive (`Industry-Specific Information Protection Guides.zip`) contains **7 two-page industry playbooks (14 PDF pages)**:
1. **Consumer Goods SMB** (`Consumer_Goods_SMB_Purview_One_Pager.pdf`, 2p): Food & Beverage, Health & Beauty, Apparel, Consumer Electronics, CPG; protects retailer joint business plans (JBPs), formulations, co-manufacturer specs, and FDA recall files.
2. **Education SMB (*New*)** (`Education_SMB_Purview_One_Pager_MVP.pdf`, 2p): K-12 Private Schools, Higher Education, Early Childhood, Workforce Training, EdTech; protects FERPA/COPPA student records, transcripts, IEP/504 plans, financial aid, and safeguarding files.
3. **Financial Services / Insurance SMB** (`Financial_Services_Insurance_SMB_Purview_One_Pager.pdf`, 2p): Capital Markets, Banking, Insurance Direct/Brokerage, Public Finance; protects KYC files, loan files, underwriting/claims, ABA/IBAN/SWIFT/credit card SITs, and AML filings.
4. **Healthcare SMB** (`Healthcare_SMB_Purview_One_Pager.pdf`, 2p): Health Provider, Pharma, Payor, MedTech, Allied Health; protects HIPAA PHI, patient intake/referrals, lab results, clinical trials, and claims/coding.
5. **Manufacturing / Distribution SMB** (`Manufacturing_Distribution_SMB_Purview_One_Pager.pdf`, 2p): Chemicals, Agribusiness, Industrial Machinery, High Tech Electronics, Semiconductor; protects CAD drawings, BOMs, chemical formulations, SDS sheets, and OEM supplier specs.
6. **Nonprofit SMB (*New*)** (`Nonprofit_SMB_Purview_One_Pager_MVP.pdf`, 2p): Human & Social Services, Foundations, Faith-Based, Advocacy, International NGOs; protects donor records, grant agreements, vulnerable-beneficiary case files, and Form 990 audit workpapers.
7. **Professional Services SMB** (`Professional_Services_SMB_Purview_One_Pager.pdf`, 2p): Accounting & Tax, Management Consulting, IT Services, Outsourced Services, Architecture & Engineering; protects client diligence packs, tax workpapers, M&A memos, and legal privilege logs.

#### The 8-Label DEFEND-Aligned Sensitivity Taxonomy (Solving LOB Encryption Breakage)
All 7 Industry One-Pagers and the Guided Assistant standardize an **8-label sensitivity hierarchy** paired with a **30 / 60 / 90-Day Service Motion** (Day 30: 5-label Business Premium MVP; Day 60: Governed external sharing; Day 90: Purview Suite expansion with custom SITs/EDM). Crucially, labels **5** and **8** introduce explicit **`INTERNAL EXCEPTION`** sub-labels for Line-of-Business (LOB) workflows where Azure RMS encryption would break legacy ERP, EHR, SIS, MRP, or core banking integrations:
1. `PUBLIC`: No encryption; external sharing allowed.
2. `GENERAL`: No encryption; internal marking only; **default email label**.
3. `CONFIDENTIAL \ ALL EMPLOYEES`: Encryption + marking; no external sharing; **default file/site label**.
4. `CONFIDENTIAL \ SPECIFIC PEOPLE`: Named-user encryption for governed external partners/clients.
5. **`CONFIDENTIAL \ INTERNAL EXCEPTION`**: **Marking only (no encryption, no external sharing)** for LOB workflows where encryption breaks ERP/EHR/SIS/MRP integrations; requires documented business justification and **quarterly (90-day) review**.
6. `HIGHLY CONFIDENTIAL \ ALL EMPLOYEES`: Strong encryption + watermark; block external sharing (payroll, PHI, safeguarding, AML, trade secrets).
7. `HIGHLY CONFIDENTIAL \ SPECIFIC PEOPLE`: Explicit named-user encryption; SIT auto-labeling recommended (regulatory filings, M&A, legal holds).
8. **`HIGHLY CONFIDENTIAL \ INTERNAL EXCEPTION`**: **Marking only without encryption** where encryption breaks critical QMS, clinical compliance, or regulatory-reporting tooling; requires IT sign-off and **quarterly (90-day) justification audit**.

---

### 7.3 Asset 2 & Asset 3 Deep Dive: Guided Assistant (`v2.0.1572`) & 22-Workstream Purview SOW Generator

- **`microsoft/DataSecurityGuidedAssistant` (`aka.ms/DataSecurityAssistant`)**: Zero-backend static browser app (`v2.0.1572`) offering three guided flows (**Labeling Tool**, **DLP Tool**, **Combined Flow**) across 8 industries, 8 global regions, and 6 license tiers, toggling seamlessly between the **8-tier DEFEND model** and **4-tier simplified model** with Word/CSV export.
- **`microsoft/SOWGenerator` (`aka.ms/SOW-Generator`)**: Browser-based SOW builder covering **22 modular services**:
  - **Priority 1 — Foundation (Business Premium, 9 workstreams)**: Audit Logging, Label Taxonomy Design, Label Creation & Encryption, Label Policy Deployment, Mandatory/Default Labeling, End-User Training, SPO/OD Sensitivity Labels, Container Labels (Teams/SPO/M365 Groups), and EXO/SPO/OD DLP Policies.
  - **Priority 2 — Intermediate (1 workstream)**: Retention Policy for Exchange Online (expandable to SPO/OD/Teams).
  - **Priority 3 — Advanced & AI Guardrails (Purview Suite Add-on 🔒, 12 workstreams)**: Custom SITs/EDM, Client-Side Auto-Labeling, Service-Side Auto-Labeling, Label-Based Encryption/RMS, Trainable Classifiers, Content/Activity Explorer, On-Premises Purview Scanner, Double Key Encryption (DKE), MIP SDK/LOB Integration, Advanced Analytics, **Extended & AI Guardrails** (**DLP for Endpoints**, **DLP for Teams**, **DLP for Copilot [two dedicated rules—one for SITs and one for sensitivity labels—with prompt/response simulation testing]**, **DLP for Microsoft Edge / Inline Web Traffic [blocks sensitive data paste/upload into unmanaged AI apps like ChatGPT and Gemini]**, and **Activate DSPM**), plus **Managed Services** (30-Day Hypercare, Monthly Health Monitoring, Quarterly Policy Tuning, Incident Response).

---

### 7.4 Asset 4 & Asset 5 Deep Dive: 6-Workload Technical Deployment Guides (360 Pages) & PowerShell 7+ `SMBBestPracticeTool`

The archive `Best Practice Security Deployment Guides for SMB.zip` (`31.82 MB`) provides **6 step-by-step engineering implementation manuals totaling 360 pages**. Every guide follows a deterministic technical structure: `Prerequisites & RBAC Roles → Priority 1 (Must-do Baseline) → Priority 2 (Enhanced Protection) → Priority 3 (Strengthened Controls) → Advanced Security (Defender / Purview Suite Step-Up)`:

| Workload | Deployment Guide PDF | Pages | Updated | Core Technical Engineering Sections | DEFEND Tier Alignment |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **Workload 1** | **Identity Protection Best Practice Deployment** (`Identity Protection Best Practice Deployment_Final030626.pdf`) | **90p** | 2026-03-06 | • **Entra ID P1 Priority 1 & 2** (pp. 8–31): Break-glass accounts (FIDO2/Passkey), passwordless & number-matching MFA, 10 Zero Trust CA templates, SSPR + Password Writeback, Least Privilege RBAC/TAP<br>• **Entra ID P2 Risk & Governance** (pp. 32–70): Separate User Risk (`High`) & Sign-in Risk (`Med/High`) CA policies, **PIM Role & Group JIT activation**, Quarterly Access Reviews (`Auto-apply` remove), Entitlement Access Packages<br>• **Defender for Identity (MDI)** (pp. 71–87): DC/ADFS/ADCS sensor install, `Set-MDIConfiguration`, gMSA DSA, NNR (TCP 135/UDP 137/TCP 3389), Honeytokens | `DEFENDBase` → `DEFENDSecurity` |
| **Workload 2** | **Data Security Deployment Guide for Small Business** (`Data Security Deployment Guide for Small Business_Final.pdf`) | **92p** | 2026-06-24 | • **Priority 1 "Good"** (pp. 9–34): Unified Audit Log, Modern Label Groups, 8-Label priority ordering (`0..7`), SPO/OD encrypted co-authoring & `Execute-AzureAdLabelSync`, per-workload DLP in Simulation mode<br>• **Priority 2 "Better"** (pp. 35–41): Static vs **Adaptive Scope** retention policies, Inactive Mailboxes, **7-year default retention storage/eDiscovery risk mitigation (start at 2 years)**<br>• **Priority 3 "Best"** (pp. 42–90): Endpoint DLP, Teams DLP, **DLP for M365 Copilot (2-rule Prompt SIT + Label RAG restriction)**, **Edge Inline Web AI DLP**, Client/Service Auto-Labeling, Online-Only Encryption (`Allow offline access = Never`), Custom SITs/EDM, **DSPM for AI**, **IRM + Adaptive Protection** | `DEFENDBase` → `DEFENDCompliance` & Purview Tiers 1–3 |
| **Workload 3** | **Email & App + Collaboration Protection Best Practice Deployment** (`Email & App + Collaboration Protection Best Practice Deployment_Final030926.pdf`) | **52p** | 2026-03-16 | • **MDO Plan 1 Priority 1–3** (pp. 9–41): SPF (`-all`)/DKIM (2048-bit)/DMARC (`p=quarantine/reject` incl. parked domains), Standard/Strict Preset Policies, Anti-Phishing impersonation, Safe Links/Attachments (Email/SPO/OD/Teams global toggle), **Outbound external auto-forwarding disabled (`Off`)**, Teams 3rd-party storage block & **Teams ZAP**<br>• **MDO Plan 2 Collaboration Security** (pp. 42–51): Priority Account tagging, **7-payload Attack Simulation Training (incl. QR code phishing & OAuth consent grant)**, AIR auto-remediation, Threat Explorer | `DEFENDBase` → `DEFENDSecurity` |
| **Workload 4** | **Device Security Best Practice Deployment** (`Device Security Best Practice Deployment_Final030926.pdf`) | **51p** | 2026-03-16 | • **Defender for Business Priority 1 & 2** (pp. 8–43): Intune-MDE connector, `Tamper Protection = On`, Silent BitLocker (`TPM 2.0 + XTS-AES`), Automatic Attack Disruption, **ASR rules staged `Audit` (`RuleMode=2`) -> `Block` (`RuleMode=1`)** (LSASS dump, WMI persistence, vulnerable signed drivers), **MDE Machine Risk = `Clear (Secure)` wired to Intune & Entra CA**<br>• **Defender for Endpoint Plan 2** (pp. 44–51): **Explicit Tenant Subscription State switch (`Defender for Business -> MDE P2`)**, SOC RBAC Device Groups & 5 remediation levels | `DEFENDBase` → `DEFENDSecurity` |
| **Workload 5** | **Device Management Best Practice Deployment** (`Device Management Best Practice Deployment_Final030726.pdf`) | **40p** | 2026-03-16 | • **MDM vs MAM Architecture** (pp. 7–14): Corporate MDM vs BYOD MAM (**explicit retirement of Windows Information Protection [WIP] in favor of Purview MIP/Endpoint DLP**), **Default Compliance Policy hardened (`Mark devices with no compliance policy assigned = Not compliant`)**<br>• **Intune Priority 2 & 3** (pp. 15–38): Platform Enrollment Restrictions (blocking personal MDM enrollment), MAM Core Apps (block iCloud/iTunes backup & unmanaged copy), Windows 10/11 Compliance Policy, **Require MFA for Intune Enrollment CA Policy (`d4ebce55-015a-49b5-a083-c84d1797ae8c`)** | `DEFENDBase` |
| **Workload 6** | **SaaS Security Best Practice Deployment** (`SaaS Security Best Practice Deployment_Final030926.pdf`) | **35p** | 2026-03-16 | • **Shadow IT & Shadow AI Discovery** (pp. 9–18): 1-click **MDE + Defender for Cloud Apps integration** (scoring **31,000+ cloud apps across 90+ risk factors** without firewall appliances) + endpoint blocking (`Unsanctioned` -> MDE Network Protection)<br>• **OAuth App Governance & Cross-SaaS DLP** (pp. 19–34): **App Governance** auditing Highly Privileged/Overprivileged/Unused Graph API apps with `Disable app` remediation, SSPM, Cross-SaaS File DLP, Conditional Access App Control session proxy & Entra ID Username Enrichment | `DEFENDSecurity` → `DEFENDComplete` |

---

#### 7.4.1 Workload 1 Engineering Specification: Identity & Access Controls + Identity Protection (90 Pages)

1. **Entra ID P1 Baseline & Hardening Controls (pp. 8–31)**:
   - **Emergency Access (Break-Glass) Accounts (pp. 12–13)**: Create `>=2` cloud-only (`*.onmicrosoft.com`) permanent Global Administrator accounts decoupled from federated identity providers; enforce hardware **FIDO2 security keys or Passkeys**; exclude them from all Conditional Access (CA) policies and PIM; monitor sign-in logs (expected normal count = `0`).
   - **Phishing-Resistant Passwordless & Number Matching (pp. 14–20)**: Enable `Microsoft Authenticator = All users, Authentication mode = Any` (enabling passwordless phone sign-in and push number matching) and enforce mandatory MFA for Azure/Entra/Intune management portals (`aka.ms/mfaforazure`).
   - **Staged Deployment of 10 Built-in Zero Trust CA Templates (pp. 21–25)**:
     - **Immediate `On` (6 templates)**: `Require MFA for admins`, `Block legacy authentication`, `Require MFA for all users`, `Require MFA for guest access`, `Require MFA for Azure management`, `Block access for unknown or unsupported device platform`.
     - **Staged in `Report-Only` (4 templates)**: `Securing security info registration` (switch `On` after configuring Trusted Network Locations & Temporary Access Pass [TAP]), `No persistent browser session` (switch `On` after device enrollment), `Require approved client apps or app protection policies` (switch `On` after Intune MAM deployment), and `Require compliant or hybrid joined device or MFA for all users`.
   - **SSPR & Least Privilege Architecture (pp. 26–31)**: Enable `Self service password reset enabled = All` (with hybrid Password Writeback); enforce dedicated **unlicensed admin accounts** (preventing email phishing on privileged identities), require FIDO2 Authentication Strength for Global Admins, and enable the **Admin Consent Workflow** to gate third-party OAuth app permissions.

2. **Entra ID P2 Risk-Based Conditional Access & Identity Governance (Defender Suite, pp. 32–70)**:
   - **Decoupled User Risk vs. Sign-In Risk CA Policies (pp. 37–41)**: Never combine User Risk and Sign-in Risk in a single CA policy; create two separate policies that also cover passwordless users:
     - **User Risk CA Policy (pp. 37–38)**: Condition `User risk = High` $\rightarrow$ Grant `Require risk remediation` (automatically enforcing `Authentication strength [MFA]` + secure password reset) + Session `Sign-in frequency = Every time` (`Report-only` $\rightarrow$ `On`).
     - **Sign-In Risk CA Policy (pp. 39–41)**: Condition `Sign-in risk = High and Medium` $\rightarrow$ Grant `Require authentication strength (Multifactor authentication)` + Session `Sign-in frequency = Every time`.
   - **Privileged Identity Management (PIM for Entra Roles & PIM for Groups, pp. 44–55)**: Convert standing `Active` administrators to `Eligible` (retaining only break-glass accounts as permanent active); enforce `Activation maximum duration = 1–8 hours`, `On activation require Azure MFA or Entra CA authentication context`, `Require justification`, and `Require approval`; use **PIM for Groups** (`isAssignableToRole = true` cloud security groups) for bundled JIT elevation.
   - **Quarterly Access Reviews (pp. 56–62) & Entitlement Management Access Packages (pp. 63–70)**: Configure quarterly reviews across all M365 groups with Guests, sensitive security groups, enterprise apps, and PIM roles with **`Auto-apply results to resource = Enabled`**, **`If reviewers don't respond = Remove access`**, and **`No sign-in within 30 days`** decision helpers; bundle groups, apps, SharePoint sites, and **service principal / agent API permissions** into **Access Packages** with separate internal/external approval policies, mandatory justification, and **30- or 90-day automatic expiration (never indefinite)**.

3. **Microsoft Defender for Identity (MDI) Hybrid AD Protection (Defender Suite, pp. 71–87)**:
   - Deploy MDI sensors on all Domain Controllers, AD FS, AD CS, and Entra Connect servers (`Azure ATP sensor Setup.exe /quiet NetFrameworkCommandLineArguments="/q" AccessKey="<Key>"`); configure Windows Advanced Audit policies automatically in Sensor `v3.x` or via `Set-MDIConfiguration -Mode Domain -Configuration All` and `Test-MDIConfiguration` in `v2.x` (auditing Event IDs 8004 NTLM, 4662 DS access, 4728/4732/4756 group modifications, and SAM-R queries); use **Group Managed Service Accounts (`gMSA`)** for Directory Service Accounts; enable **Network Name Resolution (`NNR` over RPC TCP 135, NetBIOS UDP 137, RDP TCP 3389)** to correlate raw IP telemetry to domain hosts for `DCSync`, lateral movement path, and Kerberos ticket forgery detection; tag Honeytoken accounts.

---

#### 7.4.2 Workload 2 Engineering Specification: Data Security & Generative AI Guardrails (92 Pages + 7 Vertical Guides 14 Pages)

1. **Priority 1 ("Good") — Unified Audit, Modern Label Groups & Per-Workload Simulation DLP (pp. 9–34)**:
   - **Unified Audit Log Verification (pp. 9–12)**: Verify `Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled` returns `True` (`Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true`).
   - **Modern Sensitivity Label Scheme & Priority Ordering (pp. 13–21)**: Uses **Label Groups** (logical top-level containers with protection settings applied exclusively to sub-labels, default for new tenants Oct 1, 2025+) ordered strictly from `0` (least restrictive `Public`) to `7` (most restrictive `Highly Confidential`).
   - **Technical Mechanics of `INTERNAL EXCEPTION` Sub-Labels (#5 & #8, p. 15 & 7 Vertical Guides)**:
     - Applying AES-256 Azure RMS file encryption breaks headless enterprise batch pipelines (EHR/HL7 clinical parsers, core-banking/claims batch imports, CAD/PLM/MES manufacturing controllers, SIS student imports, EDI/ERP order sync) that cannot perform interactive MIP SDK token exchange.
     - **`CONFIDENTIAL \ INTERNAL EXCEPTION` (#5)** and **`HIGHLY CONFIDENTIAL \ INTERNAL EXCEPTION` (#8)** write persistent `MSIP_Label_<GUID>_Enabled=true` classification metadata and visual headers/footers/watermarks **with `Encryption = Disabled`**, while binding those exact label GUIDs in **Purview DLP, Endpoint DLP, Teams DLP, and DLP for M365 Copilot** to block external egress, block anonymous sharing, block unmanaged device copy, and exclude items from Copilot RAG grounding—paired with a mandatory 90-day exception review.
   - **SPO/OneDrive Encrypted File Co-Authoring & Container Sync (pp. 26–28)**: Enable `Process content in encrypted Office files for OneDrive and SharePoint` and run `Execute-AzureAdLabelSync` to enforce container-level privacy (`Private`), guest access restrictions, and unmanaged device blocks across Microsoft Teams, M365 Groups, and SharePoint sites.
   - **Per-Workload Custom DLP Policies in Simulation Mode (pp. 29–34)**: Deploy separate Custom DLP policies for **Exchange email**, **SharePoint sites**, and **OneDrive accounts** (`Block only people outside your organization` for `Confidential \ All Employees` and higher) in **Simulation mode** (`Turn the policy on if it's not edited within 15 days of simulation`).

2. **Priority 2 ("Better") — Static vs. Adaptive Scope Retention & the 7-Year Default Risk Mitigation (pp. 35–41)**:
   - Use **Adaptive Scopes** (dynamic Entra user attribute or SPO site property queries for Legal/Finance/Executives) and **Inactive Mailboxes** for departed employees.
   - **Critical Engineering Guardrail on the 7-Year Template Default (p. 40)**: Purview retention templates default to **7 years**, which causes severe Exchange/SharePoint storage quota exhaustion and expands legal eDiscovery exposure. Start standard email retention at **2 years (`Retain only`)**, scoping 7-year retention strictly to regulated workloads via Adaptive Scopes.

3. **Priority 3 ("Best") — Purview Suite Expansion, Dual Copilot/Edge AI Guardrails & Adaptive Protection (pp. 42–90)**:
   - **Endpoint DLP (pp. 43–47) & Teams DLP (pp. 48–52)**: Audit or block `Copy to clipboard`, `Copy to a removable USB device`, `Copy to a network share`, and `Print` on Windows/macOS endpoints; block external guest sharing of sensitive labels/SITs in Teams chats and channels.
   - **DLP for Microsoft 365 Copilot & Copilot Chat Dual-Rule Architecture (pp. 53–57)**:
     - Scope a dedicated Custom DLP policy to **`Microsoft 365 Copilot and Copilot Chat`** with two orthogonal rules:
       - **Rule 1 (Prompt SIT Gate)**: Detects regulated SITs (Credit Card, Bank Account, SSN/National ID) in user prompts.
       - **Rule 2 (Sensitivity Label RAG Grounding Gate)**: Matches `Confidential \ Specific People` and `Highly Confidential \ *` (or `Confidential \ All Employees` for high-security scopes) with action **`Restrict Copilot from processing content`**, stripping labeled files from Graph semantic/RAG grounding at inference time.
   - **DLP for Microsoft Edge / Inline Web Traffic (p. 72 & SOW Priority 3)**: Blocks pasting or uploading sensitive content into unmanaged generative AI domains (ChatGPT, Gemini, DeepSeek) in Edge for Business.
   - **Client/Service Auto-Labeling (pp. 58–61), Online-Only Encryption (`Allow offline access = Never`, pp. 62–63) & Custom SITs (pp. 64–67)**: Enforce real-time Entra token validation on every file open (`Allow offline access = Never`) and build Custom SITs using RegEx (`EMP-[0-9]{6}`), Keyword lists/dictionaries (`Project Falcon`), checksum Functions, 300-character proximity windows, EDM, and Document Fingerprinting.
   - **DSPM for AI (pp. 68–73) & Insider Risk Management + Adaptive Protection (pp. 74–86)**: Enable one-click DSPM weekly SharePoint oversharing assessments for Copilot; enable IRM `Data leaks` + **Adaptive Protection Quick Setup** (72-hour baseline) to dynamically classify users into `Elevated`, `Moderate`, or `Minor` risk tiers and automatically enforce 3 linked policies (Teams+Exchange DLP, Endpoint DLP where `Elevated = Block`, and Entra ID P2 Conditional Access).

---

#### 7.4.3 Workload 3 Engineering Specification: Email, App & Collaboration Protection (52 Pages)

1. **Defender for Office 365 Plan 1 Hardening (pp. 9–41)**:
   - **DNS Authentication Triad (pp. 9–14)**: Configure `SPF` (`-all`), `DKIM` (2048-bit CNAME key rotation at `security.microsoft.com/dkimv2`), and `DMARC` (`p=quarantine; pct=100` $\rightarrow$ `p=reject`) across all active and **parked domains**.
   - **Standard / Strict Preset Security Policies & Anti-Phishing (pp. 15–20)**: Enforce EOP anti-spam/malware, MDO Anti-Phishing (executive/domain impersonation protection, mailbox intelligence, spoof intelligence), **Safe Links** (real-time URL detonation across Email, Teams, and Office apps), and **Safe Attachments** (`Dynamic Delivery` or `Block`).
   - **Outbound External Auto-Forwarding Block & Drift Analysis (pp. 24–28)**: Set `Outbound spam filter policy (Default) -> Automatic forwarding rules = Off — Forwarding is disabled` to block attacker inbox-rule exfiltration; run the **Configuration Analyzer** to detect drift against Standard/Strict baselines.
   - **Microsoft Teams Hardening & Zero-Hour Auto-Purge (ZAP for Teams, pp. 29–37)**: Disable third-party cloud storage (`Citrix/DropBox/Box/Google Drive/Egnyte = Off`) in Teams Admin Center; enable **Zero-hour auto purge (ZAP) for Teams** at `security.microsoft.com/securitysettings/teamsProtectionPolicy` to retroactively quarantine malicious messages/files in Teams chats; enable **`Turn on Defender for Office 365 for SharePoint, OneDrive, and Microsoft Teams`** under Safe Attachments global settings.
2. **Defender for Office 365 Plan 2 Collaboration Security (Defender Suite, pp. 42–51)**:
   - Configure **Priority Account Protection** for executive/finance targets; schedule **Attack Simulation Training** across all 7 social engineering techniques (*Credential Harvest*, *Malware Attachment*, *Link in Attachment*, *Link to Malware*, *Drive-by URL*, *OAuth Consent Grant*, *How-to Guide*, including **QR Code Phishing / Quishing**); enable **Automated Investigation & Response (AIR)** auto-remediation playbooks and **Threat Explorer** real-time hunting.

---

#### 7.4.4 Workload 4 Engineering Specification: Device Security & EDR/ASR Closed Loop (51 Pages)

1. **Defender for Business Hardening & Automatic Attack Disruption (pp. 8–43)**:
   - **Intune-MDE Connector & Tamper Protection (pp. 10–19)**: Connect Windows/Android/iOS in Intune Endpoint Security, enforce `Tamper Protection = On`, `Cloud-delivered protection level = High`, and `Block at First Sight (BAFS)`.
   - **Silent BitLocker Encryption & Automatic Attack Disruption (pp. 24–29)**: Configure Intune Disk Encryption with `Require Device Encryption = Enabled` and `Allow Warning For Other Disk Encryption = Disabled` (silent TPM 2.0 + XTS-AES encryption); rely on built-in **Automatic Attack Disruption** to isolate compromised hosts and suspend compromised accounts at the XDR graph layer.
   - **Staged Attack Surface Reduction (ASR) Rules (`Audit` $\rightarrow$ `Block`, pp. 32–38)**: Stage ASR rules in `Audit` (`RuleMode=2`), review the `ASR Rules Report`, and transition to `Block` (`RuleMode=1`), mandating Block on the 3 Standard Protection rules: (1) *Block credential stealing from the Windows local security authority subsystem (`lsass.exe`)*, (2) *Block persistence through WMI event subscription*, and (3) *Block abuse of exploited vulnerable signed drivers*.
   - **Closed-Loop MDE Machine Risk $\rightarrow$ Intune Compliance $\rightarrow$ Entra CA Gate (pp. 39–43)**: Set `Require the device to be at or under the machine risk score = Clear (Secure)` in Intune Compliance wired to `Require device to be marked as compliant` in Entra CA.
2. **Defender for Endpoint Plan 2 Tenant Subscription State Transition (Defender Suite, pp. 44–51)**:
   - **Critical Mixed-License Portal Quirk (pp. 46–47)**: Tenants holding both Business Premium (Defender for Business) and MDE Plan 2 licenses **default to the simplified Defender for Business portal experience**. Engineers must verify or request the switch at `Microsoft Defender Portal > System > Settings > Endpoints > General > Subscription state = Microsoft Defender for Endpoint Plan 2` to unlock **SOC RBAC Device Groups** (`security.microsoft.com/securitysettings/endpoints/machine_groups`) and the 5 automated remediation tiers (`No automated response` through `Full — remediate threats automatically`).

---

#### 7.4.5 Workload 5 Engineering Specification: Device Enrollment & Mobile Application Management (40 Pages)

1. **MDM vs. MAM Architecture & WIP Retirement (pp. 7–14)**:
   - Route corporate-owned endpoints through **MDM** (Windows Autopilot, Apple ABM/APNs, Android Enterprise Managed Google Play) and personal BYOD devices through **MAM App Protection Policies** without full device enrollment.
   - **Windows Information Protection (WIP) Retirement Note (p. 10)**: WIP is officially retired; migrate Windows data protection to **Purview Information Protection + Purview Endpoint DLP**.
   - **Default Compliance Policy Hardening (p. 14)**: Set `Compliance policy settings -> Mark devices with no compliance policy assigned = Not compliant` to prevent un-evaluated devices from bypassing Conditional Access.
2. **Enrollment Restrictions, MAM Data Boundaries & Enrollment MFA (pp. 15–38)**:
   - Block personal device MDM enrollment (`Personally-owned = Block`) on platforms governed by MAM; enforce MAM Core Apps protections (`Backup org data to iTunes and iCloud backups = Block`, `Send org data to other apps = Policy managed apps`, `Save copies of org data = Block`); enforce Windows 10/11 Compliance (`Require BitLocker`, `Require Secure Boot`, `Require code integrity`, `TPM`, `Firewall`, `Defender Antimalware`); and create a dedicated **Require MFA for Intune Enrollment Conditional Access Policy** targeting the `Microsoft Intune Enrollment` app (`App ID: d4ebce55-015a-49b5-a083-c84d1797ae8c`, `Sign-in frequency = Every time`).

---

#### 7.4.6 Workload 6 Engineering Specification: SaaS Security & OAuth App Governance (35 Pages)

1. **MDE + Defender for Cloud Apps (MDA) Agentless Shadow IT & Shadow AI Discovery (pp. 9–18)**:
   - Enable **`Microsoft Defender for Cloud Apps = On`** under `Settings > Endpoints > General > Advanced features` to stream endpoint network telemetry directly into MDA, scoring **>31,000 cloud apps across >90 risk factors** without firewall log collectors; enable **Cloud Discovery Anomaly Detection** and tag risky apps/GenAI tools as **`Unsanctioned`** so MDE Network Protection blocks domain access at the endpoint NIC layer.
2. **OAuth App Governance, SSPM & Session Proxy Controls (pp. 19–34)**:
   - Activate **App Governance** (`Settings > Cloud Apps > App Governance`, up to 10h graph initialization) to audit `Highly Privileged`, `Overprivileged`, and `Unused` Graph API OAuth apps and Purview-labeled data access, configuring custom OAuth policies with **`Disable app`** remediation (staged in Audit mode); connect SaaS APIs for **SSPM**, enable **Cross-SaaS File DLP** (`Enable file monitoring`), enforce real-time **Conditional Access App Control Session Policies**, enable **Entra ID Username Enrichment**, and run a **Daily / Weekly / Monthly SecOps** review cadence.

---

#### 7.4.7 Stage 5 PowerShell 7+ `SMBBestPracticeTool` & Configuration Drift Architecture (`aka.ms/Deploy-Scripts`)

- Enforces **PowerShell 7+ (`pwsh.exe`)** while isolating legacy SharePoint cmdlets in a hidden PS 5.1 subprocess (`-UseWindowsPowerShell`); supports multi-tenant **GDAP delegated administration** (`-DelegatedOrganization`), `-WhatIf` dry runs, post-write readback verification, and **HTML + JSON run reports**.
- Ships 4 workload toolkits: `Products/Purview` (includes **Deployment Plans** for pre-deployment intent, **Tenant Validation Reports** for field-level object drift detection, the **Day-30 DLP Simulation Exit Runbook**, and the 7-year retention risk note), `Products/Entra` (deploys **13 Conditional Access JSON templates in Report-Only mode by default** with permanent Global Admin break-glass verification), `Products/Intune` (6 baseline tasks with `-IncludeHighRisk` gate), and `Products/Defender` (read-only preflight + pilot-gated **ASR Audit configuration**).

---

## 8. Architectural Bridge: Mapping M365 DEFEND & SMB Toolkit to Cloud-Native Agentic AI Security

![Purview 4-Tier to Cloud-Native Agentic AI Security Bridge](./assets/purview-ai-bridge.svg)

| Security Control Plane | M365 Tenant Controls (`DEFEND Playbook` + `SMB Partner Toolkit`) | Cloud-Native Agent Runtime Controls (`Pillar 01 Azure Agent Infra`) | Unified Zero-Trust Objective |
| :--- | :--- | :--- | :--- |
| **1. Identity & Least Privilege** | **Entra ID P1/P2**: 13 Report-Only CA templates, sign-in/user risk CA, **PIM JIT elevation**, Access Reviews (`S01–S03`) | **Microsoft Entra Agent ID**: On-Behalf-Of (OBO) dual attribution (User + Agent Identity), short-lived tokens & workload federation | Prevent credential theft, lateral movement & confused-deputy agent escalation |
| **2. Execution & Compute Isolation** | **Intune Plan 1 + Defender for Business / MDE P2**: Device compliance, BitLocker, ASR rules, behavioral EDR (`B04–B07`, `S04–S06`) | **AKS Kata / Confidential Containers (SEV-SNP) & E2B Firecracker microVMs**: Hardware-virtualized kernel isolation + **Tetragon eBPF** enforcement | Isolate untrusted code execution and tool calls; prevent container escape |
| **3. Dual AI & Data Guardrails** | **Purview Tier 3 (`Data Control`) + SOW Priority 3**: 8-Label taxonomy (with LOB exception sub-labels), **DLP for Copilot (2-rule sim)**, **Edge Inline Web DLP (ChatGPT/Gemini)**, **Activate DSPM** | **Azure APIM AI Gateway + Purview SDK + Web IQ**: Inline prompt/response redaction, MCP/A2A payload inspection & malicious domain circuit breakers | Stop internal Copilot oversharing AND external Shadow AI exfiltration / indirect prompt injection |
| **4. SIEM/SOAR & AI-Assisted SOC** | **DEFENDExtend (`E01–E09`)**: Noise-tuned **Microsoft Sentinel + Defender XDR + Security Copilot** after completing `DEFENDComplete` | **Azure Monitor + Sentinel + Prometheus/Grafana**: Agent trace telemetry, microVM lifecycle metrics, APIM gateway logs & automated containment playbooks | High-signal cross-plane detection and automated SOAR containment without alert fatigue |

---

## 9. Reproducibility & Verification Commands

```powershell
# 1. Run the deterministic unit test suite (7 tests verifying slide/criteria counts, 41 capabilities, Slide 40 lock & SMB Toolkit catalog)
python -m unittest discover -s docs\research\defend-partner-playbook\simulator -p "test_*.py" -v

# 2. Regenerate verifier-summary.json, report.json, evidence.json, CSVs, and bilingual 7-card HTML decks
python docs\research\defend-partner-playbook\simulator\generate_artifacts.py
```
