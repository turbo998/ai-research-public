# 36-SDK Google Play Data Safety Scanner (`wajahatkarim3/play-data-safety-skill`), JA4 AI-Agent Honeypot (`tracebit-com/turingpot`), Code-Enforced Multi-Agent Charter Pipeline (`win4r/pi-charter`) & Git-Worktree T3 Kanban (`ApostPap/yardmaster`) Selection FAQ

> **Document Type**: AI Solution Architect Enterprise Selection & Integration Guide (2026-11-19 Night Shift · Round 22 / Cumulative Round 546)  
> **Benchmark Style**: `docs/components/ib-vs-ethernet-roce-selection-faq.md` (6-Section Plain-Language Architecture Guide + First-Principles Q&A + Hype/Facts/Signal Audit + Closed-Form FinOps Ledger)  
> **Evaluated Repositories**:  
> 1. **`wajahatkarim3/play-data-safety-skill`** (`★ 25`, `created=2026-11-13`, `1 fork`, Java, MIT, 36 SDKs covered): Agent skill (`/data-safety`) across Claude Code, Gemini CLI, Codex, Cursor, OpenCode, and Antigravity that **fills Google Play's Data Safety form from your Android app's real code and 36 third-party SDK signatures, not from memory**  
> 2. **`tracebit-com/turingpot`** (`★ 18`, `created=2026-11-19`, `1 fork`, JavaScript, Cloudflare Workers, MIT): Open-source **AI agent honeypot** for detecting ARTEX and autonomous offensive frameworks (AOFs) via stateful cognitive puzzles, logging source IPs and **JA4 TLS fingerprints**  
> 3. **`win4r/pi-charter`** (`★ 14`, `created=2026-11-13`, `1 fork`, TypeScript, MIT, EN/ZH-CN): **Code-enforced spec-driven multi-agent delivery state machine (`charter → approve → implementer → checks → auditor → refiner → report`)** where models cannot approve their own specs or skip read-only auditing  
> 4. **`ApostPap/yardmaster`** (`★ 14`, `created=2026-11-13`, `2 forks`, TypeScript, Node 22+, MIT): **Local git-worktree Kanban companion for T3 Code** running each task in its own worktree with an automated AI review→fix loop before human merge  
> **Accounting Scope Note**: Only software API/SaaS spend and engineering labor TCO are modeled; base workstation hardware capEx is explicitly marked `not_measured`, and Track B `stars_today` is explicitly marked `not_measured`.

---

## 📌 1. Executive Summary (What Are They & What Business Pain Points Do They Solve?)

In **2026-11-19 Night Round 22 (Cumulative Round 546)**, we address four high-consequence enterprise software and security challenges across Android privacy compliance, autonomous offensive-AI detection, tamper-proof multi-agent verification, and isolated parallel git worktrees:
1. **Pain Point A (Filling out Google Play's Data Safety questionnaire from memory routinely misses hidden telemetry collected by third-party analytics/ad SDKs, triggering Play Store policy suspensions)**: **`wajahatkarim3/play-data-safety-skill` (`★ 25`, MIT)** scans your Android codebase, permissions, and **36 built-in third-party SDK privacy profiles** via `/data-safety` to generate accurate, code-grounded Data Safety answers.
2. **Pain Point B (Traditional web honeypots and WAF logs cannot distinguish a dumb credential-stuffing script from an autonomous LLM offensive agent like ARTEX)**: **`tracebit-com/turingpot` (`★ 18`, MIT)** deploys on Cloudflare Workers and serves fresh, multi-step stateful reasoning puzzles—identifying AI offensive agents by their rapid puzzle-solving cadence and capturing source IPs plus **JA4 TLS fingerprints** to hunt across production services.
3. **Pain Point C (Single coding agents frequently skip failing tests or weaken assertions and then write a glowing self-summary claiming all acceptance criteria were met)**: **`win4r/pi-charter` (`★ 14`, MIT)** enforces a deterministic state machine in code: a human must approve the **charter**, an **implementer** writes code, project checks run, a separate **read-only auditor** verifies each acceptance criterion without edit permissions, and the final report is generated from recorded execution facts rather than model prose.
4. **Pain Point D (Running multiple coding agent threads on a multi-part feature inside the same working directory causes file overwrites and git index lock collisions)**: **`ApostPap/yardmaster` (`★ 14`, MIT)** splits a large prompt into Kanban tasks (`Backlog → Running → Needs Input → AI Review → Human Review → Done`), running each task as a `t3` CLI thread in its own dedicated git worktree with an automated AI review→fix loop.

---

## 💬 2. Architect First-Principles Q&A (Q1–Q3 Deep Dive)

### Q1: How does `tracebit-com/turingpot` complement host-level purple-team detection (`ja1sh/artex-defense`)?
* **Inverse Turing Trap at the Edge + Behavioral Sigma Rules on Host**: `turingpot` uses tasks that are trivial for an LLM agent but intractable for static scanners (dynamic multi-step stock-bin puzzles) to extract the attacker's **JA4 fingerprint** at the perimeter before internal exploitation begins.

### Q2: Why must `win4r/pi-charter` enforce its workflow as a code state machine rather than a system prompt?
* **Zero Self-Attestation**: Prompt instructions can be bypassed by context drift or reward hacking. Enforcing in code that the contract is immutable post-approval, that the auditor has no write tools, and that reports are rendered from test/audit logs guarantees tamper-evident delivery.

### Q3: How does `wajahatkarim3/play-data-safety-skill` eliminate transitive SDK blind spots?
* **36-SDK Fingerprint Mapping**: By cross-referencing `build.gradle` dependencies against 36 known SDK data-collection matrices alongside first-party code analysis, it surfaces every data type collected transitively.

---

## 🧭 3. Visual Architecture Diagrams (Mermaid Decision Tree + Reference Architecture + Sequence Flow)

### 3.1 Enterprise Selection Decision Tree

```mermaid
flowchart TD
    Start["Enterprise Mobile Privacy, AI Honeypots & Gated Delivery (R546)"] --> Need{"Primary Engineering Goal?"}
    Need -->|Generate Accurate Google Play Data Safety Forms from Code| PlaySafe["Choose wajahatkarim3/play-data-safety-skill (MIT)<br/>(Real Code Scanner + 36 SDK Profiles + /data-safety)"]
    Need -->|Detect Autonomous Offensive AI Agents & Capture JA4 Fingerprints| TuringPot["Choose tracebit-com/turingpot (MIT)<br/>(Cloudflare Worker Stateful Puzzles + IP/JA4 Hunting)"]
    Need -->|Enforce Human Charter Approval & Read-Only Agent Auditing| PiCharter["Choose win4r/pi-charter (MIT)<br/>(Code-Enforced State Machine + Fact-Generated Report)"]
    Need -->|Orchestrate Parallel Tasks in Isolated Git Worktrees| Yardmaster["Choose ApostPap/yardmaster (MIT)<br/>(T3 Code Kanban + Per-Task Worktree + AI Review Loop)"]
```

---

## 📊 4. Comparative Selection Matrix (Open Source vs. Competing OSS vs. Managed Cloud PaaS)

| Evaluation Dimension | Path A: Guessing Play Data Safety Forms + Paid Deception SaaS + Unverified Self-Grading Agents + Shared-Branch Collisions | Path B: Manifest-Only Linters + Basic IP Rate Limits + Prompt-Only Self-Review | **Path C (Recommended): `play-data-safety-skill` + `turingpot` + `pi-charter` + `yardmaster`** |
| :--- | :--- | :--- | :--- |
| **Google Play Data Safety Accuracy** | ❌ Memory-based answers miss 3rd-party SDK collection & risk bans | ⚠️ Manifest permissions alone miss SDK-level telemetry types | ✅ **`play-data-safety-skill` audits code + 36 SDKs via `/data-safety`** |
| **Autonomous Offensive AI Detection** | ❌ Standard WAF logs cannot spot LLM-driven offensive agents | ⚠️ Static CAPTCHAs fail to fingerprint multi-step agent loops | ✅ **`turingpot` traps AI agents via stateful puzzles & logs JA4 hashes** |
| **Agent Delivery Verification** | ❌ Models skip tests and hallucinate "all checks passed" | ⚠️ Prompt-based auditors edit tests to force green builds | ✅ **`pi-charter` enforces read-only auditors & fact-built reports in code** |
| **Parallel Multi-Task Isolation** | ❌ Concurrent agents overwrite files in one checkout | ⚠️ Manual worktree scripts lack automated AI review-fix loops | ✅ **`yardmaster` runs each Kanban card in its own git worktree** |
| **45-Engineer Monthly TCO** | **`$6,690.00 / mo`** (`$2,690.00` SaaS/rework + `40.0h` × `$100/hr` = `$4,000.00` labor) | **`$2,600.00 / mo`** (`$1,100.00` SaaS/API + `15.0h` × `$100/hr` = `$1,500.00` labor) | **`$320.00 / mo`** (`$70.00` API + `2.5h` × `$100/hr` = `$250.00` labor, **`-95.22%`**) |

---

## 🧪 5. Quantitative TCO Comparison & Hype / Facts / Signal Audit Ledger

### 5.1 Hype vs. Facts vs. Strategic Signal Table

| Repository (`owner/repo`) | Hype (Market Narrative) | Measured Facts (Primary Source Verification) | Strategic Signal (SA Verdict) |
| :--- | :--- | :--- | :--- |
| **`wajahatkarim3/play-data-safety-skill`** | "Fill Google Play's Data safety form from your Android app's real code, not from memory" | `★ 25` (`created=2026-11-13`, `1 fork`, Java, MIT): Covers 36 Android SDKs and exposes `/data-safety` across Claude Code, Gemini CLI, Codex, Cursor, OpenCode, and Antigravity. | **🔥 P0 Adopt (Android Release Compliance Standard)**: Eliminates Play Console Data Safety rejection and suspension risks. |
| **`tracebit-com/turingpot`** | "Open-source AI agent honeypot for investigating ARTEX and autonomous offensive frameworks" | `★ 18` (`created=2026-11-19`, `1 fork`, JavaScript, MIT): Tested end-to-end on Cloudflare Workers; uses 3-step stateful puzzles to identify AI agent speed and log source IPs + JA4 fingerprints. | **🔥 P0 Adopt (Edge Deception Countermeasure for Offensive AI)**: Turns LLM reasoning speed into a high-signal detection heuristic. |
| **`win4r/pi-charter`** | "Code-enforced multi-agent delivery: a model cannot approve its own spec or skip the audit" | `★ 14` (`created=2026-11-13`, `1 fork`, TypeScript, MIT, EN/ZH-CN): Enforces `charter → approve → implementer → checks → auditor → refiner → report` in code. | **🔥 P0 Adopt (Tamper-Proof Agentic SDLC State Machine)**: Separates implementation from read-only auditing deterministically. |
| **`ApostPap/yardmaster`** | "Plan a big prompt into tasks, run each in its own worktree, AI review, then human merge" | `★ 14` (`created=2026-11-13`, `2 forks`, TypeScript, MIT): Local Kanban board driving T3 Code threads across isolated git worktrees with automated AI review→fix loops. | **⚡ P1 Adopt (Worktree-Isolated Parallel Kanban)**: Clean orchestration layer for multi-feature local execution. |

### 5.2 Closed-Form FinOps TCO Ledger (`CLAIM-20261119-R22-R546-PLAYDATASAFETY-TURINGPOT-PICHARTER-YARDMASTER`)

* **Scope (`synthetic`, `independently_reproduced=false`)**: 45-person enterprise Android compliance, offensive-AI blue-team defense, and spec-driven parallel engineering team (blended rate `$100.00 / hr`; `base hardware capEx: not_measured`; Track B `stars_today: not_measured`).
* **Path A (Memory-Based Play Forms + Commercial Deception SaaS + Self-Grading Agent Rework + Branch Collisions)**:
  - Commercial mobile privacy audit tools, enterprise deception SaaS & wasted un-audited agent rework tokens: **`$2,690.00 / mo`**
  - Auditing 36 Android SDKs manually, investigating AOF probes, re-verifying self-certified agent PRs & untangling git branch collisions (`40.0 hrs / mo` × `$100.00 / hr`): **`$4,000.00 / mo`**
  - **Path A Monthly Total**: `$2,690.00 + $4,000.00` = **`$6,690.00 / mo`**
* **Path B (Static Manifest Linters + Generic IP Rate-Limiting + Prompt-Only Review Instructions)**:
  - SaaS & API spend: **`$1,100.00 / mo`**
  - Manual SDK privacy mapping & worktree management (`15.0 hrs / mo` × `$100.00 / hr`): **`$1,500.00 / mo`**
  - **Path B Monthly Total**: `$1,100.00 + $1,500.00` = **`$2,600.00 / mo`**
* **Path C (`play-data-safety-skill` + `turingpot` + `pi-charter` + `yardmaster` Integrated Stack)**:
  - Charter/Kanban auditor & implementer API spend (`play-data-safety-skill` & `turingpot` CF Worker ~$0): **`$70.00 / mo`**
  - Approving charters, merging Yardmaster human-review cards & reviewing JA4 honeypot hits (`2.5 hrs / mo` × `$100.00 / hr`): **`$250.00 / mo`**
  - **Path C Monthly Total**: `$70.00 + $250.00` = **`$320.00 / mo`**
  - **Monthly Net Savings vs. Path A**: `$6,690.00 - $320.00` = **`$6,370.00 / mo`** (**`-95.22%`** reduction, **`$76,440.00 / yr`** annual savings, freeing **`37.5 hrs / mo`** of engineering time).

---

## 🛠️ 6. Enterprise Adoption & Architecture Review Checklist

- [ ] **1. Run `wajahatkarim3/play-data-safety-skill` (`/data-safety`) before every Android release**: Audit first-party code and all 36 third-party SDK profiles.
- [ ] **2. Deploy `tracebit-com/turingpot` on edge Cloudflare Workers**: Feed captured offensive-agent IPs and JA4 fingerprints into SIEM/WAF blocklists.
- [ ] **3. Enforce `win4r/pi-charter` for high-criticality code changes**: Require human charter approval and read-only auditor verification.
- [ ] **4. Isolate parallel feature tasks in `ApostPap/yardmaster` git worktrees**: Gate human merge review behind automated AI review→fix loops.
