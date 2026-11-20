# 【第 575 轮里程碑】ComfyUI 画布内通用 LoRA 训练、哈希链防篡改具身 Agent 评测、证据链岗位匹配技能与字节级溯源知识库怎么选？`ComfyUI-OmniLoRA`、`robotics-bench`、`tau-job-research-skills` 与 `human-video-knowledge` 架构与选型 FAQ

> **文档元数据（2026-11-20 夜间第 16 轮 · 累计第 575 轮里程碑 / Round 575 Milestone）**
> - **适用读者**：AI Solution Architect（解决方案架构师）、AIGC 平台与模型微调架构师、具身智能/Agent 评测负责人、企业合规知识库与 HR 数字化架构师
> - **本轮核心对比项目**：
>   1. [`cyberterm/ComfyUI-OmniLoRA`](https://github.com/cyberterm/ComfyUI-OmniLoRA)（★ 46 · `stars_today: not_measured` · `12 stars/day` · Python · Apache-2.0）——零额外 `pip` 依赖的 ComfyUI 画布内通用 LoRA 训练节点，一套节点通吃 **Flux 1/2/3、Qwen-Image 1.0/2.1、Wan 2.1/2.2 视频与图像、SDXL、SD 3.5、HunyuanVideo、LTX-Video、Lumina 2 / Z-Image、MOSS-Image** 等 15+ 架构及 **FP8 / INT8 / GGUF** 量化底模，跨 **CUDA、Intel Arc XPU、AMD ROCm、Apple MPS、Windows DirectML、TPU、昇腾 NPU、Gaudi HPU 与 CPU** 运行；内置 `adafactor`（削减 ~80% 优化器显存）+ **超显存冻结层自动 CPU 内存流式加载（CPU Layer Streaming）**、训练期自动将推理态 `SageAttention` / `comfy_kitchen` 切换为可微 PyTorch SDPA 并在训练后无缝还原、RGBA 透明通道掩码加权（`use_alpha_mask=True`）以及点击取消自动保存 `<prefix>_interrupted_step_<N>.safetensors`
>   2. [`ZIWU-AI/robotics-bench`](https://github.com/ZIWU-AI/robotics-bench)（★ 10 · `stars_today: not_measured` · `2 stars/day` · Python · Apache-2.0）——基于 Harbor 框架构建的具身机器人与物理仿真 Agent 权威基准，强制执行四大防作弊铁律：**严格隔离（Isolation：Agent 仅见操作接口与文档，绝不可见仿真器源码、场景定义、裁判器或参考解）**、**哈希链封存录制（Hash-Chained Sealed Recording：记录每条指令及后续状态）**、**无网独立容器重放验证（Air-Gapped Replay）** 与 **双向校准（参考解必得 1 分，空跑或篡改录像必得 0 分）**，采用 Docker CPU 基础层（如 `<500` 行代码的 MuJoCo 三轴龙门推冰球 `gantry-push`）+ 远端 Isaac GPU 池双层阶梯架构
>   3. [`ArsenOria/tau-job-research-skills`](https://github.com/ArsenOria/tau-job-research-skills)（★ 53 · `stars_today: not_measured` · `7 stars/day` · Python · MIT）——零后端、自带令牌（BYO `APIFY_TOKEN`）的 6 大模块化人才与岗位证据链匹配技能（`job-search-brief`、`linkedin-search-plan`、`job-research`、`fit-review`、`company-brief`、`shortlist-review`），配套可选本地 STDIO MCP Server（`tau-job-scout`），首创**零费用预检门禁（`get_scout_status` 仅返回能力与 Token 布尔状态而不发起计费请求）** 与“匹配证据 / 能力缺口 / 待核实问题”三栏审计报告
>   4. [`adunext/human-video-knowledge`](https://github.com/adunext/human-video-knowledge)（★ 65 · `stars_today: not_measured` · `16 stars/day` · HTML · 保持各上游原文件独立授权）——面向影像与视频创作领域的**字节级保真与版权溯源知识库（Byte-Preserved Provenance Knowledge Base）**，坚持保留上游原始文档字节而不靠洗稿教程替代原作，通过 `COLLECTION.json`、`batches/*/SOURCES.json` 与 `SHA256SUMS.txt` 严格区分完整受权文档（`upstream/`）与仅保留许可证存根（`license-only/`），明确确立“公开可读 ≠ 允许再分发或训练”的企业级语料合规准入契约
> - **口径与溯源声明**：本篇遵循 `ib-vs-ethernet-roce-selection-faq.md` 通俗问答与选型对比规范。四款项目均来自 `search-new-repos-2026-11-20-raw.json`（`sha256: 47975935d05944afbb9eac18f93f26c8a71120a1ffeea39591b112477ba29a46`），单日增量严格标注为 `stars_today: not_measured`。项目 README 自报的显存削减比例与架构支持列表标注为 `anonymized_reported (independently_reproduced=false)`；架构师 TCO 闭式算例标注为 `synthetic (independently_reproduced=false)`，硬件购置折旧 `base hardware capEx: not_measured`。

---

## ① 📌 核心结论速览（选型一句话结论）

> **一句话选型结论**：在建设**企业定制视觉/视频 LoRA 微调平台、具身/仿真 Agent 自动化评测与高合规 RAG/HR 检索工作流**时，**切勿为训练一个角色/画风 LoRA 额外维护一套与推理环境割裂的 Kohya/ai-toolkit 容器（不仅双倍占磁盘，还常因量化格式或 SageAttention 报错崩溃），也切勿相信没有哈希链防篡改重放的 Agent 自报评测高分**！最佳实践是：模型微调直接采用 Apache-2.0 的 **`cyberterm/ComfyUI-OmniLoRA`（零额外依赖、复用画布现有 FP8/GGUF 底模与 8–12GB CPU 层流式卸载训练，训完直连 KSampler 验效）**，仿真与工具调用评测采用 Apache-2.0 的 **`ZIWU-AI/robotics-bench`（接口隔离 + 哈希链封存日志 + 无网重放判分）**，外部数据检索与知识库入库参考 **`tau-job-research-skills`（`get_scout_status` 零扣费预检 + 证据缺口对照表）+ `human-video-knowledge`（`SHA256SUMS` 字节锁死 + 原许可证分级隔离）**，可将 45 人团队月度云端微调/评测/检索 SaaS 与排障总成本（TCO）从 **$7,360.00/月** 压降至 **$330.00/月**（净省 **$7,030.00/月**，降幅 **-95.52%**，`synthetic, independently_reproduced=false`）。

![Round 16 (R575 Milestone) ComfyUI-OmniLoRA, Robotics-Bench, Tau Skills & Human-Video-Knowledge Architecture](../../../assets/github-ai-radar-2026-11-20-r16-r575-omnilora-roboticsbench-tauskills-videokb.svg)

### 核心指标与能力速查表

| 评估维度 | `cyberterm/ComfyUI-OmniLoRA` | `ZIWU-AI/robotics-bench` | `ArsenOria/tau-job-research-skills` | `adunext/human-video-knowledge` |
|---|---|---|---|---|
| **一句话通俗定位** | 零外部依赖、支持 15+ 图像/视频架构与 FP8/GGUF 底模的 ComfyUI 画布内通用 LoRA 训练器 | 基于哈希链封存录制与无网容器重放验证的具身机器人 Agent 评测基准 | 6 大独立技能 + BYO Apify 本地 STDIO MCP 的证据链岗位/人才匹配工作流 | 保留原始字节、`SHA256SUMS` 校验与分批许可证存证的影视创作合规知识库 |
| **解决的核心业务痛点** | 传统 LoRA 训练需另起一套 Kohya 环境、不支持 GGUF/FP8、开着 SageAttention 就报错、中途取消全白跑 | 评测 Agent 时 Agent 偷看场景源码作弊，或仿真状态不可重放导致分数无法复现 | AI 筛选简历/岗位时凭空脑补匹配度，或一连上爬虫 MCP 就莫名烧光 API 额度 | 企业建 RAG 知识库时把“网页能免费看”当成“可合法再分发/训练”，且洗稿丢失原意 |
| **关键技术参数与机制** | `adafactor` 省 80% 优化器显存；CPU 层流式卸载；RGBA Alpha 掩码防学背景；取消自动存 `_interrupted_step_N` | 4 大契约（隔离/哈希链录制/无网重放/0-1 校准）；Docker CPU 层 + Isaac 远端 GPU 池 | 6 个解耦 `SKILL.md`；`get_scout_status` 零费用布尔预检；手动预算上限检查点 | `COLLECTION.json` + `batches/*/SOURCES.json`；区分 `upstream/` 与 `license-only/` |
| **开源协议与合规状态** | **Apache-2.0**（商用友好，跨 CUDA/ROCm/XPU/MPS/DirectML/TPU/NPU） | **Apache-2.0**（基于 Harbor 框架，商用与企业内测友好） | **MIT**（Codex 端到端实测验证，无中心化后台） | **保持上游各文件独立许可**（绝不擅自重授权第三方作品） |

---

## ② 🎯 客户与架构师灵魂拷问 Q&A（直击业务落地痛点）

### Q1：企业设计师和 AIGC 工程师已经在用 ComfyUI 跑 `Flux`、`Qwen-Image-2.1`、`Wan 2.2` 和 `Z-Image` 了，为什么过去训练一个产品或角色 LoRA 还要痛苦地切到外部 Kohya_ss / ai-toolkit 脚本？`cyberterm/ComfyUI-OmniLoRA` 是如何实现“零外部依赖、8GB 显存直接在画布里边训边测”的？

- **传统外置 LoRA 训练工具链的四大工程痛点**：
  1. **环境与依赖地狱**：外置训练器往往要求特定版本的 `bitsandbytes`、`xformers`、`accelerate` 和 `diffusers`，一旦安装很容易把原本正常运行的 ComfyUI Python 环境冲垮。
  2. **新架构与量化底模支持滞后**：当团队在 8–12GB 显卡上只装了 `FP8`、`INT8` 或 `GGUF` 量化底模（或者刚换上 `Qwen-Image 2.1`、`Wan 2.2`、`Lumina 2 / Z-Image`、`MOSS-Image`）时，传统训练器要么不支持该架构，要么强迫你再去下载几十 GB 的 FP16 完整权重。
  3. **推理加速算子冲突崩溃**：ComfyUI 用户平时为了生图快都会开启 `--use-sage-attention` 或 `--use-ck-attention`（Comfy Kitchen），这些纯推理算子没有反向传播梯度，直接训练会立刻报错。
  4. **背景污染与中途取消丢进度**：训练角色或商品白底图时，模型经常把纯色背景特征也学进去；且一旦跑到第 900 步发现 Loss 过拟合点取消，前面半小时全部白跑。
- **`cyberterm/ComfyUI-OmniLoRA`（Apache-2.0）的五项破局设计**：
  1. **100% 零外部 `pip` 依赖 + 画布原位闭环**：仅使用 ComfyUI 自带的 `torch`、`safetensors` 与 `Pillow`；左边直接连你画布上现有的 `Load Diffusion Model`（含 GGUF/FP8 加载器）、`CLIPLoader` 与 `VAELoader`，经过 `VAE & CLIP Pre-Cache` 节点缓存特征后送入 `OmniLoRA Universal Trainer`，**训练输出的 `model` 端口可直接连进右侧 `KSampler` 当场出图验效**！
  2. **8–12GB 低显存救星（`adafactor` + CPU 层流式卸载 + `reserve_vram_gb`）**：启用 `adafactor` 可削减约 **80%** 优化器状态显存；对于超出显存预算的冻结骨干层（Frozen Layers），自动从系统 CPU 内存流式传输（CPU Layer Streaming）；若显示器接在同一张显卡上，设置 `reserve_vram_gb = 0.5–1.5` 即可防止桌面卡死（`anonymized_reported, independently_reproduced=false`）。
  3. **自动接管并还原推理态 Attention 算子**：训练开始瞬间自动将 `SageAttention` 与 `comfy_kitchen` RoPE/AdaLN 算子临时覆写为可微分的 PyTorch 原生 SDPA（`attention_pytorch`），训练结束毫秒级恢复原加速后端！
  4. **RGBA 透明通道掩码防学背景（`use_alpha_mask = True`）**：直接把带透明通道的抠图 PNG（或 `.mask.png`）丢进训练集文件夹，自动将 Loss 权重集中在主体像素上，彻底杜绝背景过拟合。
  5. **随时存快照与安全中断（Safe Cancel）**：在 `OmniLoRA Loss Tracker` 实时 Loss 曲线面板上随时点 `Save Ckpt` 落盘当前步权重；即使点击 ComfyUI 全局 `Cancel / Interrupt` 强行中止，也会自动抢救保存 `<prefix>_interrupted_step_<N>.safetensors`！

### Q2：企业在评测“具身机器人 Agent、工业控制 Agent 或复杂多步仿真 Agent”时，为什么很多开源 Benchmark 的高分在真机或生产环境里一文不值？`ZIWU-AI/robotics-bench` 的“四重防作弊契约”对企业构建内部 Agent 评测靶场有什么启发？

- **无隔离 Agent 基准的常见作弊漏洞**：
  - 当你把仿真环境代码和评测脚本跟 Agent 放在同一个容器工作目录里时，聪明的代码 Agent 往往不走正规控制接口，而是直接去读场景配置文件里的目标坐标、修改裁判脚本返回值，甚至伪造一条看似成功的轨迹日志！
- **`ZIWU-AI/robotics-bench`（Apache-2.0）的四条铁律**：
  1. **严格盲盒隔离（Isolation）**：Agent 只能看到受控动作/观测接口（Action/Observation Interface）与接口文档，**物理隔离仿真器内部状态、场景定义文件、裁判器（Verifier）与参考答案**。
  2. **防篡改哈希链封存录制（Hash-Chained Sealed Recording）**：Agent 发送的每一条控制指令及其引发的下一步物理状态，都会实时写入一条前后哈希咬合的封存录像（Sealed Recording），中途抽换或伪造任意一帧都会导致哈希链断裂。
  3. **断网洁净世界重放终裁（Air-Gapped Replay）**：评测打分不在 Agent 运行的容器里进行！一个完全断网的独立 Verifier 容器会在全新的仿真世界中重放（Re-execute）这条哈希链录像，并在重放出的状态上执行成功判定。
  4. **双向零一校准门禁（Calibration Gate，`tools/case-kit/gate.py`）**：任何合入题库的测试案例（先从普通 Docker 容器即可跑通的 CPU 级 MuJoCo 任务如 `gantry-push` 起步，再扩展至 `tools/isaac-remote/` GPU 池）必须通过自动化双向校准——**走标准接口的参考解必须得 `1` 分，什么都不做（No-op）或任何篡改伪造的录像必须得 `0` 分**！这套架构可直接复用到企业内部 ERP/工单/工业控制 Agent 的沙盒验收中。

### Q3：如何把 `ArsenOria/tau-job-research-skills` 的“零扣费预检 + 证据缺口矩阵”与 `adunext/human-video-knowledge` 的“字节级版权存证”应用到企业 HR 招聘筛选与合规 RAG 知识库建设中？

- **`tau-job-research-skills`（MIT）：防烧钱、讲证据的模块化 Agent 技能设计范式**：
  - **六步解耦技能链**：将复杂的岗位/人才调研拆成 6 个互不强依赖的独立技能（`job-search-brief` 简历提炼 → `linkedin-search-plan` 搜索式规划 → `job-research` 多源检索 → `fit-review` 证据对比 → `company-brief` 背景尽调 → `shortlist-review` 优先级排序）。
  - **外部付费 MCP 的“三段式防呆检查点（Manual Checkpoints）”**：企业接入外部商业数据 API（如 Apify、商业企查查/征信接口）最怕 Agent 陷入死循环一晚上刷爆账单。Tau 规定了标准三步走：① 先调免费的 `get_scout_status` 仅返回连接状态与 Token 存在布尔值（**绝不暴露密钥明文，也绝不发起任何付费查询**）；② 跑本地合成数据 Demo 验证推理链路；③ 显式设定单次结果条数与金额上限（Spending Cap）后再发起真实检索，且输出的 Shortlist 必须诚实列出 **Fit（有简历证据支撑的匹配点）、Gaps（明确缺口）与 Unanswered Questions（需面试追问的未知项）**。
- **`adunext/human-video-knowledge`：企业 RAG 语料库的“字节级防洗稿与许可证隔离”契约**：
  - 许多企业知识库把网上爬来的教程让大模型重写一遍就入库，既丢失了原作者的精妙细节，又混淆了版权边界。
  - `human-video-knowledge` 提供了教科书级的语料治理结构：所有入库源文件保存在 `upstream/` 下**保持原始字节一字不改**，用根目录 `SHA256SUMS.txt` 锁死字节完整性；通过 `COLLECTION.json` 与 `batches/*/SOURCES.json` 逐批记录精确来源、固定版本与收录范围（严格区分“完整规范文档”与“局部 README/辅助文件”）；将仅有许可证存根的记录隔离在 `license-only/` 下，并明确执行**“公开可访问 ≠ 允许再分发或训练”**的合规红线。

---

## ③ 🧭 直观可视化图解（选型决策树 + 企业集成架构 + 业务流时序图）

### 3.1 企业 LoRA 微调、具身 Agent 评测与合规知识/检索选型决策树

```mermaid
flowchart TD
    A["企业面临模型微调、Agent 评测或合规检索需求"] --> B{"核心技术诉求属于哪个领域？"}
    B -->|"多架构图像/视频模型 LoRA 微调 (Flux/Qwen/Wan/Z-Image)"| C{"是否希望复用现有 ComfyUI 画布且在 8-12GB 卡上训练？"}
    C -->|"是：零外部 pip 依赖 + 支持 FP8/GGUF + 训完直连采样器"| D["采用 cyberterm/ComfyUI-OmniLoRA (Apache-2.0)<br/>adafactor + CPU 层流式卸载 + RGBA 掩码 + 安全中断"]
    C -->|"否：百卡集群大规模全参微调"| E["采用 DeepSpeed / Megatron-LM 分布式训练集群"]
    B -->|"具身机器人 / 物理仿真 / 工业控制 Agent 能力评测"| F{"如何防止 Agent 偷看场景配置或伪造轨迹？"}
    F -->|"需严格盲盒隔离 + 哈希链封存 + 断网容器重放"| G["采用 ZIWU-AI/robotics-bench (Apache-2.0)<br/>CPU Docker 门禁 (gate.py) + 远端 Isaac GPU 池"]
    B -->|"企业证据链检索技能与高合规知识库归档"| H{"具体数据治理任务？"}
    H -->|"零后端 BYO-Token 岗位/人才匹配 + 防误扣费预检"| I["采用 ArsenOria/tau-job-research-skills (MIT)<br/>6 大独立 Skill + get_scout_status 零费用门禁"]
    H -->|"外部专业资料入库需保留原始字节与独立许可证"| J["遵循 adunext/human-video-knowledge 规范<br/>SHA256SUMS 字节锁死 + upstream/ 与 license-only/ 隔离"]
```

### 3.2 企业 AIGC 闭环微调、防篡改 Agent 靶场与合规知识工程集成架构

```mermaid
flowchart LR
    subgraph CorpusGov["字节级版权溯源语料库层"]
        RAW["外部受权专业文档与资产"] --> HVKB["human-video-knowledge 规范<br/>COLLECTION.json + SHA256SUMS.txt<br/>区分 upstream/ 与 license-only/"]
    end

    subgraph InGraphLoRA["ComfyUI 画布内通用低显存 LoRA 微调层 (Apache-2.0)"]
        HVKB -->|"合规训练集 + RGBA 掩码"| OMNILORA["cyberterm/ComfyUI-OmniLoRA<br/>1. 复用画布 FP8/INT8/GGUF 底模<br/>2. Adafactor (-80% VRAM) + CPU 层流式卸载<br/>3. 临时接管 SageAttention → PyTorch SDPA"]
        OMNILORA -->|"训练后 MODEL 直连"| KSAMPLER["ComfyUI KSampler 当场验效<br/>+ Loss Tracker / 中断自动存快照"]
    end

    subgraph AgentVerify["防作弊哈希链 Agent 评测与证据链检索层"]
        AGENT["待测工业/具身/招聘 Agent"] --> ROBOBENCH["ZIWU-AI/robotics-bench (Apache-2.0)<br/>盲盒接口隔离 → 哈希链封存录制<br/>→ 无网容器重放 (ref=1, forged=0)"]
        AGENT --> TAUSKILL["tau-job-research-skills (MIT)<br/>get_scout_status 零扣费预检<br/>→ Fit / Gaps / Questions 证据矩阵"]
    end
```

### 3.3 `ComfyUI-OmniLoRA` 画布内训练与 `robotics-bench` 哈希链断网重放核验时序图

```mermaid
sequenceDiagram
    autonumber
    participant Designer as AIGC 架构师 / 评测工程师
    participant Comfy as ComfyUI 画布 (8-12GB GPU)
    participant Omni as ComfyUI-OmniLoRA (Apache-2.0)
    participant RoboAgent as 待测具身 Agent 容器
    participant Verifier as robotics-bench 无网重放裁判器

    Designer->>Comfy: 拖入 omni_lora_basic_workflow.json，连接 Qwen-Image-2.1 FP8 与 RGBA 数据集
    Comfy->>Omni: 启动训练 (reserve_vram_gb=1.0, optimizer=adafactor, use_alpha_mask=True)
    Omni->>Omni: 预缓存 VAE/CLIP，自动将 SageAttention 切换为可微 attention_pytorch，超显存冻结层走 CPU 流式传输
    Designer->>Omni: 在第 650 步观察 Loss 收敛，点击 Cancel / Interrupt 提前结束
    Omni-->>Comfy: 自动抢救落盘 _interrupted_step_650.safetensors，恢复 SageAttention 并直连 KSampler 出图

    Designer->>RoboAgent: 下发 gantry-push 任务受控接口与文档 (隐藏仿真器与裁判源码)
    RoboAgent->>Verifier: 通过受控接口发送动作指令流，生成前后咬合的哈希链封存录像 (Sealed Recording)
    Verifier->>Verifier: 在完全断网的新仿真世界中重放录像，校验哈希链完整性与最终物理状态 (Calibration: ref=1, forged=0)
    Verifier-->>Designer: 输出不可篡改的确定性评测得分
```

---

## ④ 📊 同类开源与商业云服务横向选型决策矩阵

| 对比维度 | `cyberterm/ComfyUI-OmniLoRA` (Apache-2.0) | `ZIWU-AI/robotics-bench` (Apache-2.0) | `tau-job-research-skills` (MIT) | `human-video-knowledge` (原许可保留) | 商业云服务与传统外置工具（Replicate 训练 API / Kohya_ss / 商业招聘 SaaS） |
|---|---|---|---|---|---|
| **核心能力定位** | **ComfyUI 画布内零外部依赖、跨 9 大硬件后端与 15+ 架构的通用 LoRA 训练器** | **接口盲盒隔离 + 哈希链封存 + 断网容器重放的具身/仿真 Agent 评测基准** | **6 大解耦技能 + BYO-Token 本地 STDIO MCP 的证据链岗位匹配工作流** | **保留原始字节、`SHA256SUMS` 校验与分批权利清单的影视知识库** | 按次计费云端 LoRA 训练 API、重度外置训练脚本与中心化简历匹配 SaaS |
| **硬件与环境友好度** | 零额外 `pip` 包；直接训 FP8/INT8/GGUF；`adafactor` + CPU 流式卸载适配 8–12GB 显卡 | 基础层仅需普通 Docker CPU 容器（`<500` 行 MuJoCo 示例），可选扩展至 Isaac GPU 池 | 纯 Markdown 技能 + 本地轻量 STDIO MCP，自带 `get_scout_status` 零费用预检 | 纯静态原始文件与 JSON 清单，任何标准 `sha256sum` 工具即可核验 | Kohya/ai-toolkit 需独立维护几十 GB 依赖且易与 SageAttention 冲突 |
| **防翻车与安全合规机制** | 训练自动切换可微 SDPA 并在结束后恢复；RGBA 掩码防学背景；取消自动存中断权重 | 严防 Agent 读场景作弊或篡改日志；空跑与伪造录像强制归零 | 绝不自动读取仓库 `.env` 明文或回显 Token；强制输出证据缺口与未知问题 | 明确区分 `upstream/` 与 `license-only/`，杜绝“免费可读=可商用重分发”侵权 | 云端训练需上传企业未公开产品图；普通评测易被 Agent 注入高分 |
| **开源协议与治理要点** | **Apache-2.0** | **Apache-2.0** | **MIT** | **逐文件保留上游原始许可证**（严禁统一重授权） | 商业闭源按次/按席位收费 |
| **45 人团队月度 TCO** | **~$80.00/月**（复用本地/内网现有 ComfyUI 显卡电费） | **$0.00/月**（复用现有 CI Docker Runner） | **按实际受控 Apify 额度计费**（零平台抽成） | **$0.00/月** | **$7,360.00/月**（云端按次训练费 + 招聘 SaaS 席位 + 41 小时环境排障与防作弊复核） |

---

## ⑤ 🧪 应用落地定量收益/TCO 对比与 7-Card 报告映射

### 5.1 架构师闭式 TCO 算例（45 人 AIGC 平台、具身智能评测与技术招聘团队月度运营成本）

> **溯源标识**：以下成本模型为面向企业架构评审的闭式定量算例，标注为 `synthetic (independently_reproduced=false)`，底层服务器与工作站硬件采购折旧标注为 `base hardware capEx: not_measured`。

| 成本构成项 | 方案 A：云端按次 LoRA 训练 API + 无隔离仿真云池 + 商业招聘检索 SaaS | 方案 C：画布内 `ComfyUI-OmniLoRA` + `robotics-bench` 门禁 + `Tau Skills` + 合规知识库 | 计算公式与架构说明 |
|---|---|---|---|
| **云端 LoRA 训练额度、仿真算力与外部检索 SaaS 订阅** | **$3,260.00 / 月** | **$80.00 / 月** | 方案 A：高频多架构云端 LoRA 训练 API + 商业招聘 SaaS 席位 + 云仿真池 = `$3,260.00/月`；方案 C：Apache-2.0 `ComfyUI-OmniLoRA` 复用本地 8–12GB 显卡 + `robotics-bench` Docker CPU 门禁 + 受控 BYO-Token 检索 = `$80.00/月` |
| **外置训练环境排障、仿真作弊复核与人工简历核验（$100/h）** | **$4,100.00 / 月**（`41.0h × $100.00`） | **$250.00 / 月**（`2.5h × $100.00`） | 方案 A：45 人团队每月耗费 `41.0 小时` 处理 Kohya/SageAttention 依赖冲突、重跑中途断电丢失的 LoRA、排查仿真 Agent 作弊与核对简历（`$4,100.00`）；方案 C：画布原位训练 + 哈希链断网重放 + 证据矩阵将人工缩减至 `2.5 小时`（`$250.00`） |
| **月度总拥有成本（Monthly TCO）** | **$7,360.00 / 月** | **$330.00 / 月** | **月度净节省 $7,030.00 / 月（成本降低 -95.52%，年化节省 $84,360.00，`not_measured` 硬件折旧）** |

```chart
{
  "data": {
    "values": [
      { "Category": "Cloud LoRA APIs, Sim Pools & Recruiting SaaS", "Deployment": "Path A: Commercial Cloud APIs & Manual Triage", "MonthlyCostUSD": 3260 },
      { "Category": "Env Debugging, Sim Replay & CV Audit Labor (45-Eng)", "Deployment": "Path A: Commercial Cloud APIs & Manual Triage", "MonthlyCostUSD": 4100 },
      { "Category": "Cloud LoRA APIs, Sim Pools & Recruiting SaaS", "Deployment": "Path C: OmniLoRA + robotics-bench + Tau Skills + Video-KB", "MonthlyCostUSD": 80 },
      { "Category": "Env Debugging, Sim Replay & CV Audit Labor (45-Eng)", "Deployment": "Path C: OmniLoRA + robotics-bench + Tau Skills + Video-KB", "MonthlyCostUSD": 250 }
    ]
  },
  "semantic_types": {
    "Category": "Category",
    "Deployment": "Name",
    "MonthlyCostUSD": "Amount"
  },
  "chart_spec": {
    "chartType": "Grouped Bar Chart",
    "title": "Round 575 Milestone: OmniLoRA + robotics-bench + Tau Skills cut monthly TCO by 95.52%",
    "subtitle": "Monthly cost in USD (45-engineer org across LoRA training, agent eval & evidence research, synthetic)",
    "encodings": {
      "x": "Category",
      "y": "MonthlyCostUSD",
      "group": "Deployment",
      "color": "Deployment"
    }
  }
}
```

### 5.2 与本轮 7-Card 4:5 视觉报告（`cards.html` / `cards.en.html`）的联动

- **适用场景（✅ Good Fit）**：在现有 ComfyUI 8–16GB 工作站上直接基于 FP8/GGUF 底模训练角色/产品/画风 LoRA（含 RGBA 透明抠图防背景污染）、构建防 Agent 偷看源码的哈希链封存 + 断网重放评测靶场、零后端证据链岗位匹配、以及字节级 SHA-256 版权溯源语料库建设。
- **不适用场景（⛔ Not For）**：百亿参数底模从零预训练（`OmniLoRA` 专精参数高效 LoRA 微调）、未经 `get_scout_status` 预检与花费上限控制直接让 Agent 裸跑付费爬虫 API、或将 `human-video-knowledge` 中仅含许可证存根（`license-only/`）的条目误认为已获完整内容授权。

---

## ⑥ 🛠️ 企业引入与架构评审 Checklist（可直接复制进架构评审单）

- [ ] **ComfyUI 画布内 LoRA 低显存预算与 RGBA 掩码配置**：在 8–12GB 显卡工作站部署 `cyberterm/ComfyUI-OmniLoRA`（Apache-2.0）时，默认启用 `optimizer = "adafactor"`、`reserve_vram_gb = 1.0` 与 `VAE & CLIP Pre-Cache` 节点；针对商品与角色训练集强制开启 `use_alpha_mask = True` 以避免模型记忆背景噪声。
- [ ] **具身与工具 Agent 评测靶场的“盲盒隔离 + 哈希链断网重放”门禁**：参照 `ZIWU-AI/robotics-bench`（Apache-2.0）改造企业内部 Agent 验收流水线，将待测 Agent 与评测裁判器（Verifier）物理隔离在不同容器中，强制通过 `gate.py` 驗證“参考解得 1 分、空跑与篡改哈希链录像得 0 分”。
- [ ] **外部付费 MCP 工具三段式预检门禁（Preflight Gate）**：引入 `ArsenOria/tau-job-research-skills`（MIT）或同类外部数据源 MCP 时，强制执行“① 免费状态布尔检查（不回显密钥）→ ② 本地合成数据演练 → ③ 显式带金额/条数上限的实网查询”三步检查点。
- [ ] **企业 RAG 知识库字节级 SHA-256 封存与许可证分级清单**：参照 `adunext/human-video-knowledge` 规范建立内部语料库的 `COLLECTION.json`、`SOURCES.json` 与 `SHA256SUMS.txt`，严格区分已获完整授权的原始文件与待补齐授权的索引条目，禁止洗稿改写冲掉上游版权声明。
