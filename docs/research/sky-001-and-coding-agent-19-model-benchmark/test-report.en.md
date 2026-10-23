# SKY-001 Engineering World Model & Coding Agent 19-Model Benchmark Report (Supplement 5: `Claude Haiku 5.5` & `Gemini 4 Argon`)

> **中文版**: [`test-report.md`](test-report.md) · **Comprehensive Study**: [`README.en.md`](README.en.md) (English) / [`README.md`](README.md) (中文)
> **Format**: 7-Card 4:5 Portrait Visual Report Deck (`900x1125` / `1080x1350`)
> **Interactive / Print Deck**: [`test-report-cards.html`](test-report-cards.html) · **Structured Data**: [`report.json`](report.json) · **Primary Evidence**: [`evidence.json`](evidence.json) · **Offline Verifier**: [`simulator/sky001_and_19model_verifier.py`](simulator/sky001_and_19model_verifier.py)
> **Provenance**: `anonymized_reported` (`independently_reproduced=false`) · **Pinned Upstream Sources**: [`satomic/copilot-benchmark@a1913835`](https://github.com/satomic/copilot-benchmark/commit/a191383571a13143685fd6f7787512c4e281a9ba) + Skyfall AI Production JS Bundles (`index-D5BqB7X_.js` & `article-D6mnIEDb.js`)

---

## Card 1 (`1 / 7` · `HANDS-ON · ENGINEERING WORLD MODEL & 19-MODEL CODING BENCHMARK`)

### Haiku 5.5 (#4 at $0.33), Gemini 4 Argon (100% hidden) & **SKY-001 98.4x Critical-Path Scaling**

In Supplement 5 (`2026-10-15`, Copilot CLI `1.0.98`), the Coding Agent evaluation matrix expands to **19 models × 11 Python standard-library engineering tasks (`209` non-reference serial CLI runs, `1,310` hidden assertions per model)**: lightweight **`Claude Haiku 5.5` leaps to #4 overall (`99.24 / 100`) for just `$0.33` (`1,308 / 1,310` hidden pass)**, while **`Gemini 4 Argon` passes `1,310 / 1,310` (`100%`) hidden assertions (`98.59` mean, `$2.82`)**. Cross-auditing Skyfall AI's **`SKY-001` Engineering World Model** from its production JS bundles shows how hierarchical 3D state decomposition and Matryoshka two-pass diffusion run **`51.0x–118.5x` faster and `150.0x–188.4x` cheaper** than one-shot LLM CAD/BIM scripts across 2,000 test cases.

#### Workbench Preview (`Dual-Track Engineering Benchmark Workbench · 19 Coding Agents + SKY-001 CAD/BIM`)

| Left Column · Tracks, Cohorts & Gating | Center Column · Protocol & Verification | Right Column · Headline Metrics & Decisions |
|---|---|---|
| **Track A · Coding Agent (19 Models × 11 Tasks = 209 Runs)**<br>• **Atomic (`A1–A5`)**: `70` hidden + `15` spec + `15` quality<br>• **Medium (`M1–M2`)**: `55` hidden + `15` self-test + `15` spec + `15` quality<br>• **Complex (`C1–C4`)**: `58` hidden + `12` self-test + `15` spec + `15` quality<br>• **Supplement 5 (`2026-10-15` · CLI `1.0.98`)**: Adds **`Claude Haiku 5.5`** & **`Gemini 4 Argon`** (`+22` bundles)<br><br>**Track B · SKY-001 World Model (2,000 CAD/BIM Cases)**<br>• **Stage 1 (Hierarchical Composer)**: Coarse 3D DiT $\rightarrow$ Recursive Tree Split $\rightarrow$ Leaf Occlusion Refiner<br>• **Stage 2 (Construction World Model)**: 3D Solid State Subgoals + 2D Inverse Sketches + Matryoshka Two-Pass Refiner<br><br>**Action Gating**<br>• `Act automatically`: `1,310/1,310` hidden pass & mean `>= 98.45` (`9` models)<br>• `Confirm`: mean `97.50–98.44` or `<1,310` hidden pass (`8` models)<br>• `Send to a human`: hidden `< 1,260` or Complex `< 96.0` (`2` models) | **Controlled CLI & Bundle Audit**<br>• Fresh UUID session per `(model, task)`<br>• `--no-custom-instructions --disable-builtin-mcps`<br>• Reasoning `effort=medium` (`repeat=1`)<br>• Isolated `_verify/` hidden `pytest` suite (`1,310` assertions)<br>• SHA-256 locked Skyfall JS bundle audit + offline critical-path simulator (`6/6` unit tests passing) | **`Haiku 5.5: 99.24 (#4) · $0.33 · 35.1m`** · **`Gemini 4 Argon: 98.59 (#10) · 1310/1310 · $2.82`** · **`SKY-001 CAD: 79.7% IoU · 3.9s · $0.005`** · **`SKY-001 BIM: 43.6% IoU · 1.22s · $0.0024`**<br><br>1. **`supplement_5_coding_breakthrough` (`choice`)** $\rightarrow$ **`Haiku 5.5` (`99.24 · $0.33`) & `Gemini 4 Argon` (`98.59 · 1310/1310`)** · `Act automatically`<br>   • Haiku 5.5 overall: `99.2%` (`88.6%` cheaper than Sonnet 5.5)<br>   • Gemini 4 Argon overall: `98.6%` (9th 100%-hidden model)<br>2. **`sky_001_world_model_advantage` (`score`)** $\rightarrow$ **`51x–118.5x` faster & `150x–188.4x` cheaper (`+0.6` pt CAD IoU tie vs Astra)** · `Confirm`<br>   • Jaguar E-Type (103 leaves, depth 5): `10,336` flat steps compressed to `105` sequential steps (`98.44x`)<br>3. **`executable_cad_vs_visual_rollout` (`noul`)** $\rightarrow$ **`No` (outputs visual 3D state + 2D sketch rollouts; executable feature history is roadmap)** · `Confirm` |

> **Provenance Callout**: Two complementary engineering paradigms audited from primary artifacts (`anonymized_reported`, `independently_reproduced=false`). In code space with a CLI test loop, lightweight `Haiku 5.5` (`$0.33`) and `Gemini 4 Argon` (`$2.82`, `$0` cache-write) match flagship agents; in 3D geometry space without a visual state-feedback loop, one-shot LLM scripts stall or collapse.

---

## Card 2 (`2 / 7` · `SCENARIO: HAIKU 5.5, GEMINI 4 ARGON & SKY-001 DUAL-SOURCE AUDIT`)

### Haiku 5.5 leaps +5.28 pts to 99.24 ($0.33); Argon hits 1,310/1,310; SKY-001 cuts critical path 98.4x.

> *"Supplement 5 commit a1913835 (2026-10-15, CLI 1.0.98) adds 22 runs for claude-haiku-5.5 and gemini-4-argon while verifying zero score changes across all 17 prior models. Skyfall AI's production JS bundles (index-D5BqB7X_.js & article-D6mnIEDb.js) expose exact CAD/BIM metrics and tree node counts."*

#### 1. `claude_haiku_5_5_deep_dive` · `score` · **Confirm**
- **Question**: `Claude Haiku 5.5` vs `Haiku 4.5` & `Sonnet 5.5` across `A1–C4` (CLI `1.0.98`, `effort=medium`)
- **Result**: **`99.24 / 100` (Rank 4 of 19 · `1,308 / 1,310` hidden · `$0.33` · `94` rounds · `45.3w` out)** · `+5.28` pts overall, `+9.58` pts Complex, and `-91.6%` cost vs `Haiku 4.5` (`$3.93 -> $0.33`); only 2 hidden misses in `C4-microvm` `test_parse_errors`
  - Medium `M1–M2` mean (`99.50 / 100`): `████████████████████` `99.5%`
  - Complex `C1–C4` mean (`99.22 / 100`): `████████████████████` `99.2%`
  - Atomic `A1–A5` mean (`99.15 / 100`): `████████████████████` `99.2%`

#### 2. `gemini_4_argon_deep_dive` · `score` · **Act automatically**
- **Question**: `Gemini 4 Argon` vs `Gemini 3.8 Flash` & `GPT-6.1 Sol` (`1.05M` context, `$0/M` `cache_write`)
- **Result**: **`98.59 / 100` (Rank 10 of 19 · `1,310 / 1,310` hidden · `$2.82` · `106` rounds · `11.7w` out)** · Eliminates all 34 hidden test failures of `Gemini 3.8 Flash`, cuts API rounds by `61.7%` (`277 -> 106`), and reduces wall clock by `47.1%` (`5,122s -> 2,710s`)
  - Hidden test pass rate (`1,310 / 1,310`): `████████████████████` `100.0%`
  - Atomic `A1–A5` mean (`99.00 / 100`): `████████████████████` `99.0%`
  - Complex `C1–C4` mean (`98.06 / 100`): `████████████████████` `98.1%`

#### 3. `sky_001_bundle_discrepancy_audit` · `choice` · **Confirm**
- **Question**: What did cross-auditing Skyfall AI's blog bundle (`article-D6mnIEDb.js`) vs landing bundle (`index-D5BqB7X_.js`) reveal?
- **Result**: **Blog includes `Gemini 4` (`76.9%` CAD IoU, #3); Landing swaps in `Opus 5.5` (`69.4%`) & `Flash` (`54.7%`)** · In BIM (1,000 floor plans), `Gemini 3.8 Flash` (`42.3%` IoU) beats `GPT-6 Astra` (`40.6%` IoU) and trails `SKY-001` (`43.6%`) by just `1.3` pts
  - Jaguar critical-path compression (`105` vs `10,336`): `████████████████████` `99.0%`
  - SKY-001 Composer LLM-judge win rate (`5/5` axes): `████████████████████` `100.0%`
  - Astra Composer asset completion rate (`82%`): `████████████████░░░░` `82.0%`

> **Finding Callout**: `Haiku 5.5` achieves `100.0` on `A1`, `A4`, `M1`, `C2`, `C3` and `99.61` on `C4` — missing `Auto` gating solely due to `2/296` parser error tests in `C4-microvm`. Meanwhile, `Gemini 4 Argon` passes `100%` of hidden tests (`1,310/1,310`) with zero cache-write billing, losing points only on subjective/structural deductions in `A3` (`97.0`), `M2` (`97.25`), `C3` (`96.0`), and `C4` (`98.0`).

---

## Card 3 (`3 / 7` · `WHAT I TESTED`)

### 19 coding models (209 runs) + SKY-001 2,000-case CAD/BIM matrix

| COHORT TIER | MODEL / USAGE PROFILE | BENCHMARK RESULT | ACTION |
|---|---|---|---|
| **Tier 1 · Flagship Ceiling** | `Fable 5.1` (`142` rounds · `55.9m` wall · `$14.45` · `15.8w` out) | **99.77 mean \| Complex 99.62 \| 1310/1310 hidden** (100%) | **Auto** |
| | `Opus 5.5` (`92` rounds · `31.8m` wall · `$5.84` · `17.6w` out) | **99.68 mean \| Complex 99.62 \| 1310/1310 hidden** (100%) | **Auto** |
| | `Opus 5` (`188` rounds · `63.3m` wall · `$17.41` · `24.9w` out) | **99.59 mean \| Complex 99.38 \| 1310/1310 hidden** (100%) | **Auto** |
| **Tier 2 · High-ROI Pareto** | `Haiku 5.5 [NEW]` (`94` rounds · `35.1m` wall · **`$0.33` 2nd lowest cost** · `45.3w` out) | **99.24 mean (#4) \| Complex 99.22 \| 1308/1310 (-2 hidden)** (99%) ✕ | **Confirm** |
| | `Sonnet 5.5` (`65` rounds · **`21.7m` fastest wall** · `$2.89` · `16.1w` out) | **99.00 mean \| Complex 99.19 \| 1310/1310 hidden** (99%) | **Auto** |
| | `GPT-6.1 Sol` (**`60` fewest rounds** · `27.4m` wall · `$1.71` · `9.3w` out) | **98.86 mean \| Complex 99.38 \| 1310/1310 hidden** (99%) | **Auto** |
| | `HydraFusion` (`85` rounds · `24.1m` wall · `$3.58` · `8.9w` out) | **98.45 mean \| Complex 98.75 \| 1310/1310 hidden** (98%) | **Auto** |
| **Tier 3 · High-Score Specialist** | `Grok 4.7` (`143` rounds · `181.2m` wall · `$12.22` · `51.5w` out) | **99.21 mean (#5) \| Complex 99.33 \| 1299/1310 (-11 hidden)** (99%) ✕ | **Confirm** |
| | `GPT-6 Astra` (`62` rounds · `32.7m` wall · `$9.91` · `9.8w` out) | **98.82 mean \| Complex 99.75 (#1) \| 1310/1310 hidden** (99%) | **Auto** |
| | `Sonnet 5` (`190` rounds · `53.2m` wall · `$7.87` · `23.9w` out) | **98.70 mean \| Complex 98.88 \| 1310/1310 hidden** (99%) | **Auto** |
| | `Kimi K3` (`143` rounds · `150.5m` wall · `$5.58` · `17.5w` out) | **98.68 mean \| Complex 98.81 \| 1305/1310 (-5 hidden)** (99%) ✕ | **Confirm** |
| | `Gemini 4 Argon [NEW]` (`106` rounds · `45.2m` wall · `$2.82` · `11.7w` out) | **98.59 mean (#10) \| Complex 98.06 \| 1310/1310 hidden** (99%) | **Auto** |
| | `Grok 4.6` (`138` rounds · `69.5m` wall · `$5.21` · `19.4w` out) | **98.57 mean \| Complex 98.06 \| 1305/1310 (-5 hidden)** (99%) ✕ | **Confirm** |
| **Tier 4 · Low-Cost & Lightweight** | `GPT-6 Luna` (`139` rounds · `44.6m` wall · **`$0.17` lowest cost** · `14.5w` out) | **98.16 mean \| Complex 96.88 \| 1279/1310 (-31 hidden)** (98%) ✕ | **Confirm** |
| | `Gemini 3.8 Flash` (`277` rounds · `85.4m` wall · `$2.83` · `12.3w` out) | **98.00 mean \| Complex 97.00 \| 1276/1310 (-34 hidden)** (98%) ✕ | **Confirm** |
| | `GPT-5.6 Luna` (`235` rounds · `51.0m` wall · `$0.39` · `10.7w` out) | **97.88 mean \| Complex 96.42 \| 1293/1310 (-17 hidden)** (98%) ✕ | **Confirm** |
| | `MAI-Code-1.1-Flash` (`192` rounds · `56.5m` wall · `$0.53` · `23.3w` out) | **97.70 mean \| Complex 96.61 \| 1284/1310 (-26 hidden)** (98%) ✕ | **Confirm** |
| | `DeepSeek-V4-Flash [BYOK]` (`420` rounds · `179.0m` wall · `$1.95` · `29.0w` out) | **95.10 mean \| Complex 95.91 \| 1250/1310 (-60 hidden)** (95%) ✕ | **Human** |
| | `Haiku 4.5` (`341` rounds · `80.8m` wall · `$3.93` · `30.3w` out) | **93.96 mean \| Complex 89.64 \| 1239/1310 (-71 hidden)** (94%) ✕ | **Human** |
| **Track B · SKY-001 CAD** | `SKY-001` vs `GPT-6 Astra` (`1,000` parts · `3.9s / $0.005` vs `199s / $0.75`) | **79.7% vs 79.1% IoU (+0.6 pt tie; 51.0x faster, 150.0x cheaper)** (80%) | **Confirm** |
| **Track B · SKY-001 BIM** | `SKY-001` vs `Gemini 3.8 Flash` & `Astra` (`1,000` plans · `1.22s / $0.0024`) | **43.6% vs 42.3% Flash & 40.6% Astra (118.5x faster, 185.8x cheaper)** (44%) ✕ | **Confirm** |

> **Threshold Callout**: **9 of 19 coding models pass all `1,310 / 1,310` hidden assertions and clear the `Auto` bar (`>= 98.45` mean)**: `Fable 5.1`, `Opus 5.5`, `Opus 5`, `Sonnet 5.5`, `GPT-6.1 Sol`, `GPT-6 Astra`, `Sonnet 5`, **`Gemini 4 Argon [NEW]`**, and `HydraFusion`.
>
> **Near-Miss Champion Callout (`✕`)**: **`Claude Haiku 5.5` ranks #4 overall (`99.24`) at `$0.33` with `1,308 / 1,310` hidden pass** — outscoring `Sonnet 5.5` (`99.00`) and `GPT-6.1 Sol` (`98.86`) at `1/9th` to `1/5th` the cost, requiring only a standard unit/parser assertion gate on `C4` to run automatically.

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`)

### Copilot CLI 70/15/15 verifier vs SKY-001 Two-Pass World Model

```json
{
  "track_A_copilot_cli_supplement_5": {
    "commit": "a191383571a13143685fd6f7787512c4e281a9ba",
    "cli_version": "1.0.98",
    "haiku_5_5_C4_microvm": {
      "wall_s": 278.8,
      "api_s": 250.5,
      "rounds": 14,
      "ai_credits": 5.13,
      "hidden_tests": "294/296 (2 test_parse_errors misses -> 69.61/70)",
      "total_score": 99.61
    },
    "gemini_4_argon_C3_microdb": {
      "wall_s": 1007.4,
      "api_s": 983.9,
      "rounds": 29,
      "ai_credits": 98.58,
      "cache_write_price_per_m": 0.0,
      "hidden_tests": "377/377 (58/58 + 12/12 self_test = 70/70)",
      "total_score": 96.0
    }
  }
}
```

`↓ vs SKY-001 Hierarchical Part Tree + Matryoshka Two-Pass Construction Rollout (S=100 steps/part, W=128 workers)`

```xml
<sky_001_execution_graph steps_per_part="100" parallel_workers="128">
  Stage 1 (Hierarchical Composer): Coarse 3D DiT -> Parallel Tree Split (depth D) -> Leaf Refiner DiT
    Jaguar E-Type: L=103 leaves, N=139 nodes (36 splits), D=5
    Flat chain:   (N - L) + L * S = 36 + 103 * 100 = 10,336 sequential steps
    Tree rollout: D + ceil(L / W) * S = 5 + 1 * 100 = 105 sequential steps (98.44x shorter!)
  Stage 2 (Construction World Model):
    Pass 1: Roll out intermediate 3D solid states + 2D inverse sketches in leading Matryoshka latents
    Pass 2: Parallel full-resolution Refiner restores sharp edges, corners & vertices
</sky_001_execution_graph>
<answer>
```

> **Protocol Callout**: Why did `Haiku 5.5` emit `453,116` output tokens for only `$0.33` while `Gemini 4 Argon` cost `$2.82` for `116,755` output tokens? In `C3-microdb`, `Haiku 5.5` generated `263,769` output tokens across 24 rounds, but its CAPI rates (`$0.50/M` output, `$0.01/M` cache read) billed just `16.93` credits (`$0.17`). `Argon` bills `$2.00/M` input, `$0.10/M` cache read, **`$0.00/M` cache write**, and `$10.00/M` output (`98.58` credits on `C3`).

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`)

### Generational leaps & cross-modality sensitivity (Code vs 3D CAD)

Comparing Supplement 5 models against their predecessors on the 11-task CLI suite, and contrasting 6 frontier families across multi-turn CLI coding vs Skyfall's one-shot 3D CAD scripting benchmark:

| QUESTION / ANSWER | ORIGINAL | REVERSED / EVOLVED | CHANGE (PTS) |
|---|---:|---:|---:|
| **`Haiku 5.5` · Generational Leap vs `Haiku 4.5` (11-Task Mean & Complex)**<br>Complex mean `89.64% -> 99.22%` (`+9.58` pts); Hidden `1239 -> 1308/1310`; Cost `$3.93 -> $0.33` (`-91.6%`) | `94.0%` | `99.2%` | `+5.2` |
| **`Gemini 4 Argon` · Generational Leap vs `Gemini 3.8 Flash` (11-Task Mean)**<br>Hidden assertions `1276/1310` (`97.4%`) $\rightarrow$ `1310/1310` (`100.0%`); Rounds `277 -> 106` (`-61.7%`) | `98.0%` | `98.6%` | `+0.6` |
| **`Grok 4.7` · Modality Shift: One-Shot CAD Script vs Multi-Turn CLI Agent**<br>SKY-001 CAD benchmark: `0.0%` IoU (`null` output at `1,250s`) $\rightarrow$ Copilot CLI: `99.21%` (`#5` of 19) | `0.0%` | `99.2%` | `+99.2` |
| **`Kimi K3` · Modality Shift: One-Shot CAD Script vs Multi-Turn CLI Agent**<br>SKY-001 CAD benchmark: `9.5%` IoU (`439s`, `$0.13`) $\rightarrow$ Copilot CLI: `98.68%` (`1,305/1,310` hidden) | `9.5%` | `98.7%` | `+89.2` |
| **`GPT-6 Astra` · Modality Shift: One-Shot CAD Script vs Multi-Turn CLI Agent**<br>SKY-001 CAD: `79.1%` IoU (`-0.6` pt vs SKY-001) $\rightarrow$ Copilot CLI: `98.82%` (Complex `#1` at `99.75%`) | `79.1%` | `98.8%` | `+19.7` |
| **`Opus 5.5` · Modality Shift: One-Shot CAD Script vs Multi-Turn CLI Agent**<br>SKY-001 CAD landing: `69.4%` IoU (omitted in blog) $\rightarrow$ Copilot CLI: `99.68%` (`#2` overall, `1310/1310`) | `69.4%` | `99.7%` | `+30.3` |
| **`Gemini 4 / Argon` · Modality Shift: One-Shot CAD vs Multi-Turn CLI Agent**<br>SKY-001 CAD blog: `76.9%` IoU (omitted on landing page) $\rightarrow$ Copilot CLI: `98.59%` (`1310/1310` hidden) | `76.9%` | `98.6%` | `+21.7` |

> **Robustness Callout**: The dramatic inversion of `Grok 4.7` (`0% -> 99.21%`) and `Kimi K3` (`9.5% -> 98.68%`) proves that **general LLMs fail on 3D CAD not because they cannot write code, but because Skyfall's baseline forced them to emit a 100-step 3D script in a single blind request without spatial state feedback**. Paired with an iterative CLI test/compiler loop, the exact same models exceed `98.6%`.

---

## Card 6 (`6 / 7` · `LATENCY`)

### 11-task API inference vs wall time across top 8 models (seconds)

Blue bars (`Batched` slot in HTML) represent pure API model inference time (`task_inference_seconds`); gray bars (`One by one*` slot) represent end-to-end wall-clock time (`task_wall_seconds`, including local shell/`pytest` execution) across all 11 tasks.

| Model Cohort (`11` tasks, `repeat=1`) | Pure API Inference Time | Total Wall Clock Time | Non-Inference Tool/IO Overhead | Rounds | Cost |
|---|---:|---:|---:|---:|---:|
| **1. `Sonnet 5.5`** (`99.00` pts) | **`995 s` (`16.6m`)** | **`1,301 s` (`21.7m`)** | `306 s` (`23.5%`) | `65` | `$2.89` |
| **2. `HydraFusion`** (`98.45` pts) | **`1,034 s` (`17.2m`)** | **`1,444 s` (`24.1m`)** | `410 s` (`28.4%`) | `85` | `$3.58` |
| **3. `GPT-6.1 Sol`** (`98.86` pts) | **`1,348 s` (`22.5m`)** | **`1,645 s` (`27.4m`)** | `297 s` (`18.1%`) | `60` | `$1.71` |
| **4. `Opus 5.5`** (`99.68` pts) | **`1,570 s` (`26.2m`)** | **`1,909 s` (`31.8m`)** | `339 s` (`17.8%`) | `92` | `$5.84` |
| **5. `GPT-6 Astra`** (`98.82` pts) | **`1,617 s` (`27.0m`)** | **`1,960 s` (`32.7m`)** | `343 s` (`17.5%`) | `62` | `$9.91` |
| **6. `Haiku 5.5 [NEW]`** (`99.24` pts) | **`1,852 s` (`30.9m`)** | **`2,104 s` (`35.1m`)** | `252 s` (`12.0%`) | `94` | `$0.33` |
| **7. `Gemini 4 Argon [NEW]`** (`98.59` pts) | **`2,512 s` (`41.9m`)** | **`2,710 s` (`45.2m`)** | `198 s` (`7.3%`) | `106` | `$2.82` |
| **8. `Fable 5.1`** (`99.77` pts) | **`2,210 s` (`36.8m`)** | **`3,355 s` (`55.9m`)** | `1,145 s` (`34.1%`) | `142` | `$14.45` |

> **Latency Callout**: `Haiku 5.5` is the **fastest model of all 19 on Atomic tasks (`A1–A5`: `141.5s` total = `28.3s/task`)**; `53.0%` (`1,116s`) of its 11-task wall time was spent in a single task (`C3-microdb`, where it emitted `263,769` output tokens). Meanwhile, in 3D CAD, `SKY-001` finishes a 100-step part in **`3.9s` vs `Astra`'s `199s` (`51.0x` faster)** and a BIM floor plan in **`1.22s` vs `144.6s` (`118.5x` faster)**.

---

## Card 7 (`7 / 7` · `MY TAKE`)

### Where Haiku 5.5, Gemini 4 Argon & SKY-001 fit in production

| ✅ Good fit | ⛔ Not for |
|---|---|
| • **`Claude Haiku 5.5` (`$0.33`, `99.24` pts)**: Default high-throughput Coding Agent for atomic/medium engineering tasks and CI auto-repair backed by a unit-test gate<br>• **`Gemini 4 Argon` (`$2.82`, `1,310/1,310` hidden)**: Long-context (`1.05M`) multi-file refactoring where `$0/M` `cache_write` slashes prompt-warmed cost<br>• **`Sonnet 5.5` (`$2.89`, `21.7m`) & `GPT-6.1 Sol` (`$1.71`, `60` rds)**: Primary unattended daily drivers clearing `1,310/1,310` hidden tests<br>• **`SKY-001` World Model Architecture**: Coarse-to-fine 3D concept exploration, hierarchical assembly decomposition, and visual construction planning | • **Treating `SKY-001`'s current visual state+sketch rollouts as manufacturing-ready parametric B-Rep/STEP feature histories** (explicitly listed as future roadmap by Skyfall AI)<br>• **Benchmarking general LLMs on 3D CAD via single-request blind scripts** without a geometric solver or visual feedback loop<br>• **Running `Haiku 5.5` unguarded on complex parser/VM edge cases** without unit-test assertions (`2/296` misses on `C4-microvm`)<br>• **Over-interpreting `< 1.0` pt single-run (`repeat=1`) rank gaps** across CLI versions `1.0.84-3..1.0.98` |

> **Readiness & Provenance**
> - **Provenance**: `anonymized_reported` (`independently_reproduced=false`) + Offline Verifier Suite (`simulator/sky001_and_19model_verifier.py`, `6/6` unit tests passing).
> - **Sources**: [`satomic/copilot-benchmark@a1913835`](https://github.com/satomic/copilot-benchmark/commit/a191383571a13143685fd6f7787512c4e281a9ba) · `skyfall.ai/assets/index-D5BqB7X_.js` · `skyfall.ai/assets/article-D6mnIEDb.js` · `benchmark-harness-engineering` 7-Card Visual Deck v1.
