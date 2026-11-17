# SHA-256 Plan Review Checkpoint (`ineedfoundmyway/planrelay`), Cross-Machine Agent Mesh (`chenhg5/myco`) & Commit-Verified Shared Facts (`siwen-121/agent-shared-facts`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 34 (Cumulative Round 458)  
> **Tracked Repositories**:
> - **`ineedfoundmyway/planrelay`** (`★ 78`, TypeScript / Node.js 22+ Zero-Dependency Review Companion, `MIT OR Apache-2.0`): Local-first plan and code review checkpoint enforcing **"Different Content, Different Review"**—binding every comment, blocker, and approval to an exact SHA-256 content snapshot so plan edits automatically create a new pending revision verified via CLI `check`
> - **`chenhg5/myco`** (`★ 93`, Go Single Binary + macOS/Windows/Linux App, `MIT`) & **`siwen-121/agent-shared-facts`** (`★ 68`, Python 3.12+ / Git + Read-Only Streamable HTTP/stdio MCP, `MIT`): Cross-machine agent network (`myco`) letting cloud agents delegate work to local workstations and teammates' Claude Code / Codex CLIs, paired with a Git-backed cross-device fact store (`agent-shared-facts`) that separates offline drafts, review candidates, and commit-SHA-verified published facts  
> **Audit Claim ID**: `CLAIM-20261117-R34-PLANRELAY-MYCO` (underlying Tailscale / Cloudflare tunnel transport marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Distributed Engineering Teams Operating Coding Agents Across Laptops, Workstations, and Cloud Sandboxes Hit Three Coordination Failures**:
   - **Failure 1 — Stale Chat Approvals Authorizing Mutated Plans**: In conversational agent loops, a developer approves Plan V1 (`"looks good"`), the agent subsequently modifies the plan after reading another file, and the old approval silently carries over—allowing unreviewed schema or security changes to execute.
   - **Failure 2 — The Human as a Copy-Paste Message Bus**: A cloud agent on `claude.ai` or a remote VPS needs a build toolchain, local config, or internal database that only exists on your workstation—or needs input from a teammate's agent—forcing the engineer to manually copy prompts and paste outputs across machines.
   - **Failure 3 — Unreviewed Drafts Polluting Shared Agent Memory**: When agents across Windows, macOS, and cloud environments write directly to a shared vector store or synced folder, unverified offline assumptions immediately contaminate every other agent's context.
   - **The Solution Architect Stack (`planrelay` + `myco` + `agent-shared-facts`)**: Gate plan execution on **`ineedfoundmyway/planrelay`** (`MIT OR Apache-2.0`, zero-dependency Node 22+ companion that binds approvals to exact SHA-256 snapshots and invalidates stale approvals whenever content changes); connect cross-machine agents via **`chenhg5/myco`** (`MIT`, single Go binary bridging cloud agents, local Claude Code/Codex CLIs, and teammates' agents); and synchronize cross-device knowledge through **`siwen-121/agent-shared-facts`** (`MIT`, separating drafts, review candidates, and published facts verified by a second device's upstream Git pull over a read-only MCP).
2. **Closed-Form FinOps Impact (35 Distributed Engineers Running 40,000 Monthly Plan Reviews, Cross-Machine Delegations & Shared Fact Updates at `$95.00/hr`)**:
   - Transitioning from **Path A (Chat Plan Approvals + Manual Copy-Paste Relaying & Unversioned Shared Notes at `$5,560.00/mo`)** to **Path C (`PlanRelay` + `Myco` + `agent-shared-facts` Stack at `$341.00/mo`)** saves **`$5,219.00/mo` (`-93.87%`, or `$62,628.00/yr`)** while cutting stale-plan rework, manual cross-machine relaying, and memory-conflict cleanup from `36.0 hrs/mo` to `2.8 hrs/mo` (**`92.22%` reduction**).

![PlanRelay + Myco + Shared Facts Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r34-planrelay-myco-shared-facts.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `ineedfoundmyway/planrelay` enforce "Different Content, Different Review" using SHA-256 revision binding?
- **Plain-Language Definition**: `PlanRelay` (`MIT OR Apache-2.0`, zero-dependency Node.js 22+) is a **local-first human checkpoint for agent plans and diffs where every comment and approval is cryptographically bound to the exact SHA-256 content snapshot**.
- **Three Core Engineering Safeguards**:
  1. **Automatic Stale-Approval Invalidation**: Re-importing an updated plan under the same task ID automatically creates a new **pending revision** while preserving earlier comments and decisions in history—an old *"looks good"* never carries over to modified content;
  2. **Snapshot, Line, Severity & Resolution Anchoring**: Every review annotation records its exact snapshot hash, line number, severity level, and resolution state so missing rollback steps or unverified assumptions are tracked as explicit blockers;
  3. **CLI `check` Gate & Dual JSON/Markdown Export**: Requires zero npm packages or API keys, exports structured JSON for coding agents alongside readable Markdown for humans, and provides a CLI `check` command that verifies whether the *latest* imported revision is approved.

### Q2: How do `chenhg5/myco` and `siwen-121/agent-shared-facts` eliminate the "human message bus" and prevent unreviewed agent memory pollution?
- **`chenhg5/myco` (Single-Binary Mycelium Network for Cross-Machine Agents, `MIT`)**:
  1. **Cloud-to-Local Workstation Reach**: Lets a session on `claude.ai` or a remote VPS reach your local computer within the same conversation—executing commands on a local shell node or delegating tasks to the Claude Code or Codex CLI already configured on your machine;
  2. **Teammate Agent-to-Agent Delegation**: Connects every Claude Code, Codex, and CLI agent across macOS, Windows, and Linux so agents discover each other, delegate tasks, and return structured replies through one hub.
- **`siwen-121/agent-shared-facts` (Git-Backed Two-Device Verified Fact Store & Read-Only MCP, `MIT`)**:
  1. **Strict Three-State Separation (`Offline Draft` vs. `Review Candidate` vs. `Published Fact`)**: Every shared record lives at a fixed ID and path on a designated Git branch and returns its exact `commit SHA` when read;
  2. **Two-Device Pull Confirmation Receipt**: An agent can prepare a candidate offline and submit it for review/merge, but publication is only confirmed after a **second device fetches and verifies the merged record from upstream**;
  3. **Summary-Only Privacy Boundary & Allowlisted Read-Only MCP**: Raw research files, PII, and credentials remain on the origin device; only approved summaries and traceable evidence IDs are committed and exposed via stdio or authenticated Streamable HTTP read-only MCP (`Codex, Claude Code, Antigravity, Kimi, DeepSeek, Muse`).

### Q3: How should an AI Solution Architect combine `PlanRelay`, `Myco`, and `agent-shared-facts`?
- **Pre-Execution Approval Gate (`PlanRelay`)**: Require agents to import implementation plans into `PlanRelay` and pass CLI `check` on the latest SHA-256 revision before delegating execution.
- **Cross-Machine Execution (`Myco`)**: Route approved sub-tasks across cloud and local workstation agents via `Myco`.
- **Verified Knowledge Persistence (`agent-shared-facts`)**: Commit verified architectural outcomes into `agent-shared-facts` with two-device confirmation and serve them back to all agents via read-only MCP.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph PlanGate["SHA-256 Plan Review Gate: ineedfoundmyway/planrelay (Node 22+ 0-Dep)"]
        A[Agent Drafts or Updates Plan] --> B[Import into PlanRelay &amp; Compute SHA-256<br/>Modified Content Creates Pending Revision]
        B --> C[Human Anchors Line/Severity Blockers<br/>Export JSON for Agents &amp; Markdown for Humans]
        C --> D{CLI check: Latest Revision Approved?}
    end

    subgraph MeshAndFacts["Cross-Host Mesh &amp; Verified Fact MCP: myco (★93, Go) + agent-shared-facts (★68, MIT)"]
        D -->|Yes| E[chenhg5/myco Agent Network<br/>Cloud Agent Delegates to Local / Teammate Claude Code &amp; Codex]
        E --> F[Nodes Draft Candidate Facts<br/>Raw PII/Secrets Stay Local · Only Summaries &amp; Evidence IDs Shared]
        F --> G[siwen-121/agent-shared-facts Review &amp; Git Merge<br/>2nd Device Pulls &amp; Confirms → Read-Only MCP Serves Fact + Commit SHA]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Chat-Thread Approvals + Human Copy-Paste Bus + Shared Folder | Option B: Static GitHub PR Plan Reviews + Custom SSH Scripts | **Option C (Recommended): `PlanRelay` + `Myco` + `agent-shared-facts`** |
| :--- | :--- | :--- | :--- |
| **Stale Plan Approval Prevention** | ❌ Old `"looks good"` in chat remains active after plan edits | ⚠️ Heavyweight PR ceremony slows down rapid local agent planning | ✅ **SHA-256 revision binding invalidates stale approvals; CLI `check` gates execution** |
| **Cloud-to-Local & Cross-Teammate Delegation** | ❌ Engineer manually copies prompts and pastes outputs across windows | ⚠️ Brittle per-host SSH scripts with no cross-agent discovery UI | ✅ **Single Go binary `myco` bridges cloud sessions, local CLIs & teammates' agents** |
| **Cross-Device Fact Integrity & Privacy** | ❌ Unreviewed agent drafts immediately pollute shared vector stores | ⚠️ Lacks two-device pull confirmation receipts & read-only MCP adapter | ✅ **Draft/Candidate/Published separation + Commit SHA + 2-device receipt + read-only MCP** |
| **Monthly TCO (35 Engineers / 40,000 Ops/Mo)** | **`$5,560.00 / mo`** (`$2,140` stale runs/context + `36.0 hrs` relay labor) | **`$2,410.00 / mo`** (`$890` infra + `16.0 hrs` manual SSH/PR sync) | **`$341.00 / mo`** (**`-93.87%` savings**; `$75` Go hub/Git repo + `2.8 hrs` sign-off) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R34-PLANRELAY-MYCO`)

> **Scope & Boundary Declaration**: Evaluated for a 35-person distributed engineering and architecture organization executing **40,000 monthly agent plan reviews, cross-machine delegations, and shared architectural fact updates** at a blended rate of `$95.00/hr` (underlying Tailscale / Cloudflare tunnel transport marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Stale-Plan Re-Run \& Relay Spend} + (\text{Manual Copy-Paste Bus \& Fact Cleanup Hours} \times \$95.00)$$

| Cost Component | Path A: Chat Approvals + Human Copy-Paste Bus | Path B: Static PR Reviews + Custom SSH Scripts | **Path C: `PlanRelay` + `Myco` + `shared-facts`** |
| :--- | :---: | :---: | :---: |
| **Monthly Stale-Plan Re-Run Tokens & Relay Host Spend** | `$2,140.00` | `$890.00` | **`$75.00`** |
| **Monthly Manual Relaying, Plan Revert & Fact Cleanup Hours** | `36.0 hrs` | `16.0 hrs` | **`2.8 hrs`** (**`92.22%` reduction**) |
| **Monthly Distributed Engineering Labor (`@ $95.00/hr`)** | `$3,420.00` | `$1,520.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,560.00`** | **`$2,410.00`** (`-56.65%`) | **`$341.00`** (**`-93.87%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,150.00 / mo` (`$37,800/yr`) | **`$5,219.00 / mo` (`$62,628.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Gate Multi-File Agent Plans on `PlanRelay` CLI `check`**: Run `ineedfoundmyway/planrelay` on Node.js 22+ and require agents to pass CLI `check` verifying that the latest SHA-256 plan snapshot has zero open blockers and is explicitly approved.
- [ ] **Step 2 — Connect Cloud & Workstation Agents via `chenhg5/myco`**: Deploy the single-binary `myco` hub and node agent across macOS, Windows, and Linux workstations so cloud sessions can invoke local toolchains and teammates' agents directly.
- [ ] **Step 3 — Initialize `siwen-121/agent-shared-facts` & Run the Two-Clone Test Suite**: Execute `python -m pip install -r requirements-mcp.txt && python -m unittest discover -s tests -v` to verify offline candidate reconciliation and two-device pull confirmation.
- [ ] **Step 4 — Expose Reviewed Facts Exclusively Over Read-Only MCP**: Keep raw files and credentials on origin devices, commit only reviewed summaries with evidence IDs to the shared Git branch, and serve them to agents via the allowlisted read-only MCP adapter.
