# 11-Stage Clean-Room App Cloner (`Jakeschincariol/replica-skill`) & 100-Buyer-Agent Pre-Launch Business Simulator (`Jakeschincariol/founder-skill`) Selection & Architecture FAQ

> **Document Type**: AI Solution Architect Deep-Dive & Peer Selection FAQ (Night Shift Round 114 / Cumulative Round 297)  
> **Benchmark Style**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language First Principles + Core Q&A + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> **Covered Repositories**: `Jakeschincariol/replica-skill` (`★ 9,343` · Python · MIT · 11 Chained Claude Skills for Clean-Room App Reverse-Engineering, Rebuilding, Parity Scoring `/replica-diff` & Review-Mining Differentiation `/replica-entrepreneur`) + `Jakeschincariol/founder-skill` (`★ 3,647` · Python · MIT · 11 Chained Claude Skills Featuring a Hormozi/Thiel/Jobs Board of Directors, a 100-Buyer-Agent Consumer Panel & a Unit-Economics CFO)  
> **Evidence Anchors**: `evidence/trending-daily-2026-11-14-raw.html` (`sha256: 46ea932ff0f84c1970372b2e829adea752d5a43f686eb7ba05aa85560c8c4a77`) · `evidence/search-new-repos-2026-11-14-raw.json` (`sha256: a4edf557e91854831dc80d3670e3e7a1b49c7e9ca14e2e4dd7913489bd7cc2b2`) · `CLAIM-20261114-R114-REPLICASKILL-FOUNDERSKILL`

![2026-11-14 Night Round 114 (R297) SVG Visual Summary](../../../assets/github-ai-radar-2026-11-14-r114-replicaskill-founderskill.svg)

---

## 📌 1. Executive Summary

1. **Why do single-prompt "clone this SaaS app" attempts produce fragile toy prototypes—and why do so many technically working software launches fail to convert paying buyers?**
   - **Pain Point 1 (Single-Prompt App Clones Miss Data-Model Invariants, Edge Flows & User Pain Points)**: Asking an LLM to "clone Calendly" in one prompt yields superficial UI stubs that miss critical database constraints (such as preventing double-booked time slots) and copy the incumbent's flaws without fixing what users hate. With **`★ 9,343`**, **`Jakeschincariol/replica-skill`** (MIT License, zero `pip` dependencies) orchestrates **11 chained Claude skills** writing structured state into a `replica/` folder (`recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy`). It enforces strict **clean-room discipline** ("rebuilds what an app does, never what it owns—never its code, logo, copy, or content"), scores functional parity via `/replica-diff`, and runs **`/replica-entrepreneur`** to mine real negative user reviews of the original app and bake those fixes into your version.
   - **Pain Point 2 (Launching Without Stress-Testing Offers Against a Critical Board, 100 Buyer Personas & Real Unit Economics)**: With **`★ 3,647`**, **`Jakeschincariol/founder-skill`** (MIT License, zero `pip` dependencies) runs 11 pre-launch business validation skills: **`/founder-board`** convenes 3 sub-agent board members trained on Alex Hormozi (*$100M Offers*), Peter Thiel (*Zero to One* Monopoly), and Steve Jobs (Isaacson's *Steve Jobs*) to score the business, name what would kill it, and vote; **`/founder-consumer`** spins up a swarm of **100 buyer agents** with distinct incomes, habits, and objections to simulate 100 purchasing decisions; `/founder-pricing` and `/founder-offer` redesign the offer stack and re-test it on the 100-buyer panel; and **`/founder-ops` + `/founder-cfo`** model contribution margins, daily break-even volume, and 12-month cash flow.
2. **Closed-Form FinOps Verdict (`CLAIM-20261114-R114-REPLICASKILL-FOUNDERSKILL`)**: Across `25` competitive SaaS teardowns, clean-room rebuilds, and 100-buyer pre-launch stress tests per month (`$95/hr`, local workstation hardware: `not_measured`), combining **`replica-skill` + `founder-skill`** (Path C) reduces monthly cost to **`$417.50/mo`** compared to **`$5,555.00/mo`** for unguided clone rewrites and unvalidated ad/launch spend (Path A)—saving **`$5,137.50/mo` (`-92.48%`)** or **`$61,650.00/yr`**.

---

## 🔍 2. Core Q&A (Q1 / Q2 / Q3 First-Principles Deep Dive)

### Q1: What are they in plain English, and how do their core mechanisms work?

- **`Jakeschincariol/replica-skill`: An 11-Stage Clean-Room Software Reverse-Engineering, Parity Auditing, and Review-Driven Differentiation Pipeline**
  - **First Principle**: Clean-room software competition works by extracting the **behavioral flow graph and relational invariants (`recon.md` + `features.csv`)**, verifying parity quantitatively (`/replica-diff`), and solving the incumbent's top user complaints (`/replica-entrepreneur`).
  - **Three Core Mechanisms**:
    1. **Behavioral Recon & Schema Architecture (`/replica-recon`, `/replica-architect`, `/replica-design`)**: Maps every screen, user flow, component, and inferred data model from public pages, store listings, and an authenticated walkthrough while explicitly scoping out non-feature network moats (e.g., partner marketplaces) and encoding database constraints.
    2. **Screen-by-Screen Build, Flow Testing & Parity Scoring (`/replica-build`, `/replica-backend`, `/replica-test`, `/replica-diff`)**: Builds the UI and auth/DB/payment backend from the recon map, clicks through every flow to catch bugs, and scores parity against the original app.
    3. **Review-Mining Entrepreneur & Clean-Room Rebranding (`/replica-entrepreneur`, `/replica-brand`, `/replica-launch`, `/replica-deploy`)**: Analyzes what real users hate about the original app, implements fixes, creates an independent brand/design token system, writes the store/landing copy, and deploys to your domain.
- **`Jakeschincariol/founder-skill`: An 11-Skill Pre-Launch Business Stress-Tester with a 3-Framework Board and 100 Buyer Agents**
  - **First Principle**: Replace single-agent sycophancy with **adversarial framework sub-agents (`Board`)**, **heterogeneous multi-agent buyer simulation (`100-Buyer Panel`)**, and **closed-loop unit economics (`Ops → CFO`)**.
  - **Three Core Mechanisms**:
    1. **Three-Framework Board of Directors (`/founder-board` & `/founder-competitors`)**: Three independent sub-agents apply Hormozi's *Offers*, Thiel's *Monopoly*, and Jobs's *Product* frameworks to score the business, identify fatal flaws, and vote alongside a citation-linked competitor scout.
    2. **100-Buyer Consumer Panel & Iterative Offer Re-Testing (`/founder-consumer`, `/founder-pricing`, `/founder-offer`)**: Spawns 100 target-customer buyer agents—each with its own income, habits, and objections—to tally who buys and why others reject; `/founder-offer` builds guarantees/bonuses to answer those objections and re-runs the 100-buyer panel to verify conversion lift.
    3. **Ops-Fed CFO Unit Economics & 30-Day Launch Run Sheet (`/founder-ops`, `/founder-cfo`, `/founder-marketing`, `/founder-launch`, `/founder-plan`)**: Feeds real supplier/staffing/tooling costs from Ops into the CFO model to compute contribution margin, daily break-even, 12-month cash flow, max CAC, and a dated 30-day launch plan.

### Q2: What pain points do they solve compared to existing tools?

- **vs. One-Shot "Clone App X" Prompts**: Prevents missing database constraints, half-baked flows, and copyright/trademark contamination via a stateful 11-step `replica/` artifact pipeline and `/replica-diff` scoring.
- **vs. Generic ChatGPT SWOT / Business Plan Prompts**: Replaces polite generic advice with a 3-framework voting Board, 100 simulated buyer agents, and a unit-economics CFO model.

### Q3: How should an AI Solution Architect combine them?

- Run `/replica-recon` and `/replica-entrepreneur` from **`replica-skill`** to map an incumbent SaaS category and extract user complaints, validate the differentiated offer and unit economics through **`founder-skill`** (`/founder-board`, `/founder-consumer`, `/founder-cfo`), and then execute `/replica-architect` through `/replica-deploy`.

---

## 🧭 3. Mermaid Decision Tree & 22-Skill Product-to-Market Architecture

```mermaid
flowchart TD
    Start["🚀 AI SA Clean-Room SaaS Engineering & Pre-Launch Validation"] --> Stage{"What is the immediate objective?"}

    Stage -->|"Clean-Room Reverse-Engineering, Parity Build & Complaint Fixing<br/>(Needs 11-step replica/ pipeline + /replica-entrepreneur)"| Replica["🧬 Jakeschincariol/replica-skill (★ 9,343 · MIT)<br/>11 Chained Claude Skills · Python 3.8+"]
    Stage -->|"Pre-Launch Stress-Testing, Pricing & Unit Economics<br/>(Needs 3-framework Board + 100 buyer agents + CFO)"| Founder["🏛️ Jakeschincariol/founder-skill (★ 3,647 · MIT)<br/>11 Chained Claude Skills · Python 3.8+"]

    Replica --> R1["1. /replica-recon & architect: Map Screens, Flows & DB Constraints"]
    R1 --> R2["2. /replica-design, build & backend: Clean-Room UI + Auth/Stripe"]
    R2 --> R3["3. /replica-test & diff: E2E Flow Testing + Quantitative Parity Score"]
    R3 --> R4["4. /replica-entrepreneur, brand, launch & deploy: Fix User Complaints"]

    Founder --> F1["1. /founder-board & competitors: Hormozi/Thiel/Jobs Vote + Scout"]
    F1 --> F2["2. /founder-consumer: Run 100 Buyer Agents (Incomes/Objections)"]
    F2 --> F3["3. /founder-pricing & offer: Address Objections & Re-Test 100 Buyers"]
    F3 --> F4["4. /founder-ops, cfo & plan: Unit Economics, Break-Even & 30d Launch"]

    R4 --> Out["✅ Differentiated Clean-Room SaaS + 100-Buyer Validated Unit Economics<br/>Saves $5,137.50/mo (-92.48%)"]
    F4 --> Out
```

---

## 📊 4. Peer Comparison Matrix

| Dimension | `Jakeschincariol/replica-skill` (`★ 9,343`) | `Jakeschincariol/founder-skill` (`★ 3,647`) | Single-Prompt App Clones | Manual Teardowns & Surveys |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Role** | **11-Skill Clean-Room App Cloner & Differentiator** | **11-Skill Board, 100-Buyer Panel & CFO Simulator** | Ad-Hoc UI Code Generation | Spreadsheets & Paid Consumer Panels |
| **Multi-Stage Depth** | **Stateful `replica/` artifacts (`recon.md`, `features.csv`, `diff`)** | **3-Framework Board + 100 Buyer Sub-Agents + Ops-to-CFO** | Stateless single-turn output | Weeks of manual coordination |
| **Closed-Loop Validation** | **`/replica-test` + `/replica-diff` parity score + `/replica-entrepreneur`** | **Re-tests revised offers on the 100-buyer swarm** | None | Static survey results |
| **Legal & Setup Footprint** | **MIT License; enforces clean-room rules; 0 `pip` deps** | **MIT License; Python 3.8+ stdlib only; 0 API keys** | High risk of copying proprietary assets | Expensive agency/panel fees |

---

## 💰 5. Closed-Form FinOps Quantitative Audit

- **Claim ID**: `CLAIM-20261114-R114-REPLICASKILL-FOUNDERSKILL`
- **Workload Baseline**: `25` competitive SaaS teardown, clean-room prototyping, and 100-buyer pre-launch validation sprints/month (`$95/hr` engineering/architect rate; local workstation hardware: `not_measured`):
  - **Path A (Unguided Single-Prompt Cloning Rewrites + Unvalidated Launch/Ad Spend)**:
    - Wasted code-gen retries, unvalidated ad tests & research tool spend: `$1,850.00 / mo`
    - Manually mapping competitor flows, fixing missing DB constraints & reworking failed offers: `39.0 hrs/mo × $95.00 = $3,705.00 / mo`
    - **Path A Total Monthly Cost**: `$1,850.00 + $3,705.00 = $5,555.00 / mo`
  - **Path B (Manual Competitor Spreadsheets + Single-Prompt Business Plans)**:
    - Token & tool spend: `$820.00 / mo`
    - Manual review mining, financial spreadsheet modeling & QA labor: `17.0 hrs/mo × $95.00 = $1,615.00 / mo`
    - **Path B Total Monthly Cost**: `$820.00 + $1,615.00 = $2,435.00 / mo`
  - **Path C (`Jakeschincariol/replica-skill` 11-Stage Pipeline + `Jakeschincariol/founder-skill` 100-Buyer Panel)**:
    - Structured skill and sub-agent execution token spend ($0 license or third-party API fees): `$85.00 / mo`
    - Architect review of `replica/recon.md`, `/replica-diff` parity scores & `/founder-cfo` models: `3.5 hrs/mo × $95.00 = $332.50 / mo`
    - **Path C Total Monthly Cost**: `$85.00 + $332.50 = $417.50 / mo`
  - **Net FinOps Savings**:
    - **Monthly Savings vs. Path A**: `$5,555.00 - $417.50 = $5,137.50 / mo` (**`92.48%` reduction**)
    - **Annualized Savings**: `$5,137.50 × 12 = $61,650.00 / yr`
    - **Engineering Hours Saved**: `39.0h → 3.5h` (`35.5 hrs/mo` saved, **`91.03%` reduction**)

---

## 🛠️ 6. Actionable Quickstart Checklist

- [ ] **Step 1: Install `Jakeschincariol/replica-skill` and run the 11-stage clean-room pipeline**
  ```bash
  git clone https://github.com/Jakeschincariol/replica-skill.git
  cp -r replica-skill/replica-* ~/.claude/skills/
  ```
  - Run `/replica-recon` through `/replica-diff` and `/replica-entrepreneur` to map flows, score parity, and fix incumbent user complaints.
- [ ] **Step 2: Install `Jakeschincariol/founder-skill` and run the Board + 100-Buyer Panel**
  ```bash
  git clone https://github.com/Jakeschincariol/founder-skill.git
  cp -r founder-skill/skills/founder-* ~/.claude/skills/
  ```
  - Execute `/founder-board`, `/founder-consumer` (100 buyer agents), `/founder-pricing`, `/founder-offer`, and `/founder-cfo` before launching.
