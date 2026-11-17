# 11-Skill B2B Pre-Sale Validation Pipeline (`Jakeschincariol/whale-skill`) & 161-Skill Cross-Platform E-Commerce AI Navigator (`zarockfat/zgg-find-ecommerce-skills`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 38 (Cumulative Round 462)  
> **Tracked Repositories**:
> - **`Jakeschincariol/whale-skill`** (`★ 76`, Python 3.8+ zero-dependency `board.py` + 11 Coordinated Claude Skills, `MIT`): End-to-end B2B customer discovery and pre-sale validation suite (`market-researcher`, `demo-builder`, `whale-hunter`, `pre-sale`, `requirements`, `offer-builder`, `pricing`, `follow-up`, `objection-handler`, `case-study`, `launch-planner`) where nothing is ever sent or charged without explicit human approval
> - **`zarockfat/zgg-find-ecommerce-skills`** (`★ 93`, 161 Curated E-Commerce AI Skills + Offline-Capable Local Web Navigator, `MIT`): Cross-platform e-commerce AI skill discovery hub indexing **161 open-source skills** across Amazon, TikTok Shop, Shopee, Shopify, Temu, and 1688 with explicit fee/prerequisite transparency and multi-client installers (`Codex`, `Claude Code`, `Qwen Code`, `Kimi`, `TRAE`, `WorkBuddy`)  
> **Audit Claim ID**: `CLAIM-20261117-R38-WHALESKILL-ZGGECOM` (base LLM subscriptions & Stripe processing fees marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Enterprise AI Ventures, Solution Architects, and Cross-Border E-Commerce Teams Lose Months to Two Commercial Traps: Unvalidated Feature Builds and Opaque E-Commerce Skill Sprawl**:
   - **Trap 1 — The Build-First Speculation Trap**: Engineering teams routinely spend months building full backend pipelines before testing whether B2B buyers will actually pay for the solution, or send cold text pitches without a clickable interactive prototype or source-verified ROI numbers.
   - **Trap 2 — E-Commerce Skill Sprawl & Hidden Paid-API Lock-In**: Retail and cross-border e-commerce teams operating on Amazon, TikTok Shop, Shopee, Shopify, Temu, and 1688 struggle to discover reliable open-source AI skills for product research, listing copy, hero visuals, and affiliate vetting—often wasting hours installing a skill only to discover it requires an expensive proprietary API key.
   - **The Solution Architect & GTM Stack (`whale-skill` MIT + `zgg-find-ecommerce-skills` MIT)**: Standardize pre-launch B2B validation on **`Jakeschincariol/whale-skill`** (`MIT`, chaining 11 skills via a zero-dependency `market-researcher/board.py` tracker to research source-backed enterprise pain points, build clickable demos, and collect human-approved Stripe pre-sales whose requirements drive the actual build); and equip retail/commerce teams with **`zarockfat/zgg-find-ecommerce-skills`** (`MIT`, indexing **161 e-commerce skills** with an offline-capable local web catalog that explicitly flags paid API requirements before installation).
2. **Closed-Form FinOps Impact (25 B2B AI Solution Architects, Growth Engineers & E-Commerce Leads Running 1,500 Monthly Pre-Sale Validation & Skill Selection Workflows at `$95.00/hr`)**:
   - Migrating from **Path A (Speculative Unvalidated Builds + Paid Outbound/E-Commerce SaaS Trials & Manual Skill Vetting at `$5,670.00/mo`)** to **Path C (`whale-skill` 11-Skill Pipeline + `zgg-find-ecommerce-skills` 161-Skill Hub at `$341.00/mo`)** saves **`$5,329.00/mo` (`-93.99%`, or `$63,948.00/yr`)** while cutting speculative prototype rework and skill-vetting labor from `36.0 hrs/mo` to `2.8 hrs/mo` (**`92.22%` reduction**).

![Whale-Skill + ZGG E-Commerce Skills Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r38-whale-skill-zgg-ecommerce.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `Jakeschincariol/whale-skill` connect source-cited market research, clickable demos, and human-approved Stripe pre-sales into a single 11-skill loop?
- **Plain-Language Definition**: `whale-skill` (`MIT`, Python 3.8+ standard library `board.py`) is an **11-skill commercial validation pipeline that gets B2B customers to validate and pre-pay for a solution before you spend months engineering the wrong product**.
- **Three Architectural Pillars**:
  1. **11 Specialized Skills Sharing `market-researcher/board.py`**:
     - *Discovery & Prototype*: `market-researcher` (finds problems businesses already pay thousands to solve, requiring a verifiable source for every number) → `demo-builder` (builds a clickable interactive demo showing how your product solves the problem) → `offer-builder` & `pricing`;
     - *Outreach, Pre-Sale & Spec*: `whale-hunter` (identifies decision-makers and drafts pitches) → `pre-sale` (collects upfront payment and converts buyer requirements into the engineering spec) → `requirements` → `follow-up`, `objection-handler`, `case-study`, and `launch-planner`;
  2. **Strict Human Approval Gate ("Nothing Sent or Charged Without Your Yes")**: Integrates with your own Gmail and Stripe connectors—Claude drafts outreach and checkout flows, and a human explicitly approves every outbound action;
  3. **Zero-Dependency Portability**: Works as a Claude Code plugin (`/plugin install whale-skill@whale-skill`), local `~/.claude/skills/` folders, or even a single pasted `SKILL.md` in a web chat.

### Q2: How does `zarockfat/zgg-find-ecommerce-skills` index 161 e-commerce AI skills with explicit fee transparency and offline local web navigation?
- **161 Curated Skills Across 6 Major Commerce Platforms (`Amazon`, `TikTok Shop`, `Shopee`, `Shopify`, `Temu`, `1688`)**:
  - Organizes scattered open-source skills by platform and operational job-to-be-done: product selection & 1688 sourcing, listing title/bullet optimization, hero product imagery & short video creation, TikTok Shop creator/affiliate screening, and ad analytics/customer support.
- **Three Enterprise-Ready Features**:
  1. **Fee & Prerequisite Transparency**: Explicitly labels whether each skill is 100% free or requires paid third-party APIs—allowing prompts like *"recommend 1688 sourcing skills that do not require paid APIs and flag any unclear costs"*;
  2. **Bundled Offline-Ready Local Web Catalog**: Ships a local browser UI (`docs/images/homepage.png`) that works offline or on restricted corporate networks without registration;
  3. **Multi-Client Installation & Zero-Daemon 24h Sync**: Generates install commands for Codex (`npx skills add ...`), Claude Code, Qwen Code, Kimi Code CLI, TRAE, and WorkBuddy, checking for catalog updates at most once per 24 hours during active use with zero background processes.

### Q3: How should an AI Solution Architect combine `whale-skill` and `zgg-find-ecommerce-skills`?
- **B2B Solution Incubation (`whale-skill`)**: Require every new AI vertical initiative to pass `market-researcher` + `demo-builder` + `pre-sale` validation before allocating multi-month sprint capacity.
- **Retail & E-Commerce Automation (`zgg-find-ecommerce-skills`)**: Deploy the 161-skill navigator as the internal skill catalog for commerce operations teams, filtering strictly for fee-transparent open-source skills.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph B2BValidation["B2B Pre-Sale Validation Loop: Jakeschincariol/whale-skill (★76, MIT)"]
        A[New B2B AI Initiative] --> B[market-researcher: Source-Cited Pain Points<br/>+ Shared Zero-Dep board.py Tracker]
        B --> C[demo-builder + offer-builder + pricing<br/>Clickable Interactive Demo &amp; Tiered Offer]
        C --> D[whale-hunter + pre-sale + Human Approval Gate<br/>Drafts in Own Gmail / Stripe · Sent Only After Human Yes]
        D --> E[requirements + case-study + launch-planner<br/>Paid Customer Requirements Drive Engineering Build]
    end

    subgraph EcommerceHub["161-Skill E-Commerce Navigator: zarockfat/zgg-find-ecommerce-skills (★93, MIT)"]
        F[Amazon / TikTok Shop / Shopee / Shopify / Temu / 1688] --> G[Offline Local Web UI + Natural-Language Skill Search<br/>Sourcing · Listing Copy · Visuals/Video · Creator Vetting · Ad Ops]
        G --> H[Explicit Paid-API &amp; Prerequisite Filter<br/>Prioritizes Free Open-Source Skills + Multi-Client Install]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Speculative Builds + Paid Outbound/E-Commerce SaaS Trials | Option B: Ad-Hoc Cold Prompts + Raw GitHub Keyword Searches | **Option C (Recommended): `whale-skill` (11 Skills MIT) + `zgg-find-ecommerce-skills` (161 Skills MIT)** |
| :--- | :--- | :--- | :--- |
| **Pre-Build Demand Validation & Clickable Demos** | ❌ Months of coding before testing buyer willingness to pay | ⚠️ Disconnected prompts with no shared board or pre-sale spec loop | ✅ **11 skills sharing `board.py`: source-cited research + clickable demo + Stripe pre-sale** |
| **Outbound Email & Checkout Safety** | ⚠️ Third-party automated sequencers risk domain reputation | ⚠️ Manual copy-paste across disconnected tools | ✅ **Nothing sent or charged without human approval via your own Gmail & Stripe** |
| **Cross-Platform E-Commerce Skill Discovery & Fee Clarity** | ❌ Expensive per-seat SaaS lock-in across platforms | ❌ Hours wasted installing repos that secretly require paid API keys | ✅ **161 indexed skills across 6 platforms with explicit fee/prerequisite disclosure** |
| **Offline Catalog Access & Multi-Client Support** | ❌ Cloud-only SaaS portals | ❌ Manual folder conversion across coding agents | ✅ **Bundled offline local web UI + installers for Codex, Claude, Qwen, Kimi & WorkBuddy** |
| **Monthly TCO (25 SAs & Leads / 1,500 Workflows)** | **`$5,670.00 / mo`** (`$2,250` SaaS trials + `36.0 hrs` speculative work) | **`$2,410.00 / mo`** (`$890` tools + `16.0 hrs` manual vetting) | **`$341.00 / mo`** (**`-93.99%` savings**; `$75` static demo hosting + `2.8 hrs` human approval) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R38-WHALESKILL-ZGGECOM`)

> **Scope & Boundary Declaration**: Evaluated for 25 B2B AI solution architects, growth engineers, and e-commerce leads executing **1,500 monthly B2B pre-sale validation, clickable demo, and cross-platform e-commerce skill workflows** at a blended rate of `$95.00/hr` (base LLM subscriptions & Stripe processing fees marked `not_measured`):

$$\text{Total Monthly TCO} = \text{SaaS Trial \& Prototype Hosting Spend} + (\text{Unvalidated Demo \& Skill-Vetting Hours} \times \$95.00)$$

| Cost Component | Path A: Speculative Builds + SaaS Trials | Path B: Ad-Hoc Prompts + GitHub Search | **Path C: `whale-skill` + `zgg-find-ecommerce-skills`** |
| :--- | :---: | :---: | :---: |
| **Monthly Outbound/E-Commerce SaaS Trials & Demo Hosting** | `$2,250.00` | `$890.00` | **`$75.00`** |
| **Monthly Unvalidated Prototype Rework & Skill Vetting Hours** | `36.0 hrs` | `16.0 hrs` | **`2.8 hrs`** (**`92.22%` reduction**) |
| **Monthly SA & E-Commerce Engineering Labor (`@ $95.00/hr`)** | `$3,420.00` | `$1,520.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,670.00`** | **`$2,410.00`** (`-57.50%`) | **`$341.00`** (**`-93.99%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,260.00 / mo` (`$39,120/yr`) | **`$5,329.00 / mo` (`$63,948.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Install `Jakeschincariol/whale-skill` & Initialize `market-researcher/board.py`**: Add all 11 skills via `/plugin install whale-skill@whale-skill` or copy them into `~/.claude/skills/`, and run `market-researcher` + `demo-builder` to produce source-backed pain-point analysis and a clickable prototype before committing sprint capacity.
- [ ] **Step 2 — Gate Outbound Pitches & Pre-Sales via Gmail/Stripe Approval**: Use `whale-hunter`, `offer-builder`, `pricing`, and `pre-sale` to draft customer proposals, approve every outbound message manually, and convert paid pre-sale commitments into engineering specs with `requirements`.
- [ ] **Step 3 — Deploy `zarockfat/zgg-find-ecommerce-skills` & Launch the Offline Web Catalog**: Run `npx skills add zarockfat/zgg-find-ecommerce-skills --skill zgg-find-ecommerce-skills` to browse all 161 skills across Amazon, TikTok Shop, Shopee, Shopify, Temu, and 1688.
- [ ] **Step 4 — Filter E-Commerce Skills by Fee Transparency**: Prompt `$zgg-find-ecommerce-skills` to prioritize zero-API-fee open-source skills and explicitly flag any skill requiring paid external API credentials.
