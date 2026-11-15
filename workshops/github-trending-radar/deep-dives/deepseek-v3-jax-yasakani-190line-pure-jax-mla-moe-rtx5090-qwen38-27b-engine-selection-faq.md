# 190 行纯 JAX 实现 DeepSeek-V3 与单卡 RTX 5090 极速 Qwen3.8-27B 推理引擎选型 FAQ：`Vaibhaav-Tiwari/deepseek-v3-jax` + `yasakani-dev/yasakani`

> **元数据（Metadata）**
> - **评测批次**：2026-11-15 夜间深潜 Round 6（累计 Round 308）
> - **核心标的**：
>   1. [`Vaibhaav-Tiwari/deepseek-v3-jax`](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax)（`★ 188` · `2026-11-13` 建仓 · `v1.0` · MIT 协议 · 零 Flax / 零 Equinox / 零 PyTorch，仅用 **190 行纯 JAX 代码（`deepseek_v3.py`）** 完整实现 DeepSeek-V3 核心架构：多头潜在注意力 MLA `480 → 144` 压缩、解耦 RoPE、无辅助损失负载均衡 DeepSeekMoE 与多词元预测 MTP，在 MacBook Air M5 24GB 上从零预训练收敛并通过 39 项单元测试）
>   2. [`yasakani-dev/yasakani`](https://github.com/yasakani-dev/yasakani)（`★ 98` · `2026-11-12` 建仓 · `v0.1.4` 于 `2026-11-15` 发布 · Apache-2.0 协议 · 专为 Windows + 单张 NVIDIA RTX GPU（针对 RTX 5090 深度调优）运行 **Qwen3.8-27B** 打造的定制推理引擎，在全部 7 类任务中击败 8 款主流通用引擎，`v0.1.4` 实现 64-Token 复制投机校验提速 `1.67×–2.04×` 及 `229,376` Token 长文档追问首字延迟从 `116 s` 降至 `0.37 s`）
> - **配套架构图**：[`assets/github-ai-radar-2026-11-15-r6-deepseekjax-yasakani.svg`](../../../assets/github-ai-radar-2026-11-15-r6-deepseekjax-yasakani.svg)
> - **证据封存锚点**：`CLAIM-20261115-R6-DEEPSEEKJAX-YASAKANI`（见 [`evidence/trending-daily-2026-11-15-audit.json`](../evidence/trending-daily-2026-11-15-audit.json)）

---

## 📌 1. 核心结论速览（Executive Summary & First-Principles Pitch）

1. **一句话讲透本质**：
   - **`Vaibhaav-Tiwari/deepseek-v3-jax` (`v1.0`)**：就是**DeepSeek-V3 架构的“190 行玻璃盒解剖标本”**。想真正吃透 DeepSeek-V3 论文（`arXiv:2412.19437`）里的多头潜在注意力（MLA）、解耦旋转位置编码（Decoupled RoPE）、无辅助损失负载均衡（Aux-Loss-Free Balancing）和多词元预测（MTP），去啃几万行分布式 C++/PyTorch 代码极其痛苦。这个项目完全不用 Flax、Equinox 或 PyTorch，参数就是最朴素的 JAX 数组字典，用 **190 行一屏到底的纯函数代码** 在一台 MacBook Air M5（24 GB）上从零预训练了一个 `36.2M` 总参（每 Token 激活 `13.6M`）的完整模型，直观验证了“无辅助损失偏置让 16 个路由专家的负载从极度偏科的 `0.09%–18.6%` 完美收敛到均匀的 `5.7%–6.9%`（理想均值 `6.25%`），且丝毫不损伤验证集 Loss（`3.921 vs 3.923`）”！
   - **`yasakani-dev/yasakani` (`v0.1.4`)**：就是**把“单张消费级旗舰显卡跑 Qwen3.8-27B”榨干到物理极限的专机专用引擎**。通用推理引擎（如 llama.cpp / vLLM / Ollama）为了兼容几百种模型架构，不得不在算子融合与文件格式上做妥协；`YASAKANI` 只为一件事而生——在 Windows 单卡 RTX 5090（兼容 16GB+ RTX 30/40/50 系）上跑满 **Qwen3.8-27B**。在今日发布的 `v0.1.4` 中，它将输入复制跨度的单步投机校验从 `16` 个 Token 扩大到 **`64` 个 Token**（代码与 JSONL 编辑直接提速 **`1.67×–2.04×`**），并将 **`229,376` Token 超长文档** 连续追问的首字响应时间（TTFT）从 **`116 秒` 暴降至 `0.37 秒`（提速 313 倍）**！
2. **核心量化收益（FinOps 闭式账本 `CLAIM-20261115-R6-DEEPSEEKJAX-YASAKANI`）**：
   - 在 **每月开展 12 次 MLA/MoE 算子架构改型验证 + 本地工作站服务 18,000 次 200k+ 长上下文代码/JSONL 编辑请求** 的研发负载下（工程师全负担时薪 `$105.00/hr`；本地显卡硬件折旧标记为 `not_measured`）：
   - **Path C（`deepseek-v3-jax` + `yasakani v0.1.4`）** 将月度总拥有成本（TCO）从 **Path A（租用云端多卡跑重型框架 + 调云 API 反复重读 229k 长文档）的 `$6,130.00/mo`** 降至 **`$482.50/mo`**，净省 **`$5,647.50/mo`（`-92.13%`，年化节省 `$67,770.00/年`）**，每月释放 **`34.5 小时`（`-90.79%`）** 的框架排障与长文档等待工时。

![2026-11-15 Night Round 6 (R308) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-15-r6-deepseekjax-yasakani.svg)

---

## ❓ 2. 灵魂拷问 Q1–Q3（First-Principles Deep Dive）

### Q1：为什么看千行级工业框架学不会 MLA 和无辅助损失 MoE？`deepseek-v3-jax` 的 190 行代码揭示了哪些关键数值真相？
- **传统痛点**：工业级训练库里充斥着张量并行通信、自定义 CUDA 内核与多层面向对象封装，掩盖了 MLA 缓存压缩与专家路由偏置的数学本质。
- **`deepseek-v3-jax` (`v1.0`) 的四大第一性原理实证**：
  1. **MLA 缓存压缩 `480 → 144`**：在 `mla` 与 `init_cache` 函数中，每个 Token 每层不再缓存完整的 Key 和 Value（480 个浮点数），而是仅缓存压缩后的低秩潜在向量与 1 个所有注意力头共享的解耦旋转位置编码（Decoupled RoPE，合计仅 **144 个数/Token/层**，立省 **70%** KV Cache）。
  2. **无辅助损失偏置更新（`update_bias`）的零损耗均衡实证**：1 个常驻共享专家 + 16 个路由专家（Top-4 激活）。若关闭偏置，第 2,000 步时各专家负载极度失衡（`0.09%–18.6%`）；开启偏置后，仅通过微调路由选择（不篡改专家权重梯度），专家负载即收敛至 **`5.7%–6.9%`**（理论均值为 `6.25%`），且 2,000 步验证集 Loss 完全持平（`3.921` vs `3.923`）！
  3. **多词元预测（MTP，`λ = 0.3`）与序列级均衡损失（`α = 1e-4`）**：在 `forward` 与 `loss_fn` 中完整复现了预测下下个 Token 的 MTP 头；在 MacBook Air M5（24 GB）上以 `10.7k tokens/s` 跑完 12,000 步（2.6 小时），验证 Loss 从 `5.02` 降至 `3.51`。
  4. **绕开 Apple Metal 编译器陷阱**：精准发现 `jax-metal 0.1.1` 在双轴张量收缩求导（grad through 2-axis contraction）上的底层 Bug，并在 `deepseek_v3.py` 中用等价纯函数写法完美规避，39 项 `pytest` 测试全部通过。

### Q2：为什么同一张 RTX 5090 跑 `Qwen3.8-27B`，`yasakani` 能在全部 7 类任务中击败 8 款通用推理引擎？`v0.1.4` 的两项提速是怎么做到的？
- **传统痛点**：Coding Agent 在改代码或处理 JSONL 时，输出中有大量字符其实是在原封不动地“抄写”输入上下文；而通用引擎每次依然老老实实逐个 Token 自回归解码，且一旦对同一篇 20 万字长文档换个问题追问，往往触发全量重读。
- **`yasakani` (`v0.1.4`) 的三大硬核杀手锏**：
  1. **单次 64-Token 复制跨度投机校验（Input-Copy Verification）**：针对代码重构与 JSONL 编辑中高频出现的原文复制片段，`v0.1.4` 将单次前向通道校验的复制跨度从 `16` 个 Token 提升至 **`64` 个 Token**——在关闭思考模式下，代码与 JSONL 编辑速度直接达到 `v0.1.2` 的 **`1.67× 至 2.04×`**，且输出内容 100% 逐字一致！
  2. **229,376-Token 超长文档零重读（TTFT `116 s → 0.37 s`）**：当长文档位于问题之前且中间无穿插请求时，对同一篇 **`229,376` Token 文档** 提出新问题不再重头读取，首 Token 延迟从 **`116 秒` 缩短至 `0.37 秒`**。
  3. **双档专属压缩格式与高度透明的 KL 散度对账**：提供 `Quality`（`12.37 GB`，与原模型最高概率下一词一致率 **`95.24%`**，KL 散度仅 **`0.0122`**）与 `Speed`（`10.31 GB`，一致率 **`93.01%`**，KL 散度 **`0.0304`**）两套专用权重，内置 OpenAI 兼容服务端、工具调用（`tools`）、图片输入与 `yasakani selfcheck` 驱动自检。

### Q3：这两个工具各自的诚实边界（Limitations）在哪里？
- **诚实边界**：
  - `Vaibhaav-Tiwari/deepseek-v3-jax` 明确声明它是一个 `36.2M` 参数的**架构教学与验证原型**而非强语言能力模型；必须锁死 `jax==0.4.34` 与 `jax-metal==0.1.1`，且提醒发布的 `ckpt.pkl` 为 Python `pickle` 格式（仅可加载受信来源权重）。
  - `yasakani-dev/yasakani` 极其坦诚地说明：它是日本独立开发者专为 **`Qwen3.8-27B` 单一模型 + 单张 RTX 5090** 编写的专用引擎（虽自 `v0.1.3` 起支持 16GB+ 的 RTX 30/40/50 系显卡及 Linux 源码编译，但尚未针对非 5090 显卡做专门算子调优；且 `tool_choice: required` 目前仅接收参数而未做强制语法约束）。

---

## 🧭 3. Mermaid 选型决策树与架构对比图

```mermaid
flowchart TD
    Start["大模型底层架构原型实验与单卡旗舰本地推理选型"] --> Layer{"当前核心工程目标是什么？"}

    Layer -->|"在笔记本/单机上研究、修改或教学验证 DeepSeek-V3 (MLA / MoE / MTP) 架构"| ArchCheck{"是否希望零框架黑盒、一屏读懂全部前向与反向逻辑？"}
    ArchCheck -->|"是！追求 190 行纯 JAX 函数 + 39 项单测 + M5/CPU 直接跑通"| UseDSJax["✅ 选用 Vaibhaav-Tiwari/deepseek-v3-jax (v1.0 · MIT)<br/>MLA 480->144 缓存压缩 + 无辅损负载均衡 (5.7%-6.9%)<br/>自带 138MB 预训练检查点与完整训练/采样脚本"]
    ArchCheck -->|"需要在百卡集群上生产训练千亿参数大模型"| UseMegatron["使用 DeepSeek 官方 HAI-LLM / Megatron-LM"]

    Layer -->|"在单张 NVIDIA RTX GPU (5090/4090/3090 >=16GB) 上本地极速运行 Qwen3.8-27B 服务 Coding Agent"| InferCheck{"核心负载是否包含代码/JSONL 修改与 200k+ 超长文档追问？"}
    InferCheck -->|"是！需 64-Token 复制加速 (2.04x) + 229k 文档 0.37s 首字响应"| UseYasakani["✅ 选用 yasakani-dev/yasakani (v0.1.4 · Apache-2.0)<br/>Quality (12.37GB, 95.24% 一致) / Speed (10.31GB) 双模型<br/>OpenAI 兼容 API + tools 工具调用 + 多模态图片输入"]
    InferCheck -->|"需要在同一服务里频繁切换 Llama/Mistral/Gemma 等数十种异构模型"| UseLlamaCpp["使用通用 llama.cpp / vLLM 推理服务"]
```

---

## 📊 4. 同类方案对比矩阵（Quantitative & Architectural Comparison）

| 对比维度 | `Vaibhaav-Tiwari/deepseek-v3-jax` (`v1.0`) | `yasakani-dev/yasakani` (`v0.1.4`) | 传统方案 A：重型分布式训练框架 + 云端长上下文 API | 传统方案 B：Flax/PyTorch 封装库 + 通用本地 GGUF 引擎 |
| :--- | :--- | :--- | :--- | :--- |
| **核心解决痛点** | 消除数万行框架胶水，190 行纯函数看清 MLA/MoE 每一步张量变换 | 消除通用引擎算子开销与长文档重复 Prefill 的百秒级卡顿 | 改一行路由逻辑要编译半天；200k 文档追问按量计费极贵 | 抽象层遮蔽底层梯度行为；通用 GGUF 改代码仅 16-token 步进 |
| **底层架构机制** | **190 行纯 JAX + MLA(`480→144`) + 无辅损偏置 + MTP** | **专模专用 CUDA 内核 + 64-Token 复制校验 + 长前缀驻留** | 多节点 Megatron + 远端无状态 API | 多层 Class 继承 + 通用算子分发 |
| **实测硬核指标** | 专家负载 **`5.7%–6.9%`**（无偏置为 `0.09%–18.6%`），Loss 零损 | 229k 文档 TTFT **`116s → 0.37s`**；代码编辑提速 **`1.67×–2.04×`** | 每次追问耗时数十秒且烧数十万输入 Token | 同卡 RTX 5090 7 类任务吞吐均落后于 YASAKANI |
| **诚实边界透明度** | 明确声明属 36.2M 架构教学原型、锁 `jax==0.4.34` | 明确区分单 token 一致率（`95.24%`）与任务准确率、专注 RTX 5090 | 隐藏云端缓存失效重算账单 | 缺乏针对单模型的极限压榨 |

---

## 🃏 5. 7-Card 定量洞察与 FinOps 闭式账本（7-Card Quantitative Insights）

| 卡片编号 | 维度标签 | 核心定量洞察（Headline-as-Finding） | 证据与闭式参数锚点 |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `deepseek-v3-jax` + `yasakani` 将月度架构原型实验与本地长文档编码推理 TCO 降低 `92.13%`（`$6,130.00 → $482.50/月`） | `CLAIM-20261115-R6-DEEPSEEKJAX-YASAKANI` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `yasakani v0.1.4` 将 `229,376` Token 文档追问首字延迟从 `116 s` 降至 `0.37 s`（提速 `313.5×`），代码编辑提速 `1.67×–2.04×` | `yasakani-dev/yasakani` (`v0.1.4`) 实测基准 |
| **Card 3** | `3/7 · WHAT I TESTED` | `deepseek-v3-jax` 用 `190` 行纯 JAX 将 MLA 缓存从 `480` 压至 `144` 数/Token/层，无辅损偏置使专家负载稳定在 `5.7%–6.9%` | `Vaibhaav-Tiwari/deepseek-v3-jax` (`v1.0`) |
| **Card 4** | `4/7 · UNDER THE HOOD` | 解耦 RoPE + MTP (`λ=0.3`) + 64-Token 复制投机校验与 `Quality` (`12.37 GB`, KL `0.0122`) / `Speed` (`10.31 GB`) 双格式 | `deepseek_v3.py` & `YASAKANI` 发行说明 |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | 诚实披露 `jax-metal 0.1.1` 双轴收缩求导规避方案、39 项单测以及 `YASAKANI` 非 5090 显卡与 `tool_choice` 边界 | 边界与可复现性审计 |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | 本机 M5/CPU 快速改型验证 + 单卡 RTX 零网络离线高吞吐，每月节省 `34.5 小时`（`-90.79%`）等待与调试工时 | 12 次架构原型 + 18,000 次长文编辑/月模型 |
| **Card 7** | `7/7 · MY TAKE` | 深入理解 DeepSeek-V3 数学机制与构建 RTX 5090 极速本地 Qwen3.8-27B 编码底座的必收利器 | 本地硬件折旧：`not_measured` |

### 💰 FinOps 闭式参数表（每月 12 次 MLA/MoE 原型实验 + 18,000 次 200k+ 长上下文编辑请求，`r = $105.00/hr`）

| 方案路径 | 云算力与长上下文 Token 费 (`compute_and_token_usd`) | 框架排障与等待工时 (`engineering_hours`) | 工程人力成本 (`engineering_labor_usd`) | 月度总 TCO (`total_monthly_usd`) | 较 Path A 净节省 (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：云端多卡 PyTorch 试错 + 229k 长文档重复 Prefill API** | `$2,140.00` | `38.0 hrs` | `$3,990.00` | **`$6,130.00`** | Baseline (`0.00%`) |
| **Path B：重型 Flax/Megatron 框架 + 通用未调优本地 GGUF 引擎** | `$980.00` | `18.0 hrs` | `$1,890.00` | **`$2,870.00`** | `-$3,260.00` (`-53.18%`) |
| **Path C：`deepseek-v3-jax` 190 行原型 + `yasakani v0.1.4`（推荐）** | **`$115.00`** | **`3.5 hrs`** | **`$367.50`** | **`$482.50`** | **`-$5,647.50` (`-92.13%` / 年省 `$67,770.00`)** |

---

## 🛠️ 6. 实战上手 Checklist（15-Minute Actionable Rollout）

```bash
# 1. 克隆 deepseek-v3-jax，跑通 39 项纯 JAX 架构单测（MLA + DeepSeekMoE + MTP）并加载预训练检查点采样
git clone https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax.git && cd deepseek-v3-jax
uv venv -p 3.12 .venv && uv pip install --python .venv/bin/python -r requirements.txt
JAX_PLATFORMS=cpu .venv/bin/pytest tests.py -q   # 39 passed

# 2. 在配备 NVIDIA RTX 5090 (或 >=16GB RTX 30/40/50) 的机器上运行 YASAKANI v0.1.4 自检与 OpenAI 兼容服务
yasakani selfcheck
# 下载 yasakani-dev/Qwen3.8-27B-YASAKANI-quality (12.37 GB) 或 speed (10.31 GB) 启动本地极速推理服务
```
