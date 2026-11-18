# Event-Driven Reactive Agent Harness (`pmndrs/pine`) & Human-Led AI Team Collaboration Skills (`dabingfy-dot/solo-to-team-skills`) Selection FAQ

> **Document Scope**: This is the **2026-11-12 Night Shift Round 4 (Cumulative #103) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects and Solo/Lean Engineering Leads evaluating two high-signal agent orchestration repositories:
> 1. **`pmndrs/pine` (`130★` in 2 days, TypeScript, by Poimandres)**: A reactive agent harness where agents subscribe to live stimuli (**folders, commands, websites, FTP endpoints, MQTT, webhooks, and physical devices like Flipper Zero**) via typed `*.ts` event-source schemas — featuring **zero manual config editing (administrative tool calls only)**, a **built-in BM25 self-discovery manual**, `pine check` security auditing, and a **Kitty-protocol graphical terminal UI**!
> 2. **`dabingfy-dot/solo-to-team-skills` (`762★` in 5 days, `~152★/day`, Bilingual Skill Pack)**: A 4-skill operational discipline pack for a single human leading a team of long-running AI agents — **`dispatch-accept-verify` (3-state ledger separating Pending, Artifact Received, and Verified)**, **`evidence-before-done` (version-matched proof with incremental re-verification on changed parts)**, **`beginner-ops-writing` (one-step-at-a-time runbooks strictly reserving human-only steps as "human required")**, and **`ops-case-notes` (redacted failure postmortems)**, verified across 8 agent hosts (Codex, DeepSeek Harness, Cursor, WorkBuddy, CodeBuddy, Kimi Work, QwenWork, and Grok Bot)!
>
> **中文版本**: [pine-solo-to-team-skills-reactive-event-harness-human-led-ai-teams-selection-faq.md](pine-solo-to-team-skills-reactive-event-harness-human-led-ai-teams-selection-faq.md) · **Daily Digest**: [`daily/2026-11-12.en.md`](../daily/2026-11-12.en.md) · **Architecture Summary SVG**: [`assets/github-ai-radar-2026-11-12-r4-pine-solototeam.svg`](../../../assets/github-ai-radar-2026-11-12-r4-pine-solototeam.svg)

![pmndrs/pine and solo-to-team-skills Architecture Comparison](../../../assets/github-ai-radar-2026-11-12-r4-pine-solototeam.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "token-burning polling loops, broken JSON config files, and prompt bloat from carrying internal API docs in every turn" (`pmndrs/pine`)**: Traditional CLI harnesses sit idle until you type in chat or run a rigid cron timer. `pmndrs/pine` lets agents subscribe directly to typed `*.ts` event sources (file watchers, webhooks, MQTT, FTP, hardware). You tell the main agent what you want in plain English, and it configures sub-agents, MCPs, event sources, and schedules through **administrative tool calls** without ever corrupting user config files — while looking up internal API details on demand via a **built-in BM25 manual tool**!
   - **Ending "dropped delegated tasks, agents claiming 'done!' without running verification against the current version, and unsafe instructions that try to bypass human-only steps" (`dabingfy-dot/solo-to-team-skills`)**: When one person coordinates multiple AI assistants, tasks frequently vanish or return half-baked. `solo-to-team-skills` enforces four portable skills across 8 hosts: (1) a **3-state dispatch ledger** (`Pending` → `Artifact Received` → `Verified`) where items leave the queue only after verification; (2) **version-matched evidence gates** that re-verify modified/failed segments while reusing valid prior checks on unchanged parts; and (3) **strict human-in-the-loop runbook boundaries**!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261112-R4-PINE-SOLOTOTEAM`)**:
   - Modeled for a **10-person technical lead & operations squad running `600 event-driven automations` and `240 delegated multi-agent deliverables` per month** (fully loaded senior tech lead rate `$90.00/hr`; external commercial webhook SaaS subscriptions and physical IoT hardware costs: `not_measured`):
   - Upgrading from **Path A (polling loops carrying full docs in context + unverified agent handoffs causing rework, `$5,720.00/mo`)** to **Path C (`pmndrs/pine` reactive event subscriptions & BM25 manual discovery + `solo-to-team-skills` 3-state evidence ledger, `$690.00/mo`)** saves **`$5,030.00/mo` (`-87.94%`, or `$60,360.00/yr`)** and cuts manual follow-up, false-completion rework, and config debugging labor from `44.0 hrs/mo` to `5.0 hrs/mo` (**`-88.64%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: How does `pmndrs/pine` eliminate idle polling and context bloat via typed `*.ts` event sources, administrative tool config, and BM25 self-discovery?
- **First-Principles Breakdown**:
  1. **Typed Event-Source Subscriptions & Daemon Mode (`pine start`)**:
     - An event source is a `*.ts` service with a schema. Agents subscribe to folder changes, webhooks, MQTT, or FTP events and wake only when stimuli arrive, while `/goal` and pinned tabs persist long-running objectives.
  2. **Administrative Tool Calls (No Config Corruption) & BM25 Manual**:
     - The main agent manages PINE's configuration exclusively through administrative tool calls; agents query a built-in BM25 manual tool on demand instead of carrying documentation in context, and `pine check` audits permissions and sandbox safety.

### Q2: How do the four skills in `dabingfy-dot/solo-to-team-skills` prevent dropped tasks, unverified completions, and unsafe agent bypasses?
- **First-Principles Breakdown**:
  1. **`dispatch-accept-verify` (3-State Task Ledger)**:
     - Tracks every delegated task across three distinct states — `Pending` (who executes, who receives, when to check), `Artifact Received` (with output path), and `Verified` — removing items only after verification or explicit human cancellation.
  2. **`evidence-before-done` + `beginner-ops-writing` + `ops-case-notes`**:
     - Requires concrete proof aligned with the current revision before marking work done (incrementally re-checking only modified/failed sections while reusing valid prior checks), enforces one-step-at-a-time runbooks with strict human-only boundaries, and captures redacted operational postmortems.

### Q3: How should AI Solution Architects combine `pmndrs/pine` and `solo-to-team-skills`?
- **Golden-Combo Pattern**:
  - Run **`pmndrs/pine`** as the event-driven reactive daemon watching folders, webhooks, and repos;
  - Load **`dabingfy-dot/solo-to-team-skills`** into the coordinating agent so every event-triggered sub-agent task is logged in the 3-state ledger and gated by `evidence-before-done` before notifying the human lead!

---

## 🧭 3. Mermaid Decision Tree & Reactive Human-Led Team Pipeline

```mermaid
flowchart TD
    A["Reactive Event-Driven Automation & Human-Led AI Team Selection"] --> B{"Primary Operational Bottleneck?"}
    B -- "Need agents to react to folders, webhooks, MQTT & hardware without polling or config edits" --> C["Adopt pmndrs/pine (Reactive Agent Harness)"]
    B -- "One human coordinating multiple agents faces dropped tasks & unverified 'done' claims" --> D["Adopt dabingfy-dot/solo-to-team-skills (4-Skill Pack)"]

    C --> C1["Typed *.ts event subscriptions + administrative tool config (never breaks user config)"]
    C1 --> C2["On-demand BM25 manual lookup + pine check audit + Kitty graphical TUI"]

    D --> D1["dispatch-accept-verify: Pending -> Artifact Received -> Verified 3-state ledger"]
    D1 --> D2["evidence-before-done: Revision-matched proof + incremental re-check on edits"]
    D2 --> D3["beginner-ops-writing & ops-case-notes: Explicit human-only boundaries"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Polling Loops + Unverified Chat Handoffs | Path B: Manual Cron Scripts + Flat Todo Lists | **Path C (Recommended): `pmndrs/pine` + `solo-to-team-skills`** |
| :--- | :--- | :--- | :--- |
| **Stimulus & Event Awakening** | High-frequency polling loops burning tokens | Fragile custom shell/webhook glue scripts | **Native `*.ts` schema event sources (folders, MQTT, FTP, webhooks)** |
| **Config Safety & API Doc Overhead** | Full internal docs in prompt; raw file edits break config | Manual YAML/JSON edits prone to syntax errors | **Administrative tool calls + built-in BM25 on-demand manual lookup** |
| **Delegation & Verification Discipline** | Verbal "all done!" claims without test proof | Single `done` checkbox conflating receipt & verification | **3-state ledger (`Pending`/`Received`/`Verified`) + incremental proof gate** |
| **Cross-Host Portability & HITL Safety** | Locked to one CLI; unsafe auth bypass attempts | Ambiguous multi-step docs | **Verified across 8 hosts + strict "human-required" step boundaries** |
| **Monthly TCO (600 Events + 240 Tasks)** | **`$5,720.00 / mo`** (`$1,760` API + `$3,960` labor) | **`$2,900.00 / mo`** (`$920` API + `$1,980` labor) | **`$690.00 / mo` (Saves `$5,030.00/mo` · `-87.94%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261112-R4-PINE-SOLOTOTEAM`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A 10-person technical lead & operations squad processing **600 event-driven automations** and coordinating **240 delegated multi-agent deliverables per month**.
- **Labor Rate**: Fully loaded senior technical lead rate of **`$90.00 / hr`**.
- **Explicit Not-Measured Boundary**: Commercial third-party webhook middleware subscriptions and physical IoT device hardware costs are marked **`not_measured`**. This model strictly accounts for model API spend and engineering hours spent on chasing dropped tasks, reworking unverified completions, and fixing broken configurations.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Polling Loops + Unverified Handoffs | Path B: Manual Cron + Flat Todo Lists | **Path C: `pmndrs/pine` + `solo-to-team-skills` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Event & Multi-Agent Model API Spend** | **`$1,760.00`** | **`$920.00`** | **`$240.00`** (Event-driven wake + BM25 manual + incremental proof reuse) |
| **Dropped-Task Triage, False-Done Rework & Config Labor (`$90/hr`)** | `44.0 hrs × $90.00` = **`$3,960.00`** | `22.0 hrs × $90.00` = **`$1,980.00`** | `5.0 hrs × $90.00` = **`$450.00`** |
| **Total Monthly TCO** | **`$5,720.00 / mo`** | **`$2,900.00 / mo`** (`-49.30%`) | **`$690.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,820.00 / mo` | **Saves `$5,030.00 / mo` (`-87.94%` · `$60,360.00/yr`)** |
| **Commercial Webhook SaaS & IoT Hardware** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `pmndrs/pine` Init & Security Check**: Run `npm install -g @pmndrs/pine && pine init && pine check` to validate agent models, MCP scopes, and Linux sandbox settings.
- [ ] **2. Event-Source Subscription & BM25 Manual Test**: Ask the main agent to subscribe to a watched directory or webhook and verify administrative tool configuration without manual file edits.
- [ ] **3. `dispatch-accept-verify` 3-State Ledger Rollout**: Log every delegated sub-agent task as `Pending`, transition to `Artifact Received` with file paths, and close only after `Verified`.
- [ ] **4. `evidence-before-done` Incremental Verification**: Require revision-matched evidence on every handoff and reuse prior verified checks on unmodified sections.
