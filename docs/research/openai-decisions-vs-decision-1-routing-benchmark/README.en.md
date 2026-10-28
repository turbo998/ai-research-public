# OpenAI Decisions Enters the Ring, Yet Microsoft Decision-1 Remains #1: 8-Engine Model Routing & Prompt Sensitivity Benchmark (Switchyard v2.4.0 & v2.4.1)

> 🌐 **Language / 语言切换**: **[🇬🇧 English (README.en.md)](README.en.md)** | **[🇨🇳 中文完整报告 (README.md)](README.md)** | **[📊 7-Card Report (`test-report.md`)](test-report.md)** | **[🖼️ 7-Card Visual Deck (`test-report-cards.html`)](test-report-cards.html)** | **[↩ Back to Research Index (`../index.md`)](../index.md)**

> **Executive Summary**:
> Expanding the open-source **Switchyard (`satomic/model-router`)** benchmark (`40 bilingual tasks × 5 candidate backend models`) with **OpenAI Decisions API (`POST /v1/decisions`)** and **GPT-6-Luna** (`reasoning_effort="none"` vs default reasoning) across **8 routing engines and 3,880 total routing calls** (`v2.4.0` cost-biased prompt vs `v2.4.1` neutral + 4 prompt variants) yields four decisive production findings:
> 1. **Under Neutral Routing Instructions (`v2.4.1`), All Three System One Dedicated Engines Hit `40 / 40` (`100.0%`) With `40 / 40` Multi-Run Stability**: Removing a single cost-bias sentence (`"prefer cheaper model for simple requests"`) lifts **Microsoft Decision-1**, **TypeSafe Jev**, and **OpenJev 27B** to a perfect **`40 / 40` (`100%`)**, with **Microsoft Decision-1** delivering the lowest cloud cost at **`$7.6 / 1M` decisions** (`541 ms` P50, 1 output token billed).
> 2. **Under Cost-Biased Instructions (`v2.4.0`), System One Threshold Gates Catch 100% of Misses while OpenAI Decisions Drops to `80.0%`**: In `v2.4.0`, **TypeSafe Jev** (`39.3/40 = 98.3%`, `$21.7/1M`, `350 ms`) and **Microsoft Decision-1** (`37.7/40 = 94.2%`, `$8.6/1M`, `541 ms`) keep 100% of their misses below `P <= 0.56` (100% caught by a `0.60` confidence gate). By contrast, **OpenAI Decisions (`POST /v1/decisions` on `gpt-6-luna`)** scores only **`32.0 / 40` (`80.0%`)** at `$28.4 / 1M`, with 9 false-cheap calls exceeding `0.60–0.75` confidence.
> 3. **Prompt Sensitivity & Unidirectional Cheap-Bias Law**: Across 4 prompt variants (`neutral`, `cheap`, `strong`, `bare`), **TypeSafe Jev** varies by just `1` task (`39–40/40`) and **Microsoft Decision-1** by `2` tasks (`38–40/40`), whereas **OpenAI Decisions** swings by `6` tasks (`32–38/40`). Every single error made by `Jev` (`3/3`), `Decision-1` (`9/9`), `OpenJev` (`18/18`), and `OpenAI Decisions` (`48/48`) biases toward the cheapest model (`gpt-4.1-mini`)—never once over-escalating.
> 4. **Reasoning Hurts Routing**: Enabling default reasoning on `gpt-6-luna` drops routing accuracy from **`35.3 / 40` (`88.3%`, `none`)** down to **`30.3 / 40` (`75.8%`, `default`)** due to chain-of-thought over-rationalization, while destabilizing `13 / 40` tasks across runs.

![8-Engine Model Routing Benchmark Overview](assets/overview.svg)

---

## 1. 8-Engine Head-to-Head Scorecard (`v2.4.0` Cheap Prompt vs `v2.4.1` Neutral Prompt)

| Routing Engine | Protocol / Backend | `v2.4.0` (`cheap`) Accuracy | `v2.4.1` (`neutral`) Accuracy | Multi-Run Stability (`v2.4.0` → `v2.4.1`) | P50 Latency (`ms`) | Cloud Cost (`/ 1M Decisions`) | `0.60` Confidence Gate Miss Catch Rate |
|---|---|---:|---:|---:|---:|---:|---:|
| **TypeSafe Jev (`jev-latest`)** | System One (`/v1/systemone`) | **`39.3 / 40` (`98.3%`)** | **`40.0 / 40` (`100.0%`)** | `39/40` → **`40/40`** | **`350 ms`** | `$21.7–$24.1` | **`100%`** (`2/2` misses `<=0.49`) |
| **Microsoft Decision-1** | System One (Azure AI Foundry) | **`37.7 / 40` (`94.2%`)** | **`40.0 / 40` (`100.0%`)** | `37/40` → **`40/40`** | `541 ms` | **`$7.6–$8.6`** | **`100%`** (`7/7` misses `<=0.56`) |
| **OpenJev 27B (Local MLX 4-bit)** | System One (Local M4 Pro 48GB) | `37.0 / 40` (`92.5%`) | **`40.0 / 40` (`100.0%`)** | `40/40` → **`40/40`** | `2,566 ms` | `$0` (CC BY-NC 4.0) | `88.9%` (`1/3` tasks `>0.60`) |
| **OpenAI Decisions API** | OpenAI (`POST /v1/decisions`) | `32.0 / 40` (`80.0%`) | `37.0 / 40` (`92.5%`) (`38/40` on `bare`) | `38/40` → `39/40` | `462 ms` | `$26.1–$28.4` | `62.5%` (`9/24` calls `0.60–0.75`) |
| **`gpt-4.1-mini` (JSON Schema)** | Chat Completions Structured | `36.0 / 40` (`90.0%`) | — | `40/40` | `785 ms` | `$141.8` (`16.5x`) | Uncalibrated verbalized score |
| **`gpt-6-luna` (`effort="none"`)** | Responses API (`none`) | `35.3 / 40` (`88.3%`) | — | `38/40` | `612 ms` | `$39.9` | Uncalibrated verbalized score |
| **`gpt-6-luna` (Default Reasoning)** | Responses API (`default`) | `30.3 / 40` (`75.8%`) | — | `27/40` (13 flips) | `1,840 ms` | `$94.2` | Uncalibrated verbalized score |
| **Laya 8B (Local MLX 4-bit)** | System One (Local 8B) | `29.0 / 40` (`72.5%`) | `33.0 / 40` (`82.5%`) | `40/40` | `920 ms` | `$0` (Apache-2.0) | Requires calibration |

---

## 2. Production Selection Guidance

1. **Primary Cloud Recommendation — `Microsoft Decision-1` (Azure AI Foundry)**: Delivers `100%` accuracy on neutral prompts, `94.2%` on cost-biased prompts with `100%` miss interception at threshold `0.60`, and the lowest cloud cost (`$7.6–$8.6 / 1M` decisions).
2. **Lowest-Latency Cloud Alternative — `TypeSafe Jev`**: Best prompt-wording immunity (`39–40/40` across all 4 prompt styles) and `~330–350 ms` P50 latency at `~3x` the cost of `Decision-1`.
3. **If Using `OpenAI Decisions` (`POST /v1/decisions`)**: Strip all `"prefer cheaper"` phrasing from the routing instruction and move capability boundaries into each candidate's `description` field to recover `37–38 / 40` (`92.5%–95.0%`) accuracy.

- **Full Chinese Technical Report**: [`README.md`](README.md)
- **7-Card 4:5 Benchmark Report & HTML Deck**: [`test-report.md`](test-report.md) · [`test-report-cards.html`](test-report-cards.html) · [`report.json`](report.json)
