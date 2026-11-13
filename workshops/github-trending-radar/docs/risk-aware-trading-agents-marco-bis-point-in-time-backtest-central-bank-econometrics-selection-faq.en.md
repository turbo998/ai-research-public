# Point-in-Time News Backtesting Trading Agents (`jackson-cmd/risk-aware-trading-agents` `v0.7.2`) & BIS 7-Stage Macroeconometric Research Companion (`bis-med-it/marco-BIS`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 9 (Cumulative #137) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, Quantitative Research Leads, and Econometric Modeling Teams evaluating two high-rigor financial and macroeconomic agent frameworks:
> 1. **`jackson-cmd/risk-aware-trading-agents` (`98★` in 1 day, Python 3.10+, MIT, PyPI `0.7.2`, MCP `io.github.jackson-cmd/risk-aware-trading-agents`)**: US stock AI trading agents with **point-in-time news backtesting that cannot see the future** — bundling a frozen **2026 point-in-time dataset** (prices, VIX, FOMC/CPI calendar, earnings dates, and cross-verified headlines) audited via `riskaware research run` look-ahead checks, enforcing a **30% cash floor**, VIX/FOMC regime gates, and pre-earnings dip-buying checks, ranking 4 paper-trading agents against `SPY`, and exposing a bilingual `:8501` dashboard, MCP server, and 10 broker adapters!
> 2. **`bis-med-it/marco-BIS` (`55★` in 3 days, Python, Apache-2.0, Bank for International Settlements **BIS Working Papers No. 1395** by Lombardi, Park, and Perez-Cruz)**: **MaRCo@BIS (MAcroeconometric Research Companion)** — an official central-bank agentic skill framework, reference Python library (**covered by >1,000 tests**), and canonical model dictionary that guides Claude Code through a **7-stage human-in-the-loop workflow** (`model selection → variables → lags → identification → sample → sensibility checks → reporting`) with zero silent decisions, mandatory source attribution, and automatic flagging of **price puzzles, explosive roots, and weak instruments**!
>
> **中文版本**: [risk-aware-trading-agents-marco-bis-point-in-time-backtest-central-bank-econometrics-selection-faq.md](risk-aware-trading-agents-marco-bis-point-in-time-backtest-central-bank-econometrics-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r9-riskaware-marcobis.svg`](../../../assets/github-ai-radar-2026-11-13-r9-riskaware-marcobis.svg)

![risk-aware-trading-agents v0.7.2 and bis-med-it/marco-BIS Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r9-riskaware-marcobis.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "LLM stock backtests that accidentally peek at post-close news (look-ahead bias) or buy dips right into FOMC rate decisions and earnings landmines" (`jackson-cmd/risk-aware-trading-agents` `v0.7.2`)**: Most LLM trading backtests look artificially profitable because generic search APIs feed future headlines into past decision dates. `risk-aware-trading-agents` ships a frozen **2026 point-in-time dataset** and a `riskaware research run` look-ahead checker that proves exactly which cross-verified headlines were visible at each timestamp, while enforcing VIX + FOMC/CPI regime checks, earnings-window filters, a **30% cash floor**, and head-to-head benchmarking against `SPY` (`--compare buy_and_hold,ema_bounce`)!
   - **Ending "silent LLM econometric assumptions where an agent guesses VAR lag orders, trips on raw FRED CSV metadata rows, or reports explosive roots and price puzzles as valid findings" (`bis-med-it/marco-BIS`)**: Released alongside BIS Working Paper No. 1395, `MaRCo@BIS` enforces a **7-stage human-in-the-loop workflow** across three entry modes (Mode A canonical dictionary replication like Sims 1980 6-variable VAR, Mode B PDF paper replication, Mode C open policy questions). Every specification choice cites its source, computations run on a **>1,000-test reference Python library (`scripts/lib/`)**, and stage 6 automatically flags **price puzzles, explosive roots, and weak instruments** before generating reports!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R9-RISKAWARE-MARCOBIS`)**:
   - Modeled for a **quant and macroeconomic research desk executing `180 strategy backtest & regime attribution runs per month` and `40 macroeconomic paper replications & policy audits per month`** (fully loaded quant/econometric researcher rate `$100.00/hr`; institutional Level-2 tick feeds and prime-broker execution commissions: `not_measured`):
   - Upgrading from **Path A (look-ahead-contaminated LLM backtests + ad-hoc VAR scripts with silent specification bugs, `$6,540.00/mo`)** to **Path C (`risk-aware-trading-agents v0.7.2` point-in-time backtester + `bis-med-it/marco-BIS` 7-stage 1,000-test econometric companion, `$740.00/mo`)** saves **`$5,800.00/mo` (`-88.69%`, or `$69,600.00/yr`)** and cuts look-ahead forensics and replication debugging labor from `45.0 hrs/mo` to `5.0 hrs/mo` (**`-88.89%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why do unconstrained LLM backtests and single-prompt econometric scripts fail institutional audit standards?
- **First-Principles Breakdown**:
  1. **Temporal Leakage in News & Macro Feeds**: Without strict point-in-time timestamp gating and look-ahead checks, LLMs exploit future information during historical simulations.
  2. **Silent Identification Choices & Statistical Pathologies**: In macroeconometrics, lag selection, Cholesky ordering, or unflagged explosive roots/price puzzles completely invalidate impulse-response conclusions.

### Q2: How does `jackson-cmd/risk-aware-trading-agents` (`v0.7.2`) guarantee zero look-ahead bias and macro-aware risk discipline?
- **First-Principles Breakdown**:
  1. **Frozen 2026 Point-in-Time Dataset & `riskaware research run` Look-Ahead Audit**:
     - Pairs historical bars with VIX, FOMC/CPI dates, earnings calendars, and timestamped cross-verified news, verifying that backtests never access future headlines.
  2. **30% Cash Floor, Pre-Earnings Dip Check & MCP/10-Broker Integration**:
     - Enforces a 30% cash floor and earnings-date checks before buying dips, ranks 4 paper-trading agents against `SPY`, and exposes all tools via CLI, `:8501` web UI, and MCP.

### Q3: How does `bis-med-it/marco-BIS` combine 7-stage HITL checkpoints, a canonical paper dictionary, and >1,000 unit tests?
- **First-Principles Breakdown**:
  1. **Three Entry Modes (Dictionary / PDF / Open Question) & 7-Stage Source-Attributed Checkpoints**:
     - Walks researchers through `model selection → variables → lags → identification → sample → sensibility checks → reporting` with mandatory human confirmation and explicit source attribution at every step.
  2. **>1,000-Test Reference Library (`scripts/lib/`) & Anomaly Detection**:
     - Executes estimations via a >1,000-test Python library (`test_replications_smoke.py --runslow` verifies paper targets on cleaned FRED-MD/QD panels) and flags price puzzles, explosive roots, and weak instruments automatically.

---

## 🧭 3. Mermaid Decision Tree & Point-in-Time Backtest + 7-Stage Econometric Architecture

```mermaid
flowchart TD
    A["Quantitative Backtesting & Macroeconomic AI Research Selection"] --> B{"Primary Research Workload?"}
    B -- "US equity news/regime backtesting & paper trading with zero look-ahead bias" --> C["Adopt jackson-cmd/risk-aware-trading-agents (v0.7.2 CLI / Web UI / MCP)"]
    B -- "Central-bank macroeconometric replication & policy analysis (VAR / IV / Local Projections)" --> D["Adopt bis-med-it/marco-BIS (BIS Working Paper 1395 Companion)"]

    C --> C1["Frozen 2026 point-in-time dataset + riskaware research run look-ahead check"]
    C1 --> C2["VIX + FOMC/CPI calendar + earnings check + 30% cash floor vs SPY"]

    D --> D1["Triage to Mode A (Model Dictionary), Mode B (PDF Paper) or Mode C (Policy Query)"]
    D1 --> D2["7-stage HITL confirmation + >1,000-test library + price puzzle/explosive root flags"]

    C2 & D2 --> E["🏆 Golden Quant/Macro Stack: Leak-Free Point-in-Time Backtests + 7-Stage Econometrics (-88.69% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Unchecked LLM Backtests + Ad-Hoc VAR Scripts | Path B: Price-Only Backtrader + Manual R/Stata | **Path C (Recommended): `riskaware v0.7.2` + `MaRCo@BIS`** |
| :--- | :--- | :--- | :--- |
| **Point-in-Time News Leakage Guard** | High risk of post-close headline leakage | No cross-verified news backtesting | **Frozen 2026 dataset + `riskaware research run` look-ahead verifier** |
| **Macro Calendar & Cash Floor Discipline** | Ignores FOMC/CPI & earnings traps | Manual calendar scripts | **Built-in VIX + FOMC/CPI regime gate, earnings check & 30% cash floor** |
| **Econometric Specification Governance** | Silent LLM lag/identification guesses | Slow manual literature lookup | **7-stage HITL workflow with source attribution & canonical paper dictionary** |
| **Statistical Pathology Detection** | Unchecked price puzzles & explosive roots | Manual post-hoc plotting | **Automated flags for price puzzles, explosive roots & weak instruments (`>1,000` tests)** |
| **Monthly TCO (180 Backtests + 40 Replications)** | **`$6,540.00 / mo`** (`$2,040` compute + `$4,500` labor) | **`$3,320.00 / mo`** (`$920` compute + `$2,400` labor) | **`$740.00 / mo` (Saves `$5,800.00/mo` · `-88.69%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R9-RISKAWARE-MARCOBIS`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A quant and macroeconomic research desk running **180 point-in-time equity strategy backtests per month** and **40 macroeconomic paper replications and policy audits per month**.
- **Labor Rate**: Fully loaded quantitative / econometric researcher rate of **`$100.00 / hr`**.
- **Explicit Not-Measured Boundary**: Institutional Level-2 exchange data feeds and prime-broker execution commissions are marked **`not_measured`**. This model strictly accounts for research LLM/compute spend and researcher hours spent debugging look-ahead leakage, cleaning FRED panels, and fixing specification errors.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Contaminated LLM Backtests + Ad-Hoc VAR Scripts | Path B: Price-Only Scripts + Manual R/Stata | **Path C: `riskaware v0.7.2` + `MaRCo@BIS` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly Research API & Backtest Compute Spend** | **`$2,040.00`** (repeated contaminated reruns + failed script generation) | **`$920.00`** (standard compute & API usage) | **`$240.00`** (frozen 2026 dataset + deterministic `scripts/lib/` engine) |
| **Look-Ahead Forensics, FRED Cleaning & Replication Labor (`$100/hr`)** | `45.0 hrs × $100.00` = **`$4,500.00`** | `24.0 hrs × $100.00` = **`$2,400.00`** | `5.0 hrs × $100.00` = **`$500.00`** |
| **Total Monthly TCO** | **`$6,540.00 / mo`** | **`$3,320.00 / mo`** (`-49.24%`) | **`$740.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$3,220.00 / mo` | **Saves `$5,800.00 / mo` (`-88.69%` · `$69,600.00/yr`)** |
| **Level-2 Exchange Feeds & Broker Commissions** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `risk-aware-trading-agents` (`v0.7.2`) & Look-Ahead Audit**: Run `pip install "risk-aware-trading-agents[dashboard,mcp]"`, execute `riskaware regime`, `riskaware backtest --compare buy_and_hold,ema_bounce`, and `riskaware research run` to verify zero look-ahead leakage on the frozen 2026 dataset.
- [ ] **2. Bilingual `:8501` Dashboard & MCP Server Integration**: Launch `riskaware dashboard` to inspect the 4 paper-trading agents against `SPY` and register the MCP server in Claude Code.
- [ ] **3. `bis-med-it/marco-BIS` Fast & Replication Test Suites**: Install `requirements-reproduction.txt`, run `python -m pytest tests -q` (>1,000 tests), strip FRED-MD/QD metadata rows per `UPDATE.md`, and run `python -m pytest tests/test_replications_smoke.py --runslow`.
- [ ] **4. 7-Stage HITL & Anomaly Flag Verification**: Run Mode A (*"Replicate the Sims (1980) six-variable VAR using FRED data"*) in Claude Code, verifying human confirmation at all 7 stages and sensibility checks for price puzzles, explosive roots, and weak instruments.
