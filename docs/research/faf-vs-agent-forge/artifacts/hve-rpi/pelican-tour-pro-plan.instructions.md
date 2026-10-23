<!-- markdownlint-disable-file -->
---
description: "Implementation plan for Pelican Tour Pro (HVE-Core RPI Phase 2)"
applyTo: "demo-hve-pelican.html"
---

# Implementation Plan: Pelican Tour Pro (`pelican-tour-pro`)

* **Date**: 2026-10-24
* **Agent**: `task-planner` + `Plan Validator` (`microsoft/hve-core@3.3.101`, RPI Phase 2)
* **Research Reference**: `.copilot-tracking/research/2026-10-24/pelican-tour-pro-research.md`
* **Details Reference**: `.copilot-tracking/details/2026-10-24/pelican-tour-pro-details.md`
* **Planning Log**: `.copilot-tracking/plans/logs/2026-10-24/pelican-tour-pro-log.md`

---

## Phase 1: Longitudinal Cycling Physics & 11-Speed Drivetrain Engine (Sequential)

- [x] **Step 1.1**: Implement `CyclingPhysicsEngine` computing $F_{\text{gravity}}$, $F_{\text{rolling}}$, and $F_{\text{aero}}$ across road gradient $\theta_{\text{grade}} \in [-10\%, +15\%]$, cadence $\text{RPM} \in [30, 130]$, 11-speed cassette gear ratios ($1.2\times \text{ to } 4.5\times$), and headwind $v_{\text{wind}} \in [-20, +50]\text{ km/h}$.
- [x] **Step 1.2**: Implement analytical 2-bone Law-of-Cosines IK solver (`solvePelicanLegIK`) with forward avian knee topology (`tibiotarsus` + `tarsometatarsus`) and posture-dependent hip/shoulder anchors (**Upright Climb**, **Aero Tuck**, **Out-of-Saddle Sprint**, **No-Hands Coast**).

## Phase 2: Wind-Tunnel Streamline & Multi-Terrain Canvas2D Renderer (Parallelizable)

- [x] **Step 2.1**: Render procedural terrain slope geometry (Alpine Hors Catégorie Climb, Coastal Cobblestone Classic, Cyber-Velodrome Wind Tunnel, Descending Switchback) with dynamic slope rotation of the entire bicycle + rider assembly.
- [x] **Step 2.2**: Implement real-time Laminar/Turbulent Wind-Tunnel smoke streamlines flowing over the pelican's beak, aero helmet, gular pouch, and carbon deep-section wheels, with live $C_d A$ drag wake vectors.

## Phase 3: Interactive Telemetry HUD, RPI Phase Inspector & Adversarial Challenge Mode (Sequential)

- [x] **Step 3.1**: Build real-time scrolling Power (Watts) & Avian Heart Rate (BPM) sparkline chart, 11-speed electronic shifter (`Di2 Up/Down`), posture selector, and `postMessage` synchronization API for the 3-Way Pelican Arena.
- [x] **Step 3.2**: Embed the interactive HVE-Core **RPI + Task Challenger Inspector** allowing users to inspect `.copilot-tracking/research`, `plans`, `details`, `changes`, `reviews`, and `challenges` directly inside the workbench.
