# Real-Time Terminal Agent HUD (`jarrodwatts/claude-hud`), Anti-Context-Rot File Planning (`OthmanAdi/planning-with-files`), Dolt Distributed Graph Issue Tracker (`gastownhall/beads`) & Whole-Codebase Semantic MCP (`zilliztech/claude-context`) Selection & Architecture FAQ

> **Document Type**: AI Solution Architect Selection & Integration Guide (2026-11-24 Night Round 31 / Cumulative Round 818)  
> **Reading Time**: ~8 minutes  
> **Covered Repositories**: [`jarrodwatts/claude-hud`](https://github.com/jarrodwatts/claude-hud) (`★ 29,298` · `1,349 forks` · JavaScript · `MIT`) · [`gastownhall/beads`](https://github.com/gastownhall/beads) (`★ 29,009` · `1,959 forks` · Go · `MIT`) · [`OthmanAdi/planning-with-files`](https://github.com/OthmanAdi/planning-with-files) (`★ 28,219` · `2,331 forks` · Shell · `MIT`) · [`zilliztech/claude-context`](https://github.com/zilliztech/claude-context) (`★ 12,725` · `941 forks` · TypeScript · `MIT`)  
> **Evidence Provenance**: GitHub REST API verified metadata (2026-11-24) and sealed local evidence files `trending-daily-2026-11-24-raw.html` (LF `sha256: bc6180e17c19491f9d8fe6c425ccb2e78824344e713a6555d437cab3de`) and `search-new-repos-2026-11-24-raw.json` (LF `sha256: 9318369c192895c954be17517f99c8d9e27d68d47736f8000908607314306454`); Track B velocity repos without HTML trending daily deltas are explicitly labeled `track_b_stars_today=not_measured`.  
> **中文版本**: [`claude-hud-beads-pwf-claude-context-selection-faq.md`](./claude-hud-beads-pwf-claude-context-selection-faq.md)

![2026-11-24 Night Round 31 R818 Architecture Summary](../../../assets/github-ai-radar-2026-11-24-r31-r818-claude-hud-beads-pwf-claude-context.svg)

---

## ① 📌 Executive Summary

**One-Sentence Selection Verdict**: When enterprise engineering teams running multi-hour agentic refactoring sessions need to **eliminate context rot, unexpected compaction amnesia, multi-agent task collisions, and blind grep loops**—combining **an always-visible terminal HUD showing live context usage, rate limits, active tools, and sub-agents (`jarrodwatts/claude-hud`), Manus-style crash-proof file planning with per-turn re-injection across `/clear` and compaction (`OthmanAdi/planning-with-files`), a Dolt-powered distributed dependency-graph issue tracker (`gastownhall/beads`), and whole-codebase AST + semantic search over MCP (`zilliztech/claude-context`)**—deploying this 100% `MIT`-licensed stack cuts monthly TCO for a 45-engineer team from **`$9,320.00/mo`** (Path A: Context-Rot Rework After Compaction + Unmonitored Token Burn + Commercial Code Search SaaS) to **`$305.00/mo`** (Path C), saving **`$9,015.00/mo` (`-96.73%`)**.

| Dimension | `jarrodwatts/claude-hud` (L1 Real-Time Agent HUD) | `OthmanAdi/planning-with-files` (L2 Anti-Rot File Planning) | `gastownhall/beads` (L3 Dolt Graph Issue Tracker) | `zilliztech/claude-context` (L4 Whole-Codebase MCP) |
|---|---|---|---|---|
| **Verified Stars & Forks** | `★ 29,298` · `1,349 forks` | `★ 28,219` · `2,331 forks` | `★ 29,009` · `1,959 forks` | `★ 12,725` · `941 forks` |
| **Language & License** | JavaScript (`MIT`) | Shell / Hooks (`MIT`) | Go (`MIT`) | TypeScript (`MIT`) |
| **Plain-English Positioning** | Always-visible Claude Code HUD displaying context usage, rate limits, active tools, running sub-agents & todo progress | Manus-style persistent file planning across 60+ agents with session recovery after `/clear`, per-turn re-injection & completion gates | `bd` (Beads): distributed graph issue tracker and memory upgrade for coding agents powered by Dolt | Zilliz's code search MCP server making an entire codebase the semantic context for any coding agent |
| **Core Enterprise Pain Solved** | Gives developers real-time visibility into context window saturation and rate limits before compaction degrades output quality | Prevents agents from forgetting architectural constraints or skipping subtasks after `/clear`, crashes, or context compaction | Replaces flat todo lists with a version-controlled Dolt dependency graph (`bd ready`) across branches and sessions | Eliminates 20-turn blind `grep` loops when searching unfamiliar monorepos for conceptual or architectural patterns |
| **When to Choose vs Cloud PaaS** | Essential status bar for every engineer using Claude Code daily | Mandatory for any coding task lasting >20 minutes or spanning 5+ files across 60+ CLI agents | Choose for multi-session, multi-agent epics with complex task prerequisite graphs | Choose for whole-monorepo semantic search; pair with `serena` (Round 14) for symbol-level LSP edits |

---

## ② 🎯 Architect & Customer Q&A (1–2 Minute Read)

### Q1: Why do coding agents degrade sharply ("context rot") after 45 minutes or right after automatic context compaction, and how do `jarrodwatts/claude-hud` (`★ 29,298`) and `OthmanAdi/planning-with-files` (`★ 28,219`) prevent it?
- **The Pain**: As the context window fills above 75%, early architectural constraints fade from attention or get stripped during lossy compaction—and without a HUD, developers never see compaction coming.
- **Architect's Dual Defense**:
  1. **Real-Time Telemetry via `jarrodwatts/claude-hud` (`MIT`)**: Sits directly below your input line showing **live context window percentage, rate limits, active tools, running sub-agents, and todo progress**, alerting engineers before the context window saturates.
  2. **Crash-Proof External Working Memory via `OthmanAdi/planning-with-files` (`MIT`)**: Maintains persistent Markdown planning files (`task_plan.md`, `findings.md`, `progress.md`) across 60+ coding agents (Claude Code, Codex, Cursor, OpenCode), **re-injecting plan state on every turn against context rot**, recovering seamlessly after `/clear` or compaction, and enforcing a **deterministic completion gate**.

### Q2: How does Steve Yegge's `gastownhall/beads` (`★ 29,009`) go beyond single-session Markdown checklists?
- **Dolt-Powered Distributed Dependency Graphs (`bd`)**: While `planning-with-files` governs the active session's working memory, multi-day epics require tracking hundreds of interdependent tasks across branches. Powered by **Dolt** (version-controlled SQL), `gastownhall/beads` (`MIT`) gives agents a **distributed graph issue tracker** where `bd ready` deterministically returns only tasks whose upstream prerequisites are 100% complete.

### Q3: Where does `zilliztech/claude-context` (`★ 12,725`) fit in the developer workflow?
- **Whole-Codebase Semantic Context over MCP**: When an agent needs to find *"where retry backoff is implemented across payment microservices"* without knowing exact symbol names, `zilliztech/claude-context` (`MIT`) combines AST-aware code chunking with Milvus/Zilliz vector search over MCP—returning exact relevant code blocks in one tool call.

---

## ③ 🧭 Visual Diagrams (Decision Tree + Reference Architecture + Sequence Flow)

### 3.1 Selection Decision Tree

```mermaid
flowchart TD
    A["Enterprise Long-Horizon Coding Agent Telemetry, Planning, Dependency Graph & Search Need"] --> B{"Which failure mode is hurting velocity most?"}
    B -->|"No visibility into context %, rate limits, active tools or sub-agents"| C["Adopt jarrodwatts/claude-hud (★29.2k, JS, MIT)"]
    B -->|"Agents forget plans after /clear, compaction, or long multi-turn runs"| D["Adopt OthmanAdi/planning-with-files (★28.2k, Shell, MIT)"]
    B -->|"Multi-branch, multi-session epics need a distributed dependency graph"| E["Adopt gastownhall/beads (★29.0k, Go, MIT)"]
    B -->|"Agents waste tokens grepping blindly across large monorepos"| F["Adopt zilliztech/claude-context (★12.7k, TS, MIT)"]
    B -->|"100% Cloud-hosted repository search & enterprise cloud issue tracking"| G["Use GitHub Copilot Enterprise + GitHub Issues"]
```

### 3.2 End-to-End Enterprise Production Reference Architecture

```mermaid
flowchart LR
    subgraph L1_HUD["L1: Live Terminal Telemetry (Claude HUD)"]
      HUD["jarrodwatts/claude-hud<br/>Context % · Rate Limits · Active Tools · Sub-Agents"]
    end

    subgraph L2_Plan["L2: Anti-Context-Rot File Planning (PWF)"]
      PWF["OthmanAdi/planning-with-files<br/>Crash-Proof Markdown Plans + /clear Recovery + Completion Gate"]
    end

    subgraph L3_Graph["L3: Distributed Graph Issue Tracker (Beads / bd)"]
      BDS["gastownhall/beads<br/>Dolt-Backed Task Dependency Graph (bd ready)"]
    end

    subgraph L4_Context["L4: Whole-Codebase Semantic Search MCP"]
      CTX["zilliztech/claude-context<br/>AST Chunking + Hybrid Vector Code Search MCP"]
    end

    HUD <-->|"Trigger proactive /clear at 75% context"| PWF
    BDS -->|"Dispatch unblocked tasks via bd ready"| PWF
    PWF -->|"MCP: Semantic codebase lookup"| CTX
    PWF -->|"Close verified node in Dolt graph"| BDS
```

### 3.3 End-to-End Execution Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Solution Architect / Senior Engineer
    participant BDS as gastownhall/beads (L3 Dolt Graph)
    participant PWF as planning-with-files (L2 File Planner)
    participant HUD as claude-hud (L1 Terminal HUD)
    participant CTX as claude-context (L4 Code Search MCP)

    Dev->>BDS: 1. Run `bd ready` to pull next unblocked refactoring task from Dolt graph
    BDS-->>PWF: 2. Initialize 3-file persistent Markdown plan for task #42
    PWF->>CTX: 3. Query claude-context MCP for all cross-service idempotency handlers
    CTX-->>PWF: 4. Return AST-chunked code matches; log discoveries into findings.md
    HUD-->>Dev: 5. HUD displays Context at 78% & 2 active sub-agents finishing
    Dev->>PWF: 6. Execute `/clear`; planning-with-files re-injects exact plan & progress into fresh window
    PWF->>PWF: 7. Complete remaining steps & pass Deterministic Completion Gate
    PWF->>BDS: 8. Mark task #42 done in Dolt graph, unlocking downstream tasks #43 & #44
```

---

## ④ 📊 Comparative Selection Matrix: OSS Stack vs. Peer OSS vs. Cloud PaaS

| Dimension | This OSS Stack (`claude-hud` + `planning-with-files` + `beads` + `claude-context`) | Unassisted CLI Workflow (`Blind Terminal` + `In-Chat Plans` + `Raw Grep`) | Managed Cloud Stack (`GitHub Copilot Enterprise` + `Zilliz Cloud` + `Azure Boards`) |
|---|---|---|---|
| **Core Role** | Live terminal HUD + crash-proof file planning + Dolt dependency graph + semantic code MCP | Zero context telemetry + ephemeral chat plans lost on compaction + keyword grep | Cloud repo indexing + managed vector cloud + enterprise web ALM |
| **Best-Fit Scenario** | Multi-hour refactors, 60+ CLI agents, distributed multi-agent epics & large monorepo search | Quick 5-minute single-file bug fixes | Cloud-standardized enterprises preferring managed web dashboards |
| **Integration Effort** | **Very Low** (100% `MIT`; installable via plugin marketplace, `npx`, and Go binary in <10 min) | None (Built-in defaults, but high rework rate on long tasks) | Medium (Cloud indexing permissions and per-seat enterprise licensing) |
| **Operational Complexity** | **Very Low** (Local files + embedded Dolt DB + shared Milvus container; ~`2.4h/mo` ops) | Very High (Recovering from compaction amnesia and blind grep loops costs ~`45.5h/mo`) | Low (Managed cloud services, plus ~`10.5h/mo` board and index admin) |
| **License & Compliance** | **100% `MIT` License across all 4 repositories** | N/A | Proprietary per-seat and per-vector cloud terms |
| **45-Engineer Monthly TCO** | **`$305.00/mo`** (`$65.00` shared internal Milvus node + `2.4h` ops) | ~`$4,620.00/mo` (Wasted full-window tokens + `45.5h` context-rot rework) | **`$2,890.00/mo`** (Path B) to **`$9,320.00/mo`** (Path A commercial stack) |

---

## ⑤ 🧪 Quantitative ROI & Closed-Form FinOps TCO Comparison

> **Provenance Disclosure**: The TCO table below is a closed-form synthetic architectural model (`provenance: synthetic`, `independently_reproduced: false`) for a **45-engineer enterprise software engineering team** running 4 long-horizon refactoring sessions per engineer per day across a multi-service monorepo (`$100.00/hr` loaded engineering rate). Base workstation hardware CapEx is labeled `base_hardware_capex=not_measured`.

| Cost Component | Path A: Compaction Amnesia Rework + Unmonitored Context Burn + Commercial Code Search SaaS | Path B: GitHub Copilot Enterprise + Managed Zilliz Cloud + Azure Boards | Path C: `claude-hud` + `planning-with-files` + `beads` + `claude-context` |
|---|---|---|---|
| **Monthly API / SaaS / Cloud Spend** | **`$4,770.00`** (Repeated 95%-full context window token billing + blind grep loops + code search seats) | **`$1,840.00`** (Enterprise seat tier + managed vector cloud) | **`$65.00`** (Internal shared Milvus container for `claude-context`; `$0` license fees across all 4 `MIT` tools) |
| **Monthly Context-Rot Rework & Task Alignment Labor** | `45.5h` (Redoing work lost after compaction/crashes + manual task dependency tracking) | `10.5h` (Cloud board sync & index administration) | **`2.4h`** (Proactive `/clear` guided by `claude-hud` + lossless `planning-with-files` recovery + `bd ready`) |
| **Monthly Labor Cost (`$100.00/hr`)** | **`$4,550.00`** (`45.5 * 100.00`) | **`$1,050.00`** (`10.5 * 100.00`) | **`$240.00`** (`2.4 * 100.00`) |
| **Total Monthly TCO** | **`$9,320.00 / mo`** | **`$2,890.00 / mo`** | **`$305.00 / mo`** |
| **Net Monthly Savings vs. Path A** | Baseline (`$0.00`) | Saves `$6,430.00 / mo` (`-68.99%`) | **Saves `$9,015.00 / mo` (`-96.73%`)** |

---

## ⑥ 🛠️ Enterprise Architecture Review & Adoption Checklist

- [ ] **Proactive 75% Context Reset Policy (`jarrodwatts/claude-hud` & `OthmanAdi/planning-with-files`)**: Train engineers to watch `claude-hud`'s live context gauge and run `/clear` proactively at ~75% capacity after `planning-with-files` flushes findings to disk—avoiding lossy auto-compaction and cutting per-turn input token costs.
- [ ] **Deterministic Completion Gate Enforcement (`OthmanAdi/planning-with-files`)**: Keep the `planning-with-files` completion gate active so coding agents cannot terminate a turn while required test or verification checkboxes remain open.
- [ ] **Dolt Graph Prerequisite Locking (`gastownhall/beads`)**: Model cross-module refactoring dependencies in `bd` (`gastownhall/beads`) so parallel agents only claim tasks surfaced by `bd ready`.
- [ ] **On-Premise Milvus Deployment for Proprietary Code (`zilliztech/claude-context`)**: Point `zilliztech/claude-context` at a self-hosted internal Milvus instance and internal embedding endpoint so proprietary source code chunks never leave your corporate network.
