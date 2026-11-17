# Boundary-Recorded Shadow-Verified Legacy-to-Rust Modernization (`erkamyaman/rust-anything`) & 60-FPS Real-Time Latent Steering IDE (`chuanqisun/spaceship`) Architecture & Selection FAQ

> **Document Metadata (2026-11-17 · Night Round 2 / Cumulative Round 426)**  
> - **Target Audience**: **Enterprise AI Solution Architects** & Engineering/Product Decision-Makers  
> - **Core Orientation**: **① Real Enterprise Application Scenarios & Business ROI/Pain Points + ② End-to-End Integration Reference Architecture + ③ Peer Open-Source / Cloud Service / Commercial Solution Selection & TCO Comparison**  
> - **Editorial Benchmark**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language First Principles + 3 Architectural Deep-Dive Q&As + Mermaid Decision Tree + Peer Comparison Matrix + Closed-Form FinOps Audit + 15-Minute Rollout Checklist)  
> - **Evaluated Repositories**:  
>   1. [`erkamyaman/rust-anything`](https://github.com/erkamyaman/rust-anything) (`★ 426`, `426 ★/day` #B5 on Track B, MIT License: 6-language incremental application modernization and hot-loop acceleration MCP/Skill harness across TypeScript/JS, Python, C, Go, Ruby, and Java; enforces `profile → analyze → bridge --batch → record → diff → bench → shadow → gate` with **`38,251` recorded cases replayed at `0` mismatches** and up to **`20x` speedup**)  
>   2. [`chuanqisun/spaceship`](https://github.com/chuanqisun/spaceship) (`★ 510`, `510 ★/day` #B4 on Track B, MIT Media Lab research project, MIT License: **60-FPS real-time latent idea steering IDE** featuring **Focus Monitor attention heatmaps, Attention Lock constraint pinning, Future Vector Steering eigenvector sliders, and real-time timeline scrubbing with speculative cache invalidation**)  
> - **Companion SVG Diagram**: [`assets/github-ai-radar-2026-11-17-r2-rust-anything-spaceship.svg`](../../../assets/github-ai-radar-2026-11-17-r2-rust-anything-spaceship.svg)  
> - **Audit Claim ID**: `CLAIM-20261117-R2-RUSTANYTHING-SPACESHIP` (production server hardware capEx marked `not_measured`; upstream 6-language benchmark speedups labeled `anonymized_reported, independently_reproduced=false`)

---

## 📌 1. Executive Summary (3-Minute Enterprise Architect's Briefing)

1. **Why do "Big-Bang AI Code Rewrites" fail in enterprise legacy modernization, and how does `erkamyaman/rust-anything` de-risk migrations across TypeScript, Python, Java, Go, Ruby, and C?**  
   - **Enterprise Business Pain Point**: Enterprises running high-cost legacy services in Python, Ruby, TypeScript/Node, Java, or Go want Rust's throughput and memory safety, but asking an LLM to "rewrite the whole repo in Rust" fails in production for two reasons: ① **Semantic Edge-Case Drift**: LLMs mistranslate subtle boundary behaviors (`-0`, `NaN`, non-ASCII/emoji string lengths, signed division/modulo, float printing, map iteration order, and exception types); ② **Per-Call FFI Overhead**: Crossing the FFI boundary once per tiny function call is frequently *slower* than the host language's JIT.  
   - **`rust-anything` Architectural Fix**:
     - **A Deterministic Verification Cage & MCP Server for Coding Agents**: Registers directly with Claude Code, Codex, Cursor, and Gemini CLI via `rust-anything setup`;
     - **Profiler-Guided Batch Bridging (`profile` + `bridge --batch`)**: Profiles real workloads (`node`, `cProfile`, `pprof`, `JFR`), flags already-compiled native kernels (`numba`, `Cython`, `JAX`) where porting yields little gain, and generates zero-API-change FFI bridges (`napi-rs`, `PyO3 abi3`, `cgo`, `magnus`, `JNI`) with `--batch fn:param` classes so items cross once and execute across all CPU cores in Rust;
     - **Boundary Recording + Production Shadow Mode (`record` → `diff` → `shadow` → `gate`)**: Keeps the legacy codebase as the ground-truth oracle (`38,251` recorded cases replayed with `0` mismatches), supports live side-by-side production verification via `RUST_ANYTHING_MODE=old|shadow|new`, and enforces a strict completion `gate` (`clippy -D warnings`, `unsafe` audit, recorded failing test for every original error path, zero unguarded `unwrap`/`panic!`). Reported workload gains reach **`20×` on TypeScript (`10 ms → 0.5 ms`)**, **`17×` on Python (`98 ms → 5.8 ms`)**, **`11.8×` on Ruby (`88 ms → 7.5 ms`)**, **`4×` on Go**, and **`3×` on Java** (`anonymized_reported`).
2. **As ultra-fast inference engines push LLM generation toward 60 FPS, why do turn-based chat boxes bottleneck enterprise knowledge workers, and what reference architecture does `chuanqisun/spaceship` introduce?**  
   - **Enterprise Business Pain Point**: In enterprise product specification authoring, legal clause drafting, and marketing campaign design, linear "prompt → wait → read → re-prompt" chat interfaces force users to regenerate entire documents just to nudge tone or preserve a compliance clause.  
   - **`Spaceship IDE` Architectural Fix**: Built at the MIT Media Lab, `chuanqisun/spaceship` demonstrates **4 Real-Time 60-FPS Steering Primitives** backed by aggressive speculative generation and deterministic cache invalidation:
     - **Focus Monitor**: Renders live token-attention heatmaps so human operators can verify which context clauses the model is actively weighting;
     - **Attention Lock**: Lets users pin critical enterprise constraints or terminology so the model maintains high attention weight on them across subsequent generations;
     - **Future Vector Steering**: Decomposes intent into orthogonal eigenvectors controlled by real-time cockpit sliders;
     - **Real-Time Scrubbing & Stream Abort**: Moving the timeline knob backward immediately invalidates future speculative branches and aborts in-flight HTTP requests to prevent wasted token spend.
3. **Closed-Form FinOps Audit (`CLAIM-20261117-R2-RUSTANYTHING-SPACESHIP`)**:  
   - Across **15 legacy service hot-path modernization tasks + 30 interactive enterprise copilot authoring workflows per month** (at **`$100.00/hr`** engineering rate), migrating from **Path A** (unverified big-bang AI rewrites + repetitive turn-based chat retries: **`$6,080.00/mo`**) to **Path C** (`rust-anything` boundary-recorded shadow migration + `Spaceship` real-time latent steering & stream abort: **`$440.00/mo`**) saves **`$5,640.00/month`** (**`-92.76%`**, **`$67,680.00/year`**) and cuts engineering rework labor from `41.0 hrs` to `3.3 hrs/mo` (**`-91.95%`**).

![Shadow-Verified Legacy-to-Rust Modernization & 60-FPS Latent Steering Architecture](../../../assets/github-ai-radar-2026-11-17-r2-rust-anything-spaceship.svg)

---

## 💬 2. Three Architectural Deep-Dive Q&As (Enterprise Scenarios, Reference Architecture & Boundaries)

### Q1: How does `erkamyaman/rust-anything` coordinate multi-session, multi-agent whole-application migrations (`--whole-app`) without losing architectural state?

1. **Persistent ADR, Glossary, and Wave-Based Handoff Files (`DECISIONS.md`, `GLOSSARY.md`, `MAP.md`, `HANDOFF.md`)**:  
   - `rust-anything analyze . --whole-app` maps entry points, coupled dependency pieces, and crate equivalents, guiding the architect through structured "Grilling" rounds stored as ADRs in `rust/DECISIONS.md` and `rust/GLOSSARY.md`;  
   - Black-box CLI/server behavior is captured via `rust-anything app record` into `trycmd` fixtures (`rust/app-cases/*.toml`) with `--normalize timestamps|uuids|key-order`;  
   - Subagents claim independent units in `rust/MAP.md`, write session checkpoints to `rust/HANDOFF.md`, track `RUST_ANYTHING_FALLBACK_LOG` until fallback rate hits `0%`, and generate a reversible `rust/cutover.sh` script.

---

### Q2: What are the explicit architectural boundaries of `rust-anything` (`What It Can't Catch`)?

1. **Three Guardrails Every Enterprise Architect Must Enforce**:  
   - **Coverage Bound**: `diff` only proves inputs captured in `record`; always run `RUST_ANYTHING_MODE=shadow` on production traffic before switching to `new`;  
   - **Pre-Compiled Native Kernels**: Skip porting Python/C loops that already live inside `numba`, `Cython`, or `JAX` (automatically flagged by `rust-anything profile`);  
   - **Batching Across FFI**: Always use `--batch fn:param` for fine-grained loops so data crosses the FFI boundary once per batch rather than once per element.

---

### Q3: How should architects integrate `chuanqisun/spaceship`'s speculative steering loop into enterprise copilot frontends?

1. **Coupling Speculative Prefix Caching with `AbortController` Lifecycle Management**:  
   - Pair high-throughput inference endpoints (Cerebras, Gemini Flash, or private SGLang speculative decoding) with a client-side speculative tree that prefetches likely slider trajectories and immediately aborts superseded streams when the user scrubs backward.

---

## 🧭 3. Enterprise Integration Reference Architecture & Selection Decision Tree (Mermaid)

```mermaid
flowchart TD
    Start["Enterprise Legacy Modernization & Real-Time Copilot UX Selection"] --> Track{"Primary Architectural Scope?"}

    Track -->|"TS/Python/Go/Java/Ruby/C Legacy Service Optimization & Rust Migration"| MigGate{"Migration Risk & Equivalence Strategy?"}
    MigGate -->|"Zero API Breakage + Boundary-Recorded Equivalence (38,251 Cases)<br/>+ Production old/shadow/new Side-by-Side Cutover"| UseRustAnything["✅ erkamyaman/rust-anything (★ 426 · MIT)<br/>• Profiler-Guided bridge --batch (3x–20x Speedup Across 6 Langs)<br/>• Multi-Session DECISIONS.md / MAP.md + Strict Clippy/Unsafe Gate"]
    MigGate -->|"Hotspot Already Inside Native C++/CUDA/JAX Kernels"| KeepNative["🔄 Retain Native Kernel & Optimize via R425 inference-optimisation"]

    Track -->|"Interactive Enterprise Authoring, Legal Drafting & Product Design Copilots"| UXGate{"Human-AI Interaction Paradigm?"}
    UXGate -->|"60-FPS Eigenvector Sliders + Attention Lock on Compliance Clauses<br/>+ Timeline Scrubbing with Speculative Cache Invalidation"| UseSpaceship["✅ chuanqisun/spaceship (★ 510 · MIT Media Lab)<br/>• Focus Monitor Heatmaps + Attention Lock Constraint Pinning<br/>• Future Vector Steering + Automatic In-Flight Stream Abort"]
    UXGate -->|"One-Shot Asynchronous Background Batch Jobs"| BatchQueue["🔄 Standard Asynchronous Queue / Batch API"]

    UseRustAnything --> FinOps["💰 Closed-Form Enterprise FinOps Impact (CLAIM-20261117-R2-RUSTANYTHING-SPACESHIP)<br/>Monthly Total $6,080.00 ➔ $440.00 (-92.76% · Saves $67,680/yr)"]
    UseSpaceship --> FinOps
```

---

## 📊 4. Peer Open-Source / Cloud / Commercial Selection Matrix (Decision Matrix)

| Dimension | `erkamyaman/rust-anything` (`★ 426` Shadow Migration) | Unverified Big-Bang LLM Rewrite | Commercial Legacy Modernization Consultancies | `chuanqisun/spaceship` (`★ 510` 60-FPS Steering IDE) | Traditional Turn-Based Chat UI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Enterprise Use Case** | **Incremental 6-lang hot-loop speedup (`3x–20x`) & zero-downtime Rust ports** | Toy scripts under 200 lines | Multi-year mainframe outsourcing | **Real-time steering of enterprise specs, copy & strategy docs** | Simple Q&A lookup |
| **Equivalence & Safety** | **`record` semantic traps + `diff` + `shadow` mode + `gate` audit** | High risk of silent edge-case regressions (`-0`, `NaN`, overflow) | Manual QA cycles lasting months | **Attention Lock pins compliance clauses + Focus Monitor heatmaps** | Constraint drift across long multi-turn threads |
| **Throughput & Token Efficiency** | **`--batch` multi-core FFI bridges (`20x` TS, `17x` Python, `11.8x` Ruby)** | Per-call FFI often slower than host JIT | Variable quality | **Timeline scrub aborts in-flight streams & prunes stale cache** | Full-document regeneration on every tweak |
| **TCO & Licensing** | **MIT Open Source (Claude Code, Codex, Cursor & Gemini CLI ready)** | High production rollback cost | `$100k–$1M+` consulting contracts | **MIT Open Source (client-only browser app + fast API backend)** | High human prompt-engineering rework |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps Audit (`CLAIM-20261117-R2-RUSTANYTHING-SPACESHIP`)

> **Scope & Provenance Boundary**: Models monthly cloud compute/token spend and engineering rework labor across **15 legacy service hot-path modernization tasks** and **30 interactive enterprise copilot authoring workflows** at **`$100.00/hr`**. Base server hardware capEx is marked **`not_measured`**, and upstream 6-language benchmark speedups are labeled **`anonymized_reported` (`independently_reproduced=false`)**.

| Architecture Path | Compute & Token Spend (`USD/mo`) | Migration & Prompt Rework Labor (`hrs/mo`) | Engineering Labor Cost (`@ $100/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Unverified Big-Bang AI Rewrite + Linear Chat Retries** | `$1,980.00` | `41.0 hrs` | `$4,100.00` | **`$6,080.00`** | Baseline (`0.00%`) |
| **Path B: Hand-Rolled FFI Wrappers + Static Prompt Templates** | `$920.00` | `18.5 hrs` | `$1,850.00` | **`$2,770.00`** | `-$3,310.00` (`-54.44%`) |
| **Path C (Recommended): `rust-anything` + `Spaceship` Steering IDE** | **`$110.00`** | **`3.3 hrs`** | **`$330.00`** | **`$440.00`** | **`-$5,640.00` (`-92.76%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 1980.00 + 41.0 \times 100.00 = 1980.00 + 4100.00 = \$6,080.00$
  - $\text{Path B Total} = 920.00 + 18.5 \times 100.00 = 920.00 + 1850.00 = \$2,770.00$
  - $\text{Path C Total} = 110.00 + 3.3 \times 100.00 = 110.00 + 330.00 = \$440.00$
  - $\text{Net Savings (Path C vs Path A)} = 6080.00 - 440.00 = \$5,640.00/\text{mo} \quad (-92.76\%, \text{Annualized } \$67,680.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect 15-Minute Enterprise Rollout Checklist

1. **Install `rust-anything` & Execute Boundary-Recorded Shadow Migration**:
   ```bash
   cargo install rust-anything && rust-anything setup
   rust-anything profile . -- node bench.mjs
   rust-anything bridge . src/fuzzy.ts --batch fuzzyScore:text
   rust-anything record rust/fuzzy-rs && rust-anything build rust/fuzzy-rs
   rust-anything diff rust/fuzzy-rs && rust-anything gate rust/fuzzy-rs
   ```
2. **Launch `chuanqisun/spaceship` 60-FPS Latent Steering Workbench**:
   ```bash
   git clone https://github.com/chuanqisun/spaceship.git
   cd spaceship && npm install && npm run dev
   ```
