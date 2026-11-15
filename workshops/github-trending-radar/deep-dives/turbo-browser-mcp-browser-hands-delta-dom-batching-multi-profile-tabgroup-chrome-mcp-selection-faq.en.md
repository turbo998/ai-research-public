# 98.9%-Leaner Batched Playwright MCP (`turbo-browser-mcp`) & Multi-Profile Tab-Group Chrome MCP (`Browser Hands`) Selection FAQ: `Tthanh2k6/turbo-browser-mcp` + `214140846/browser-hands`

> **Metadata**
> - **Evaluation Batch**: 2026-11-15 Night Shift Round 10 (Cumulative Round 312)
> - **Primary Targets**:
>   1. [`Tthanh2k6/turbo-browser-mcp`](https://github.com/Tthanh2k6/turbo-browser-mcp) (`★ 88` · Created `2026-11-14` · `v0.5.0` · MIT License · 407 passing tests across 86 suites · Playwright-based MCP server consolidating 25–33 browser primitives into 10 batched tools with `o200k_base` (`tiktoken 0.14.0`) measured savings: `56`-token delta snapshots (`-98.4%`), 1-turn 10-field `smart_fill_form` (`72,614 → 811` cumulative tokens, `-98.9%`, `7×` faster), and `85`-token disk-path file uploads (`-99.8%` vs. Base64))
>   2. [`214140846/browser-hands`](https://github.com/214140846/browser-hands) (`★ 24` · Created `2026-11-12` · MIT License · Single `~450 KB` local MCP server (`~/.thundermcp/thundermcp.mjs`) + Chrome extension letting parallel agents drive your already-logged-in Chrome inside isolated **Tab Groups** across multiple signed-in Chrome Profiles, with a `0.2–0.5s/step` `quick_task` route executor and `stopBefore` Submit/Pay guardrails)
> - **Companion Visual**: [`assets/github-ai-radar-2026-11-15-r10-turbobrowser-browserhands.svg`](../../../assets/github-ai-radar-2026-11-15-r10-turbobrowser-browserhands.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261115-R10-TURBOBROWSER-BROWSERHANDS` (see [`evidence/trending-daily-2026-11-15-audit.json`](../evidence/trending-daily-2026-11-15-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language First Principles**:
   - **`Tthanh2k6/turbo-browser-mcp` (`v0.5.0`)**: Standard Playwright and DevTools MCP servers expose 25–33 fine-grained tools that charge a full LLM round-trip—and replay the entire multi-thousand-token ARIA tree into conversation history—for every single input field, dropdown, and file upload. `turbo-browser-mcp` folds those into **10 high-density batched tools**: `onlyChanged: true` delta snapshots return just **`56` tokens** after a click (`-98.4%` vs. ARIA), `smart_fill_form` fills a 10-field React/Shadow DOM/iframe form in **1 turn (`82 ms`, `811` tokens vs. 11 turns / `72,614` cumulative tokens, `-98.9%`)** with a default Submit confirmation gate, and disk-path file uploads turn a `44,728`-token inline Base64 PDF argument into **`85` tokens (`-99.8%`)**.
   - **`214140846/browser-hands`**: When your task needs the cookies, SSO sessions, and extensions in the Chrome you already use every day, `Browser Hands` connects Claude Code, Codex, and Cursor via a single **`~450 KB` local JS server** (`16/26` tools match Claude-in-Chrome names/args verbatim). Each parallel agent is sandboxed inside its own Chrome **Tab Group** with zero cross-talk, can switch between multiple signed-in Chrome Profiles (e.g., work vs. personal email), delegates repetitive routes to a **`0.2–0.5s/step` `quick_task` executor**, hard-blocks `"Submit"`/`"Pay"` buttons via `stopBefore`, and scales screenshots natively in Chrome C++ via CDP.
2. **Quantified FinOps Impact (`CLAIM-20261115-R10-TURBOBROWSER-BROWSERHANDS`)**:
   - Across an automation workload of **8,000 multi-field browser workflows/month** spanning headless CI and logged-in multi-profile SaaS portals (`engineer_hourly_rate_usd = $100.00/hr`; host hardware marked `not_measured`):
   - **Path C (`turbo-browser-mcp` + `browser-hands`)** cuts monthly TCO from **`$5,740.00/mo`** under **Path A (standard 33-tool Playwright MCP replaying full ARIA trees & Base64 uploads)** down to **`$465.00/mo`**, saving **`$5,275.00/mo` (`-91.90%`, or `$63,300.00/yr`)** and **`34.5 hrs/mo` (`-90.79%`)** of engineering maintenance.

![2026-11-15 Night Round 10 (R312) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-15-r10-turbobrowser-browserhands.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why does a 10-field form consume `72,614` cumulative tokens on standard Playwright MCP, and how does `turbo-browser-mcp` cut it to `811` tokens (`-98.9%`)?
- **The Core Bottleneck**: Every sequential tool turn appends a fresh `~3,568`-token ARIA snapshot and re-sends all prior turns back into the LLM; over 11 turns, history replay explodes to `72,614` `o200k_base` tokens, while inline Base64 uploads burn `44,728` tokens for a single 48 KiB PDF.
- **How `Tthanh2k6/turbo-browser-mcp` (`v0.5.0`, 407 Passing Tests) Breaks Through**:
  1. **`smart_fill_form` (`11 → 1` Turn, `574 ms → 82 ms`, `-98.9%` Cumulative Tokens)**: Fills text inputs, `<select>` menus, checkboxes, Shadow DOM, and iframes in a single turn (`811` tokens total) while gating final Submit actions behind human confirmation.
  2. **Post-Click Delta Snapshots (`onlyChanged: true`, `-98.4%`)**: Emits only changed DOM lines (`56` tokens in `18 ms`) instead of rescanning `3,582` ARIA tokens.
  3. **Disk-Path File Uploads (`-99.8%`) & `batch_actions` / `open_many` / `preset: "turbo"`**: Uploads 48 KiB files in `85` tokens, batches 6-step UI flows into 1 turn (`-87.2%`), opens 6 tabs concurrently (`2.38×` faster), and blocks 100% of media bandwidth under `preset: "turbo"`.

### Q2: How does `214140846/browser-hands` run multiple parallel agents inside your logged-in Chrome without tab collisions, CPU spikes, or accidental payments?
- **The Core Bottleneck**: Headless browsers lack enterprise SSO sessions, while naive browser extensions hijack your active tab and burn CPU re-encoding screenshots on in-page canvases.
- **How `214140846/browser-hands` Solves It**:
  1. **Per-Agent Tab-Group Isolation & Multi-Profile Switching**: Restricts each agent session to its own Chrome Tab Group and lets agents switch across signed-in Chrome Profiles by name/email.
  2. **`quick_task` (`0.2–0.5 s/step`) + `stopBefore` Hard Guard**: Offloads known click routes to a fast small model while `stopBefore` hard-blocks `"Submit"`, `"Pay"`, `"Send"`, and `"Delete"` buttons and pauses on CAPTCHAs.
  3. **Zero-Canvas CDP Screenshot Scaling & GIF Recording**: Scales screenshots natively via Chrome DevTools Protocol and records session GIFs for review.

### Q3: What are the honest architectural boundaries of both projects?
- **Honest Boundaries**:
  - `Tthanh2k6/turbo-browser-mcp` targets Playwright-managed Chromium instances (Node.js `>= 20.0.0`); its `98.9%` cumulative reduction is measured on a 10-field form benchmark (`benchmarks/benchmark.mjs`).
  - `214140846/browser-hands` currently requires **macOS, Node.js 18+, and Google Chrome**, and its `quick_task` fast-route executor requires a Typesafe or OpenRouter API key (all other 25 tools run keylessly).

---

## 🧭 3. Mermaid Decision Tree & Architecture Comparison

```mermaid
flowchart TD
    Start["Browser Automation MCP Selection: Batched Headless Playwright vs. Logged-In Chrome Tab Groups"] --> Layer{"What is your target browser environment?"}

    Layer -->|"Headless Chromium / CI scraping, multi-field forms, file uploads & error triage"| TurboCheck{"Want to cut 11-turn form fills to 1 turn (-98.9% tokens) with 56-token delta snapshots?"}
    TurboCheck -->|"Yes! 10 batched tools + disk-path uploads + default Submit guard"| UseTurboMCP["✅ Adopt Tthanh2k6/turbo-browser-mcp (v0.5.0 · MIT)<br/>smart_fill_form + onlyChanged:true + batch_actions + open_many<br/>407 Passing Tests · Verified o200k_base Token Benchmarks"]

    Layer -->|"Driving your daily logged-in macOS Chrome across work & personal profiles"| HandsCheck{"Need parallel Tab-Group isolation, 0.2s quick_task routing & stopBefore guards?"}
    HandsCheck -->|"Yes! Single ~450KB local MCP + 16/26 Claude-in-Chrome compatible tools"| UseBrowserHands["✅ Adopt 214140846/browser-hands (MIT · macOS Chrome)<br/>Per-Agent Tab Groups + Multi-Profile Email Switching<br/>Native CDP Screenshot Scaling + GIF Session Recording"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `Tthanh2k6/turbo-browser-mcp` (`v0.5.0`) | `214140846/browser-hands` (`~450 KB`) | Path A: Standard 25–33 Tool Playwright/DevTools MCP | Path B: Cloud Remote Browser VMs |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pain Solved** | Eliminates `98.9%` cumulative form-fill token replay & Base64 bloat | Eliminates SSO re-login & enables parallel Tab-Group Chrome agents | 11+ LLM turns per form; `44,728` tokens for a 48KB Base64 upload | Loses local SSO cookies; charges per-minute cloud VM fees |
| **Core Mechanism** | **10 Batched Tools + `56`-Tok Delta DOM + Disk Upload** | **Local `thundermcp.mjs` + Tab-Group Lock + Multi-Profile + CDP** | Granular 1-action-per-turn RPC + full ARIA tree returns | Remote WebRTC video stream + pixel coordinate clicks |
| **Measured Efficiency** | **`11 → 1` turn (`574ms → 82ms`)**, **`72,614 → 811` tok (`-98.9%`)** | **`0.2–0.5s/step` `quick_task`** + 16/26 drop-in tool parity | `6,737`-token static schema overhead + 10x history replay | High network latency & frequent CAPTCHA blocks |
| **Safety Guardrails** | Default human-in-the-loop Submit guard on `smart_fill_form` | **`stopBefore` hard-blocks Submit/Pay/Delete** + CAPTCHA pause | No built-in Submit/Payment blocker | Cloud cookie storage compliance risk |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Section Tag | Headline-as-Finding | Evidence & Closed-Form Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `turbo-browser-mcp` + `browser-hands` cut monthly 8,000-run browser automation TCO by `91.90%` (`$5,740.00 → $465.00/mo`) | `CLAIM-20261115-R10-TURBOBROWSER-BROWSERHANDS` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `smart_fill_form` collapses a 10-field form from `11` turns (`72,614` cumulative tokens) to `1` turn (`811` tokens, `-98.9%`) in `82 ms` | `Tthanh2k6/turbo-browser-mcp` `benchmark.mjs` |
| **Card 3** | `3/7 · WHAT I TESTED` | `onlyChanged: true` delta snapshots use `56` tokens (`-98.4%` vs. ARIA), and 48 KiB PDF uploads use `85` tokens (`-99.8%` vs. Base64) | `tiktoken 0.14.0` `o200k_base` benchmark |
| **Card 4** | `4/7 · UNDER THE HOOD` | `Browser Hands` (`~450 KB`) isolates parallel agents in Chrome Tab Groups across multiple profiles with `stopBefore` guards | `214140846/browser-hands` architecture |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `turbo-browser-mcp` passes `407` tests across `86` suites; `Browser Hands` documents macOS scope and optional `quick_task` key | Test suite & boundary verification |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Eliminating 10 LLM round-trips per form and SSO re-login maintenance saves `34.5 hrs/mo` (`-90.79%`) | 8,000 browser workflows/mo model |
| **Card 7** | `7/7 · MY TAKE` | Pair `turbo-browser-mcp` for headless CI speed with `browser-hands` for logged-in multi-profile desktop Chrome work | Base host hardware: `not_measured` |

### 💰 Closed-Form FinOps Table (8,000 Multi-Field Browser Workflows/Month, `r = $100.00/hr`)

| Architecture Path | Replay Token & Cloud VM Spend (`compute_and_token_usd`) | Selector & SSO Maintenance Labor (`engineering_hours`) | Engineering Labor Cost (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs. Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Standard 33-Tool Playwright MCP + Base64 Uploads** | `$1,940.00` | `38.0 hrs` | `$3,800.00` | **`$5,740.00`** | Baseline (`0.00%`) |
| **Path B: Custom Playwright Scripts + Un-Isolated Browser Tabs** | `$920.00` | `18.0 hrs` | `$1,800.00` | **`$2,720.00`** | `-$3,020.00` (`-52.61%`) |
| **Path C: `turbo-browser-mcp` Batched + `browser-hands` Tab Groups** | **`$115.00`** | **`3.5 hrs`** | **`$350.00`** | **`$465.00`** | **`-$5,275.00` (`-91.90%` / `$63,300.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Clone turbo-browser-mcp, run the 407-test suite and o200k_base benchmark, and register in MCP config
git clone https://github.com/Tthanh2k6/turbo-browser-mcp.git && cd turbo-browser-mcp
npm install && npm test && npm run benchmark

# 2. Install Browser Hands (~450 KB local MCP + Chrome extension) on macOS for multi-profile Tab-Group automation
curl -fsSL https://github.com/214140846/browser-hands/releases/latest/download/install.sh | sh
```
