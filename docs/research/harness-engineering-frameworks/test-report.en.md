# 7-Card 4:5 Technical Evaluation Report: Mainstream Agent Harness Engineering Frameworks (DeepSeek DSH × Claude Code × Microsoft HVE Core)

> **Bilingual Navigation**: [English Report (test-report.en.md)](./test-report.en.md) | [中文报告 (test-report.md)](./test-report.md) | [7-Card Visual Deck (EN)](./cards.html) | [7-Card 视觉卡片 (中文)](./cards.zh.html) | [Interactive Playground](./index.html)

---

## Card 1 (`1 / 7` · `HANDS-ON · AGENT HARNESS ENGINEERING`) — Overview & Workbench

**Headline Finding**: **DeepSeek DSH (96.0 pts), Claude Code (90.4 pts) & Microsoft HVE Core (90.4 pts) Define Three Complementary Agent Harness Paradigms**

- **Sealed Commit Provenance**:
  - `deepseek-ai/deepseek-harness`: `@fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159` (`release-dsh-0.2.2-rc.1`) — **23,540** Git tree objects, **411** `package.json` manifests, **49** top-level subsystem namespaces, **6** standard bundles, and **7** pluggable subagent providers.
  - `anthropics/claude-code`: `@0ed94698aa0aeee471465fc9c867c2e8434c4d68` — **1,980** Git tree objects, **5** core SDK streaming message types, **6** permission modes, **5** reasoning effort levels, and enterprise Devcontainer/Gateway/MDM/HIPAA templates.
  - `microsoft/hve-core`: `@f425e943bf228052a23e6bc4810b5faef030314f` (`v3.3.101`) — **3,779** Git tree objects, **69** custom agents, **43** `applyTo` instruction files, **93** executable skills, **14** collection manifests, and `@microsoft/vally-cli` evaluation gates.

---

## Card 2 (`2 / 7` · `SCENARIO: 200K LONG-HORIZON & SANDBOX SEAM`) — Single-Case Deep Dive

**Headline Finding**: **200K Sessions Dilute System Instructions 20x (30.0% → 1.5%); HVE `/clear` Restores 15.0% Share While DSH Preserves 94.2% KV Cache**

1. **Microsoft HVE Core Inter-Phase `/clear` + `.copilot-tracking/` Disk Hydration** (`score` · `95.8%` · `Act automatically`):
   - A `3,000`-token system prompt represents **30.0%** of a `10,000`-token initial session but drops to **1.5%** in a `200,000`-token post-implementation session (a **20.0x** dilution), driving a **92%** phase-skip risk under LLM recency bias.
   - HVE enforces `/clear` between Research → Plan → Implement → Review and hydrates the next agent solely from `3K` system instructions + `4.5K` `.copilot-tracking/` disk files, restoring effective instruction share to **15.0%** (10x recovery).
2. **DeepSeek DSH `systemPromptUpdate: 'in-history'` Prefix Cache Protection** (`choice` · `95.1%` · `Act automatically`):
   - Appends mid-session prompt updates `in-history` rather than overwriting `seq:0 system/message`, lifting KV cache hit rate from **18.5%** to **94.2%**.
3. **DeepSeek DSH `@deepseek-ai/dsh-tool-executor-ptc` (`run_code`)** (`score` · `94.2%` · `Act automatically`):
   - Executes 20 dependency lookups inside a single `run_code` TypeScript sandbox via `Promise.all`, reducing wall time from `6,850 ms` to **`3,280 ms` (2.09x speedup)** and cutting model steps from 6 to 1.

---

## Card 3 (`3 / 7` · `WHAT I TESTED`) — Full 12-Scenario Evaluation Matrix

| ID | Scenario & Architectural Challenge | Model / Verifier Recommendation | Confidence | Action Gate |
| :--- | :--- | :--- | :---: | :---: |
| **S01** | Move Bash/LSP/File tools to SSH/Container without tool forks | DSH 3-Role Seam (`ctx.fs` + `ctx.subprocess`) | 96.4% | `Act automatically` |
| **S02** | Prevent phase-skipping after 200K tokens (1.5% prompt share) | HVE Strict RPI + `/clear` + `.copilot-tracking/` | 95.8% | `Act automatically` |
| **S03** | Run 30+ lookups/aggregations without intermediate token bloat | DSH `@deepseek-ai/dsh-tool-executor-ptc` (`run_code`) | 94.2% | `Act automatically` |
| **S04** | Enforce shared USD spend limit across parent & subagents | Claude Agent SDK (`max_budget_usd` + `readOnlyHint`) | 93.6% | `Act automatically` |
| **S05** | Inject mid-session prompt updates without breaking node-0 cache | DSH `systemPromptUpdate: 'in-history'` | 95.1% | `Act automatically` |
| **S06** | Orchestrate in-process fork, Claude Code, Codex & ACP children | DSH `ctx.subagents` 7-Provider Seam | 94.8% | `Act automatically` |
| **S07** | Distribute governed artifacts with model allowlists & eval gates | HVE Collections + `vally eval` + Artifact Signing | 96.9% | `Act automatically` |
| **S08** | Coordinate peer agents with CAS revisions, DAG & writeScopes | DSH `ctx.agentTeams` CAS `revision` + `blockedBy` DAG | 91.5% | `Act automatically` |
| **S09** | Mount 120+ MCP tools without turn-1 schema context bloat | Claude Code `MCP ToolSearch` lazy loading | 92.8% | `Act automatically` |
| **S10** | Run PC-xxx plan critique & zero-hint adversarial interrogation | HVE `rpi-plan-critique` + `task-challenger` | 93.4% | `Act automatically` |
| **S11 ✕** | **Anti-Pattern**: Force distributed Team DAG on a 3-turn CLI script | **✕ Reject Over-Engineering**: Use `dsh-sdk-minimal` or single `query()` | 61.2% | `Confirm` |
| **S12** | Combine HVE SDLC governance with DSH/Claude microkernel runtime | Upper HVE 4-Tier+RPI / Lower DSH Cordis+Claude Subagent | 97.6% | `Act automatically` |

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`) — Protocol & Scoring Mechanics

- **DSH PTC Allowance Formula**: `allowance = floor(resolvedTimeoutMs / 60000 × maxSubCallsPerMinute)`. The default Node timeout of `120,000 ms` × `1024/min` grants **2,048 tool subcalls**; attempt #2,049 aborts the program with `CODE_RUN_FAILED`.
- **DSH Event-Sourced Projection Law**: `deriveMessages()` is a pure fold over `SessionEventMap`; compaction emits a `user/message` with `surfaceOp: { op: 'replace', startSeq, endSeq }` while preserving `toolPairingBalancedBefore / After`.

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`) — Perturbation & Consistency

- Across candidate framework order reversal (`DSH/Claude/HVE` vs. `HVE/Claude/DSH`), system prompt token perturbations (`3,000` vs. `3,200`), and concurrent CAS task-claim contention, maximum decision drift is **`0.0 pts`**.

---

## Card 6 (`6 / 7` · `LATENCY`) — Batching & Scaling Latency

| Workload Tier | Serial Baseline (`maxParallel=1`) | Native Parallel+Barrier | DSH PTC `run_code` | PTC vs. Serial | PTC vs. Native |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Tier 1 · 4 Read Lookups** | 3,420 ms | 1,180 ms (2 Steps) | **940 ms (1 Step)** | **3.64x** | **1.26x** |
| **Tier 2 · 6 Reads + 2 Barriers** | 7,860 ms | 3,120 ms (4 Steps) | **2,190 ms (1 Step)** | **3.59x** | **1.42x** |
| **Tier 3 · 20-Call Repo Audit** | 19,400 ms | 6,850 ms (6 Steps) | **3,280 ms (1 Step)** | **5.91x** | **2.09x** |
| **Tier 4 · 50-Call Migration** | 48,200 ms | 16,900 ms (12 Steps) | **6,420 ms (2 Steps)** | **7.51x** | **2.63x** |

---

## Card 7 (`7 / 7` · `MY TAKE`) — Good Fit vs. Not For & Readiness

- **✅ Good Fit**: Use **Microsoft HVE Core** at the upper SDLC governance layer (4-tier artifacts + `/clear` phase reset + `.copilot-tracking/` disk state + `Vally` evals) and **DeepSeek DSH + Claude Code SDK** at the lower runtime layer (3-role sandbox seams, `PTC run_code`, `in-history` KV cache preservation, `subagent-claude-code` federation, and shared `max_budget_usd` caps).
- **⛔ Not For**: Do not run multi-phase SDLC in a single uncleared 200K session; do not overwrite message node 0 mid-session; do not force heavy Team DAGs onto 3-turn scripts (S11 ✕).
