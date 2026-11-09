# Parallel Coding-Agent Worktree & HITL Plan-Review Selection FAQ: `max-sixty/worktrunk` + `backnotprop/plannotator` vs. Raw `git worktree` Commands & Terminal Scrollback Review

> **中文版 (Chinese Edition)**: [worktrunk-plannotator-hitl-vs-raw-git-worktree-selection-faq.md](worktrunk-plannotator-hitl-vs-raw-git-worktree-selection-faq.md)  
> **Related Daily Digest**: [2026-11-09 GitHub AI Trending Digest (EN)](../daily/2026-11-09.en.md) · **7-Card Benchmark Deck**: [`cards.en.html`](../cards.en.html) · **Live Dashboard**: [`github-radar.html`](../../../github-radar.html)

![max-sixty/worktrunk + backnotprop/plannotator Parallel Worktree & HITL Annotation Selection Diagram](../../../assets/github-ai-radar-2026-11-09-r4-worktrunk-plannotator.svg)

This guide is written for **AI Solution Architects and AI-Native Engineering Leads** based on primary-source verification of **`max-sixty/worktrunk` (`v0.81.0`, MIT/Apache-2.0, Rust Git worktree CLI for parallel agents, `12,222` stars, `+2,313 stars this week`)** and **`backnotprop/plannotator` (`v0.28.56`, Apache-2.0/MIT, browser & TUI plan/diff annotation surface across 9 coding agents, `9,936` stars, `+39 stars today`)**. Using plain language and first principles, it answers:
1. **When running 5–10 parallel Claude Code / Codex / Copilot CLI sessions on one machine, why does raw `git worktree add` blow up local SSDs with duplicate `target/` and `node_modules/` directories while colliding on `localhost:3000`?**
2. **Why does reviewing a 300-line agent plan inside terminal scrollback cause engineers to miss design flaws—and how does `plannotator inbox` deliver non-blocking, line-anchored plan, HTML, and diff annotations straight back into the asking agent's next turn?**
3. **How should an architect combine `worktrunk`, `plannotator`, `herdr`, and `OpenMausBot`?**

> 🛡️ **Provenance & Attribution Disclosure**:
> - **`measured` (Primary API & Trending Verification)**: GitHub REST API metadata for `max-sixty/worktrunk` (`12,222` stars, `474` forks, `v0.81.0`, Rust, Weekly Trending `#4` `+2,313 stars this week`) and `backnotprop/plannotator` (`9,936` stars, `752` forks, `v0.28.56`, TypeScript, Apache-2.0/MIT, TypeScript Daily `#10` `+39 stars today`).
> - **`anonymized_reported` (`independently_reproduced=false`, Upstream Repo Architecture Claims)**: `worktrunk` core commands (`wt switch -c -x`, `wt list --full`, `wt remove`, `wt merge`), `wt step copy-ignored` Copy-on-Write build-cache sharing (APFS/btrfs/XFS), `hash_port` template filter, and Windows `git-wt` binary alias; plus `plannotator` native plugin/MCP integration across 9 agents (`plannotator inbox`, `herdr-annotate`, `--render-html`, and Git/GitButler/Jujutsu `jj`/Perforce `p4` diff reviews), cited from their official `README.md` files.
> - **`synthetic` (`independently_reproduced=false`, Architect Parametric FinOps & Disk Model)**: Section 5.1 models a 10-engineer team running **800 parallel agent worktree tasks/month** (`8` concurrent worktrees per machine, `3.50 GB` build/dependency cache per worktree) at `$3.00/1M` input and `$15.00/1M` output tokens (API-only scope; laptop depreciation and cloud CI runner bills are marked `not_measured`): local disk drops from **`28.00 GB` to `4.55 GB` (`-83.75%`)**, and monthly rework API spend drops from Path A **`$324.00/mo` (`64.0h`)** to Path C **`$59.40/mo` (`12.0h`)**, saving **`$264.60/mo` (`-81.67%` API-only, `$3,175.20/yr`)** and **`52.0 hours/mo` (`-81.25%`)**.

---

## 1. 📌 Executive Summary

| Selection Dimension | Plain-English Takeaway (First Principles) |
| :--- | :--- |
| **What is `max-sixty/worktrunk` (`wt` / `git-wt`)?** | It is a Rust CLI that makes Git worktrees as effortless as branches for running 5–10+ AI agents in parallel. It replaces `git worktree add -b feat ../repo.feat && cd ../repo.feat && claude` with **`wt switch -c -x claude feat`**, shares `target/` and `node_modules/` across worktrees via Copy-on-Write (`wt step copy-ignored`), and assigns collision-free dev-server ports via `hash_port`. |
| **What is `backnotprop/plannotator`?** | It is a local browser and terminal (`herdr-annotate` / `plannotator-tui`) review surface and unified **Inbox (`plannotator inbox`)** for 9 coding agents. When an agent proposes a plan, renders HTML, or finishes a diff, you highlight lines, attach comments, and click Send—routing structured feedback directly to that agent's next turn without holding sessions open. |
| **Why pair them together?** | **`worktrunk` eliminates filesystem, build-cache, and port friction when spawning 8 parallel agents**; **`plannotator` eliminates human review bottleneck when steering and approving those 8 agents' plans and diffs**! |

---

## 2. 🎯 First-Principles Deep Dive (Q1 / Q2 / Q3)

### Q1: Why is plain `git worktree` painful when running 8 coding agents in parallel?

**Plain-English Answer: Plain `git worktree` only checks out tracked source files—leaving each agent with an empty `node_modules/` or `target/` cache, colliding `:3000` dev servers, and clunky 3-step shell commands!**

1. **The `node_modules/` & `target/` Duplication Tax**: Creating 8 worktrees with plain Git forces 8 separate dependency installs and cold builds, consuming `8 × 3.50 GB = 28.00 GB` of disk. `worktrunk`'s **`wt step copy-ignored`** uses filesystem Copy-on-Write (APFS on macOS, btrfs/XFS on Linux) so all 8 worktrees share existing build artifacts instantaneously (`4.55 GB` total).
2. **Dev-Server Port Collisions**: Parallel agents running web servers crash on `localhost:3000`. `worktrunk`'s **`hash_port`** template filter deterministically hashes each branch name to a unique port in lifecycle hooks.
3. **Windows `wt.exe` Conflict Resolution**: Because Windows Terminal owns `wt` on Windows, `worktrunk`'s Winget package installs **`git-wt`** alongside `wt` out of the box.

---

### Q2: Why does reviewing agent plans in terminal scrollback fail, and how does `plannotator inbox` fix it?

1. **Line-Anchored Plan, HTML & Diff Annotations**:
   - Reading a 250-line plan in a terminal forces vague prose replies (*"change step 3"*), triggering multi-turn rework. `plannotator` opens plans, live HTML artifacts (`--render-html`), and unified diffs (`Git`, `GitButler`, `Jujutsu jj`, `Perforce p4`) in a side-by-side annotation UI where comments anchor to exact lines or DOM elements.
2. **Non-Blocking Multi-Agent `plannotator inbox`**:
   - Instead of babysitting 8 terminal tabs waiting for permission prompts, `plannotator inbox` aggregates pending questions, plans, and diffs from Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Pi, Kiro, Droid, and Amp (via native plugins or `plannotator inbox mcp`).
3. **Terminal-Native Option (`herdr-annotate` & `plannotator-tui`)**:
   - Engineers who prefer staying inside the terminal can run `herdr plugin install plannotator/herdr-annotate` or `plannotator-tui`, sharing the exact same annotation store.

---

### Q3: How should an AI Solution Architect combine `worktrunk`, `plannotator`, `herdr`, and `OpenMausBot`?

- **Need full OS/VM container isolation per agent (untrusted repos or GUI CUA)** → Choose **`milind-soni/OpenMausBot`**.
- **Need high-speed local parallel coding across 5–10 branches on trusted repos**:
  - **L1 Worktree & CoW Build Cache Provisioning** → **`max-sixty/worktrunk` (`wt` / `git-wt`)**
  - **L2 Terminal Multiplexing & PTY Status** → **`herdrdev/herdr`** + `wt list --full`
  - **L3 Human-in-the-Loop Plan, HTML & Diff Annotation** → **`backnotprop/plannotator` (`plannotator inbox`)**

---

## 3. 🧭 Mermaid Selection Decision Tree & Parallel Workflow Sequence

### 3.1 Multi-Agent Local Engineering Stack Selection Decision Tree

```mermaid
flowchart TD
    Start(["🚀 Start Multi-Agent Parallel Development Stack Selection"]) --> Q_Iso{"What isolation boundary does the workload require?"}
    
    Q_Iso -- "Untrusted code / Desktop GUI automation /<br/>Dedicated container VM per bot contact" --> Maus["🖥️ Choose milind-soni/OpenMausBot<br/>4-Container Docker Compose Desktop + Permission Broker"]
    
    Q_Iso -- "Trusted enterprise repo on developer workstation<br/>Running 5–10 parallel branch agents locally" --> Q_Bottleneck{"Which local workflow bottleneck are you solving?"}
    
    Q_Bottleneck -- "L1: Worktree CLI friction, duplicate 3.5GB build caches<br/>& localhost port collisions" --> WT["🌳 Choose max-sixty/worktrunk (v0.81.0)<br/>wt switch -c -x + CoW copy-ignored + hash_port"]
    
    Q_Bottleneck -- "L2: Tracking which terminal tab is idle or blocked" --> Herdr["📟 Choose herdrdev/herdr + wt list --full<br/>Rust PTY state machine & CI/diff dashboard"]
    
    Q_Bottleneck -- "L3: Reviewing agent plans, HTML mocks & multi-file diffs<br/>with line-anchored feedback" --> Plan["✍️ Choose backnotprop/plannotator (v0.28.56)<br/>plannotator inbox (Plugin/MCP) + herdr-annotate"]

    style WT fill:#dcfce7,stroke:#16a34a,stroke-width:2.5px,color:#0f172a
    style Plan fill:#dbeafe,stroke:#2563eb,stroke-width:2.5px,color:#0f172a
    style Herdr fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#0f172a
    style Maus fill:#f3e8ff,stroke:#9333ea,stroke-width:2px,color:#0f172a
```

### 3.2 `worktrunk` + `plannotator inbox` Parallel Agent Loop

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Architect / Engineer
    participant WT as worktrunk (wt / git-wt)
    participant FS as APFS/btrfs/XFS CoW Cache
    participant Agent as Coding Agent (Claude / Codex / Copilot)
    participant Inbox as Plannotator Inbox (Browser / Herdr TUI)

    Dev->>WT: Run wt switch -c -x claude feat-payment
    WT->>FS: 1. Create Git worktree + CoW clone target/ & node_modules/ (<2s)
    WT->>WT: 2. Run post-create hook with hash_port (:3418)
    WT->>Agent: 3. Launch agent inside isolated worktree
    Agent->>Inbox: 4. Submit proposed Plan / HTML artifact / Diff to plannotator inbox
    Dev->>Inbox: 5. Highlight lines, attach inline review comments & click Send
    Inbox->>Agent: 6. Deliver structured annotations as the agent's next turn (Plugin/MCP)
    Agent->>WT: 7. Implement exact changes & pass local tests
    Dev->>WT: 8. Run wt merge (squash/rebase/merge + worktree cleanup in 1 step)
```

---

## 4. 📊 Comprehensive Selection Matrix

| Evaluation Dimension | **`worktrunk` (`v0.81.0`) + `plannotator` (`v0.28.56`)** | **Raw `git worktree` + Terminal Scrollback** | **Single-Checkout Branch Switching (`git switch`)** | **Push-First GitHub Web PR Review** |
| :--- | :--- | :--- | :--- | :--- |
| **Worktree + Agent Launch UX** | ✅ **1 command (`wt switch -c -x claude feat`)** | ❌ 3 manual commands + manual env copy | ⚠️ Serial only (1 agent at a time) | ⚠️ Cloud sandbox cold start |
| **8-Worktree Build Cache Disk** | ✅ **`4.55 GB` via CoW `wt step copy-ignored` (`-83.75%`)** | ❌ **`28.00 GB` (`8 × 3.50 GB` full duplicates)** | ✅ `3.50 GB` (no parallelism) | ✅ Local zero (burns CI minutes) |
| **Dev-Server Port Isolation** | ✅ **Automatic `hash_port` template filter** | ❌ Collides on `:3000` / `:8080` | ✅ Single server | ⚠️ Requires cloud preview URLs |
| **Plan & Diff Review Precision** | ✅ **Pre-code Plan + HTML + Diff inline annotations** | ❌ Unanchored prose in terminal scrollback | ❌ Terminal scrollback | ⚠️ Post-code only (too late for plan errors) |
| **Multi-VCS Compatibility** | ✅ **Git, GitButler, Jujutsu (`jj`), Perforce (`p4`)** | ⚠️ Git only | ⚠️ Git only | ⚠️ Pushed Git branches only |

---

## 5. 🧪 Quantitative FinOps, Disk & Engineering Hours Worked Example

### 5.1 Parametric 800-Task/Month Parallel Agent Rework & Disk Model (`synthetic`, `independently_reproduced=false`)

> 📌 **Scope & Provenance**: This closed-form model evaluates **local SSD footprint (`3.50 GB` build cache × 8 concurrent worktrees), rework LLM API token spend, and engineer context-switch hours (`synthetic`, `independently_reproduced=false`; workstation hardware and cloud CI runner bills are marked `not_measured`)** across **800 parallel agent tasks/month** at `$3.00/1M` input and `$15.00/1M` output tokens (output counted once):

| Architecture Path | 8-Worktree Local Disk Footprint | Monthly Correction Rounds & Per-Round Cost | Monthly Rework LLM API Cost (Input + Output) | Monthly Engineer Context-Switch & Cleanup Hours | Net Savings vs. Path A |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Path A: Raw `git worktree` + Terminal Scrollback Prose Corrections** | **`28.00 GB`**<br/>(`8 × 3.50 GB`) | `800 tasks × 3.00 rounds = 2,400 rounds/mo`<br/>`0.030M` in (`$0.0900`) + `0.003M` out (`$0.0450`) = `$0.1350/round` | `$216.00` in + `$108.00` out<br/>= **`$324.00 / mo`** | **`64.0 hours / mo`**<br/>(manual worktree commands, port clashes & plan misreads) | Baseline (disk bloat & multi-turn rework) |
| **Path B: Shell Aliases + Post-Push GitHub Web PR Review** | **`28.00 GB`**<br/>(no CoW sharing) | `800 tasks × 2.00 rounds = 1,600 rounds/mo`<br/>`0.025M` in (`$0.0750`) + `0.0025M` out (`$0.0375`) = `$0.1125/round` | `$120.00` in + `$60.00` out<br/>= **`$180.00 / mo`** | **`40.0 hours / mo`**<br/>(catching plan flaws only after full code push) | `-$144.00/mo` (`-44.44%` API-only) |
| **Path C: `worktrunk` (`wt` CoW) + `plannotator inbox` Inline Plan/Diff Review** | **`4.55 GB`**<br/>(**`-83.75%`** via CoW) | `800 tasks × 1.10 rounds = 880 rounds/mo`<br/>`0.015M` in (`$0.0450`) + `0.0015M` out (`$0.0225`) = `$0.0675/round` | `$39.60` in + `$19.80` out<br/>= **`$59.40 / mo`** | **`12.0 hours / mo`**<br/>(pre-code inline plan markup + 1-cmd `wt merge`) | **Saves `$264.60/mo` (`-81.67%` API-only, `$3,175.20/yr`), `52.0h/mo` (`-81.25%`) & `23.45 GB` (`-83.75%`) disk** |

---

## 6. 🛠️ Production & 30-Minute PoC Verification Checklist

- [ ] **Step 1 — Install `worktrunk` (`wt` / `git-wt` on Windows)**: Run `brew install worktrunk && wt config shell install` on macOS/Linux or `winget install max-sixty.worktrunk && git-wt config shell install` on Windows.
- [ ] **Step 2 — Enable `wt step copy-ignored` & `hash_port` Hooks**: Configure post-create hooks to CoW-clone `node_modules/` or `target/` and assign per-branch ports via `hash_port`.
- [ ] **Step 3 — Launch `plannotator inbox` & Connect Agent Plugins/MCP**: Start `plannotator inbox` (or `plannotator inbox mcp`) and verify that plans from Claude Code, Codex, and Copilot CLI appear grouped by agent thread.
- [ ] **Step 4 — Test `--render-html` & `/plannotator-review` on Local Diffs**: Annotate a rendered HTML prototype and an uncommitted diff, press Send, and confirm the agent receives line-anchored feedback on its next turn.
- [ ] **Step 5 — Reclaim Worktrees with `wt list --full` & `wt merge`**: Inspect CI status and AI branch summaries via `wt list --full`, then squash/rebase/merge and clean up completed worktrees in one command with `wt merge`.
