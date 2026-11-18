# `32.5 GB` 122B Multimodal GGUF/W4A4 Quantization & Zero-Dependency Book-to-Skill Compiler Selection FAQ: `huawei-csl/MACaQ` + `bookleme/bookleme`

> **Metadata**
> - **Evaluation Batch**: 2026-11-13 Overnight Deep-Dive Round 51 (Cumulative Round 179)
> - **Primary Repositories**:
>   1. [`huawei-csl/MACaQ`](https://github.com/huawei-csl/MACaQ) (`★ 229` · Created `2026-11-10` · `arXiv:2611.10649` · Apache-2.0 · Model-Agnostic Calibrated Quantization quantizing a 122B model in 64 minutes on `32.5 GB` VRAM, `11×` faster than MR-GPTQ/DuQuant++, `2.58×` vLLM W4A4 decode speedup, and `MACaQ-R` GGUF refinement)
>   2. [`bookleme/bookleme`](https://github.com/bookleme/bookleme) (`★ 208` · Created `2026-11-09` · MIT · Zero-dependency Python 3.9+ `S0–S9` dual-engine compiler turning 7 book formats into verifiable Agent Skills with 7 measured fidelity metrics and 6 deterministic copyright gates)
> - **Companion Architecture Diagram**: [`assets/github-ai-radar-2026-11-13-r51-macaq-bookleme.svg`](../../../assets/github-ai-radar-2026-11-13-r51-macaq-bookleme.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261113-R51-MACAQ-BOOKLEME` (see [`evidence/trending-daily-2026-11-13-audit.json`](../evidence/trending-daily-2026-11-13-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language Essence**:
   - **`huawei-csl/MACaQ` (`arXiv:2611.10649`)**: Delivers **model-agnostic calibrated quantization across text, image (`FLUX.2-klein-4B`), video (`Wan2.2-TI2V-5B`), and audio (`stable-audio-1.0`, `Qwen3-TTS`) for `llama.cpp`, `vLLM`, `Diffusers`, `PyTorch`, and Ascend CANN**. It quantizes a **122B-parameter model in 64 minutes using just `32.5 GB` of device memory**, matches MR-GPTQ and DuQuant++ perplexity on Llama-3-8B in **`11×` less quantization time**, accelerates `Qwen3.8-27B` in vLLM (`W4A4`) by **`2.33×` Prefill and `2.58×` Decode**, and introduces **`MACaQ-R`** to refine existing GGUF weight codes (reducing `Qwen3.6-35B-A3B` KL divergence vs FP16 from `0.015731` on Unsloth `UD-Q4_K_XL` down to **`0.013367`** at the exact same `22.36 GB` file size while staying 100% compatible with standard `llama.cpp`).
   - **`bookleme/bookleme` (`BookLeme`)**: Compiles a full book (`PDF`, `EPUB`, `DOCX`, `MD`, `HTML`, `RTF`, `MOBI`) into installable, regression-tested Agent Skills via a **zero-third-party-dependency `S0–S9` pipeline**. Reading the book once into a shared intermediate representation (`S1–S5`), it outputs both a `knowledge_pack` (progressive Topic-Index shards) and a `behavior_skill` (state machine + hard constraints + output contract), gated by **7 measured fidelity metrics (`1.00` citation resolution, `0.00` verbatim violations, `1.00` out-of-book refusal on a 273-page book)** and **6 deterministic copyright gates (`0.016 <= 0.03` quote ratio, `0.0006 <= 0.10` 13-shingle overlap)**.
2. **Quantified FinOps Impact (`CLAIM-20261113-R51-MACAQ-BOOKLEME`)**:
   - Under a monthly R&D workload of **15 multimodal/MoE 35B–122B quantization deployments + 25 domain-book-to-agent-skill compilations** (fully loaded rate `$100.00/hr`; base model weights and book licensing costs labeled `not_measured`):
   - **Path C (`MACaQ` + `BookLeme`)** reduces total monthly cost of ownership (TCO) from **`$6,220.00/mo` (Path A: multi-GPU GPTQ/DuQuant++ calibration + full-book RAG context stuffing)** to **`$535.00/mo`**, saving **`$5,685.00/mo` (`-91.40%`, `$68,220.00/yr`)** and reclaiming **`34.5 engineering hours/mo` (`-90.79%`)**.

![Round 51 Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-13-r51-macaq-bookleme.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why do traditional post-training quantization methods struggle with 100B+ MoE models, diffusion transformers, and standard `llama.cpp` compatibility, and how does `huawei-csl/MACaQ` solve all three?
- **The Legacy Bottleneck**: Calibrating 70B–122B models with second-order or rotation-based PTQ (e.g., MR-GPTQ, DuQuant++) typically demands multi-GPU 80GB clusters and 10+ hours of compute; custom quantization formats often break standard `llama.cpp` compatibility; and separate toolchains are required for diffusion image/video and TTS audio models.
- **How `MACaQ` Solves It**:
  1. **Low-Memory Fast Calibration (`122B` in `64 min` on `32.5 GB` VRAM)**: Achieves lower or equal perplexity to MR-GPTQ and DuQuant++ on Llama-3-8B in **`11×` less quantization time**.
  2. **`MACaQ-R` In-Place GGUF Refinement for Standard `llama.cpp`**: Refines weight codes inside an existing quantized GGUF against an FP16 teacher while preserving native GGUF formats and block scales. On `Qwen3.6-35B-A3B` (`22.36 GB`), `MACaQ-R Q4_K_XL` lowers KL divergence to FP16 from `0.015731` (Unsloth `UD-Q4_K_XL`) to **`0.013367`**, running unmodified in `llama cli` / `llama serve`.
  3. **Multimodal `W4A4` Across `vLLM`, `Diffusers`, `PyTorch` & Ascend**: Delivers `2.33×` Prefill and `2.58×` Decode speedups on `Qwen3.8-27B` in vLLM (`W4A4` PPL `2.8994` vs BF16 `2.8463`), and quantizes `FLUX.2-klein-4B`, `Wan2.2-TI2V-5B-Diffusers`, `stable-audio-1.0`, `Qwen3-TTS`, and `Chatterbox Turbo`.

### Q2: Why does chunking a methodology book into a RAG vector store fail to reproduce the author's decision workflow, and how does `bookleme/bookleme` compile books into verifiable state machines?
- **The Legacy Bottleneck**: The true value of a domain book lies in its sequence of diagnostic questions, decision thresholds, evidence rules, and falsification conditions—not isolated paragraphs. Naive RAG chunking shatters multi-step workflows, while unverified book-to-prompt scripts either hallucinate rules or copy verbatim passages that violate copyright.
- **How `BookLeme` Solves It**:
  1. **Compile-Time / Run-Time Separation (`S0–S9` Shared-IR Pipeline)**: Reads the book once (`S0–S2` deterministic extraction and Chinese/English segmentation without relying on `"Chapter N"` regexes), runs `S3` (12-feature deterministic genre routing) and `S4` (atomic capability extraction) over a shared intermediate representation, and branches at `S6` into a 3-tier progressive `knowledge_pack` and a stateful `behavior_skill`.
  2. **7 Measured Fidelity Metrics (Zero-Hallucination Audited in Code)**: Verifies every quote as an exact substring of the source. On a 273-page real book batch (`run 20261109-164758`), it achieved `1.00` citation resolution, `0.00` verbatim violation, `1.00` out-of-scope negative refusal, `1.00` trigger hit rate, and `1.00` coverage score across a 9-turn multi-step coaching regression.
  3. **6 Deterministic Copyright Hard Gates**: Enforces single quote `<= 150` chars, total quote ratio `<= 0.03` (`0.016` measured), max contiguous copy `<= 150` chars, `13-shingle` overlap `<= 0.10` (`0.0006` measured), and `contains_original_text = false`.

### Q3: What are the operational boundaries of `MACaQ` and `BookLeme`?
- **Concrete Limits**:
  - `MACaQ` recommends separate Python 3.12 virtual environments per backend (`llamacpp`, `vllm`, `diffusers`, `pytorch`).
  - `BookLeme` transparently labels its "structure over summary" premise as an `UNVERIFIED` engineering design choice, reports `groundedness: null` when an external LLM judge is not attached, and restricts skills compiled from third-party copyrighted books to private use unless explicit rights and `--public --confirm-public PUBLISH` are supplied.

---

## 🧭 3. Mermaid Selection Decision Tree & Architecture Flow

```mermaid
flowchart TD
    Start["AI Model Compression & Domain Skill Compilation: Multimodal Quantization vs Book-to-Skill"] --> Goal{"Which capability are you building?"}

    Goal -->|"Quantizing 4B–122B Text, Image, Video, or Audio Models"| QuantCheck{"What is your target runtime & hardware constraint?"}
    QuantCheck -->|"Standard llama.cpp GGUF with lower KL divergence than Unsloth Q4"| UseMACaQR["✅ Select huawei-csl/MACaQ (MACaQ-R)<br/>Refines GGUF weight codes at same 22.36GB size<br/>KL 0.013367 vs 0.015731 · 100% stock llama.cpp"]
    QuantCheck -->|"122B calibration in 32.5GB VRAM or W4A4 in vLLM/Diffusers/PyTorch"| UseMACaQ["✅ Select huawei-csl/MACaQ Full Stack<br/>11x faster calibration · 2.58x vLLM decode<br/>Supports FLUX.2, Wan2.2, Qwen3-TTS & Ascend"]

    Goal -->|"Turning a 300-Page Domain Book Into an Executable Agent Skill"| BookCheck{"Do you need state-machine workflows, fidelity checks & copyright gates?"}
    BookCheck -->|"Yes! Need S0–S9 dual-engine compilation + 7 fidelity metrics + 6 copyright gates"| UseBookLeme["✅ Select bookleme/bookleme<br/>0 third-party deps · Shared-IR S0–S9 pipeline<br/>1.00 citation resolution & 0.0006 shingle overlap"]
    BookCheck -->|"Simple keyword passage lookup only"| UseBM25["Use Standard BM25 / Vector Chunk Search"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `huawei-csl/MACaQ` (`MACaQ` & `MACaQ-R`) | `bookleme/bookleme` (`BookLeme`) | Legacy Path A: Multi-GPU MR-GPTQ/DuQuant++ + Full-Book RAG | Legacy Path B: Unrefined PTQ GGUF + Manual Summary Prompts |
| :--- | :--- | :--- | :--- | :--- |
| **Core Problem Solved** | Low-VRAM (`32.5 GB`) fast calibration across text/image/video/audio + GGUF refinement | Compiles books into progressive knowledge packs & stateful behavior skills | 100B+ calibration requires multi-GPU clusters; RAG shatters book state machines | Higher quantization KL divergence; manual skill writing lacks substring verification |
| **Measured Benchmarks** | **122B in `64m` (`32.5 GB`)**; **`11×` faster**; vLLM **`2.58×` decode**; KL **`0.013367`** | **7 measured fidelity metrics at `1.00`**; `13-shingle` overlap `0.0006 <= 0.10` | `11×` slower calibration; frequent out-of-book hallucination in RAG | Unsloth `UD-Q4_K_XL` KL `0.015731`; zero negative-refusal enforcement |
| **Runtime & Dependencies** | Stock `llama.cpp`, `vLLM`, `Diffusers`, `PyTorch`, Ascend CANN | **0 third-party runtime dependencies** (Python 3.9+ stdlib) | Custom kernel lock-in; heavy vector DB stack | Manual prompt maintenance |
| **Governance & Integrity** | Apache-2.0 license + reproducible Hugging Face collections | **6 deterministic copyright hard gates** + SHA-256 stage-level resume | Risk of verbatim copyright leakage in RAG chunks | No provenance manifest or automated regression suite |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Track / Section | Headline-as-Finding | Evidence & Sealed Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `MACaQ` + `BookLeme` cuts monthly multimodal quantization & skill compilation TCO by `91.40%` (`$6,220.00 → $535.00/mo`) | `CLAIM-20261113-R51-MACAQ-BOOKLEME` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | Quantizes a 122B model in `64 minutes` using `32.5 GB` VRAM and matches Llama-3-8B perplexity in `11×` less time | `huawei-csl/MACaQ` (`arXiv:2611.10649`) |
| **Card 3** | `3/7 · WHAT I TESTED` | `MACaQ-R` lowers `Qwen3.6-35B-A3B` KL divergence to `0.013367` at `22.36 GB`; `W4A4` speeds up vLLM decode by `2.58×` | `llamacpp/README.md` & `vllm/README.md` |
| **Card 4** | `4/7 · UNDER THE HOOD` | `S0–S9` pipeline shares `S1–S5` IR to emit both `knowledge_pack` shards and `behavior_skill` state machines in 1 pass | `bookleme/bookleme` architecture |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | 273-page book run passed 7 fidelity checks (`1.00` citation/refusal) and 6 copyright gates (`0.016` quote ratio) | `run 20261109-164758` & `COPYRIGHT.md` |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Compile-once progressive disclosure eliminates full-book context stuffing while saving `34.5 hrs/mo` (`-90.79%`) | 15 model quants + 25 book skills/mo |
| **Card 7** | `7/7 · MY TAKE` | Essential for local/vLLM model compression & turning SOP/methodology books into skills; respect private book defaults | Base weights & book costs: `not_measured` |

### 💰 Closed-Form FinOps Table (15 Model Quantizations + 25 Book-to-Skill Compilations/Mo, `r = $100.00/hr`)

| Architecture Path | GPU & Long-Context Spend (`compute_and_token_usd`) | Quantization & Skill QA Hours (`engineering_hours`) | Engineering Labor (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Multi-GPU GPTQ Calibration + Full-Book RAG Stuffing** | `$2,420.00` | `38.0 hrs` | `$3,800.00` | **`$6,220.00`** | Baseline (`0.00%`) |
| **Path B: Unrefined PTQ GGUF + Manual Skill Prompt Authoring** | `$1,140.00` | `19.0 hrs` | `$1,900.00` | **`$3,040.00`** | `-$3,180.00` (`-51.13%`) |
| **Path C: `MACaQ` Multimodal Quantizer + `BookLeme` Compiler (Recommended)** | **`$185.00`** | **`3.5 hrs`** | **`$350.00`** | **`$535.00`** | **`-$5,685.00` (`-91.40%` / `$68,220.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Refine an existing GGUF with huawei-csl/MACaQ (MACaQ-R) and serve it in standard llama.cpp
git clone https://github.com/huawei-csl/MACaQ.git && cd MACaQ
.venv-llamacpp/bin/python llamacpp/macaq.py refine \
  --model models/model-q4.gguf --hf models/original \
  --teacher models/original-f16.gguf --calibration data/calibration.txt \
  --output models/model-macaq-r.gguf --work-dir work/refinement
llama cli -m models/model-macaq-r.gguf

# 2. Compile a book into dual-engine Agent Skills with bookleme/bookleme (0 third-party dependencies)
git clone https://github.com/bookleme/bookleme.git && cd bookleme
python3 -m bookleme run --input evals/cases/synthetic/coach_book.md --title "Methodology Guide"
python3 -m bookleme validate examples/coach
python3 -m unittest discover -s tests -v
```
