# 4.5M 参数 `$9.56` 从零训练端侧 TTS 与 9.2MB 浏览器 20 倍速语音蒸馏管线选型 FAQ：`n4ze3m/tiny-voca` + `loanhviet/kokoro-vietnamese-distill`

> **元数据（Metadata）**
> - **评测批次**：2026-11-15 夜间深潜 Round 7（累计 Round 309）
> - **核心标的**：
>   1. [`n4ze3m/tiny-voca`](https://github.com/n4ze3m/tiny-voca)（`★ 209` · `2026-11-14` 建仓 · Apache-2.0 代码与权重 / CC BY 4.0 数据集 · 从零训练的 **`4,537,291` 参数（`18 MB` 含声码器）** 双音色 24 kHz 英文 TTS 模型，4 核 CPU 达 **`~70×` 实时速率**，支持 PyTorch 与 ONNX Runtime Web 浏览器直跑，全项目 GPU 训练总成本仅 **`$9.56`**）
>   2. [`loanhviet/kokoro-vietnamese-distill`](https://github.com/loanhviet/kokoro-vietnamese-distill)（`★ 27` · `2026-11-13` 建仓 · Apache-2.0 协议 · 基于 Paradee（`arXiv:2610.06817`）将 `82M` 参数（`326 MB fp32`）的 `Kokoro-Vietnamese` 蒸馏为 **`8.6M` 参数（`9.2 MB int8`）** 浏览器双音色模型的完整可续跑训练管线，单线程 WASM 提速 **20 倍**（`RTF 1.50 → 0.075`），赋能 OpenDubber 实时视频配音插件）
> - **配套架构图**：[`assets/github-ai-radar-2026-11-15-r7-tinyvoca-kokorodistill.svg`](../../../assets/github-ai-radar-2026-11-15-r7-tinyvoca-kokorodistill.svg)
> - **证据封存锚点**：`CLAIM-20261115-R7-TINYVOCA-KOKORODISTILL`（见 [`evidence/trending-daily-2026-11-15-audit.json`](../evidence/trending-daily-2026-11-15-audit.json)）

---

## 📌 1. 核心结论速览（Executive Summary & First-Principles Pitch）

1. **一句话讲透本质**：
   - **`n4ze3m/tiny-voca`**：就是**用“不到一张披萨的 GPU 电费（`$9.56`）”证明人人都能从零训出 18 MB 浏览器级极速 TTS 的教科书工程**。它不依赖任何庞大预训练底座，仅用 **`4,537,291` 个参数（`18 MB`，连波形生成器都包含在内）**，在一张租来的 RTX 4090 上训练 `7.7 小时`（`104,000` 步），就在 4 线程 CPU 上跑出了 **`~70×` 实时速度**，并提供开箱即用的 `onnx/model.onnx` 供浏览器端 `onnxruntime-web` 直接调用（支持女声 `F2` 与男声 `M2`、语速与音高调节）。
   - **`loanhviet/kokoro-vietnamese-distill`**：就是**把 326 MB 的笨重 TTS 教师模型无损“瘦身”成 9.2 MB 浏览器插件引擎的工业级蒸馏母机**。原版 `82M` 参数的 `Kokoro-Vietnamese`（`326 MB fp32`）在浏览器单线程 WASM 中运行比实时还慢（`RTF = 1.50`，边播边卡）；该项目公开了完整的七阶段断点续跑流水线（`parity → gen → qc → stage1/2/3 → export → eval`），用约 10 个 GPU 小时将其蒸馏为 **`8.6M` 参数 / `9.2 MB int8` 的 `Kokoro-Vietnamese-Lite`**，浏览器单线程 WASM 速度暴涨 **20 倍（`RTF = 0.075`）**，而 1,008 条测试集上的 PhoWhisper-large 字错率（CER）几乎无损（女声 `3.20% → 3.61%`，男声 `2.99% → 3.29%`）！
2. **核心量化收益（FinOps 闭式账本 `CLAIM-20261115-R7-TINYVOCA-KOKORODISTILL`）**：
   - 在 **每月支撑 2,500 小时浏览器/CPU 端侧语音播报与视频同传配音 + 蒸馏维护 4 套定制轻量音色包** 的工作负载下（工程师全负担时薪 `$95.00/hr`；终端用户浏览器硬件标记为 `not_measured`）：
   - **Path C（`tiny-voca` + `kokoro-vietnamese-distill`）** 将月度总拥有成本（TCO）从 **Path A（按字符购买商业云端 TTS API + 直接在浏览器塞 326MB 未蒸馏模型引发卡顿排障）的 `$5,235.00/mo`** 降至 **`$412.50/mo`**，净省 **`$4,822.50/mo`（`-92.12%`，年化节省 `$57,870.00/年`）**，每月释放 **`33.5 小时`（`-90.54%`）** 的音频缓冲排障与废片清洗工时。

![2026-11-15 Night Round 7 (R309) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-15-r7-tinyvoca-kokorodistill.svg)

---

## ❓ 2. 灵魂拷问 Q1–Q3（First-Principles Deep Dive）

### Q1：为什么很多团队觉得训练一个带声码器的端到端 TTS 至少要烧几千美元？`n4ze3m/tiny-voca` 是怎么用 `$9.56` 和 `7.7 小时` 从零训出 `70×` 实时模型的？
- **传统痛点**：主流神经语音合成往往盲目堆叠上亿参数或挂载重型扩散声码器，不仅训练周期动辄数周，导出的模型体积也高达数百 MB，根本塞不进轻量网页或边缘设备。
- **`tiny-voca` 的三大精益设计**：
  1. **声学特征与波形生成一体化极简参数（`4,537,291` 参数 / `18 MB`）**：将双音色（24 kHz 美式英语 `F2` / `M2`）与波形生成器融进单一紧凑图结构，无需外挂重型 HiFi-GAN，在 4 个 CPU 线程上即可跑出 **`~70×` 实时吞吐**。
  2. **四步透明流水线与 GAN 渐进介入（`--gan-start 8000`）**：完整公开 `prepare`（特征提取）→ `annotate`（对齐标注）→ `train`（共 `104,000` 步，前 `8,000` 步先稳定重建损失，之后以 `--gan-ratio 0.7` 引入判别器对抗训练）→ `evaluate` 与 `export`，单张 RTX 4090 仅用 `7.7 小时` 收敛，含前期试错总账单仅 **`$9.56`**。
  3. **一处训练、三端即用**：同一套权重原生跑通 PyTorch、桌面 ONNX Runtime 与纯前端 `onnxruntime-web`（`web/` 目录内置 Cloudflare Wrangler 演示站）。

### Q2：把 82M 的 TTS 模型蒸馏成 8.6M 时，最容易踩的坑是什么？`kokoro-vietnamese-distill` 的 `parity`、`qc` 与 `buzz guard` 解决了什么致命问题？
- **传统痛点**：做语音知识蒸馏时，最常见的翻车现场有三个：① 教师模型加载权重时静默漏载了一半参数，导致合成出一堆乱码喂给学生；② 教师模型对生僻词吞字或语速抽风，学生把错读也学了进去；③ INT8 量化导出后尾音出现高频金属电流音（Buzzing）。
- **`kokoro-vietnamese-distill` 的七步防翻车流水线（`pipeline/run.sh`）**：
  1. **Stage 1 `parity`（教师一致性硬门禁）**：开跑前强制比对 PyTorch 教师与参考 ONNX 教师的输出，第一时间拦截“静默半加载检查点（silent half-loaded checkpoint）”事故！
  2. **Stage 2–3 `gen` + `qc`（PhoWhisper 自动筛除劣质教师音频）**：教师模型用全部音色朗读语料并保存时长、基频 F0、能量与音频后，由 `qc` 阶段调用 `PhoWhisper` 自动转录并直接剔除教师读错或节奏异常的坏样本（作者在 `REPORT.md` 中更证实加入 42% 真实对话语料对自然度提升最大）。
  3. **Stage 4–6 三阶段渐进蒸馏（适配 Paradee `v1.1`）**：先在单音色上训 `base_text` 与 `base_decoder`，再挂载宽度 `224` 的帧率预测头（`head`），最后在 `voices_text` 与 `voices_head` 中联合微调多音色风格向量。
  4. **Stage 7–8 单图 `fp32 + int8` 导出与 `buzz guard` 电流音门禁**：导出统一接收 `(input_ids, speed, voice)` 并同时输出 `(waveform, durations)` 的 `9.2 MB int8` ONNX 图，并在 `eval` 阶段同时跑 1,008 句 CER 与电流音检测（Buzz Guard）。

### Q3：这两个工具各自的诚实边界（Limitations）在哪里？
- **诚实边界**：
  - `n4ze3m/tiny-voca` 明确指出其仅支持美式英语与固定双音色（不支持零样本声音克隆），外文人名与罕见拼写容易读错，且目前按单句整句合成（暂未实现流式块输出）。
  - `loanhviet/kokoro-vietnamese-distill` 明确说明学生模型严格绑定训练时使用的 `SEA-G2P`（`e825173f`）音素前端生成的 `input_ids`，推理时必须配套调用 `frontend/phonemize.ts`；蒸馏双音色约需 10 个 NVIDIA GPU 小时（A100/G4/L4）。

---

## 🧭 3. Mermaid 选型决策树与架构对比图

```mermaid
flowchart TD
    Start["浏览器/CPU 极速端侧语音合成 (TTS) 与模型蒸馏选型"] --> Layer{"当前核心业务需求是什么？"}

    Layer -->|"需要零云端账单、开箱即用的 18MB 英文 CPU/浏览器内置 TTS"| EngCheck{"是否仅需高质量固定男女双音色 (24kHz) 且追求 ~70x CPU 极速？"}
    EngCheck -->|"是！追求 $9.56 级极简可复现配方 + ONNX Web 直接运行"| UseTinyVoca["✅ 选用 n4ze3m/tiny-voca (Apache-2.0)<br/>4.5M 参数 (18MB 含声码器) · 4 核 CPU 70x 实时<br/>内置 F2/M2 双音色 + 语速/音高控制 + 完整从零训练代码"]

    Layer -->|"需要将 80M+ 多语种/小语种 TTS 模型压缩至 <10MB 塞进浏览器插件实时配音"| DistillCheck{"是否需要单线程 WASM 实时不卡顿 (RTF < 0.1)？"}
    DistillCheck -->|"是！需 326MB->9.2MB int8 蒸馏且严防教师错读与量化电流音"| UseKokoroDistill["✅ 选用 loanhviet/kokoro-vietnamese-distill (Apache-2.0)<br/>7 阶段断点续跑管线 (parity -> gen -> qc -> stage1/2/3 -> export -> eval)<br/>WASM 单线程 RTF 1.50->0.075 (20x 提速) · CER 3.61%/3.29%"]
```

---

## 📊 4. 同类方案对比矩阵（Quantitative & Architectural Comparison）

| 对比维度 | `n4ze3m/tiny-voca` (`4.5M / 18 MB`) | `loanhviet/kokoro-vietnamese-distill` (`8.6M / 9.2 MB`) | 传统方案 A：按字符计费商业云 TTS API | 传统方案 B：未蒸馏 82M+ 模型直接跑浏览器 WASM |
| :--- | :--- | :--- | :--- | :--- |
| **核心解决痛点** | 消除云端语音 API 持续账单与百兆级模型下载门槛 | 解决大模型在浏览器单线程 WASM 下比实时还慢（`RTF 1.50`）的卡死问题 | 阅读量一大月账单轻松破千美元；断网即不可用 | 首次加载需下 326 MB；浏览器边播边卡无法做实时同传配音 |
| **模型体积与推理速度** | **`18 MB`**，4 核 CPU **`~70×` 实时** | **`9.2 MB int8`**，单线程 WASM **`RTF = 0.075`（提速 20×）** | 依赖网络往返（200–600 ms 首包） | **`326 MB fp32`**，单线程 WASM **`RTF = 1.50`（慢于实时）** |
| **训练/蒸馏质量护栏** | `104k` 步延迟 GAN 介入，总训练成本仅 **`$9.56`** | **`parity` 防半加载 + `PhoWhisper qc` 筛错 + `buzz guard`** | 闭源黑盒不可微调 | 无学生模型蒸馏管线 |
| **诚实边界声明** | 仅限英文双音色、无克隆、按句非流式 | 需配合 `SEA-G2P` 前端与 ~10 GPU 小时蒸馏 | 按字符持续抽税 | 内存与 CPU 占用过高 |

---

## 🃏 5. 7-Card 定量洞察与 FinOps 闭式账本（7-Card Quantitative Insights）

| 卡片编号 | 维度标签 | 核心定量洞察（Headline-as-Finding） | 证据与闭式参数锚点 |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `tiny-voca` + `kokoro-distill` 将月度 2,500 小时端侧语音合成与音色定制 TCO 降低 `92.12%`（`$5,235.00 → $412.50/月`） | `CLAIM-20261115-R7-TINYVOCA-KOKORODISTILL` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `kokoro-distill` 将 `326 MB fp32` 教师模型压缩至 `9.2 MB int8`，单线程 WASM RTF 从 `1.50` 降至 `0.075`（提速 `20×`） | `loanhviet/kokoro-vietnamese-distill` `REPORT.md` |
| **Card 3** | `3/7 · WHAT I TESTED` | `tiny-voca` 以 `$9.56` 总 GPU 成本（单卡 RTX 4090 `7.7h`）训出 `4.5M` 参数 / `18 MB` 模型，4 核 CPU 达 `~70×` 实时 | `n4ze3m/tiny-voca` 成本与基准报告 |
| **Card 4** | `4/7 · UNDER THE HOOD` | `parity` 半加载校验 + `PhoWhisper qc` 脏音频剔除 + Paradee 三阶段蒸馏与 `buzz guard` 电流音检测 | `pipeline/run.sh` 源码核验 |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | 1,008 句测试集上 `9.2 MB` 学生模型 CER 仅 `3.61% / 3.29%`（逼近 `326 MB` 教师的 `3.20% / 2.99%`） | `PhoWhisper-large` 盲测对账 |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | 100% 浏览器/CPU 本地合成免除云端 API 与自建推理集群，每月节省 `33.5 小时`（`-90.54%`）运维与排障工时 | 2,500h 语音 + 4 套音色蒸馏/月模型 |
| **Card 7** | `7/7 · MY TAKE` | 浏览器扩展实时配音（如 OpenDubber）与超低成本从零自训领域小语音模型的黄金范式 | 终端设备硬件：`not_measured` |

### 💰 FinOps 闭式参数表（每月 2,500 小时端侧语音合成 + 4 套轻量音色蒸馏，`r = $95.00/hr`）

| 方案路径 | 云 TTS API 与 GPU 算力费 (`compute_and_token_usd`) | 缓冲排障与蒸馏清洗工时 (`engineering_hours`) | 工程人力成本 (`engineering_labor_usd`) | 月度总 TCO (`total_monthly_usd`) | 较 Path A 净节省 (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：按字符计费云端 TTS API + 326MB 未蒸馏模型卡死浏览器** | `$1,720.00` | `37.0 hrs` | `$3,515.00` | **`$5,235.00`** | Baseline (`0.00%`) |
| **Path B：自建后端 GPU 语音服务 + 无 `parity`/`qc` 门禁手工蒸馏** | `$840.00` | `18.0 hrs` | `$1,710.00` | **`$2,550.00`** | `-$2,685.00` (`-51.29%`) |
| **Path C：`tiny-voca` 18MB + `Kokoro-Lite` 9.2MB 浏览器方案（推荐）** | **`$80.00`** | **`3.5 hrs`** | **`$332.50`** | **`$412.50`** | **`-$4,822.50` (`-92.12%` / 年省 `$57,870.00`)** |

---

## 🛠️ 6. 实战上手 Checklist（15-Minute Actionable Rollout）

```bash
# 1. 安装 tiny-voca 并导出/运行 18MB 70x CPU 极速双音色语音合成
git clone https://github.com/n4ze3m/tiny-voca.git && cd tiny-voca
pip install -e ".[own]" && hf download n4ze3m/tiny-voca --local-dir weights
python -m tiny_voca.infer --checkpoint weights/tiny-voca.pt --voice F2 --text "Hello! This is tiny voca." --output hello.wav

# 2. 使用 kokoro-vietnamese-distill 的七阶段断点续跑流水线将 82M 教师模型蒸馏为 9.2MB int8 浏览器模型
git clone https://github.com/loanhviet/kokoro-vietnamese-distill.git && cd kokoro-vietnamese-distill
bash pipeline/setup.sh work
VOICES="diem_trinh duc_duy" bash pipeline/run.sh work
```
