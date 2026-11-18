# Dual-Persona 3-View 3D Printing Workbench (`AFangTeam/PrintLab` `v0.4.0`) & 257-Episode Full-Subtitle Game-Feel Review Skill (`kociden/sakurai-skill`) Selection FAQ

> **Document Scope**: This is the **2026-11-13 Night Shift Round 5 (Cumulative #133) standalone 6-part selection guide**, modeled strictly after `ib-vs-ethernet-roce-selection-faq.md` with first-principles explanations and closed-form FinOps math. It is written for AI Solution Architects, Hardware-Software Prototyping Leads, and Interactive Experience Designers evaluating two breakout repositories that bridge digital prompts to physical fabrication and tactile interactive polish:
> 1. **`AFangTeam/PrintLab` (`209★` in 2 days, `105★/d` velocity, Python / Node.js, released `v0.4.0` today)**: A local-first 3D printing workbench (`http://127.0.0.1:8018`) for **Mac / Windows + Codex + Bambu Lab printers** — pairing two workspace-bound AI personas (**`Sarah · 3D Printing Advisor`** for printer specs, filament inventory, and authorized cart additions, plus **`Mike · Workflow Designer`** for tool connectors and `verify_onboarding.py` checks) with a 9-stage **Idea-to-Physical gate** (`1 Shape Concept → 4 Orthographic Three-View Sets → Text-to-CAD → Slicing Comparison → Confirmed Print Package & Physical Receipt`) and Bambuddy local history recovery (`printlab history-recover`)!
> 2. **`kociden/sakurai-skill` (`169★` in 1 day, `169★/d` velocity, Python / Markdown)**: A progressive-disclosure game-design and game-feel ("手応え" / hitstop / motion / camera / UI) Agent Skill (`skills/sakurai/SKILL.md` ~27k chars + 14 on-demand `references/*.md` files) compiled directly from **all 257 main-episode transcripts (`001–259`)** of Masahiro Sakurai's *Creating Games* via `tools/to_text.py` and `tools/build_refs.py`, complete with a playable **Godot 4.6** one-screen action game (`examples/hajiki/`) built end-to-end by an AI agent!
>
> **中文版本**: [printlab-sakurai-skill-3d-printing-workbench-257-video-game-feel-skill-selection-faq.md](printlab-sakurai-skill-3d-printing-workbench-257-video-game-feel-skill-selection-faq.md) · **Daily Digest**: [`daily/2026-11-13.en.md`](../daily/2026-11-13.en.md) · **Topic SVG**: [`assets/github-ai-radar-2026-11-13-r5-printlab-sakurai.svg`](../../../assets/github-ai-radar-2026-11-13-r5-printlab-sakurai.svg)

![AFangTeam/PrintLab v0.4.0 and kociden/sakurai-skill Architecture Comparison](../../../assets/github-ai-radar-2026-11-13-r5-printlab-sakurai.svg)

---

## 📌 1. Executive Summary

1. **In plain English, what core pain points do these two repositories solve?**
   - **Ending "blind single-prompt Text-to-STL prints that fail on overhangs/tolerances, waste spools of filament, and forget your printer nozzle/AMS setup across sessions" (`AFangTeam/PrintLab` `v0.4.0`)**: Jumping straight from a text prompt to a 3D mesh skips orthographic dimension checks and slicer comparison. `PrintLab` binds Codex to a persistent local workspace (`http://127.0.0.1:8018`) staffed by **`Sarah` (3D Printing Advisor)** and **`Mike` (Workflow Designer)** plus per-project task groups. Every physical build progresses through a strict gate: pick 1 shape concept, choose 1 of **4 orthographic three-view sets**, run Text-to-CAD with interface/tolerance checks, compare slicing time and filament grams, issue a bound print confirmation receipt, and log physical feedback alongside Bambuddy history!
   - **Ending "sluggish, floaty AI-generated games and interactive UIs ('手応えがない / もっさり') while avoiding 250-video context bloat" (`kociden/sakurai-skill`)**: Unassisted LLMs write functional movement scripts that feel lifeless because they lack frame-exact hitstop, risk-reward tension, acceleration curves, and audio-visual punch. `sakurai-skill` processes **all 257 full episode subtitles (`001–259`)** of Masahiro Sakurai's channel into a lightweight ~27k-char `SKILL.md` (14 chapters of core principles and review workflows) plus **14 on-demand category files under `references/`** (`gameplay.md`, `motion.md`, `effects.md`, `ui.md`, `sound.md`, etc.), proven by a playable Godot 4.6 action game (`Hajiki`) with episode-numbered design citations!
2. **Closed-Form FinOps Conclusion (`CLAIM-20261113-R5-PRINTLAB-SAKURAI`)**:
   - Modeled for a **hardware-software prototyping studio producing `80 physical 3D-printed mechanisms/enclosures per month` and `60 interactive game-feel / UI-juice prototypes per month`** (fully loaded prototyping engineer rate `$85.00/hr`; physical Bambu printer hardware and commercial CAD seat capex: `not_measured`):
   - Upgrading from **Path A (blind single-prompt Text-to-STL printing + unstructured vibe-coding game loops, `$5,320.00/mo`)** to **Path C (`AFangTeam/PrintLab v0.4.0` 3-view/slicing-gated workbench + `kociden/sakurai-skill` 257-episode progressive-disclosure skill, `$620.00/mo`)** saves **`$4,700.00/mo` (`-88.35%`, or `$56,400.00/yr`)** and cuts failed-print and game-feel tuning labor from `44.0 hrs/mo` to `5.0 hrs/mo` (**`-88.64%`**).

---

## 🎯 2. Three First-Principles Deep-Dive Questions (Q1 / Q2 / Q3)

### Q1: Why do one-shot prompts fail when crossing into physical 3D tolerances and millisecond-level interactive game feel?
- **First-Principles Breakdown**:
  1. **Perspective Ambiguity vs. Physical Slicer Constraints**: A single perspective render hides rear geometry, wall thickness, and overhang angles; without orthographic three-view lock-in and slicer comparison, prints fail on the build plate.
  2. **Game Feel Is Sub-Second Multi-Sensory Synchronization**: Tactile impact ("手応え") depends on 3–6 frame hitstops, risk-reward proximity mechanics, camera lead, and sound transient contrast — details absent from generic coding prompts.

### Q2: How does `AFangTeam/PrintLab` (`v0.4.0`) govern the Idea-to-Physical lifecycle across Mac, Windows, Codex, and Bambu Lab?
- **First-Principles Breakdown**:
  1. **Workspace-Bound Dual Personas (`Sarah` & `Mike`) + Project Task Groups**:
     - `Sarah` tracks printer profiles (e.g., X2D, 0.4mm nozzle, AMS, textured PEI plate), filament inventory, and cross-project shopping lists; `Mike` manages tool bindings and `verify_onboarding.py`; each artifact gets a dedicated project conversation stored under local `Project/`.
  2. **4-Set Three-View Gate, Bambuddy Sync & Safe Synthetic Testing**:
     - Enforces `Concept -> 4 Three-View Sets -> Text-to-CAD -> Slicing Comparison -> Print Receipt -> Physical Feedback`, recovers missing previews via `printlab history-recover`, and isolates tests on synthetic devices unless `PRINTLAB_LIVE_TEST=1` is explicitly set.

### Q3: How does `kociden/sakurai-skill` balance 257-episode primary-source completeness with low token overhead?
- **First-Principles Breakdown**:
  1. **Full 257-Episode Subtitle Pipeline (`to_text.py` & `build_refs.py`)**:
     - Extracts directly from all 257 main episodes (`001–259`, including `misc.md`), tagging every guideline with its exact episode number and title for primary-source traceability.
  2. **Two-Tier Progressive Disclosure (`SKILL.md` + 14 `references/*.md`) & Godot 4.6 Proof**:
     - Keeps `SKILL.md` concise (~27k chars) while isolating detailed parameters and examples into 14 category files (`gameplay.md`, `motion.md`, `effects.md`, `ui.md`, etc.) loaded only when needed, demonstrated in the playable Godot 4.6 game `examples/hajiki/`.

---

## 🧭 3. Mermaid Decision Tree & Physical 3D Printing + 257-Episode Game-Feel Architecture

```mermaid
flowchart TD
    A["Physical 3D Fabrication & Interactive Game-Feel Prototyping Selection"] --> B{"Primary Deliverable Type?"}
    B -- "Physical 3D-printed enclosures/parts with Codex + Bambu Lab printers" --> C["Adopt AFangTeam/PrintLab (v0.4.0 Sarah+Mike Dual-Persona Workbench)"]
    B -- "Interactive games or UI prototypes needing crisp hitstop, motion & risk-reward feel" --> D["Adopt kociden/sakurai-skill (257-Episode Progressive-Disclosure Skill)"]

    C --> C1["Single shape selection -> 4-set orthographic three-view confirmation -> Text-to-CAD"]
    C1 --> C2["Slicing time/filament comparison -> bound print receipt & Bambuddy history"]

    D --> D1["Load ~27k-char SKILL.md (14 chapters) to diagnose sluggish ('mossari') feel"]
    D1 --> D2["Load on-demand references/motion.md & effects.md with 001-259 episode citations"]

    C2 & D2 --> E["🏆 Golden Prototyping Stack: 3-View/Slicer Physical Gate + 257-Episode Tactile Polish (-88.35% TCO)"]
```

---

## 📊 4. Head-to-Head Selection Matrix

| Dimension | Path A: Blind Text-to-STL + Unstructured Game Prompts | Path B: Manual CAD/Slicer + Secondary Summary Notes | **Path C (Recommended): `PrintLab v0.4.0` + `kociden/sakurai-skill`** |
| :--- | :--- | :--- | :--- |
| **3D Geometry & Slicer Verification** | Unchecked meshes cause overhangs & failed prints | Manual file juggling across CAD and slicer apps | **1 Concept → 4 Three-View Sets → CAD → Slicing Diff & Print Receipt** |
| **Printer & Filament State Continuity** | Lost across chat sessions | Manual spreadsheets | **Workspace-bound `Sarah` & `Mike` personas + Bambuddy history sync** |
| **Game-Feel Corpus Completeness** | Generic LLM platitudes | Partial secondary summaries without episode IDs | **All 257 episodes (`001–259`) distilled directly from full subtitles** |
| **Context Efficiency & Live Proof** | Multi-turn blind trial-and-error | Heavy multi-router overhead | **~27k-char `SKILL.md` + 14 on-demand `references/*.md` + Godot 4.6 `Hajiki` demo** |
| **Monthly TCO (80 Prints + 60 Prototypes)** | **`$5,320.00 / mo`** (`$1,580` API/waste + `$3,740` labor) | **`$2,760.00 / mo`** (`$720` API/mat + `$2,040` labor) | **`$620.00 / mo` (Saves `$4,700.00/mo` · `-88.35%`)** |

---

## 🧪 5. Closed-Form FinOps Worked Example & 7-Card Insights (`CLAIM-20261113-R5-PRINTLAB-SAKURAI`)

### 5.1 Baseline Parameters & Explicit Scope Boundaries
- **Scenario**: A hardware-software prototyping lab producing **80 physical 3D-printed parts/enclosures per month** and **60 interactive game-feel / UI prototypes per month**.
- **Labor Rate**: Fully loaded industrial / interactive prototyping engineering rate of **`$85.00 / hr`**.
- **Explicit Not-Measured Boundary**: Physical Bambu Lab 3D printer hardware and commercial CAD seat licenses are marked **`not_measured`**. This model strictly accounts for LLM/3D generation API spend, wasted filament/reprint material cost, and engineering rework/tuning hours.

### 5.2 Three-Path Monthly Cost Comparison

| Cost Component | Path A: Blind Text-to-STL + Unstructured Game Prompts | Path B: Manual CAD/Slicer + Generic Prompts | **Path C: `PrintLab v0.4.0` + `sakurai-skill` (Recommended)** |
| :--- | :--- | :--- | :--- |
| **Monthly API & Prototyping Material Spend** | **`$1,580.00`** (repeated 3D API retries + wasted filament spools) | **`$720.00`** (standard material use + ad-hoc API calls) | **`$195.00`** (3-view/slicer gate prevents failed prints + on-demand `references/`) |
| **Failed-Print Rework & Game-Feel Tuning Labor (`$85/hr`)** | `44.0 hrs × $85.00` = **`$3,740.00`** | `24.0 hrs × $85.00` = **`$2,040.00`** | `5.0 hrs × $85.00` = **`$425.00`** |
| **Total Monthly TCO** | **`$5,320.00 / mo`** | **`$2,760.00 / mo`** (`-48.12%`) | **`$620.00 / mo`** |
| **Net Savings vs. Path A** | Baseline | Saves `$2,560.00 / mo` | **Saves `$4,700.00 / mo` (`-88.35%` · `$56,400.00/yr`)** |
| **Physical 3D Printers & Commercial CAD Seats** | `not_measured` | `not_measured` | `not_measured` |

---

## 🛠️ 6. Production Adoption Checklist

- [ ] **1. `AFangTeam/PrintLab` (`v0.4.0`) Setup & Automated Test Suite**: Run `scripts/setup.sh` & `scripts/start.sh` (or `setup.ps1` / `start.ps1` on Windows), open `http://127.0.0.1:8018`, and verify `verify_onboarding.py`, `pytest Harness/tests -q`, and `node --test Harness/tests/native-inspection.test.mjs` against synthetic devices (`PRINTLAB_LIVE_TEST` unset).
- [ ] **2. `Sarah` + `Mike` Onboarding & 4-Set Three-View Workflow**: Initialize the `Sarah` and `Mike` workspace chats, complete `docs/ONBOARDING.md`, and run a full `Concept -> 4 Three-View Sets -> Text-to-CAD -> Slicing Comparison -> Print Receipt` loop.
- [ ] **3. `kociden/sakurai-skill` Installation & Progressive Reference Loading**: Copy `sakurai-skill/skills/sakurai` into `~/.claude/skills/`, prompt your coding agent to review an interactive prototype's hitstop and feel, and verify on-demand loading of `references/motion.md` and `references/effects.md`.
- [ ] **4. Godot 4.6 `Hajiki` Reference Audit**: Inspect `examples/hajiki/README.md` to trace how specific numbered episodes (`001–259`) were applied to bullet-deflection risk-reward mechanics, hitstop frames, and UI polish.
