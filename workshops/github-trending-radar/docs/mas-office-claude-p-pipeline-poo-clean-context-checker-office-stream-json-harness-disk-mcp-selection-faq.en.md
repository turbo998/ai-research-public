# Clean-Context Checker Multi-Agent Office (`weixijia/mas-office`), Persistent `claude -p` Harness (`claude-p-pipeline`) & Disk Cleanup MCP (`morajabi/poo`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 36 (Cumulative Round 460 Milestone)  
> **Tracked Repositories**:
> - **`weixijia/mas-office`** (`★ 98`, JavaScript / Zero-Dependency Protocol `v0.2` & `v0.3.0` Engine, `MIT`): Framework-agnostic multi-agent protocol and live isometric office running on real signed-in Claude Code and Codex sessions (`mas-office up`) with locked role tools, a dependency-aware **`"Needs you"` inbox**, and an independent **clean-context checker** that verifies every URL link and source-tagged claim
> - **`Saekisui/claude-p-pipeline`** (`★ 98`, JavaScript / 26-Chapter Reference + 0-Dep `mini-chat` Skeleton + 6-Check `npm run smoke`, `AGPL-3.0`) & **`morajabi/poo`** (`★ 70`, Rust / macOS Menu Bar + Linux/macOS CLI + MCP Server, `MIT`): Complete engineering guide and runnable harness for persistent `claude -p` bidirectional `stream-json` pipelines (auto-stripping `ANTHROPIC_API_KEY` to prevent accidental per-token billing and surviving reconnects via `--resume`), paired with a Rust disk-space cleaner MCP (`poo`) that groups reclaimable builds, caches, simulators, and agent worktrees by cleanup cost  
> **Audit Claim ID**: `CLAIM-20261117-R36-MASOFFICE-CLAUDEP` (base personal Claude Pro/Max subscription marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Engineering Teams Running Multi-Agent Research Loops and Local `claude -p` Automations Hit Three Operational Pitfalls: Self-Confirming Hallucinations, Accidental API-Key Billing Leaks, and Worktree Disk Exhaustion**:
   - **Pitfall 1 — Self-Confirming Multi-Agent Hallucinations**: When a research agent gathers web sources and evaluates its own synthesis inside the same polluted context window, confirmation bias causes broken URLs and misread figures to pass unchecked into final decision reports.
   - **Pitfall 2 — Silent `ANTHROPIC_API_KEY` Billing Fallback & CLI Upgrade Regressions**: When `ANTHROPIC_API_KEY` is present in a developer's shell environment, `claude -p` silently bypasses the user's flat-rate Pro/Max subscription and bills per token against the API key. Meanwhile, frequent Claude Code CLI updates can break undocumented flags (`--system-prompt-snapshot off`, `--resume`, thinking blocks) without an automated smoke suite.
   - **Pitfall 3 — Build & Agent Worktree Disk Exhaustion**: Parallel agent sessions leave behind tens of gigabytes of Rust/Node build artifacts, Xcode simulator caches, and stale Git worktrees.
   - **The Solution Architect Stack (`mas-office` MIT + `claude-p-pipeline` + `morajabi/poo` MIT)**: Orchestrate multi-agent research inside **`weixijia/mas-office`** (`MIT`, locking each role's tools in code, surfacing blocking approvals in one `"Needs you"` inbox, and grading every claim/URL in a **clean-context checker** session); harden personal `claude -p` automations using **`Saekisui/claude-p-pipeline`** (stripping `ANTHROPIC_API_KEY` at spawn and gating CLI upgrades on the 6-check `npm run smoke` suite); and reclaim workstation storage safely via **`morajabi/poo`** (`MIT`, Rust CLI, menu-bar app, and MCP server grouping reclaimable gigabytes by rebuild cost).
2. **Closed-Form FinOps Impact (30 Engineering & Research Seats Running 35,000 Monthly Multi-Agent Research, Local Pipeline & Disk Hygiene Ops at `$95.00/hr`)**:
   - Transitioning from **Path A (Unchecked Multi-Agent Loops + Accidental `ANTHROPIC_API_KEY` Billing Leaks & Manual Disk Cleanup at `$5,705.00/mo`)** to **Path C (`mas-office` + `claude-p-pipeline` + `poo` MCP Stack at `$341.00/mo`)** saves **`$5,364.00/mo` (`-94.02%`, or `$64,368.00/yr`)** while cutting manual link/citation audits, stream-disconnect debugging, and disk cleanup labor from `37.0 hrs/mo` to `2.8 hrs/mo` (**`92.43%` reduction**).

![MAS Office + claude-p-pipeline + Poo Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r36-mas-office-claude-p-poo.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `weixijia/mas-office` enforce locked role boundaries, dependency-aware human approvals, and clean-context claim verification?
- **Plain-Language Definition**: `MAS Office` (`MIT`, zero dependencies, Protocol `v0.2` / `v0.3.0`) is a **framework-agnostic multi-agent runtime and live isometric office where every desk is a real local Claude Code or Codex session (`mas-office up`)**.
- **Three Architectural Safeguards**:
  1. **Locked Team Design & Code-Enforced Tool Boundaries**: You design the roles (`Retail finder`, `Market finder`, `Catch checker`, `Lead`) and lock the configuration; deterministic plain code schedules execution and enforces each role's allowed tools, while JS and Python SDKs let you visualize any external multi-agent framework in the same office UI;
  2. **Dependency-Aware `"Needs you"` Inbox**: Tool approvals, clarifying questions, stuck roles, checker flags, and stage checkpoints from all sessions converge in one `"Needs you"` inbox—explicitly stating which downstream roles are held up (e.g., *"holds up the Catch checker and the Lead"*) with inline `Allow once`, `Deny`, or reply actions;
  3. **Independent Clean-Context Claim & Link Checker**: Every claim in a draft report must carry its source tag; each link is verified deterministically, and a dedicated **checker role running in a clean context** independently judges every claim against its cited source.

### Q2: What production lessons does `Saekisui/claude-p-pipeline` codify for `claude -p`, and how does `morajabi/poo` safely reclaim agent disk space?
- **`Saekisui/claude-p-pipeline` (26-Chapter Reference + 0-Dep `mini-chat` Skeleton + 6-Check `npm run smoke`)**:
  1. **Preventing Silent API-Key Billing (`env -u ANTHROPIC_API_KEY`)**: Automatically strips `ANTHROPIC_API_KEY` when spawning `claude -p` so personal local pipelines never accidentally bill per token instead of using the logged-in subscription;
  2. **Persistent Bidirectional `stream-json` + `--resume` Crash Recovery**: Maintains one long-lived `claude -p` process per chat window with SSE heartbeats, hot-swappable personas (`--system-prompt-snapshot off`), per-window MCP routing, and seamless `--resume` reconciliation when a browser tab closes or the server restarts;
  3. **6-Check CLI Upgrade Smoke Suite (`npm run smoke`)**: Runs 6 automated checks on an isolated port using `haiku` after every Claude Code upgrade to verify streaming, thinking blocks, image uploads, MCP calls, and reconnects (strictly enforcing personal/single-owner subscription terms in §25).
- **`morajabi/poo` (Cost-Grouped Rust Disk Cleaner App, CLI & MCP Server, `MIT`)**:
  - Scans builds, package caches, Xcode simulators, and orphaned **agent worktrees**, grouping reclaimable space by **"what a clean costs you"** (zero-penalty unused caches vs. artifacts that require a rebuild) and exposing safe cleanup tools over an **MCP server and Agent Skill**.

### Q3: How should an AI Solution Architect combine `mas-office`, `claude-p-pipeline`, and `poo`?
- **Workstation Runtime & Storage Layer (`claude-p-pipeline` + `poo` MCP)**: Strip `ANTHROPIC_API_KEY` in personal `claude -p` wrappers, run `npm run smoke` after CLI updates, and attach `poo`'s MCP server so agents can safely free gigabytes of stale build/worktree caches on demand.
- **Multi-Agent Research & Verification Layer (`mas-office`)**: Run multi-role feasibility, pricing, and literature investigations through `mas-office up` so every output passes through the `"Needs you"` inbox and the clean-context `Catch checker`.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph HostHygiene["Local Runtime &amp; Storage Hygiene: claude-p-pipeline (★98) + morajabi/poo (★70, MIT)"]
        A[Workstation Claude Code / Codex Environment] --> B[claude-p-pipeline Discipline<br/>Strip ANTHROPIC_API_KEY at Spawn + npm run smoke 6-Check Gate]
        A --> C[morajabi/poo Rust CLI &amp; MCP Server<br/>Group Builds / Simulators / Agent Worktrees by Cleanup Cost]
    end

    subgraph MasOffice["Locked-Role Multi-Agent Office: weixijia/mas-office (★98, MIT)"]
        B & C --> D[mas-office up Launches Locked Role Team<br/>Deterministic Code Scheduler + Hard Role Tool Limits]
        D --> E[Needs You Unified Inbox<br/>Shows Held-Up Downstream Roles + Allow / Deny / Reply]
        E --> F[Independent Clean-Context Catch Checker<br/>Verifies Every URL Link + Judges Every Source-Tagged Claim]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Unchecked Multi-Agent Loops + Raw `claude -p` Spawns | Option B: Single-Session Prompts + Manual `rm -rf` Scripts | **Option C (Recommended): `mas-office` (MIT) + `claude-p-pipeline` + `poo` (MIT)** |
| :--- | :--- | :--- | :--- |
| **Multi-Agent Claim & Link Verification** | ❌ Same polluted context writes and self-approves hallucinated links | ⚠️ Long-context attention drift misses subtle citation errors | ✅ **Source-tagged claims + deterministic URL checks + independent clean-context checker** |
| **Role Tool Isolation & Approval Prioritization** | ❌ Scattered terminal prompts hide which approval blocks the critical path | ✅ Single thread, but slow sequential execution | ✅ **Code-locked role tools + `"Needs you"` inbox showing held-up downstream roles** |
| **`ANTHROPIC_API_KEY` Leak Prevention & Upgrade QA** | ❌ Leftover env keys trigger silent per-token bills; CLI updates break flags | ⚠️ Discovered only after monthly billing shock or broken runs | ✅ **Auto-strips `ANTHROPIC_API_KEY` at spawn + 6-check `npm run smoke` upgrade gate** |
| **Safe Build & Agent Worktree Disk Reclamation** | ❌ Stale worktrees and build caches silently fill workstation SSDs | ❌ Blind `rm -rf` scripts risk deleting active worktrees | ✅ **`poo` Rust CLI/MCP groups reclaimable space by rebuild cost for safe cleanup** |
| **Monthly TCO (30 Seats / 35,000 Ops/Mo)** | **`$5,705.00 / mo`** (`$2,190` API leaks/SSD + `37.0 hrs` link/stream fixes) | **`$2,525.00 / mo`** (`$910` compute + `17.0 hrs` manual checks/cleanup) | **`$341.00 / mo`** (**`-94.02%` savings**; `$75` local runners + `2.8 hrs` inbox/smoke review) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R36-MASOFFICE-CLAUDEP`)

> **Scope & Boundary Declaration**: Evaluated for 30 engineering and technical research seats running **35,000 monthly multi-agent research workflows, local `claude -p` pipeline turns, and workstation disk cleanups** at a blended engineering rate of `$95.00/hr` (base personal Claude Pro/Max subscription marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Accidental API Leak \& SSD Spend} + (\text{Citation Verification, Stream Fix \& Disk Cleanup Hours} \times \$95.00)$$

| Cost Component | Path A: Unchecked Multi-Agent + Env-Key Leaks | Path B: Single-Session Prompts + Manual `rm -rf` | **Path C: `mas-office` + `claude-p-pipeline` + `poo` MCP** |
| :--- | :---: | :---: | :---: |
| **Monthly Accidental API Billing Leaks & SSD Expansion** | `$2,190.00` | `$910.00` | **`$75.00`** |
| **Monthly Citation Audit, Stream Fix & Disk Cleanup Hours** | `37.0 hrs` | `17.0 hrs` | **`2.8 hrs`** (**`92.43%` reduction**) |
| **Monthly Engineering & Research Labor (`@ $95.00/hr`)** | `$3,515.00` | `$1,615.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,705.00`** | **`$2,525.00`** (`-55.74%`) | **`$341.00`** (**`-94.02%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,180.00 / mo` (`$38,160/yr`) | **`$5,364.00 / mo` (`$64,368.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Launch Locked Multi-Agent Research Teams in `weixijia/mas-office`**: Run `mas-office up` on local Claude Code and Codex sessions, lock role tool permissions in code, manage approvals from the `"Needs you"` inbox, and require every claim and URL to pass the clean-context `Catch checker`.
- [ ] **Step 2 — Strip `ANTHROPIC_API_KEY` & Run `npm run smoke` on Personal `claude -p` Pipelines**: Apply `Saekisui/claude-p-pipeline`'s spawn hygiene (`env -u ANTHROPIC_API_KEY`) and execute the 6-check `npm run smoke` suite after every Claude Code CLI update (strictly honoring single-owner personal use).
- [ ] **Step 3 — Install `morajabi/poo` & Register Its Disk Cleanup MCP Server**: Run `curl -fsSL poo.morajabi.com/install | sh` (SHA-256 verified) on macOS/Linux workstations and enable its MCP server and Agent Skill.
- [ ] **Step 4 — Automate Zero-Penalty Cache & Stale Worktree Reclamation**: Instruct coding agents to query `poo` over MCP whenever free disk drops below threshold, cleaning zero-cost cache groups first while preserving active branches.
