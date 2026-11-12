# Zero-Dependency Book-to-Skill Compiler (`bookleme/bookleme`) & Proof-Based Anti-Agent De-Blinding MCP (`pktq/lasik` `1,262×` Token Reduction) Selection FAQ

> **Document Scope**: This is the **2026-11-12 Night Shift Round 11 (Cumulative #110) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for Enterprise Knowledge Architects and AppSec / Reverse-Engineering Leads evaluating two high-signal repositories:
> 1. **`bookleme/bookleme` (`148★`, Python 3.9+, `zero third-party deps` at runtime, MIT, supporting PDF / EPUB / DOCX / MD / HTML / RTF / MOBI)**: A dual-engine compiler that transforms 300-page books from passive reading notes into two installable, unit-testable artifacts — **`knowledge_pack` (structured reference shards)** and **`behavior_skill` (executable state machines encoding question sequences, decision criteria, evidence rules, and falsification checks)** — with **compile-time/runtime separation, 3-tier progressive disclosure, and verbatim fidelity verification**!
> 2. **`pktq/lasik` (`116★`, TypeScript / CLI + MCP Server, `lasik-agents` on npm, `v0.3`, MIT)**: A **proof-based, 100% static de-blinding CLI and MCP server** that undoes [`qybaihe/bla` (Blind LLM Agents)](https://github.com/qybaihe/bla) anti-agent hardening — healing **59/63 shields in `BLA 3.2.2`** (opaque predicates, encrypted strings, decoy code, tamper checks, binary padding, and embedded prompt-injection text) via `v0.3` structural behaviour detection without ever executing the input, shrinking the public BLA CrackMe corpus from **21 million tokens down to 17 thousand (`1,262×` fewer tokens)**!
>
> **中文版本**: [bookleme-lasik-book-to-skill-compiler-static-deblinding-mcp-selection-faq.md](bookleme-lasik-book-to-skill-compiler-static-deblinding-mcp-selection-faq.md) · **Daily Digest**: [`daily/2026-11-12.en.md`](../daily/2026-11-12.en.md) · **Architecture Summary SVG**: [`assets/github-ai-radar-2026-11-12-r11-bookleme-lasik.svg`](../../../assets/github-ai-radar-2026-11-12-r11-bookleme-lasik.svg)

![BookLeme and LASIK v0.3 Architecture Comparison](../../../assets/github-ai-radar-2026-11-12-r11-bookleme-lasik.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "chunking a 300-page domain book into vector RAG where the agent quotes isolated paragraphs but fails to follow the author's step-by-step diagnostic and falsification workflow" (`bookleme/bookleme`)**: The most valuable part of a technical or financial book is not its summary conclusions, but the author's **operational state machine** (question ordering, decision thresholds, evidence rules, and falsification conditions). `BookLeme` reads a book once at compile time and emits both a `knowledge_pack` and an executable `behavior_skill` with **3-tier progressive disclosure** (resident entry → on-demand shards → local full text), decoupling deterministic extraction from probabilistic generation and verifying verbatim fidelity!
   - **Ending "anti-agent obfuscators (`BLA`) blinding coding and security agents with 21 million tokens of decoy code, binary padding, and embedded prompt injections" (`pktq/lasik` `v0.3`)**: When auditing third-party builds hardened with `qybaihe/bla`, coding agents exhaust their context windows on decoy control flow or get hijacked by injected prompts. `pktq/lasik` (`lasik-agents`) performs **100% static, proof-based de-blinding**: a transform runs only when behaviour preservation is proven (unprotected files return **byte-identical**), `v0.3` detects protections by structural behaviour rather than symbol names, and **59/63 BLA 3.2.2 shields heal cleanly — cutting token count by `1,262×` (from ~21M to ~17k tokens)**!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261112-R11-BOOKLEME-LASIK`)**:
   - Modeled for a **12-person enterprise knowledge-engineering & binary security team compiling `20 domain books/playbooks` and auditing `40 obfuscated/hardened software builds` per month** (fully loaded senior engineer rate `$90.00/hr`; commercial ebook copyright licenses and IDA Pro/Binary Ninja seats: `not_measured`):
   - Upgrading from **Path A (raw 300-page PDF RAG stuffing + feeding 21M-token BLA-protected builds into agents, `$6,580.00/mo`)** to **Path C (`BookLeme` 3-tier compiled skills + `LASIK v0.3` static proof-based de-blinding MCP, `$680.00/mo`)** saves **`$5,900.00/mo` (`-89.67%`, or `$70,800.00/yr`)** and cuts manual skill authoring and deobfuscation labor from `46.0 hrs/mo` to `5.0 hrs/mo` (**`-89.13%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: How does `bookleme/bookleme` compile books into unit-testable `behavior_skill` state machines with 3-tier progressive disclosure?
- **First-Principles Breakdown**:
  1. **Dual-Engine Output (`knowledge_pack` + `behavior_skill`) & Deterministic/Probabilistic Split**:
     - Extracts an author's question sequences, judgment criteria, evidence rules, and falsification triggers into structured, diffable artifacts while separating deterministic structural parsing from probabilistic synthesis.
  2. **Compile-Once 3-Tier Progressive Disclosure & Verbatim Fidelity**:
     - Loads only a compact resident entry at runtime, fetching knowledge shards or local full-text passages on demand, with genre-specific back-verification and explicit `UNVERIFIED` tags on unvalidated hypotheses.

### Q2: How does `pktq/lasik` (`v0.3`) heal 59/63 BLA shields and achieve a `1,262×` token reduction without ever executing the input?
- **First-Principles Breakdown**:
  1. **Proof-Based Behaviour Preservation & Byte-Identical Guarantee**:
     - Removes opaque predicates, encrypted strings, decoy code, tamper checks, binary padding, and prompt-injection strings only when behaviour preservation is mathematically proven; unprotected files pass through byte-identical.
  2. **v0.3 Structural Detection & Pure Static Safety**:
     - Identifies protection layers by structural semantics rather than identifier names (verified against renamed builds in CI), running 100% statically with no `eval`, sandbox, or WASM execution via CLI (`lasik heal`) or MCP.

### Q3: How should AI Solution Architects combine `BookLeme` and `LASIK`?
- **Golden-Combo Pattern**:
  - Compile authoritative reverse-engineering, AppSec, and architecture textbooks into executable `behavior_skill` state machines with **`bookleme/bookleme`**;
  - Pre-process hardened or obfuscated target builds through the **`pktq/lasik` MCP server** (`1,262×` token reduction) before running the compiled audit skills!

---

## 🧭 3. Mermaid Decision Tree & Book-Compilation + Static-De-Blinding Pipeline

```mermaid
flowchart TD
    A["Enterprise Methodology Compilation & Anti-Agent De-Blinding Selection"] --> B{"Primary Engineering Bottleneck?"}
    B -- "300-page books in RAG only quote snippets instead of executing decision workflows" --> C["Adopt bookleme/bookleme (Zero-Dep Dual-Engine Compiler)"]
    B -- "Target builds hardened with BLA exhaust agent context (21M tokens) & inject prompts" --> D["Adopt pktq/lasik v0.3 (Proof-Based Static De-Blinding CLI + MCP)"]

    C --> C1["Compile once -> emit knowledge_pack + executable behavior_skill state machine"]
    C1 --> C2["3-tier runtime disclosure (Entry -> Shards -> Full Text) + verbatim fidelity check"]

    D --> D1["v0.3 structural detection heals 59/63 BLA shields (renamed builds included, 0 eval)"]
    D1 --> D2["Strips decoy code, encrypted strings & prompt injections (21M -> 17k tokens, 1,262x)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Raw 300p PDF RAG + Raw 21M-Token BLA Builds | Path B: Manual Markdown Notes + Regex Deobfuscators | **Path C (Recommended): `BookLeme` + `LASIK v0.3`** |
| :--- | :--- | :--- | :--- |
| **Methodology Execution Fidelity** | Retrieves loose paragraphs; misses falsification rules | Labor-intensive manual notes; no fidelity verifier | **Compiles `knowledge_pack` + testable `behavior_skill` state machine** |
| **Runtime Context Footprint** | Dumps large PDF chunks on every turn | Full notes pinned in system prompt | **3-tier progressive disclosure with zero 3rd-party runtime deps** |
| **Counter-BLA De-Blinding Power** | Context overflow (21M tokens) & prompt-injection hijack | Regex breaks as soon as identifiers are renamed | **v0.3 structural detection heals 59/63 shields (`1,262×` token drop)** |
| **Semantic Safety & Host Security** | LLM rewrites break program semantics | Dynamic sandboxes risk malware escape | **Proof-based (clean files byte-identical) + 100% static (no `eval`)** |
| **Monthly TCO (20 Books + 40 Audits)** | **`$6,580.00 / mo`** (`$2,440` API + `$4,140` labor) | **`$3,220.00 / mo`** (`$1,060` API + `$2,160` labor) | **`$680.00 / mo` (Saves `$5,900.00/mo` · `-89.67%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261112-R11-BOOKLEME-LASIK`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A 12-person enterprise knowledge-engineering & binary security team compiling **20 domain books/playbooks** and auditing **40 obfuscated/BLA-hardened software builds per month**.
- **Labor Rate**: Fully loaded senior knowledge/security engineering rate of **`$90.00 / hr`**.
- **Explicit Not-Measured Boundary**: Commercial ebook copyright acquisition fees and IDA Pro / Binary Ninja seat licenses are marked **`not_measured`**. This model strictly accounts for LLM token spend and engineering hours spent on manual skill authoring and manual deobfuscation.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Raw PDF RAG + Raw 21M-Token BLA Builds | Path B: Manual Summaries + Regex Scripts | **Path C: `BookLeme` + `LASIK v0.3` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Compilation & Security Audit Token Spend** | **`$2,440.00`** | **`$1,060.00`** | **`$230.00`** (3-tier disclosure + `1,262×` static token reduction) |
| **Manual Skill Authoring & Deobfuscation Labor (`$90/hr`)** | `46.0 hrs × $90.00` = **`$4,140.00`** | `24.0 hrs × $90.00` = **`$2,160.00`** | `5.0 hrs × $90.00` = **`$450.00`** |
| **Total Monthly TCO** | **`$6,580.00 / mo`** | **`$3,220.00 / mo`** (`-51.06%`) | **`$680.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$3,360.00 / mo` | **Saves `$5,900.00 / mo` (`-89.67%` · `$70,800.00/yr`)** |
| **Commercial Ebook Rights & IDA Pro Licenses** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `BookLeme` Dual-Artifact Compilation & Fidelity Check**: Compile a domain PDF/EPUB into a `knowledge_pack` and `behavior_skill`, verifying source fidelity checks pass.
- [ ] **2. 3-Tier Progressive Disclosure Verification**: Confirm that runtime sessions load only the resident entry until specific shards or verbatim passages are requested.
- [ ] **3. `pktq/lasik` (`v0.3`) Byte-Identical Regression Test**: Run `npx lasik-agents heal` on known-clean files and verify byte-for-byte SHA-256 identity.
- [ ] **4. Static Counter-BLA MCP Pipeline**: Mount the `lasik` MCP server ahead of code-review agents to strip opaque predicates, decoy code, and prompt injections before LLM ingestion.
