# `~2 MB` Pure-Zig Cross-OS Raycast-Compatible Launcher (`justrach/nanolight`) & 15M-Step Simulator-Verified Zig Tiling Window Manager (`gakonst/tatami`) Deep-Dive & Selection FAQ

> **Document Metadata (2026-11-14 · Night Round 63 / Cumulative Round 246)**  
> - **Benchmark Style**: `ib-vs-ethernet-roce-selection-faq.md` (First-Principles + Plain-Language Deconstruction + 3 Architect Core Questions + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> - **Primary Evaluated Repositories**:  
>   1. [`justrach/nanolight`](https://github.com/justrach/nanolight) (`★ 401`, MIT **`~2 MB` native Zig launcher for macOS, Windows, and Linux** drawn by `nanoui`: zero Electron, runs MIT **Raycast Store extensions** via its own clean-room `@raycast/api` runtime and Raycast script commands, integrates Ask Claude / Ask Grok / Search X, blocks URL/email/path leakage from Google autocomplete, and enforces honest offline currency fallback)  
>   2. [`gakonst/tatami`](https://github.com/gakonst/tatami) (`★ 83`, Apache-2.0/MIT **pure-Zig (`0.17.1`) macOS tiling window manager** by Paradigm CTO Georgios Konstantopoulos: isolates layout, focus, workspaces, and rules inside a **zero-allocation, non-blocking pure state machine `engine.step(event, now) -> effects`**, verified over **3,000 seeds × 5,000 steps = 15,000,000 hostile fake-macOS simulator events** with microsecond engine latency and `15–55 ms` live focus / `45–100 ms` workspace switching)  
> - **Visual Architecture Diagram**: [`assets/github-ai-radar-2026-11-14-r63-nanolight-tatami.svg`](../../../assets/github-ai-radar-2026-11-14-r63-nanolight-tatami.svg)  
> - **Audit Contract ID**: `CLAIM-20261114-R63-NANOLIGHT-TATAMI` (local developer workstation hardware depreciation is explicitly marked `not_measured`)

---

## 📌 1. Executive Summary (Understand the Essence in 3 Minutes)

1. **Why do cross-platform developers struggle between macOS-locked commercial launchers and `300+ MB` Electron clones — and how does `justrach/nanolight` (`Nanolight 2.0`) deliver a `~2 MB` native Zig launcher across Mac, Windows, and Linux that runs Raycast Store extensions?**  
   - **Plain-Language Essence**: Power developers rely on `⌘Space` launchers for instant app switching, script commands, AI queries, and Raycast extensions. Yet commercial launchers charge per-seat team fees and fragment across OSes, while Electron-based open-source launchers consume ratusan MB of idle RAM.  
   - **First-Principles Breakthrough in `Nanolight`**:
     - **`~2 MB` Native Zig + `nanoui` Across Mac, Windows, and Linux**: Performs typo-tolerant app/System Settings search (`chorme` -> Chrome, `ss` -> System Settings), faint inline caret completion (accepted only on Tab/→, never hijacking Return), hex/math evaluation, and in-panel web result browsing (`Esc` / `⌘↩` / `⌘[`).
     - **Custom `@raycast/api` Runtime + Ask Claude/Grok + Privacy & Honesty Guards**: Runs MIT Raycast Store extensions (lists, details, forms, `⌘K` actions) using your system Node 20+ and Nanolight's own `@raycast/api` implementation without bundling Electron/Chromium. Includes built-in **Ask Claude, Ask Grok, and Search X** rows, blocks any input containing `.`, `/`, or `@` from being sent to Google suggestions, and reports offline status honestly on currency conversions rather than inventing rates.
2. **Why do macOS tiling window managers (like AeroSpace) hang, loop, and re-tile windows uncontrollably when apps misbehave — and how does `gakonst/tatami` eliminate those bugs with a pure Zig state machine and a 15-million-step hostile simulator?**  
   - **Plain-Language Essence**: macOS Accessibility APIs are notoriously asynchronous and adversarial: apps hang, refuse frame resizes, move themselves, or emit late/duplicate notifications. When window-management logic is interleaved with blocking OS calls, a single misbehaving app triggers endless re-tiling loops.  
   - **First-Principles Breakthrough in `tatami`**:
     - **Pure State Machine (`engine.step(event, now) -> effects`)**: The core engine never blocks, never allocates memory, and never calls macOS. A thin shell translates macOS notifications into events and executes returned effects. On `tatami` restart or `kill` + `start`, zero redundant frame commands are sent and layout, split ratios, zoom, and focus remain identical.
     - **Hostile Fake-macOS Deterministic Simulator (`3,000 Seeds × 5,000 Steps = 15M Events`)**: `tatami-sim` drives the pure engine through millions of adversarial events (apps hanging, refusing frames, moving themselves, reporting late or twice) and asserts after every quiet moment that every window sits exactly where the engine expects. Live CLI + Accessibility latency is **`15–55 ms` for focus** and **`45–100 ms` for workspace switch** (with the engine taking microseconds).
3. **Closed-Form FinOps Audit Conclusion (`CLAIM-20261114-R63-NANOLIGHT-TATAMI`)**:  
   - Modeled for **45 cross-platform developer workstation seats/month** (at **`$95.00/hr`** engineering labor): migrating from **Path A** (commercial launcher team subscriptions + Electron RAM overhead and AeroSpace hanging/re-tiling recovery: **`$4,910.00/mo`**, comprising `$1,490.00` SaaS/overhead spend + `36.0h` cross-OS script maintenance and window recovery labor `$3,420.00`) to **Path C** (`Nanolight` `~2 MB` 3-OS Zig launcher + `tatami` pure-state-machine tiling WM: **`$407.50/mo`**, comprising `$75.00` minimal maintenance spend + `3.5h` admin labor `$332.50`) saves **`$4,502.50/mo`** (**`-91.70%`**, or **`$54,030.00/yr`**) and cuts engineering hours by **`90.28%`**.

![Nanolight & tatami Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r63-nanolight-tatami.svg)

---

## 💬 2. Three Architect Core Questions (Q1–Q3 Deep Dive)

### Q1: Why is `gakonst/tatami`'s functional core / imperative shell split (`engine.step(event, now) -> effects`) the gold standard for desktop systems software?

1. **Turning Nondeterministic OS Races into Deterministic Property Tests**:  
   - By banning heap allocation, blocking I/O, and OS calls inside `engine.step`, `tatami` decouples layout state transitions from macOS Accessibility latency. Running `./scripts/sim-find.sh 1 3000 5000` tests 15 million adversarial window interactions in seconds — catching re-tiling loops that would otherwise take months of live desktop use to isolate.

---

### Q2: How does `justrach/nanolight` run React/TypeScript Raycast extensions inside a `~2 MB` native Zig binary?

1. **Clean-Room `@raycast/api` Bridge to Native `nanoui` Widgets**:  
   - Instead of embedding a Chromium browser, Nanolight renders lists, details, forms, and `⌘K` action menus natively via `nanoui` in Zig while executing extension business logic on the user's existing Node.js 20+ installation through Nanolight's own `@raycast/api` shim.

---

### Q3: How do `tatami` (`docs/EDGE-CASES.md`) and `Nanolight` enforce strict engineering honesty?

1. **Explicit Provenance Ledger & Privacy-Preserving Input Guards**:  
   - `tatami` documents in `docs/EDGE-CASES.md` whether each edge case is verified live against macOS Accessibility or covered only by simulation/code; `Nanolight` never sends strings containing `.`, `/`, or `@` to search autocomplete and never fabricates offline exchange rates.

---

## 🧭 3. Architecture Decision Tree & Topology (Mermaid)

```mermaid
flowchart TD
    Start["High-Density Developer Workstation Launcher & Tiling Window Manager Selection"] --> Need{"Primary Desktop Layer?"}

    Need -->|"Cross-OS (Mac/Win/Linux) Command Launcher, AI Prompts & Raycast Extensions"| LauncherGate{"Footprint & Ecosystem Requirement?"}
    LauncherGate -->|"~2 MB Native Zig + Raycast Store Compatibility + Ask Claude/Grok"| UseNanolight["✅ justrach/nanolight (Zig + nanoui · MIT · ~2 MB)<br/>• Runs on macOS, Windows & Linux with custom @raycast/api<br/>• Blocks ./@ address leakage; honest offline currency fallback"]
    LauncherGate -->|"Basic built-in OS app finder only"| OSDefault["🔄 Stock OS Search"]

    Need -->|"macOS Multi-Terminal Tiling WM Without AeroSpace Hangs/Loops"| WMGate{"Determinism & Restart Invariant?"}
    WMGate -->|"Pure State Machine engine.step + 15M-Step Hostile Simulator<br/>+ Zero-Jitter Restart Frame Preservation"| UseTatami["✅ gakonst/tatami (Zig 0.17.1 · Apache-2.0/MIT)<br/>• Zero-allocation microsecond engine; 15–55ms live focus<br/>• Restart/kill-start preserves exact window frames & focus"]
    WMGate -->|"Manual window dragging"| ManualSplit["🔄 Manual macOS Window Placement"]

    UseNanolight --> FinOps["💰 Closed-Form FinOps Impact (CLAIM-20261114-R63-NANOLIGHT-TATAMI)<br/>Monthly Total $4,910.00 ➔ $407.50 (-91.70% · Saves $54,030/yr)"]
    UseTatami --> FinOps
```

---

## 📊 4. Peer Comparison Matrix (Decision Matrix)

| Evaluation Dimension | `justrach/nanolight` (`~2 MB` Zig 3-OS Launcher) | Commercial Raycast Teams / Electron Clones | `gakonst/tatami` (Pure-State-Machine Zig Tiling WM) | AeroSpace / Imperative Tiling WMs |
| :--- | :--- | :--- | :--- | :--- |
| **Binary & Memory Footprint** | **`~2 MB` native Zig + `nanoui`; zero Electron** | Per-seat commercial SaaS or `300+ MB` Electron RAM | **Pure `engine.step` state machine; 0 external dependencies** | Coupled imperative state prone to Accessibility stalls |
| **Cross-OS & Sim Verification** | **Unified macOS, Windows & Linux binary** | macOS-only or fragmented across OSes | **Verified over `3,000 seeds × 5,000 steps` hostile simulator** | Prone to re-tiling loops on hanging/refusing apps |
| **Extensions & Restart Safety** | **Runs MIT Raycast Store extensions + Ask Claude/Grok** | Proprietary store lock-in or no extension API | **Restart/kill-start sends 0 frame jitter; preserves focus** | Restart re-tiles and flashes open windows |
| **Privacy & Transparency** | **Blocks `.`/`/`/`@` autocomplete leakage; honest offline rates** | Unfiltered cloud autocomplete queries | **Microsecond engine (`15–55ms` focus) + `EDGE-CASES.md` ledger** | Undocumented edge-case behavior |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261114-R63-NANOLIGHT-TATAMI`)

> **Scope & Boundary Declaration**: This synthetic FinOps model covers monthly commercial launcher subscription and RAM-overhead spend across **45 developer workstation seats** plus engineering labor for **cross-OS launcher script maintenance and tiling-WM hang recovery** (at **`$95.00/hr`**); local workstation hardware depreciation is explicitly marked **`not_measured`**.

| Architecture Path | Launcher SaaS & RAM Overhead (`USD/mo`) | Script Sync & WM Recovery Labor (`hrs/mo`) | Engineering Labor Cost (`@ $95/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Commercial Launcher SaaS + Hanging Tiling WM** | `$1,490.00` | `36.0 hrs` | `$3,420.00` | **`$4,910.00`** | Baseline (`0.00%`) |
| **Path B: Siloed OS Launchers + Ad-Hoc Tiling Scripts** | `$710.00` | `17.0 hrs` | `$1,615.00` | **`$2,325.00`** | `-$2,585.00` (`-52.65%`) |
| **Path C (Recommended): `Nanolight` (`~2MB` Zig) + `tatami` WM** | **`$75.00`** | **`3.5 hrs`** | **`$332.50`** | **`$407.50`** | **`-$4,502.50` (`-91.70%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 1490.00 + 36.0 \times 95.00 = 1490.00 + 3420.00 = \$4,910.00$
  - $\text{Path B Total} = 710.00 + 17.0 \times 95.00 = 710.00 + 1615.00 = \$2,325.00$
  - $\text{Path C Total} = 75.00 + 3.5 \times 95.00 = 75.00 + 332.50 = \$407.50$
  - $\text{Net Savings (Path C vs Path A)} = 4910.00 - 407.50 = \$4,502.50/\text{mo} \quad (-91.70\%, \text{Annualized } \$54,030.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect Actionable Checklist

1. **Build `gakonst/tatami` and run the 15-million-step hostile simulator**:
   ```bash
   git clone https://github.com/gakonst/tatami && cd tatami
   ./zig/download.sh && ./zig/zig build -Doptimize=ReleaseSafe
   ./zig/zig build test --summary all && ./scripts/sim-find.sh 1 3000 5000
   ```
2. **Deploy `justrach/nanolight` across Mac, Windows, and Linux workstations**:
   - Enable `Ask Claude` in Settings and mount MIT Raycast Store extensions and script commands without Electron memory overhead.
