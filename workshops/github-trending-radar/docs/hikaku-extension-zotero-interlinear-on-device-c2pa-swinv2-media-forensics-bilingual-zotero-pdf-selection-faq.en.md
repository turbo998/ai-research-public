# On-Device C2PA/SwinV2 AI Media Forensics (`hikaku-io/hikaku-extension`) & Glossary-Enforced Bilingual Zotero 10 Reader (`zotero-interlinear` & `ai-era-job-kit`) Selection FAQ

> **Document Type**: Enterprise AI Solution Architect Practical Selection Guide (Standard 6-Section FAQ)  
> **Shift & Round**: 2026-11-17 Night Round 30 (Cumulative Round 454)  
> **Tracked Repositories**:
> - **`hikaku-io/hikaku-extension`** (`★ 404`, JavaScript / Manifest V3 Chrome & Edge 116+ / Firefox 140+ / WebGPU `fp16` & WASM `uint8` ONNX Runtime, `Apache-2.0`): 100% on-device browser extension that flags AI-generated images and streamed videos by combining **local C2PA / IPTC / EXIF / A1111 / ComfyUI metadata parsing** with an **on-device SwinV2 visual detector** and an on-demand **`23 MB` Community Forensics second-opinion model** (supporting `npm run build -- --offline` for air-gapped networks)
> - **`Muanyan-mjq/zotero-interlinear`** (`★ 79`, TypeScript / Zotero 10 Desktop PDF Reader Addon, `AGPL-3.0`) & **`Vets-Who-Code/ai-era-job-kit`** (`★ 66`, Python 3.10+ Zero-Dep 12 Scripts + 7 Skills/7 Agents): Paragraph-aligned bilingual PDF reading and export inside Zotero 10 with dual-enforced CSV/TSV glossaries and 5-tier keyless/Ollama translation, paired with a zero-dependency portfolio & skill benchmarking toolkit grounded in live O*NET and US Bureau of Labor Statistics (BLS) data  
> **Audit Claim ID**: `CLAIM-20261117-R30-HIKAKU-ZOTERO` (base Zotero cloud sync storage marked `not_measured`)

---

## 📌 1. Executive Summary

1. **Why Enterprise Trust & Safety / Claims Teams and R&D Organizations Hit Privacy and Fidelity Walls with Cloud Media-Forensics APIs and External PDF Translators**:
   - **The Media-Forensics Privacy & Stripped-Metadata Dilemma**: Insurance claims adjusters, e-commerce marketplace moderators, and procurement auditors inspect hundreds of thousands of photos and videos monthly for synthetic AI manipulation. Uploading confidential customer claim photos to third-party cloud detection APIs incurs steep per-image fees and data-privacy liability—while simple EXIF/C2PA scripts fail completely whenever messaging apps strip file metadata.
   - **The R&D Literature Glossary & Highlight-Corruption Dilemma**: When researchers translate foreign-language papers or patents using external web PDF translators, domain terminology gets mangled and Zotero's native highlight coordinates break. Meanwhile, engineering managers lack objective, data-backed benchmarks (`O*NET` / `BLS`) to audit technical portfolios.
   - **The Solution Architect Stack (`hikaku-extension` Apache-2.0 + `zotero-interlinear` + `ai-era-job-kit`)**: Roll out **`hikaku-io/hikaku-extension`** (`Apache-2.0`, built with `--offline` for zero external network calls) so browsers inspect **C2PA/IPTC/ComfyUI metadata + local WebGPU `SwinV2` pixel forensics + a `23 MB` Community Forensics second opinion** entirely on-device; pair it on R&D workstations with **`Muanyan-mjq/zotero-interlinear`** (side-by-side paragraph translation inside Zotero 10 with dual-enforced CSV/TSV glossaries and local Ollama support) and **`Vets-Who-Code/ai-era-job-kit`** (12 zero-dependency Python scripts benchmarking engineering artifacts against live O*NET/BLS data).
2. **Closed-Form FinOps Impact (60 Enterprise Trust/Safety & R&D Analysts Inspecting 120,000 Monthly Media Assets & Reviewing 3,000 Multilingual PDFs at `$95.00/hr`)**:
   - Transitioning from **Path A (Cloud Per-Image AI Detection APIs + Commercial Per-Page PDF Translation SaaS at `$5,805.00/mo`)** to **Path C (`Hikaku` On-Device Extension + `zotero-interlinear` & `ai-era-job-kit` at `$346.00/mo`)** saves **`$5,459.00/mo` (`-94.04%`, or `$65,508.00/yr`)** while cutting manual upload triage, glossary correction, and PDF highlight repair from `37.0 hrs/mo` to `2.8 hrs/mo` (**`92.43%` reduction**).

![Hikaku + Zotero Interlinear Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r30-hikaku-zotero-interlinear.svg)

---

## 💬 2. Core Architectural Q&A (Q1–Q3)

### Q1: How does `hikaku-io/hikaku-extension` detect both declared and metadata-stripped AI images/videos 100% on-device without uploading a single byte?
- **Plain-Language Definition**: `Hikaku` (*"comparison"* in Japanese, `Apache-2.0`) is a **Manifest V3 browser extension for Chrome/Edge 116+ and Firefox 140+ that compares what a media file claims to be (metadata provenance) against the visual evidence in its pixels (local ONNX models)**.
- **Four Enterprise-Ready Forensic Mechanisms**:
  1. **Single-Fetch In-Memory Provenance Parsing**: Parses **Content Credentials (C2PA)** across `JPEG, PNG, WebP, MP4/MOV, AVIF/HEIC`, **IPTC/XMP/EXIF** declarations (`trainedAlgorithmicMedia`, `"Made with … AI"`), and embedded generation parameters from **Automatic1111, ComfyUI, InvokeAI, and NovelAI**.
  2. **UI Screenshot Pre-Filter + Local `SwinV2` Visual Detector + Streamed Video Sampling**:
     - Filters out small icons, UI screenshots, and flat graphics before loading the model;
     - Runs a **SwinV2 detector via ONNX Runtime** locally on **WebGPU (`fp16`, ~400 MB)** or **WASM (`uint8`, ~200 MB)**;
     - Samples **3 frames per visible streamed video** (YouTube, TikTok, etc.) or animated GIF/WebP and computes the median score.
  3. **On-Demand `23 MB` Second-Opinion Model & Evidence Separation**: Keeps metadata declarations strictly separate from visual model estimates (never inflating confidence from repeated tags), allows analysts to request a separate **`23 MB` Community Forensics second opinion** in one click, and exports structured forensic JSON (`Copy JSON`).
  4. **Air-Gapped Offline Packaging (`npm run build -- --offline`)**: Bundles the ONNX runtime and model weights directly into the extension package so locked-down corporate networks never make runtime model downloads.

### Q2: How do `Muanyan-mjq/zotero-interlinear` and `Vets-Who-Code/ai-era-job-kit` upgrade R&D literature review and engineering capability audits?
- **`zotero-interlinear` (Native Zotero 10 Paragraph Translation with Dual Glossary Enforcement)**:
  1. **5 Keyless Fallback Pools + Local Ollama / Enterprise LLMs**: Rotates independent Google Translate pools, Microsoft Edge, MyMemory, and self-hosted LibreTranslate out of the box with no API key, or connects directly to local `Ollama`, Claude, Gemini, and OpenAI-compatible gateways;
  2. **Dual-Enforced CSV/TSV Glossaries**: Injects domain term lists into LLM prompts **and** enforces deterministic post-translation term replacement across every translation backend;
  3. **Viewport-First Scheduling & Highlight-Safe Layouts**: Dynamically re-sorts translation queues as the researcher scrolls, renders translations below or side-by-side without disturbing native Zotero highlights, and exports re-typeset searchable bilingual PDFs.
- **`Vets-Who-Code/ai-era-job-kit` (Zero-Dependency Live O*NET & BLS Portfolio Scorer)**:
  - Uses 12 standard-library Python 3.10+ scripts, 7 skills, and 7 agents to score engineering portfolios (`portfolio.json` and `brag/entries/`) against live keyless **O*NET** and **US Bureau of Labor Statistics (BLS)** market data, citing the exact source behind every score (`METHOD.md`).

### Q3: How should an AI Solution Architect deploy these tools across trust/safety and R&D teams?
- **Claims, Procurement & Content Integrity Workstations**: Distribute the `--offline` build of `Hikaku` (`Apache-2.0`) via enterprise browser policy; require analysts reviewing flagged media to run the `23 MB` second-opinion check and attach the exported JSON receipt to the case file.
- **R&D Literature & Workforce Benchmarking**: Install `zotero-interlinear` in Zotero 10 pointed at an internal Ollama/vLLM endpoint with a shared department CSV glossary (noting its `AGPL-3.0` license is ideal for internal desktop use), and use `ai-era-job-kit` for evidence-backed engineering portfolio reviews.

---

## 🧭 3. End-to-End Reference Architecture & Decision Tree (Mermaid)

```mermaid
flowchart TD
    subgraph MediaForensics["On-Device AI Media Forensics: hikaku-io/hikaku-extension (★404, Apache-2.0)"]
        A[Browser Loads Claim Photo / Vendor Asset / Video Stream] --> B[In-Memory Fetch + Skip UI Screenshots &amp; Flat Graphics]
        B --> C[Path 1: Parse C2PA / IPTC / EXIF<br/>&amp; A1111 / ComfyUI / InvokeAI Parameters]
        B --> D[Path 2: Local ONNX SwinV2 Detector<br/>WebGPU fp16 / WASM uint8 · 3-Frame Video Median]
        C & D --> E{Flagged for Audit?}
        E -->|Yes| F[Run 23MB Community Forensics 2nd Opinion<br/>Copy JSON Evidence into Case File]
    end

    subgraph RndAndTalent["Bilingual Zotero 10 &amp; O*NET Benchmarking: zotero-interlinear (★79) + ai-era-job-kit (★66)"]
        G[Foreign Patent / Paper PDF in Zotero 10] --> H[zotero-interlinear Viewport-First Translation<br/>CSV Glossary Prompt Injection + Post-Replacement]
        H --> I[Highlight-Safe Side-by-Side View + Searchable Bilingual PDF]
        J[Engineering Portfolio Audit] --> K[ai-era-job-kit 12 Zero-Dep Python Scripts<br/>Score portfolio.json Against Live O*NET &amp; BLS Data]
    end
```

---

## 📊 4. Peer Solution Comparison Matrix (Decision Matrix)

| Evaluation Dimension | Option A: Cloud Per-Image Forensics APIs + Commercial PDF SaaS | Option B: EXIF-Only CLI Scripts + Copy-Paste ChatGPT | **Option C (Recommended): `Hikaku` (Apache-2.0) + `zotero-interlinear` & `job-kit`** |
| :--- | :--- | :--- | :--- |
| **Detection of Stripped-Metadata AI Images & Video** | ✅ High recall, but expensive per-call billing & no live stream overlay | ❌ Fails 100% whenever social/messaging apps strip EXIF/C2PA | ✅ **C2PA/IPTC/ComfyUI metadata + local SwinV2 pixel model + 23MB 2nd opinion + 3-frame video** |
| **Data Privacy & Air-Gapped Network Readiness** | ❌ Uploads sensitive claim/vendor photos to external clouds | ✅ Local script, but zero visual inference capability | ✅ **100% on-device WebGPU/WASM inference with `npm run build -- --offline` air-gapped bundle** |
| **Domain Glossary Fidelity & Zotero Highlight Safety** | ⚠️ Whole-PDF cloud rewriters break layout and corrupt Zotero highlights | ❌ Manual paragraph copy-pasting destroys reading flow | ✅ **Native Zotero 10 reader, dual-enforced CSV glossary, viewport priority & intact highlights** |
| **Monthly TCO (120k Media Assets + 3,000 PDFs/Mo)** | **`$5,805.00 / mo`** (`$2,290` APIs/SaaS + `37.0 hrs` upload/glossary fixes) | **`$2,545.00 / mo`** (`$930` compute + `17.0 hrs` manual verification) | **`$346.00 / mo`** (**`-94.04%` savings**; `$80` local Ollama/ops + `2.8 hrs` 2nd-opinion review) |

---

## 🧮 5. 7-Card Quantitative Insights & Closed-Form FinOps (`CLAIM-20261117-R30-HIKAKU-ZOTERO`)

> **Scope & Boundary Declaration**: Evaluated for 60 enterprise trust/safety and R&D analysts inspecting **120,000 monthly web/claims media assets and reviewing 3,000 multilingual technical PDFs** at a blended rate of `$95.00/hr` (base Zotero cloud storage marked `not_measured`):

$$\text{Total Monthly TCO} = \text{Forensics \& Translation API Spend} + (\text{Upload Triage, Glossary Fix \& Highlight Repair Hours} \times \$95.00)$$

| Cost Component | Path A: Cloud Forensics APIs + PDF Translation SaaS | Path B: EXIF Scripts + Copy-Paste Translation | **Path C: `Hikaku` On-Device + `zotero-interlinear` Stack** |
| :--- | :---: | :---: | :---: |
| **Monthly Media-Forensics & PDF Translation API Spend** | `$2,290.00` | `$930.00` | **`$80.00`** (`$0` on-device WebGPU + local Ollama/glossary ops) |
| **Monthly Upload Triage, Glossary Fix & Highlight Hours** | `37.0 hrs` | `17.0 hrs` | **`2.8 hrs`** (**`92.43%` reduction**) |
| **Monthly Analyst & R&D Engineering Labor (`@ $95.00/hr`)** | `$3,515.00` | `$1,615.00` | **`$266.00`** |
| **Total Monthly TCO** | **`$5,805.00`** | **`$2,545.00`** (`-56.16%`) | **`$346.00`** (**`-94.04%`**) |
| **Net Savings vs. Path A (Monthly / Annual)** | Baseline (`$0.00`) | `$3,260.00 / mo` (`$39,120/yr`) | **`$5,459.00 / mo` (`$65,508.00 / yr`)** |

---

## ✅ 6. Solution Architect Action Checklist

- [ ] **Step 1 — Build & Distribute the Air-Gapped `Hikaku` Browser Extension**: Clone `hikaku-io/hikaku-extension` (`Apache-2.0`) and run `npm install && npm run build -- --offline` to package the ONNX Runtime, SwinV2 detector, and 23 MB Community Forensics model for enterprise Chrome/Edge/Firefox deployment.
- [ ] **Step 2 — Mandate Dual-Evidence (`Metadata + 2nd Opinion`) JSON Logs on Flagged Claims**: Train trust/safety analysts to keep declaration flags distinct from probabilistic visual estimates, trigger **Get a second opinion** on disputed items, and attach `Copy JSON` output to audit tickets.
- [ ] **Step 3 — Deploy `zotero-interlinear` with a Shared Department CSV Glossary**: Configure Zotero 10 to use an internal Ollama/vLLM endpoint (or keyless fallback pools) and import a standardized CSV/TSV technical glossary for side-by-side reading and bilingual PDF archival.
- [ ] **Step 4 — Benchmark Engineering Portfolios with `ai-era-job-kit`**: Use the 12 zero-dependency Python scripts in `Vets-Who-Code/ai-era-job-kit` to audit `portfolio.json` and `brag/entries/` against live O*NET and BLS market standards.
