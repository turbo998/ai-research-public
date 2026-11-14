# Quota-Guarded Colab GPU MiniMax H3 Skill (`dseditor/h3-colab-skill`) & 4-Sheet 6-Platform Animated Sticker Studio (`fantuan-lab/animated-sticker-studio`) Deep-Dive & Selection FAQ

> **Document Metadata (2026-11-14 · Night Round 70 / Cumulative Round 253)**  
> - **Benchmark Style**: `ib-vs-ethernet-roce-selection-faq.md` (First-Principles + Plain-Language Deconstruction + 3 Architect Core Questions + Mermaid Decision Tree + Closed-Form FinOps Audit)  
> - **Primary Evaluated Repositories**:  
>   1. [`dseditor/h3-colab-skill`](https://github.com/dseditor/h3-colab-skill) (`★ 112`, Python skill for Claude, Codex, and Hermes that automates **MiniMax H3 2K multi-image editing, talking video, video extension (`@id` chaining), and voice-clone TTS** on your own **Google Colab L4/G4 GPU** or local 16GB+ **ComfyUI Desktop**: completes a full image+video+TTS batch on L4 in **`10.1 minutes` for `~0.5` compute units** while enforcing a **GPU allowlist [preventing A100 CLI typo charges], `<5`-unit pre-boot cutoff, offline `selftest_graph.py` validation, and an out-of-process 15-minute idle auto-shutdown timer**)  
>   2. [`fantuan-lab/animated-sticker-studio`](https://github.com/fantuan-lab/animated-sticker-studio) (`★ 66`, MIT Claude Code & Codex skill turning **1 character image into a 24-sticker animated pack using just 4 image-generation calls (`1 character sheet + 3 pose sheets`)**: combines `#1–16` procedural motion with `#17–24` true frame-by-frame animation and exports size-verified bundles for **WeChat (`240×240 ≤500 KB`), Telegram, LINE, Discord, Slack, and WhatsApp**)  
> - **Visual Architecture Diagram**: [`assets/github-ai-radar-2026-11-14-r70-h3colab-stickerstudio.svg`](../../../assets/github-ai-radar-2026-11-14-r70-h3colab-stickerstudio.svg)  
> - **Audit Contract ID**: `CLAIM-20261114-R70-H3COLAB-STICKERSTUDIO` (local workstation base hardware depreciation is explicitly marked `not_measured`)

---

## 📌 1. Executive Summary (Understand the Essence in 3 Minutes)

1. **How can a laptop without a discrete GPU run heavy MiniMax H3 multimodal workflows (2K image editing, talking video, extensions, and TTS) on Google Colab without risking orphaned GPU instances or accidental A100 charges? How does `dseditor/h3-colab-skill` protect your compute units?**  
   - **Plain-Language Essence**: Google AI Pro includes ~400 Colab compute units/month (`~1.5 units/hr` on an L4 GPU = ~300 hours). However, automating Colab via CLI has two dangerous traps: a typo in the GPU flag silently provisions an expensive **A100**, and a crashed or closed chat session leaves the remote GPU running until your quota hits zero!  
   - **First-Principles Breakthrough in `h3-colab-skill`**:
     - **`@id`-Chained Single-Boot Batching (`10.1 Min` = `~0.5 Units` on L4) + Shared Local ComfyUI Mode**: Boots the Colab L4, installs ComfyUI in `<40s`, loads models in `3.5m`, and chains 2K 2-reference image editing (`112s`), 5s 480P talking video (`160s`), and 6s voice-clone TTS (`17s`) in one `10.1-minute` run (`~0.5` compute units). If you have a local 16GB+ NVIDIA GPU, `h3local.py` runs locally against `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Shared\models` with zero duplicate downloads.
     - **4-Layer Quota Watchdog**: Refuses to boot if `<5` compute units remain; strictly validates GPU names against `L4/G4/A100/H100` so CLI typos never default to A100; runs `selftest_graph.py` offline without a GPU to catch broken ComfyUI graphs before booting; and spawns an **independent host timer that shuts down the Colab instance after 15 minutes of inactivity even if the agent chat closes**!
2. **Why does generating 24 chat stickers one by one cause character drift and platform upload rejections — and how does `fantuan-lab/animated-sticker-studio` ship a 24-sticker animated pack across 6 messaging platforms in just 4 image-generation calls?**  
   - **Plain-Language Essence**: Calling an image model 24 separate times drifts character proportions, while WeChat (`240×240 ≤500 KB` GIF), Telegram, LINE, Discord, Slack, and WhatsApp each enforce incompatible resolution and file-size ceilings.  
   - **First-Principles Breakthrough in `animated-sticker-studio`**:
     - **`1 Character Sheet + 3 Pose Sheets = 4 Calls` for 24 Hybrid-Animated Stickers**: Synthesizes a 24-pack (proven on the *Onigiri Cat* WeChat submission) using `#1–16` procedural motion and `#17–24` true frame-by-frame animation (waving paws, streaming tears, opening yawns) with zero manual retouching, then auto-compresses and verifies every file against all 6 platforms' upload specifications.
3. **Closed-Form FinOps Audit Conclusion (`CLAIM-20261114-R70-H3COLAB-STICKERSTUDIO`)**:  
   - Modeled for **25 multimodal H3 video/TTS batches and 6-platform animated sticker packs/month** (at **`$95.00/hr`** engineering labor): migrating from **Path A** (commercial per-second video APIs + orphaned cloud GPU instances and 24-call per-sticker generation: **`$5,100.00/mo`**, comprising `$1,680.00` GPU/API spend + `36.0h` manual Colab/compression labor `$3,420.00`) to **Path C** (`h3-colab-skill` 0.5-unit auto-shutdown batching + `animated-sticker-studio` 4-sheet pipeline: **`$427.50/mo`**, comprising `$95.00` Colab/API spend + `3.5h` review labor `$332.50`) saves **`$4,672.50/mo`** (**`-91.62%`**, or **`$56,070.00/yr`**) and cuts engineering hours by **`90.28%`**.

![h3-colab-skill & animated-sticker-studio Architecture Overview](../../../assets/github-ai-radar-2026-11-14-r70-h3colab-stickerstudio.svg)

---

## 💬 2. Three Architect Core Questions (Q1–Q3 Deep Dive)

### Q1: Why must `dseditor/h3-colab-skill`'s 15-minute idle shutdown timer run as an independent host process rather than inside the AI agent's conversation loop?

1. **Surviving Chat Termination & User Disconnection**:  
   - An LLM agent only executes tool calls during an active turn. If the user closes their laptop while the agent waits for a reply on whether to keep the warm GPU alive, an in-conversation timer never fires. Spawning an independent OS-level watchdog process guarantees deterministic Colab teardown after 15 idle minutes (or immediately on job failure).

---

### Q2: How does `scripts/selftest_graph.py` prevent wasted Colab boot cycles?

1. **Zero-GPU Offline ComfyUI Graph Validation**:  
   - Booting a Colab instance and staging 60 GB of weights takes ~4.5 minutes. `selftest_graph.py` validates every generated ComfyUI workflow graph locally before provisioning any cloud GPU.

---

### Q3: How does `fantuan-lab/animated-sticker-studio` combine cost efficiency with frame-by-frame expressiveness across 6 platforms?

1. **Multi-Pose Sheet Batching (`4 Calls`) + Hybrid Procedural/Frame Animation**:  
   - By packing poses into 3 multi-grid pose sheets anchored to 1 character sheet, the skill cuts image API calls by 6× while rendering `#1–16` with procedural motion and `#17–24` with multi-frame keyframe animation, followed by automated per-platform byte-ceiling compression.

---

## 🧭 3. Architecture Decision Tree & Topology (Mermaid)

```mermaid
flowchart TD
    Start["MiniMax H3 Multimodal GPU Orchestration & 6-Platform Animated Sticker Production"] --> Task{"Target Creative Workload?"}

    Task -->|"MiniMax H3 2K Image Edit, Talking Video, Extensions & Voice-Clone TTS"| H3Gate{"Local Hardware Profile?"}
    H3Gate -->|"Thin-and-Light Laptop: Dispatch to Google Colab L4/G4 GPU"| UseColabH3["✅ dseditor/h3-colab-skill (Colab Remote Mode)<br/>• 10.1m full batch on L4 (~0.5 compute units) via @id job chaining<br/>• A100 typo guard + <5 unit cutoff + 15m out-of-process auto-shutdown"]
    H3Gate -->|"Workstation with >=16GB NVIDIA GPU & ComfyUI Desktop"| UseLocalH3["✅ dseditor/h3-colab-skill (h3local.py Local Mode)<br/>• Shares models in ComfyUI-Shared/models with zero cloud wait"]

    Task -->|"1 Character Image ➔ 24 Animated Stickers for WeChat/TG/LINE/Discord/Slack/WA"| StickerGate{"Export Scope?"}
    StickerGate -->|"4 Image Calls (1 Character + 3 Pose Sheets) + 6-Platform Spec Compression"| UseStickerStudio["✅ fantuan-lab/animated-sticker-studio (MIT · Python)<br/>• #1–16 procedural motion + #17–24 frame-by-frame animation<br/>• Auto-compresses under platform limits (e.g., WeChat 240x240 <=500KB)"]
    StickerGate -->|"Single static avatar"| SingleAvatar["🔄 Single Image Prompt"]

    UseColabH3 --> FinOps["💰 Closed-Form FinOps Impact (CLAIM-20261114-R70-H3COLAB-STICKERSTUDIO)<br/>Monthly Total $5,100.00 ➔ $427.50 (-91.62% · Saves $56,070/yr)"]
    UseLocalH3 --> FinOps
    UseStickerStudio --> FinOps
```

---

## 📊 4. Peer Comparison Matrix (Decision Matrix)

| Evaluation Dimension | `dseditor/h3-colab-skill` (Guarded Colab/Local H3) | Manual Colab / Commercial Video APIs | `fantuan-lab/animated-sticker-studio` (6-Platform 24-Pack) | 24-Call Individual Prompts + Manual AE |
| :--- | :--- | :--- | :--- | :--- |
| **Batching & Efficiency** | **Chains image+video+TTS via `@id` (`10.1m` = `~0.5` L4 units)** | Manual browser uploads or expensive per-second APIs | **4 image calls (`1 char + 3 pose sheets`) produce 24 stickers** | 24+ separate calls cause severe character drift |
| **Quota & Spec Guardrails** | **GPU allowlist + `<5`-unit cutoff + 15m independent shutdown timer** | CLI typos boot A100s; forgotten tabs drain quota | **Enforces exact dimensions, FPS & byte caps across 6 platforms** | Manual exports fail WeChat `500 KB` / Telegram caps |
| **Motion & Hybrid Execution** | **Seamless switch between Colab L4/G4 & local ComfyUI Desktop** | Siloed cloud vs local model directories | **`#1–16` procedural motion + `#17–24` frame-by-frame animation** | Static images or rigid uniform pans |
| **Automation & Verification** | **Offline `selftest_graph.py` + end-to-end agent lifecycle** | Requires human babysitting | **MIT open-source; self-checks output and zips upload bundle** | Hours of manual slicing and GIF compression |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261114-R70-H3COLAB-STICKERSTUDIO`)

> **Scope & Boundary Declaration**: This synthetic FinOps model covers monthly commercial video API, orphaned cloud GPU, and image-generation spend across **25 multimodal H3 batches and 6-platform animated sticker packs** plus engineering labor for **Colab instance supervision and multi-platform sticker slicing/compression** (at **`$95.00/hr`**); local workstation hardware depreciation is explicitly marked **`not_measured`**.

| Architecture Path | GPU & API Spend (`USD/mo`) | Supervision & Multi-Platform Slicing Labor (`hrs/mo`) | Engineering Labor Cost (`@ $95/hr`) | Total Monthly Cost (`USD/mo`) | Net Savings vs. Path A (`USD/mo` & `%`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Commercial Video APIs + Orphaned GPUs + 24-Call Packs** | `$1,680.00` | `36.0 hrs` | `$3,420.00` | **`$5,100.00`** | Baseline (`0.00%`) |
| **Path B: Manual Colab Clicking + Single-Platform Scripts** | `$790.00` | `17.0 hrs` | `$1,615.00` | **`$2,405.00`** | `-$2,695.00` (`-52.84%`) |
| **Path C (Recommended): `h3-colab-skill` + `sticker-studio`** | **`$95.00`** | **`3.5 hrs`** | **`$332.50`** | **`$427.50`** | **`-$4,672.50` (`-91.62%`)** |

- **Closed-Form Verification Equations**:
  - $\text{Path A Total} = 1680.00 + 36.0 \times 95.00 = 1680.00 + 3420.00 = \$5,100.00$
  - $\text{Path B Total} = 790.00 + 17.0 \times 95.00 = 790.00 + 1615.00 = \$2,405.00$
  - $\text{Path C Total} = 95.00 + 3.5 \times 95.00 = 95.00 + 332.50 = \$427.50$
  - $\text{Net Savings (Path C vs Path A)} = 5100.00 - 427.50 = \$4,672.50/\text{mo} \quad (-91.62\%, \text{Annualized } \$56,070.00/\text{yr})$

---

## 🛠️ 6. AI Solution Architect Actionable Checklist

1. **Validate ComfyUI graphs offline before booting Colab GPUs in `dseditor/h3-colab-skill`**:
   ```bash
   python scripts/selftest_graph.py
   ```
2. **Generate 6-platform animated sticker packs in 4 image calls with `fantuan-lab/animated-sticker-studio`**:
   - Supply one character reference image to generate 1 character sheet + 3 pose sheets and export verified packages for WeChat, Telegram, LINE, Discord, Slack, and WhatsApp.
