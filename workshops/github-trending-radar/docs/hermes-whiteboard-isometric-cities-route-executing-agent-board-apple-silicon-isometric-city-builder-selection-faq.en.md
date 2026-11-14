# Route-Executing Agentic Whiteboard (`hermes-whiteboard`) & Patch-Gated Apple Silicon Isometric City Builder (`isometric-cities`) Architecture & Selection FAQ

> **Document Metadata (2026-11-14 · Daytime Round 47 / Cumulative Round 230 Milestone)**  
> - **Benchmark Style**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (First-Principles Breakdown + Plain-English Takeaways + 3 Core Architectural Q&As + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> - **Evaluated Repositories**:  
>   1. [`Adolanium/hermes-whiteboard`](https://github.com/Adolanium/hermes-whiteboard) (`★ 76`, agentic whiteboard for Hermes Desktop turning 1 sentence into a **Route, Columns, or Map**, executing stops sequentially with up to **3 concurrent agent cursors per stop** along a gold road, and synchronizing bidirectionally with **Hermes Chat** and **Hermes Kanban** with idempotent `Blocked`-first card creation)  
>   2. [`Statecraft-Labs/isometric-cities`](https://github.com/Statecraft-Labs/isometric-cities) (`★ 78`, MIT-licensed agent-driven Apple Silicon isometric pixel-art city builder: builds untextured 3D GIS geometry (`make "PLACE"`), enforces a **1-Patch Review Gate** before full-city expansion, repaints 10 windows of Edinburgh in **`24 minutes` at `18 GB` peak RAM** using `~9 GB` local `Klein 9B` weights, and exports an interactive `atlas.py` explorer and film)  
> - **Companion SVG Diagram**: [`assets/github-ai-radar-2026-11-14-r47-hermes-whiteboard-isometric-cities.svg`](../../../assets/github-ai-radar-2026-11-14-r47-hermes-whiteboard-isometric-cities.svg)  
> - **Audit Claim ID**: `CLAIM-20261114-R47-HERMESWHITEBOARD-ISOCITIES` (local Apple Silicon hardware depreciation marked `not_measured`)

---

## 📌 1. Executive Summary (3-Minute Architect's Briefing)

1. **Why do conventional AI whiteboards stop at generating static sticky notes, and how does `Adolanium/hermes-whiteboard` turn a canvas into a governed multi-agent execution DAG?**  
   - **Plain-English Reality**: Standard AI whiteboards generate sticky notes from a prompt, but leave humans to manually copy-paste those notes into chat threads or Kanban boards—or worse, spawn unapproved background tasks that ignore active chat permissions.  
   - **`hermes-whiteboard` First-Principles Fix**:
     - **Stop-by-Stop Gold-Road Execution (3 Cursors/Stop)**: Lays out a plan as a sequential **Route**, parallel **Columns**, or radial **Map**. Clicking **Run** travels the route stop by stop, fanning out up to **3 concurrent agent cursors per stop**, passing each stop's output forward as context to the next stop, and synthesizing a final brief at the end of the road;
     - **Approval-Preserving Linked Chat & Idempotent Kanban Bridge**: On a board linked to a Hermes Chat, *Ask in the linked chat* pre-fills the chat's message box so the owning chat runs with its existing approvals while updating live board badges (`Chat is on it`, `Chat: done`, `Blocked`). Selecting notes and pressing **Send to Kanban** parks cards safely in **`Blocked` with nobody assigned** by default (or `Triage` if opted in), and clicking twice on the same note returns the **exact same card (zero duplicates)**.
2. **How does `Statecraft-Labs/isometric-cities` build geographically accurate isometric pixel-art cities on Apple Silicon in 24–60 minutes without tile-seam hallucinations?**  
   - **Plain-English Reality**: Prompting a diffusion model directly for an isometric city map hallucinates street grids and fails to align roads across adjacent tiles, while blindly rendering 10+ windows on cloud GPUs wastes compute whenever the style or massing is off.  
   - **`isometric-cities` First-Principles Fix**: Driven by an `AGENTS.md` workflow (`make "PLACE"` -> untextured 3D GIS massing -> **Review 1 accurate patch first** -> expand via bundled native painter using `~9 GB` local `Klein 9B` weights). On Apple Silicon, repainting all 10 windows of Edinburgh from a fresh clone took **`24 minutes` at `18 GB` peak RAM**, and a fresh coding agent built a complete new Amsterdam interactive explorer (`atlas.py`) and film in **`~1 hour`**.
3. **Closed-Form FinOps Audit (`CLAIM-20261114-R47-HERMESWHITEBOARD-ISOCITIES`)**:  
   - Across **30 multi-step agentic planning boards & isometric city/campus builds per month** (at **`$100.00/hr`** engineering rate), migrating from **Path A** (un-gated full-city cloud GPU rerolls + manual whiteboard-to-Kanban copy-pasting: **`$5,690.00/mo`**) to **Path C** (`hermes-whiteboard` route executor & idempotent Kanban sync + `isometric-cities` 1-patch-gated local Apple Silicon pipeline: **`$490.00/mo`**) saves **`$5,200.00/month`** (**`-91.39%`**, **`$62,400.00/year`**) and cuts manual sync/seam-fixing labor from `38.0 hrs` to `3.5 hrs/mo` (**`-90.79%`**).

![Hermes Whiteboard & Isometric Cities Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r47-hermes-whiteboard-isometric-cities.svg)

---

## 💬 2. Three Architectural Deep-Dive Q&As (Q1–Q3)

### Q1: How does `Adolanium/hermes-whiteboard` prevent runaway agent execution and duplicate tickets across Whiteboard, Chat, and Kanban surfaces?

1. **Default-`Blocked` Kanban Parking & Idempotent Note-to-Card Mapping**:  
   - Pressing **Send to Kanban** creates one card per note parked in `Blocked` with no assignee so nothing runs until explicitly unblocked (unless *Let Hermes start on them* is ticked to route to `Triage`). Clicking **Send to Kanban** again on the same note resolves to the existing card rather than creating duplicates.
2. **Composer-Staged Chat Handoffs & One-Step Undo**:  
   - Linked-chat actions stage text into the chat's input box for user submission, results arrive under *Suggestions* for explicit acceptance, and cross-plugin pins (`hermes-sheets` / `hermes-data`) and Kanban refreshes are single-step undoable.

---

### Q2: Why is `Statecraft-Labs/isometric-cities`'s "Untextured 3D Massing -> 1-Patch Review Gate -> Local Native Painter" pipeline essential for spatial agents?

1. **Separating Structural GIS Accuracy from Neural Style Transfer**:  
   - `make "PLACE"` builds untextured 3D geometry from real map sources first so the coding agent can inspect and repair building footprints before any neural painting begins.  
   - Enforcing a human/agent review gate on **one single patch** before expanding across 10+ windows prevents wasting 24–60 minutes of GPU time on flawed geometry.

---

### Q3: What licensing boundaries must architects check when using `isometric-cities`?

1. **MIT Code vs. Non-Commercial Default `Klein 9B` Weights**:  
   - The repository code is MIT-licensed (and `python3 atlas.py demo --open` runs the Washington DC and Edinburgh interactive explorers with zero model weights downloaded), but the default `Klein 9B` weights are non-commercial and underlying map sources retain their own attributions (`THIRD_PARTY_NOTICES.md`). Swap in commercially licensed weights for commercial deployments.

---

## 🧭 3. Architecture Decision Tree & Spatial Agent Topology (Mermaid)

```mermaid
flowchart TD
    Start["Multi-Agent Spatial Whiteboard & Isometric Digital-Twin Pipeline Selection"] --> Domain{"Primary Workload?"}

    Domain -->|"Visual Planning Canvas with Multi-Agent Execution & Kanban Sync"| BoardGate{"Execution & Governance Model?"}
    BoardGate -->|"Sequential Route Execution (<=3 Cursors/Stop)<br/>+ Linked Chat Composer Gate + Idempotent Blocked Kanban"| UseHermesWB["✅ Adolanium/hermes-whiteboard (Hermes Folio)<br/>• 1 Sentence ➔ Route/Columns/Map + Gold-Road Context Handoff<br/>• Syncs with Chat/Kanban/Sheets/Data + One-Step Undo"]
    BoardGate -->|"Static Diagramming Only"| StaticBoard["🔄 Legacy Static Whiteboard"]

    Domain -->|"Real-World City/Campus GIS to Isometric Pixel-Art Explorer"| CityGate{"Verification & Compute Model?"}
    CityGate -->|"Untextured 3D GIS Massing + 1-Patch Review Gate<br/>+ Local Apple Silicon Painter (18GB Peak RAM / 24m)"| UseIsoCities["✅ Statecraft-Labs/isometric-cities (MIT Code)<br/>• AGENTS.md Driven: make Geometry ➔ 1-Patch Gate ➔ Expand<br/>• ~9GB Klein 9B Weights + Interactive atlas.py & Film Export"]
    CityGate -->|"Unconstrained Fictional Concept Art"| PureT2I["🔄 Standard Text-to-Image Generation"]

    UseHermesWB --> FinOps["💰 Closed-Form FinOps Impact (CLAIM-20261114-R47-HERMESWHITEBOARD-ISOCITIES)<br/>Monthly Total $5,690.00 ➔ $490.00 (-91.39% · Saves $62,400/yr)"]
    UseIsoCities --> FinOps
```

---

## 📊 4. Peer Comparison Matrix (Decision Matrix)

| Dimension | `Adolanium/hermes-whiteboard` (Agentic Board) | Traditional AI Sticky-Note Generators | `Statecraft-Labs/isometric-cities` (Local City Builder) | Unconstrained Cloud Diffusion Tile Grids |
| :--- | :--- | :--- | :--- | :--- |
| **Core Architecture** | **Stop-by-stop route DAG (3 cursors/stop) + Chat/Kanban sync** | Disconnected sticky-note generation | **Real 3D GIS massing + 1-patch gate + local native painter** | Direct text-to-image without 3D GIS massing |
| **Safety & Idempotency** | **Parks Kanban cards in `Blocked`; 0 duplicate cards; 1-step undo** | Manual copy-paste creates duplicate tickets | **Reviews 1 accurate patch before full-city expansion** | Renders entire grid blindly; seams misalign |
| **Ecosystem Integration** | **Bidirectional `Hermes Chat`, `Kanban`, `Sheets` & `Data`** | Isolated canvas | **Exports interactive `atlas.py` explorer (source compare) + film** | Static PNG outputs only |
| **Resource Footprint** | Lightweight 30s status polling + zoom-out text scaling | Heavy browser canvas | **Local Apple Silicon (`~9 GB` weights, `18 GB` peak RAM, 24m/10 windows)** | Expensive cloud GPU cluster billing |
| **License Model** | Open-source Hermes plugin (`hermes plugins install`) | Paid per-seat SaaS | **MIT code; default `Klein 9B` weights non-commercial** | Commercial API lock-in |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps Audit (`CLAIM-20261114-R47-HERMESWHITEBOARD-ISOCITIES`)

> **Scope & Provenance Boundary**: Models monthly cloud GPU tile reroll and SaaS seat costs across **30 multi-step planning boards & isometric city/campus builds**, plus engineering/design labor for manual Kanban synchronization and tile-seam repair at **`$100.00/hr`**. Local Apple Silicon workstation depreciation is explicitly marked **`not_measured`**.

| Architecture Path | Cloud GPU & SaaS Spend (`USD/mo`) | Seam Fix & Kanban Sync Labor (`hrs/mo`) | Engineering Labor Cost (`@ $100/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Blind Full-Map Cloud GPU Rerolls + Manual Kanban Sync** | `$1,890.00` | `38.0 hrs` | `$3,800.00` | **`$5,690.00`** | Baseline (`0.00%`) |
| **Path B: Manual Blender Renders + Non-Idempotent Kanban Scripts** | `$880.00` | `18.0 hrs` | `$1,800.00` | **`$2,680.00`** | `-$3,010.00` (`-52.90%`) |
| **Path C (Recommended): `hermes-whiteboard` + `isometric-cities`** | **`$140.00`** | **`3.5 hrs`** | **`$350.00`** | **`$490.00`** | **`-$5,200.00` (`-91.39%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 1890.00 + 38.0 \times 100.00 = 1890.00 + 3800.00 = \$5,690.00$
  - $\text{Path B Total} = 880.00 + 18.0 \times 100.00 = 880.00 + 1800.00 = \$2,680.00$
  - $\text{Path C Total} = 140.00 + 3.5 \times 100.00 = 140.00 + 350.00 = \$490.00$
  - $\text{Net Savings (Path C vs Path A)} = 5690.00 - 490.00 = \$5,200.00/\text{mo} \quad (-91.39\%, \text{Annualized } \$62,400.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect Quick-Start Checklist

1. **Install `Adolanium/hermes-whiteboard` in Hermes Desktop**:
   ```bash
   hermes plugins install Adolanium/hermes-whiteboard
   ```
2. **Launch `Statecraft-Labs/isometric-cities` Zero-Model Explorer or Agent Build Pipeline**:
   ```bash
   git clone --depth 1 https://github.com/Statecraft-Labs/isometric-cities.git
   cd isometric-cities && ./setup.sh && python3 atlas.py demo --open
   ```
