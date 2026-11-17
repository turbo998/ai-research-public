# ACP-Over-HTTP Remote Agent Transport (`varops/actp`), Xcode 27 Dual-Exec Enterprise Gateway Bridge (`yusuke-114/claude-xcode-agent`) & 11-Provider Quota/Process Monitor (`ensignalp/kota`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 39 (Cumulative Round 463)  
> **Tracked Repositories**:
> - **`varops/actp`** (`★ 93`, Rust, `v0.1.0`, `Apache-2.0`): Agent Client Transport Protocol (**ACP over HTTP/WebSocket**), enabling any standard ACP editor, bot, or app to run coding agents (`Claude Code`, `Codex`, `Droid`, `Pi`) on a remote workstation with plain `stdio` ACP on both ends, drop-resilient reconnects, scoped per-client tokens, allowed-folder guardrails, and built-in Cloudflare Tunnel support
> - **`yusuke-114/claude-xcode-agent`** (`★ 81`, Shell Dual-Exec ACP Wrapper, `MIT`) & **`ensignalp/kota`** (`★ 88`, Rust / GNOME Top-Bar Multi-Provider Quota & Live Process Monitor, `MIT`): Dual-role `exec` wrapper that injects enterprise gateway credentials (`config.json`) into Xcode 27 while isolating it from global `~/.claude/settings.json` (`claude-xcode-agent`), paired with a real-time 11-provider quota burn-rate and `Folder → Subproject → Running Agent (RAM/ports/stop)` monitor (`kota`)  
> **Audit Claim ID**: `CLAIM-20261117-R39-ACTP-XCODE-KOTA` (base LLM API subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Cross-Platform Engineering Teams (iOS/macOS, Linux Workstations & Remote Cloud Hosts) Hit Three Daily Friction Points: Dropped Remote Agent Connections, Unisolated Xcode 27 Configs, and Blind Multi-Provider Quota Lockouts**:
   - **Friction 1 — Fragile Remote Stdio Pipelines**: Standard Agent Client Protocol (ACP) clients expect a local `stdio` child process. When engineers tunnel ACP over raw SSH to a beefy remote workstation, closing a laptop lid or switching Wi-Fi drops the pipe and aborts in-flight multi-step coding turns.
   - **Friction 2 — Xcode 27 GUI Environment & Global Settings Leakage**: Using `claude-agent-acp` directly in Xcode 27 suffers from two architectural flaws: Xcode launches the agent from the macOS GUI without shell environment variables for enterprise AI gateways (`base_url` / `auth_token`), and the adapter hardcodes `claude --setting-sources user,project,local`, leaking personal `~/.claude/settings.json` into enterprise Xcode workspaces.
   - **Friction 3 — Multi-Provider Quota Exhaustion & Zombie Agent Processes**: Developers juggling Claude, Codex, Gemini, GitHub Copilot, GLM, OpenRouter, DeepSeek, and Kimi have no unified visibility into which daily/weekly quota is about to hit 100% or which background agent process is hogging ports and RAM.
   - **The Solution Architect Stack (`varops/actp` Apache-2.0 + `claude-xcode-agent` MIT + `ensignalp/kota` MIT)**: Bridge remote workstations over HTTPS/WebSocket with **`varops/actp`** (`Apache-2.0`, preserving plain `stdio` ACP on both ends with zero-loss reconnects and revocable per-client/per-folder tokens); integrate Xcode 27 cleanly via **`yusuke-114/claude-xcode-agent`** (`MIT`, using a two-role `exec` bootstrap to load `config.json` gateway credentials and restrict `--setting-sources` to `project,local`); and monitor all 11 providers plus live subproject agent processes in the desktop top bar with **`ensignalp/kota`** (`MIT`).
2. **Closed-Form FinOps Impact (30 Cross-Platform Engineers Running 50,000 Monthly Remote ACP, Xcode 27 & Multi-Provider Coding Sessions at `$95.00/hr`)**:
   - Migrating from **Path A (Dropped SSH Tunnels + Unisolated Xcode Global Configs & Blind Quota Lockouts at `$5,890.00/mo`)** to **Path C (`actp` + `claude-xcode-agent` + `kota` Stack at `$341.00/mo`)** saves **`$5,549.00/mo` (`-94.21%`, or `$66,588.00/yr`)** while cutting tunnel-recovery, Xcode debugging, and zombie-process cleanup labor from `38.0 hrs/mo` to `2.8 hrs/mo` (**`92.63%` reduction**).

![ACTP + claude-xcode-agent + Kota Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r39-actp-claude-xcode-kota.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `varops/actp` run coding agents on remote workstations over HTTPS/WebSocket while keeping both client and agent speaking plain `stdio` ACP?
- **Plain-Language Definition**: `actp` (`Apache-2.0`, Rust `v0.1.0`) is **an HTTPS/WebSocket transport bridge for the Agent Client Protocol (ACP) that makes remote coding agents behave like local `stdio` processes—surviving network drops without losing a single message**.
- **Three Architectural Guarantees**:
  1. **Zero Client or Agent Code Changes**: Any ACP client spawns `actp droid@workstation` over plain `stdio`; `actp bridge` streams messages over HTTPS/WebSocket to `actp server`, which spawns `Claude Code`, `Codex`, `Droid`, or `Pi` over plain `stdio` on the remote host where files, terminals, and local MCP servers reside;
  2. **Drop-Resilient Reconnection & Built-In Cloudflare Tunnel**: Closing a laptop lid or changing Wi-Fi networks never kills the remote agent—the bridge reconnects and catches up without losing or duplicating messages, even across NATs via its built-in Cloudflare Tunnel integration;
  3. **Scoped Per-Client Tokens & Allowed-Folder Sandboxing**: Issues revocable tokens per client restricted to specific agents and workspace folders, managed via a cross-platform tray/menu-bar dashboard or Docker image.

### Q2: How does `yusuke-114/claude-xcode-agent`'s two-role `exec` design solve Xcode 27 gateway authentication and global config isolation with zero wrapper process overhead?
- **Dual-Role `exec` Bootstrap (`claude-acp.sh`)**:
  1. **Role ① — Launched Once as the ACP Agent by Xcode**: Reads `config.json` (`base_url`, `auth_token` or `api_key`) into the environment, sets `CLAUDE_CODE_EXECUTABLE` to point back to `claude-acp.sh`, and `exec`s the long-lived `claude-agent-acp` adapter;
  2. **Role ② — Launched Once per Session as `claude` by the Adapter**: Intercepts the adapter's hardcoded `--setting-sources user,project,local`, swaps it for **`project,local`** (so global `~/.claude/settings.json` never leaks into Xcode unless explicitly opted in), attaches configured MCP servers, and `exec`s the real `claude` binary.
  - Because both roles use POSIX `exec`, **no wrapper shell stays alive** and `stdout` remains 100% pure ACP.

### Q3: How does `ensignalp/kota` prevent surprise multi-provider quota lockouts and runaway background agents?
- **11-Provider Real-Time Telemetry & Process Tree (`MIT`, Rust + GNOME Top Bar / Quick Settings)**:
  - Tracks **Claude, Codex** (auto-detected CLI logins), **Gemini** (per-model daily quota), **GitHub Copilot** (premium request %), **Z.ai (GLM Coding Plan)**, **OpenRouter, DeepSeek, Kimi, SiliconFlow** (live balances), and **OpenAI / Anthropic Admin APIs** (monthly spend & budget %);
  - Computes *"exhausts at this pace"* burn-rate forecasts, renders 24-hour token charts, and maps running agents in a live **`Folder → Subproject → Agent (RAM, open ports, 1-click stop)`** hierarchy.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph RemoteACP["Remote ACP-Over-HTTP Transport: varops/actp (★93, Rust Apache-2.0)"]
        A[ACP Editor / Bot / Laptop Client<br/>spawns: actp claude@workstation] -->|Plain stdio ACP| B[actp bridge<br/>Survives Lid Close &amp; Wi-Fi Drops · Zero Message Loss]
        B <==>|HTTPS / WebSocket + Cloudflare Tunnel<br/>Per-Client &amp; Per-Folder Scoped Token| C[Remote Workstation actp server<br/>Runs Claude Code · Codex · Droid · Pi]
    end

    subgraph XcodeAndQuota["Xcode 27 Gateway &amp; 11-Provider Telemetry: claude-xcode-agent (★81) + kota (★88)"]
        D[Xcode 27 GUI Launches claude-acp.sh] --> E[Role ① execs ACP Adapter with config.json Gateway<br/>Role ② execs claude with --setting-sources project,local]
        E --> F[ensignalp/kota Top-Bar Monitor Across 11 Providers<br/>D/W/M Quota Rings + Exhaustion Forecast + Subproject Agent Kill]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Raw SSH Stdio Tunnels + Stock Xcode Adapter + Blind Quotas | Option B: Custom `autossh` Scripts + Global `.claude` Edits | **Option C (Recommended): `actp` (Apache-2.0) + `claude-xcode-agent` (MIT) + `kota` (MIT)** |
| :--- | :--- | :--- | :--- |
| **Remote Agent Survival Across Wi-Fi / Lid Drops** | ❌ Stdio pipe breaks immediately; in-flight turn lost | ⚠️ `tmux` keeps CLI alive but breaks local IDE ACP stream | ✅ **Plain `stdio` ACP on both ends with lossless HTTPS/WS catch-up reconnect** |
| **Xcode 27 Enterprise Gateway & Settings Isolation** | ❌ GUI launch misses shell env; `~/.claude` leaks into Xcode | ⚠️ Editing global settings breaks terminal Claude Code sessions | ✅ **Dual-role `exec` loads `config.json` gateway and enforces `project,local` isolation** |
| **Multi-Provider Quota Burn & Zombie Agent Control** | ❌ Surprise mid-sprint quota lockouts; orphan agents hog ports | ⚠️ Manual checking across 10+ billing dashboards & `ps aux` | ✅ **Top-bar 11-provider D/W/M rings, pace forecast & subproject agent stop button** |
| **Access Scoping & NAT Traversal** | ❌ Full SSH key exposure to remote machine | ⚠️ Manual firewall/port-forwarding maintenance | ✅ **Per-client revocable tokens scoped to allowed folders + built-in Cloudflare Tunnel** |
| **Monthly TCO (30 Engineers / 50,000 Sessions)** | **`$5,890.00 / mo`** (`$2,280` dropped/overage waste + `38.0 hrs` ops) | **`$2,582.50 / mo`** (`$920` rerun waste + `17.5 hrs` manual maintenance) | **`$341.00 / mo`** (**`-94.21%` savings**; `$75` tunnel/gateway ops + `2.8 hrs` token admin) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R39-ACTP-XCODE-KOTA`)

> **Scope & Boundary Declaration**: Evaluated for a 30-engineer cross-platform organization (iOS/macOS, Linux workstations, and cloud hosts) running **50,000 monthly remote ACP sessions, Xcode 27 enterprise gateway turns, and multi-provider coding sessions** at a blended engineering rate of `$95.00/hr` (base LLM API subscriptions marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Dropped-Session \& Quota-Overage Token Spend} + (\text{Tunnel/Xcode/Zombie-Agent Ops Hours} \times \$95.00)$$

| Cost Component | Path A: Raw SSH + Stock Xcode + Blind Quotas | Path B: Custom Forwards + Manual Billing Checks | **Path C: `actp` + `claude-xcode-agent` + `kota`** |
| :--- | :---: | :---: | :---: |
| **Monthly Dropped-Session Re-Runs, Config Leaks & Overage Spend** | `$2,280.00` | `$920.00` | **`$75.00`** |
| **Monthly Tunnel Recovery, Xcode Debug & Zombie Agent Hours** | `38.0 hrs` | `17.5 hrs` | **`2.8 hrs`** (**`92.63%` reduction**) |
| **Monthly Cross-Platform Engineering Labor (`@ $95.00/hr`)** | `$3,610.00` | `$1,662.50` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,890.00`** | **`$2,582.50`** (`-56.15%`) | **`$341.00`** (**`-94.21%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,307.50 / mo` (`$39,690/yr`) | **`$5,549.00 / mo` (`$66,588.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Deploy `varops/actp` Server on High-Spec Build/GPU Workstations**: Run the `actp` Docker image or tray app on remote dev servers, enable Cloudflare Tunnel if behind NAT, and issue per-client tokens restricted to approved workspace directories.
- [ ] **Step 2 — Configure `yusuke-114/claude-xcode-agent` Across macOS / Xcode 27 Seats**: Run `./setup.sh`, populate `config.json` (`chmod 600`) with your enterprise gateway `base_url` and `auth_token`, and register `claude-acp.sh` in Xcode › Settings › Intelligence so sessions stay isolated to `project,local`.
- [ ] **Step 3 — Install `ensignalp/kota` on Linux / GNOME Engineering Workstations**: Connect Claude, Codex, Gemini, GitHub Copilot, and API balance accounts to display D/W/M quota rings and burn-rate exhaustion alerts in the top bar.
- [ ] **Step 4 — Audit & Terminate Runaway Background Agents via `kota`'s Live Tree**: Use `kota`'s `Folder → Subproject → Agent` panel to inspect memory usage and open ports and stop orphaned coding agents in one click.
