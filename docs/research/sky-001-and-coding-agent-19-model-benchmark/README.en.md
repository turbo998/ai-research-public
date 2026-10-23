# SKY-001 Engineering World Model & Coding Agent 19-Model Benchmark Deep Dive (Supplement 5: Adding `Claude Haiku 5.5` & `Gemini 4 Argon`)

> **中文版**: [`README.md`](README.md) · **7-Card 4:5 Visual Benchmark Report**: [`test-report.en.md`](test-report.en.md) (English) / [`test-report.md`](test-report.md) (中文) / [`test-report-cards.html`](test-report-cards.html) (Self-contained CSP HTML Deck)
> **Structured Data & Evidence Lock**: [`report.json`](report.json) · [`evidence.json`](evidence.json) · [`evidence/verifier-summary.json`](evidence/verifier-summary.json) · **Methodology Audit**: [`review.md`](review.md)
> **Runnable Offline Verification Suite**: [`simulator/sky001_and_19model_verifier.py`](simulator/sky001_and_19model_verifier.py) · [`simulator/test_sky001_and_19model_verifier.py`](simulator/test_sky001_and_19model_verifier.py)

---

## 1. Attribution, Reproduction Boundaries & Primary Evidence Anchors

- **Provenance Status**: `anonymized_reported` (`independently_reproduced=false`) + Local Deterministic Offline Verifier Suite (`6/6` unit tests passing).
- **Dual-Track Scope**:
  1. **Track A — Coding Agent 19-Model Benchmark (Supplement 5)**: Pinned to public repository [`satomic/copilot-benchmark`](https://github.com/satomic/copilot-benchmark) at commit [`a191383571a13143685fd6f7787512c4e281a9ba`](https://github.com/satomic/copilot-benchmark/commit/a191383571a13143685fd6f7787512c4e281a9ba) (`2026-10-15T08:28:58Z`, commit message `"add haiku 5.5 and gemini 5 argon"`; note that the commit message contained a typo `"gemini 5 argon"`, whereas all bundle directories, `run.json` files, and the CAPI `/models` catalog identify the model as `gemini-4-argon` / `Gemini 4 Argon`). Executed on **GitHub Copilot CLI `1.0.98`**, Supplement 5 adds `22` complete run bundles (`11` tasks × `2` models) for **`Claude Haiku 5.5`** and **`Gemini 4 Argon`**, expanding the non-reference matrix from 17 models (`187` runs, see [`coding-agent-17-model-benchmark`](../coding-agent-17-model-benchmark/README.md)) to **19 models × 11 tasks = `209` serial CLI runs** (plus `11` `_reference` golden bundles, with `1,310` hidden `pytest` assertions per model).
  2. **Track B — Skyfall AI `SKY-001` ("The First World Model for Engineering")**: Audited directly from Skyfall AI's production JavaScript bundles published on `2026-10-19` — the product landing bundle (`https://skyfall.ai/assets/index-D5BqB7X_.js`, `494,518` bytes, SHA-256 `1bc34257c0f2f1db82336d13f95f88c391950c0957655377f752954b4cd7199f`) and the technical blog bundle (`https://skyfall.ai/assets/article-D6mnIEDb.js`, `77,103` bytes, SHA-256 `8f22592c0d7f0bc1600158903685a5212ddb417499cde1c1e93754de5e6a9830`). `SKY-001` is currently a waitlist-only closed preview with no public model weights, API, or raw 2,000-case geometry files.

---

## 2. Executive Summary

1. **`Claude Haiku 5.5` Redefines the Lightweight Coding Agent Pareto Frontier (Rank #4 Overall, `99.24` Mean, `$0.33`)**:
   - Under the exact same 11 Python standard-library tasks and `70/15/15` rubric, `Haiku 5.5` achieves a **`99.24 / 100` overall mean (`1,091.61 / 1,100` total)**, ranking **#4 out of 19 models** — trailing only `Fable 5.1` (`99.77`), `Opus 5.5` (`99.68`), and `Opus 5` (`99.59`), while beating `Grok 4.7` (`99.21`), `Sonnet 5.5` (`99.00`), `GPT-6.1 Sol` (`98.86`), and `GPT-6 Astra` (`98.82`).
   - Compared to its predecessor `Haiku 4.5` (`93.96` mean, `89.64` Complex mean, `1,239/1,310` hidden pass, `$3.93`), `Haiku 5.5` **gains `+5.28` overall points and `+9.58` Complex points (to `99.22`), cuts API rounds by `72.4%` (`341 -> 94`), and slashes cost by `91.6%` (`$3.93 -> $0.33`)**, making it the second-cheapest model in the 19-model cohort after `GPT-6 Luna` (`$0.17`).
   - Across `1,310` hidden assertions, `Haiku 5.5` misses only **2 assertions** (`1,308 / 1,310 = 99.85%`), both in `C4-microvm` (`_verify.test_c4::test_parse_errors[if true { }]` and `[while true { }]`).
2. **`Gemini 4 Argon` Becomes the 9th Model to Pass `1,310 / 1,310` (`100%`) Hidden Assertions (Rank #10, `98.59` Mean, `$2.82`)**:
   - `Gemini 4 Argon` scores **`98.59 / 100` overall (`1,084.50 / 1,100`)** and passes **`1,310 / 1,310` (`100%`) hidden assertions**, eliminating all 34 hidden test failures of `Gemini 3.8 Flash` (`1,276/1,310`).
   - It reduces API rounds by `61.7%` vs `Gemini 3.8 Flash` (`277 -> 106`) and wall-clock time by `47.1%` (`5,122s -> 2,710s = 45.2m`). Aided by its **`$0.00 / 1M tokens` `cache_write` pricing** in the CAPI catalog, its 11-task cost is **`$2.82`** (`282.09` AI credits).
3. **`SKY-001` Demonstrates Why Hierarchical 3D State Decomposition Beats One-Shot LLM Scripting — Along With Clear Readiness Boundaries**:
   - **Two-Stage Architecture**: Stage 1 (`Hierarchical Composer`) generates coarse 3D variations via a Diffusion Transformer (DiT), recursively splits them in parallel across tree depth $D$, and refines occluded internal leaf geometry. Stage 2 (`Construction World Model`) predicts intermediate 3D solid states (subgoals) before predicting the inverse 2D sketch between consecutive states, using a **Matryoshka-style autoencoder** (rolling out in compact leading latents first, then restoring sharp edges and exact vertices via a parallel full-resolution Refiner).
   - **Critical-Path Mathematics**: On `Jaguar E-Type Roadster` ($L=103$ leaves, $N=139$ nodes, depth $D=5$, $S=100$ steps/part, $W=128$ parallel workers), a flat autoregressive chain requires $36 + 103 \times 100 = 10,336$ sequential steps, whereas `SKY-001`'s tree requires only $5 + 1 \times 100 = 105$ sequential steps (**`98.44x` shorter critical path**).
   - **Dual-Source JS Bundle Audit Findings**:
     - On the 1,000-part CAD construction benchmark, `SKY-001` reaches **`79.7%` IoU at `3.9s/case` and `$0.005/case`** vs `GPT-6 Astra`'s **`79.1%` IoU at `199s/case` and `$0.75/case`** — a `+0.6` pt IoU tie without variance disclosure, but **`51.0x` faster and `150.0x` cheaper**.
     - **Undisclosed Blog vs Landing Page Discrepancy**: The blog bundle (`article-D6mnIEDb.js`) includes **`Gemini 4` (`76.9%` IoU, `253s`, `$0.25`)** in the CAD table, whereas the landing page bundle (`index-D5BqB7X_.js`) omits `Gemini 4` and replaces it with **`Opus 5.5` (`69.4%` IoU, `110s`, `$0.31`)** and **`Gemini 3.8 Flash` (`54.7%` IoU, `112s`, `$0.08`)**.
     - On the 1,000-plan BIM benchmark, **`Gemini 3.8 Flash` (`42.3%` IoU) beats `GPT-6 Astra` (`40.6%` IoU) to take 2nd place overall**, trailing `SKY-001` (`43.6%` IoU, `1.22s`, `$0.0024`) by just `1.3` percentage points.
     - **Capability Boundary**: Today's `SKY-001` outputs a **visual plan (predicted 3D states + 2D sketches)** rather than an executable parametric CAD feature tree (the blog explicitly notes that *"sketch rollouts would become executable operations with an editable feature history"* is future work).

---

## 3. Skyfall AI `SKY-001` Engineering World Model Technical Audit

### 3.1 Founders, Corpus Density & Problem Formulation

Founded by Maluuba co-founders **Sam Pasupalak** and **Kaheer Suleman** alongside **Sumit Pasupalak**, Skyfall AI developed `SKY-001` over 18 months (`skyfall.ai/blog/introducing-sky-001`). Their central thesis is that CAD and BIM are **hierarchical, state-dependent spatial construction problems** that map poorly to flat 1D token streams:

1. **Absence of Intermediate 3D State**: When an LLM writes a 100-step Blender or CAD script in one shot, it cannot observe the evolving 3D solid after step $t$ before deciding step $t+1$.
2. **Serial Critical-Path Bottlenecks**: Generating 100 parts × 100 steps sequentially requires $10,000$ serial forward passes.
3. **Dataset Part-Density Gap**: Public 3D datasets such as PartVerse have a median of **`6` parts/object (`p99 = 33`)**, whereas Skyfall's proprietary corpus (`>200,000` parts for Composer, `>600,000` CAD construction trajectories, `~35,000` BIM floor plans / `~2,000,000` drawing states) has a median of **`288` parts/object (`p99 = 4,180`)** (e.g., fat bike `988` vs BMX `8`, Ducati 900SS `751` vs Harley `34`, quadruped robot `542` vs mech `85`).

### 3.2 Critical-Path Tree Parallelization Verification

For an assembly tree with $N$ total nodes, $L$ leaves, $N-L$ internal split nodes, depth $D$, $S=100$ construction steps per leaf, and $W=128$ parallel workers:
$$T_{\text{flat}} = (N - L) + L \times S, \qquad T_{\text{tree}} = D + \left\lceil \frac{L}{W} \right\rceil \times S$$

| Showcase Assembly | Leaves ($L$) | Total Nodes ($N$) | Internal Splits ($N-L$) | Tree Depth ($D$) | Flat Sequential Steps ($T_{\text{flat}}$) | Hierarchical Sequential Steps ($T_{\text{tree}}$) | Critical-Path Speedup |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Jaguar E-Type Roadster** | `103` | `139` | `36` | `5` | `10,336` | `105` | **`98.44x`** |
| **Minitractor 4x4** | `92` | `130` | `38` | `5` | `9,238` | `105` | **`87.98x`** |
| **Jet Engine** | `70` | `96` | `26` | `5` | `7,026` | `105` | **`66.91x`** |
| **FANUC ArcMate 100iB** | `35` | `55` | `20` | `4` | `3,520` | `104` | **`33.85x`** |

### 3.3 Dual-Source JS Bundle Benchmark Audit (`article-D6mnIEDb.js` vs `index-D5BqB7X_.js`)

#### Table 3.3A: CAD Construction Benchmark (1,000 Parts, ~100 Steps/Part, Metric: 3D IoU / Time / Cost)

| Model | Blog Bundle IoU (`article-D6mnIEDb.js`) | Landing Bundle IoU (`index-D5BqB7X_.js`) | Time (`s/case`) | Cost (`$/case`) | Speed Ratio vs `SKY-001` | Cost Ratio vs `SKY-001` | Audit Note |
|---|---:|---:|---:|---:|---:|---:|---|
| **`SKY-001` (Ours)** | **`79.7%`** | **`79.7%`** | **`3.9 s`** | **`$0.005`** | `1.0x` | `1.0x` | Identical across both bundles |
| **`GPT-6 Astra`** | **`79.1%`** | **`79.1%`** | `199.0 s` | `$0.750` | **`51.0x` slower** | **`150.0x` costlier** | `-0.6` pt IoU gap (statistical tie without spread) |
| **`Gemini 4`** | **`76.9%`** | *Omitted* | `253.0 s` | `$0.250` | `64.9x` slower | `50.0x` costlier | **Present only in blog bundle**; removed on landing page |
| **`Opus 5.5`** | *Omitted* | **`69.4%`** | `110.0 s` | `$0.310` | `28.2x` slower | `62.0x` costlier | **Present only in landing page bundle** |
| **`Gemini 3.8 Flash`** | *Omitted* | **`54.7%`** | `112.0 s` | `$0.080` | `28.7x` slower | `16.0x` costlier | **Present only in landing page bundle** |
| **`Qwen 3.8 Max`** | `34.4%` | `34.4%` | `764.0 s` | `$0.300` | `195.9x` slower | `60.0x` costlier | Identical across both bundles |
| **`Kimi K3`** | `9.5%` | `9.5%` | `439.0 s` | `$0.130` | `112.6x` slower | `26.0x` costlier | Severe degradation in blind one-shot 3D scripting |
| **`Grok 4.7`** | `null` (no output) | `null` (no output) | `1,250.0 s` | `$0.590` | `320.5x` slower | `118.0x` costlier | Failed to produce valid output within budget |

#### Table 3.3B: BIM Floor Plan Construction Benchmark (1,000 Floor Plans: ~350 IFC + 650 Apartments, ~70 Steps/Plan)

| Model | Blog IoU | Landing IoU | Blog / Landing Time | Blog / Landing Cost | Speed Ratio vs `SKY-001` | Cost Ratio vs `SKY-001` | Audit Note |
|---|---:|---:|---:|---:|---:|---:|---|
| **`SKY-001` (Ours)** | **`43.6%`** | **`43.6%`** | **`1.22 s`** / `1.22 s` | **`$0.0024`** / `$0.00237` | `1.0x` | `1.0x` | Landing bundle retains 5 decimal places (`0.00237`) |
| **`Gemini 3.8 Flash`** | **`42.3%`** | **`42.3%`** | `346.2 s` / `345.4 s` | `$0.218` / `$0.2185` | `283.8x` slower | `90.8x` costlier | **2nd place overall**, beating `GPT-6 Astra` by `+1.7` pts |
| **`GPT-6 Astra`** | **`40.6%`** | **`40.6%`** | `144.6 s` / `144.4 s` | `$0.446` / `$0.4465` | **`118.5x` slower** | **`185.8x–188.4x` costlier** | Launch thread "125x faster / 210x cheaper" overstates exact bundle ratios |
| **`Opus 5.5`** | *Omitted* | **`34.4%`** | — / `113.1 s` | — / `$0.276` | `92.7x` slower | `116.5x` costlier | **Present only in landing page bundle** |
| **`Kimi K3`** | `33.7%` | `33.7%` | `113.9 s` / `114.0 s` | `$0.270` / `$0.270` | `93.4x` slower | `112.5x` costlier | Substantially better on BIM than on CAD |
| **`Qwen 3.8 Max`** | `28.8%` | `28.8%` | `255.3 s` / `254.5 s` | `$0.111` / `$0.111` | `209.3x` slower | `46.3x` costlier | `0.8s` rounding difference between bundles |
| **`Grok 4.7`** | `28.2%` | `28.2%` | `592.1 s` / `592.3 s` | `$0.305` / `$0.305` | `485.3x` slower | `127.1x` costlier | Produces valid BIM output (`28.2%`), unlike CAD (`null`) |

---

## 4. Supplement 5: Coding Agent 19-Model Benchmark Analysis

### 4.1 Scores by Difficulty & Hidden Test Pass Rate (`19` Models × `11` Tasks = `209` Runs)

| Rank | Model | Cohort | CLI Version | Atomic (`A1–A5`) | Medium (`M1–M2`) | Complex (`C1–C4`) | Total Mean (`11` Tasks) | Hidden Assertions (`1,310`) | Action Gating |
|---:|---|---|---|---:|---:|---:|---:|---:|---|
| **1** | **Fable 5.1** | Baseline (5-Model) | `1.0.84-3` | `100.00` | `99.50` | `99.62` | **`99.77`** | `1,310 / 1,310` (`100.0%`) | `Act automatically` |
| **2** | **Opus 5.5** | Supplement 3 (15-Model) | `1.0.89-5` | `99.80` | `99.50` | `99.62` | **`99.68`** | `1,310 / 1,310` (`100.0%`) | `Act automatically` |
| **3** | **Opus 5** | Baseline (5-Model) | `1.0.84-3` | `99.80` | `99.50` | `99.38` | **`99.59`** | `1,310 / 1,310` (`100.0%`) | `Act automatically` |
| **4** | **Haiku 5.5 [NEW]** | **Supplement 5 (19-Model)** | **`1.0.98`** | **`99.15`** | **`99.50`** | **`99.22`** | **`99.24`** | **`1,308 / 1,310` (`99.85%`)** | `Confirm` |
| **5** | **Grok 4.7** | Supplement 2 (12-Model) | `1.0.89-0` | `99.00` | `99.50` | `99.33` | **`99.21`** | `1,299 / 1,310` (`99.16%`) | `Confirm` |
| **6** | **Sonnet 5.5** | Supplement 4 (17-Model) | `1.0.90-5` | `98.80` | `99.12` | `99.19` | **`99.00`** | `1,310 / 1,310` (`100.0%`) | `Act automatically` |
| **7** | **GPT-6.1 Sol** | Supplement 4 (17-Model) | `1.0.90-5` | `98.40` | `99.00` | `99.38` | **`98.86`** | `1,310 / 1,310` (`100.0%`) | `Act automatically` |
| **8** | **GPT-6 Astra** | Baseline (5-Model) | `1.0.84-3` | `98.00` | `99.00` | **`99.75`** | **`98.82`** | `1,310 / 1,310` (`100.0%`) | `Act automatically` |
| **9** | **Sonnet 5** | Baseline (5-Model) | `1.0.84-3` | `98.40` | `99.12` | `98.88` | **`98.70`** | `1,310 / 1,310` (`100.0%`) | `Act automatically` |
| **10** | **Kimi K3** | Supplement 1 (10-Model) | `1.0.84-8` | `98.40` | `99.12` | `98.81` | **`98.68`** | `1,305 / 1,310` (`99.62%`) | `Confirm` |
| **11** | **Gemini 4 Argon [NEW]** | **Supplement 5 (19-Model)** | **`1.0.98`** | **`99.00`** | **`98.62`** | **`98.06`** | **`98.59`** | **`1,310 / 1,310` (`100.0%`)** | `Act automatically` |
| **12** | **Grok 4.6** | Supplement 1 (10-Model) | `1.0.84-8` | `98.40` | `100.00` | `98.06` | **`98.57`** | `1,305 / 1,310` (`99.62%`) | `Confirm` |
| **13** | **HydraFusion** | Supplement 3 (15-Model) | `1.0.89-5` | `98.40` | `98.00` | `98.75` | **`98.45`** | `1,310 / 1,310` (`100.0%`) | `Act automatically` |
| **14** | **GPT-6 Luna** | Supplement 2 (12-Model) | `1.0.89-0` | `98.80` | `99.12` | `96.88` | **`98.16`** | `1,279 / 1,310` (`97.63%`) | `Confirm` |
| **15** | **Gemini 3.8 Flash** | Supplement 1 (10-Model) | `1.0.84-8` | `98.75` | `98.12` | `97.00` | **`98.00`** | `1,276 / 1,310` (`97.40%`) | `Confirm` |
| **16** | **GPT-5.6 Luna** | Supplement 1 (10-Model) | `1.0.84-8` | `98.40` | `99.50` | `96.42` | **`97.88`** | `1,293 / 1,310` (`98.70%`) | `Confirm` |
| **17** | **MAI-Code-1.1-Flash** | Supplement 1 (10-Model) | `1.0.84-8` | `98.20` | `98.62` | `96.61` | **`97.70`** | `1,284 / 1,310` (`98.02%`) | `Confirm` |
| **18** | **DeepSeek-V4-Flash** | Supplement 3 (BYOK) | `1.0.89-6` | `97.30` | `88.00` | `95.91` | **`95.10`** | `1,250 / 1,310` (`95.42%`) | `Send to a human` |
| **19** | **Haiku 4.5** | Baseline (5-Model) | `1.0.84-3` | `97.25` | `94.39` | `89.64` | **`93.96`** | `1,239 / 1,310` (`94.58%`) | `Send to a human` |

### 4.2 API Rounds, Token Usage, Wall/Inference Time & Cost (`19` Models)

| Model | Atomic Rds | Medium Rds | Complex Rds | C/A Ratio | Total Rds | Output Tokens | Total Cost (`$`) | Wall Time (`s` / `min`) | Pure Inference (`s` / `min`) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Fable 5.1** | `4.2` | `13.0` | `23.8` | `5.7x` | `142` | `157,854` (`15.8w`) | `$14.45` | `3,355s` (`55.9m`) | `2,210s` (`36.8m`) |
| **Opus 5.5** | `4.8` | `7.5` | `13.2` | `2.8x` | `92` | `175,976` (`17.6w`) | `$5.84` | `1,909s` (`31.8m`) | `1,570s` (`26.2m`) |
| **Opus 5** | `5.0` | `12.5` | `34.5` | `6.9x` | `188` | `249,164` (`24.9w`) | `$17.41` | `3,797s` (`63.3m`) | `3,042s` (`50.7m`) |
| **Haiku 5.5 [NEW]** | **`4.2`** | **`8.5`** | **`14.0`** | **`3.3x`** | **`94`** | **`453,116` (`45.3w`)** | **`$0.33`** | **`2,104s` (`35.1m`)** | **`1,852s` (`30.9m`)** |
| **Grok 4.7** | `5.0` | `6.5` | `26.2` | `5.2x` | `143` | `514,873` (`51.5w`) | `$12.22` | `10,873s` (`181.2m`) | `7,849s` (`130.8m`) |
| **Sonnet 5.5** | **`2.8`** | `6.5` | `9.5` | `3.4x` | `65` | `161,136` (`16.1w`) | `$2.89` | **`1,301s` (`21.7m`)** | **`995s` (`16.6m`)** |
| **GPT-6.1 Sol** | `4.4` | **`5.0`** | **`7.0`** | `1.6x` | **`60`** | `92,907` (`9.3w`) | `$1.71` | `1,645s` (`27.4m`) | `1,348s` (`22.5m`) |
| **GPT-6 Astra** | `4.0` | `5.5` | `7.8` | `1.9x` | `62` | `98,061` (`9.8w`) | `$9.91` | `1,960s` (`32.7m`) | `1,617s` (`27.0m`) |
| **Sonnet 5** | `5.0` | `12.5` | `35.0` | `7.0x` | `190` | `239,150` (`23.9w`) | `$7.87` | `3,192s` (`53.2m`) | `2,393s` (`39.9m`) |
| **Kimi K3** | `6.6` | `16.5` | `19.2` | `2.9x` | `143` | `175,321` (`17.5w`) | `$5.58` | `9,028s` (`150.5m`) | `4,944s` (`82.4m`) |
| **Gemini 4 Argon [NEW]** | **`6.0`** | **`7.5`** | **`15.2`** | **`2.5x`** | **`106`** | **`116,755` (`11.7w`)** | **`$2.82`** | **`2,710s` (`45.2m`)** | **`2,512s` (`41.9m`)** |
| **Grok 4.6** | `8.0` | `10.0` | `19.5` | `2.4x` | `138` | `194,210` (`19.4w`) | `$5.21` | `4,172s` (`69.5m`) | `3,302s` (`55.0m`) |
| **HydraFusion** | `6.2` | `8.0` | `9.5` | **`1.5x`** | `85` | **`88,979` (`8.9w`)** | `$3.58` | `1,444s` (`24.1m`) | `1,034s` (`17.2m`) |
| **GPT-6 Luna** | `4.8` | `8.0` | `24.8` | `5.2x` | `139` | `145,411` (`14.5w`) | **`$0.17`** | `2,675s` (`44.6m`) | `2,129s` (`35.5m`) |
| **Gemini 3.8 Flash** | `18.0` | `28.5` | `32.5` | `1.8x` | `277` | `122,989` (`12.3w`) | `$2.83` | `5,122s` (`85.4m`) | `3,750s` (`62.5m`) |
| **GPT-5.6 Luna** | `9.2` | `14.0` | `40.2` | `4.4x` | `235` | `106,599` (`10.7w`) | `$0.39` | `3,061s` (`51.0m`) | `1,316s` (`21.9m`) |
| **MAI-Code-1.1-Flash** | `6.0` | `14.0` | `33.5` | `5.6x` | `192` | `233,100` (`23.3w`) | `$0.53` | `3,388s` (`56.5m`) | `2,448s` (`40.8m`) |
| **DeepSeek-V4-Flash** | `8.0` | `22.0` | `84.0` | `10.5x` | `420` | `290,100` (`29.0w`) | `$1.95` | `10,740s` (`179.0m`) | `5,618s` (`93.6m`) |
| **Haiku 4.5** | `13.8` | `22.0` | `57.0` | `4.1x` | `341` | `303,100` (`30.3w`) | `$3.93` | `4,849s` (`80.8m`) | `3,163s` (`52.7m`) |

---

## 5. Cross-Modality Synthesis: One-Shot 3D CAD Scripting vs Multi-Turn CLI Software Engineering

| Model Family | Copilot CLI Coding Mean (`11` Tasks) | Copilot CLI Complex Mean (`C1–C4`) | Copilot CLI Hidden Pass | Copilot CLI 11-Task Cost / Wall | SKY-001 CAD 1,000-Case IoU (One-Shot) | SKY-001 CAD Time / Cost per Part | SKY-001 BIM 1,000-Plan IoU | Root-Cause Synthesis |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **`GPT-6 Astra`** | `98.82` (#8) | **`99.75` (#1)** | `1,310 / 1,310` (`100%`) | `$9.91` / `32.7m` | **`79.1%`** (#2) | `199s` / `$0.75` | `40.6%` (#3) | Strong spatial and systems reasoning, but serial 100-step CAD generation is `51x` slower |
| **`Claude Opus 5.5`** | **`99.68` (#2)** | `99.62` (#2) | `1,310 / 1,310` (`100%`) | `$5.84` / `31.8m` | `69.4%` (landing) | `110s` / `$0.31` | `34.4%` (landing) | Near-perfect with a CLI test loop; handicapped when forced into single-shot blind 3D scripting |
| **`Gemini 4 / Argon`** | `98.59` (#11) | `98.06` | `1,310 / 1,310` (`100%`) | `$2.82` / `45.2m` | `76.9%` (blog #3) | `253s` / `$0.25` | *Not listed* | Top-3 spatial CAD IoU (`76.9%`) and `100%` CLI hidden pass rate |
| **`Gemini 3.8 Flash`** | `98.00` (#15) | `97.00` | `1,276 / 1,310` (`97.4%`) | `$2.83` / `85.4m` | `54.7%` (landing) | `112s` / `$0.08` | **`42.3%` (#2!)** | Exceptional 2D/3D floor-plan layout (beats Astra on BIM); superseded by Argon on complex code |
| **`Kimi K3`** | `98.68` (#10) | `98.81` | `1,305 / 1,310` (`99.6%`) | `$5.58` / `150.5m` | `9.5%` | `439s` / `$0.13` | `33.7%` | Relies on iterative execution feedback; collapses in feedback-free one-shot CAD |
| **`Grok 4.7`** | `99.21` (#5) | `99.33` | `1,299 / 1,310` (`99.2%`) | `$12.22` / `181.2m` | `null` (`0%`) | `1,250s` / `$0.59` | `28.2%` | Heavy reasoning token volume (`51.5w` in CLI); times out on single-request 3D CAD scripts |

---

## 6. Running the Offline Verifier & Unit Tests

```powershell
python docs\research\sky-001-and-coding-agent-19-model-benchmark\simulator\sky001_and_19model_verifier.py
python docs\research\sky-001-and-coding-agent-19-model-benchmark\simulator\test_sky001_and_19model_verifier.py
```
