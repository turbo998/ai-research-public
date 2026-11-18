# Pure-Zig Cross-Vendor Inference Engine (`ashhart/TensorFold` `v1.2.7` + `ATC`) & Low-VRAM Model-Agnostic Calibrated Quantization (`huawei-csl/MACaQ` `arXiv:2611.10649`) Selection FAQ

> **Document Scope**: This is the **2026-11-12 Night Shift Round 2 (Cumulative #101) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Infrastructure Architects evaluating two high-signal inference and quantization repositories:
> 1. **`ashhart/TensorFold` (Daily Trending DOM `#7`, `1,864★`, `+58★ today`, Zig, Apache-2.0, `v1.2.7`)**: A zero-Python, zero-MLX single Zig binary serving LLMs directly on **Apple Silicon (Metal), NVIDIA GPUs (CUDA 13), and Vulkan** — `v1.2.7` resumes long conversations on M3 Ultra in **0.3s instead of 85s** even when clients strip earlier reasoning blocks, while pioneering **`ashhart/ATC` (Agent Traffic Control)** to prevent multi-agent file collisions!
> 2. **`huawei-csl/MACaQ` (`176★`, C++ / Python, Apache-2.0, `arXiv:2611.10649`)**: Huawei Computing Systems Lab's **Model-Agnostic Calibrated Quantization** framework — quantizing a **122B-parameter model in 64 minutes on just 32.5 GB of device memory** (**11× faster** than MR-GPTQ and DuQuant++ with lower perplexity), supporting W4A4 across text, image (`FLUX.2-klein-4B`), video (`Wan2.2-TI2V-5B`), and speech (`Qwen3-TTS`) (achieving `2.33×` prefill and `2.58×` decode speedup in vLLM), plus **`MACaQ-R` to refine existing GGUF models while keeping 100% standard `llama.cpp` compatibility**!
>
> **中文版本**: [tensorfold-macaq-zig-cross-gpu-inference-calibrated-gguf-quantization-selection-faq.md](tensorfold-macaq-zig-cross-gpu-inference-calibrated-gguf-quantization-selection-faq.md) · **Daily Digest**: [`daily/2026-11-12.en.md`](../daily/2026-11-12.en.md) · **Architecture Summary SVG**: [`assets/github-ai-radar-2026-11-12-r2-tensorfold-macaq.svg`](../../../assets/github-ai-radar-2026-11-12-r2-tensorfold-macaq.svg)

![TensorFold v1.2.7 and Huawei MACaQ Architecture Comparison](../../../assets/github-ai-radar-2026-11-12-r2-tensorfold-macaq.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "fragile multi-GB Python/MLX/CUDA virtualenvs and 85-second full-history re-prefills whenever a chat client drops earlier `<think>` blocks" (`ashhart/TensorFold` `v1.2.7`)**: Running separate Python stacks for Apple Silicon (MLX) and Linux NVIDIA GPUs (vLLM/PyTorch) creates constant dependency drift. Worse, when chat clients strip earlier reasoning blocks on follow-up turns, naive engines suffer a KV-cache prefix miss and re-prefill the entire conversation. `TensorFold` ships a single Zig binary that drives Metal and CUDA 13 kernels directly without Python, and `v1.2.7` resumes `Qwen3.8-27B` on M3 Ultra at the end of its history in **~0.3s instead of 85s (283× faster)**, complete with `--parallel auto` slot management and `/v1/responses` WebSocket streaming!
   - **Ending "needing an 8×H100 cluster for 10+ hours to calibrate 100B+ quantizations and suffering severe MoE quality degradation on naive GGUF exports" (`huawei-csl/MACaQ` `arXiv:2611.10649`)**: High-quality calibrated quantization methods like MR-GPTQ or DuQuant++ traditionally require massive VRAM and long runtimes. Huawei's `MACaQ` quantizes a **122B model in 64 minutes using just 32.5 GB of device memory** (**11× faster** for matching perplexity), and introduces **`MACaQ-R`**, which refines weight codes inside an existing GGUF (cutting `Qwen3.6-35B-A3B` `Q4_K_XL` KL divergence to FP16 from `0.015731` to **`0.013367`** at the exact same `22.36 GB` file size) while running unmodified on standard `llama.cpp`!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261112-R2-TENSORFOLD-MACAQ`)**:
   - Modeled for a **12-engineer AI infrastructure team operating 24 local/hybrid inference endpoints (M3 Ultra + NVIDIA CUDA) and executing 16 custom quantization releases per month** (fully loaded AI Infra engineer rate `$90.00/hr`; physical colocation rack space and utility electricity bills: `not_measured`):
   - Upgrading from **Path A (split Python MLX/vLLM/Diffusers stacks + 85s dropped-thinking re-prefills + rented multi-GPU calibration runs, `$6,120.00/mo`)** to **Path C (`TensorFold v1.2.7` zero-Python binary + `MACaQ / MACaQ-R` 32.5GB calibrated quantization, `$730.00/mo`)** saves **`$5,390.00/mo` (`-88.07%`, or `$64,680.00/yr`)** and reduces engineering maintenance/calibration labor from `44.0 hrs/mo` to `5.0 hrs/mo` (**`-88.64%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: How does `ashhart/TensorFold` (`v1.2.7`) cut M3 Ultra follow-up latency from `85s` to `0.3s` when clients strip `<think>` blocks, and how does `ATC` prevent multi-agent collisions?
- **First-Principles Breakdown**:
  1. **History-End State Resumption & Two-Tier RAM/Disk Prompt Cache (`v1.2.7`)**:
     - When clients omit earlier reasoning turns, `TensorFold v1.2.7` matches and resumes the conversation state at the end of history on Metal (`Qwen3.8-27B`) and CUDA (`TF_GLM_REQUEST_STARTS=1`), falling back cleanly to RAM if disk cache restore fails. It also adds `TF_FLASHNEXT_SCALE_INDEX=1` (16-bit scale indexing + SSD-expert cache on M1–M4), `LightOnOCR-3` BF16 vision chat on CUDA, and WebSocket mode on `GET /v1/responses`.
  2. **`ashhart/ATC` (Agent Traffic Control) Multi-Agent Lock**:
     - Coordinates concurrent coding agents via `atc check`, `atc claim`, 5-minute `atc pulse` heartbeats, `atc who`, and `atc overlap` before PR creation, publishing live state to `tensorfold.dev/atc`.

### Q2: How does `huawei-csl/MACaQ` (`arXiv:2611.10649`) quantize a 122B model on 32.5 GB VRAM in 64 minutes and refine GGUFs without patching `llama.cpp`?
- **First-Principles Breakdown**:
  1. **32.5 GB Memory-Bounded Calibration & `MACaQ-R` In-Place Code Refinement**:
     - `MACaQ` bounds calibration memory to **32.5 GB** for 122B models (**64 minutes**, **11× faster** than MR-GPTQ/DuQuant++).
     - **`MACaQ-R` (`llamacpp/macaq.py refine`)** optimizes discrete quantized weight codes against an FP16 teacher (`--teacher`) and workload calibration text while preserving native GGUF block formats and scales — reducing `Qwen3.6-35B-A3B` `Q4_K_XL` (`22.36 GB`) KL divergence from `0.015731` to **`0.013367`** for stock `llama cli` / `llama serve`.
  2. **Cross-Modal W4A4 Acceleration**:
     - Delivers **2.33× prefill and 2.58× decode speedups** on `Qwen3.8-27B` in **vLLM** (`W4A4` perplexity `2.8994` vs BF16 `2.8463`), plus W4A4 quantization for **Diffusers** (`FLUX.2-klein-4B`, `Wan2.2-TI2V-5B-Diffusers`, `stable-audio-1.0`), **PyTorch** (`Qwen3-TTS`, `Chatterbox Turbo`), and **Ascend CANN**.

### Q3: How should AI Solution Architects combine `TensorFold` and `MACaQ` in production?
- **Golden-Combo Pattern**:
  - Run **`huawei-csl/MACaQ`** on a single 32GB–48GB workstation GPU to calibrate W4A4 checkpoints (for vLLM/Diffusers) or refine GGUFs via `MACaQ-R`;
  - Deploy **`ashhart/TensorFold v1.2.7`** across Apple Silicon and NVIDIA CUDA 13 nodes for zero-Python deployment and 0.3s long-horizon agent turn resumption!

---

## 🧭 3. Mermaid Decision Tree & Quantization-to-Serving Pipeline

```mermaid
flowchart TD
    A["Cross-Chip Local Inference & Low-VRAM Quantization Architecture Selection"] --> B{"Primary Infrastructure Bottleneck?"}
    B -- "Python/MLX/CUDA dependency drift or 85s re-prefill stalls when clients drop <think> blocks" --> C["Adopt ashhart/TensorFold v1.2.7 (Pure-Zig Binary + ATC Lock)"]
    B -- "100B+ calibration OOMs on single GPUs or MoE GGUF / Diffusion W4A4 accuracy drops" --> D["Adopt huawei-csl/MACaQ (32.5GB 122B Calibration + MACaQ-R GGUF)"]

    C --> C1["Direct Metal / CUDA 13 / Vulkan execution with zero Python or MLX dependencies"]
    C1 --> C2["v1.2.7 resumes long chats with dropped reasoning in ~0.3s vs 85s on M3 Ultra"]
    C2 --> C3["Built-in --parallel auto queuing & WebSocket /v1/responses streaming"]

    D --> D1["GGUF branch: macaq.py refine produces 100% standard llama.cpp files (KL 0.013367)"]
    D1 --> D2["Server branch: vLLM W4A4 (2.33x prefill / 2.58x decode) + Diffusers/PyTorch W4A4"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Split Python Stacks + 8×H100 Calibration | Path B: Uncalibrated PTQ GGUF + Manual Env Sync | **Path C (Recommended): `TensorFold v1.2.7` + `MACaQ / MACaQ-R`** |
| :--- | :--- | :--- | :--- |
| **Runtime Footprint & Cross-Chip Portability** | Multi-GB Python virtualenvs per backend | C++ binary, but lacks stripped-thinking state resume | **Single Zig binary for Metal/CUDA 13/Vulkan + `MACaQ-R` for stock `llama.cpp`** |
| **Follow-Up Latency After Stripped `<think>`** | Full history re-prefill (**~85.0s** on M3 Ultra) | Prefix cache miss & full re-prefill | **`v1.2.7` resumes at history tail in `~0.3s` on M3 Ultra (283× faster)** |
| **122B Model Calibrated Quantization Hardware** | Requires multi-GPU 8×A100/H100 for 10+ hours | Naive round-to-nearest (notable MoE quality loss) | **Single `32.5 GB` GPU in `64 minutes` (`11×` faster; KL cut to `0.013367`)** |
| **Multimodal (Image/Video/Speech) W4A4** | Disjointed per-modality repos | Text/vision only | **Unified W4A4 across `vLLM` (`2.58×` decode), `Diffusers` & `PyTorch` speech** |
| **Multi-Agent Contributor Collision Control** | None | Post-hoc git merge conflicts | **Built-in `ashhart/ATC` (`atc claim/pulse/overlap`) with 5-minute leases** |
| **Monthly TCO (24 Endpoints + 16 Quant Runs)** | **`$6,120.00 / mo`** (`$2,160` GPU + `$3,960` labor) | **`$3,080.00 / mo`** (`$1,100` GPU + `$1,980` labor) | **`$730.00 / mo` (Saves `$5,390.00/mo` · `-88.07%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261112-R2-TENSORFOLD-MACAQ`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A 12-engineer AI infrastructure team managing **24 local/hybrid inference endpoints (Apple Silicon M3 Ultra + Linux NVIDIA GPUs)** and running **16 custom 30B–122B and multimodal quantization releases per month**.
- **Labor Rate**: Fully loaded senior AI Infrastructure engineer rate of **`$90.00 / hr`**.
- **Explicit Not-Measured Boundary**: Data-center colocation rack space and utility electricity bills are marked **`not_measured`**. This model strictly accounts for rented cloud GPU calibration compute, wasted re-prefill GPU cycles, and engineering hours spent on Python environment debugging and quantization tuning.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Split Python Stacks + 8×H100 Calibration | Path B: Uncalibrated PTQ + Manual Env Sync | **Path C: `TensorFold v1.2.7` + `MACaQ` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Cloud Calibration & Re-Prefill GPU Spend** | **`$2,160.00`** | **`$1,100.00`** | **`$280.00`** (32.5GB single-GPU 64m calibration + 0.3s cache resume) |
| **Env Debugging, KV-Miss Tuning & Quantization Labor (`$90/hr`)** | `44.0 hrs × $90.00` = **`$3,960.00`** | `22.0 hrs × $90.00` = **`$1,980.00`** | `5.0 hrs × $90.00` = **`$450.00`** |
| **Total Monthly TCO** | **`$6,120.00 / mo`** | **`$3,080.00 / mo`** (`-49.67%`) | **`$730.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$3,040.00 / mo` | **Saves `$5,390.00 / mo` (`-88.07%` · `$64,680.00/yr`)** |
| **Colocation Rack Space & Utility Power Bills** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `TensorFold v1.2.7` SHA-256 Verification & Zero-Python Launch**: Verify release archive checksums on Apple Silicon or Linux NVIDIA (driver R580+ / CUDA 13), run `tensorfold capabilities --json`, and inspect `/stats` prompt/disk cache telemetry.
- [ ] **2. Stripped-Reasoning Long-Chat Resume Benchmark**: Send multi-turn requests from a client that strips earlier `<think>` blocks (with `TF_GLM_REQUEST_STARTS=1` on CUDA) and verify sub-second (`~0.3s`) time-to-first-token.
- [ ] **3. `MACaQ-R` Standard `llama.cpp` GGUF Refinement**: Run `python llamacpp/macaq.py refine` with domain calibration text and an FP16 teacher, verifying lower KL divergence and direct execution via `llama serve`.
- [ ] **4. `ashhart/ATC` Multi-Agent Collision Gate**: Enforce `atc check`, `atc claim`, and `atc overlap --json` before multi-agent edits on shared inference repositories.
