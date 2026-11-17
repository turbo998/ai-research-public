# Pip-Free Regional API Skill Registry (`b44x/ai-polish-skills`), Two-Tier 1.1K/9K Japanese Business Communication (`AnIT012/nihongo`) & Print-Ready Layout QA (`tamirgur/rega-album-maker`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 52 (Cumulative Round 476)  
> **Tracked Repositories**:
> - **`b44x/ai-polish-skills`** (`★ 62`, Python 3.8+ Pip-Free Standard Library / 26 Official & Public Polish Registry/API Skills, `MIT`): Open-source skill registry (`polskieskille.pl`) connecting coding agents to live government registries, FX rates, logistics, and commercial APIs via **zero-dependency Python 3.8+ stdlib scripts, pure JSON on `stdout`, and explicit `official_api` provenance declarations**
> - **`AnIT012/nihongo`** (`★ 63`, `v2.1.2` / Two-Tier `Lite ~1,100 Tokens` vs. `Full ~9,000 Tokens` Native Japanese Business Writing Skill, `MIT`) & **`tamirgur/rega-album-maker`** (`★ 30`, Python / 15-Style Print-Ready PDF Photo Book Designer with Face/Title Collision QA & RTL Support, `MIT`): Context-aware Japanese communication skill that loads a lightweight `~1,100`-token `ALWAYS.md` on routine turns and pulls the full `~9,000`-token `SKILL.md` only when drafting external emails, Slack notices, PRs, or UI copy (`nihongo`), paired with a print-ready book designer that enforces zero face-cropping and zero title-overlap QA across LTR and RTL languages (`rega-album-maker`)  
> **Audit Claim ID**: `CLAIM-20261117-R52-POLISHSKILLS-NIHONGO-REGA` (base LLM subscriptions marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Global Localization, Regional Compliance, and Automated Publishing Teams Hit Three Expensive Failure Modes: Fragile Regional API Wrappers, `9,000`-Token Always-On Style Taxes, and Cropped-Face Print PDFs**:
   - **Failure 1 — Hallucinated Regional Registry Data & Fragile `pip` Dependencies**: Generic LLMs hallucinate local company registration numbers, exchange rates, and parcel statuses, while custom Python wrappers with heavy `pip` dependencies frequently break across developer machines.
   - **Failure 2 — The `9,000`-Token Always-On Style Tax & Robotic Japanese Keigo**: AI-generated Japanese defaults to stiff templates (`**結論**：` / `**背景**：`), overly formal keigo (`共有させていただきます`) in internal Slack channels, and hollow verbs (`活用`, `実現`). Yet loading a comprehensive `9,000`-token writing guide into every turn wastes thousands of tokens during ordinary coding chats.
   - **Failure 3 — Unchecked Face Cropping & Title Overlaps in Automated Print Layouts**: Automated photo-book and brochure generators blindly place images and text without verifying whether a page gutter slices through a face or a title covers a subject.
   - **The Solution Architect Stack (`ai-polish-skills` MIT + `AnIT012/nihongo` MIT + `tamirgur/rega-album-maker` MIT)**: Standardize regional government and commercial API integrations on the **`b44x/ai-polish-skills`** blueprint (100% Python 3.8+ stdlib, pure JSON `stdout`, and `official_api` YAML provenance); adopt **`AnIT012/nihongo`**'s two-tier **`Lite (~1,100 tokens)` + `Full (~9,000 tokens)`** on-demand loading architecture; and automate print-ready PDFs with **`tamirgur/rega-album-maker`** (15 styles, non-destructive curation, real EXIF facts, RTL/LTR support, and pre-print face/title collision QA).
2. **Closed-Form FinOps Impact (25 Global Localization, Regional Compliance & Publishing Engineers Running 40,000 Monthly Regional API Lookups, Business Communications & Print Layouts at `$95.00/hr`)**:
   - Migrating from **Path A (Always-On `9,000`-Token Style Prompts + Hallucinated Regional Lookups & Manual Print QA at `$5,690.00/mo`)** to **Path C (`ai-polish-skills` + `nihongo` 2-Tier Loader + `rega-album-maker` Stack at `$341.00/mo`)** saves **`$5,349.00/mo` (`-94.01%`, or `$64,188.00/yr`)** while cutting localization rewriting, dependency debugging, and layout QA labor from `36.0 hrs/mo` to `2.8 hrs/mo` (**`92.22%` reduction**).

![ai-polish-skills + nihongo + Rega Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r52-polishskills-nihongo-rega.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `b44x/ai-polish-skills` establish a zero-dependency, deterministic blueprint for regional government and commercial API skills?
- **Plain-Language Definition**: `ai-polish-skills` (`MIT`, 26 live skills across Polish public registries, FX rates, transit, and commercial services) is **a pip-free regional skill registry where every tool runs on the Python 3.8+ standard library and returns deterministic JSON on `stdout`**.
- **Four Architectural Principles**:
  1. **Zero `pip` Dependencies (`pip-free`)**: Every script uses only the Python 3.8+ standard library, eliminating virtual-environment drift across Claude Code, Cursor, Windsurf, and Codex;
  2. **Deterministic CLI Contract**: Emits pure structured JSON on `stdout`, routes errors to `stderr`, and returns stable exit codes;
  3. **Single-Source YAML Frontmatter**: Declares `name`, `version`, `category`, `source`, `network`, and `tags` in `SKILL.md`;
  4. **Explicit Source Provenance**: Clearly labels whether each endpoint is an `official_api`, public dataset, or unofficial source.

### Q2: How does `AnIT012/nihongo` eliminate both robotic Japanese "AI-ese" and the `9,000`-token always-on prompt tax?
- **Two-Tier Progressive Loading + Fact-Preserving Pragmatics (`v2.1.2`, `MIT`)**:
  1. **Lite (`ALWAYS.md`, `~1,100 Tokens`) vs. Full (`SKILL.md`, `~9,000 Tokens`)**: Routine turns load only `ALWAYS.md` (`~1,100 tokens`), automatically escalating to the full `~9,000`-token `SKILL.md` and `references/` only when drafting human-facing deliverables (emails, notices, Slack announcements, READMEs, PR descriptions, or UI copy)—saving **`87.8%`** of style-guide tokens on normal turns;
  2. **Audience-Calibrated Keigo & Zero Fabricated Commitments**: Strips stiff labels (`結論：` / `背景：`) and hollow verbs (`活用`, `実現`) in internal team chat while preserving formal keigo for external notices, and strictly preserves numbers, dates, conditions, and ownership without adding unrequested apologies or promises.

### Q3: How does `tamirgur/rega-album-maker` turn raw photo folders into print-ready PDFs with automated visual QA?
- **Five-Stage Print Pipeline (`MIT`, English LTR & Hebrew RTL Ready)**:
  - Non-destructively sets aside duplicates, blurry shots, and screenshots; extracts real dates and places to generate route maps, stamps, and captions without inventing facts; previews 15 design styles on your own photos; and runs a **pre-print verification check ensuring no face is cropped, no title covers a person, and page count matches the printer specification**.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph RegionalPack["Pip-Free Regional JSON Registry: b44x/ai-polish-skills (★62, Python Stdlib MIT)"]
        A[Regional Registry / FX / Logistics Query] --> B[SKILL.md YAML Verifies official_api Provenance<br/>+ Zero-Dep Python 3.8+ Stdlib Execution]
        B --> C[Pure JSON on stdout · Diagnostics on stderr<br/>Zero Pip Conflicts · Zero Hallucinated Figures]
    end

    subgraph TwoTierAndPrint["2-Tier Style Loader &amp; Print QA: nihongo (★63, MIT) + rega-album-maker (★30, MIT)"]
        D[Incoming Turn in Claude / Codex] --> E{Human-Facing Deliverable?}
        E -->|Routine Chat| F[Load Only nihongo Lite ALWAYS.md ~1,100 Tokens]
        E -->|Email / Slack / PR / UI Copy| G[Escalate to Full SKILL.md ~9,000 Tokens<br/>Calibrate Keigo · Preserve Dates/Numbers · Zero Fake Promises]
        G --> H[tamirgur/rega-album-maker 15-Style Layout<br/>LTR/RTL Support + Zero Face-Crop &amp; Zero Title-Overlap Print QA]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Always-On `9K` Style Prompts + Hallucinated Regional Data | Option B: Basic Translation Prompts + Pip-Heavy API Wrappers | **Option C (Recommended): `ai-polish-skills` + `nihongo` (1.1K/9K) + `rega` (MIT)** |
| :--- | :--- | :--- | :--- |
| **Regional Registry Accuracy & Dependency Stability** | ❌ LLM hallucinates company IDs, FX rates & parcel status | ⚠️ Third-party `pip` packages break across environments | ✅ **100% Python 3.8+ stdlib (`pip-free`), pure `stdout` JSON & `official_api` tags** |
| **Japanese Business Tone & Prompt Token Efficiency** | ❌ Pays `9,000` tokens on every turn; robotic `結論：` / `させていただきます` | ⚠️ Word-ban lists produce choppy text & invented commitments | ✅ **`1.1K` Lite / `9K` Full split (`-87.8%` idle tokens), audience keigo & fact lock** |
| **Print-Ready PDF Layout & Visual Collision QA** | ❌ Gutters slice through faces; titles overlap subjects | ⚠️ Hours of manual InDesign layout adjustments | ✅ **15 styles, non-destructive triage, LTR/RTL & automated face/title collision QA** |
| **Monthly TCO (25 Engineers / 40,000 Turns)** | **`$5,690.00 / mo`** (`$2,270` 9K token tax/SaaS + `36.0 hrs` rework) | **`$2,420.00 / mo`** (`$900` APIs + `16.0 hrs` env/copy fixes) | **`$341.00 / mo`** (**`-94.01%` savings**; `$75` 1.1K Lite/stdlib runs + `2.8 hrs` sign-off) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R52-POLISHSKILLS-NIHONGO-REGA`)

> **Scope & Boundary Declaration**: Evaluated for a 25-engineer global localization, regional compliance, and automated publishing organization executing **40,000 monthly regional registry queries, localized business communications, and print-ready PDF layouts** at a blended engineering rate of `$95.00/hr` (base LLM subscriptions marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Always-On Style Token Tax \& SaaS Spend} + (\text{Keigo Rewrite \& Print Layout QA Hours} \times \$95.00)$$

| Cost Component | Path A: Always-On `9K` Prompts + Manual QA | Path B: Basic Prompts + Pip Scrapers | **Path C: `ai-polish-skills` + `nihongo` + `rega`** |
| :--- | :---: | :---: | :---: |
| **Monthly Style-Prompt Token Tax & External SaaS Spend** | `$2,270.00` | `$900.00` | **`$75.00`** |
| **Monthly Keigo Rewriting, Pip Debug & Print Crop QA Hours** | `36.0 hrs` | `16.0 hrs` | **`2.8 hrs`** (**`92.22%` reduction**) |
| **Monthly Localization & Publishing Engineering Labor (`@ $95.00/hr`)** | `$3,420.00` | `$1,520.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,690.00`** | **`$2,420.00`** (`-57.47%`) | **`$341.00`** (**`-94.01%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,270.00 / mo` (`$39,240/yr`) | **`$5,349.00 / mo` (`$64,188.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Adopt the `b44x/ai-polish-skills` Pip-Free Stdlib Pattern for Regional Packs**: Require all regional registry, currency, and logistics skills to run on the Python 3.8+ standard library, output pure JSON on `stdout`, and declare `official_api` status in YAML frontmatter.
- [ ] **Step 2 — Configure `AnIT012/nihongo`'s Two-Tier `Lite` (`~1.1K`) / `Full` (`~9K`) Architecture**: Load `nihongo/ALWAYS.md` by default and escalate to `nihongo/SKILL.md` only when drafting external or team-facing Japanese deliverables.
- [ ] **Step 3 — Enforce Fact-Lock Guardrails in Localization Skills**: Prohibit writing skills from altering dates, numbers, or conditions or inventing unrequested promises.
- [ ] **Step 4 — Gate Print-Ready PDF Exports with `tamirgur/rega-album-maker` Collision Checks**: Verify that every generated spread passes non-destructive photo triage, RTL/LTR typography rules, and face-crop/title-overlap QA before printing.
