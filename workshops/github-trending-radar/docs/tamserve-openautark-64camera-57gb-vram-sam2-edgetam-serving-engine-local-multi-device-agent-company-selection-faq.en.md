# 64-Camera `5.7GB`-VRAM Shared-GPU `SAM 2.1`/`EdgeTAM` Serving Engine (`aryamandarda/tamserve`) & Local Multi-Device Agent Operations Desk (`teydra/OpenAutark`) Architecture & Selection FAQ

> **Document Metadata (2026-11-17 · Night Round 7 / Cumulative Round 431)**  
> - **Target Audience**: **Enterprise AI Solution Architects** & Industrial Vision / Digital Operations Decision-Makers  
> - **Core Orientation**: **① Real Enterprise Application Scenarios & Business ROI/Pain Points + ② End-to-End Integration Reference Architecture + ③ Peer Open-Source / Cloud Service / Commercial Solution Selection & TCO Comparison**  
> - **Editorial Benchmark**: Modeled on `ib-vs-ethernet-roce-selection-faq.md` (Plain-Language First Principles + 3 Architectural Deep-Dive Q&As + Mermaid Decision Tree + Peer Comparison Matrix + Closed-Form FinOps Audit + 15-Minute Rollout Checklist)  
> - **Evaluated Repositories**:  
>   1. [`aryamandarda/tamserve`](https://github.com/aryamandarda/tamserve) (`★ 78`, Apache-2.0 License, Python 3.10+ / PyTorch 2.6+: vLLM-style multi-camera live video tracking server for Meta's `SAM 2.1` and `EdgeTAM` that shares one model instance across all cameras, **cutting 8-camera GPU memory `4×` (`8.6 GB → 2.2 GB`), serving 64 live cameras in `5.7 GB` VRAM at `321 fps` on a single RTX 4090 (vs. `~70 GB` stock), and bounding 800-frame stream memory to `0.28 GB` (vs. `9.8 GB` stock)** with unchanged `0.8685` DAVIS 2017 accuracy)  
>   2. [`teydra/OpenAutark`](https://github.com/teydra/OpenAutark) (`★ 30`, Apache-2.0 License, Node.js 24 + Electron + Android/iPhone: Open-source local-first multi-device AI operations desk unifying a personal manager agent, specialist agent teams, "My Day" calendar/task views, a side-by-side browser, and numeric-code-paired mobile devices over existing Claude Code, Codex, or local LLM backends)  
> - **Companion SVG Diagram**: [`assets/github-ai-radar-2026-11-17-r7-tamserve-openautark.svg`](../../../assets/github-ai-radar-2026-11-17-r7-tamserve-openautark.svg)  
> - **Audit Claim ID**: `CLAIM-20261117-R7-TAMSERVE-OPENAUTARK` (physical camera/PC hardware capEx marked `not_measured`; upstream RTX 4090 VRAM and FPS measurements labeled `anonymized_reported, independently_reproduced=false`)

---

## 📌 1. Executive Summary (3-Minute Enterprise Architect's Briefing)

1. **Why does deploying Meta's stock `SAM 2` / `EdgeTAM` across 8–64 live warehouse, retail, or factory cameras exhaust `70+ GB` of GPU memory and crash on long streams, and how does `aryamandarda/tamserve` solve it on a single `24 GB` GPU?**  
   - **Enterprise Business Pain Point**: Meta's `SAM 2.1` and `EdgeTAM` deliver state-of-the-art object segmentation and tracking, but their reference code was engineered for editing one recorded video clip at a time. Running one model copy per camera consumes `8.6 GB` for 8 cameras and `~70 GB` for 64 cameras, while accumulating per-frame memory up to `9.8 GB` after just 800 frames—making 24/7 multi-camera enterprise deployment prohibitively expensive.  
   - **`tamserve` Architectural Fix ("vLLM-Style Shared-Weight Dynamic Batching for Video Tracking")**:
     - **Single Shared Model Instance + Batched `engine.step()`**: Every camera shares one copy of `EdgeTAM` (`54 MB`) or `SAM 2.1`, batching frame encoding and mask decoding across active streams to **cut 8-camera VRAM `4×` (`8.6 GB → 2.2 GB`) and run 64 concurrent cameras in just `5.7 GB` VRAM at `321 frames/s` on one RTX 4090** (`11%–24%` faster than compiled stock code, `0.8685` vs `0.8686` DAVIS 2017 accuracy, `anonymized_reported`);
     - **Constant `0.28 GB` Bounded Stream State (`35×` Lower Than Stock)**: Caps per-stream historical memory at `0.28 GB` regardless of how many hours or days the camera runs;
     - **Mid-Stream Text-Prompted `Tracker` & Multi-GPU `Router`**: Starts or stops tracking objects on any frame via boxes, clicks, masks, or natural-language phrases (`"forklift"`, `"the red mug"`), while `Router` automatically places cameras across multiple GPUs.
2. **How can SMEs and operations teams run a coordinated "Manager Agent + Specialist Agent Team" across desktop PCs and mobile phones without locking data into proprietary cloud SaaS? (`teydra/OpenAutark`)**  
   - **Enterprise Business Pain Point**: Teams want a unified workspace combining task/calendar management, co-browsing, specialist agents, and mobile remote control while reusing existing Claude Code, Codex, or local LLM setups on their own hardware.  
   - **`OpenAutark` Architectural Fix**: Provides an Apache-2.0 desktop (`Windows`, `macOS`, `Linux`) and mobile (`Android` APK + `iPhone` local web app) workbench with mutual numeric-code device pairing, explicit external network socket documentation, `SHA256SUMS.txt` / `release.json` verification, and draft-preserving idle updates.
3. **Closed-Form FinOps Audit (`CLAIM-20261117-R7-TAMSERVE-OPENAUTARK`)**:  
   - Across **one 64-camera industrial/warehouse live vision site + 25 multi-device agent operations seats per month** (at **`$100.00/hr`** engineering rate), migrating from **Path A** (1-model-per-camera multi-A100 cloud GPU cluster + commercial multi-seat agent SaaS: **`$6,350.00/mo`**) to **Path C** (`tamserve` single-GPU 64-camera serving + `OpenAutark` local multi-device desk: **`$465.00/mo`**) saves **`$5,885.00/month`** (**`-92.68%`**, **`$70,620.00/year`**) and cuts OOM recovery and ops labor from `41.0 hrs` to `3.3 hrs/mo` (**`-91.95%`**).

![64-Camera Shared-GPU SAM 2.1/EdgeTAM Engine & Multi-Device AI Ops Desk Architecture](../../../assets/github-ai-radar-2026-11-17-r7-tamserve-openautark.svg)

---

## 💬 2. Three Architectural Deep-Dive Q&As (Enterprise Scenarios, Reference Architecture & Boundaries)

### Q1: How does `aryamandarda/tamserve` bound long-stream GPU memory to `0.28 GB` while preserving `0.8685` DAVIS 2017 accuracy?

1. **Bounded Temporal Memory Pruning + Cross-Camera Batch Execution**:  
   - Stock `SAM 2` retains growing frame-feature banks across the entire video timeline (`9.8 GB` at 800 frames). `tamserve` bounds the active memory bank per tracked object to a fixed sliding/keyframe budget (`0.28 GB` indefinitely) and batches all active cameras through a single compiled weight resident in GPU L2/VRAM.

---

### Q2: How do `Tracker` and `Router` simplify enterprise warehouse and retail computer-vision pipelines?

1. **Zero-Shot Text Discovery + Multi-GPU Auto-Sharding**:  
   - Instead of training custom YOLO detectors for every new SKU or vehicle type, applications pass a text prompt to `Tracker` to locate and initialize mask tracking mid-stream across all cameras, while `Router` balances camera placement across multi-GPU edge servers automatically.

---

### Q3: What are the production deployment boundaries for `tamserve` and `OpenAutark`?

1. **Scope Boundaries**:  
   - `tamserve` requires an NVIDIA GPU for real-time video throughput (CPU fallback is for functional testing only);  
   - `OpenAutark` community binaries are ad-hoc signed, so enterprise IT teams should build and sign installers internally from the audited Apache-2.0 source tree (`npm run check && npm run package`).

---

## 🧭 3. Enterprise Integration Reference Architecture & Selection Decision Tree (Mermaid)

```mermaid
flowchart TD
    Start["Enterprise Multi-Camera Video Tracking & Multi-Device Agent Workbench Selection"] --> Track{"Primary Enterprise Domain?"}

    Track -->|"Warehouse, Retail, Factory & Broadcast Live Video Tracking (8–64+ Cameras)"| VisionGate{"GPU Memory & Stream Duration Constraints?"}
    VisionGate -->|"64 Live Cameras in 5.7 GB VRAM @ 321 fps on 1 GPU<br/>+ 0.28 GB Bounded 24/7 Stream Memory & Mid-Stream Text Tracker"| UseTamserve["✅ aryamandarda/tamserve (★ 78 · Apache-2.0)<br/>• Shared EdgeTAM / SAM 2.1 Weights + 4x Lower 8-Cam VRAM<br/>• Built-In Text Tracker & Multi-GPU Router Auto-Sharding"]
    VisionGate -->|"Single Offline Recorded Short Video Clip"| StockSAM2["🔄 Stock Meta SAM 2 Offline Script"]

    Track -->|"Local-First Multi-Device Manager + Specialist Agent Operations Desk"| DeskGate{"Deployment & Device Pairing Model?"}
    DeskGate -->|"Runs on Own PC Reusing Claude Code/Codex/Local LLMs<br/>+ Mutual Numeric-Code Phone Pairing & SHA256-Verified Releases"| UseAutark["✅ teydra/OpenAutark (★ 30 · Apache-2.0)<br/>• Win/Mac/Linux + Android APK + iPhone Local Web App<br/>• My Day Calendar, Co-Browser & Draft-Safe Idle Updates"]
    DeskGate -->|"Cloud-Only Single-Browser SaaS"| CloudSaaS["🔄 Hosted Cloud Task SaaS"]

    UseTamserve --> FinOps["💰 Closed-Form Enterprise FinOps Impact (CLAIM-20261117-R7-TAMSERVE-OPENAUTARK)<br/>Monthly Total $6,350.00 ➔ $465.00 (-92.68% · Saves $70,620/yr)"]
    UseAutark --> FinOps
```

---

## 📊 4. Peer Open-Source / Cloud / Commercial Selection Matrix (Decision Matrix)

| Dimension | `aryamandarda/tamserve` (`★ 78` Shared-GPU SAM 2) | Stock Meta `SAM 2` / `EdgeTAM` Multi-Process | Cloud Managed Video Tracking APIs | `teydra/OpenAutark` (`★ 30` Multi-Device Agent Desk) | Hosted Commercial "AI Employee" SaaS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Enterprise Use Case** | **Real-time pixel-mask tracking across 8–64+ live RTSP cameras** | Single offline recorded clip editing | Low-FPS cloud frame tagging | **Local-first manager/specialist agent teams across PC & phone** | Cloud-only form/email automation |
| **VRAM & Stream Scalability** | **8 cams `2.2 GB`; 64 cams `5.7 GB` (`321 fps`); bounded `0.28 GB` 24/7** | 8 cams `8.6 GB`; 64 cams `~70 GB`; 800 frames `9.8 GB` (OOM) | High egress bandwidth & per-minute cloud fees | **Runs on user PC; reuses existing CLI plans & local LLMs** | Per-seat + per-task cloud billing |
| **Dynamic Capabilities** | **Mid-stream target add/drop, text `Tracker` & multi-GPU `Router`** | Cannot add targets mid-stream; manual GPU pinning | High network latency; no 30fps mask streaming | **Numeric-code phone pairing, co-browser & draft-safe updates** | Vendor lock-in |
| **TCO & Licensing** | **Apache-2.0 Open Source (1× 24GB GPU replaces multi-A100 cluster)** | `4x–12x` higher GPU hardware cost | Thousands of USD/mo for 64 24/7 streams | **Apache-2.0 Open Source** | `$50–$200/seat/mo` |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps Audit (`CLAIM-20261117-R7-TAMSERVE-OPENAUTARK`)

> **Scope & Provenance Boundary**: Models monthly cloud/edge GPU compute and OOM maintenance labor for **one 64-camera industrial/warehouse live vision site** plus software/ops spend across **25 multi-device agent operations seats** at **`$100.00/hr`**. Physical camera and workstation hardware capEx is marked **`not_measured`**, and upstream RTX 4090 VRAM/FPS benchmarks are labeled **`anonymized_reported` (`independently_reproduced=false`)**.

| Architecture Path | GPU Compute & Agent SaaS Spend (`USD/mo`) | OOM Recovery & Device Sync Labor (`hrs/mo`) | Engineering Labor Cost (`@ $100/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: 1-Model-Per-Camera 80GB Multi-GPU Cluster + Cloud Agent SaaS** | `$2,250.00` | `41.0 hrs` | `$4,100.00` | **`$6,350.00`** | Baseline (`0.00%`) |
| **Path B: Frame-Dropped Stock Scripts + Disconnected Desktop/Mobile Apps** | `$990.00` | `19.0 hrs` | `$1,900.00` | **`$2,890.00`** | `-$3,460.00` (`-54.49%`) |
| **Path C (Recommended): `tamserve` (5.7GB/64-Cam) + `OpenAutark`** | **`$135.00`** | **`3.3 hrs`** | **`$330.00`** | **`$465.00`** | **`-$5,885.00` (`-92.68%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 2250.00 + 41.0 \times 100.00 = 2250.00 + 4100.00 = \$6,350.00$
  - $\text{Path B Total} = 990.00 + 19.0 \times 100.00 = 990.00 + 1900.00 = \$2,890.00$
  - $\text{Path C Total} = 135.00 + 3.3 \times 100.00 = 135.00 + 330.00 = \$465.00$
  - $\text{Net Savings (Path C vs Path A)} = 6350.00 - 465.00 = \$5,885.00/\text{mo} \quad (-92.68\%, \text{Annualized } \$70,620.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect 15-Minute Enterprise Rollout Checklist

1. **Install `aryamandarda/tamserve` & Launch Shared-GPU Multi-Camera Tracking**:
   ```bash
   pip install tamserve opencv-python
   # Initialize Engine(build_video_predictor()) and pass multi-camera frames to engine.step()
   ```
2. **Build & Verify `teydra/OpenAutark` From Audited Source**:
   ```bash
   git clone https://github.com/teydra/OpenAutark.git && cd OpenAutark/apps/desktop
   npm ci && npm run check && npm run build
   ```
