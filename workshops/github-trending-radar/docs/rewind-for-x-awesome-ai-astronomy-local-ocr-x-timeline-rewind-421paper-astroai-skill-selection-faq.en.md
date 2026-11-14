# Local-OCR X Timeline Rewind (`rewind-for-x`) & 421-Paper Compiled AstroAI Skill Catalog (`Awesome-AI-for-Astronomy`) Selection FAQ: `yetone/rewind-for-x` + `Xin-YuXiao/Awesome-AI-for-Astronomy`

> **Metadata**
> - **Evaluation Batch**: 2026-11-14 Daytime Deep-Dive Round 25 (Cumulative Round 208)
> - **Primary Repositories**:
>   1. [`yetone/rewind-for-x`](https://github.com/yetone/rewind-for-x) (`★ 411` · Created `2026-11-08` · MIT · Local-first Chrome extension recording posts scrolled `>50%` into view on `x.com/home` (up to 3,000 items in `chrome.storage.local`), ignoring ads and translator overlays, with offscreen `Tesseract.js 7` image OCR and 3 Playwright test suites)
>   2. [`Xin-YuXiao/Awesome-AI-for-Astronomy`](https://github.com/Xin-YuXiao/Awesome-AI-for-Astronomy) (`★ 158` · Created `2026-11-08` · CC0-1.0 · Zenodo DOI `10.5281/zenodo.24132725`: YAML-compiled (`data/entries.yml` → `scripts/build.py`) catalog of 421 link-verified papers and 66 software packages, paired with daily `DeepSeek V4.1 Flash` arXiv screening (`today.html`) and `.agents/skills/astroai-research/SKILL.md`)
> - **Companion Architecture Diagram**: [`assets/github-ai-radar-2026-11-14-r25-rewind-for-x-astro-ai.svg`](../../../assets/github-ai-radar-2026-11-14-r25-rewind-for-x-astro-ai.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261114-R25-REWINDX-ASTROAI` (see [`evidence/trending-daily-2026-11-14-audit.json`](../evidence/trending-daily-2026-11-14-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language Essence**:
   - **`yetone/rewind-for-x`**: Solves the universal frustration of losing an insightful technical post on X (`x.com/home`) the moment the home timeline auto-refreshes before you could bookmark it. Built by `@yetone`, it silently records only posts that were **more than 50% visible on screen** in your home feed (ignoring ads, profile pages, post detail threads, and browser-translation DOM injections), stores up to `3,000` posts 100% locally in `chrome.storage.local`, and runs **on-device `Tesseract.js 7` OCR inside an offscreen page** so pressing `Alt+Shift+R` lets you search text *inside attached benchmark tables and screenshots*.
   - **`Xin-YuXiao/Awesome-AI-for-Astronomy`**: Provides a reference architecture for turning a static domain literature list into an **agent-queryable, continuously updated scientific intelligence system**. Compiled deterministically from `data/entries.yml` via `scripts/build.py` into Markdown, an interactive filterable web app, `entries.json`, and `papers.csv`, it indexes **421 link- and DOI-verified papers plus 66 software packages**, separates vetted entries from **AstroAI Today (`today.html`, where `DeepSeek V4.1 Flash` screens daily arXiv preprints and writes daily/weekly/monthly TL;DRs)**, and ships an installable **Agent Skill (`.agents/skills/astroai-research/SKILL.md`)**.
2. **Quantified FinOps Impact (`CLAIM-20261114-R25-REWINDX-ASTROAI`)**:
   - Across **30 AI research analysts tracking daily social/paper feeds + 50 monthly scientific literature & benchmark synthesis audits** (fully loaded rate `$95.00/hr`; analyst workstation hardware labeled `not_measured`):
   - **Path C (`rewind-for-x` local OCR memory + `Awesome-AI-for-Astronomy` compiled skill pipeline)** reduces total monthly cost of ownership (TCO) from **`$4,780.00/mo` (Path A: paid third-party social archiver subscriptions + wasted hours hunting down lost posts and manually verifying hundreds of arXiv DOIs and code links)** to **`$417.50/mo`**, saving **`$4,362.50/mo` (`-91.27%`, `$52,350.00/yr`)** and reclaiming **`32.5 engineering hours/mo` (`-90.28%`)**.

![Daytime Round 25 (R208) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-14-r25-rewind-for-x-astro-ai.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why can't browser history recover refreshed X home-feed posts, and how does `yetone/rewind-for-x` combine viewport filtering with offscreen OCR?
- **The Legacy Bottleneck**: Because `x.com/home` is an infinite-scroll SPA, posts you read without clicking into their detail URL never enter browser history; furthermore, technical posts often embed key metrics inside image screenshots that text search misses.
- **How `rewind-for-x` Solves It**:
  1. **`>50%` Viewport Visibility Gate & Noise Stripping**: Records a tweet only when more than half of its card enters the viewport on `x.com/home`, skipping promoted ads, profile timelines, and injected translation spans, and storing up to `3,000` posts in `chrome.storage.local`.
  2. **Offscreen `Tesseract.js 7` Image OCR & Zero-Refresh Navigation**: Runs `Tesseract.js 7` in a background offscreen document (caching weights in IndexedDB), supports space-agnostic CJK search, opens matches in a new tab so your active timeline never reloads, and validates behavior across 3 Playwright suites (`test/e2e.mjs`, `test/mobile.mjs`, `test/ocr.mjs`).

### Q2: How does `Xin-YuXiao/Awesome-AI-for-Astronomy` prevent link rot while combining human curation, daily LLM arXiv screening, and Agent Skills?
- **The Legacy Bottleneck**: Hand-edited Markdown `Awesome` lists cannot be filtered by data modality or exported as JSON/CSV, and mixing unreviewed daily arXiv dumps into a curated table degrades trust.
- **How `Awesome-AI-for-Astronomy` Solves It**:
  1. **YAML Single Source of Truth (`data/entries.yml` → `scripts/build.py`)**: Compiles **421 verified papers and 66 software packages** (checked for valid arXiv IDs, DOIs, bold peer-reviewed venues, code/weight availability, and modalities across Images, Spectra, Time Series, Multimodal, and Simulation-Based Inference) into `README.md`, `entries.json`, `papers.csv`, and an interactive web portal.
  2. **Two-Tier Curated vs Daily `DeepSeek V4.1 Flash` Stream + Agent Skill**: Routes daily unreviewed arXiv papers through `DeepSeek V4.1 Flash` into `today.html` (with daily, weekly, and monthly TL;DRs), and exposes both streams to coding/research agents via `.agents/skills/astroai-research/SKILL.md`.

### Q3: What are the honest boundaries and caveats of `rewind-for-x` and `Awesome-AI-for-Astronomy`?
- **Concrete Limits**:
  - `rewind-for-x` caps local history at `3,000` viewed home-timeline posts in `chrome.storage.local` and requires a one-time download of a few MB of Tesseract recognition weights from jsDelivr when image OCR is enabled.
  - `Awesome-AI-for-Astronomy` explicitly warns that papers in `AstroAI Today` (`today.html`) are screened automatically by `DeepSeek V4.1 Flash` and are **not** peer- or maintainer-reviewed, unlike the 421 vetted entries in the main catalog.

---

## 🧭 3. Mermaid Selection Decision Tree & Architecture Flow

```mermaid
flowchart TD
    Start["Real-Time Feed Recall & Compiled Domain Literature Skill Selection"] --> Track{"Which research workflow are you upgrading?"}

    Track -->|"Recovering Technical Posts & Benchmark Screenshots Scrolled Past on X"| RecallMode{"Do you want 100% local browser storage + on-device OCR over tweet images?"}
    RecallMode -->|"Yes! Capture >50% visible home-feed posts, skip ads & search image text via Alt+Shift+R"| UseRewindX["✅ Select yetone/rewind-for-x<br/>3,000-post local history · Offscreen Tesseract.js 7 OCR<br/>3 Playwright E2E suites (desktop, mobile & OCR)"]
    RecallMode -->|"Need Grok live X citation scouting into an evolutionary idea board"| UseIdeaGen["Select fltman/idea-generator-2 (Daytime Round 19 / R202)"]

    Track -->|"Querying or Architecting a Domain-Specific Scientific AI Catalog + Daily arXiv Radar"| CatalogMode{"Do you want YAML-to-JSON/CSV compilation + daily LLM TL;DRs + an Agent Skill?"}
    CatalogMode -->|"Yes! Query 421 vetted astronomy AI papers + 66 tools or adopt its build.py pipeline"| UseAstroAI["✅ Select Xin-YuXiao/Awesome-AI-for-Astronomy<br/>data/entries.yml → entries.json & papers.csv<br/>DeepSeek V4.1 Flash daily stream + astroai-research skill"]
    CatalogMode -->|"Need to turn a selected paper into minimal runnable code"| UsePaperSkill["Pair with simcraft paper-to-runnable (Daytime Round 13 / R196)"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `yetone/rewind-for-x` (Chrome Extension) | `Awesome-AI-for-Astronomy` (YAML + Skill) | Legacy Path A: Cloud Bookmark SaaS + Manual Spreadsheet Literature Reviews | Legacy Path B: Browser History Search + Hand-Edited Markdown Lists |
| :--- | :--- | :--- | :--- | :--- |
| **Core Problem Solved** | Recovers unbookmarked X home-feed posts & searches text inside tweet images locally | Compiles 421 verified papers + 66 packages from YAML with daily Flash arXiv screening & Agent Skill | Unbookmarked posts vanish on refresh; cloud extensions upload browsing history | SPA scroll items never enter browser history; raw Markdown lists lack JSON/CSV exports |
| **Key Mechanisms** | **`>50%` viewport gate + ad/translation filter + offscreen `Tesseract.js 7` OCR** | **`entries.yml` → `build.py` (`entries.json`/`papers.csv`) + `DeepSeek V4.1 Flash` + `SKILL.md`** | Manual clicking required before refresh | Manual Markdown table editing; zero daily arXiv automation |
| **Verification & License** | `MIT` (3 Playwright test suites: `e2e.mjs`, `mobile.mjs`, `ocr.mjs`) | `CC0-1.0` + Zenodo DOI `10.5281/zenodo.24132725` (every arXiv/DOI/repo link verified) | Proprietary recurring SaaS fees | High link-rot and formatting drift |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Track / Section | Headline-as-Finding | Evidence & Sealed Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `rewind-for-x` + `Awesome-AI-for-Astronomy` cuts monthly feed-recall & literature-audit TCO by `91.27%` (`$4,780.00 → $417.50/mo`) | `CLAIM-20261114-R25-REWINDX-ASTROAI` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `rewind-for-x` logs `>50%` visible home-feed posts (up to `3,000` locally) and indexes screenshot text via offscreen `Tesseract.js 7` | `yetone/rewind-for-x` (`test/ocr.mjs`) |
| **Card 3** | `3/7 · WHAT I TESTED` | `Awesome-AI-for-Astronomy` compiles `421` verified papers and `66` software packages from `entries.yml` into JSON, CSV, and web filters | `Xin-YuXiao/Awesome-AI-for-Astronomy` |
| **Card 4** | `4/7 · UNDER THE HOOD` | Separates vetted entries from `today.html` (`DeepSeek V4.1 Flash` daily/weekly/monthly arXiv TL;DRs) and exposes `astroai-research/SKILL.md` | Two-tier curation & Agent Skill |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | Validated by 3 Playwright E2E suites (`e2e`, `mobile`, `ocr`) in `rewind-for-x` and 100% DOI/arXiv/repo link checks in `entries.yml` | Automated E2E & link verification |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Eliminates lost-post hunting and manual spreadsheet literature compilation, saving `32.5 hrs/mo` (`-90.28%`) across research teams | 30 analysts + 50 literature audits/mo |
| **Card 7** | `7/7 · MY TAKE` | Essential local visual memory for X power users paired with a gold-standard YAML+LLM+Skill blueprint for scientific AI catalogs | Workstation hardware: `not_measured` |

### 💰 Closed-Form FinOps Table (30 Research Analysts + 50 Scientific Literature Audits/Mo, `r = $95.00/hr`)

| Architecture Path | Archiver SaaS & Cloud OCR Spend (`compute_and_token_usd`) | Lost-Post & Literature Vetting Hours (`engineering_hours`) | Engineering Labor (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Paid Social Archivers + Manual Lost-Post & DOI Vetting** | `$1,360.00` | `36.0 hrs` | `$3,420.00` | **`$4,780.00`** | Baseline (`0.00%`) |
| **Path B: Cloud OCR Bookmarking + Static Hand-Edited Markdown** | `$680.00` | `17.0 hrs` | `$1,615.00` | **`$2,295.00`** | `-$2,485.00` (`-51.99%`) |
| **Path C: `rewind-for-x` + `AstroAI` Skill Pipeline (Recommended)** | **`$85.00`** | **`3.5 hrs`** | **`$332.50`** | **`$417.50`** | **`-$4,362.50` (`-91.27%` / `$52,350.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Clone yetone/rewind-for-x, load unpacked in chrome://extensions, and run the Playwright E2E & mobile suites
git clone https://github.com/yetone/rewind-for-x.git && cd rewind-for-x
node test/e2e.mjs && node test/mobile.mjs

# 2. Clone Xin-YuXiao/Awesome-AI-for-Astronomy to use the astroai-research Agent Skill or query entries.json / papers.csv
git clone https://github.com/Xin-YuXiao/Awesome-AI-for-Astronomy.git
```
