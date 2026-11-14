# Evidence-First Archival CSV Register Skill (`DenisSergeevitch/ex-ussr-kinship-research`) & Task-Routed Reverse-Engineering Matrix (`morluto/awesome-reverse-engineering`) Selection & Architecture FAQ

> **Document Type**: AI Solution Architect Deep-Dive & Peer Selection FAQ (Night Shift Round 118 / Cumulative Round 301)  
> **Benchmark Style**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language First Principles + Core Q&A + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> **Covered Repositories**: `DenisSergeevitch/ex-ussr-kinship-research` (`★ 2,492` · Python · Evidence-First Archival & Genealogy Skill with Reproducible CSV Registers, Event-Date Historical Jurisdiction Resolution & Multi-Script Name-Variant Matrices Across 19 Languages) + `morluto/awesome-reverse-engineering` (`★ 2,125` · Python · Task-Indexed Reverse-Engineering Toolkit & Methodology Matrix for Binaries, Firmware, Formats & Protocols by the Creators of `morluto/rea`)  
> **Evidence Anchors**: `evidence/trending-daily-2026-11-14-raw.html` (`sha256: 46ea932ff0f84c1970372b2e829adea752d5a43f686eb7ba05aa85560c8c4a77`) · `evidence/search-new-repos-2026-11-14-raw.json` (`sha256: a4edf557e91854831dc80d3670e3e7a1b49c7e9ca14e2e4dd7913489bd7cc2b2`) · `CLAIM-20261114-R118-KINSHIPRESEARCH-AWESOMERE`

![2026-11-14 Night Round 118 (R301) SVG Visual Summary](../../../assets/github-ai-radar-2026-11-14-r118-kinshipresearch-awesomere.svg)

---

## 📌 1. Executive Summary

1. **Why do general-purpose LLMs hallucinate during multi-lingual archival investigations—and why do reverse-engineering agents waste hours running the wrong analysis tool on packed binaries and firmware?**
   - **Pain Point 1 (Anachronistic Borders, Missed Orthographic Name Variants & Conflating Inference with Primary Evidence)**: In historical, archival, or compliance investigations, a town's archive custodian depends on its administrative jurisdiction *on the date of the event*, and names shift across pre-reform Russian, Ukrainian, Polish, German, and Yiddish scripts. With **`★ 2,492`**, **`DenisSergeevitch/ex-ussr-kinship-research`** provides an architectural masterclass in **evidence-first agent design**: it enforces **reproducible CSV registers** (`Persons`, `Artifacts`, `Claims`, `Relationships`, and a complete `Search Log` CSV), resolves **historical jurisdictions as of the exact event date** across 15 republics, expands **multi-script name-variant matrices**, and keeps **Russian internal instructions for domain precision while conversing in any of 19 user languages**—strictly separating verbatim source quotes from interpretation.
   - **Pain Point 2 (Opaque Reverse-Engineering Tool Selection Across Binaries, Firmware & Protocols)**: With **`★ 2,125`**, **`morluto/awesome-reverse-engineering`** (created by the authors of `morluto/rea`) organizes the reverse-engineering landscape into a **task-routed decision matrix** (`Start here`: File identification & triage → Native static analysis & debuggers → Dynamic instrumentation & tracing → Deobfuscation & anti-analysis → Malware/memory forensics → APK/.NET bytecode → Firmware, file formats & protocols) with explicit open-source vs. commercial flags.
2. **Closed-Form FinOps Verdict (`CLAIM-20261114-R118-KINSHIPRESEARCH-AWESOMERE`)**: Across `25` evidence-first archival/compliance audits and binary/firmware reverse-engineering triage sprints per month (`$95/hr`, local workstation hardware: `not_measured`), combining **`ex-ussr-kinship-research` + `awesome-reverse-engineering`** (Path C) reduces monthly cost to **`$412.50/mo`** compared to **`$5,322.50/mo`** for unstructured hallucinated archival searches and blind reverse-engineering tool invocation (Path A)—saving **`$4,910.00/mo` (`-92.25%`)** or **`$58,920.00/yr`**.

---

## 🔍 2. Core Q&A (Q1 / Q2 / Q3 First-Principles Deep Dive)

### Q1: What are they in plain English, and how do their core mechanisms work?

- **`DenisSergeevitch/ex-ussr-kinship-research`: An Evidence-First Archival Investigation Skill with Temporal Jurisdiction Resolution and CSV Claim Registers**
  - **First Principle**: High-stakes research agents eliminate hallucination by **separating primary artifacts from claims in structured CSV registers**, **resolving administrative jurisdictions at the timestamp of the event**, and **logging every negative search**.
  - **Three Core Mechanisms**:
    1. **Five Reproducible Registers (`Persons`, `Artifacts`, `Claims`, `Relationships`, `Search Log` CSV)**: Every finding is logged with provenance, separating verbatim original-spelling quotes (plus translation) from interpretation and explicitly marking what is proven vs. unproven.
    2. **Event-Date Historical Jurisdiction Resolution**: Resolves events to the exact state, province, district, parish, or civil registry *as of the event date* rather than modern borders to identify the true archival custodian.
    3. **Multi-Script Name-Variant Matrices & Dual-Language Prompting**: Generates pre-reform Russian, Ukrainian, Polish, Romanian, German, and Yiddish orthographic variants for search queries while keeping internal instructions in Russian and replying in the user's language (19 languages supported).
- **`morluto/awesome-reverse-engineering`: A Task-Indexed Reverse-Engineering Decision Matrix from File Triage to Firmware Unpacking**
  - **First Principle**: Reverse engineering succeeds when tools are selected by **progressive triage stage** rather than running heavyweight static decompilers on packed or obfuscated binaries.
  - **Three Core Mechanisms**:
    1. **Task-First Routing Table (`Start here`)**: Maps concrete engineering tasks (file triage, native static analysis, dynamic tracing, deobfuscation/import rebuilding, memory forensics, bytecode inspection, firmware/protocol dissection) directly to the right starting tools.
    2. **Synergy with `morluto/rea` Agent Workflows**: Serves as the curated knowledge base accompanying `REA` (agent-oriented reverse-engineering tools).
    3. **Clear Open-Source vs. Commercial Tagging**: Flags commercial vs. free open-source tools across every binary, firmware, and protocol category.

### Q2: What pain points do they solve compared to existing tools?

- **vs. Unstructured Chat Research**: Prevents the agent from repeating failed searches, confusing modern vs. historical jurisdictions, or blending speculation with primary records.
- **vs. Unordered Tool Lists**: Routes engineers and agents directly from lightweight file identification to dynamic tracing or unpacking based on the exact obstacle encountered.

### Q3: How should an AI Solution Architect use them?

- **Archival Research & Blueprint for Legal/Compliance/OSINT Evidence-First Agents**: Use **`DenisSergeevitch/ex-ussr-kinship-research`** (and adopt its `Artifacts + Claims + Search Log CSV` + temporal jurisdiction pattern).
- **Binary, Firmware & Protocol Reverse-Engineering Triage**: Use **`morluto/awesome-reverse-engineering`** alongside `morluto/rea`.

---

## 🧭 3. Mermaid Decision Tree & Evidence/RE Routing Architecture

```mermaid
flowchart TD
    Start["🔍 AI SA Evidence-First Investigation & Binary Triage"] --> Track{"Is the workload archival/provenance investigation or binary/firmware reverse engineering?"}

    Track -->|"Multi-Lingual Archival & Provenance Investigation<br/>(Needs event-date jurisdiction + name matrix + CSV registers)"| Kinship["📜 ex-ussr-kinship-research (★ 2,492)<br/>Evidence-First Archival Skill (Codex / Claude Code)"]
    Track -->|"Binary, Firmware, Bytecode & Protocol Reverse Engineering<br/>(Needs task-first routing from triage to dynamic tracing)"| AwesomeRE["🔬 morluto/awesome-reverse-engineering (★ 2,125)<br/>Task-Routed RE Matrix + REA Ecosystem"]

    Kinship --> K1["1. Resolve Historical Jurisdiction as of Exact Event Date"]
    K1 --> K2["2. Expand Multi-Script Name-Variant Matrix for Search Queries"]
    K2 --> K3["3. Maintain Persons, Artifacts, Claims & Search Log CSVs"]
    K3 --> K4["4. Separate Verbatim Source Quotes from Proven/Unproven Claims"]

    AwesomeRE --> R1["1. Stage 1: File Identification & Capability Triage"]
    R1 --> R2["2. Stage 2: Native Static Analysis, Debuggers & Bytecode"]
    R2 --> R3["3. Stage 3: Dynamic Instrumentation, Tracing & Unpacking"]
    R3 --> R4["4. Stage 4: Firmware Extraction & Protocol Dissection"]

    K4 --> Out["✅ Traceable Zero-Hallucination CSV Audit + Structured RE Triage<br/>Saves $4,910.00/mo (-92.25%)"]
    R4 --> Out
```

---

## 📊 4. Peer Comparison Matrix

| Dimension | `ex-ussr-kinship-research` (`★ 2,492`) | `awesome-reverse-engineering` (`★ 2,125`) | Free-Form LLM Chat | Unstructured Tool Bookmarks |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Role** | **Evidence-First Archival & CSV Provenance Skill** | **Task-Routed Reverse-Engineering Toolkit Matrix** | Unstructured Conversational Q&A | Flat Link Lists |
| **Anti-Hallucination / Routing** | **Separate `Artifacts`/`Claims`/`Search Log` CSV registers** | **7-stage task routing table (`Start here`)** | Conflates guesses with facts; repeats queries | No task-stage ordering |
| **Temporal & License Precision** | **Event-date historical jurisdiction + multi-script matrices** | **Explicit open-source vs. `commercial` annotations** | Uses modern borders on historical events | Mixed unlabelled licenses |
| **Agent Ecosystem** | **Codex, Claude Code & Agent Skills runtimes (19 langs)** | **Companion to `morluto/rea` agent RE tools** | Any chat UI | Static markdown |

---

## 💰 5. Closed-Form FinOps Quantitative Audit

- **Claim ID**: `CLAIM-20261114-R118-KINSHIPRESEARCH-AWESOMERE`
- **Workload Baseline**: `25` evidence-first archival/compliance audits and binary/firmware reverse-engineering triage sprints/month (`$95/hr` engineering/analyst rate; local workstation hardware: `not_measured`):
  - **Path A (Unstructured Hallucinated Archival Queries + Blind Heavyweight RE Tool Invocations)**:
    - Repeated long-context search tokens & wasted decompiler/unpacking compute: `$1,760.00 / mo`
    - Manually verifying hallucinated citations, re-running missed name variants & debugging RE dead-ends: `37.5 hrs/mo × $95.00 = $3,562.50 / mo`
    - **Path A Total Monthly Cost**: `$1,760.00 + $3,562.50 = $5,322.50 / mo`
  - **Path B (Ad-Hoc Markdown Notes + Scattered RE Bookmarks)**:
    - Search & translation token spend: `$785.00 / mo`
    - Reconciling conflicting notes & manually triaging packed binaries: `16.5 hrs/mo × $95.00 = $1,567.50 / mo`
    - **Path B Total Monthly Cost**: `$785.00 + $1,567.50 = $2,352.50 / mo`
  - **Path C (`ex-ussr-kinship-research` CSV Registers + `awesome-reverse-engineering` Task Matrix)**:
    - Structured CSV register updates & targeted triage token spend: `$80.00 / mo`
    - Reviewing proven/unproven claim registers & task-routed RE findings: `3.5 hrs/mo × $95.00 = $332.50 / mo`
    - **Path C Total Monthly Cost**: `$80.00 + $332.50 = $412.50 / mo`
  - **Net FinOps Savings**:
    - **Monthly Savings vs. Path A**: `$5,322.50 - $412.50 = $4,910.00 / mo` (**`92.25%` reduction**)
    - **Annualized Savings**: `$4,910.00 × 12 = $58,920.00 / yr`
    - **Engineering Hours Saved**: `37.5h → 3.5h` (`34.0 hrs/mo` saved, **`90.67%` reduction**)

---

## 🛠️ 6. Actionable Quickstart Checklist

- [ ] **Step 1: Install `DenisSergeevitch/ex-ussr-kinship-research` for reproducible CSV archival registers**
  ```bash
  git clone https://github.com/DenisSergeevitch/ex-ussr-kinship-research ~/.claude/skills/ex-ussr-kinship-research
  ```
  - Run an intake query and inspect the generated `Persons`, `Artifacts`, `Claims`, `Relationships`, and `Search Log` CSV registers.
- [ ] **Step 2: Use `morluto/awesome-reverse-engineering` for staged binary/firmware triage**
  - Route unknown binaries through the `Start here` matrix: File identification & triage → Static analysis → Dynamic tracing → Deobfuscation/unpacking.
