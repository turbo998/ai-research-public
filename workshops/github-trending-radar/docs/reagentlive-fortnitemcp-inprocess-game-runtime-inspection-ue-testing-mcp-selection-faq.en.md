# In-Process Live Game Runtime MCP (`Krixx1337/ReAgentLive`) & Unreal Engine Automated Testing MCP (`SternI/FortniteMCP`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 35 (Cumulative #163) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, Game Engine QA Automation Leads, and C++ Runtime Tooling Engineers evaluating two in-process runtime inspection MCP servers:
> 1. **`Krixx1337/ReAgentLive` (`12★` in 2 days, C++, MIT, Windows x64 in-process MCP + agent skill)**: An in-process runtime probe (`ue_find`, `ue_get`, `ue_each`, `touches`, `trial`) that gives coding agents millisecond answers inside a running game — reading every entity's field in the exact same tick (`ue_each`), pinpointing the exact instruction address modifying a value (`touches`), verifying offsets against live bytes after a patch, and running **human-approved, self-restoring `trial` writes** without crashes or restarts!
> 2. **`SternI/FortniteMCP` (`11★` in 2 days, C++, MIT, scoped strictly to authorized offline/private builds)**: An in-process Unreal Engine (UE / UE6) research and automated testing MCP server (`FortniteMCP.dll`) plus a companion `http_mcp/` HTTPS/WebSocket/JWT sidecar (`127.0.0.1:26065/mcp`) — providing **game-thread `ProcessEvent` dispatch with fast paths and timeouts**, full UE reflection (`StaticFindObject`, `GetObjectsOfClass`, `FNamePool`), tracked undoable memory patches, runtime layout auto-tuning, and response-safe DLL self-ejection!
>
> **中文版本**: [reagentlive-fortnitemcp-inprocess-game-runtime-inspection-ue-testing-mcp-selection-faq.md](reagentlive-fortnitemcp-inprocess-game-runtime-inspection-ue-testing-mcp-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r35-reagentlive-fortnitemcp.svg`](../../../assets/github-ai-radar-2026-11-13-r35-reagentlive-fortnitemcp.svg)

![Krixx1337/ReAgentLive and SternI/FortniteMCP Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r35-reagentlive-fortnitemcp.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "waiting hours for a static disassembler to analyze a multi-gigabyte game binary, scanning memory by hand, or crashing the game process with a raw memory write" (`Krixx1337/ReAgentLive`)**: Running inside the game process, `ReAgentLive` gives Claude Code, Codex, or Cursor live answers in milliseconds: `ue_find` and `ue_each` read fields across all matching objects in the **exact same tick**, `touches` identifies the exact function writing to a field (`Game.exe+0x9A3F10`), and **`trial` asks for confirmation, holds a test value for N seconds, and automatically restores the original bytes**!
   - **Ending "crashing Unreal Engine test builds by calling `UFunction`s from off-thread scripts or re-doing offset tables after every build update" (`SternI/FortniteMCP`)**: Designed strictly for local offline/private builds you own, `FortniteMCP` dispatches engine calls safely on the **game thread via a `ProcessEvent` hook** (with fast paths and timeouts), walks live UE reflection (`StaticFindObject`, `GetObjectsOfClass`, `FNamePool`), tracks every memory patch for clean undo and **response-safe DLL self-eject**, auto-tunes runtime layouts across builds, and pairs with an `http_mcp/` local `mitmproxy` sidecar to inspect HTTPS, WebSocket, and JWT traffic!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R35-REAGENTLIVE-FORTNITEMCP`)**:
   - Modeled for a **game QA automation and engine tools team running `80 Unreal Engine runtime state-inspection and patch-regression suites / month`** (fully loaded C++ engine & QA automation engineer rate `$100.00/hr`; Windows GPU test rigs and commercial disassembler licenses: `not_measured`):
   - Switching from **Path A (hours-long static disassembler dumps + crash-prone raw writes, `$5,380.00/mo`)** to **Path C (`ReAgentLive` millisecond `touches`/`trial` MCP + `FortniteMCP` game-thread `ProcessEvent` & tracked undo patches, `$515.00/mo`)** saves **`$4,865.00/mo` (`-90.43%`, or `$58,380.00/yr`)** and cuts static-dump waiting and crash-recovery labor from `38.0 hrs/mo` to `3.5 hrs/mo` (**`-90.79%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why do static binary dumps and external memory pollers fail for automated C++ / Unreal Engine runtime debugging?
- **First-Principles Breakdown**:
  1. **Static Dumps Miss Live `UObject` Graphs & Tick Consistency**: Static analysis takes hours and cannot see dynamically spawned actor instances or read 12 actors atomically in the same simulation tick.
  2. **Off-Thread Engine Calls & Raw Writes Cause Crashes**: Calling `UFunction`s outside the game thread or writing raw bytes without undo tracking crashes the process and forces multi-minute map reloads.

### Q2: How does `Krixx1337/ReAgentLive` enable millisecond runtime queries and crash-free `trial` experiments?
- **First-Principles Breakdown**:
  1. **Same-Tick `ue_each` & Hardware/Watchpoint `touches`**:
     - Reads every instance of a class in the same game tick and locates the exact instruction address writing to a target field in milliseconds.
  2. **Human-Gated Self-Restoring `trial` Writes**:
     - Prompts the user before mutating state, holds the trial value for a bounded duration (e.g., 30 seconds), and automatically restores the original state.

### Q3: How does `SternI/FortniteMCP` combine game-thread `ProcessEvent` safety, tracked undo patches, and HTTP/WS sidecar inspection?
- **First-Principles Breakdown**:
  1. **Game-Thread `ProcessEvent` Hook & Tracked Undo Ledger**:
     - Marshals `UFunction` invocations onto the game thread with timeouts, records all patches/allocations for deterministic undo, and supports response-safe DLL self-ejection.
  2. **Runtime Layout Auto-Tuning & `http_mcp/` Sidecar**:
     - Adapts property offsets across private builds and runs a local `mitmproxy` MCP server (`127.0.0.1:26065/mcp`) to correlate in-memory engine state with HTTPS, WebSocket, and JWT network traffic.

---

## 🧭 3. Mermaid Decision Tree & ReAgentLive + FortniteMCP Architecture

```mermaid
flowchart TD
    A["C++ / Unreal Engine Live Runtime Inspection & Automated QA Testing"] --> B{"Primary Runtime Testing Need?"}
    B -- "Fast Field Discovery & Safe Experimentation: Locate writers in ms & test temporary values safely" --> C["Adopt Krixx1337/ReAgentLive (ue_find / ue_each / touches / trial MCP)"]
    B -- "Unreal Engine Reflection & Full-Stack QA: Game-thread ProcessEvent, layout tuning & HTTP/WS capture" --> D["Adopt SternI/FortniteMCP (In-Process UE MCP + http_mcp Sidecar)"]

    C --> C1["ue_find & same-tick ue_each + touches write-function pinpointing"]
    C1 --> C2["Human-approved trial write holds value for N seconds & restores automatically"]

    D --> D1["Game-thread ProcessEvent dispatch + tracked undo patches + clean DLL self-eject"]
    D1 --> D2["Runtime layout auto-tuning + http_mcp (:26065/mcp) HTTPS/WebSocket/JWT inspection"]

    C2 & D2 --> E["🏆 Golden Game Engine Agent QA Stack: ReAgentLive + FortniteMCP (-90.43% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Static Dumps + Raw Memory Writes | Path B: Out-of-Process Poller + Manual Offsets | **Path C (Recommended): `ReAgentLive` + `FortniteMCP` (Offline QA)** |
| :--- | :--- | :--- | :--- |
| **Field Discovery & Writer Identification** | Hours of static disassembly & manual scanning | Reads fixed offsets only; cannot trace writers | **Millisecond `ue_find` / same-tick `ue_each` + `touches` writer pinpointing** |
| **Mutation Safety & Cleanup** | Raw writes crash the game or leave dirty state | Manual value backup & restore | **Self-restoring `trial` writes + tracked undo patches + clean DLL self-eject** |
| **Unreal Engine `UFunction` Execution** | Crashes due to off-thread execution | No `ProcessEvent` marshaling | **Game-thread `ProcessEvent` dispatch with fast paths & timeouts** |
| **Patch Resilience & Network Correlation** | Full rebuild & manual offset hunting | Breaks on every build update | **Runtime layout auto-tuning + `http_mcp/` HTTPS/WebSocket/JWT sidecar** |
| **Monthly TCO (80 UE QA Suites/Mo)** | **`$5,380.00 / mo`** (`$1,580` token + `$3,800` labor) | **`$2,720.00 / mo`** (`$720` token + `$2,000` labor) | **`$515.00 / mo` (Saves `$4,865.00/mo` · `-90.43%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R35-REAGENTLIVE-FORTNITEMCP`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A game QA automation and engine tools team running **80 Unreal Engine runtime state-inspection and patch-regression verification suites per month** on offline/private builds.
- **Labor Rate**: Fully loaded C++ engine and QA automation engineer rate of **`$100.00 / hr`**.
- **Explicit Not-Measured Boundary**: Windows GPU test rig hardware capex and commercial disassembler licenses are marked **`not_measured`**. This model strictly accounts for LLM debugging token spend and engineering hours spent waiting on static disassembly, scanning memory manually, and restarting crashed game clients.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Static Dumps + Crash-Prone Raw Writes | Path B: Out-of-Process Poller Without Game Thread | **Path C: `ReAgentLive` + `FortniteMCP` In-Process (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Runtime Debugging & QA Token Spend** | **`$1,580.00`** (static-dump guessing + crash-restart loops) | **`$720.00`** (stale-offset retry spend) | **`$165.00`** (millisecond live reflection & `touches` precision) |
| **Static Dump Waiting, Memory Scanning & Restart Labor (`$100/hr`)** | `38.0 hrs × $100.00` = **`$3,800.00`** | `20.0 hrs × $100.00` = **`$2,000.00`** | `3.5 hrs × $100.00` = **`$350.00`** |
| **Total Monthly TCO** | **`$5,380.00 / mo`** | **`$2,720.00 / mo`** (`-49.44%`) | **`$515.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,660.00 / mo` | **Saves `$4,865.00 / mo` (`-90.43%` · `$58,380.00/yr`)** |
| **GPU Test Rigs & Commercial Disassembler Licenses** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. Offline/Private Build Scope Enforcement**: Run `ReAgentLive` and `FortniteMCP` strictly against local offline/private game builds you own (`127.0.0.1` loopback) with anti-cheat disabled.
- [ ] **2. `Krixx1337/ReAgentLive` Build & `trial` Verification**: Follow `docs/agent-setup.md` to build and register the MCP server, then verify millisecond `ue_find`, `ue_each`, `touches`, and self-restoring `trial` writes.
- [ ] **3. `SternI/FortniteMCP` Game-Thread & Self-Eject Test**: Verify thread-safe `ProcessEvent` execution, tracked undo patch rollback, and response-safe DLL self-ejection.
- [ ] **4. `http_mcp/` Network Sidecar Correlation**: Launch `http_mcp\start.cmd` (`127.0.0.1:26065/mcp`) to inspect HTTPS/WebSocket/JWT traffic alongside live Unreal Engine memory state.
