# Resource-Safe Zero-Copy Rust Inference Bindings (`ncnn.rust`) & 5.4x Faster Rust 3D Gaussian Splat Reconstruction Engine (`Vauss`) Deep-Dive Architecture & Selection FAQ

> **Document Metadata**  
> - **Evaluation Date**: 2026-11-15 (Night Round 22 · Cumulative Round 324 Standalone Selection FAQ)  
> - **Evaluated Repositories**: [`Edwardssss/ncnn.rust`](https://github.com/Edwardssss/ncnn.rust) (`★41`, created 2026-11-08, resource-safe Rust bindings for Tencent `ncnn` `20261020` featuring zero-copy borrowed views, graph-bound endpoint tokens, `continue_session()` KV cache, `retain_pages()` heap pooling & optional Vulkan backend, BSD-3-Clause) & [`voyager-so/vauss`](https://github.com/voyager-so/vauss) (`★26`, created 2026-11-12, `5.4x` faster 3D Gaussian Splat trainer than `gsplat-MCMC` at `~50%` GPU memory, `3–6 min` per scene / `28.5` PSNR, exporting browser viewers, playable voxel worlds, Blender 5.3 packs & Unity collision meshes)  
> - **Target Audience**: AI Solution Architects (AI SAs), Rust Systems & Edge Inference Engineers, 3D Reconstruction & Spatial Computing Leads  
> - **Related Radar Digest**: [2026-11-15 Panorama & Velocity Digest (`daily/2026-11-15.en.md`)](../daily/2026-11-15.en.md) · [中文版 (`ncnn-rust-vauss-zero-copy-vulkan-inference-bindings-5x-gaussian-splat-trainer-selection-faq.md`)](ncnn-rust-vauss-zero-copy-vulkan-inference-bindings-5x-gaussian-splat-trainer-selection-faq.md)  
> - **Visual Summary**: [`assets/github-ai-radar-2026-11-15-r22-ncnnrust-vauss.svg`](../../../assets/github-ai-radar-2026-11-15-r22-ncnnrust-vauss.svg)

![ncnn.rust + Vauss Architecture Overview](../../../assets/github-ai-radar-2026-11-15-r22-ncnnrust-vauss.svg)

---

## 📌 1. Executive Summary

1. **First-Principles Essence (What & Why)**:
   - **What is `Edwardssss/ncnn.rust`?** It is a **resource-safe, zero-allocation-ready Rust binding suite (`ncnn-rust` + `ncnn-rust-sys`) for Tencent's `ncnn` (`20261020`) inference engine with optional Vulkan GPU residency**. Its microbenchmarks expose a critical systems lesson: on a 65,536-element FP32 tensor request path, zero-copy borrowed output takes **`10.930 µs`** (`+5%` vs native C `10.422 µs`), whereas allocating a fresh 256 KB `Vec` per request costs **`226 µs`** due to glibc/NT page faults (**a 20x slowdown**), and keeping a caller's input `Mat` handle alive blocks `ncnn` light-mode buffer recycling (**another 20x penalty**). `ncnn.rust` eliminates both penalties by consuming input handles early, resolving graph-bound endpoint tokens once (`resolve_blob`), writing into caller-reused buffers (`extract_into` / `infer_view_into`), retaining mapped heap pages (`ncnn_rust::heap::retain_pages()`), preserving quantized widths (`infer_stored` for `i8`/`bf16`/`fp16`), and supporting stateful autoregressive KV caching (`ex.continue_session()`).
   - **What is `voyager-so/vauss`?** It is a **pure-Rust 3D Gaussian Splatting (`3DGS`) reconstruction CLI and agent tool that trains `5.4x` faster than `gsplat-MCMC` using `~50%` of the GPU memory** (`3–6 minutes` per scene on a single 8GB+ GPU, achieving **`28.5 PSNR`** across 9 standard benchmark scenes). From a single phone video, 360° equirectangular capture, circular fisheye action-cam clip (`--camera-model opencv-fisheye`), or AI-generated video, `vauss` solves cameras, trains splats, and exports **5 ready-to-use targets**: a serverless browser viewer (`export-viewer`), a **first-person playable & destructible voxel world (`export-game`, pressing `V` toggles between splats and voxels)**, a **Blender 5.3 pack (`export-blender`)**, a **web `.spz` bundle (`export-web`)**, and **convex-decomposed Unity collision geometry (`export-collision --unity`)**.
2. **Why AI SAs Should Adopt This Pattern Tonight**:
   - `ncnn.rust` provides the blueprint for wrapping C/C++ inference runtimes in Rust without falling into the `226 µs` per-request allocation/page-fault trap or corrupting shared blobs under `light_mode`.
   - `vauss` bridges the gap between neural rendering and interactive game/simulation engines by turning video into both high-PSNR Gaussian splats and playable voxel/collision geometry in under 6 minutes.
3. **Quantitative FinOps Summary (`CLAIM-20261115-R22-NCNNRUST-VAUSS`)**:
   - Across `60,000,000` monthly edge/server vision & OCR inferences (`NanoDet-m` / `PP-OCRv5`) and `90` monthly 3D scene reconstructions & multi-engine exports (`$100.00/hr` engineer rate; base host compute: `not_measured`), moving from "Unpooled FFI copy wrappers + slow Python `gsplat-MCMC` pipelines (Path A, `$5,950.00/mo`)" to "`ncnn.rust` zero-copy pooled inference + `vauss` 5.4x Rust splat engine (Path C, `$460.00/mo`)" **saves `$5,490.00/mo` (`-92.27%`), or `$65,880.00/yr`, while freeing `36.5` engineering hours/month (`-91.25%`)**.

---

## 🔍 2. First-Principles Deep Dive (Q1–Q3)

### Q1: Why do naive FFI inference wrappers suffer 20x microsecond-scale slowdowns, and how does `ncnn.rust` hold wrapper overhead to `+1.6%` on `NanoDet-m`?

- **Two Hidden 20x Penalties Measured in `docs/performance.md`**:
  1. **Live Input Handle Blocking Light-Mode Recycling**: If a caller retains an input tensor reference while `Extractor` runs, `ncnn` cannot recycle that buffer in light mode—costing 20x more on guest OS heaps. `ncnn.rust` makes `Extractor::input` consume the `Mat` handle before execution starts, so the fastest memory path is the default path.
  2. **Per-Request 256 KB Allocation & OS Page Faults (`226 µs` vs `10.930 µs`)**: Allocating and dropping a 256 KB output vector per request triggers OS page unmapping/remapping. `ncnn.rust` provides `extract_into(&output_id, &mut buffer)`, `NetBuilder::reuse_blob_memory()`, and `ncnn_rust::heap::retain_pages()` to achieve zero post-warmup allocations (`NanoDet-m` CPU: `23.011 ms` native vs `23.379 ms` `ncnn-rust`, `+1.6%`; `PP-OCRv5` Vulkan: `10.863 ms` native vs `10.210 ms` `ncnn-rust`).
- **Compile-Time & Graph-Level Safety Contracts**:
  - **Graph-Bound Endpoint Tokens**: `net.resolve_blob("input")` tokens are rejected if passed to a foreign or reloaded `Net`.
  - **Shared-Blob Light-Mode Guard**: Refuses `ex.set_light_mode(true)` whenever `!net.shared_blobs()?.is_empty()`, preventing premature freeing of branched intermediate tensors unless an explicit `Split` layer is present.
  - **Stateful Decode & Stored Widths**: `ex.continue_session()` + `set_kvcache_max_seqlen_hint(2048)` maintain attention KV caches across tokens, while `infer_stored` preserves raw `i8`/`fp16`/`bf16` element widths.

### Q2: How does `vauss` train 3D Gaussian Splats 5.4x faster at half the VRAM and turn them into playable voxel worlds and Unity collision meshes?

- **End-to-End Rust Pipeline (`vauss` v0.1.21-rc)**:
  1. **CPU Preflight Audit (`vauss check room.mp4 --room`)**: Evaluates lighting, sharpness, camera motion, and room coverage on CPU before consuming GPU time.
  2. **Native Fisheye & 360° Camera Solving**: Trains directly on circular fisheye lenses (`--camera-model opencv-fisheye`, masking outside the image circle without cropping FOV) and 2:1 stitched equirectangular 360° video (`--camera-model equirect`).
  3. **5-Target Multi-Modal Export**: From a single `3–6 minute` training run (`28.5 PSNR` mean across 9 benchmark scenes), `vauss` exports:
     - `export-viewer` (standalone local browser viewer)
     - `export-game` (first-person playable/destructible voxel level with `V`-key splat/voxel toggle)
     - `export-blender` (Blender 5.3 PLY, textured mesh, and colored surface voxels)
     - `export-web` (`scene.spz` + `scene.json`)
     - `export-collision --unity` (convex collision pieces + floor estimate for Unity).

### Q3: How should AI SAs combine both tools in spatial computing and edge AI architectures?

- Use `vauss` (driven directly by CLI or coding agents) to reconstruct physical rooms or AI-generated video into `.spz`/Blender/Unity environments in 5 minutes, and deploy `ncnn.rust` (with Vulkan residency and `extract_into` buffer pooling) for low-latency on-device vision/OCR/KV-cached inference.

---

## 🧭 3. Architecture & Selection Decision Tree (Mermaid)

```mermaid
flowchart TD
    Start["AI SA High-Performance Rust Inference & 3D Splat Reconstruction Need"] --> Track{"Which system layer is targeted?"}

    Track -->|"Need memory-safe, zero-allocation Tencent ncnn<br/>inference in Rust (CPU / Vulkan + KV cache)"| Ncnn["Adopt Edwardssss/ncnn.rust<br/>(10.9µs Request Path · Graph Tokens · Vulkan)"]
    Track -->|"Need 5.4x faster 3D Gaussian Splat training<br/>with Voxel, Blender 5.3 & Unity collision exports"| Vauss["Adopt voyager-so/vauss<br/>(3-6 Min/Scene · ~50% VRAM · 28.5 PSNR)"]

    Ncnn --> NStep1["1. Resolve graph-bound tokens via net.resolve_blob"]
    NStep1 --> NStep2["2. Check net.shared_blobs().is_empty() before light_mode"]
    NStep2 --> NStep3["3. Reuse buffers via extract_into + heap::retain_pages()"]
    NStep3 --> NStep4["4. Use continue_session() for stateful KV-cached decoding"]

    Vauss --> VStep1["1. Run CPU preflight: vauss check room.mp4 --room"]
    VStep1 --> VStep2["2. Train splat: vauss run room.mp4 (pinhole / fisheye / 360)"]
    VStep2 --> VExport{"Select Export Target"}
    VExport -->|"Browser / Web"| EView["export-viewer & export-web (scene.spz)"]
    VExport -->|"Playable Voxel Level"| EGame["export-game (WASD + V-key splat/voxel toggle)"]
    VExport -->|"Blender 5.3 & Unity Physics"| EEng["export-blender & export-collision --unity"]
```

---

## 📊 4. Comparison Matrix Against Alternative Approaches

| Dimension | Naive FFI Copy Wrappers + Python `gsplat-MCMC` (Path A) | Python ONNX Runtime + Manual COLMAP Scripts (Path B) | `ncnn.rust` + `vauss` Rust Stack (Path C) |
| :--- | :--- | :--- | :--- |
| **64K FP32 Tensor Request Wrapper Overhead** | ❌ `226 µs` per-request 256 KB alloc/page-fault penalty | ⚠️ High Python GIL & serialization overhead | ✅ **`10.930 µs` (`+5%` vs C API; `+1.6%` on full `NanoDet-m` CPU)** |
| **Light-Mode Safety & Foreign-Graph Protection** | ❌ Unchecked `light_mode` corrupts branched blobs | N/A | ✅ **Consuming input + `shared_blobs()` guard + graph-bound tokens** |
| **Quantized Output Widths & Stateful KV Cache** | ❌ Forced FP32 conversion; stateless extractors | ⚠️ Manual external KV buffer plumbing | ✅ **`infer_stored` (`i8`/`bf16`/`fp16`) + `ex.continue_session()`** |
| **3DGS Training Speed, VRAM & Lens Support** | ❌ `gsplat-MCMC` takes 20–35 mins; high VRAM | ⚠️ Crops circular fisheye lenses, losing FOV | ✅ **`5.4x` faster (`3–6 min`), `~50%` VRAM, `28.5 PSNR` + native fisheye** |
| **Game & DCC Exports (Voxels / Blender / Unity)** | ❌ Raw `.ply` splats only; no collision geometry | ⚠️ Manual mesh decimation & collider authoring | ✅ **5 built-in exports: Viewer, Playable Voxels, Blender 5.3, `.spz` & Unity Colliders** |

---

## 📈 5. 7-Card Quantitative Insights & Closed-Form FinOps Ledger

### 5.1 7-Card Benchmark Summary

1. **Card 1 (Overview & Workbench)**: Across `60M` monthly vision/OCR inferences and `90` monthly 3D scene reconstructions/exports, Path C reduces monthly cost from `$5,950.00` to `$460.00` (`-92.27%`).
2. **Card 2 (Single-Case Deep Dive)**: `ncnn.rust` runs `NanoDet-m` in `23.379 ms` CPU (`+1.6%` vs C) / `4.702 ms` Vulkan and `PP-OCRv5` in `10.210 ms` Vulkan; `vauss` trains a `2M`-splat scene in `3–6 min` (`28.5 PSNR`) and exports Blender 5.3 + playable voxel + Unity collision packs.
3. **Card 3 (Evaluation Matrix)**: Evaluates request-path latency (`10.930 µs` zero-copy vs `226 µs` alloc), 3DGS speedup (`5.4x` vs `gsplat-MCMC`), VRAM reduction (`~50%`), and one-command export formats (`5`).
4. **Card 4 (Under the Hood)**: `ncnn.rust` enforces consuming input handles, `extract_into`, and `retain_pages()`; `vauss` integrates camera solving, splat training, voxelization, and convex collision decomposition in Rust.
5. **Card 5 (Robustness Check)**: `ncnn.rust` deterministically rejects `set_light_mode(true)` when `net.shared_blobs()` is non-empty; `vauss check --room` flags blurry or under-covered video before GPU training.
6. **Card 6 (Latency & Labor Scaling)**: Cuts monthly FFI memory debugging and 3D asset conversion labor from `40.0h` to `3.5h` (`36.5h/mo` saved, `-91.25%`).
7. **Card 7 (My Take — Good Fit vs Not For)**:
   - ✅ **Good Fit**: High-throughput Rust edge/server inference services and 3D pipelines turning video into Blender 5.3 sets, web viewers, or playable voxel/Unity levels.
   - ⛔ **Not For**: Unstitched raw `.insv`/`.360` camera files (export stitched 2:1 video first) or environments without an installed `ncnn` C++ SDK.

### 5.2 Closed-Form FinOps Ledger (`CLAIM-20261115-R22-NCNNRUST-VAUSS`)

> **Provenance & Parameter Disclosure**: Synthetic FinOps model (`synthetic_model`, `independently_reproduced=false`) for `N_inf = 60,000,000` inferences/month and `N_splat = 90` 3D scene reconstructions/month at `$100.00/hr` engineer rate (base host compute: `not_measured`). Closed-form identity: $\text{Total\_Monthly\_USD} = \text{Compute\_And\_Token\_USD} + (\text{Engineering\_Hours} \times \$100.00)$.

| Architecture Path | Monthly Inference & 3D GPU Spend (USD) | Monthly FFI & 3D Conversion Labor (Hours) | Engineering Labor Cost (`@ $100.00/hr`) | Total Monthly Cost (USD) | Net Savings vs Path A (USD / %) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A: Per-Request Alloc FFI + Python `gsplat-MCMC` Pipeline** | `$1,950.00` | `40.0h` | `$4,000.00` | **`$5,950.00`** | Baseline (`0.00%`) |
| **Path B: Python ONNX Wrapper + Manual COLMAP/Blender Glue** | `$940.00` | `19.0h` | `$1,900.00` | **`$2,840.00`** | `-$3,110.00` (`-52.27%`) |
| **Path C: `ncnn.rust` Zero-Copy + `vauss` 5.4x Splat (Recommended)** | `$110.00` | `3.5h` | `$350.00` | **`$460.00`** | **`-$5,490.00` (`-92.27%`)** |

---

## 🛠️ 6. 15-Minute Rollout Checklist

- [ ] **Step 1 (4 mins): Build the pinned `ncnn` (`20261020`) SDK and run `ncnn.rust` workspace tests**
  ```bash
  git clone https://github.com/Edwardssss/ncnn.rust.git
  cd ncnn.rust
  python3 tools/fetch-ncnn.py && python3 tools/build-ncnn-sdk.py
  export NCNN_INSTALL_DIR=$PWD/ncnn-install
  cargo test --workspace
  ```
- [ ] **Step 2 (3 mins): Configure zero-allocation `extract_into` and `heap::retain_pages()` in Rust**
  ```rust
  ncnn_rust::heap::retain_pages();
  let in_id = net.resolve_blob("input")?;
  let out_id = net.resolve_blob("output")?;
  ex.extract_into(&out_id, &mut reusable_buf)?;
  ```
- [ ] **Step 3 (4 mins): Install `vauss` (`0.1.21-rc`), run CPU capture preflight, and train a 3D scene in 3–6 mins**
  ```bash
  curl -fsSL https://raw.githubusercontent.com/voyager-so/vauss/main/scripts/install.sh | sh -s -- 0.1.21-rc
  vauss doctor
  vauss check room.mp4 --room
  vauss run room.mp4 --goal "walk-through of my living room" --driver fixed --run-dir runs/room
  ```
- [ ] **Step 4 (4 mins): Export Browser Viewer, Playable Voxel Game, Blender 5.3 Pack & Unity Collision Meshes**
  ```bash
  vauss export-viewer runs/room
  vauss export-game runs/room
  vauss export-blender runs/room
  vauss export-web runs/room --out exports/room
  vauss export-collision exports/room --unity exports/room-unity
  ```
