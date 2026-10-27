# 8-Way Model Routing Benchmark Test Report — OpenAI Decisions vs Microsoft Decision-1 (`Switchyard v2.4.0 & v2.4.1`)

> **Format**: 7-Card 4:5 Visual Report (`900x1125` / `1080x1350` portrait cards)
> **Interactive / Print Deck**: [`test-report-cards.html`](test-report-cards.html) · **Structured Data**: [`report.json`](report.json) · **Primary Evidence**: [`evidence.json`](evidence.json)
> **Provenance**: `anonymized_reported` (`independently_reproduced=false`) · **Public Router**: [`satomic/model-router`](https://github.com/satomic/model-router) (`v2.3.0` `b58bfd31`, `v2.4.0` `3408c39c`, `v2.4.1` `8a20a7b6`)

---

## Card 1 (`1 / 7` · `HANDS-ON · 8-WAY MODEL ROUTING BENCHMARK (V2.4.0 & V2.4.1)`)

### OpenAI Decisions joins the 8-way routing test — **Microsoft Decision-1 remains #1**

Across `960` decisions under cost-biased instructions (`v2.4.0`) and `2,760` decisions across 4 instruction variants (`v2.4.1`) on `40` bilingual prompts (`20` EN / `20` ZH, `5` target models), **`Microsoft Decision-1` hits `37.7 / 40` (`94.2%`) → `40 / 40` (`100.0%` neutral) at `$7.6–$8.6 / 1M` decisions**, outperforming **`OpenAI Decisions` (`32 / 40` = `80.0%` → `37 / 40` = `92.5%` neutral at `$26.1–$28.4 / 1M`)** in accuracy, instruction robustness, probability calibration, and cost.

#### Workbench Preview (`Switchyard v2.4.0 & v2.4.1 · 8 Routing Approaches × 40 Bilingual Prompts`)

| Left Column · Scenarios, Cohorts & Gating | Center Column · Protocol & Instruction Variants | Right Column · Headline Metrics & Decisions |
|---|---|---|
| **Prompt Suites (`40` Single-Turn Prompts, `3` Rounds Each)**<br>• **Set A (`20` explicit: `10` EN + `10` ZH)**: Clear task cues matching catalog descriptions<br>• **Set B (`20` implicit: `10` EN + `10` ZH)**: Short or borderline phrasing whose surface length belies actual complexity<br><br>**5 Candidate Backend Models**<br>• `gpt-4.1-mini`: Greetings, chit-chat, trivial one-line Q&A, simple translation<br>• `gpt-4o`: Summaries, rewriting, format conversion, everyday answers<br>• `gpt-4.1`: Everyday programming, code explanation, moderate debugging<br>• `gpt-5.4`: Hard algorithms, mathematical proofs, complex system design<br>• `gpt-6-luna`: Creative long-form writing (stories, poems, marketing copy)<br><br>**Confidence Gate (`τ = 0.60`)**<br>• `Act automatically`: `p >= 0.60` & 4-variant spread `<= 2/40` (`Jev`, `Decision-1`)<br>• `Confirm`: `p < 0.60` fallback or moderate sensitivity (`OpenAI`, `OpenJev`, `LLM mini/luna-none`)<br>• `Send to a human`: high-confidence wrong picks or CoT flips (`luna-default`, `Laya`) | **4 Instruction Variants Tested in `v2.4.1` (`2,760` Decisions)**<br>• **`neutral` (`v2.4.1` default)**: *"Which backend model should handle this request? Pick the option whose description best matches what the request needs."*<br>• **`cheap` (`v2.4.0` default)**: `neutral` + *"Prefer a cheaper, faster model when the request is simple, and a stronger model only when the request needs it."*<br>• **`strong`**: `neutral` + *"When in doubt, prefer the stronger, more capable model rather than risking a weak answer."*<br>• **`bare`**: *"Pick the backend model for this request."* | **`Decision-1: 94.2%→100% · $7.6–$8.6/1M · 541–597ms`** · **`TypeSafe Jev: 98.3%→100% · $21.7–$24.1/1M · 326–350ms`** · **`OpenAI Decisions: 80.0%→92.5% · $26.1–$28.4/1M · 369–417ms`** · **`OpenJev 27B 4-bit: 92.5%→100% · $0 API · 2.28–2.57s`**<br><br>1. **`production_cloud_router` (`choice`)** → **`Microsoft Decision-1` (`100%` neutral / `94.2%` cheap · `$7.6–$8.6/1M`)** · `Act automatically`<br>   • TypeSafe Jev (`98.3%` cheap / `100%` neutral): `98.3%`<br>   • Microsoft Decision-1 (`94.2%` cheap / `100%` neutral): `94.2%`<br>   • OpenAI Decisions (`80.0%` cheap / `92.5%` neutral): `80.0%`<br>2. **`instruction_robustness_4variants` (`score`)** → **`Jev 97.5%` (`39/40`) · `Decision-1 95.0%` (`38/40`) · `OpenAI 80.0%` (`32/40`)** · `Act automatically`<br>   • Spread across `neutral/cheap/strong/bare`: `Jev` `1` pt, `Decision-1` `2` pts, `OpenJev` `4` pts, `OpenAI` `6` pts<br>3. **`confidence_gate_060_reliability` (`noul`)** → **`Yes` for `Jev` (`3/3` caught) & `Decision-1` (`0` misses outside cheap); `No` for `OpenAI` (`24/48 >= 0.60`)** · `Confirm` |

> **Finding Callout**: Removing the single cost-saving sentence (*"Prefer a cheaper, faster model when the request is simple..."*) raises `TypeSafe Jev` (`39.3 → 40/40`), `Microsoft Decision-1` (`37.7 → 40/40`), and `OpenJev 27B` (`37.0 → 40/40`) to **`100.0%` accuracy**, and lifts `OpenAI Decisions` from `32/40` (`80.0%`) to `37/40` (`92.5%`). Even under neutral instructions, `Decision-1` is more accurate (`100%` vs `92.5%`) and `3.4x` cheaper (`$7.6` vs `$26.1 / 1M`).

---

## Card 2 (`2 / 7` · `SCENARIO: IMPLICIT BORDERLINE PROMPTS (B14, B8, B9)`)

### Why OpenAI Decisions misses 8 prompts in v2.4.0 and 3 in v2.4.1 neutral

> *"B14 (ZH, want gpt-4o): '一句话总结这个 PR：把日志从 logrus 换成了 slog，删除了 3 个废弃接口，并更新了 README。' | B8 (EN, want gpt-5.4): 'What is the expected number of fair coin flips until the sequence HTHT first appears? Show your work.' | B9 (EN, want gpt-6-luna): 'Give me a fun, rhyming toast for my sister's wedding.'"*

#### 1. `case_B14_pr_one_line_summary` · `choice` · **Confirm**
- **Question**: `B14`: Summarize PR in one sentence (expected: `gpt-4o` for summaries; surface contains *"一句话"* matching `gpt-4.1-mini`'s *"trivial one-line questions"*)
- **Result**: **`v2.4.1 neutral`: `Jev` `gpt-4o` (`0.93`) · `Decision-1` `gpt-4o` (`0.61`) · `OpenAI` `gpt-4.1-mini` (`0.53`)** · Under `v2.4.0 cheap`, only `Jev` (`0.76`) and `gpt-4.1-mini` got `B14` right; removing cost bias unlocks `Decision-1` (`0.61`), `OpenJev` (`0.52`), and `luna-none`
  - TypeSafe Jev → `gpt-4o` (`0.76` cheap / `0.93` neutral): `███████████████████░` `93.0%`
  - Microsoft Decision-1 → `gpt-4o` (`0.45` cheap / `0.61` neutral): `████████████░░░░░░░░` `61.0%`
  - OpenAI Decisions → `gpt-4.1-mini` (`0.60` cheap / `0.53` neutral / `0.75` strong): `███████████░░░░░░░░░` `53.0%`

#### 2. `case_B8_htht_coin_flip_markov` · `choice` · **Act automatically**
- **Question**: `B8`: Expected coin flips until `HTHT` first appears (expected: `gpt-5.4` Markov chain / renewal equation, `E = 20`)
- **Result**: **`v2.4.1 neutral`: `Jev` `gpt-5.4` (`1.00`) · `Decision-1` `gpt-5.4` (`0.996`) · `OpenAI` `gpt-4.1-mini` (`0.38`)** · `OpenAI Decisions` routes `B8` to `gpt-4.1-mini` under `neutral` (`0.38`), `cheap` (`0.34`), and `strong` (`0.45`), only picking `gpt-5.4` (`0.57`) under the 7-word `bare` instruction
  - TypeSafe Jev → `gpt-5.4` (`p = 1.000` neutral): `████████████████████` `100.0%`
  - Microsoft Decision-1 → `gpt-5.4` (`p = 0.996` neutral): `████████████████████` `99.6%`
  - OpenAI Decisions → `gpt-4.1-mini` (`p = 0.38` neutral / `0.34` cheap): `████████░░░░░░░░░░░░` `38.0%`

#### 3. `case_B9_rhyming_wedding_toast` · `choice` · **Send to a human**
- **Question**: `B9`: Fun, rhyming toast for sister's wedding (expected: `gpt-6-luna` creative writing)
- **Result**: **`v2.4.1 neutral`: `Jev` `gpt-6-luna` (`0.99`) · `Decision-1` `gpt-6-luna` (`0.972`) · `OpenAI` `gpt-4.1-mini` (`0.66`)** · `OpenAI Decisions` routes `B9` to `gpt-4.1-mini` across all 4 variants with `p = 0.65` (`cheap`), `0.66` (`neutral`), `0.70` (`strong`), and `0.78` (`bare`) — bypassing a `0.60` confidence gate
  - TypeSafe Jev → `gpt-6-luna` (`p = 0.990` neutral): `████████████████████` `99.0%`
  - Microsoft Decision-1 → `gpt-6-luna` (`p = 0.972` neutral): `███████████████████░` `97.2%`
  - OpenAI Decisions → `gpt-4.1-mini` (`p = 0.66` neutral / `0.78` bare): `█████████████░░░░░░░` `66.0%`

> **Finding Callout**: Across all `480` decisions in `v2.4.1`, **100% of `OpenAI Decisions`' 48 wrong picks landed on `gpt-4.1-mini`** (`33/48` downgraded from stronger tiers + `15/48` routed sideways from creative `gpt-6-luna` to `gpt-4.1-mini`). On `B9` and `B14`, `OpenAI Decisions` never selected the target model under any of the 4 instruction variants.

---

## Card 3 (`3 / 7` · `WHAT I TESTED`)

### 8 routing approaches across v2.4.0 (cost-biased) & v2.4.1 (neutral): full scorecard

| PROTOCOL FAMILY | ENGINE / LATENCY / COST | ACCURACY (`V2.4.0 CHEAP` → `V2.4.1 NEUTRAL`) | ACTION |
|---|---|---|---|
| **1. Cloud System One API** | `TypeSafe Jev` (`jev-latest` · P50 `326–350ms` · P95 `643–720ms` · `$21.7–$24.1/1M`) | **v2.4.0: 39.3/40 (98.3%) → v2.4.1 neutral: 40/40 (100%) \| 40/40 stable** (100%) | **Auto** |
| | `Microsoft Decision-1` (`Foundry East US 2` · P50 `541–597ms` · P95 `1.25–1.34s` · `$7.6–$8.6/1M`) | **v2.4.0: 37.7/40 (94.2%) → v2.4.1 neutral: 40/40 (100%) \| 40/40 stable** (100%) | **Auto** |
| **2. OpenAI Native API** | `OpenAI Decisions` (`/v1/decisions` `gpt-6-luna` · P50 `369–417ms` · P95 `759–804ms` · `$26.1–$28.4/1M`) | **v2.4.0: 32.0/40 (80.0%) → v2.4.1 neutral: 37.0/40 (92.5%) \| 40/40 stable (-3 B-set)** (93%) ✕ | **Confirm** |
| **3. Local Open-Weight (`M4 Pro`)** | `OpenJev 27B` (`MLX 4-bit 15.6GB` · P50 `2,276–2,566ms` · P95 `2,597–3,030ms` · `$0 API` · `CC BY-NC 4.0`) | **v2.4.0: 37.0/40 (92.5%) → v2.4.1 neutral: 40/40 (100%) \| 40/40 stable** (100%) | **Confirm** |
| | `Self-hosted Laya 0.3.20` (`196MB` · P50 `111–127ms` · P95 `143–491ms` · `$0 API` · `Apache-2.0`) | **v2.4.0: 20.0/40 (50.0%) → v2.4.1 neutral: 19.0/40 (47.5%) \| 40/40 stable (-21 misses)** (48%) ✕ | **Human** |
| **4. General LLM Prompt Router** | `LLM: gpt-6-luna reasoning='none'` (`Foundry` · P50 `1,714–1,739ms` · P95 `2.58–2.73s` · `$39.8/1M`) | **v2.4.0: 35.3/40 (88.3%, 1 err) → v2.4.1 neutral: 36.3/40 (90.8%) \| 36/40 stable** (91%) ✕ | **Confirm** |
| | `LLM: gpt-4.1-mini` (`Foundry` · P50 `1,427–1,608ms` · P95 `2,090–2,510ms` · `$141.4–$141.8/1M`) | **v2.4.0: 36.0/40 (90.0%) → v2.4.1 neutral: 36.0/40 (90.0%) \| 40/40 stable (-4 over-escalated)** (90%) ✕ | **Confirm** |
| | `LLM: gpt-6-luna default reasoning` (`Foundry` · P50 `2,079–2,132ms` · P95 `3.05–3.54s` · `$62.4–$63.1/1M`) | **v2.4.0: 30.3/40 (75.8%, 27/40 stable) → v2.4.1 neutral: 29.0/40 (72.5%, 29/40 stable, 1 err)** (73%) ✕ | **Human** |

> **Threshold Callout**: **3 System One engines (`TypeSafe Jev`, `Microsoft Decision-1`, `OpenJev 27B`) hit `40 / 40` (`100.0%`) under `v2.4.1` neutral instructions**. `Decision-1` achieves the same `40/40` accuracy as `Jev` at `1/3` the cost (`$7.6` vs `$24.1 / 1M`) because it bills only `1` completion token (`~180` input + `1` output at `$0.042/1M`), whereas `Jev` bills `~82` internal reasoning tokens.
>
> **Misses Callout (`✕`)**: **5 approaches still miss `3` to `21` prompts under neutral instructions** — and **chain-of-thought reasoning actively harms LLM routing**: enabling default reasoning on `gpt-6-luna` drops accuracy from `90.8%` (`luna-none`) to `72.5%` (`luna-default`) and causes `11–13 / 40` prompts to flip across rounds. Meanwhile, `gpt-4.1-mini` is the only engine whose errors (`4/40`: `A2`, `B1`, `B11`, `B12`) all **over-escalate** to stronger models.

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`)

### OpenAI `/v1/decisions` vs Microsoft & TypeSafe `/v1/systemone` wire protocol

```json
// 1. OpenAI Decisions API: POST https://api.openai.com/v1/decisions
// Model fixed to "gpt-6-luna"; 2-decimal probabilities; 0 completion_tokens ($0.10/1M in)
{
  "model": "gpt-6-luna",
  "input": "What is the expected number of fair coin flips until HTHT first appears?",
  "questions": [{
    "type": "choice", "name": "model",
    "instructions": "Which backend model should handle this request? Pick the option whose description best matches...",
    "choices": [{"value": "gpt-4.1-mini", "description": "Cheapest and fastest..."}, {"value": "gpt-5.4", "description": "Strongest reasoning..."}]
  }]
}
// -> {"answers": [{"name": "model", "choice": "gpt-4.1-mini", "probabilities": [{"value": "gpt-4.1-mini", "probability": 0.38}, ...]}]}
```

`↓ Switchyard (satomic/model-router v2.4.0 / v2.4.1) protocol adapter + confidence threshold gate (tau = 0.60) ↓`

```json
// 2. System One API: POST https://<resource>.services.ai.azure.com/providers/microsoft/v1/systemone
// Full float64 probabilities; Decision-1 bills ~180 prompt + 1 completion token ($7.6/1M at $0.042/1M)
{
  "model": "msft-decision-1",
  "state": {"user_request": "What is the expected number of fair coin flips until HTHT first appears?"},
  "questions": {
    "model": {
      "type": "choice",
      "instructions": "Which backend model should handle `user_request`? Pick the option whose description best matches...",
      "criteria": {"gpt-4.1-mini": "Cheapest and fastest...", "gpt-5.4": "Strongest reasoning..."}
    }
  }
}
// -> {"answers": {"model": {"choice": "gpt-5.4", "probabilities": {"gpt-5.4": 0.9961, ...}}}, "usage": {"prompt_tokens": 180, "completion_tokens": 1}}
<answer>
```

> **Protocol Callout**: `Switchyard v2.4.0` also uncovered and fixed a silent fallback bug for OpenAI reasoning models (`gpt-6-luna`) on Chat Completions: `gpt-6-luna` rejects requests that pass legacy `max_tokens` or `temperature` when reasoning is active (`HTTP 400`). Earlier router versions caught the exception and silently fell back to default `gpt-4.1-mini` (recording `0 ms`); `v2.4.0` switches to `max_completion_tokens` and adds `ai_router.decision_reasoning_effort` (`"none"` vs default).

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`)

### Instruction sensitivity & 0.60 confidence gate across 2,760 calls (v2.4.1)

Comparing cost-biased (`cheap`, `v2.4.0` default) vs neutral (`neutral`, `v2.4.1` default) accuracy, plus the 4-variant spread (`neutral` / `cheap` / `strong` / `bare`, `480` decisions per dedicated engine).

| ENGINE / 4-VARIANT PROFILE | CHEAP (`V2.4.0`) | NEUTRAL (`V2.4.1`) | GAIN (PTS) |
|---|---:|---:|---:|
| **TypeSafe Jev (`jev-latest`) · 4-Variant Spread: `1/40` (`39..40/40`)**<br>`neutral 40/40 · cheap 39/40 · strong 40/40 · bare 40/40 \| 0/3 wrong >=0.60 (max 0.45), 0/477 false blocks` | `97.5%` | `100.0%` | `+2.5` |
| **Microsoft Decision-1 (`Foundry`) · 4-Variant Spread: `2/40` (`38..40/40`)**<br>`neutral 40/40 · cheap 38/40 · strong 40/40 · bare 39/40 \| 3/9 wrong >=0.60 (only cheap, max 0.642), 11/471 false blocks` | `95.0%` | `100.0%` | `+5.0` |
| **OpenJev 27B (`MLX 4-bit Local`) · 4-Variant Spread: `4/40` (`36..40/40`)**<br>`neutral 40/40 · cheap 36/40 · strong 39/40 · bare 39/40 \| 6/18 wrong >=0.60 (max 0.751), 9/462 false blocks` | `90.0%` | `100.0%` | `+10.0` |
| **OpenAI Decisions (`gpt-6-luna`) · 4-Variant Spread: `6/40` (`32..38/40`)**<br>`neutral 37/40 · cheap 32/40 · strong 37/40 · bare 38/40 \| 24/48 wrong >=0.60 (max 0.78), 27/432 false blocks` | `80.0%` | `92.5%` | `+12.5` |
| **LLM Router: `gpt-6-luna` (`reasoning='none'`) · Cheap vs Neutral**<br>`v2.4.0 cheap 35.33/40 (88.3%, 37/40 stable) → v2.4.1 neutral 36.33/40 (90.8%, 36/40 stable)` | `88.3%` | `90.8%` | `+2.5` |
| **LLM Router: `gpt-4.1-mini` · Cheap vs Neutral (Identical 4 Over-Escalations)**<br>`v2.4.0 cheap 36/40 (90.0%) → v2.4.1 neutral 36/40 (90.0%) \| Misses A2, B1, B11, B12 (all stronger)` | `90.0%` | `90.0%` | `0.0` |
| **Self-hosted Laya `0.3.20` · 4-Variant Spread: `2/40` (`19..21/40`)**<br>`neutral 19/40 · cheap 21/40 · strong 20/40 · bare 21/40 \| 24/237 wrong >=0.60 (max 0.911), 192/243 false blocks` | `52.5%` | `47.5%` | `-5.0` |

> **Robustness Callout**: **Asymmetric instruction response**: *"Prefer cheaper"* hurts every dedicated engine (`-2.5` to `-12.5` pts), while *"Prefer stronger"* never causes over-escalation. Across all `480` calls per engine in `v2.4.1`, **100% of errors in `Jev` (`3/3`), `Decision-1` (`9/9`), `OpenJev` (`18/18`), and `OpenAI Decisions` (`48/48`: `33` cheaper + `15` sideways to `gpt-4.1-mini`) erred toward cheaper models** — zero errors ever picked a stronger model than needed.

---

## Card 6 (`6 / 7` · `LATENCY`)

### End-to-end decision latency: P50 vs P95 across all 8 engines (v2.4.1 neutral)

Measured from Mainland China client to cloud APIs (`OpenAI 1P`, `Azure AI Foundry East US 2`, `TypeSafe Cloud`) and local `Apple M4 Pro 48GB` (`OpenJev 27B MLX 4-bit`, `Laya 0.3.20`).

| ENGINE / TIER | P50 MEDIAN (`v2.4.1` / `v2.4.0`) | P95 TAIL (`v2.4.1` / `v2.4.0`) |PAIRED BARS (`v2.4.1` P50 vs P95) |
|---|---:|---:|---|
| **1. Self-hosted Laya 0.3.20** (`47.5%` acc · `$0 API`) | **`111 ms`** (`127 ms`) | **`491 ms`** (`143 ms`) | `█` `111 ms` / `███` `491 ms` |
| **2. TypeSafe Jev Cloud** (`100%` neutral / `98.3%` cheap · `$24.1/1M`) | **`326 ms`** (`350 ms`) | **`643 ms`** (`720 ms`) | `██` `326 ms` / `████` `643 ms` |
| **3. OpenAI Decisions Cloud** (`92.5%` neutral / `80.0%` cheap · `$26.1/1M`) | **`417 ms`** (`369 ms`) | **`804 ms`** (`759 ms`) | `███` `417 ms` / `█████` `804 ms` |
| **4. Microsoft Decision-1 Cloud** (`100%` neutral / `94.2%` cheap · `$7.6/1M`) | **`597 ms`** (`541 ms`) | **`1,344 ms`** (`1,251 ms`) | `████` `597 ms` / `████████` `1,344 ms` |
| **5. LLM Router: `gpt-4.1-mini`** (`90.0%` acc · `$141.4/1M`) | **`1,608 ms`** (`1,427 ms`) | **`2,510 ms`** (`2,090 ms`) | `█████████` `1,608 ms` / `██████████████` `2,510 ms` |
| **6. LLM Router: `gpt-6-luna` `reasoning='none'`** (`90.8%` acc · `$39.8/1M`) | **`1,739 ms`** (`1,714 ms`) | **`2,731 ms`** (`2,578 ms`) | `██████████` `1,739 ms` / `███████████████` `2,731 ms` |
| **7. LLM Router: `gpt-6-luna` default reasoning** (`72.5%` acc · `$63.1/1M`) | **`2,079 ms`** (`2,132 ms`) | **`3,538 ms`** (`3,045 ms`) | `████████████` `2,079 ms` / `████████████████████` `3,538 ms` |
| **8. OpenJev 27B Local (`M4 Pro 48GB MLX 4-bit`)** (`100%` neutral · `$0 API`) | **`2,276 ms`** (`2,566 ms`) | **`2,597 ms`** (`3,030 ms`) | `█████████████` `2,276 ms` / `███████████████` `2,597 ms` |

> **Latency Callout**: All 3 dedicated cloud decision APIs respond in **`326–597 ms` P50** — **3x to 5x faster** than Chat Completions LLM routing (`1,427–2,132 ms`). `Microsoft Decision-1` bills only `1` completion token (`~180` input + `1` output = `$7.6/1M`), whereas `TypeSafe Jev` bills `~82` internal reasoning tokens (`$24.1/1M`).

---

## Card 7 (`7 / 7` · `MY TAKE`)

### Why Microsoft Decision-1 stays the #1 production choice after OpenAI Decisions joins

| ✅ Good fit | ⛔ Not for |
|---|---|
| • **`Microsoft Decision-1` as default cloud router on Azure AI Foundry**: `100%` neutral accuracy (`94.2%` cheap), `$7.6–$8.6 / 1M` cost (`3.3x` cheaper than `OpenAI Decisions`, `16x` cheaper than `gpt-4.1-mini`), `~550 ms` P50, and clean `0.60` threshold gating.<br>• **`TypeSafe Jev` when maximum instruction immunity (`39..40/40` across all 4 variants, `0` false blocks at `0.60`) and lowest cloud latency (`~330 ms` P50)** justify `~3x` `Decision-1`'s price (`$21.7–$24.1 / 1M`).<br>• **Neutral routing instructions (*"Pick the option whose description best matches..."*)** while encoding tier boundaries inside candidate descriptions (`+12.5%` on `OpenAI Decisions`, `+5.8%` on `Decision-1`).<br>• **`OpenAI Decisions` for teams already on an OpenAI 1P key** needing a fast (`~400 ms` P50) drop-in endpoint under neutral/bare instructions (`92.5%–95.0%`).<br>• **Setting `reasoning_effort='none'` whenever using a reasoning LLM (`gpt-6-luna`) as a prompt-based router** (`+15.0` to `+18.3` pts accuracy, `-400 ms` latency, `-37%` cost vs default reasoning). | • **Combining `OpenAI Decisions` with cost-saving prompt instructions (*"prefer cheaper when simple"*)**: accuracy drops to `80.0%` (`32/40`) and `14/20` (`70%`) on implicit Set B requests.<br>• **Relying on a `0.60` confidence gate with `OpenAI Decisions`**: `50%` of its misses (`24/48` across `v2.4.1`) have `p >= 0.60` (up to `0.78`), failing silently without triggering fallback.<br>• **Calling `/openai/v1/decisions` on Azure AI Foundry**: returns `HTTP 404`; Foundry serves `Microsoft Decision-1` at `/providers/microsoft/v1/systemone` instead.<br>• **Leaving default reasoning enabled on LLM routers**: `gpt-6-luna` default drops to `72.5%–75.8%` accuracy and flips choices across rounds on `11–13 / 40` prompts.<br>• **Commercial production use of `OpenJev 27B` weights (`CC BY-NC 4.0` non-commercial license)** or 5-way general model routing with `Laya 0.3.20` (`47.5%–52.5%` accuracy). |

> **Provenance & Readiness**: `anonymized_reported` (`independently_reproduced=false`). Evaluated `2026-10-11..10-13` across `Switchyard` `v2.3.0`, `v2.4.0` (`960` calls), and `v2.4.1` (`2,760` calls + `160` direct API diagnostic calls). Public router: [`satomic/model-router`](https://github.com/satomic/model-router) (`b58bfd31`, `3408c39c`, `8a20a7b6`).
