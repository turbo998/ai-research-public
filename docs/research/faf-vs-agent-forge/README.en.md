# Agent Forge (FAF v2) vs. Microsoft AGENT-FORGE: Deep-Dive Architecture & Comparison Guide

[中文版本 (Chinese Version)](./README.zh-CN.md) | [16-Dimension Matrix](./comparison-matrix.en.md) | [7-Card 4:5 Benchmark Report](./test-report.en.md) | [HTML Visual Deck (4:5)](./test-report-cards.html) | [Verified Evidence Ledger](./evidence.json)

> **Executive Summary**:
> Although **`customer-success-microsoft/faf-agents`** (documented internally as **Agent Forge (FAF)**, marketplace name `agent-forge-plugins`, `v2.0.1`) and **`microsoft/agent-forge`** (published on npm as `@agent-forge-copilot/cli`, `v0.3.0`) share the name "Agent Forge", they operate at **completely different meta-levels** and solve distinct, complementary problems:
> 1. **`customer-success-microsoft/faf-agents` (FAF v2.0.1)** is a **pre-built, domain-specific Agentic SDLC Delivery System & Copilot Plugin Marketplace** for enterprise customer engagements. It ships **6 GA GenAI Role Agents + 6 registered Fabric Analytics Agents (plus 3 experimental workflow runners in source) + 17 curated domain skills + quantitative scoring cards + external Knowledge Base management (Harness Engineering)**—guiding solution architects and delivery engineers from customer discovery, AI initiative prioritization (9 gates), C4 architecture specification, and weighted accelerator scoring (`>70%` Agentic Customization vs. `<40%` Agentic Development) through Azure Bicep Landing Zone deployment and code implementation.
> 2. **`microsoft/agent-forge` (`@agent-forge-copilot/cli` v0.3.0)** is a **stack-agnostic Context Engineering Meta-Generator CLI**. Rather than shipping domain delivery methodology or Azure/Fabric architects, it runs a multi-agent **Planner → Orchestrator → 7 Specialized Writer Agents → Deterministic Validator (44 valid VS Code tools + Levenshtein distance `<=3` typo auto-fix) → Smart Merger** pipeline (`forge init` / `forge generate`) that inspects *any* software repository (14 tech-stack manifest detectors) and dynamically synthesizes tailored `.github/agents/`, `.github/prompts/`, `.github/instructions/`, `.github/skills/`, `.github/hooks/`, `.vscode/mcp.json`, and `.github/workflows/`.

---

## 1. Verified Commit Baseline & Reproducibility Anchors

This study is grounded in static source code and contract verification (`static_contract_verified`) against exact Git commit snapshots retrieved on October 23, 2026 (without modifying local global VS Code plugins or global npm packages, and with strict sanitization of any internal customer/employee identifiers):

| Dimension | `customer-success-microsoft/faf-agents` (FAF v2) | `microsoft/agent-forge` (AGENT-FORGE CLI) |
| --- | --- | --- |
| **Core Identity** | Enterprise GenAI & Microsoft Fabric SDLC Delivery Practice & Copilot Plugin Marketplace | Context Engineering Meta-Generator CLI for synthesizing `.github/` Copilot customizations |
| **Visibility & License** | Microsoft Internal EMU Repository (`INTERNAL`), `MIT License` (includes Anthropic-derived document skill notices) | Public GitHub Repository (`PUBLIC`), `MIT License` |
| **Verified Commit SHA** | `a740ad88afa0b054e656207e72205002ca6744f0` (`2026-10-21T09:21:48Z`) | `655ff3401d18bd000252907a512a3f674114f708` (`2026-04-16T04:50:36Z`) |
| **Git Tree Scale** | `590` blob objects / `736` total tree entries | `38` blob objects / `48` total tree entries |
| **Distribution & Version** | Copilot Plugin Marketplace (`agent-forge-plugins` `v2.0.1`: `faf-core@2.1.1`, `faf-genai@2.1.0`, `faf-analytics@1.0.1`) | npm CLI package `@agent-forge-copilot/cli@0.3.0` (binary `forge`, Node.js `>=20.0.0`) |
| **Primary Entrypoint** | VS Code Copilot Chat `/FAF-genai-*` and `/FAF-analytics-*` slash prompts & role agent picker | Terminal CLI commands: `forge init`, `forge generate`, `forge validate`, `forge list`, `forge add`, `forge audit` |

---

## 2. Part I: `customer-success-microsoft/faf-agents` (FAF v2) Setup & Architecture

### 2.1 Core Philosophy: From Rigid End-to-End IP to Composable Agent-Driven Practices

Traditional enterprise delivery relies heavily on monolithic, end-to-end solution accelerators. Whenever a customer's business domain, data topology, or compliance boundary deviates from the template's assumptions, delivery teams face costly rewrites.

**FAF (Agent Forge)** shifts this paradigm by decomposing reusable IP into four composable layers:
1. **Stage-Gated Role Agents**: Specialized agents for Analyst (scoping & PRD), Architect (C4 specs, model evaluation, Azure TCO), Implementation Recommender (weighted accelerator scoring), Product Owner (backlog & issue decomposition), Developer (implementation & custom agent orchestration), and Infra (Bicep & AI Landing Zone deployment).
2. **On-Demand Domain Skills**: Reusable skill modules such as `faf-ai-prioritization` (3-dimension prioritization with 9 gating rules), `faf-genai-foundry-model-evaluation` (11-dimension model scorecard), `faf-azure-pricing` (live retail queries against `https://prices.azure.com/api/retail/prices`), `faf-diagrams` / `faf-drawio-azure-diagrams`, and Office document generation (`docx`, `pptx`, `xlsx`, `pdf`).
3. **Two Canonical Delivery Paths**:
   - **Path A — Agentic Customization (Weighted Accelerator Score `> 70%`)**: Clone the highest-scoring solution accelerator, use the Product Owner Agent to perform gap analysis against the customer's `specs/spec.md`, and use the Developer Agent for targeted customization.
   - **Path B — Agentic Development (Weighted Accelerator Score `< 40%`)**: Start from a lightweight App Starter, invoke **`faf-kb-manager` (Harness Engineering)** to pull stack-specific knowledge bases from `customer-success-microsoft/faf-knowledge-bases`, and build from scratch with Infra, PO, and Developer Agents.
   - **Middle Review Band (`40% – 70%`)**: Flagged as `Further Assessment Required`, requiring human architect review to weigh customization effort vs. greenfield build.
4. **Built-In Telemetry & Cost Accounting (FAF Token Benchmark)**: Driven by `src/core/hooks.json` and `src/core/scripts/faf_benchmark.py` (124,109 bytes, 53 unit tests), capturing tokens, AI Credits (`nano-AIU / 1,000,000,000`), active execution duration (excluding `ask_user` human wait intervals), and subagent attribution with **zero extra LLM calls**.

---

### 2.2 Installation Guide & VS Code Plugin Cache Gotcha

FAF v2 is distributed as a **VS Code Copilot Agent Plugin Marketplace** (defined in `.github/plugin/marketplace.json`).

#### Recommended Setup via VS Code Plugin Marketplace

1. **Prerequisites**:
   - **VS Code** (latest stable or Insiders) with **GitHub Copilot Chat** enabled.
   - GitHub access to `customer-success-microsoft/faf-agents` (authenticated via `gh auth login` or VS Code GitHub sign-in).
   - Enable `chat.plugins.enabled` in VS Code Settings (`Ctrl+,`).
2. **Register the Marketplace Repository**:
   - In VS Code Settings, search for `chat.plugins.marketplaces`, click **Add Item**, and add:
     ```text
     customer-success-microsoft/faf-agents
     ```
3. **Install the Three Modular Plugins** (`Ctrl+Shift+P` → `Chat: Plugins` or filter Extensions by `@agentPlugins`):
   - **`faf-core` (`v2.1.1`) [Mandatory Base]**: Located in `./src/core/`, providing shared skills (`faf-kb-manager`, `faf-azure-pricing`, `faf-diagrams`, `faf-drawio-azure-diagrams`, `docx`, `pptx`, `xlsx`, `pdf`) and `hooks.json` benchmark hooks.
   - **`faf-genai` (`v2.1.0`) [GenAI Delivery Suite]**: Located in `./src/genai/`, providing 6 GA role agents, 3 GenAI skills, and 9 `/FAF-genai-*` slash prompts.
   - **`faf-analytics` (`v1.0.1`) [Fabric Analytics Suite]**: Located in `./src/analytics/`, providing 6 registered Fabric analytics agents, 6 skills, and 8 `/FAF-analytics-*` slash prompts.
4. **Configure MCP Servers & Companion Extensions**:
   - `.vscode/mcp.json` registers 3 core MCP servers:
     - `microsoft-learn` (`https://learn.microsoft.com/api/mcp`) for authoritative Azure/Fabric documentation.
     - `deepWiki` (`https://mcp.deepwiki.com/mcp`) for open-source repo and pattern inspection.
     - `github` (`https://api.githubcopilot.com/mcp/`) for backlog and issue creation.
   - Install `hediet.vscode-drawio` in VS Code to view and edit `.drawio` architecture diagrams.
   - Optionally package/install the **FAF Agent Workbench (`v0.1.0`)** extension under `src/genai/extensions/faf-agent-workbench/` for a visual sidebar tracking `scope/`, `specs/`, `impl_rec/`, `arch/`, and `plan/` artifacts.

#### ⚠️ Critical Operational Gotcha: Manual Cache Deletion Required on Plugin Upgrade

As documented in `docs/marketplace/INSTALL.md` (blob `e86a8676`), **uninstalling a plugin in VS Code and adding it back reuses the cached copy on disk rather than pulling new commits from GitHub!**
To upgrade FAF cleanly:
1. Uninstall `faf-core`, `faf-genai`, and `faf-analytics` in VS Code.
2. Close all VS Code windows completely.
3. Delete the cached `agentPlugins` directory manually:
   - **Windows (PowerShell)**:
     ```powershell
     Remove-Item -Recurse -Force "$env:APPDATA\Code\agentPlugins\github.com\customer-success-microsoft\faf-agents"
     ```
   - **macOS / Linux**:
     ```bash
     rm -rf ~/.config/Code/agentPlugins/github.com/customer-success-microsoft/faf-agents
     ```
4. Reopen VS Code and reinstall the plugins.

---

### 2.3 Breakdown of FAF Plugins & Quantitative Scoring Mechanics

#### (1) `faf-genai` (`v2.1.0`): 6 GA Role Agents & End-to-End Contract

```
[Customer Discovery Notes / RFP]
       │
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. Analyst Agent (/FAF-genai-scope, /FAF-genai-prd)                     │
│    • Skill: faf-ai-prioritization (Value / Feasibility / Readiness)     │
│    • Gates: 2 Hard Gates + 7 Readiness Gates + 40% Confidence Floor     │
│    • Outputs: scope/*.md (Use-Case Prioritization) + specs/prd.md       │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │ Handoff
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 2. Architect Agent (/FAF-genai-spec, /FAF-genai-adr, /FAF-genai-model-eval)│
│    • Skill: faf-genai-foundry-model-evaluation (11-Dim Model Scorecard) │
│    • Skill: faf-diagrams / faf-drawio-azure-diagrams + faf-azure-pricing │
│    • Outputs: specs/spec.md (C4 L1-L3 Spec) + specs/adr/*.md            │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │ Handoff
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 3. Implementation Recommender (/FAF-genai-recommend-impl)               │
│    • 8-Area Weighted Scorecard: UseCase(25%)+Agentic(20%)+AIStack(18%)  │
│      +Data(15%)+Hosting(10%)+API(5%)+UI(4%)+Infra(3%) = 100%            │
│    • Output: impl_rec/impl-rec.md                                       │
└──────────────────┬───────────────────────────────────┬──────────────────┘
     Score > 70%   │ (40-70%: Human Architect Review)  │ Score < 40%
                   ▼                                   ▼
┌─────────────────────────────────────┐ ┌─────────────────────────────────┐
│ Path A: Agentic Customization       │ │ Path B: Agentic Development     │
│ • Reuse 6 Tech Success Accelerators │ │ • Pick lightweight App Starter  │
│   or Copilot Studio Accelerators    │ │ • faf-kb-manager pulls KBs      │
│ • PO Agent runs Gap Analysis        │ │ • Infra Agent deploys Bicep/LZ  │
│ • Dev Agent customizes accelerator  │ │ • PO + Dev Agent build greenfield│
└─────────────────────────────────────┘ └─────────────────────────────────┘
```

1. **Analyst Agent (`FAF-analyst.agent.md`)**:
   - Converts customer discovery notes into project scoping documents (`scope/`) and Product Requirements Documents (`specs/prd.md`).
   - **AI Initiative Prioritization (`scoring-framework.yaml`)**:
     - **Value (100%)** = Business Value (`60%`) + Strategic Alignment (`40%`);
     - **Feasibility (100%)** = AI Suitability (`35%`) + Technical Feasibility (`40%`) + Risk & Compliance (`25%`);
     - **Readiness (100%)** = Data Readiness (`50%`) + Organizational Readiness (`50%`);
     - **Bands**: `High >= 65`, `Medium 40–64`, `Low < 40`, with a `confidence_floor: 40` (below 40% is marked `Provisional`).
     - **9 Gating Rules**: 2 Hard Gates (`ai_unsuitable`, `regulatory_prohibition`) and 7 Readiness Gates (`no_executive_sponsor`, `no_data_available`, `no_data_access`, `no_business_owner`, `stakeholders_not_committed`, `no_run_owner`, `security_approval_missing`).
2. **Architect Agent (`FAF-architect.agent.md`)**:
   - Authors C4 (Context, Container, Component) technical specifications (`specs/spec.md`), ADRs (`specs/adr/`), Azure retail cost estimates, and Foundry model evaluations.
   - **11-Dimension Foundry Model Evaluation (`lllm-model-scoring-card.md`)**: Evaluates `task_alignment`, `reasoning`, `multimodal`, `context_window`, `latency`, `cost`, `language_support`, `safety_compliance`, `customizability`, `ecosystem`, plus a mandatory **`deprecation_date` lifecycle gate (models retiring within 6 months are disqualified)**.
3. **Implementation Recommender Agent (`FAF-impl-recommender.agent.md`)**:
   - **8-Area Weighted Scorecard (`accelerators-scoring-card.md`)**: Scores individual sub-metrics on `{0%, 25%, 50%, 75%, 100%}`, computes area averages, and applies strict weights:
     - `use_case` (**25%**) + `agentic_patterns` (**20%**) + `ai_stack` (**18%**) + `data_scenario` (**15%**) + `hosting` (**10%**) + `api_integration` (**5%**) + `ui_scenario` (**4%**) + `infrastructure` (**3%**) = **100%**.
   - Evaluates 6 default Tech Success code accelerators (`agent-openai-python-banking-assistant`, `Agentic-AI-Investment-Analysis-Sample`, `ai-document-processor`, `gpt-rag`, `contentflow`, `live-voice-practice`) and Copilot Studio accelerators (`ContentFlow`, `AISearch Flow`, `Video RAG`, etc.).
4. **Product Owner Agent (`FAF-product-owner.agent.md`)**:
   - Breaks architecture specs and implementation plans into Sprint Backlogs (`plan/`) or GitHub Issues.
5. **Developer Agent (`FAF-dev.agent.md`)**:
   - Implements code changes and includes a **Custom Agent Orchestration** workflow that pairs with `faf-kb-manager` to synthesize stack-specific coding subagents.
6. **Infra Agent (`FAF-infra.agent.md`)**:
   - Supports **Workflow 1 (Dev/Demo)** via modular Bicep + `azd`, and **Workflow 2 (Production AI Landing Zone)** built on **`Azure/bicep-ptn-aiml-landing-zone`**.

#### (2) `faf-analytics` (`v1.0.1`): Microsoft Fabric Analytics Delivery Chain

- **Source Tree vs. Plugin Manifest Discrepancy (Key Verification Finding)**:
  - While `src/analytics/agents/` contains **9 `.agent.md` files**, `src/analytics/plugin.json` registers **6 user-facing agents** (`FAF-analytics-analyst`, `FAF-analytics-architect`, `FAF-analytics-impl-recommender`, `FAF-analytics-assessment`, `FAF-analytics-product-owner`, `FAF-analytics-developer`), intentionally omitting 3 internal evaluation/workflow runner agents (`FAF-analytics-workflow-runner`, `FAF-analytics-workflow-tester`, `FAF-analytics-workflow-batch-runner`).
  - Furthermore, `analytics/RELEASE_NOTES_v1.md` scopes the formal v1.0 release testing gate to **Analyst + Architect** across two golden scenarios: **(1) Microsoft Fabric Real-Time Intelligence (RTI)** and **(2) On-premises SQL Server / Synapse Dedicated SQL Pool to Fabric Data Warehouse migration**.
  - `docs/analytics/evaluation/faf-analytics-score-below-70-analysis.md` documents why an earlier external evaluation scored ~54–60% (<70%): the external rubric expected a single monolithic document, whereas FAF intentionally separates responsibilities across Analyst (PRD), Architect (Spec), and Assessment (Medallion spec).

#### (3) `faf-core` (`v2.1.1`): Harness Engineering & Zero-Extra-Call Token Benchmark

- **Harness Engineering (`faf-kb-manager`)**:
  - Decouples rapidly evolving framework/SDK documentation into `customer-success-microsoft/faf-knowledge-bases`, allowing on-demand checkout into `~/.faf-kb/` or `docs/kb/` without bloating the plugin distribution.
- **FAF Token Benchmark (`src/core/scripts/faf_benchmark.py`)**:
  - Activated opt-in by including `benchmark=true benchmark-label=<label>` in a prompt. When unmarked, hook fast-exit overhead on Windows averages **`0.93s`** (`0.70–1.19s`) on `UserPromptSubmit` and **`1.00s`** (`0.86–1.34s`) on `Stop`.
  - Reads full per-call and nested-subagent telemetry (`6/6` dimensions) from Copilot CLI/App session stores or VS Code OTel (`agent-traces.db`), and gracefully degrades to request-aggregate journal estimates (`2/6` exact dimensions) when VS Code OTel is disabled.

---

## 3. Part II: `microsoft/agent-forge` (`@agent-forge-copilot/cli`) Deep Dive

### 3.1 Core Identity: Turning Manual `.github/` Authoring into a Multi-Agent Compiler Pipeline

Writing and maintaining `.github/agents/*.agent.md`, `.github/instructions/*.instructions.md`, `.github/skills/*/SKILL.md`, `.github/hooks/*.json`, and `.vscode/mcp.json` across diverse repositories is error-prone. **`microsoft/agent-forge`** (which retains its legacy marker `<!-- Generated by SpecForge -->` in `src/lib/merger.ts`) automates this as a **Context Engineering Toolkit**.

### 3.2 The 4-Stage Plan-Then-Execute Pipeline

1. **Workspace Detection (`src/lib/detector.ts`)**:
   - Scans **14 `TECH_INDICATORS`** (`package.json`, `tsconfig.json`, `pyproject.toml`, `requirements.txt`, `go.mod`, `Cargo.toml`, `pom.xml`, `build.gradle`, `Gemfile`, `composer.json`, `mix.exs`, `Dockerfile`, `docker-compose.yml`, `.csproj`) and **14 `PROJECT_TYPE_HINTS`** to classify projects into `web`, `api`, `cli`, `library`, `data-pipeline`, or `other`, while auditing existing `.github/` customizations.
2. **Dual-Mode Planner (Greenfield vs. Brownfield)**:
   - Invokes Copilot CLI (`maxContinues: 25`) to produce `.github/forge-plan.json` (`GenerationPlan`), selecting one of **6 `OrchestrationPattern` topologies**: `flat`, `coordinator-worker`, `multi-perspective`, `tdd`, `pipeline`, or `iteration`.
3. **Orchestrator & 7 Specialized Writer Agents (`src/cli/writers/*.ts`)**:
   - Delegates generation to `forge-agent-writer`, `forge-prompt-writer`, `forge-instruction-writer`, `forge-skill-writer`, `forge-hook-writer`, `forge-mcp-writer`, and `forge-workflow-writer` (`maxContinues: 15`).
4. **Deterministic Auto-Fix, LLM Validation & Smart Merge (`validator.ts` & `merger.ts`)**:
   - `postGenerationValidateAndFix` reconstructs missing YAML frontmatter, strips unknown keys, validates tool names against **44 `VALID_VSCODE_TOOLS`** using **Levenshtein distance `<= 3`** for typo suggestions, and repairs broken cross-file `handoffs.agent` references (`autoFixHandoffReferences`).
   - `merger.ts` guarantees non-destructive updates by refusing to overwrite any existing file unless `--force` is passed or the file carries `<!-- Generated by AGENT-FORGE -->` (or `<!-- Generated by SpecForge -->`).
   - Also bundles **11 static gallery templates (`src/lib/gallery.ts`)** installable in `~120ms` with zero LLM calls via `forge init --mode templates`.

---

## 4. Part III: High-Level Comparison & Combined Enterprise Workflow

For the complete 16-dimension source-verified comparison, see [**`comparison-matrix.en.md`**](./comparison-matrix.en.md).

| Dimension | `customer-success-microsoft/faf-agents` (FAF v2.0.1) | `microsoft/agent-forge` (`@agent-forge-copilot/cli` v0.3.0) |
| --- | --- | --- |
| **1. Meta-Level Identity** | **Pre-Built Domain Delivery Team**: Curated role agents, skills, and scorecards that directly execute enterprise SDLC work | **Context Engineering Meta-Compiler**: A CLI generator that writes `.github/` customization files for any software project |
| **2. Target Audience** | Microsoft CSU / FastTrack / partner architects delivering **Azure GenAI & Microsoft Fabric** customer engagements | Software engineers across any stack wanting automated, validated `.github/` Copilot configurations |
| **3. Lifecycle Coverage** | **Full Customer SDLC**: Discovery & AI prioritization → PRD → C4 Spec & Model Eval → Accelerator Scoring → Bicep/LZ → Code & Token Audit | **Repo Context Engineering Lifecycle**: Workspace detection → Plan (`forge-plan.json`) → 7 Writers → Schema Auto-Fix → Smart Merge |
| **4. Quantitative Models** | **3 Business Scorecards** (AI Prioritization 9 gates, Foundry 11-dim eval, Accelerator 8-area weights) + **FAF Token Benchmark** | **Configuration Quality Audit (`forge audit` / `forge validate`)**: 0–100 score across coverage, frontmatter compliance, and handoff integrity |
| **5. Cloud / Stack Coupling** | **Deeply coupled to Azure & Microsoft Fabric** (Foundry, AI Search, Bicep Landing Zone, Fabric RTI/DW, Azure Retail Prices API) | **Cloud- and language-agnostic** (supports 14 tech stack manifests across TS/Python/Go/Rust/Java/C#/etc.) |
| **6. File Merge Safety** | Installs plugins in VS Code `agentPlugins`; writes project deliverables to `scope/`, `specs/`, `impl_rec/`, `plan/`, `docs/kb/` | Writes to `.github/` and `.vscode/mcp.json`; `merger.ts` preserves all non-marker files unless `--force` is specified |

### Recommended Combined Workflow: Running FAF + AGENT-FORGE Together

1. **Phase 1 — Scoping, Architecture & Accelerator Selection (Use FAF `faf-genai` / `faf-analytics`)**:
   - Run `/FAF-genai-scope`, `/FAF-genai-prd`, `/FAF-genai-spec`, and `/FAF-genai-recommend-impl` in VS Code Copilot Chat to produce `scope/`, `specs/prd.md`, `specs/spec.md`, and `impl_rec/impl-rec.md`.
2. **Phase 2 — Scaffolding & Landing Zone Provisioning (Use FAF `faf-kb-manager` + `FAF-infra`)**:
   - Clone the recommended accelerator (`>70%`) or starter (`<40%`), sync framework knowledge bases into `docs/kb/` via `faf-kb-manager`, and generate Bicep / AI Landing Zone code via `FAF-infra`.
3. **Phase 3 — Repo-Specific Context Engineering (Use `npx @agent-forge-copilot/cli init`)**:
   - Run `npx @agent-forge-copilot/cli init --mode analyze --strategy guided` on the scaffolded repository to synthesize path-specific `.instructions.md`, TDD/review subagents, and pre-commit quality hooks—while `merger.ts` safely preserves all FAF artifacts.
4. **Phase 4 — Validation & Telemetry**:
   - Validate `.github/` schema integrity in CI with `forge validate`, and track delivery token/credit burn using FAF's `benchmark=true benchmark-label=<sprint>` hook.

---

## 5. Deliverables Index

- [`README.en.md`](./README.en.md): English Research Guide (this document)
- [`README.zh-CN.md`](./README.zh-CN.md) / [`README.md`](./README.md): Chinese Research Guide
- [`comparison-matrix.en.md`](./comparison-matrix.en.md) / [`comparison-matrix.md`](./comparison-matrix.md): Bilingual 16-Dimension Source-Verified Comparison Matrix
- [`test-report.en.md`](./test-report.en.md) / [`test-report.md`](./test-report.md): Bilingual 7-Card 4:5 Benchmark Report (Markdown)
- [`test-report-cards.html`](./test-report-cards.html): Self-contained CSP-safe 7-Card 4:5 Visual Deck (HTML)
- [`evidence.json`](./evidence.json) & [`evidence/report.json`](./evidence/report.json): Machine-verifiable commit/blob SHA ledger and sealed evaluation coordinates
- [`review.md`](./review.md): Quality, bilingual parity, and sanitization verification log
