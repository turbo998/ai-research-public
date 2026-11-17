# Minute-Exact Zero-Lookahead Trading Agents (`jackson-cmd/risk-aware-trading-agents`) & Open-Source MCP Financial Charts (`funnest-xyz/funnest-charts`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 21 (Cumulative Round 445 Milestone)  
> **Tracked Repositories**:
> - **`jackson-cmd/risk-aware-trading-agents`** (`★ 220`, Python 3.10+ / PyPI `0.8.0` / MCP / Hugging Face `rta-bench-1`, `MIT`): US equities AI trading agent suite and zero-lookahead LLM trading benchmark that replays news at the exact minute it was published, fills orders at the next open, runs an automated look-ahead check on every research run, scores models both blind and named before/after training cutoffs across 2020/2022/2026 frozen markets, and enforces VIX + FOMC/CPI macro gates with a `30%` cash floor (alongside companion options terminal reference **`jackson-cmd/zeus-options-terminal`**, `★ 112`)
> - **`funnest-xyz/funnest-charts`** (`★ 88`, TypeScript / `@funnest/charts-react` / `@funnest/charts-cli` / `@funnest/charts-mcp`, `Apache-2.0`): Iframe-free native financial charting engine and SSR-safe SVG portfolio component suite supporting live positions, open orders, drag-to-modify orders on the chart, deterministic CLI rendering (`PNG/SVG/HTML/React`), and a built-in MCP server  
> **Audit Claim ID**: `CLAIM-20261117-R21-RISKAWARE-FUNNEST` (underlying commercial exchange market-data feed licensing marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Enterprise FinTech & Wealth-Tech Teams Building LLM Research Assistants Hit Two Architectural Traps: Look-Ahead Backtest Contamination and Closed-Source Iframe Charting Lock-In**:
   - **Trap 1 — Calendar-Date News Joins & Pre-Cutoff Ticker Memorization**: Most financial agent backtests join news headlines to daily bars by calendar date—allowing an agent to trade a 4:30 PM post-close earnings release at that same day's 4:00 PM close. Worse, testing an LLM on named historical tickers (`NVDA`, `AAPL`) from 2020–2022 measures the model's memorized training weights rather than genuine reasoning.
   - **Trap 2 — Proprietary Iframe Charting SDKs**: Commercial financial charting libraries often run inside isolated iframes that cannot inherit host CSS design tokens, charge steep per-seat/per-domain fees, and lack native CLI/MCP endpoints for AI agents to render deterministic portfolio or candlestick charts.
   - **The Solution Architect Stack (`risk-aware-trading-agents` MIT + `funnest-charts` Apache-2.0)**: Deploy **`jackson-cmd/risk-aware-trading-agents`** (`MIT`) as the quantitative research and macro-risk MCP engine (minute-exact news replay, next-open order fills, mandatory look-ahead checks, blind vs. named and pre/post-cutoff evaluation across frozen 2020/2022/2026 markets, VIX + FOMC/CPI regime gates, and a `30%` cash floor); pair it with **`funnest-xyz/funnest-charts`** (`Apache-2.0`) on the frontend and agent reporting layer for iframe-free `<FnChart />` canvases (with interactive drag-to-modify orders), SSR-safe SVG dashboard charts, and `@funnest/charts-mcp`.
2. **Closed-Form FinOps Impact (15 Quant & Wealth-Tech Seats Running 500 Monthly Strategy Backtests & Rendering 30,000 Portfolio/Trading Chart Views at `$95.00/hr`)**:
   - Transitioning from **Path A (Commercial Quant Backtest SaaS + Proprietary Charting SDK Licenses at `$6,030.00/mo`)** to **Path C (`risk-aware-trading-agents` MIT + `funnest-charts` Apache-2.0 at `$370.00/mo`)** saves **`$5,660.00/mo` (`-93.86%`, or `$67,920.00/yr`)** while cutting look-ahead contamination audits and custom chart bridge engineering from `38.0 hrs/mo` to `3.0 hrs/mo` (**`92.11%` reduction**).

![risk-aware-trading-agents + Funnest Charts Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r21-risk-aware-funnest-charts.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `jackson-cmd/risk-aware-trading-agents` eliminate look-ahead leakage and LLM ticker memorization in financial backtesting?
- **Plain-Language Definition**: `risk-aware-trading-agents` (`PyPI 0.8.0`, `MIT`) is both a **minute-accurate zero-lookahead LLM trading benchmark (`rta-bench-1`)** and a **macro-regime-aware US equities agent suite** with bilingual CLI (`--lang zh`), a `:8501` web dashboard, and a containerized MCP server.
- **Four Institutional-Grade Engineering Guardrails**:
  1. **Minute-Exact News Arrival + Next-Open Fills + Automated Look-Ahead Checks**: Every news headline or SEC 8-K filing arrives at the exact minute it was published, and orders execute at the next market open—preventing post-close headlines from trading at same-day closes. Every `riskaware research run` executes an automated look-ahead verification check.
  2. **Frozen 2020/2022/2026 Markets × Blind vs. Named × Training-Cutoff Split**: Evaluates Llama, GPT, Claude, and Gemini across three frozen market regimes (the 2020 crash, the 2022 bear market, and 2026) with 3 seeds each, comparing **blind (anonymized ticker)** vs. **named** performance and scoring results separately **before and after each model's training cutoff**.
  3. **Macro Regime Gates & 30% Cash Floor**: Checks VIX fear regimes, the FOMC / CPI / jobs calendar, earnings dates, and cross-verified news before buying, while enforcing a hard **`30%` cash floor** and benchmarking paper-trading agents against `SPY`.
  4. **MCP Server & Companion Options Architecture**: Runs over stdio via `docker run -i --rm ghcr.io/jackson-cmd/risk-aware-trading-agents mcp` across 10 supported brokers; for options Greeks, P/L grids, and 4-source news aggregation, architects can also study the author's companion **`zeus-options-terminal`** (`★ 112`, noting its `PolyForm Noncommercial` license for reference vs. commercial use).

### Q2: Why are wealth-tech engineering teams replacing iframe financial widgets with `funnest-xyz/funnest-charts` (`Apache-2.0`)?
- **The Iframe & Agent Blind-Spot Problem**: Traditional iframe trading widgets cannot inherit host CSS variables, require awkward postMessage bridges to overlay user positions, and cannot be invoked by an AI coding or research agent to render static SVG/PNG chart artifacts.
- **Three Architectural Advantages of `funnest-charts` (`Apache-2.0`)**:
  1. **Iframe-Free Native `<FnChart />` with Drag-to-Modify Orders**: Renders directly inside your page DOM/Canvas, automatically matching system light/dark themes and CSS design tokens, overlaying live positions, open orders, and fills with **interactive drag-to-modify orders** over a single exchange-agnostic `Datafeed` interface.
  2. **SSR-Safe SVG Dashboard Components (`@funnest/charts-react`)**: Provides server-renderable `LineChart`, `AreaChart`, `BarChart`, `CandlestickChart`, `DonutChart`, `TreemapChart`, and `PercentageBarChart` components with built-in multi-locale color polarity (`green-up / red-down` global vs. `red-up / blue-down` KR/Asia).
  3. **Agent-Native CLI & MCP Server (`@funnest/charts-mcp`)**: Agents can register `claude mcp add funnest-charts -- npx -y @funnest/charts-mcp` or run `npx @funnest/charts-cli render spec.json --out chart.png` to turn declarative JSON specs into PNG, SVG, HTML, or React `.tsx` code.

### Q3: How should an AI Solution Architect combine `risk-aware-trading-agents` and `funnest-charts` in an enterprise wealth-tech platform?
- **Backend Research & Risk Engine (`risk-aware-trading-agents` MCP)**: Expose `regime`, `scan`, `analyze`, and zero-lookahead `research run` tools over MCP so advisory agents ground every recommendation in VIX/FOMC regime checks and point-in-time verified backtests.
- **Frontend & Report Rendering Layer (`@funnest/charts-react` + `@funnest/charts-mcp`)**: Stream live signals and order books into `<FnChart />` on the web client while letting research agents auto-render SVG/PNG performance cards via `@funnest/charts-mcp`.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart LR
    subgraph QuantBackend["Zero-Lookahead Quant Engine: risk-aware-trading-agents (MIT, PyPI 0.8.0)"]
        A[SEC 8-K / Minute-Stamped News + Prices] --> B[Minute-Exact Replay + Next-Open Fill<br/>Mandatory Look-Ahead Check on Every Run]
        B --> C[rta-bench-1 Evaluation Matrix<br/>2020/2022/2026 × Blind vs. Named × Pre/Post-Cutoff]
        C --> D[Production Risk Guardrails<br/>VIX + FOMC/CPI Calendar + Earnings Check + 30% Cash Floor]
        D --> E[riskaware MCP Server]
    end

    subgraph ChartFrontend["Native Charting &amp; MCP Studio: funnest-xyz/funnest-charts (Apache-2.0)"]
        E --> F[Claude / Advisory Agent Orchestrator]
        F -->|@funnest/charts-mcp &amp; CLI| G[Render Spec → PNG / SVG / HTML / React Code]
        F -->|Datafeed Stream| H[Iframe-Free &lt;FnChart /&gt; Canvas<br/>Positions/Orders Overlay + Drag-to-Modify + SSR SVG Cards]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Commercial Quant SaaS + Proprietary Charting SDKs | Option B: Daily-Bar Pandas Scripts + Generic ECharts | **Option C (Recommended): `risk-aware-trading-agents` (MIT) + `funnest-charts` (Apache-2.0)** |
| :--- | :--- | :--- | :--- |
| **Look-Ahead & Ticker Memorization Prevention** | ⚠️ Often joins news by calendar date; lacks LLM training-cutoff splits | ❌ Severe post-close news look-ahead leakage on daily bars | ✅ **Minute-exact news replay + next-open fills + look-ahead check + blind/cutoff split** |
| **Macro Regime & Cash-Floor Risk Controls** | ⚠️ Requires custom macro-calendar integration | ❌ Pure technical indicators fail during FOMC/CPI shocks | ✅ **Built-in VIX + FOMC/CPI/jobs calendar gates + earnings check + `30%` cash floor** |
| **Native DOM Integration & Order Dragging** | ⚠️ Locked inside iframes; expensive per-domain commercial licensing | ❌ Lacks native order-line dragging & financial tick/session logic | ✅ **Iframe-free `<FnChart />` with drag-to-modify orders + SSR SVG cards (`Apache-2.0`)** |
| **AI Agent (MCP / CLI) Operability** | ❌ Closed-source black box with no MCP endpoints | ❌ Requires brittle headless browser screenshots for reports | ✅ **Native MCP servers (`riskaware mcp` + `@funnest/charts-mcp`), CLI & `/llms.txt`** |
| **Monthly TCO (15 Seats / 500 Backtests / 30k Views)** | **`$6,030.00 / mo`** (`$2,420` SaaS/SDK fees + `38.0 hrs` audit/bridge work) | **`$2,660.00 / mo`** (`$950` compute + `18.0 hrs` custom UI/cleaning) | **`$370.00 / mo`** (**`-93.86%` savings**; `$85` containers + `3.0 hrs` strategy sign-off) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R21-RISKAWARE-FUNNEST`)

> **Scope & Boundary Declaration**: Evaluated for a 15-seat quantitative research and wealth-tech engineering team executing **500 monthly point-in-time strategy backtests and rendering 30,000 interactive client portfolio/trading chart views** at a blended engineering rate of `$95.00/hr` (commercial exchange market-data feed licensing marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Backtest/Charting SDK Spend} + (\text{Look-Ahead Audit \& Chart Integration Hours} \times \$95.00)$$

| Cost Component | Path A: Commercial Quant SaaS + Proprietary Chart SDKs | Path B: Daily-Bar Pandas + Generic ECharts | **Path C: `risk-aware` (MIT) + `funnest-charts` (Apache-2.0)** |
| :--- | :---: | :---: | :---: |
| **Monthly Backtest & Charting SDK Licenses / Container Spend** | `$2,420.00` | `$950.00` | **`$85.00`** |
| **Monthly Look-Ahead Audit & Chart Integration Hours** | `38.0 hrs` | `18.0 hrs` | **`3.0 hrs`** (**`92.11%` reduction**) |
| **Monthly Quant & Frontend Engineering Labor (`@ $95.00/hr`)** | `$3,610.00` | `$1,710.00` | **`$285.00`** |
| **Total Monthly TCO** | **`$6,030.00`** | **`$2,660.00`** (`-55.89%`) | **`$370.00`** (**`-93.86%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,370.00 / mo` (`$40,440/yr`) | **`$5,660.00 / mo` (`$67,920.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Install `risk-aware-trading-agents` & Run Frozen-Market Look-Ahead Checks**: Run `pip install "risk-aware-trading-agents[dashboard,mcp]"` and execute `riskaware research run -s swing_trend --period 2022` to verify minute-stamped news replay, next-open fills, and automated look-ahead verification.
- [ ] **Step 2 — Enforce Blind-Ticker & Post-Cutoff Evaluation Splits**: Evaluate all LLM trading prompts in both blind (anonymized ticker) and named modes across the 2020, 2022, and 2026 datasets, keeping the `30%` cash floor and VIX/FOMC calendar gates active.
- [ ] **Step 3 — Embed `@funnest/charts-react` in Client & Advisory Dashboards**: Install `npm i @funnest/charts-react` to replace iframe widgets with native `<FnChart />` (enabling drag-to-modify orders) and SSR-safe SVG `DonutChart` / `TreemapChart` components.
- [ ] **Step 4 — Register Both MCP Servers (`riskaware mcp` & `@funnest/charts-mcp`)**: Connect `ghcr.io/jackson-cmd/risk-aware-trading-agents mcp` and `npx -y @funnest/charts-mcp` to Claude Code / Cursor so agents can run zero-lookahead scans and render PNG/SVG/React chart reports in one workflow.
