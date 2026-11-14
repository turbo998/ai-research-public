# Zero-Search 6.6M Entity-Transformer RL with Failure Restarts (`HalfVulpes/sts2ai`) & `3200×1800@60fps` UI Redline Morphing Skill (`rjmahesh/ui-redline-walkthrough`) Deep-Dive & Selection FAQ

> **Document Metadata (2026-11-14 · Night Round 67 / Cumulative Round 250 Quarter-Millennium Milestone!)**  
> - **Benchmark Style**: `ib-vs-ethernet-roce-selection-faq.md` (First-Principles + Plain-Language Deconstruction + 3 Architect Core Questions + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> - **Primary Evaluated Repositories**:  
>   1. [`HalfVulpes/sts2ai`](https://github.com/HalfVulpes/sts2ai) (`★ 44`, GPL-2.0 official implementation of University of Waterloo's `arXiv:2611.12088` — *Zero-Search Reinforcement Learning for Slay the Spire 2 with Failure-Driven Restarts*: selects every action with **one forward pass of a `6.6M`-parameter entity transformer [zero lookahead search]**, executes the game's actual compiled `.NET 9` assemblies [11 hash-verified DLLs, 2,650-token vocabulary] in a deterministic headless simulator, and uses a **failure-driven restart curriculum** across 5 released hero policies)  
>   2. [`rjmahesh/ui-redline-walkthrough`](https://github.com/rjmahesh/ui-redline-walkthrough) (`★ 61`, MIT Claude skill that turns before/after UI screenshots into a **`3200×1800 @ 60fps` animated redline walkthrough HTML + MP4**: uses `scripts/measure.py` [NumPy/Pillow/SciPy] and `extract_icons.py` to measure exact bounding boxes, colors, and text extents before animating red-ink callouts and morphing the flawed UI into the clean redesign)  
> - **Visual Architecture Diagram**: [`assets/github-ai-radar-2026-11-14-r67-sts2ai-uiredline.svg`](../../../assets/github-ai-radar-2026-11-14-r67-sts2ai-uiredline.svg)  
> - **Audit Contract ID**: `CLAIM-20261114-R67-STS2AI-UIREDLINE` (local workstation GPU hardware depreciation is explicitly marked `not_measured`)

---

## 📌 1. Executive Summary (Understand the Essence in 3 Minutes)

1. **In complex stochastic state machines (like *Slay the Spire 2* or enterprise scheduling engines), why do re-implemented Python simulators drift from real runtime behavior while uniform episode starts waste 90% of training compute on easy early stages? How does `HalfVulpes/sts2ai` (`arXiv:2611.12088`) solve both?**  
   - **Plain-Language Essence**: Rewriting a complex production rules engine in Python inevitably introduces subtle behavioral bugs, and restarting every RL episode from step 0 starves late-stage bottleneck states of gradient updates.  
   - **First-Principles Breakthrough in `sts2ai`**:
     - **Headless `.NET 9` Host Running Actual Compiled Assemblies + Clean-Room BYO Importer**: `tools/import_game.py` verifies all 11 assembly SHA-256 hashes from the user's local installation (`v0.107.1`, distributing zero proprietary game files) and runs them inside a headless `.NET 9` simulator (`Sts2Sim.dll`) that replays any seed and action sequence deterministically.
     - **`6.6M`-Parameter Entity Transformer (Zero Search) + Failure-Driven Restarts**: Every action is chosen in a single forward pass of a `6.6M`-parameter entity transformer (`2,650` vocabulary) with zero lookahead tree search. A **failure-driven curriculum** restarts training episodes directly at the states where complete runs were lost, producing 5 strong released policies (`ironclad`, `silent`, `defect`, `necrobinder`, `regent`) that run inside the game via native C# inference.
2. **When presenting a UI redesign, why do static side-by-side screenshots fail to tell the story while LLM-guessed CSS coordinates place redline circles in the wrong spot? How does `rjmahesh/ui-redline-walkthrough` automate `3200×1800 @ 60fps` redline-to-morph films?**  
   - **Plain-Language Essence**: High-impact design reviews show the "before" UI, circle each flaw with red ink and handwritten notes, and smoothly morph each region into the "after" redesign. Doing this in After Effects takes hours; asking an LLM to guess pixel coordinates from a screenshot misses by dozens of pixels.  
   - **First-Principles Breakthrough in `ui-redline-walkthrough`**:
     - **Deterministic Raster Measurement (`measure.py`) + Alpha Sprite Cutout (`extract_icons.py`)**: Before authoring animation beats, Python scripts using `numpy`, `pillow`, and `scipy` measure exact bounding boxes, colors, and text line extents from the before/after screenshots and extract clean transparent icons.
     - **Red-Ink Choreography + `3200×1800 @ 60fps` Headless Export (`export_mp4.py`)**: Compiles a self-contained interactive `template.html` (Space pauses, arrow keys seek) and drives headless Playwright Chromium + `ffmpeg` to render a frame-accurate `3200×1800 @ 60fps` MP4 walkthrough.
3. **Closed-Form FinOps Audit Conclusion (`CLAIM-20261114-R67-STS2AI-UIREDLINE`, Cumulative R250 Milestone)**:  
   - Modeled for **28 combinatorial policy training runs and UI redline walkthrough deliverables/month** (at **`$100.00/hr`** engineering labor): migrating from **Path A** (online MCTS/LLM tree-search rollouts + manual After Effects redline morphing: **`$5,750.00/mo`**, comprising `$1,950.00` compute/design spend + `38.0h` simulator alignment and manual keyframing labor `$3,800.00`) to **Path C** (`sts2ai` 6.6M zero-search failure-restart RL + `ui-redline-walkthrough` 60fps pipeline: **`$495.00/mo`**, comprising `$145.00` lean compute spend + `3.5h` review labor `$350.00`) saves **`$5,255.00/mo`** (**`-91.39%`**, or **`$63,060.00/yr`**) and cuts engineering hours by **`90.79%`**.

![sts2ai & ui-redline-walkthrough Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r67-sts2ai-uiredline.svg)

---

## 💬 2. Three Architect Core Questions (Q1–Q3 Deep Dive)

### Q1: How can enterprise architects apply `HalfVulpes/sts2ai`'s "headless compiled-assembly host + failure-driven restarts" pattern to industrial optimization and risk engines?

1. **Zero Sim-to-Real Gap + Targeted Tail-Risk Curriculum**:  
   - Instead of re-coding legacy `.NET` or JVM pricing/dispatch binaries in Python for RL training, wrap the production compiled assemblies in a deterministic seed-replay host and restart training trajectories directly from historical failure/breach states.

---

### Q2: Why does a `6.6M`-parameter Entity Transformer achieve strong zero-search play without MCTS rollouts?

1. **Set-Equivariant Entity Representation & Sub-Millisecond C# Inference**:  
   - Cards, relics, enemies, and status effects form variable-size sets. An entity transformer processes arbitrary entity sets in one forward pass, exporting compact `.bin` weights that execute natively in C# with zero search latency.

---

### Q3: Why does `rjmahesh/ui-redline-walkthrough` pair `scripts/measure.py` with `references/measuring.md` before choreography?

1. **Eliminating Raster-vs-DOM Alignment Traps**:  
   - `measure.py` computes exact pixel bounding boxes, colors, and text extents from raster screenshots so red-ink strokes and DOM morph keyframes align to the pixel at `3200×1800 @ 60fps`.

---

## 🧭 3. Architecture Decision Tree & Topology (Mermaid)

```mermaid
flowchart TD
    Start["Zero-Search Combinatorial RL & Animated UI Redline Walkthrough Selection"] --> Domain{"Target Engineering Workflow?"}

    Domain -->|"Long-Horizon Stochastic State-Machine Policy Learning & Real-Time Inference"| RLGate{"Simulator & Latency Contract?"}
    RLGate -->|"Headless Compiled .NET 9 Host + Failure-Driven Restarts<br/>+ 6.6M Entity Transformer Zero-Search Forward Pass"| UseSTS2AI["✅ HalfVulpes/sts2ai (C#/.NET 9 + PyTorch · arXiv:2611.12088)<br/>• Verifies 11 assembly hashes for bit-exact seed replay<br/>• Restarts episodes at failure bottlenecks; native C# inference"]
    RLGate -->|"Offline unconstrained tree search"| OnlineSearch["🔄 Online MCTS / LLM Rollouts"]

    Domain -->|"Before/After UI Redesign Presentation & Executive Design Review"| UIWalkGate{"Visual Output Format?"}
    UIWalkGate -->|"measure.py Pixel Boxes + Animated Red-Ink Callouts<br/>+ Smooth UI Morphing at 3200x1800 @ 60fps"| UseRedline["✅ rjmahesh/ui-redline-walkthrough (MIT · Python + Playwright)<br/>• Extracts exact boxes, colors & transparent icon sprites<br/>• Exports interactive HTML + 3200x1800 60fps MP4 via Chromium"]
    UIWalkGate -->|"Static side-by-side PNGs"| StaticSlide["🔄 Static Slide Comparison"]

    UseSTS2AI --> FinOps["💰 Closed-Form FinOps Impact (CLAIM-20261114-R67-STS2AI-UIREDLINE · R250 Milestone)<br/>Monthly Total $5,750.00 ➔ $495.00 (-91.39% · Saves $63,060/yr)"]
    UseRedline --> FinOps
```

---

## 📊 4. Peer Comparison Matrix (Decision Matrix)

| Evaluation Dimension | `HalfVulpes/sts2ai` (6.6M Zero-Search Failure-Restart RL) | Re-Coded Python Sim + Online MCTS | `rjmahesh/ui-redline-walkthrough` (`3200×1800@60fps` Redline Skill) | Manual AE Morphing / VLM Coordinate Guesses |
| :--- | :--- | :--- | :--- | :--- |
| **Fidelity & Coordinate Accuracy** | **Runs actual compiled `.NET 9` assemblies (11 hash-checked DLLs)** | Re-coded simulators drift on edge cases | **`measure.py` (NumPy/SciPy) measures exact pixel boxes & colors** | VLM coordinate guesses miss by 30–80px |
| **Sample & Authoring Efficiency** | **Failure-driven restarts focus compute on lost late-game states** | Uniform starts waste 90% compute on Act 1 | **2 screenshots → red-ink critique → smooth DOM morph → 60fps MP4** | Hours of manual After Effects masking & easing |
| **Inference Speed & Resolution** | **1 forward pass of `6.6M` Entity Transformer in native C#** | Slow multi-second tree search per action | **Self-contained HTML player + `3200×1800 @ 60fps` MP4 export** | Low-res screen captures with frame drops |
| **IP Cleanliness & Reproducibility** | **0 proprietary assets shipped; full `MANIFEST.json` & seed logs** | Often bundles copyrighted game data | **MIT open-source with runnable 19s `3200×1800` reference demo** | Proprietary binary project files |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261114-R67-STS2AI-UIREDLINE` · R250 Milestone)

> **Scope & Boundary Declaration**: This synthetic FinOps model covers monthly tree-search/rollout compute and design software spend across **28 combinatorial policy runs and UI redline walkthrough deliverables** plus engineering labor for **simulator rule debugging and manual 60fps UI morphing animation** (at **`$100.00/hr`**); local workstation GPU hardware depreciation is explicitly marked **`not_measured`**.

| Architecture Path | Search Compute & Design Spend (`USD/mo`) | Sim Alignment & Animation Labor (`hrs/mo`) | Engineering Labor Cost (`@ $100/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Online Tree-Search + Manual AE Redline Morphing** | `$1,950.00` | `38.0 hrs` | `$3,800.00` | **`$5,750.00`** | Baseline (`0.00%`) |
| **Path B: Uniform-Start RL + Static Annotated Slides** | `$920.00` | `18.0 hrs` | `$1,800.00` | **`$2,720.00`** | `-$3,030.00` (`-52.70%`) |
| **Path C (Recommended): `sts2ai` RL + `ui-redline` 60fps** | **`$145.00`** | **`3.5 hrs`** | **`$350.00`** | **`$495.00`** | **`-$5,255.00` (`-91.39%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 1950.00 + 38.0 \times 100.00 = 1950.00 + 3800.00 = \$5,750.00$
  - $\text{Path B Total} = 920.00 + 18.0 \times 100.00 = 920.00 + 1800.00 = \$2,720.00$
  - $\text{Path C Total} = 145.00 + 3.5 \times 100.00 = 145.00 + 350.00 = \$495.00$
  - $\text{Net Savings (Path C vs Path A)} = 5750.00 - 495.00 = \$5,255.00/\text{mo} \quad (-91.39\%, \text{Annualized } \$63,060.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect Actionable Checklist

1. **Stage hash-verified `.NET 9` assemblies and build the `HalfVulpes/sts2ai` headless simulator**:
   ```bash
   python3 tools/import_game.py --game-dir "/path/to/steamapps/common/Slay the Spire 2"
   dotnet build sim/Sts2Sim.csproj -c Release
   dotnet sim/bin/Release/net9.0/Sts2Sim.dll vocab --out gamebin/v0.107.1/vocab.json --quiet
   ```
2. **Measure before/after UI screenshots and export a `3200×1800 @ 60fps` redline walkthrough**:
   ```bash
   pip install numpy pillow scipy playwright && playwright install chromium
   python scripts/measure.py before.png after.png
   python scripts/export_mp4.py assets/template.html --out demo.mp4
   ```
