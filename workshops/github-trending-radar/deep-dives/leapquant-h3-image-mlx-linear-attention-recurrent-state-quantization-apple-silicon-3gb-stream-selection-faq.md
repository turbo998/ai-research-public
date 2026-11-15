# 线性注意力循环状态无损量化加速（`LeapQuant`）与 Apple Silicon 3.23GB 流式预取高清生图（`H3-Image-MLX`）深度架构拆解与同类方案选型 FAQ

> **文档元数据（Document Metadata）**  
> - **评审日期**：2026-11-15（Night Round 32 · 累计第 334 轮独立选型专题）  
> - **对标项目**：[`leapquant/LeapQuant`](https://github.com/leapquant/LeapQuant)（`★56`，2026-11-11 创建，面向 Qwen Gated DeltaNet 与 GLM Kimi Delta Attention 线性注意力模型的免训练 8/6/4-bit 循环状态量化插件，算子级提速 `2.05–3.70x`、vLLM 端到端提速 `1.57x` 且精度反超 BF16 对齐 FP32，Apache-2.0） & [`Anionex/h3-image-mlx`](https://github.com/Anionex/h3-image-mlx)（`★57`，2026-11-10 创建，基于 MLX 与 W8A8 Metal TensorOps 的 Apple Silicon 本地 MiniMax H3 Image 生图与多图编辑引擎，通过分进程卸载与异步预取流式加载将 1024p 峰值内存从 `21.18 GB` 压至 `3.23 GB` 且保持 `23.61s` 满速，Apache-2.0）  
> - **适用角色**：AI Solution Architect（AI 解决方案架构师）、vLLM 高性能推理加速工程师、Apple Silicon 端侧多模态架构师  
> - **关联雷达日报**：[2026-11-15 全景洞察与飙升榜 (`daily/2026-11-15.md`)](../daily/2026-11-15.md) · [English Version (`leapquant-h3-image-mlx-linear-attention-recurrent-state-quantization-apple-silicon-3gb-stream-selection-faq.en.md`)](leapquant-h3-image-mlx-linear-attention-recurrent-state-quantization-apple-silicon-3gb-stream-selection-faq.en.md)  
> - **可视化总结图**：[`assets/github-ai-radar-2026-11-15-r32-leapquant-h3imagemlx.svg`](../../../assets/github-ai-radar-2026-11-15-r32-leapquant-h3imagemlx.svg)

![LeapQuant + H3-Image-MLX Architecture Overview](../../../assets/github-ai-radar-2026-11-15-r32-leapquant-h3imagemlx.svg)

---

## 📌 一、核心结论速览（Executive Summary — 先看结论再看细节）

1. **一句话讲透本质（What & Why）**：
   - **`leapquant/LeapQuant` 是什么？** 它是由 MIT Song Han、UC Berkeley Kurt Keutzer 与 Ion Stoica 等团队联合开源（`arXiv:2609.38166`）的 **“专为新一代线性注意力大模型（如 `Qwen3.5-9B` / `Qwen3.8-Flash-Next` 的 Gated DeltaNet 与 `GLM-5.3-Flash` 的 Kimi Delta Attention）设计的免训练、近乎无损的 8-bit / 6-bit / 4-bit 循环状态（Recurrent State）量化引擎（已集成进 `vLLM 0.30.0`）”**。为什么在线性注意力模型里直接对循环状态做常规 FP8 或 INT8 量化会导致模型彻底变傻（`Qwen3.5-9B` 的 AIME 2026 数学竞赛得分直接从 FP32 的 **`87.9%` 暴跌至 FP8 的 `0.0%`、INT8 的 `3.9%`**）？因为循环状态在每个解码步都被反复读写更新，每步一次的舍入误差会随生成长度指数级累积，且状态矩阵中存在极端离群行列！`LeapQuant` 用三大绝招根治：① **按窗口跳跃量化（Per-Window Quantization，窗口内保持低比特状态固定，仅在窗口末尾量化一次）**；② **秩 1 补偿 Token（Compensator Tokens，将最大离群值存为与真实 Token 更新同构的秩 1 外积）**；③ **残差通道平滑（Residual Smoothing）**——在 B200 / RTX PRO 6000 / RTX 5090 上实现 **算子级 `2.05–3.70x` 提速、端到端 `1.57x` 提速**，且 8-bit/6-bit 四大基准平均分高达 **`84.4%`**（不仅完胜 BF16 的 `72.5%`，甚至略超 FP32 的 `84.0%`）！
   - **`Anionex/h3-image-mlx` 是什么？** 它是面向 Apple Silicon Mac（M1–M5 Pro）的 **“利用三阶段独立子进程内存释放 + W8A8 ConvRot Metal TensorOps + 异步块预取流式加载（`H3_ASYNC=1 H3_PREFETCH=1`），将 MiniMax H3 Image 1024×1024 峰值内存从 `21.18 GB` 砍掉 `85%` 降至 `3.23 GB`（16GB M5 Air 仅占 `2.48 GB`，4K `4096×4096` 仅占 `7.18 GB`），同时生成速度与全常驻显存模式分秒不差（`23.61 s` vs `23.63 s`，逐像素 100% 一致）”** 的神仙级端侧生图与 16 图参考编辑引擎！
2. **为什么值得 AI SA 今晚立刻掌握？**
   - 这两个项目分别攻克了 2026 年底云端与端侧推理最核心的显存带宽墙：**云端用 `LeapQuant` 解决混合线性注意力模型（GDN/KDA）在 vLLM 中的循环状态读写瓶颈**；**端侧用 `H3-Image-MLX` 的“计算与下一层 Safetensors 磁盘读取完全重叠”消除流式卸载的速度惩罚**。
3. **定量收益摘要（Closed-Form FinOps Ledger `CLAIM-20261115-R32-LEAPQUANT-H3IMAGEMLX`）**：
   - 在每月运行 `1,200` GPU 小时线性注意力模型 vLLM 推理与本地 Mac 工作站生成/编辑 `6,000` 张高清/4K 图像场景下（工程师时薪 `$100.00/hr`，底层宿主机硬件成本 `not_measured`），从“被迫使用慢速 FP32/精度崩坏的 BF16 + 38GB–48GB 内存占用的 ComfyUI MPS 管线（Path A，`$6,240.00/mo`）”切换到“`LeapQuant` vLLM 插件 + `H3-Image-MLX` 3.23GB 异步预取引擎（Path C，`$475.00/mo`）”，**每月净省 `$5,765.00`（`-92.39%`），年化节省 `$69,180.00/yr`，每月释放 `37.5` 小时精度排障与显存优化工时（`-91.46%`）**。

---

## 🔍 二、第一性原理灵魂三问（Q1–Q3 Deep Dive）

### Q1：为什么在线性注意力（Gated DeltaNet / Kimi Delta Attention）上连 BF16 都会掉点 11.5%、普通 FP8/INT8 直接归零？`LeapQuant` 的三大免训练机制是如何满血复活 8/6/4-bit 的？

- **线性注意力循环状态（Recurrent State）的精度脆弱性**：
  - 标准 Softmax 注意力把历史存为追加只读的 KV Cache（量化误差只影响单次读取，不会污染后续状态）；而线性注意力（GDN / KDA）把全部上下文压缩进一个固定大小二维状态矩阵 $S_t$，**每生成一个新 Token 都要对 $S_t$ 做原地乘加更新**！
  - 在 `Qwen3.5-9B`、`GLM-5.3-Flash` 与 `Qwen3.8-Flash-Next` 的 AIME 2026 / BeyondAIME / GPQA / LiveCodeBench v6 实测中，光是把循环状态从 **FP32（平均 `84.0%`）降到 BF16（平均 `72.5%`）就狂掉 `11.5` 个百分点**；若每步直接做朴素 FP8 / INT8 量化，`Qwen3.5-9B` 的 AIME 得分直接变成 **`0.0%` / `3.9%`**！
- **`LeapQuant` 的三步外科手术**：
  1. **按窗口跳跃量化（Per-Window Quantization）**：不再每步重编码状态！在一个 Token 窗口内，低比特状态保持只读固定，窗口内的新 Token 更新暂存在高精度小缓冲中；等跳过整个窗口后，才在窗口边界执行一次状态合并与量化，将累积量化噪声降低一个数量级。
  2. **秩 1 补偿 Token（Compensator Tokens）**：状态矩阵中最致命的离群值被单独抽离，表示为几个高精度的 **秩 1 外积（Rank-One Outer Product）**——由于其数学形式与窗口内真实 Token 的状态更新完全一致，可直接复用窗口缓冲更新路径，几乎零额外算子开销！
  3. **窗口级残差平滑（Residual Smoothing）**：剥离补偿 Token 后，在每个窗口边界对各 Key 通道行重新计算缩放因子平衡量级，使 8-bit / 6-bit 均取得 **`84.4%` 平均分**，甚至 4-bit 仍高达 **`80.6%`**（对比 `TurboQuant` 4-bit 仅 `45.0%`、`MXFP4` 仅 `16.7%`）。

### Q2：为什么以往的“流式按层加载（Layer Streaming）”虽然省显存但慢如蜗牛？`H3-Image-MLX` 是如何在砍掉 85% 内存（`21.18 GB -> 3.23 GB`）的同时做到 `23.61s vs 23.63s` 零减速的？

- **三大系统级内存与流水线优化**：
  1. **三阶段独立进程物理隔离（Separate Process per Stage）**：将文本编码（Text Encoding）、去噪（Denoising）与重叠分块 VAE 解码（Overlapping Tile Decoding）放在独立子进程中顺序执行；上一阶段落盘中间张量后进程直接退出，由操作系统 100% 回收物理内存页。
  2. **异步预取与 GPU 计算完美重叠（`H3_ASYNC=1 H3_PREFETCH=1`）**：
     - 普通流式模式（Plain Streaming）在跑完第 $i$ 个 Transformer Block 后才同步从 SSD 读取第 $i+1$ 块权重，耗时从常驻模式的 `23.63 s` 退化到 `32.33 s`。
     - 开启 `H3_ASYNC=1 H3_PREFETCH=1` 后，当 Metal GPU 正在计算当前 Block 时，后台线程提前从 `safetensors` 预取下一个 Block 权重——在 M5 Pro 上实测耗时 **`23.61 s`**（与 `21.18 GB` 全常驻模式完全打平！），而峰值物理内存仅 **`3.23 GB`（降低约 85%）**，在 16GB M5 MacBook Air 上峰值更是低至 **`2.48 GB`**！
  3. **原生 W8A8 ConvRot 与 Metal TensorOps 加速**：直接读取 INT8 ConvRot 权重，在 macOS 26.4+ 上自动探测并启用原生 INT8 Metal TensorOps，在同机对比中比本地 ComfyUI 快 **`4.38 倍`（1024p）至 `1.80 倍`（4096p 4K，峰值内存 `7.18 GB` vs ComfyUI `42.31 GB`）**。

### Q3：AI SA 如何将这两个项目纳入团队的云端与端侧推理基建？

- **云端 vLLM 集群**：在部署 `Qwen3.5`、`Qwen3.8-Flash-Next` 或 `GLM-5.3-Flash` 等线性注意力混合架构模型时，严禁用默认 BF16 或朴素 FP8 跑循环状态；统一挂载 `LeapQuant` 插件（`vLLM 0.30.0`），以 8-bit/6-bit 满血还原 FP32 推理智力并收获 `1.57x` 端到端吞吐红利；
- **端侧 Mac 创意工作站**：使用 `h3-image-mlx`（开启 `H3_ASYNC=1 H3_PREFETCH=1 --dit-mode stream`）在 16GB–48GB MacBook 上以 `~3 GB` 内存静默后台生成 1K–4K 图像与多参考图局部编辑（`--reference`）。

---

## 🧭 三、架构拓扑与选型决策树（Mermaid Decision Tree）

```mermaid
flowchart TD
    Start["AI SA 线性注意力云端推理与 Apple Silicon 端侧 4K 生图需求"] --> Target{"优化目标属于哪一侧？"}

    Target -->|"在 NVIDIA B200 / RTX 5090 部署 Qwen / GLM<br/>线性注意力模型 (GDN/KDA)，需兼顾精度与吞吐"| Leap["选用 leapquant/LeapQuant (vLLM 0.30.0 插件)<br/>(窗口跳跃量化 + 秩1补偿 Token + 残差平滑)"]
    Target -->|"在 16GB-48GB Apple Silicon Mac 本地运行<br/>MiniMax H3 Image 1K-4K 生图与多图编辑"| H3Mlx["选用 Anionex/h3-image-mlx<br/>(三阶段进程隔离 + W8A8 TensorOps + 异步预取)"]

    Leap --> LeapBit{"选择循环状态比特位宽"}
    LeapBit -->|"无损精度优先 (84.4% Avg vs 84.0% FP32)"| Bit86["启用 8-bit 或 6-bit LeapQuant<br/>(算子提速 2.05-3.70x · 端到端提速 1.57x)"]
    LeapBit -->|"极致显存压缩 (80.6% Avg)"| Bit4["启用 4-bit LeapQuant (大幅超越 TurboQuant 45.0%)"]

    H3Mlx --> MlxMode{"Mac 内存容量与并发需求？"}
    MlxMode -->|"16GB-32GB 笔记本或多应用后台共存"| StreamAsync["开启 H3_ASYNC=1 H3_PREFETCH=1 --dit-mode stream<br/>(1024p 仅占 3.23 GB 且保持 23.61s 常驻级速度)"]
    MlxMode -->|"4096x4096 4K 超清大图生成"| Stream4K["流式分块生成 4K (峰值仅 7.18 GB vs ComfyUI 42.31 GB)"]
```

---

## 📊 四、同类方案核心能力对比矩阵（Comparison Matrix）

| 评估维度 | 原生 BF16/朴素 FP8 + 本地 ComfyUI MPS (Path A) | `TurboQuant`/`KVQuant` + 普通同步流式加载 (Path B) | `LeapQuant` + `H3-Image-MLX` (Path C) |
| :--- | :--- | :--- | :--- |
| **线性注意力（GDN/KDA）四基准平均精度** | ❌ BF16 跌至 `72.5%`；朴素 FP8 崩至 `45.1%`（Qwen3.5 AIME `0.0%`） | ⚠️ `KVQuant` 8-bit `75.2%`；`TurboQuant` 6-bit 跌至 `60.1%` | ✅ **8-bit / 6-bit 均达 `84.4%`（对齐并略超 FP32 基线 `84.0%`）** |
| **vLLM 线性注意力算子与端到端提速比** | Baseline (`1.00x`) | ⚠️ 离群值处理开销抵消部分加速 | ✅ **算子级 `2.05–3.70x` 提速，vLLM 端到端 `1.57x` 提速** |
| **Mac 端 1024×1024 H3 Image 峰值物理内存** | ❌ ComfyUI 高达 `31.29 GB`（16GB/24GB Mac 直接卡死） | ✅ 普通流式 `2.53 GB`，但耗时慢至 `32.33 s` | ✅ **`3.23 GB`（减少 `~85%`），且耗时 `23.61 s` 追平全常驻 `23.63 s`！** |
| **Mac 端 4096×4096 (4K) 峰值内存与速度** | ❌ ComfyUI 峰值 `42.31 GB`，耗时 `570.59 s` | ⚠️ 无异步预取等待磁盘 I/O | ✅ **峰值仅 `7.18 GB`，耗时 `317.29 s`（比 ComfyUI 快 `1.80x`）** |
| **多参考图指令编辑（Reference Editing）** | ⚠️ 显存叠加极易 OOM | ⚠️ 缺乏分阶段进程物理释放 | ✅ **独立参考图 VAE 编码子进程，支持 `--reference <Picture 1..N>`** |

---

## 📈 五、7-Card 定量洞察与闭式 FinOps 账本（Quantitative Insights & FinOps Ledger）

### 5.1 7-Card 核心评测摘要（对标 Model Benchmark Report Standard）

1. **Card 1（Overview & Workbench）**：针对每月 `1,200` GPU 小时线性注意力 vLLM 服务与 `6,000` 次 Apple Silicon 高清/4K 图像生成编辑场景，Path C 将月度总成本从 `$6,240.00` 降至 `$475.00`（节省 `-92.39%`）。
2. **Card 2（Single-Case Deep Dive）**：`LeapQuant` 在 `Qwen3.5-9B`、`GLM-5.3-Flash` 与 `Qwen3.8-Flash-Next` 上以 8-bit/6-bit 斩获 `84.4%` 均分（修复 BF16 的 `72.5%` 掉点与 FP8 的 `45.1%` 崩溃）；`H3-Image-MLX` 在 M5 Pro 上以 `3.23 GB` 峰值内存跑出 `23.61 s`（追平 `21.18 GB` 常驻模式的 `23.63 s`）。
3. **Card 3（Evaluation Matrix）**：覆盖 `LeapQuant` 8/6-bit 平均精度（`84.4%`）、端到端加速比（`1.57x`）、`H3-Image-MLX` 1024p 内存削减率（`-84.75%`，`21.18 GB -> 3.23 GB`）及双模式逐像素一致率（`100%`）。
4. **Card 4（Under the Hood）**：`LeapQuant` 基于 `TileLang`、`Flash Linear Attention` 与 `vLLM 0.30.0`；`H3-Image-MLX` 基于 `MLX`、INT8 `ConvRot` 与 `H3_ASYNC=1 H3_PREFETCH=1` 双缓冲流水线。
5. **Card 5（Robustness Check）**：在 16GB 内存的入门级 M5 MacBook Air 上，`H3-Image-MLX` 流式模式以 `2.48 GB`（1024p）与 `2.78 GB`（2048p）峰值内存稳定完赛，且仓库内附带完整的 `benchmarks/controlled/2026-11-12-prefetch/summary.json` 原始核验记录。
6. **Card 6（Latency & Labor Scaling）**：每月因排查线性注意力长文本精度退化与 Mac 显存交换卡死耗费的工时从 `41.0h` 降至 `3.5h`（净省 `37.5h/mo`，`-91.46%`）。
7. **Card 7（My Take — Good Fit vs Not For）**：
   - ✅ **Good Fit**：使用 Gated DeltaNet / Kimi Delta Attention 架构模型的 vLLM 生产集群（B200 / RTX 5090），以及在 16GB–64GB Apple Silicon Mac 上运行 MiniMax H3 Image 的开发者。
   - ⛔ **Not For**：纯标准 Softmax Full-Attention 老模型（无需循环状态量化），或非 Apple Silicon 的 Windows/Linux 显卡运行 `h3-image-mlx`。

### 5.2 闭式参数化 FinOps 账本（`CLAIM-20261115-R32-LEAPQUANT-H3IMAGEMLX`）

> **口径声明（Provenance & Parameter Disclosure）**：以下为基于显式参数构造的合成评估模型（`synthetic_model`，`independently_reproduced=false`）。设团队每月消耗 `N_vllm = 1,200` GPU 小时线性注意力推理、在 Mac 端执行 `N_img = 6,000` 次高清/4K 图像生成与编辑，工程师折算时薪 `R_eng = $100.00/hr`，底层宿主机硬件成本记为 `not_measured`。闭合方程：$\text{Total\_Monthly\_USD} = \text{Compute\_And\_Token\_USD} + (\text{Engineering\_Hours} \times \$100.00)$。

| 方案路径（Path） | 月度推理集群与工作站算力费（USD） | 精度排障与显存调优工时（Hours/mo） | 工程人工成本（`@ $100.00/hr`） | 月度总成本（Total Monthly USD） | 相对 Path A 净节省（USD / %） |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：FP32/BF16 未优化状态 + 38GB–48GB ComfyUI MPS** | `$2,140.00` | `41.0h` | `$4,100.00` | **`$6,240.00`** | Baseline (`0.00%`) |
| **Path B：`TurboQuant` 有损量化 + 未开启异步预取流式加载** | `$1,010.00` | `19.5h` | `$1,950.00` | **`$2,960.00`** | `-$3,280.00` (`-52.56%`) |
| **Path C：`LeapQuant` vLLM + `H3-Image-MLX` 异步流（推荐）** | `$125.00` | `3.5h` | `$350.00` | **`$475.00`** | **`-$5,765.00` (`-92.39%`)** |

---

## 🛠️ 六、15 分钟极速落地 Checklist（15-Minute Rollout Checklist）

- [ ] **Step 1（4 分钟）：在 `vLLM 0.30.0` 环境安装 `LeapQuant` 并启动 8-bit 线性注意力状态推理服务**
  ```bash
  git clone https://github.com/leapquant/LeapQuant.git
  cd LeapQuant && pip install -e .
  bash serve.sh Qwen/Qwen3.5-9B
  ```
- [ ] **Step 2（3 分钟）：在 Apple Silicon Mac（Python 3.11+）安装 `h3-image-mlx` 并拉取模型权重**
  ```bash
  python3 -m venv .venv && source .venv/bin/activate
  python -m pip install --upgrade 'h3-image-mlx==0.1.0a8'
  h3-image-mlx fetch --models ./models
  ```
- [ ] **Step 3（4 分钟）：启用 `H3_ASYNC=1 H3_PREFETCH=1 --dit-mode stream` 在 `3.23 GB` 峰值内存下满速出图**
  ```bash
  H3_ASYNC=1 H3_PREFETCH=1 h3-image-mlx generate \
    --models ./models --dit-mode stream --output teapot.png \
    --prompt 'A yellow enamel teapot and a white cup on a blue wooden table.'
  ```
- [ ] **Step 4（4 分钟）：测试多参考图局部替换编辑（`--reference <Picture 1> --reference <Picture 2>`）**
  ```bash
  H3_ASYNC=1 H3_PREFETCH=1 h3-image-mlx generate --models ./models --dit-mode stream --output edit.png \
    --reference teapot.png --reference bird.png \
    --prompt 'Edit <Picture 1>. Replace the white cup with the bird from <Picture 2>. Keep the teapot and table.'
  ```
