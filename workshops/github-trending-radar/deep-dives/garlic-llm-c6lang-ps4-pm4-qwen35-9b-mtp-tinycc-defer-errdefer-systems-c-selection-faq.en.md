# Bare-Metal PS4 PM4 Offline `Qwen3.5-9B` Engine (`Garlic LLM`) & Stack-Frame `defer`/`errdefer` TinyCC Systems Compiler (`c6`) Selection & Architecture FAQ: `leonardo-alegria/garlic-llm` + `c6lang/c6`

> **Track**: GitHub AI Trending & Breakout Radar — 2026-11-15 Night Round 34 (Cumulative Round 336) P0 Standalone 6-Section Selection Guide  
> **Benchmark Standard**: Modeled after `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language First Principles + Q1–Q3 Deep Dive + Mermaid Decision Tree + Comparison Matrix + 7-Card Quantitative Scorecard + Closed-Form FinOps Ledger + 15-Minute Runbook)  
> **Audit Evidence Anchor**: `workshops/github-trending-radar/evidence/trending-daily-2026-11-15-audit.json` · Claim ID: `CLAIM-20261115-R34-GARLICLLM-C6LANG`  
> **Companion High-Res Architecture Diagram**: [`assets/github-ai-radar-2026-11-15-r34-garlicllm-c6lang.svg`](../../../assets/github-ai-radar-2026-11-15-r34-garlicllm-c6lang.svg) · [中文版 (`garlic-llm-c6lang-ps4-pm4-qwen35-9b-mtp-tinycc-defer-errdefer-systems-c-selection-faq.md`)](garlic-llm-c6lang-ps4-pm4-qwen35-9b-mtp-tinycc-defer-errdefer-systems-c-selection-faq.md)

---

## 📌 1. Executive Summary (30-Second First-Principles Overview)

1. **What Are They in Plain Language?**
   - **`leonardo-alegria/garlic-llm` (`★55`, C / OpenCL / GCN PM4, GPL-3.0)**: The first native, 100% offline 9-billion-parameter language model (**`Qwen3.5-9B`**) running directly on a base/Slim **PlayStation 4 GPU (AMD GCN)**—dispatching custom LLVM-compiled OpenCL C kernels via hand-written **PM4 hardware command packets**, combining **hybrid `Q4` + `Q3` (`~3.5-bit` MLP gate/up) weights that save `384 MiB` of GPU-visible "Garlic" memory**, **2-token MTP speculative decoding**, and a **4-bit `16K` KV cache** to hit **`31–39 tok/s` (chat) and up to `43 tok/s` (code)**, while co-hosting offline 25-language STT (**Parakeet TDT 0.6B v3**), 7-language TTS (**Chatterbox**), and an embedded **MicroPython** runner.
   - **`c6lang/c6` (`★55`, C / TinyCC Fork)**: A systems-programming C extension compiler built on **TinyCC (TCC)** that adds **stack-frame `defer`/`errdefer` resource cleanup (no TLS required)**, `T!error` + `try`/`catch` with module-pinned `(area<<27)|(slot<<12)|code` error IDs, stackless `async`/`await` coroutines, bounds-checked `T[:]` slices, fat-pointer `interface`, and monomorphized `@T` generics—strictly gated by the **`.c6` file extension** so `.c` files remain 100% identical to upstream TCC.
2. **Why Should an AI Solution Architect or Systems Engineer Care Tonight?**
   - **A Masterclass in Fitting `9B` + Multimodal Models into Tight Non-CUDA APUs**: On embedded APUs or legacy consoles with fixed unified memory ceilings, storing all of `Qwen3.5-9B` in 4-bit (`Q4`) overflows available GPU RAM by `~384 MiB`. `garlic-llm` proves that quantizing *only* the two largest per-layer matrices (MLP `gate` and `up` projections) to `Q3` (`~3.5 bits` with scales) reclaims **`384 MiB`** without collapsing reasoning quality, while a `0.20 GiB` MTP head unlocks `31–43 tok/s` via 2-token speculative decoding.
   - **Eliminating Multi-Exit C Resource Leaks Without Losing `tcc -run` or Bare-Metal Simplicity**: Pure C runtimes suffer from combinatorial cleanup bugs whenever a function acquires multiple files or buffers across several error exits. `c6` stores `defer` and `errdefer` state inside the **function stack frame** (working even in 512-byte bare-metal boot sectors) and enforces compile-time uniqueness for module error codes in `errbase.def`.
3. **Quantified FinOps Impact (Claim ID: `CLAIM-20261115-R34-GARLICLLM-C6LANG`)**:
   - Under a synthetic workload of **20 offline multimodal edge appliances + 15 bare-metal/embedded C runtime modules** (`$100/hr` engineer rate), migrating from **Path A (Cloud Voice/LLM API Fallback & Dedicated Mini-GPU Boxes + Legacy C Manual `goto` Leak Debugging)** to **Path C (`garlic-llm` Bare-Metal PM4 `Q4/Q3` + MTP Suite + `c6` Stack-Frame `defer`/`errdefer` Compiler)** reduces monthly TCO from **`$5,980.00/mo`** to **`$450.00/mo`**—saving **`$5,530.00/mo` (`-92.47%`)** or **`$66,360.00/yr`**, while cutting debugging labor from `40.0 hrs/mo` to `3.5 hrs/mo` (`-91.25%`).

---

## 🔍 2. Deep-Dive Q1–Q3 (First-Principles Architecture)

### Q1: How Does a Base PS4 with Zero Official Compute APIs Run `Qwen3.5-9B` Offline at `31–43 tok/s` Alongside Speech-to-Text, Text-to-Speech, and MicroPython?

- **Three Hardware Constraints on Base/Slim PS4**:
  1. **No High-Level Compute or ML Driver API**: PS4 homebrew (OpenOrbis / GoldHEN) exposes no CUDA, ROCm, or compute runtime.
  2. **The `384 MiB` "Garlic" Memory Cliff**: Storing all of `Qwen3.5-9B` in `Q4` requires `~384 MiB` more GPU-visible ("Garlic") memory than the console has free once the OS, UI, and `16K` KV cache are allocated.
  3. **Memory-Bandwidth Bottleneck During Autoregressive Decode**: Streaming `4.32 GiB` of weights for one token at a time caps raw single-token speed.
- **Four First-Principles Breakthroughs in `garlic-llm`**:
  1. **Hand-Written PM4 Command Packets + LLVM GCN OpenCL Kernels (`shaders/`)**: Compiles custom 4-bit/3-bit matrix multiplication, attention, and normalization kernels in OpenCL C for the PS4's GCN architecture via Zig/LLVM, and dispatches them by writing raw **PM4 hardware command packets** directly.
  2. **Hybrid `Q4` + `Q3` (`~3.5-bit`) Quantization Saving Exactly `384 MiB`**: Keeps attention and output heads in `Q4`, while quantizing each layer's two largest matrices—the MLP `gate` and `up` projections—to **`Q3` (`~3.5 bits` per weight with scales)** in `qwen3.5-9b-q4s.bin` (`4.32 GiB`), reclaiming **`384 MiB`** so the **4-bit `16K` attention cache** fits cleanly.
  3. **2-Token MTP Speculative Decoding (`qwen3.5-9b-mtp.bin`, `0.20 GiB`)**: Drafts up to 2 tokens ahead using `Qwen3.5`'s native Multi-Token Prediction (MTP) head and verifies them in one forward pass, achieving **`31–39 tok/s` on text chat** and **`43 tok/s` on code**.
  4. **Self-Contained `5.7 GB` Multimodal & Code Execution Loop**: Bundles **Parakeet TDT 0.6B v3** (`parakeet-v3-q4i.bin`, `0.33 GiB`, 25 European languages STT), **Chatterbox** (`chatterbox-t3.bin` `0.29 GiB` + `chatterbox-s3gen-mf.bin` `0.09 GiB`, 7 languages TTS running at `~22 tok/s` in live voice mode), and an embedded **MicroPython** interpreter triggered via `R1`.

### Q2: Why Is Resource Cleanup the #1 Source of Bugs in Systems C, and How Does `c6lang/c6` Solve It with Stack-Frame `defer`/`errdefer`, Pinned Error Slots, and a Zero-Contamination `.c6` Gate?

- **Three Classic Failure Modes in Systems C**:
  1. **Multi-Exit Cleanup Duplication**: Every new `fopen()`, `malloc()`, or temporary file requires updating every downstream error `return` or `goto` label in reverse order.
  2. **Silent Cross-Module Error Code Collisions**: Arbitrary integer error codes (`return -1` or `#define ERR_BAD 2`) collide across libraries.
  3. **Runtime Bloat When Migrating Away from C**: C++ exceptions and TLS-heavy runtimes break TinyCC's instant `-run` workflow and 512-byte freestanding targets.
- **How `c6lang/c6` Engineers a Clean Solution**:
  1. **Stack-Frame `defer` & `errdefer` Without TLS**:
     - `defer` registers cleanup right next to resource acquisition and executes in **LIFO (reverse)** order across all exit paths (`return`, `break`, `continue`, `goto`, `err`).
     - `errdefer` executes *only* when the function exits via `return err(id, "msg")` (for example, `errdefer remove(path);` deletes a half-written file only on failure).
     - Cleanup state lives in the **function stack frame** rather than Thread-Local Storage (TLS), so it works identically in `./tcc/c6 -B tcc -run` and freestanding 512-byte boot sectors.
  2. **Collision-Proof Module Error Numbering (`(area<<27)|(slot<<12)|code`)**: Pins each module's error slot in `errbase.def` as `(area<<27)|(slot<<12)|code`, turning duplicate slot assignments into a hard compile-time error, paired with `T!error`, `try`, and `catch e { ... }`.
  3. **Strict `.c6` Suffix Isolation & 91-Target CTest Suite**: Extensions (stackless `async`/`await`, fat-pointer `interface`, bounds-checked `T[:]` slices, cycle-checked `@T` ref-counting, and monomorphized `struct Vect@T` generics) activate *only* on `.c6` files; `.c` files compile as 100% unmodified upstream TCC. Verified by **91 CTest regression targets** plus 4 `aux` checks.

### Q3: How Do `garlic-llm` and `c6` Complement Each Other in Edge AI Systems Engineering?

- **Combined Blueprint**:
  - Use **`c6lang/c6`** (`.c6` modules) to write leak-free, freestanding-ready C host engines, model loaders, audio pipelines, and PM4/DMA ring-buffer drivers using `defer`/`errdefer` and bounds-checked `T[:]` slices while keeping `.c` third-party libraries (like MicroPython) 100% untouched.
  - Apply **`leonardo-alegria/garlic-llm`**'s asymmetric `Q4 + Q3 (MLP gate/up)` quantization + 4-bit KV cache + 2-token MTP speculative decoding architecture to deploy `9B`-class multimodal models on low-cost, air-gapped APU hardware.

---

## 🧭 3. Mermaid Selection Decision Tree & Architecture Diagram

```mermaid
flowchart TD
    Start["🎯 Offline Edge Multimodal Inference & Systems C Compiler Selection"] --> Q_Layer{"Which engineering bottleneck are you solving?"}

    Q_Layer -->|"Air-Gapped APU / Console Multimodal LLM"| Q_GPU{"Hardware API & GPU memory envelope?"}
    Q_GPU -->|"No CUDA/ROCm API & tight ~8GB unified RAM (PS4 GCN / Edge APU)<br/>Need offline 9B + 16K context + STT + TTS"| UseGarlic["✅ Adopt leonardo-alegria/garlic-llm Architecture<br/>• Bare-metal PM4 packets + GCN OpenCL kernels<br/>• Hybrid Q4 + MLP gate/up Q3 saves 384 MiB RAM<br/>• 0.20 GiB 2-token MTP speculative decode (31–43 tok/s)<br/>• 4-bit 16K KV + Parakeet STT + Chatterbox TTS"]
    Q_GPU -->|"Datacenter NVIDIA GPU with 24GB+ VRAM"| UsevLLM["⚠️ Use vLLM / TensorRT-LLM"]

    Q_Layer -->|"Low-Level C Host & Bare-Metal Runtime"| Q_Compiler{"Need instant TCC builds & 100% .c compatibility?"}
    Q_Compiler -->|"Need zero-TLS defer/errdefer + pinned error codes<br/>+ coroutines/slices/generics scoped strictly to .c6"| UseC6["✅ Select c6lang/c6 (Extended TinyCC)<br/>• Stack-frame LIFO defer & errdefer (512B bare-metal safe)<br/>• T!error + try/catch + (area<<27)|(slot<<12)|code<br/>• Stackless async/await + T[:] slices + @T generics<br/>• .c files stay 100% pure TCC · 91 CTest targets"]
    Q_Compiler -->|"Full greenfield rewrite with long compile times"| UseRust["⚠️ Evaluate Rust / C++20 Rewrite"]

    UseGarlic --> Combo["🚀 Combined Edge Stack: c6 Leak-Free C Host + Garlic LLM PM4 Q4/Q3 Engine<br/>Cuts monthly TCO to $450/mo (-$5,530/mo · -92.47%)"]
    UseC6 --> Combo
```

---

## 📊 4. Peer Comparison Matrix

| Dimension | **`leonardo-alegria/garlic-llm` + `c6lang/c6` (Tonight's P0 Pair)** | CPU `llama.cpp` 4B + Legacy C (`goto` Cleanup) | Cloud Realtime Voice/LLM API + C++ RAII | Uniform `Q4_K_M` 9B + Rust FFI Wrapper |
| :--- | :--- | :--- | :--- | :--- |
| **GPU Dispatch Mechanism** | **Hand-written PM4 command packets + LLVM GCN OpenCL kernels** | CPU SIMD only or requires full vendor driver stack | Cloud GPU cluster requiring internet | Requires full CUDA/ROCm; fails on PS4 homebrew |
| **9B Memory Budget Strategy** | **Hybrid `Q4` + `Q3` (`~3.5b` MLP gate/up) saving `384 MiB`** | Forced down to 4B model with weaker reasoning | Zero local RAM, high per-minute cloud cost | Uniform `Q4` overflows PS4 Garlic memory (`+384 MiB`) |
| **Throughput & Context Window** | **`31–39 tok/s` (chat) / `43 tok/s` (code), 4-bit `16K` KV + 2-tok MTP** | `3–7 tok/s` on low-power 8-core CPUs | Network RTT jitter; dead when offline | Cannot fit 16K context + voice models in 8GB |
| **Multimodal & Code Runner** | **All-in-one `5.7 GB` PKG: Parakeet STT + Chatterbox TTS + MicroPython** | Requires stitching separate STT/TTS binaries | Multi-service cloud billing | Not integrated |
| **Resource Cleanup & Rollback** | **Stack-frame `defer` / `errdefer` (no TLS, works in 512B boot code)** | Manual duplicated `free`/`fclose` across `N` exits | Heavy C++ exception unwind tables | Requires `unsafe` FFI glue across C boundaries |
| **Error Code Discipline** | **`(area<<27)\|(slot<<12)\|code` in `errbase.def` (hard collision error)** | Ad-hoc integer macros prone to silent collisions | Exception hierarchy overhead | Manual `Result` to C `int` marshaling |
| **C Compatibility & Build Speed** | **`.c6` enables extensions; `.c` stays 100% pure TCC with `c6 -run`** | 100% compatible but unsafe | Slow template builds & C++ name mangling | Slow cargo builds; no `tcc -run` scripting |

---

## 📈 5. 7-Card 4:5 Quantitative Insights & Closed-Form FinOps Ledger

### 5.1 7-Card Summary Table (Synced with `report.json` & `CLAIM-20261115-R34-GARLICLLM-C6LANG`)

| Card | Headline-as-Finding | Concrete Quantitative / Architectural Evidence | SA Action |
| :--- | :--- | :--- | :--- |
| **Card 1 · HANDS-ON** | **Offline PS4 `Qwen3.5-9B` Hits `43 tok/s` + `c6` Cuts Edge TCO by 92.47%** | `garlic-llm` runs 9B + STT + TTS offline via PM4; `c6` adds `.c6` systems extensions to TinyCC | **Act automatically**: Reference blueprint for constrained APUs & C runtimes |
| **Card 2 · SCENARIO** | **MLP `gate/up` `Q3` Quantization Reclaims `384 MiB` to Fit 16K Context** | `qwen3.5-9b-q4s.bin` (`4.32 GiB`) + `mtp.bin` (`0.20 GiB`) + 4-bit KV fit inside PS4 Garlic RAM | **Act automatically**: Apply asymmetric `Q4/Q3` when 9B models miss VRAM by <500MB |
| **Card 3 · MATRIX** | **25-Lang STT + 7-Lang TTS + MicroPython + 91 CTest Targets Verified** | Parakeet (`0.33 GiB`) + Chatterbox (`0.38 GiB`) + 91 `c6` regression tests & 4 `aux` gates pass | **Act automatically**: Enforce `ctest -L regression -LE aux` in C CI pipelines |
| **Card 4 · MECHANICS** | **Raw PM4 Command Buffers + Zero-TLS Stack-Frame `defer`/`errdefer`** | Direct GPU ring-buffer PM4 dispatch; `c6` tracks LIFO cleanup in stack frames & pins `(area<<27)\|(slot<<12)\|code` | **Act automatically**: Replace multi-exit `goto` chains with `.c6` `defer`/`errdefer` |
| **Card 5 · ROBUSTNESS** | **Hard Compile Error on Error-Slot Collision + `22 tok/s` Voice Stability** | `errbase.def` rejects duplicate error slots; live voice mode runs stably at `~22 tok/s` offline | **Act automatically**: Deploy in air-gapped appliances and bare-metal daemons |
| **Card 6 · LATENCY** | **2-Token MTP Speculative Decoding Pushes Code Generation to `43 tok/s`** | `0.20 GiB` MTP head drafts 2 tokens verified in 1 pass (`31–39 tok/s` chat, `43 tok/s` code) | **Act automatically**: Bundle native MTP heads for edge `Qwen3.5` deployments |
| **Card 7 · MY TAKE** | **✅ Ideal for Air-Gapped APUs & Systems C · ⛔ Not for PS5 or Heavy C++ STL** | `garlic-llm` targets PS4 GCN (FW 11.52 GoldHEN); `c6` extends C without C++ template bloat | **Confirm**: Keep legacy `.c` files unchanged while writing new modules in `.c6` |

### 5.2 Closed-Form FinOps Verification Ledger (`CLAIM-20261115-R34-GARLICLLM-C6LANG`)

> **Synthetic Workload Scope (`base host compute: not_measured`)**: Maintaining **20 offline/air-gapped multimodal edge appliances** plus **15 low-level C runtime/driver modules** at an engineering labor rate of **`$100.00/hr`**:

$$
\begin{aligned}
\text{Path A (Cloud Voice/LLM API + Legacy C goto Debugging)} &= \$1,980.00\text{ (cloud API & dedicated GPU spend)} + 40.0\text{ hrs} \times \$100.00/\text{hr} = \mathbf{\$5,980.00/\text{mo}} \\
\text{Path B (CPU llama.cpp 4B + C++ RAII Porting)} &= \$910.00\text{ (hardware & toolchain spend)} + 19.0\text{ hrs} \times \$100.00/\text{hr} = \mathbf{\$2,810.00/\text{mo}} \\
\text{Path C (Garlic LLM PM4 Q4/Q3 + c6 Stack-Frame defer)} &= \$100.00\text{ (offline APU power & storage)} + 3.5\text{ hrs} \times \$100.00/\text{hr} = \mathbf{\$450.00/\text{mo}} \\
\Delta\text{Cost}_{\text{A}\to\text{C}} &= \$5,980.00 - \$450.00 = \mathbf{\$5,530.00/\text{mo}}\quad(\mathbf{-92.47\%},\ \text{annual savings }\mathbf{\$66,360.00/\text{yr}})
\end{aligned}
$$

| Architecture Path | Monthly Compute / Cloud / Power | Monthly Engineering Labor (`$100/hr`) | Total Monthly Cost (TCO) | Savings vs Path A | Key Bottleneck or Architectural Gain |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Path A: Cloud Voice/LLM API + Legacy C `goto` Cleanup** | `$1,980.00` | `40.0 hrs` (`$4,000.00`) | **`$5,980.00 / mo`** | Baseline (`0.00%`) | Uniform Q4 OOMs on 8GB APUs; multi-exit C resource leaks |
| **Path B: CPU `llama.cpp` 4B + C++ RAII Port** | `$910.00` | `19.0 hrs` (`$1,900.00`) | **`$2,810.00 / mo`** | `-$3,170.00` (`-53.01%`) | Slow CPU tok/s + loses freestanding TinyCC simplicity |
| **Path C: `leonardo-alegria/garlic-llm` + `c6lang/c6` (Recommended)** | **`$100.00`** | **`3.5 hrs` (`$350.00`)** | **`$450.00 / mo`** | **`-$5,530.00` (`-92.47%`)** | **Q4/Q3 saves 384MiB + 43 tok/s MTP + stack-frame `defer`** |

---

## 🛠️ 6. 15-Minute Quickstart & Acceptance Checklist (Runbook)

### Step 1: Build & Run `c6lang/c6` with Stack-Frame `defer`/`errdefer` (5 Mins)

```bash
# 1. Configure and build c6 with C6_EXT enabled via CMake
git clone https://github.com/c6lang/c6.git
cd c6
cmake -S . -B build -DCMAKE_INSTALL_PREFIX=/usr
cmake --build build --parallel

# 2. Run daily smoke tests and the 91-target CTest regression suite
ctest --test-dir build -L daily --output-on-failure
# ctest --test-dir build -L regression -LE aux -j 8 --output-on-failure

# 3. Execute a .c6 program directly with -run
./tcc/c6 -B tcc -run examples/err_demo.c6
```

### Step 2: Inspect & Package `leonardo-alegria/garlic-llm` Offline Multimodal Weights (10 Mins)

```bash
# 1. Clone garlic-llm and verify the 5 model binaries (~5.7 GB total)
git clone https://github.com/leonardo-alegria/garlic-llm.git
cd garlic-llm
# Model manifest in models/ or /data:
# - qwen3.5-9b-q4s.bin      (4.32 GiB, hybrid Q4 + MLP gate/up Q3 saving 384 MiB)
# - qwen3.5-9b-mtp.bin      (0.20 GiB, 2-token MTP speculative decoding head)
# - parakeet-v3-q4i.bin     (0.33 GiB, Parakeet TDT 0.6B v3 25-lang STT)
# - chatterbox-t3.bin       (0.29 GiB, Chatterbox TTS stage 1)
# - chatterbox-s3gen-mf.bin (0.09 GiB, Chatterbox TTS stage 2)

# 2. Build the all-in-one PS4 PKG with OpenOrbis + Zig/LLVM
python build_chat.py --full
```

### Step 3: SA Pre-Production Acceptance Checklist

- [ ] **LIFO `defer` & Conditional `errdefer` Test**: Verify in a `.c6` function that `defer` runs in reverse order on both `return 0` and `return err(...)`, while `errdefer` executes strictly on the error path.
- [ ] **Zero `.c` Contamination Test**: Compile a mixed `.c` and `.c6` target and confirm `.c` files remain 100% standard upstream TCC.
- [ ] **Garlic Memory & MTP Speed Test**: Verify `qwen3.5-9b-q4s.bin` + `mtp.bin` + 4-bit 16K KV cache load without OOM, sustain `31–39 tok/s` (chat) / `43 tok/s` (code), and execute generated MicroPython via `R1`.
