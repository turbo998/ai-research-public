# 5-Level Progressive `VIDEO.md` Spec (`videomd/videomd`) & Rust `tmux` Single-Card Attention Queue (`nodo-labs-uk/attention-queue`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 38 (Cumulative #166) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, Multimodal Video Pipeline Engineers, and Linux/`tmux` Power Users evaluating two context-progressive and attention-preserving workflows:
> 1. **`videomd/videomd` (`10★` in 1 day, Python, Apache-2.0 + CC BY 4.0, PyPI `videomd`, Spec v1)**: An open 5-level progressive-disclosure format (`VIDEO.md` [`L0` card + `L1` overview/map] → `video/timeline.md` & `video/sound.md` [`L2`] → `video/shots/01.md` [`L3`] → `frames/` [`L4`]) where **"Every skill has a `SKILL.md`. Every video gets a `VIDEO.md`"** — declaring exact token counts per file, pinning source video `sha256` and filmed-vs-code ratios, and **strictly separating directly observed facts (`seen`) from inferred attributes (keys ending in `~`)**!
> 2. **`nodo-labs-uk/attention-queue` (`10★` in 3 days, Rust, MIT, `aq` CLI for Linux + `tmux`)**: A terminal attention queue that merges `PreToolUse`, `PostToolUse`, and `PermissionRequest` hooks into `~/.claude/settings.json` to push diffs, edit approvals, permission prompts, and questions from all running `tmux` Claude Code sessions into **one non-preemptive single-card-at-a-time queue (`review / step / quiz / vibe`)** — where new arrivals wait their turn without hijacking the screen and prompts answered in their own `tmux` pane are marked `"answered elsewhere"`!
>
> **中文版本**: [videomd-attention-queue-5level-progressive-video-spec-rust-tmux-attention-queue-selection-faq.md](videomd-attention-queue-5level-progressive-video-spec-rust-tmux-attention-queue-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r38-videomd-attentionqueue.svg`](../../../assets/github-ai-radar-2026-11-13-r38-videomd-attentionqueue.svg)

![videomd/videomd and nodo-labs-uk/attention-queue Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r38-videomd-attentionqueue.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "dumping dozens of raw video frames or a monolithic VLM transcript into context every time an agent needs to check a single shot — while mixing up what was actually seen on screen with what the model guessed" (`videomd/videomd`)**: Just as `SKILL.md` brought progressive disclosure to agent skills, `VIDEO.md` structures video breakdowns into **5 explicit layers (`L0` card → `L1` map → `L2` `timeline.md`/`sound.md` → `L3` `shots/01.md` → `L4` raw `frames/`)**. Every file states how many tokens it holds, pins the source file `sha256`, records production ratios (e.g., `Filmed (70%) + code-rendered (30%)`), and **keeps what was `seen` strictly separate from inferred fields (keys ending in `~`)**!
   - **Ending "cycling endlessly through `tmux` windows to find which Claude Code session is waiting on you — or having a newly finished session yank focus away while you are mid-way through reviewing another diff" (`nodo-labs-uk/attention-queue`)**: Written in Rust for Linux and `tmux`, `aq` uses Claude Code's `PreToolUse`, `PostToolUse`, and `PermissionRequest` hooks to push all waiting diffs, edit approvals, and questions into **one terminal queue shown one card at a time**. A card that arrives while you are reading another waits its turn and never steals the screen; if you answer it directly in its own `tmux` window, `aq` marks it `"answered elsewhere"` until you press a key!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R38-VIDEOMD-ATTENTIONQUEUE`)**:
   - Modeled for a **12-engineer multimodal and systems team analyzing `400 multi-shot videos / month` and running `120 concurrent tmux Claude Code panes` (10 per engineer)** (fully loaded multimodal & systems engineer rate `$95.00/hr`; local GPU workstations and object storage buckets: `not_measured`):
   - Switching from **Path A (full-frame VLM context dumps + manual `tmux` window hunting and interrupted reviews, `$5,250.00/mo`)** to **Path C (`VIDEO.md` `L0→L4` progressive disclosure + `aq` single-card non-preemptive `tmux` queue, `$497.50/mo`)** saves **`$4,752.50/mo` (`-90.52%`, or `$57,030.00/yr`)** and cuts VLM hallucination triage and `tmux` context-switching toil from `38.0 hrs/mo` to `3.5 hrs/mo` (**`-90.79%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why do monolithic VLM video transcripts waste tokens and corrupt downstream video remake pipelines?
- **First-Principles Breakdown**:
  1. **Zero Progressive Disclosure**: Loading a 30-shot transcript when an agent only needs to inspect Shot #1 or the audio track wastes >90% of the context window.
  2. **Conflation of Observation and Inference**: Without structural separation between directly observed visual facts and guessed camera/production parameters, downstream agents treat VLM hallucinations as ground truth.

### Q2: How does `videomd/videomd` enforce `L0–L4` progressive reading and `seen` vs. `~` provenance?
- **First-Principles Breakdown**:
  1. **Five-Layer Package with Upfront Token Counts**:
     - Starts with a compact `VIDEO.md` card (`L0/L1` with `sha256`, duration, shot count, and filmed/code split), expands into 1-line-per-shot `video/timeline.md` and topic files like `video/sound.md` (`L2`), drills into `video/shots/01.md` (`L3`), and reserves `frames/` (`L4`) for image/program access.
  2. **Explicit `seen` vs. `~` Inferred Keys**:
     - Any inferred key in the timeline or shot breakdown must end with a tilde (`~`), keeping observed evidence and model hypotheses distinct.

### Q3: How does `nodo-labs-uk/attention-queue` (`aq`) protect developer focus across parallel `tmux` Claude Code sessions?
- **First-Principles Breakdown**:
  1. **Push-Based Hook Queue (`PreToolUse`, `PostToolUse`, `PermissionRequest`)**:
     - Let the work come to you instead of polling panes; `aq` merges its hooks non-destructively into `~/.claude/settings.json`.
  2. **Non-Preemptive Single-Card Display & `"answered elsewhere"` Sync**:
     - Displays exactly one card at a time (`review`, `step`, `quiz`, or `vibe`), holds new arrivals in the queue without taking over the screen, and detects when a prompt was already resolved in its native `tmux` pane.

---

## 🧭 3. Mermaid Decision Tree & VIDEO.md + Attention-Queue Architecture

```mermaid
flowchart TD
    A["Multimodal Video Breakdown Context & Parallel tmux Claude Code Triage"] --> B{"Primary Workflow Bottleneck?"}
    B -- "Video Understanding: Full-video VLM dumps waste tokens & mix seen facts with guesses" --> C["Adopt videomd/videomd (L0-L4 Progressive VIDEO.md Spec v1)"]
    B -- "Terminal Multi-Session Triage: Cycling tmux panes wastes time & popups interrupt diff reviews" --> D["Adopt nodo-labs-uk/attention-queue (Rust aq Single-Card Hook Queue)"]

    C --> C1["Read L0/L1 VIDEO.md card first -> drill into L2 timeline/sound or L3 shots/01.md on demand"]
    C1 --> C2["Declare exact tokens per file + separate seen facts from inferred (~) keys"]

    D --> D1["Merge PreToolUse, PostToolUse & PermissionRequest hooks into ~/.claude/settings.json"]
    D1 --> D2["Review 1 card at a time (zero screen preemption) + sync 'answered elsewhere' state"]

    C2 & D2 --> E["🏆 Golden Progressive-Context & Deep-Focus Stack: VIDEO.md + aq Queue (-90.52% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Full-Frame VLM Dump + `tmux` Hunting | Path B: Flat Monolithic Video JSON + Grid Dashboard | **Path C (Recommended): `videomd/videomd` + `attention-queue` (`aq`)** |
| :--- | :--- | :--- | :--- |
| **Video Context Token Efficiency** | Re-sends full keyframes/transcripts on every query | Loads entire multi-shot JSON at once | **`L0→L4` progressive disclosure with explicit per-file token budgets** |
| **Fact vs. Inference Separation** | Hallucinated camera/lighting guesses mixed with facts | Untyped free-text descriptions | **Source `sha256` pinned + strict `seen` vs. `~` inferred key separation** |
| **`tmux` Multi-Session Focus Protection** | Manual pane cycling; missed prompts expire cache | Multi-pane dashboards cause visual overload or preempt focus | **Non-preemptive 1-card-at-a-time queue (`review / step / quiz / vibe`)** |
| **Cross-Pane Resolution Sync** | Stale prompts or duplicate approvals | Manual refresh required | **Automatically marks prompts resolved in their own pane as `"answered elsewhere"`** |
| **Monthly TCO (400 Videos + 120 Panes)** | **`$5,250.00 / mo`** (`$1,640` VLM/cache + `$3,610` labor) | **`$2,630.00 / mo`** (`$730` token + `$1,900` labor) | **`$497.50 / mo` (Saves `$4,752.50/mo` · `-90.52%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R38-VIDEOMD-ATTENTIONQUEUE`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A 12-engineer multimodal and systems team analyzing **400 multi-shot product/reference videos per month** and operating **120 concurrent `tmux` Claude Code panes** (10 panes per engineer).
- **Labor Rate**: Fully loaded multimodal and systems engineer rate of **`$95.00 / hr`**.
- **Explicit Not-Measured Boundary**: Local GPU workstation depreciation and cloud object storage bucket fees are marked **`not_measured`**. This model strictly accounts for VLM/context token spend and expired `tmux` prompt caches plus engineering hours spent verifying video hallucinations and cycling through `tmux` windows.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Full-Frame VLM Dump + `tmux` Hunting | Path B: Flat Video JSON + Manual Window Cycle | **Path C: `VIDEO.md` (`L0–L4`) + `aq` Rust Queue (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly VLM Reading & Session-Cache Token Spend** | **`$1,640.00`** (repeated full-frame VLM reads + expired caches) | **`$730.00`** (monolithic JSON prefill spend) | **`$165.00`** (`L0→L3` progressive reads + fast `aq` queue turnaround) |
| **Hallucination Audit & `tmux` Context-Switch Labor (`$95/hr`)** | `38.0 hrs × $95.00` = **`$3,610.00`** | `20.0 hrs × $95.00` = **`$1,900.00`** | `3.5 hrs × $95.00` = **`$332.50`** |
| **Total Monthly TCO** | **`$5,250.00 / mo`** | **`$2,630.00 / mo`** (`-49.90%`) | **`$497.50 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,620.00 / mo` | **Saves `$4,752.50 / mo` (`-90.52%` · `$57,030.00/yr`)** |
| **GPU Workstations & Object Storage Buckets** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `videomd/videomd` Package Authoring**: Install `pip install videomd` and package reference videos into `VIDEO.md` (`L0/L1`), `video/timeline.md` (`L2`), `video/shots/*.md` (`L3`), and `frames/` (`L4`).
- [ ] **2. Token Budget & `seen` vs. `~` Audit**: Confirm that every markdown file declares its token count and separates `seen` observations from `~` inferred keys.
- [ ] **3. `nodo-labs-uk/attention-queue` (`aq`) Hook Merge**: Install `aq` on Linux + `tmux`, back up `~/.claude/settings.json`, and merge the `PreToolUse`, `PostToolUse`, and `PermissionRequest` hooks from `contrib/settings-hooks.json`.
- [ ] **4. Single-Card Non-Preemption & `"answered elsewhere"` Test**: Trigger concurrent prompts across two `tmux` sessions, verify that the second card waits without stealing focus, and test resolving a prompt in its own pane to confirm the `"answered elsewhere"` badge.
