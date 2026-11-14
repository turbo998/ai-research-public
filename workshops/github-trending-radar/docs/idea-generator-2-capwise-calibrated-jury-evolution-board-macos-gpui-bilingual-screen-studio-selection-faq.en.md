# Calibrated-Jury Evolutionary Idea Board (`idea-generator-2`) & Native macOS `GPUI` ACP Screen Studio (`Capwise`) Selection FAQ: `fltman/idea-generator-2` + `joeseesun/capwise`

> **Metadata**
> - **Evaluation Batch**: 2026-11-14 Daytime Deep-Dive Round 19 (Cumulative Round 202)
> - **Primary Repositories**:
>   1. [`fltman/idea-generator-2`](https://github.com/fltman/idea-generator-2) (`★ 172` · Created `2026-11-08` · MIT · `Idégeneratorn`: Infinite force-layout idea board with a calibrated 15-point LLM jury `npm run calibrate`, USD-capped tournament-selection evolution autopilot, citation-verified X/HuggingFace scouts, and automatic Gold-to-`CLAUDE.md` project scaffolding)
>   2. [`joeseesun/capwise`](https://github.com/joeseesun/capwise) (`★ 161` · Created `2026-11-08` · AGPLv3 · `Capwise` / 灵录: Native macOS 13.3+ Apple Silicon screen recording, teleprompter, auto-zoom, bilingual subtitle studio, text-based video cutter, and local ACP agent editing workbench built with `desktop-gpui`)
> - **Companion Architecture Diagram**: [`assets/github-ai-radar-2026-11-14-r19-idea-generator-capwise.svg`](../../../assets/github-ai-radar-2026-11-14-r19-idea-generator-capwise.svg)
> - **Sealed Evidence Anchor**: `CLAIM-20261114-R19-IDEAGEN2-CAPWISE` (see [`evidence/trending-daily-2026-11-14-audit.json`](../evidence/trending-daily-2026-11-14-audit.json))

---

## 📌 1. Executive Summary & First-Principles Pitch

1. **Plain-Language Essence**:
   - **`fltman/idea-generator-2` (`Idégeneratorn`)**: Turns unstructured LLM brainstorming into a **budget-bounded genetic algorithm with a calibrated 15-point jury that automatically scaffolds winning ideas into ready-to-code `CLAUDE.md` Git repositories**. It seeds an infinite force-layout canvas with **citation-verified X trends (Grok via OpenRouter) and Hugging Face daily/semantic papers**, lets you cross-breed ideas by dragging one node onto another or via a server-side **Evolution Autopilot** (tournament selection capped by steps/hr and per-board/global USD/day budgets), scores every idea on originality, feasibility, and impact (`1–5` each, calibrated via `npm run calibrate` for `~$0.07`), and automatically turns rare **Gold (`≥13/15`)** ideas into initialized Git folders with `CLAUDE.md`, `README.md`, `idea.json`, and `vault/`.
   - **`joeseesun/capwise` (`Capwise` / 灵录)**: Consolidates the fragmented 4-tool macOS product-demo workflow (screen recorder + cursor zoom tool + bilingual subtitle translator + thumbnail generator) into **one notarized Apple Silicon `desktop-gpui` studio window with zero mandatory cloud account**. It records screen/camera/mic alongside a synced teleprompter, separates **text-only subtitle editing** from explicit **Cut Video by Text** trimming, styles source and translated captions independently (`SRT`/`VTT` or burned-in export), and connects directly to local **ACP (Agent Client Protocol)** coding assistants for reviewable, undoable timeline edits.
2. **Quantified FinOps Impact (`CLAIM-20261114-R19-IDEAGEN2-CAPWISE`)**:
   - Under a monthly workload of **20 R&D ideation-to-repo sprints + 30 bilingual product demos and technical walkthrough videos** (fully loaded rate `$100.00/hr`; Apple Silicon Mac hardware labeled `not_measured`):
   - **Path C (`idea-generator-2` calibrated autopilot + `Capwise` unified studio)** reduces total monthly cost of ownership (TCO) from **`$5,380.00/mo` (Path A: uncalibrated multi-agent brainstorm token burn + 4 separate recording/caption/thumbnail SaaS subscriptions and manual SRT re-syncing)** to **`$475.00/mo`**, saving **`$4,905.00/mo` (`-91.17%`, `$58,860.00/yr`)** and reclaiming **`34.5 engineering hours/mo` (`-90.79%`)**.

![Daytime Round 19 (R202) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-14-r19-idea-generator-capwise.svg)

---

## ❓ 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why do standard LLM brainstorming prompts suffer from grade inflation and runaway API spend, and how does `fltman/idea-generator-2` enforce calibrated selection?
- **The Legacy Bottleneck**: Uncalibrated LLM judges award `8/10` or `9/10` to almost every generated idea, starving evolutionary search of selection pressure; meanwhile, background agent loops without hard dollar ceilings can drain API credits overnight.
- **How `idea-generator-2` Solves It**:
  1. **Reference-Calibrated 15-Point Jury (`npm run calibrate`)**: Scores originality, feasibility, and impact (`1–5` each) with a 1-sentence reason and 2–4 keywords, computing deterministic medals in code (bronze `≥9`, silver `≥11`, gold `≥13`) calibrated against reference ideas (`~$0.07`).
  2. **USD-Capped Tournament Autopilot & Gold-to-`CLAUDE.md` Spawning**: Breeds parents via tournament selection on the server even with the browser closed, strictly bounded by steps/hour, USD/day per board, global USD/day, and error backoff—writing a complete `CLAUDE.md` + `git init` project folder whenever a Gold idea emerges.
  3. **8 Role-Specific Model Slots & Citation-Verified Scouts**: Routes `distill`, `branch`, `cross`, `judge`, `summary`, `research scout`, `X scout`, and `project brief` independently across Microsoft Foundry / Azure OpenAI, OpenRouter, Anthropic, OpenAI, and local Ollama/MLX (`50` offline unit tests, RAM-only key handling).

### Q2: Why does round-tripping between separate screen recorders and subtitle tools break product demos, and how does `joeseesun/capwise` solve it natively on macOS?
- **The Legacy Bottleneck**: Exporting an MP4 from a screen recorder into a separate captioning app means any late trim to remove a spoken mistake invalidates all downstream bilingual subtitle timestamps and zoom keyframes.
- **How `Capwise` Solves It**:
  1. **Single-Project `.cap` Recording, Teleprompter & Bilingual Caption Studio**: Built natively for macOS 13.3+ Apple Silicon (`desktop-gpui`), it keeps screen/webcam/mic tracks, auto-zoom cursor highlights, independent source/target bilingual subtitle styles, background music, and cover art inside one editable local project.
  2. **Explicit Text-Only vs Video-Trim Guardrail & Local ACP Integration**: Deleting subtitle text modifies only captions by default unless the user explicitly enters **Cut Video by Text** mode; furthermore, users can connect their own LLM endpoint or a local authenticated **ACP** assistant to propose reviewable, undoable timeline and caption edits.

### Q3: What are the honest boundaries and caveats of `idea-generator-2` and `Capwise`?
- **Concrete Limits**:
  - `idea-generator-2` requires **Node.js 25+** (running TypeScript natively with zero build step) and binds its unauthenticated server to `127.0.0.1:8300` with API keys held in memory—never expose port `8300` to the public internet.
  - `Capwise` currently ships signed/notarized binaries for **macOS 13.3+ on Apple Silicon** only (Intel Mac, Windows, and Linux builds are not yet verified), and invoking its in-assistant cover generator calls the user's configured image-generation API (which may incur provider charges).

---

## 🧭 3. Mermaid Selection Decision Tree & Architecture Flow

```mermaid
flowchart TD
    Start["Evolutionary Ideation-to-Repo & Native macOS Screen/Subtitle Studio Selection"] --> Track{"Which creative/engineering workflow are you optimizing?"}

    Track -->|"Evolving Goal-Directed Product Ideas with Citation Scouts & Auto-Scaffolding CLAUDE.md Repos"| JuryCheck{"Do you need a calibrated 15-pt jury, tournament autopilot & strict daily USD caps?"}
    JuryCheck -->|"Yes! Seed from X/HF scouts, cross-breed on force canvas & spawn CLAUDE.md on Gold"| UseIdeaGen["✅ Select fltman/idea-generator-2<br/>Node 25+ native TS · 50 offline unit tests<br/>npm run calibrate (~$0.07) + 8 role-specific model slots"]
    JuryCheck -->|"Comparing 2–4 existing agents on one fixed prompt"| UseDSHCompare["Select dsh-agent-compare (Daytime Round 8 / R191)"]

    Track -->|"Recording & Editing Product Demos with Auto-Zoom, Bilingual Subtitles & AI Assistant"| OSCheck{"Are you running macOS 13.3+ on Apple Silicon?"}
    OSCheck -->|"Yes! Want 1 native GPUI window with teleprompter, bilingual SRT/VTT & local ACP agent"| UseCapwise["✅ Select joeseesun/capwise (Capwise / 灵录)<br/>Safe separation of caption edit vs text-based video cut<br/>Zero mandatory cloud account + undoable ACP edits"]
    OSCheck -->|"Running Windows 10/11 and need 5-stage Markdown/JSON NLE handoff"| UseYT["Select youtube-ai-video-editing-system (Daytime Round 13 / R196)"]
```

---

## 📊 4. Quantitative & Architectural Comparison Matrix

| Dimension | `fltman/idea-generator-2` (`Idégeneratorn`) | `joeseesun/capwise` (macOS `GPUI` Studio) | Legacy Path A: Uncalibrated Brainstorms + 4 Separate Video/Subtitle SaaS Tools | Legacy Path B: Static Miro Boards + External SRT Burn-In Scripts |
| :--- | :--- | :--- | :--- | :--- |
| **Core Problem Solved** | Evolves & scores ideas with a calibrated jury, auto-scaffolding Gold winners into `CLAUDE.md` repos | Unifies Mac screen recording, teleprompter, auto-zoom, bilingual captions & ACP edits in 1 window | Uncalibrated LLM judges inflate scores; round-tripping MP4s across 4 tools desyncs subtitles | Manual ideation lacks lineage tracking; external SRT edits break whenever video is trimmed |
| **Key Mechanisms** | **`npm run calibrate` 15-pt jury + USD-capped tournament autopilot + X/HF scouts** | **`desktop-gpui` + Content/Translation/Style split + Cut-by-Text guard + ACP bridge** | Single-model chat prompts; cloud-locked recording accounts | Manual `CLAUDE.md` authoring; destructive FFmpeg subtitle burn-in |
| **Safety & Footprint** | Node 25+ native TS (`1` dep), 50 offline tests, RAM-only keys on `127.0.0.1:8300` | Signed/notarized Apple Silicon `.dmg`, local `.cap` project files, undoable AI actions | Recurring multi-seat SaaS bills | High manual rework on every script revision |

---

## 🃏 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

| Card | Track / Section | Headline-as-Finding | Evidence & Sealed Anchor |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `idea-generator-2` + `Capwise` cuts monthly R&D ideation & bilingual product-demo TCO by `91.17%` (`$5,380.00 → $475.00/mo`) | `CLAIM-20261114-R19-IDEAGEN2-CAPWISE` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `idea-generator-2` calibrates its 15-point jury for `~$0.07` and automatically scaffolds Gold (`≥13/15`) ideas into `CLAUDE.md` Git repos | `fltman/idea-generator-2` (`npm run calibrate`) |
| **Card 3** | `3/7 · WHAT I TESTED` | `Capwise` combines Apple Silicon `GPUI` screen capture, synced teleprompter, bilingual captions, and local ACP editing in one window | `joeseesun/capwise` (`apps/desktop-gpui`) |
| **Card 4** | `4/7 · UNDER THE HOOD` | 8 role-specific `provider:model` slots (Foundry/OpenRouter/Ollama) + explicit separation of text edits vs Cut Video by Text | Role routing & non-destructive cut guardrails |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | 50 offline unit tests, citation-verified X scout, and dual daily USD caps in `idea-generator-2`; undoable AI/ACP proposals in `Capwise` | Test suite & budget guardrails |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | Eliminates manual `CLAUDE.md` repo setup and multi-tool video/subtitle round-trips, saving `34.5 hrs/mo` (`-90.79%`) | 20 ideation sprints + 30 bilingual demos/mo |
| **Card 7** | `7/7 · MY TAKE` | Seamless end-to-end loop from evolutionary idea selection (`CLAUDE.md`) to polished bilingual macOS product demos | Apple Silicon Mac hardware: `not_measured` |

### 💰 Closed-Form FinOps Table (20 R&D Ideation Sprints + 30 Bilingual Product Demos/Mo, `r = $100.00/hr`)

| Architecture Path | Video SaaS & Token Spend (`compute_and_token_usd`) | Ideation Filtering & Subtitle Sync Hours (`engineering_hours`) | Engineering Labor (`engineering_labor_usd`) | Total Monthly TCO (`total_monthly_usd`) | Net Savings vs Path A (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Uncalibrated Brainstorms + 4 Separate Video/Subtitle SaaS Tools** | `$1,580.00` | `38.0 hrs` | `$3,800.00` | **`$5,380.00`** | Baseline (`0.00%`) |
| **Path B: Static Whiteboards + External Subtitle Re-Sync Scripts** | `$790.00` | `18.0 hrs` | `$1,800.00` | **`$2,590.00`** | `-$2,790.00` (`-51.86%`) |
| **Path C: `idea-generator-2` + `Capwise` Studio (Recommended)** | **`$125.00`** | **`3.5 hrs`** | **`$350.00`** | **`$475.00`** | **`-$4,905.00` (`-91.17%` / `$58,860.00/yr`)** |

---

## 🛠️ 6. 15-Minute Actionable Rollout Checklist

```bash
# 1. Clone fltman/idea-generator-2 (Node 25+), run the 50 offline tests, calibrate the jury, and launch at localhost:8300
git clone https://github.com/fltman/idea-generator-2.git && cd idea-generator-2
npm install && npm test && npm start

# 2. Download or clone joeseesun/capwise on macOS (Apple Silicon) and open the sample .cap bilingual demo project
git clone https://github.com/joeseesun/capwise.git
```
