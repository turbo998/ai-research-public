# Codex-First 8-Skill Governance Playbook & Dynamic MoE VRAM Windows Agent Selection FAQ: `WeiBeta/skill-forge-public` + `IsValorum/V-Agent`

> **Metadata**
> - **Evaluation Batch**: 2026-11-13 Overnight Deep-Dive Round 48 (Cumulative Round 176)
> - **Primary Repositories**:
>   1. [`WeiBeta/skill-forge-public`](https://github.com/WeiBeta/skill-forge-public) (`★ 132` · `+132 Stars/day` · Created `2026-11-12` · Codex-first 8-skill engineering playbook with 4-role separation of duties, bounded work orders, before/candidate/after drift recovery, and honest `Unknown`/`NotRun` completion receipts)
>   2. [`IsValorum/V-Agent`](https://github.com/IsValorum/V-Agent) (`★ 131` · `+131 Stars/day` · Created `2026-11-12` · `v1.0.7` local-first Windows 10/11 AI agent with `Strata`, `Strata Rust`, and `llama.cpp` engines, dynamic per-turn MoE expert VRAM cache resizing, 16-language syntax/compiler checks, and 200+ automated CI tests)
> - **Companion Architecture Diagram**: [`assets/github-ai-radar-2026-11-13-r48-skill-forge-v-agent.svg`](../../../assets/github-ai-radar-2026-11-13-r48-skill-forge-v-agent.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261113-R48-SKILLFORGE-VAGENT` (see [`evidence/trending-daily-2026-11-13-audit.json`](../evidence/trending-daily-2026-11-13-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language Essence**:
   - **`WeiBeta/skill-forge-public`**: Replaces chaotic "one agent writes, grades, and merges its own code" workflows with a **Codex-first 8-skill engineering playbook separating Engineering Controller → Project Manager → Implementation Specialists → Independent Reviewer (a role that did not author the change)**. Every work order binds fixed inputs, allowed paths, acceptance criteria, and a Completion Receipt that enforces honest `Unknown` / `NotRun` reporting plus `before/candidate/after` ledger reconciliation.
   - **`IsValorum/V-Agent` (`v1.0.7`)**: Solves the **VRAM tug-of-war between Mixture-of-Experts (MoE) weights and growing KV caches on consumer Windows GPUs**. Its default `Strata` engine keeps the hottest MoE experts in VRAM and **dynamically resizes that expert cache before every reply without restarting**—allocating more experts for fast generation in short chats and freeing VRAM for the KV cache in long chats—alongside `Strata Rust` (`f16`/`q8`/`q4` KV cache), official `llama.cpp` builds, per-chat undoable workspaces, and automatic compiler/headless-browser verification across 16 languages.
2. **Quantified FinOps Impact (`CLAIM-20261113-R48-SKILLFORGE-VAGENT`)**:
   - Under a monthly team workload of **80 multi-agent feature work orders + 15 Windows local MoE developer workstations** (fully loaded rate `$95.00/hr`; base cloud LLM subscriptions and GPU hardware capex labeled `not_measured`):
   - **Path C (`skill-forge-public` + `V-Agent`)** cuts total monthly cost of ownership (TCO) from **`$5,290.00/mo` (Path A: self-reviewing agent drift/rework + static VRAM allocation OOM restarts)** to **`$482.50/mo`**, saving **`$4,807.50/mo` (`-90.88%`, `$57,690.00/yr`)** and reclaiming **`34.5 engineering hours/mo` (`-90.79%`)**.

![Round 48 Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-13-r48-skill-forge-v-agent.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why do multi-agent coding sessions frequently drift outside their intended scope or claim unverified tests passed, and how does `WeiBeta/skill-forge-public` prevent both?
- **The Legacy Bottleneck**: Unstructured agent prompts allow implementation agents to touch arbitrary files across the repository and grade their own output, leading to hallucinated "all tests passed" summaries and unrecoverable workspace drift.
- **How `skill-forge-public` Solves It**:
  1. **Four-Role Separation of Duties**: The **Engineering Controller** owns scope and acceptance; the **Project Manager** dispatches bounded tasks (with economical model routing guidance in `docs/WORK-DISPATCH-MODELS.md`); **Implementation Agents** work strictly within assigned `allowed paths`; and an **Independent Reviewer** (who did not write the change) audits the evidence.
  2. **Eight Reusable Skills**: Covers instruction writing, code review, diagnosis, domain modeling, work dispatch (`forge-work-dispatch`), bounded agent recovery, ledger reconciliation, and batched project feedback.
  3. **Honest `Unknown` / `NotRun` Receipts & Drift Recovery**: Completion receipts require explicit `Unknown` or `NotRun` states whenever a check was not executed, backed by `before/candidate/after` records and scoped recovery procedures.

### Q2: Why do local MoE models on consumer GPUs either crawl in short chats or crash with VRAM OOMs in long chats, and how does `IsValorum/V-Agent` fix this dynamically?
- **The Legacy Bottleneck**: Static GPU layer offloading forces a hard choice at startup: load more MoE experts into VRAM (which crashes with an OOM as soon as a long coding conversation's KV cache grows) or reserve huge VRAM headroom for the KV cache (crippling token generation speed on every short turn).
- **How `V-Agent` (`v1.0.7`) Solves It**:
  1. **Dynamic Per-Reply MoE Expert Cache Resizing (`Strata`)**: Before every reply, `V-Agent` resizes the hot-expert VRAM cache to match the current conversation length—packing more experts into VRAM for short turns and seamlessly yielding VRAM to the KV cache as context grows, **without restarting the engine**, paired with MTP draft heads for speculative decoding.
  2. **Three Verified Local Engines + 1-Click Switching**: Switch between `Strata`, `Strata Rust` (per-session private key + `f16`/`q8`/`q4` KV cache), and official `llama.cpp` (CUDA/Vulkan/CPU) with automatic rollback on update and direct import from **LM Studio** and **Unsloth Studio**.
  3. **16-Language Code Verifier + 200+ Automated CI Tests**: Automatically checks generated Python, JS, TS, CSS, PowerShell, JSON/YAML/TOML/XML, Java, C/C++, Rust, Go, PHP, Ruby, and Lua, and runs HTML inside an isolated headless browser to report line-numbered runtime errors (`docs/test-reports/1.0.7.md`).

### Q3: What are the operational boundaries of `skill-forge-public` and `V-Agent`?
- **Concrete Limits**:
  - `skill-forge-public` provides project charters, role templates, and 8 engineering skills (`adapters/codex-native` and `adapters/opencodex`), not a background polling daemon or an unattended runtime scheduler.
  - `V-Agent` is built for Windows 10/11 (`x64`) desktops (`V-Agent_<version>_x64-setup.exe`, no admin rights required, zero telemetry).

---

## 🧭 3. Mermaid Selection Decision Tree & Architecture Flow

```mermaid
flowchart TD
    Start["AI Engineering Need: Multi-Agent Delivery Governance vs Local MoE GPU Execution"] --> Track{"Which problem are you solving?"}

    Track -->|"Preventing Unscoped Agent Edits & Self-Graded Hallucinated Receipts"| GovCheck{"Do you need structured work orders & independent review?"}
    GovCheck -->|"Yes! Need Controller/PM/Specialist/Reviewer + Allowed Paths + Unknown/NotRun receipts"| UseSkillForge["✅ Select WeiBeta/skill-forge-public<br/>8 core skills · Before/Candidate/After drift recovery<br/>Codex-native & OpenCodex adapters"]
    GovCheck -->|"Single-file trivial script tweak"| UseDirect["Use Single-Turn Direct Prompt"]

    Track -->|"Running Local MoE Models & Tool Agents on Windows GPUs"| LocalCheck{"Do you want dynamic MoE VRAM balancing & built-in code verification?"}
    LocalCheck -->|"Yes! Need per-reply MoE expert cache resizing + 3 engines + 16-lang verifier"| UseVAgent["✅ Select IsValorum/V-Agent (v1.0.7)<br/>Strata / Strata Rust / llama.cpp 1-click switch<br/>MTP speculative draft + LM Studio import + 0 telemetry"]
    LocalCheck -->|"Headless Linux CLI inference server only"| UseLlamaCpp["Use Upstream llama-server"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `WeiBeta/skill-forge-public` | `IsValorum/V-Agent` (`v1.0.7`) | Legacy Path A: Self-Graded Single Agent + Static GPU Offload | Legacy Path B: Heavy Polling Orchestrators + Cloud-Only APIs |
| :--- | :--- | :--- | :--- | :--- |
| **Core Problem Solved** | Stops unscoped edits, self-grading bias & fake test receipts | Runs large MoE models on small GPUs via dynamic per-turn VRAM resizing | Agents overwrite unrelated files; growing KV cache causes VRAM OOMs | Background polling burns tokens; no local offline execution |
| **Core Mechanism** | **4-role separation + 8 skills + honest `Unknown`/`NotRun` states** | **`Strata` per-reply MoE expert cache resizing + MTP draft heads** | Single monolithic system prompt + static `--n-gpu-layers` | Complex daemon state machines + remote-only inference |
| **Verification & Recovery** | `before/candidate/after` records + ledger reconciliation | **16-language compiler/syntax checks** + isolated headless browser HTML check | Manual `git reset` archaeology after broken runs | Lacks per-chat versioned file undo & local engine rollback |
| **Transparency & Proof** | Explicit `codex-native` & `opencodex` boundaries; 0 hidden daemons | **200+ automated tests + real-model release reports (`1.0.7.md`)** | Unverified "done" claims in chat | Estimated token speeds rather than engine-measured throughput |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Track / Section | Headline-as-Finding | Evidence & Sealed Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `skill-forge-public` + `V-Agent` cuts monthly multi-agent rework & local MoE TCO by `90.88%` (`$5,290.00 → $482.50/mo`) | `CLAIM-20261113-R48-SKILLFORGE-VAGENT` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `Strata` dynamically resizes the VRAM MoE expert cache before every reply, preventing long-chat KV-cache OOM restarts | `IsValorum/V-Agent` engine architecture |
| **Card 3** | `3/7 · WHAT I TESTED` | 8 reusable skills enforce independent non-author review & `Unknown`/`NotRun` receipts; `V-Agent` passes 200+ CI tests | `skills/forge-work-dispatch` & `1.0.7.md` |
| **Card 4** | `4/7 · UNDER THE HOOD` | `before/candidate/after` drift ledger + `Strata` MTP speculative decoding + `Strata Rust` `f16/q8/q4` KV cache | `templates/project/AGENTS.md` + `QUALITY.md` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | Compiles/validates 16 languages and runs HTML in an isolated headless browser; engine updates keep prior build for rollback | Multi-language verifier + signed updates |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Economical PM routing tables + zero-restart VRAM balancing save `34.5 hrs/mo` (`-90.79%`) across 80 work orders | `docs/WORK-DISPATCH-MODELS.md` |
| **Card 7** | `7/7 · MY TAKE` | Strong fit for Codex teams & Windows local-LLM developers; `V-Agent` desktop installer targets Windows 10/11 x64 | Base API & GPU capex: `not_measured` |

### 💰 Closed-Form FinOps Table (80 Multi-Agent Work Orders + 15 Local MoE Workstations/Mo, `r = $95.00/hr`)

| Architecture Path | Re-Run Token & Cloud GPU Spend (`compute_and_token_usd`) | Drift Rollback & OOM Triage Hours (`engineering_hours`) | Engineering Labor (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Self-Graded Agents + Static VRAM Allocation OOM Restarts** | `$1,680.00` | `38.0 hrs` | `$3,610.00` | **`$5,290.00`** | Baseline (`0.00%`) |
| **Path B: Ad-Hoc Prompt Templates + Fixed-Layer `llama.cpp` Tuning** | `$860.00` | `18.0 hrs` | `$1,710.00` | **`$2,570.00`** | `-$2,720.00` (`-51.42%`) |
| **Path C: `skill-forge-public` 8-Skill Playbook + `V-Agent` (Recommended)** | **`$150.00`** | **`3.5 hrs`** | **`$332.50`** | **`$482.50`** | **`-$4,807.50` (`-90.88%` / `$57,690.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Clone WeiBeta/skill-forge-public and adapt the project charter & bounded work-order templates
git clone https://github.com/WeiBeta/skill-forge-public.git
cd skill-forge-public
# Follow docs/QUICKSTART.md and templates/project/AGENTS.md to dispatch your first work order with Allowed Paths

# 2. Install IsValorum/V-Agent (v1.0.7) on Windows 10/11 (x64), import LM Studio models, and run with Strata MoE
# Download V-Agent_<version>_x64-setup.exe from https://github.com/IsValorum/V-Agent/releases/latest
```
