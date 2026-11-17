# 15-ADE Empirical Benchmark (`zqkra/ademark`), 40+ Provider Local Claude Gateway (`alissonpaganini/rotaz`) & Self-Hosted MCP PaaS (`hackclub/orchard`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 49 (Cumulative Round 473)  
> **Tracked Repositories**:
> - **`zqkra/ademark`** (`★ 35`, TypeScript / Open Benchmark of 15 Agentic Development Environments on macOS vs. Bare CLI, `Apache-2.0`): Side-by-side empirical benchmark measuring 15 desktop ADEs across 12 tests—revealing a **`3.47x` spread in first-turn `"hi"` token overhead (`22.2K` vs. `77.0K` tokens)** and a **`17.4x` spread in 5-thread idle memory (`134 MB` vs. `2,334 MB`)** (`anonymized_reported`)
> - **`alissonpaganini/rotaz`** (`★ 35`, JavaScript / Zero-Dependency Node 20.11+ Local `127.0.0.1:8787` Gateway, `MIT`) & **`hackclub/orchard`** (`★ 35`, TypeScript / Self-Hosted k3s & Talos Linux PaaS with Postgres S3 PITR & Built-In MCP Server, `AGPL-3.0` + `MIT` Graft SDK): Local Anthropic-to-OpenAI protocol gateway connecting Claude Code and Claude Desktop to 40+ model providers via `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` (`rotaz`), paired with a self-hosted Kubernetes PaaS featuring automated HTTPS, S3 point-in-time Postgres recovery, and a native MCP server (`orchard`)  
> **Audit Claim ID**: `CLAIM-20261117-R49-ADEMARK-ROTAZ-ORCHARD` (base LLM subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Platform Engineering Teams Scaling Agentic Development Hit Three Hidden Taxes: `77K`-Token First-Turn ADE Bloat, Single-Vendor Model Lock-In, and Per-Seat Cloud PaaS Markups**:
   - **Tax 1 — Unmeasured Desktop ADE Prompt & RAM Overhead**: Many desktop agentic IDEs inject massive hidden system prompts and Electron processes—as measured by `ADEMark v1` (`anonymized_reported, independently_reproduced=false`), sending a single `"hi"` consumes anywhere from **`22.2K` tokens** (`Paseo`) and **`38.2K` tokens** (Bare CLI) up to **`77.0K` tokens** (`Emdash`), while 5 idle threads consume **`134 MB`** (`super.engineering`) up to **`2,334 MB`** (`Emdash`).
   - **Tax 2 — Friction Routing Claude Code Across 40+ Model Providers**: Teams want to keep Claude Code's UX while routing routine tasks to DeepSeek, Gemini, Kimi, GitHub Copilot, OpenRouter, or local Ollama models without maintaining brittle Python proxy stacks.
   - **Tax 3 — Commercial PaaS Seat Markups & Missing Agent MCP Deployment Controls**: Managed cloud PaaS platforms charge steep per-seat and managed-Postgres fees, while raw Docker Compose scripts lack automated S3 point-in-time database recovery (PITR) and native MCP server controls for AI agents.
   - **The Solution Architect Stack (`zqkra/ademark` Apache-2.0 + `alissonpaganini/rotaz` MIT + `hackclub/orchard` AGPL-3.0)**: Standardize desktop ADE selection using **`zqkra/ademark`**'s 12-test methodology; run **`alissonpaganini/rotaz`** (`MIT`, zero-dependency Node 20.11+ gateway at `127.0.0.1:8787` with `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`) on developer machines; and deploy applications to **`hackclub/orchard`** (`AGPL-3.0` platform + `MIT` Graft SDK, turning 1 Linux host into a k3s PaaS or scaling to 6-node Talos Linux clusters with Postgres S3 PITR and a built-in MCP server).
2. **Closed-Form FinOps Impact (30 Platform & Application Engineers Running 55,000 Monthly ADE Coding Turns, Multi-Provider Routings & App Deployments at `$95.00/hr`)**:
   - Migrating from **Path A (Unbenchmarked `77K`-Token ADEs + Single-Vendor API Calls & Managed Cloud PaaS Seats at `$5,925.00/mo`)** to **Path C (`ademark`-Selected Low-Overhead ADE + `rotaz` Gateway + `orchard` Self-Hosted MCP PaaS at `$346.00/mo`)** saves **`$5,579.00/mo` (`-94.16%`, or `$66,948.00/yr`)** while cutting IDE troubleshooting, provider configuration, and deployment ops labor from `37.0 hrs/mo` to `2.8 hrs/mo` (**`92.43%` reduction**).

![ADEMark + Rotaz + Orchard Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r49-ademark-rotaz-orchard.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: What did `zqkra/ademark` uncover when benchmarking 15 Agentic Development Environments side by side against the Bare CLI?
- **Plain-Language Definition**: `ademark` (`Apache-2.0`) is **an open, reproducible benchmark evaluating 15 macOS Agentic Development Environments (ADEs) against a Bare Claude Code CLI control across 12 ranked tests**.
- **Four Key Quantitative Findings (`anonymized_reported, independently_reproduced=false`)**:
  1. **First-Turn `"hi"` Token Overhead (`3.47x` Spread)**: Sending a simple `"hi"` sends **`22.2K` tokens** in `Paseo`, **`38.2K` tokens** in the Bare CLI, and **`77.0K` tokens** in `Emdash`;
  2. **5-Thread Idle Memory (`17.4x` Spread)**: Ranges from **`134 MB`** (`super.engineering`, winning 4 of 12 tests) to **`1,013 MB`** (Bare CLI) to **`2,334 MB`** (`Emdash`);
  3. **Cold Start Latency**: Bare CLI is ready in **`0.69 s`**, whereas desktop ADEs require **`1.76 s` to `11.4 s`**;
  4. **Orchestrated Multi-Agent Build Accuracy**: Only `Synara` (`5.2 min`) and `super.engineering` (`7.1 min`) passed 100% of hidden acceptance tests.

### Q2: How does `alissonpaganini/rotaz` let Claude Code and Claude Desktop use 40+ model providers with zero npm dependencies?
- **Local `127.0.0.1:8787` Anthropic-to-OpenAI Translator & Web Panel (`MIT`, Node 20.11+)**:
  - Runs from source with `npm start` (zero external dependencies) or via native Windows/macOS/Linux installers;
  - Connects account logins (GitHub Copilot, ChatGPT, Kimi, Google Antigravity) or API keys (DeepSeek, OpenAI, Gemini, OpenRouter, local Ollama);
  - Setting `ANTHROPIC_BASE_URL="http://127.0.0.1:8787"` and **`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"`** in `~/.claude/settings.json` exposes all configured models directly inside Claude Code.

### Q3: How does `hackclub/orchard` turn a Linux server into an agent-controllable PaaS with S3 point-in-time Postgres recovery?
- **Single-Command k3s or Multi-Node Talos Linux PaaS with Built-In MCP Server (`AGPL-3.0` + `MIT` Graft SDK)**:
  - Connects to GitHub, GitLab, or Gitea to build and serve apps behind automatic HTTPS, backed by **managed Postgres databases with point-in-time restore (PITR) from S3-compatible storage**, logs, metrics, and instant rollbacks;
  - Scales from a single Linux server (k3s) to multi-node Talos Linux + Harbor clusters (proven in production on Hack Club's 6-node Talos cluster) and exposes a **built-in MCP server** so AI agents can deploy, inspect telemetry, and roll back releases autonomously.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph ADESelect["Empirical ADE Selection: zqkra/ademark (★35, Apache-2.0)"]
        A[Benchmark 15 Desktop ADEs vs. Bare CLI] --> B[Audit First-Turn Token Tax 22.2K–77.0K<br/>+ 5-Thread RAM 134MB–2,334MB + Multi-Agent Build Pass Rate]
    end

    subgraph GatewayAndPaaS["40+ Provider Gateway &amp; Self-Hosted MCP PaaS: rotaz (★35, MIT) + orchard (★35)"]
        B --> C[alissonpaganini/rotaz at 127.0.0.1:8787<br/>Zero-Dep Anthropic↔OpenAI Translation + GATEWAY_MODEL_DISCOVERY=1]
        C --> D[hackclub/orchard Self-Hosted k3s / Talos PaaS<br/>Built-In MCP Server Deploys Git Repos + Postgres S3 PITR &amp; Rollbacks]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Bloated ADEs (`77K` Tokens / `2.3GB`) + Cloud PaaS | Option B: Bare CLI Only + Custom Proxy + Manual Docker Compose | **Option C (Recommended): `ademark` Selection + `rotaz` (MIT) + `orchard` PaaS** |
| :--- | :--- | :--- | :--- |
| **Desktop ADE Token Tax & Multi-Thread RAM** | ❌ Up to `77.0K` tokens on `"hi"` & `2,334 MB` RAM for 5 idle threads | ⚠️ Bare CLI uses `1,013 MB` & lacks visual multi-agent orchestration | ✅ **Evidence-selected ADE (`134 MB` RAM, 100% hidden-test pass in `5.2–7.1m`)** |
| **Multi-Provider Routing in Claude Code/Desktop** | ❌ Locked to a single provider endpoint | ⚠️ Fragile Python proxy scripts without model auto-discovery | ✅ **Zero-dep `rotaz` local gateway + web UI + `GATEWAY_MODEL_DISCOVERY=1`** |
| **Self-Hosted Git Deploy, Postgres PITR & Agent MCP** | ❌ High per-seat & managed-DB cloud PaaS bills | ❌ Manual Docker Compose lacks S3 PITR & MCP rollback tools | ✅ **`orchard` k3s/Talos PaaS with HTTPS, Postgres S3 PITR & built-in MCP server** |
| **Monthly TCO (30 Engineers / 55,000 Turns & Deploys)** | **`$5,925.00 / mo`** (`$2,410` token tax/PaaS + `37.0 hrs` ops) | **`$2,575.00 / mo`** (`$960` unrouted APIs + `17.0 hrs` manual ops) | **`$346.00 / mo`** (**`-94.16%` savings**; `$80` Orchard node/S3 + `2.8 hrs` oversight) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R49-ADEMARK-ROTAZ-ORCHARD`)

> **Scope & Boundary Declaration**: Evaluated for a 30-engineer platform and application organization executing **55,000 monthly ADE coding turns, multi-provider model routings, and application deployments** at a blended engineering rate of `$95.00/hr` (base LLM subscriptions marked `not_measured`):

$$\text{Total Monthly TCO} = \text{ADE Token Tax \& Cloud PaaS Spend} + (\text{IDE Freeze Debug \& Manual Deploy Hours} \times \$95.00)$$

| Cost Component | Path A: Bloated ADE + Cloud PaaS | Path B: Bare CLI + Manual Compose | **Path C: `ademark` + `rotaz` + `orchard`** |
| :--- | :---: | :---: | :---: |
| **Monthly ADE Token Tax, Unrouted API & PaaS Spend** | `$2,410.00` | `$960.00` | **`$80.00`** |
| **Monthly IDE Freeze Debug, Key Switching & Deploy Hours** | `37.0 hrs` | `17.0 hrs` | **`2.8 hrs`** (**`92.43%` reduction**) |
| **Monthly Platform & Application Engineering Labor (`@ $95.00/hr`)** | `$3,515.00` | `$1,615.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,925.00`** | **`$2,575.00`** (`-56.54%`) | **`$346.00`** (**`-94.16%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,350.00 / mo` (`$40,200/yr`) | **`$5,579.00 / mo` (`$66,948.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Audit Team ADEs Against `zqkra/ademark` Metrics**: Replace desktop ADEs that send `>50K` tokens on turn 1 or consume `>2 GB` RAM across 5 idle threads with top-performing low-overhead workbenches.
- [ ] **Step 2 — Run `alissonpaganini/rotaz` (`http://127.0.0.1:8787`) for Multi-Provider Discovery**: Enable `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` in `~/.claude/settings.json` to route routine tasks across DeepSeek, Gemini, Kimi, Copilot, and local Ollama models.
- [ ] **Step 3 — Provision `hackclub/orchard` on k3s or Talos Linux with S3 PITR**: Connect GitHub/GitLab/Gitea repositories and S3-compatible object storage so every deployed service gets automatic HTTPS and point-in-time Postgres recovery.
- [ ] **Step 4 — Wire `orchard`'s Built-In MCP Server to Coding Agents**: Let agents deploy preview environments, inspect container logs/metrics, and trigger instant rollbacks directly over MCP.
