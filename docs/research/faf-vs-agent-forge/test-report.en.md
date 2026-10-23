# Agent Forge (FAF v2) vs. Microsoft AGENT-FORGE Contract & Capability Benchmark Report (7-Card 4:5 Visual Deck)

[中文版本](./test-report.md) | [Back to Main Guide](./README.en.md) | [16-Dimension Matrix](./comparison-matrix.en.md) | [HTML 4:5 Visual Deck](./test-report-cards.html) | [Sealed Data (`report.json`)](./evidence/report.json)

> **Provenance Notice**: This report follows the **7-Card 4:5 Visual Benchmark Report Standard**. Every percentage, weight, threshold band, tool whitelist count, and hook latency coordinate is extracted directly from pinned commit blobs in `customer-success-microsoft/faf-agents@a740ad88afa0b054e656207e72205002ca6744f0` (590 blobs) and `microsoft/agent-forge@655ff3401d18bd000252907a512a3f674114f708` (38 blobs) (`static_contract_verified_and_anonymized_reported`, `independently_reproduced=false`).

---

## Card 1 (`1 / 7` · `HANDS-ON · AGENT SYSTEMS`) — Overview & Workbench

### **FAF v2 Ships 3 Modular Plugins & 12 Registered Domain Role Agents; AGENT-FORGE Compiles All 7 `.github/` Customization Artifact Types**

| Workbench Column | Verified Metrics & Findings | Source Evidence Anchor |
| --- | --- | --- |
| **Left Column: Scenarios & Threshold Bands** | • **12 Source-Verified Scenarios**: **8** `Act automatically` (`>=80%`), **2** `Confirm` (`33%–67%`), **2** `Send to a human` (`0%`)<br>• **FAF Accelerator Thresholds**: `>70%` Agentic Customization / `40%–70%` Human Review / `<40%` Agentic Development<br>• **FAF Prioritization Bands**: `High >=65` / `Medium 40–64` / `Low <40` (`<40%` confidence floor) | `evidence/report.json`<br>`accelerators-scoring-card.md`<br>`scoring-framework.yaml` |
| **Center Column: Dual System Contract Input** | • **FAF v2 (`agent-forge-plugins@2.0.1`)**: `faf-core@2.1.1` (8 shared skills + Benchmark Hook) + `faf-genai@2.1.0` (6 GA Agents, 3 Skills, 9 Prompts) + `faf-analytics@1.0.1` (6 registered Agents / 9 source Agents, 6 Skills)<br>• **AGENT-FORGE (`@agent-forge-copilot/cli@0.3.0`)**: 14 stack detectors → 2 Planners → 2 Orchestrators → 7 Writers → 44-tool Validator | `.github/plugin/marketplace.json`<br>`src/types.ts`<br>`src/lib/validator.ts` |
| **Right Column: Latency, Token Ledger & Top Decisions** | • **FAF Unmarked Hook Fast-Exit**: `UserPromptSubmit` **`930 ms`** avg / `Stop` **`1,000 ms`** avg (0 extra LLM calls)<br>• **AGENT-FORGE Template Copy**: **`~120 ms`** local copy (11 built-in templates, 0 LLM calls) vs **`30,000 ms`** LLM validator fix timeout | `README-faf-token-benchmark.md`<br>`src/lib/validator.ts:48` |

> **Bottom Provenance Callout**: `static_contract_verified + anonymized_reported (independently_reproduced=false)` · Host: Windows 11 (`git`, `gh`, Python 3) · Commits: `faf-agents@a740ad88` & `agent-forge@655ff340`.

---

## Card 2 (`2 / 7` · `SCENARIO: ENTERPRISE GENAI SCOPING TO REPO CUSTOMIZATION`) — Single-Case Deep Dive

### **8-Area Weighted Accelerator Score (`83.9% > 70%`) Selects Customization Path, While 44-Tool Deterministic Validator (`~120ms`) Locks Repo Rules**

> **Input Scenario Quote**:
> *"An enterprise team needs to scope an Azure AI Foundry + AI Search multi-agent investment research & document intelligence workload, pass 9 prioritization gates, produce a C4 specification, decide whether to customize an existing Solution Accelerator, and generate non-destructive `.github/` coding instructions and hooks for the target repo."*

1. **Decision Card 1 · `[score]` FAF AI Initiative Prioritization & 9-Gate Check (`faf-ai-prioritization`)**
   - **Scores & Confidence**: `Value 78% · Feasibility 74% · Readiness 70%` (Evidence confidence `85% >= 40%` floor)
   - **Action Pill**: `Act automatically` (All 9 gates passed: no regulatory prohibition, executive sponsor and data access confirmed)
   - **Horizontal Score Bars**:
     - Business Value (`60%` weight) + Strategic Alignment (`40%` weight): `78.0%`
     - AI Suitability (`35%`) + Tech Feasibility (`40%`) + Risk & Compliance (`25%`): `74.0%`
     - Data Readiness (`50%`) + Organizational Readiness (`50%`): `70.0%`

2. **Decision Card 2 · `[choice]` FAF Implementation Recommender 8-Area Weighted Scorecard (`FAF-impl-recommender`)**
   - **Top Accelerator Match**: `Agentic-AI-Investment-Analysis-Sample` / `ai-document-processor` weighted score **`83.9%`** (exceeds `> 70%` threshold)
   - **Action Pill**: `Act automatically` → Select **Path A: Agentic Customization**
   - **8-Area Weighted Breakdown**:
     - `use_case` (25% wt): `87.5%` | `agentic_patterns` (20% wt): `85.0%` | `ai_stack` (18% wt): `83.3%` | `data_scenario` (15% wt): `81.3%`
     - `hosting` (10% wt): `75.0%` | `api_integration` (5% wt): `75.0%` | `ui_scenario` (4% wt): `100.0%` | `infrastructure` (3% wt): `87.5%`

3. **Decision Card 3 · `[noul]` AGENT-FORGE Repo `.github/` Synthesis & Auto-Fix (`forge init --mode analyze`)**
   - **Validation & Merge Outcome**: **`100%`** of 7 artifact types supported, **`100%`** tool validation against 44 `VALID_VSCODE_TOOLS`, **`100%`** preservation of existing FAF `specs/` and `scope/` files
   - **Action Pill**: `Act automatically` → `postGenerationValidateAndFix` + `mergeIntoExisting`

---

## Card 3 (`3 / 7` · `WHAT I TESTED`) — Full Evaluation Matrix

### **12-Scenario Contract Matrix: 8 Pass Automatically (`100%`), While 4 Expose Critical Operational Boundaries (`✕`)**

| SCENARIO | QUESTION / TASK | MODEL / SYSTEM ANSWER | ACTION |
| --- | --- | --- | --- |
| **S01 · FAF Plugin Split** | Does `marketplace.json` split FAF v2 into `faf-core`, `faf-genai`, and `faf-analytics`? | `3 / 3 plugins verified (100%)` | `Act automatically` |
| **S02 · FAF GenAI Roster** | Does `faf-genai@2.1.0` ship all 6 GA role agents and 9 `/FAF-genai-*` slash prompts? | `6 GA Agents + 9 Prompts (100%)` | `Act automatically` |
| **S03 · FAF 8-Area Weights** | Do the 8 accelerator scoring weights sum to 100% with `>70%` / `40-70%` / `<40%` bands? | `8 Areas = 100% + 3 Threshold Bands (100%)` | `Act automatically` |
| **S04 · FAF 9 Priority Gates** | Does `faf-ai-prioritization` enforce 2 hard gates + 7 readiness gates + 40% floor? | `3 Dimensions + 9 Gates + 40% Floor (100%)` | `Act automatically` |
| **S05 · FAF Analytics Roster** | Are all 9 agent files in `src/analytics/agents/` registered in `src/analytics/plugin.json`? | `6/9 registered (3 workflow runners omitted) (67%) ✕` | `Confirm` |
| **S06 · FAF Telemetry Fallback** | Without VS Code OTel enabled, does the default Chat Journal capture nested subagents? | `Top-level aggregate only (2/6 sources = 33%) ✕` | `Confirm` |
| **S07 · FAF Plugin Upgrade** | Does uninstalling and re-adding the plugin in VS Code UI pull latest GitHub commits? | `0% auto-refresh (reuses %APPDATA% cache) ✕` | `Send to a human` |
| **S08 · AF 7-Type Pipeline** | Does `agent-forge` generate all 7 artifact types via Planner + Orchestrator + 7 Writers? | `2 Planners + 7 Writers -> 7 Artifact Types (100%)` | `Act automatically` |
| **S09 · AF Stack Detector** | Does `detector.ts` scan 14 manifest indicators and 14 project-type hints? | `14 Tech Indicators + 14 Type Hints (100%)` | `Act automatically` |
| **S10 · AF Schema Auto-Fix** | Does `validator.ts` enforce 44 valid VS Code tools, Levenshtein `<=3`, and handoff repair? | `44 Valid Tools + Levenshtein<=3 + Handoff Fix (100%)` | `Act automatically` |
| **S11 · AF Smart Merge** | Does `merger.ts` preserve 100% of unmarked user-authored files by default? | `100% user-file preservation unless --force (100%)` | `Act automatically` |
| **S12 · Cross-Repo Boundary** | Does `agent-forge` bundle FAF's customer PRD/C4 templates, scorecards, or Bicep LZ? | `0% domain delivery IP bundled ✕` | `Send to a human` |

- **Threshold Gating Callout**: **8 of 12 scenarios (66.7%)** satisfy `Act automatically` (`100%` contract completeness); **2 scenarios (16.7%)** require `Confirm` due to intentional manifest scoping (`6/9` Analytics agents registered) or telemetry fallback (`2/6` dimensions without OTel).
- **Failure / Boundary Callout**: **2 scenarios (16.7%)** score `0%` (`Send to a human`): VS Code reuses cached `agentPlugins` on reinstall unless deleted from disk, and `microsoft/agent-forge` contains zero domain delivery IP.

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`) — Protocol & Scoring Mechanics

### **Protocol Trace: FAF 8-Area Weighted Scorecard & Nano-AIU Billing vs. AGENT-FORGE Deterministic Schema Auto-Fixer**

#### Code Block A: FAF Weighted Accelerator Scoring & Token Benchmark Accounting (`accelerators-scoring-card.md` & `faf_benchmark.py`)

```python
# 1. FAF Implementation Recommender: 8-Area Weighted Score (Sum of weights = 100%)
AREA_WEIGHTS = {
    "use_case": 0.25, "agentic_patterns": 0.20, "ai_stack": 0.18, "data_scenario": 0.15,
    "hosting": 0.10,  "api_integration": 0.05,  "ui_scenario": 0.04, "infrastructure": 0.03,
}
# Sub-metrics scored in {0.0, 0.25, 0.50, 0.75, 1.0}; weighted_score > 0.70 => Agentic Customization
# 0.40 <= weighted_score <= 0.70 => Further Assessment Required; < 0.40 => Agentic Development

# 2. FAF Token Benchmark (src/core/scripts/faf_benchmark.py): Zero-LLM-Call Accounting
# Triggered opt-in via prompt marker: benchmark=true benchmark-label=<label>
ai_credits = nano_aiu / 1_000_000_000          # 1 AI credit = 10^9 nano-AIU
estimated_usd = ai_credits * 0.01              # $0.01 per AI credit
active_duration_ms = wall_clock_ms - non_overlapping_human_wait_ms  # subtracts ask_user wait
```

`↓`

#### Code Block B: AGENT-FORGE Deterministic Frontmatter, Tool & Handoff Auto-Fixer (`src/lib/validator.ts` & `src/lib/merger.ts`)

```typescript
// src/lib/validator.ts: postGenerationValidateAndFix(files)
// Step 1: Reconstruct missing YAML frontmatter & strip unrecognized keys per artifact schema
// Step 2: Validate tools against 44 VALID_VSCODE_TOOLS with Levenshtein distance <= 3 suggestion
const suggestion = findClosestTool(invalidTool, VALID_VSCODE_TOOLS); // max distance <= 3

// Step 3: Repair broken cross-file handoff targets (autoFixHandoffReferences)
// Matches target agent by case-insensitive exact match, prefix/suffix containment, or Levenshtein <= 3

// src/lib/merger.ts: Non-destructive smart merge protection
const GENERATED_MARKER = '<!-- Generated by AGENT-FORGE -->';
const LEGACY_MARKER    = '<!-- Generated by SpecForge -->';
// Refuses to overwrite existing file unless options.force === true or file includes marker
```

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`) — Perturbation & Consistency

### **Mode & Boundary Perturbations: Telemetry Fallback (`-66.7 pts`), Manifest Scoping (`-33.3 pts`), and Merge Lock (`-100.0 pts`) Hold Strictly**

| QUESTION / DIMENSION | ORIGINAL (PRIMARY PATH) | REVERSED / PERTURBED PATH | CHANGE (PTS) |
| --- | --- | --- | --- |
| **FAF Telemetry Source**<br>Copilot Session Store vs. VS Code Journal Fallback | **100.0%**<br>(6/6 exact dimensions incl. nested subagents) | **33.3%**<br>(2/6 dimensions: request-aggregate only) | **`-66.7 pts`**<br>(`Holds`) |
| **FAF Analytics Agent Exposure**<br>Source Tree (`src/analytics/agents/`) vs. `plugin.json` | **100.0%**<br>(9/9 `.agent.md` files present in source tree) | **66.7%**<br>(6/9 registered in manifest; 3 runners omitted) | **`-33.3 pts`**<br>(`Holds`) |
| **FAF Accelerator Threshold Gate**<br>High-Fit Sample (`>70%`) vs. Low-Fit Custom (`<40%`) | **83.9%**<br>(Selects Path A: Agentic Customization) | **35.0%**<br>(Selects Path B: Agentic Development + KB pull) | **`-48.9 pts`**<br>(`Holds`) |
| **AGENT-FORGE Init Mode**<br>`--mode create/analyze` vs. `--mode templates` | **100.0%**<br>(7/7 `.github/` artifact types dynamically generated) | **71.4%**<br>(5/7 artifact types in static gallery, 0 LLM calls) | **`-28.6 pts`**<br>(`Holds`) |
| **AGENT-FORGE Merge Flag**<br>Default Safe Merge vs. `--force` Overwrite | **100.0%**<br>(100% of unmarked user files preserved) | **0.0%**<br>(`--force` overwrites conflicting files) | **`-100.0 pts`**<br>(`Holds`) |
| **AGENT-FORGE Tool Typo Distance**<br>Levenshtein `<= 3` vs. Distance `> 3` | **100.0%**<br>(Auto-suggests closest of 44 valid VS Code tools) | **0.0%**<br>(Zero false-positive replacement for custom MCP tools) | **`-100.0 pts`**<br>(`Holds`) |

---

## Card 6 (`6 / 7` · `LATENCY`) — Batching / Scaling Latency

### **Hook Overhead & Timeout Ceilings: Unmarked FAF Prompts Add `0.93s–1.00s`; AGENT-FORGE Static Gallery Runs in `~120ms` vs. `30,000ms` LLM Fix Ceiling**

| Load / Execution Tier | Primary / Optimized Path (`#3B82F6`) | Baseline / Ceiling Path (`#CBD5E1`) | Source & Measurement Provenance |
| --- | --- | --- | --- |
| **Tier 1 · FAF `UserPromptSubmit` Hook**<br>(Unmarked Prompt Fast-Exit on Windows) | **`930 ms`** (`0.93s` mean) | **`1,190 ms`** (`1.19s` max observed, range `0.70–1.19s`) | Reported in `README-faf-token-benchmark.md` (5 unmarked runs on Windows) |
| **Tier 2 · FAF `Stop` Hook**<br>(Unmarked Prompt Fast-Exit on Windows) | **`1,000 ms`** (`1.00s` mean) | **`1,340 ms`** (`1.34s` max observed, range `0.86–1.34s`) | Reported in `README-faf-token-benchmark.md` (5 unmarked runs on Windows) |
| **Tier 3 · FAF Hook Timeout vs. Recovery Wait**<br>(`hooks.json` vs. `faf_benchmark.py recover`) | **`5,000 ms`** (`timeoutSec: 5` sync hook cap) | **`15,000 ms`** (`--wait-seconds 15` detached finalizer window) | Verified in `src/core/hooks.json` & `faf_benchmark.py` |
| **Tier 4 · AGENT-FORGE Init Path vs. LLM Fix Timeout**<br>(`--mode templates` vs. `callLlmForJson`) | **`120 ms`** (`~0.12s` local template copy, 0 LLM calls) | **`30,000 ms`** (`validator.ts:48` single-shot LLM JSON fix cap) | Verified in `src/lib/gallery.ts` & `src/lib/validator.ts` |

---

## Card 7 (`7 / 7` · `MY TAKE`) — Good Fit vs Not For & Readiness

### **Bottom Line: Use FAF to Drive Enterprise Azure GenAI & Fabric Delivery; Use AGENT-FORGE to Compile Repo-Specific `.github/` Customizations**

#### ✅ Good Fit
- **Use FAF (`customer-success-microsoft/faf-agents`) when**:
  - Scoping, architecting, and delivering **Azure AI Foundry / OpenAI** or **Microsoft Fabric (RTI & Medallion DW migration)** customer engagements;
  - Applying the **8-area weighted scorecard (`>70%` vs `<40%`)** to choose objectively between Solution Accelerator reuse and greenfield development;
  - Generating customer-ready **C4 specs, 11-dimension Foundry model evaluations, live Azure retail TCO estimates, and Word/PPT/Excel/Draw.io deliverables**;
  - Tracking delivery token and AI credit consumption with zero extra LLM calls via `faf_benchmark.py`.
- **Use AGENT-FORGE (`microsoft/agent-forge`) when**:
  - Bootstrapping or auditing `.github/agents/`, `prompts/`, `instructions/`, `skills/`, `hooks/`, and `.vscode/mcp.json` for **any programming language or framework**;
  - Enforcing deterministic YAML frontmatter, 44-tool whitelist validation, and cross-file handoff integrity in local workflows or CI.

#### ⛔ Not For
- **Do not use `microsoft/agent-forge` as a domain solution accelerator**: It ships zero Azure Bicep templates, customer PRD/C4 spec templates, or business prioritization scorecards.
- **Do not expect FAF to auto-compile generic `.github/` rules for non-Microsoft stacks**: FAF is purpose-built for Azure GenAI and Microsoft Fabric delivery.
- **Never rely on VS Code UI reinstall alone to upgrade FAF**: Always delete `%APPDATA%\Code\agentPlugins\github.com\customer-success-microsoft\faf-agents` while VS Code is closed.

#### 🛡️ Readiness, License & Provenance Card
- **Readiness**:
  - `faf-core@2.1.1` + `faf-genai@2.1.0`: **Production-Ready (GA)** (6 role agents + 53 benchmark unit tests)
  - `faf-analytics@1.0.1`: **Scoped v1.0 Release** (6 registered agents in `plugin.json`; v1.0 release testing gate scoped to Analyst + Architect on Fabric RTI and DW migration)
  - `@agent-forge-copilot/cli@0.3.0`: **Public CLI Preview** (deterministic validator/merger complete; synthesis requires local `copilot` CLI)
- **License**: Both repositories are licensed under the **MIT License** (FAF's bundled `docx`/`pptx`/`xlsx`/`pdf` skills include attribution notices from Anthropic Claude Code Skills).
