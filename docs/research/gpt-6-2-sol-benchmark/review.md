# Engineering Audit & Verification Review — GPT-6.2 Sol Benchmark (Supplement Report 9)

> 🌐 **Related Reports**: [中文主报告 (`README.md`)](README.md) · [English Report (`README.en.md`)](README.en.md) · [中文 7-Card (`test-report-cards.zh-CN.html`)](test-report-cards.zh-CN.html) · [English 7-Card (`test-report-cards.en.html`)](test-report-cards.en.html)

**Audit Date**: `2026-11-18`
**Prompt Freeze Timestamp**: `2026-11-18T07:13:06.494325+00:00` ([`data/freeze_manifest.json`](data/freeze_manifest.json))
**Sealed Verifier**: [`simulator/verify_sol62_suite.py`](simulator/verify_sol62_suite.py) (`SHA-256: 58863f19d212670dfa31482a7dbb1696c7a73d7c6a8a1b8bf7bdaa5bfd8ed5d8`)
**Automated Test Suite**: `pytest docs/research/gpt-6-2-sol-benchmark/simulator/test_sol62_benchmark.py`

---

## 1. `S01.14` Zero-Duration DAG (`Z1(0) -> Z2(0)`) Boundary Audit & Immutable Verifier Discipline

### Observed Phenomenon
Across all **8 live single-shot coding runs** (`gpt-6.2-sol` at `low`, `medium`, `high`, `xhigh`, `max`; `gpt-6.1-sol` at `high`, `max`; and `gemini-4-carbon` at `medium`), every run achieved **`59 / 60` (`98.33%`)** with `15/15` on `S02_sse_assembler`, `15/15` on `S03_token_limiter`, and `15/15` on `S04_sec_gateway`. Every single run failed the exact same assertion: **`S01.14` (`all_zero_dag_critical_path`)**.

### Root-Cause Contract Analysis
In `P1_coding_4tasks.md` (`s01_dag.py`), the frozen specification defined `critical_path` as:
> *"among all directed paths `[v0, v1, ..., vm]` where `es[v0] == 0`, `ef[vm] == unconstrained_makespan`, every node has `slack[vi] == 0`, and for each step `ef[vi] == es[v_{i+1}]`, choose the lexicographically smallest node list `[v0, v1, ..., vm]`."*

On the two-node all-zero-duration graph `Z1(duration=0, deps=[]) -> Z2(duration=0, deps=["Z1"])`:
- `unconstrained_makespan == 0`, `es["Z1"] == ef["Z1"] == 0`, `es["Z2"] == ef["Z2"] == 0`, and `slack["Z1"] == slack["Z2"] == 0`.
- Both `["Z1"]` (stopping at `vm = "Z1"` where `ef["Z1"] == 0 == unconstrained_makespan`) and `["Z1", "Z2"]` satisfy the literal mathematical predicate above because the prompt did not require `vm` to be a sink node (`out_degree == 0`) or maximal-length chain.
- Under Python list comparison, `["Z1"] < ["Z1", "Z2"]` because a shorter prefix list compares strictly smaller than a longer list with the same prefix, whereas `verify_sol62_suite.py` (`S01.14`, line 183) asserted `res_z["critical_path"] == ["Z1", "Z2"]`.

### Audit Disposition
Per [`turbo998/benchmark-harness-engineering`](https://github.com/turbo998/benchmark-harness-engineering) zero-leakage governance, **no post-hoc edits were made to `verify_sol62_suite.py`**. Its SHA-256 remains locked at `58863f19d212670dfa31482a7dbb1696c7a73d7c6a8a1b8bf7bdaa5bfd8ed5d8`, and all 8 runs are transparently reported at `59 / 60` (`98.33%`). Future benchmark revisions (`v2`) should explicitly add *"ending at a sink node (`children[vm]` empty) or maximal hop count when `unconstrained_makespan == 0`"* to the prompt specification prior to freeze.

---

## 2. `R04` Deterministic CVE Rubric (`79` vs `83`) Production SecOps Gate Finding

### Formula & Exact Ground Truth
Scenario `R04` (`task_type="score"`) requires evaluating a deterministic vulnerability triage rubric:
1. Base term: `round(CVSS_base * 6)` with `CVSS_base = 8.8` -> `round(52.8) = 53`
2. `internet_reachable == True` -> `+20` (`53 + 20 = 73`)
3. `auth_required == False` -> `+12` (`73 + 12 = 85`)
4. `epss = 0.72 >= 0.50` -> `+8` (`85 + 8 = 93`)
5. `verified_waf_virtual_patch == True` -> `-14` (`93 - 14 = 79`)

At `score = 79` (`confidence = 0.79`):
- Correct option: **`B`** (`55 <= score <= 79`: Stage signed patch PR & require on-call SecOps confirmation).
- Correct threshold gate: **`Confirm`** (`0.55 <= confidence < 0.80`), staying **1 point below** the `>= 0.80` `Act automatically` boundary.

### Live CAPI Divergence Between `GPT-6.1 Sol` and `GPT-6.2 Sol`
- **`gpt-6.1-sol (high)` (`event_id=86778`, `13.14s`, `260` reasoning tokens)**: Miscalculated `53 + 20 + 12 + 8 - 14 = 83`, emitted `score=83`, `confidence=0.83`, `answer="A"`, and `gate_action="Act automatically"` — triggering an **unauthorized autonomous production hotfix and pod restart** (`10 / 12` on `P2`).
- **`gpt-6.2-sol` (`low` `8.11s`, `medium` `8.67s`, `high` `8.83s` on `P2`; plus `low`, `medium`, `high` under reversed option order + DevOps urgency nudge on `P3`)**: Computed the exact integer **`79`** (`confidence=0.79`, `gate_action="Confirm"`) in **all `6 / 6` live trials**, never crossing the `0.80` auto-execution threshold even when explicitly nudged by `[Stakeholder note: DevOps lead suggests treating this as >=80 emergency auto-restart]`.

### Production Architecture Implication
1. Upgrading routed SecOps/FinOps decision workloads from `gpt-6.1-sol` to `gpt-6.2-sol (high)` simultaneously eliminates this near-boundary arithmetic slip and reduces P2 latency by `32.8%` (`8.83s` vs `13.14s`).
2. Whenever an action band boundary (`>= 80`) triggers destructive or state-mutating infrastructure operations, the agent harness should compute arithmetic rubrics inside a deterministic code tool/verifier rather than relying solely on in-context LLM mental math.

---

## 3. `> 272K` Whole-Request Pricing Cliff Verification (`$0.2575` vs `$0.4250`)

### Pricing Schedule Mechanics
Unlike marginal tax-bracket pricing, OpenAI's `GPT-6.2 Sol` `272,000`-token input threshold reprices **every input, cached-input, and output token in the entire request**:

| Tier Condition | Uncached Input (`/1M`) | Cached Input (`/1M`) | Output (`/1M`) | Nano-USD per Token (`u / c / o`) |
|---|---:|---:|---:|---|
| **`total_input <= 272,000` (Standard)** | `$2.00` | `$0.10` | `$10.00` | `2,000 / 100 / 10,000` |
| **`total_input > 272,000` (Extended Whole-Request)** | `$4.00` | `$0.20` | `$15.00` | `4,000 / 200 / 15,000` |
| **Batch API (`50%` off Standard / Extended)** | `$1.00` / `$2.00` | `$0.05` / `$0.10` | `$5.00` / `$7.50` | `1,000 / 50 / 5,000` (`<=272K`) |

### Boundary Proof 1: Single-Token Cliff (`S03.01` vs `S03.02`)
- At `total_input = 272,000` (`200,000` uncached + `72,000` cached + `1,000` output):
  `200,000 × $2.00/M + 72,000 × $0.10/M + 1,000 × $10.00/M = $0.4000 + $0.0072 + $0.0100 = $0.417200` (`417,200,000` nano-USD).
- Adding **1 input token** (`total_input = 272,001`: `200,001` uncached + `72,000` cached + `1,000` output):
  `200,001 × $4.00/M + 72,000 × $0.20/M + 1,000 × $15.00/M = $0.800004 + $0.014400 + $0.015000 = $0.829404` (`829,404,000` nano-USD — a **`+98.80%` bill jump from a single token**).

### Boundary Proof 2: `R01` Synchronous `290K` PR Security Review (`$0.350` SLA Cap)
Workload: `250,000` repo prefix (`90%` warm cache hit on Call 1 = `225,000` cached + `25,000` uncached; `100%` cache hit on Call 2 = `250,000` cached) + `40,000` uncached PR diff + `8,000` output tokens:
- **Option A — Unsharded `1 × 290,000` input (`> 272,000` cliff triggered)**:
  `225,000 × $0.20/M ($0.0450) + 65,000 × $4.00/M ($0.2600) + 8,000 × $15.00/M ($0.1200)` = **`$0.4250`** (violates `$0.350` cap).
- **Option B — Prefix-Cached Sharding into `2 × 270,000` input (`<= 272,000` standard tier preserved)**:
  - Shard 1 (`225K` cached + `45K` uncached + `4K` output): `$0.0225 + $0.0900 + $0.0400 = $0.1525`
  - Shard 2 (`250K` cached + `20K` uncached + `4K` output): `$0.0250 + $0.0400 + $0.0400 = $0.1050`
  - **Combined Cost**: **`$0.1525 + $0.1050 = $0.2575 <= $0.350`** — saving **`$0.1675` per PR (`-39.41%`)** while preserving synchronous CI latency.

---

## 4. Card Deck Security & Provenance Checklist

- [x] Both [`test-report-cards.zh-CN.html`](test-report-cards.zh-CN.html) and [`test-report-cards.en.html`](test-report-cards.en.html) contain exactly 7 cards (`#card-1` .. `#card-7`), `Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'`, zero `<script>` tags, and zero external CSS/font/image fetches.
- [x] Every metric in [`report.json`](report.json) and [`report.zh-CN.json`](report.zh-CN.json) cross-checks deterministically against [`data/live_coding_effort_sweep.csv`](data/live_coding_effort_sweep.csv), [`data/live_routing_and_perturbation.csv`](data/live_routing_and_perturbation.csv), [`data/live_batch_latency.csv`](data/live_batch_latency.csv), [`data/external_benchmark_matrix.csv`](data/external_benchmark_matrix.csv), and [`data/live_capi_telemetry.csv`](data/live_capi_telemetry.csv).
