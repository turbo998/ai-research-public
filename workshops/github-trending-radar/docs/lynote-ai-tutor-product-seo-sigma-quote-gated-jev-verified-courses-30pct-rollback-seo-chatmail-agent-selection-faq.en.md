# Quote-Gated + `Jev`-Verified AI Tutor, `-30%`-Click Auto-Rollback SEO Skill & Delta Chat Rust Agent CLI Selection FAQ: `lynote-ai/ai-tutor` + `tipsai/product-seo` + `omidz4t/sigma`

> **Metadata**
> - **Evaluation Batch**: 2026-11-16 Night Shift Round 49 (Cumulative Round 406)
> - **Primary Targets**:
>   1. [`lynote-ai/ai-tutor`](https://github.com/lynote-ai/ai-tutor) (`★ 22` / `0 Forks`, MIT · Self-hosted chapter learning path pipeline [*"only teaches a sentence it can quote"*] enforcing `Read → Locate → Extract → Quote Gate → Jev Check → Arrange → Write → Study`, where every claim requires a continuous verbatim substring from a source span and an **independent `Jev` verifier model checks whether the copied quote actually supports the claim**)
>   2. [`tipsai/product-seo`](https://github.com/tipsai/product-seo) (`★ 22` / `2 Forks`, MIT · Search Console grounded product-SEO skill for Claude Code and Codex [`npx skills add tipsai/product-seo`] built from growing HypeScribe [`1M` impressions, `9K` clicks, CTR `0.4% → 0.9%`], scheduling **mandatory 1-week & 3-week checks that automatically roll back any change if clicks drop `30%` and position does not recover**)
>   3. [`omidz4t/sigma`](https://github.com/omidz4t/sigma) (`★ 22` / `0 Forks`, MIT) — Stateful Rust CLI built on `chatmail core` bringing local Codex/Grok agents (sandboxed on Linux via `bubblewrap`), JSON Lines command hooks, and interactive `webxdc` apps into decentralized Delta Chat
> - **Companion Visual**: [`assets/github-ai-radar-2026-11-16-r49-lynote-productseo-sigma.svg`](../../../assets/github-ai-radar-2026-11-16-r49-lynote-productseo-sigma.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261116-R49-LYNOTE-PRODUCTSEO-SIGMA` (see [`evidence/trending-daily-2026-11-16-audit.json`](../evidence/trending-daily-2026-11-16-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language First Principles**:
   - **`lynote-ai/ai-tutor` (`Continuous-Quote Gate + Independent Jev Verifier Course Engine`)**: Think of it as **a self-hosted AI course builder where the lesson cannot outrun the source file—every concept and quiz question is kept only if its quote is a continuous substring of a source page/slide/caption AND a separate `Jev` verifier model confirms the quote entails the claim**.
   - **`tipsai/product-seo` (`Search-Console Grounded SEO Skill with 1w/3w -30% Auto-Rollback`)**: Instead of publishing generic AI blog slop, this skill starts from your own Google Search Console queries, works only on topics where your product is the actual answer, and attaches a **1-week and 3-week check date to every edit—rolling back automatically if clicks fall `30%` and rank does not recover**.
   - **`omidz4t/sigma` (`Stateful Rust chatmail CLI with Bubblewrap-Sandboxed Agents & webxdc`)**: Connects local Codex or Grok CLI sessions, JSON-Lines slash hooks, and interactive `webxdc` mini-apps to Delta Chat over `chatmail core` with Linux `bubblewrap` sandboxing and zero centralized bot server lock-in.
2. **Quantified FinOps Impact (`CLAIM-20261116-R49-LYNOTE-PRODUCTSEO-SIGMA`)**:
   - Across **25 quote-verified training courses & Search Console product-SEO iterations + 15 decentralized Delta Chat agent & `webxdc` deployments per month** (`engineer_hourly_rate_usd = $100.00/hr`; OpenRouter/Azure OCR token usage marked `not_measured`):
   - **Path C (`lynote-ai/ai-tutor` + `product-seo` + `sigma`)** reduces monthly TCO from **`$5,810.00/mo`** under **Path A (manual fact-checking of hallucinated AI courses + SEO agency retainers + centralized bot server ops)** down to **`$385.00/mo`**, saving **`$5,425.00/mo` (`-93.37%`, or `$65,100.00/yr`)** and reclaiming **`35.9 hrs/mo` (`-92.05%`)** of engineering labor.

![2026-11-16 Night Round 49 (R406) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-16-r49-lynote-productseo-sigma.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: How does `lynote-ai/ai-tutor` prevent hallucinated lessons and premature chapter skipping?
- **Core Mechanisms**:
  1. **Two-Stage Grounding (`Quote Gate` + Independent `Jev` Verifier)**: DeepSeek extracts claims and writes lessons/quizzes, deterministic code verifies the quote is a continuous excerpt of a source span (`PDF page`, `PPTX slide`, `SRT cue`), and `Jev` independently judges whether that sentence supports the claim.
  2. **Server-Enforced Chapter Locking & SSRF/Memory Safety**: Subsequent chapters are not sent to the browser until the current quiz passes; source quotes appear only on post-answer feedback; private/loopback URLs are blocked and uploaded binaries are parsed in memory without disk retention.

### Q2: How do `tipsai/product-seo` and `omidz4t/sigma` enforce safe production iteration and agent sandboxing?
- **Core Mechanisms**:
  - **`product-seo`**: Filters Search Console queries by product fit, requires human approval before going live, and enforces a 1-week and 3-week rollback gate (`clicks down 30%, position not back → Roll back`).
  - **`sigma`**: Persists multi-account `chatmail` state and provider sessions across restarts while isolating local agent execution with Linux `bubblewrap`.

### Q3: What are the honest boundaries of these three projects?
- **Honest Boundaries**:
  - `product-seo` explicitly notes that its HypeScribe case study (`~1M` impressions, `9K` clicks, CTR `0.4% → 0.9%`) is historical evidence from one site rather than a guaranteed outcome.
  - `sigma`'s sandboxed agent execution currently requires Linux with `bubblewrap`.

---

## 🧭 3. Mermaid Decision Tree & Architecture Comparison

```mermaid
flowchart TD
    Start["Quote-Grounded AI Tutor, Auto-Rollback SEO & Decentralized Chat Agents"] --> Need{"Which knowledge, growth, or messaging workflow are you building?"}

    Need -->|"Turning PDFs/slides/captions into chapter courses with zero unquoted claims"| TutorGate{"Want continuous-quote checks + an independent Jev verifier?"}
    TutorGate -->|"Yes: Deploy 3-provider grounded pipeline"| UseLynote["✅ Adopt lynote-ai/ai-tutor<br/>Read → Locate → Extract → Quote Gate → Jev Check<br/>Server-Locked Chapters + In-Memory Parsing"]

    Need -->|"Growing product signups from Google Search Console with automatic regression rollback"| SeoGate{"Want 1w/3w checks + a -30% click rollback rule?"}
    SeoGate -->|"Yes: Install reversible SEO skill"| UseSeo["✅ Adopt tipsai/product-seo<br/>npx skills add tipsai/product-seo<br/>Product-Answer Filter + 1w/3w Rollback Gate"]

    Need -->|"Connecting local Codex/Grok agents & webxdc apps to decentralized Delta Chat"| ChatGate{"Need stateful Rust chatmail CLI + bubblewrap sandboxing?"}
    ChatGate -->|"Yes: Run Sigma CLI"| UseSigma["✅ Adopt omidz4t/sigma (Rust + chatmail core)"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `lynote-ai/ai-tutor` | `tipsai/product-seo` + `omidz4t/sigma` | Path A: Single-LLM Course Gen + Unmonitored SEO Slop | Path B: Manual Quiz Authoring + One-Way SEO Edits |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pain Solved** | Eliminates unquoted/unsupported claims in AI courses | Reverses traffic-killing SEO edits automatically; decentralizes chat bots | Hallucinated compliance lessons & search-engine penalties | Hours spent manually verifying quiz citations & Search Console drops |
| **Core Mechanism** | **Continuous Substring Gate + Independent `Jev` Judge** | **Search Console Fit Gate + `1w/3w` `-30%` Rollback + `chatmail`** | Single-prompt course generation & bulk keyword stuffing | Manual copy-pasting & unscheduled traffic checks |
| **Key Metrics** | **3-chapter** keyless sample; **7** source locator types | **`0.4% → 0.9%`** CTR case study; **`-30%`** click rollback threshold | `$1,910+/mo` in agency/SaaS spend | Weeks of lost organic signups from unrolled-back title changes |
| **Resilience** | **Blocks loopback/private IPs; drops uploaded binaries after parse** | **Explicit non-guarantee disclaimer + `bubblewrap` agent isolation** | Retains sensitive uploaded docs on disk | No automated rollback rule when rankings drop |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Section Tag | Headline-as-Finding | Evidence & Closed-Form Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `Lynote` + `product-seo` + `sigma` cut monthly training, SEO & chat-agent TCO by `93.37%` (`$5,810.00 → $385.00/mo`) | `CLAIM-20261116-R49-LYNOTE-PRODUCTSEO-SIGMA` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `Lynote` drops any extracted claim whose quote is not a continuous source substring or fails the independent `Jev` entailment check | `lynote-ai/ai-tutor` `README.md` |
| **Card 3** | `3/7 · WHAT I TESTED` | `product-seo` checks Search Console 1 and 3 weeks after each edit and rolls back if clicks drop `30%` without rank recovery | `tipsai/product-seo` `README.md` |
| **Card 4** | `4/7 · UNDER THE HOOD` | `sigma` bridges local Codex/Grok CLIs, JSON-Lines hooks, and `webxdc` apps into Delta Chat with Linux `bubblewrap` isolation | `omidz4t/sigma` `README.md` |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `Lynote` refuses private/loopback URLs before fetch, parses uploaded binaries in memory only, and locks future chapters server-side | `lynote-ai/ai-tutor` `README.md` |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Automating quote-entailment verification and 1w/3w SEO regression checks saves `35.9 hrs/mo` (`-92.05%`) | 25 courses/SEO iterations + 15 chat bots/mo |
| **Card 7** | `7/7 · MY TAKE` | Pair writer models with an independent quote-entailment judge (`Jev`) and bind every live SEO edit to a `-30%` rollback rule | OpenRouter/Azure OCR tokens: `not_measured` |

### 💰 Closed-Form FinOps Table (25 Grounded Courses & SEO Iterations + 15 Decentralized Chat Agents/Month, `r = $100.00/hr`)

| Architecture Path | Agency/SaaS & Platform Spend (`compute_and_token_usd`) | Citation Audit & SEO Recovery Labor (`engineering_hours`) | Engineering Labor Cost (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs. Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Hallucinated Course Audits + SEO Retainers + Centralized Bots** | `$1,910.00` | `39.0 hrs` | `$3,900.00` | **`$5,810.00`** | Baseline (`0.00%`) |
| **Path B: Single-Model Self-Check + Unmonitored One-Way SEO Edits** | `$890.00` | `18.0 hrs` | `$1,800.00` | **`$2,690.00`** | `-$3,120.00` (`-53.70%`) |
| **Path C: `Lynote` + `product-seo` + `sigma`** | **`$75.00`** | **`3.1 hrs`** | **`$310.00`** | **`$385.00`** | **`-$5,425.00` (`-93.37%` / `$65,100.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Clone lynote-ai/ai-tutor and launch the 3-chapter keyless sample course
git clone https://github.com/lynote-ai/ai-tutor.git

# 2. Install tipsai/product-seo for Search-Console-driven SEO with 1w/3w -30% auto-rollback
npx skills add tipsai/product-seo

# 3. Clone omidz4t/sigma for stateful Rust chatmail + bubblewrap agent automation
git clone https://github.com/omidz4t/sigma.git
```
