# 2% Context Ledger Surviving `/clear` (`adamoelz/gemkeeper`), Claude Orchestrator + Local GPU OpenCode Plugin (`a-schaefers/claudes-workbench`), KMS-Backed LLM Watermark Control Plane (`Vecshield/Markwright`) & `N+K` Selective Human-Assisted Judge (`mczlwl/Askjudge`) Selection FAQ

> **Document Type**: AI Solution Architect Enterprise Selection & Integration Guide (2026-11-19 Night Shift · Round 27 / Cumulative Round 551)  
> **Benchmark Style**: `docs/components/ib-vs-ethernet-roce-selection-faq.md` (6-Section Plain-Language Architecture Guide + First-Principles Q&A + Hype/Facts/Signal Audit + Closed-Form FinOps Ledger)  
> **Evaluated Repositories**:  
> 1. **`adamoelz/gemkeeper`** (`★ 10`, `created=2026-11-16`, `2 forks`, Shell, MIT): **Claude Code plugin recording the 2% of mission-critical context while the model still remembers it** so sessions survive `/clear` and compaction at full quality  
> 2. **`a-schaefers/claudes-workbench`** (`★ 9`, `created=2026-11-16`, `1 fork`, Python, MIT): **Claude orchestrates; a local OpenCode LLM on your GPU writes the code**—connected seamlessly inside a standard Claude Code session  
> 3. **`Vecshield/Markwright`** (`★ 9`, `created=2026-11-16`, `1 fork`, Python 3.11+, 110+ tests across 3 tiers, Apache-2.0): **Open-source control plane for LLM text watermarking (`SynthID-Text` / `KGW`)** providing model-version registries, KMS/Vault key custody with rotation, and calibrated statistical evidence  
> 4. **`mczlwl/Askjudge`** (`★ 6`, `created=2026-11-14`, `1 fork`, Python, MIT): **Selective human assistance for batch LLM-as-a-Judge workflows (`N + K` model calls)**—finishing clear cases immediately while asking one focused human question on `K` ambiguous cases  
> **Accounting Scope Note**: Only software API/SaaS spend and engineering labor TCO are modeled; base workstation hardware capEx is explicitly marked `not_measured`, and Track B `stars_today` is explicitly marked `not_measured`.

---

## 📌 1. Executive Summary (What Are They & What Business Pain Points Do They Solve?)

In **2026-11-19 Night Round 27 (Cumulative Round 551)**, we solve four critical enterprise LLM engineering and governance bottlenecks across context compaction amnesia, hybrid cloud/local coding economics, cryptographic text watermark operations, and human-in-the-loop evaluation scaling:
1. **Pain Point A (Long Claude Code sessions accumulate 98% noise—old logs, dead ends, verbose tool outputs—forcing engineers to choose between paying for bloated 180k-token turns until auto-compaction causes amnesia or running `/clear` and losing critical architectural decisions)**: **`adamoelz/gemkeeper` (`★ 10`, MIT)** continuously writes the **2% of mission-critical context** into a tiny persistent ledger *while Claude still remembers it*, enabling engineers to `/clear` bloated sessions at will and resume at full quality.
2. **Pain Point B (Using frontier cloud Claude tokens to write every line of boilerplate code is expensive, while switching manually to a separate local GPU coding window breaks orchestration context)**: **`a-schaefers/claudes-workbench` (`★ 9`, MIT)** connects Claude Code directly to a local GPU LLM running via **OpenCode**—letting frontier Claude handle architecture and orchestration while offloading heavy code generation to your local GPU inside the same session.
3. **Pain Point C (Models already ship with `SynthID-Text` or `KGW` watermarking, but enterprises lack the operational control plane to track which model version and key marked a document, rotate keys without breaking historical verifications, and report matches with calibrated false-positive rates)**: **`Vecshield/Markwright` (`★ 9`, Apache-2.0)** provides that missing control plane ("Evidence, not verdict"), wrapping published watermarking schemes and KMS/Vault primitives with 110+ tests across 3 tiers.
4. **Pain Point D (In batch LLM-as-a-Judge runs of `N` cases, ~85% are clear-cut while ~15% (`K` cases) depend on unstated human preferences—causing pure-automated judges to guess wrong and 100%-human review to bottleneck)**: **`mczlwl/Askjudge` (`★ 6`, MIT)** runs concurrent initial judgments across all `N` cases, completes clear cases immediately, and asks a human **one focused question** only for the `K` cases flagged with `needs_human=true` before issuing the final judgment (`N + K` total model calls), without altering your custom output schema.

---

## 💬 2. Architect First-Principles Q&A (Q1–Q3 Deep Dive)

### Q1: Why does `adamoelz/gemkeeper`'s "capture the 2% while fresh + proactive `/clear`" beat reactive auto-compaction?
* **Incremental Signal Extraction vs. Late Lossy Summarization**: Auto-compaction summarizes an already-polluted 180k-token window after attention degradation has set in. Capturing invariants incrementally keeps the active context window small, fast, and cheap.

### Q2: Why does `Vecshield/Markwright` explicitly state "Not an AI detector — Evidence, not verdict"?
* **Cryptographic Keyed Provenance vs. Uncalibrated Classifier Guessing**: Post-hoc "AI detectors" guess on arbitrary unwatermarked text with high false positives. `Markwright` verifies keyed watermarks (`SynthID-Text` / `KGW`) against a versioned KMS key registry and reports calibrated statistical p-values/FPRs.

### Q3: How does `mczlwl/Askjudge` preserve arbitrary downstream evaluation schemas while adding human-in-the-loop routing?
* **Out-of-Band Control Metadata (`needs_human` + `question`)**: It treats the judge's domain verdict/score string as completely opaque and inspects only the control fields, making it a drop-in upgrade for any existing evaluation prompt.

---

## 🧭 3. Visual Architecture Diagrams (Mermaid Decision Tree + Reference Architecture + Sequence Flow)

### 3.1 Enterprise Selection Decision Tree

```mermaid
flowchart TD
    Start["Enterprise Context Hygiene, Hybrid GPU Coding, Watermarks & Judge Selection (R551)"] --> Need{"Primary Bottleneck?"}
    Need -->|Preserve the 2% Critical Context Across /clear & Compaction| Gemkeeper["Choose adamoelz/gemkeeper (MIT)<br/>(Always-Current Micro-Ledger Surviving /clear)"]
    Need -->|Pair Cloud Claude Orchestration w/ Local GPU OpenCode Coding| Workbench["Choose a-schaefers/claudes-workbench (MIT)<br/>(In-Session Claude Planner + Local OpenCode Coder)"]
    Need -->|Operate SynthID/KGW Watermarks w/ Key Rotation & Calibrated FPR| Markwright["Choose Vecshield/Markwright (Apache-2.0)<br/>(KMS Key Custody + Model Registry + Statistical Evidence)"]
    Need -->|Scale Batch LLM-as-a-Judge w/ Selective Human Context (N+K)| AskJudge["Choose mczlwl/Askjudge (MIT)<br/>(Clear Cases Auto-Finish + 1 Question per Ambiguous Case)"]
```

---

## 📊 4. Comparative Selection Matrix (Open Source vs. Competing OSS vs. Managed Cloud PaaS)

| Evaluation Dimension | Path A: Bloated 180k Sessions + All-Cloud Boilerplate Coding + Unmanaged Watermark Keys + 100% Manual Eval Review | Path B: Manual Markdown Handoffs + Separate Local LLM Windows + Black-Box AI Detectors | **Path C (Recommended): `gemkeeper` + `claudes-workbench` + `Markwright` + `Askjudge`** |
| :--- | :--- | :--- | :--- |
| **Long-Session Context & Cost** | ❌ Re-billing 180k tokens/turn until compaction amnesia | ⚠️ Manual handoff notes before `/clear` miss subtle invariants | ✅ **`gemkeeper` logs the 2% critical context live for lossless `/clear`** |
| **Cloud + Local GPU Code Generation** | ❌ Frontier cloud rates billed for every line of boilerplate | ⚠️ Copy-pasting specs between Claude and local OpenCode windows | ✅ **`claudes-workbench` delegates code writing to local GPU in-session** |
| **LLM Watermark Key & Version Ops** | ❌ Key rotation breaks verification of older watermarked outputs | ⚠️ Uncalibrated "AI detectors" suffer from high false positives | ✅ **`Markwright` manages KMS key rotation & calibrated SynthID/KGW proof** |
| **Batch LLM-as-a-Judge Scaling** | ❌ Pure LLM judges guess on edge cases; full human review is slow | ⚠️ Rigid commercial eval schemas break custom judge prompts | ✅ **`Askjudge` resolves `N` cases in `N+K` calls w/ `K` human answers** |
| **45-Engineer Monthly TCO** | **`$6,770.00 / mo`** (`$2,720.00` bloated tokens/API + `40.5h` × `$100/hr` = `$4,050.00` labor) | **`$2,610.00 / mo`** (`$1,110.00` API + `15.0h` × `$100/hr` = `$1,500.00` labor) | **`$320.00 / mo`** (`$70.00` API + `2.5h` × `$100/hr` = `$250.00` labor, **`-95.27%`**) |

---

## 🧪 5. Quantitative TCO Comparison & Hype / Facts / Signal Audit Ledger

### 5.1 Hype vs. Facts vs. Strategic Signal Table

| Repository (`owner/repo`) | Hype (Market Narrative) | Measured Facts (Primary Source Verification) | Strategic Signal (SA Verdict) |
| :--- | :--- | :--- | :--- |
| **`adamoelz/gemkeeper`** | "Claude writes down the 2% of context that matters while it still remembers it, surviving `/clear`" | `★ 10` (`created=2026-11-16`, `2 forks`, Shell, MIT): Claude Code plugin & `skills.sh` skill maintaining an always-current ledger backed by `gemkeeper-bench` token/quality benchmarks. | **🔥 P0 Adopt (High-ROI Context Compaction Shield)**: Turns `/clear` from a context reset into a precision garbage-collection step. |
| **`a-schaefers/claudes-workbench`** | "Claude orchestrates. An OpenCode local LLM on your GPU writes the code" | `★ 9` (`created=2026-11-16`, `1 fork`, Python, MIT): Claude Code plugin with nightly CI testing against the latest Claude Code and OpenCode releases. | **🔥 P0 Adopt (Seamless Hybrid Cloud-Planner / Local-Coder Pattern)**: Cuts frontier output token spend on workstations with local GPUs. |
| **`Vecshield/Markwright`** | "Open-source control plane for LLM text watermarking: registry, key rotation, calibrated evidence" | `★ 9` (`created=2026-11-16`, `1 fork`, Python 3.11+, Apache-2.0): 110+ tests across 3 tiers wrapping `SynthID-Text` and `KGW` with KMS key custody and statistical calibration. | **🔥 P0 Adopt (Enterprise AIGC Provenance Infrastructure)**: Solves key rotation and statistical auditability for watermarked text. |
| **`mczlwl/Askjudge`** | "Selective human assistance for LLM-as-a-Judge workflows in `N + K` model calls" | `★ 6` (`created=2026-11-14`, `1 fork`, Python, MIT): Preserves opaque judge outputs while routing `needs_human` cases to a single focused human question. | **⚡ P1 Adopt (Optimal Human-in-the-Loop Eval Router)**: Focuses scarce human SME time strictly on ambiguous `K` cases. |

### 5.2 Closed-Form FinOps TCO Ledger (`CLAIM-20261119-R27-R551-GEMKEEPER-CLAUDESWORKBENCH-MARKWRIGHT-ASKJUDGE`)

* **Scope (`synthetic`, `independently_reproduced=false`)**: 45-person enterprise long-session coding, hybrid cloud/local GPU execution, AIGC watermark governance, and LLM evaluation team (blended rate `$100.00 / hr`; `base hardware capEx: not_measured`; Track B `stars_today: not_measured`).
* **Path A (Bloated 180k Sessions + All-Cloud Boilerplate Coding + Unmanaged Watermark Keys + 100% Manual Eval Review)**:
  - Bloated 180k-context token re-billing & frontier coder token spend on routine boilerplate: **`$2,720.00 / mo`**
  - Re-explaining forgotten constraints after `/clear`, manually reviewing all `N` evaluation cases & disputing uncalibrated detector claims (`40.5 hrs / mo` × `$100.00 / hr`): **`$4,050.00 / mo`**
  - **Path A Monthly Total**: `$2,720.00 + $4,050.00` = **`$6,770.00 / mo`**
* **Path B (Manual Handoff Notes + Separate Local LLM Windows + Ad-Hoc Watermark Scripts)**:
  - SaaS & API spend: **`$1,110.00 / mo`**
  - Manual handoff note writing & watermark key management (`15.0 hrs / mo` × `$100.00 / hr`): **`$1,500.00 / mo`**
  - **Path B Monthly Total**: `$1,110.00 + $1,500.00` = **`$2,610.00 / mo`**
* **Path C (`gemkeeper` + `claudes-workbench` + `Markwright` + `Askjudge` Integrated Stack)**:
  - Frontier orchestration & `N + K` judge API spend (`claudes-workbench` local GPU coding & `gemkeeper` lean `/clear` sessions): **`$70.00 / mo`**
  - Answering only the `K` focused `Askjudge` questions & reviewing calibrated `Markwright` evidence (`2.5 hrs / mo` × `$100.00 / hr`): **`$250.00 / mo`**
  - **Path C Monthly Total**: `$70.00 + $250.00` = **`$320.00 / mo`**
  - **Monthly Net Savings vs. Path A**: `$6,770.00 - $320.00` = **`$6,450.00 / mo`** (**`-95.27%`** reduction, **`$77,400.00 / yr`** annual savings, freeing **`38.0 hrs / mo`** of engineering time).

---

## 🛠️ 6. Enterprise Adoption & Architecture Review Checklist

- [ ] **1. Install `adamoelz/gemkeeper` across long-running Claude Code sessions**: Continuously persist the 2% critical context and `/clear` bloated histories proactively.
- [ ] **2. Connect local workstation GPUs via `a-schaefers/claudes-workbench`**: Keep Claude as the orchestrator while delegating bulk code writing to local OpenCode models.
- [ ] **3. Manage `SynthID-Text` and `KGW` watermarks through `Vecshield/Markwright`**: Enforce KMS key rotation and versioned statistical verification.
- [ ] **4. Route batch evaluations through `mczlwl/Askjudge`**: Resolve clear cases automatically and surface only `K` focused questions to human SMEs.
