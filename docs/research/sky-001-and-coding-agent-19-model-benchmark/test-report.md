# SKY-001 工程世界模型与 Coding Agent 十九模型基准评测报告（增补报告 5：`Claude Haiku 5.5` 与 `Gemini 4 Argon`）

> **English Version**: [`test-report.en.md`](test-report.en.md) · **综合研究文档**: [`README.md`](README.md)（中文） / [`README.en.md`](README.en.md)（English）
> **版面规格**: 7-Card 4:5 竖版视觉评测卡片集（`900x1125` / `1080x1350`）
> **交互式 / 打印卡片集**: [`test-report-cards.html`](test-report-cards.html) · **结构化数据**: [`report.json`](report.json) · **一手证据锁**: [`evidence.json`](evidence.json) · **离线校验器**: [`simulator/sky001_and_19model_verifier.py`](simulator/sky001_and_19model_verifier.py)
> **数据溯源**: `anonymized_reported`（`independently_reproduced=false`） · **固定上游提交**: [`satomic/copilot-benchmark@a1913835`](https://github.com/satomic/copilot-benchmark/commit/a191383571a13143685fd6f7787512c4e281a9ba) + Skyfall AI 生产前端 Bundle（`index-D5BqB7X_.js` & `article-D6mnIEDb.js`）

---

## Card 1 (`1 / 7` · `HANDS-ON · ENGINEERING WORLD MODEL & 19-MODEL CODING BENCHMARK`)

### Haiku 5.5（总榜 #4 · $0.33）、Gemini 4 Argon（100% 隐藏测试通过）与 **SKY-001 98.4 倍关键路径压缩**

在增补报告 5（`2026-10-15`，Copilot CLI `1.0.98`）中，评测矩阵扩展至 **19 个模型 × 11 道 Python 标准库工程任务（共 `209` 次非参考串行 CLI 运行，每模型 `1,310` 项隐藏断言）**：轻量级 **`Claude Haiku 5.5` 以 `$0.33` 极低成本跃升至总榜第 4（`99.24 / 100`，仅错 2 项隐藏断言）**，而 **`Gemini 4 Argon` 实现 `1,310 / 1,310`（`100%`）隐藏断言全通过（总均分 `98.59`，总成本 `$2.82`）**。同步对 Skyfall AI 发布的 **`SKY-001` 工程世界模型**进行双源前端 Bundle 审计表明：分层 3D 状态树分解与 Matryoshka 双通道扩散在 1,000 例 CAD/BIM 构造任务上比单次盲写脚本的前沿 LLM **快 `51.0x–118.5x`、便宜 `150.0x–188.4x`**。

#### 工作台预览（`Dual-Track Engineering Benchmark Workbench · 19 Coding Agents + SKY-001 CAD/BIM`）

| 左栏 · 评测赛道、批次与动作门禁 | 中栏 · 协议与验证契约 | 右栏 · 核心指标胶囊与 Top 决策 |
|---|---|---|
| **Track A · Coding Agent（19 模型 × 11 题 = 209 次运行）**<br>• **简单级（`A1–A5`）**：`70` 隐藏测试 + `15` 规范 + `15` 质量<br>• **中等级（`M1–M2`）**：`55` 隐藏 + `15` 自测 + `15` 规范 + `15` 质量<br>• **复杂级（`C1–C4`）**：`58` 隐藏 + `12` 自测 + `15` 规范 + `15` 质量<br>• **增补批次 5（`2026-10-15` · CLI `1.0.98`）**：新增 **`Claude Haiku 5.5`** 与 **`Gemini 4 Argon`**（`+22` 份完整运行包）<br><br>**Track B · SKY-001 工程世界模型（2,000 例 CAD/BIM）**<br>• **Stage 1（Hierarchical Composer）**：粗粒度 3D DiT $\rightarrow$ 递归树分割 $\rightarrow$ 叶节点遮挡几何精修<br>• **Stage 2（Construction World Model）**：3D 实体中间态子目标 + 2D 逆向草图动作 + Matryoshka 双通道精修<br><br>**动作门禁（Action Gating）**<br>• `Act automatically`：`1,310/1,310` 隐藏全过且均分 `>= 98.45`（`9` 模型）<br>• `Confirm`：均分 `97.50–98.44` 或隐藏未满分（`8` 模型）<br>• `Send to a human`：隐藏 `< 1,260` 或复杂题 `< 96.0`（`2` 模型） | **受控评测与离线验证器**<br>• 独立 UUID 会话、`--no-custom-instructions --disable-builtin-mcps`<br>• 推理强度 `effort=medium`（`repeat=1`）<br>• 外部隔离 `_verify/` 隐藏 `pytest` 套件（`1,310` 断言）<br>• Skyfall 生产包 SHA-256 锁定核验与关键路径模拟器（`6/6` 单元测试通过） | **`Haiku 5.5: 99.24 (#4) · $0.33 · 35.1m`** · **`Gemini 4 Argon: 98.59 (#10) · 1310/1310 · $2.82`** · **`SKY-001 CAD: 79.7% IoU · 3.9s · $0.005`** · **`SKY-001 BIM: 43.6% IoU · 1.22s · $0.0024`**<br><br>1. **`supplement_5_coding_breakthrough` (`choice`)** $\rightarrow$ **`Haiku 5.5` (`99.24 · $0.33`) & `Gemini 4 Argon` (`98.59 · 1310/1310`)** · `Act automatically`<br>   • Haiku 5.5 总均分：`99.2%`（成本比 Sonnet 5.5 低 `88.6%`）<br>   • Gemini 4 Argon 总均分：`98.6%`（第 9 个隐藏测试满分模型）<br>2. **`sky_001_world_model_advantage` (`score`)** $\rightarrow$ **`51x–118.5x` 更快 & `150x–188.4x` 更省（CAD IoU 领先 Astra `+0.6` pt）** · `Confirm`<br>   • Jaguar E-Type（103 叶节点，深度 5）：`10,336` 步串行压缩至 `105` 步（`98.44x`）<br>3. **`executable_cad_vs_visual_rollout` (`noul`)** $\rightarrow$ **`No`（当前输出为视觉 3D 状态 + 2D 草图序列，非可编辑参数化特征树）** · `Confirm` |

> **溯源说明**：两条工程智能赛道均基于一手公开产物进行审计（`anonymized_reported`，`independently_reproduced=false`）。在配备编译器/测试闭环的代码空间中，`Haiku 5.5`（`$0.33`）与 `Gemini 4 Argon`（`$2.82`，`$0` 缓存写入费）逼平旗舰；而在无状态反馈的单次 3D 几何生成中，通用 LLM 脚本彻底暴露串行瓶颈与空间盲区。

---

## Card 2 (`2 / 7` · `SCENARIO: HAIKU 5.5, GEMINI 4 ARGON & SKY-001 DUAL-SOURCE AUDIT`)

### Haiku 5.5 暴涨 +5.28 分至 99.24（$0.33）；Argon 达成 1,310/1,310；SKY-001 缩短关键路径 98.4 倍。

> *"Supplement 5 提交 a1913835（2026-10-15，CLI 1.0.98）新增了 claude-haiku-5.5 与 gemini-4-argon 的 22 份运行包，同时经字节级核对确认前 17 个模型的得分与隐藏测试通过数发生零漂移。Skyfall AI 的两个前端生产包（index-D5BqB7X_.js 与 article-D6mnIEDb.js）则完整暴露了 CAD/BIM 原始数组与装配树节点数。"*

#### 1. `claude_haiku_5_5_deep_dive` · `score` · **Confirm**
- **问题**：`Claude Haiku 5.5` 相比前代 `Haiku 4.5` 与同代 `Sonnet 5.5` 在 11 道任务（CLI `1.0.98`，`effort=medium`）上的跨代跃迁表现如何？
- **结果**：**`99.24 / 100`（19 模型第 4 · `1,308 / 1,310` 隐藏测试 · `$0.33` · `94` 轮 · `45.3w` 输出 Token）** · 较 `Haiku 4.5` 总分 `+5.28` 分、复杂题 `+9.58` 分、成本下降 `91.6%`（`$3.93 -> $0.33`）；仅在 `C4-microvm` 的 `test_parse_errors` 漏掉 2 个语法错误断言
  - 中等级 `M1–M2` 均分（`99.50 / 100`）：`████████████████████` `99.5%`
  - 复杂级 `C1–C4` 均分（`99.22 / 100`）：`████████████████████` `99.2%`
  - 简单级 `A1–A5` 均分（`99.15 / 100`）：`████████████████████` `99.2%`

#### 2. `gemini_4_argon_deep_dive` · `score` · **Act automatically**
- **问题**：`Gemini 4 Argon` 相比 `Gemini 3.8 Flash` 与 `GPT-6.1 Sol`（`1.05M` 上下文，`$0/M` 缓存写入费）表现如何？
- **结果**：**`98.59 / 100`（19 模型第 10 · `1,310 / 1,310` 隐藏测试全过 · `$2.82` · `106` 轮 · `11.7w` 输出 Token）** · 彻底消除 `Gemini 3.8 Flash` 的 34 项隐藏测试失败，API 轮次减少 `61.7%`（`277 -> 106`），Wall 耗时缩短 `47.1%`（`5,122s -> 2,710s`）
  - 隐藏断言通过率（`1,310 / 1,310`）：`████████████████████` `100.0%`
  - 简单级 `A1–A5` 均分（`99.00 / 100`）：`████████████████████` `99.0%`
  - 复杂级 `C1–C4` 均分（`98.06 / 100`）：`████████████████████` `98.1%`

#### 3. `sky_001_bundle_discrepancy_audit` · `choice` · **Confirm**
- **问题**：交叉审计 Skyfall AI 技术博客包（`article-D6mnIEDb.js`）与产品着陆页包（`index-D5BqB7X_.js`）发现了哪些未公开披露的差异？
- **结果**：**博客包含 `Gemini 4`（CAD `76.9%` IoU，第 3 名），着陆页将其删除并替换为 `Opus 5.5`（`69.4%`）与 `Gemini 3.8 Flash`（`54.7%`）** · 在 BIM 1,000 图测试中，`Gemini 3.8 Flash`（`42.3%` IoU）反超 `GPT-6 Astra`（`40.6%` IoU）位居全榜第 2，仅落后 `SKY-001`（`43.6%`）`1.3` 个百分点
  - Jaguar E-Type 关键路径压缩比（`105` vs `10,336` 步）：`████████████████████` `99.0%`
  - SKY-001 Composer 盲测评审胜率（5/5 维度领先 Astra）：`████████████████████` `100.0%`
  - GPT-6 Astra 装配生成完整返回率（82% 资产未崩溃）：`████████████████░░░░` `82.0%`

> **深度发现**：`Haiku 5.5` 在 `A1`、`A4`、`M1`、`C2`、`C3` 五道题拿下 `100.0` 满分，在最难的 `C3-microdb`（377 项隐藏测试）与 `C2-git-object-store`（350 项隐藏测试）均实现零失误；`Gemini 4 Argon` 则凭借 `$0.00/M` 的 `cache_write` 定价在 `C3-microdb` 29 轮长上下文迭代中将总成本控制在 `$0.99`。

---

## Card 3 (`3 / 7` · `WHAT I TESTED`)

### 19 个 Coding 模型（209 次运行）+ SKY-001 2,000 例 CAD/BIM 完整评测矩阵

| 梯队 / 赛道 | 模型与资源画像 | 评测结果（均分 \| 复杂题 \| 隐藏测试 / IoU） | 动作门禁 |
|---|---|---|---|
| **Tier 1 · 旗舰天花板** | `Fable 5.1`（`142` 轮 · `55.9m` wall · `$14.45` · `15.8w` out） | **99.77 均分 \| 复杂 99.62 \| 1310/1310 隐藏** (100%) | **Auto** |
| | `Opus 5.5`（`92` 轮 · `31.8m` wall · `$5.84` · `17.6w` out） | **99.68 均分 \| 复杂 99.62 \| 1310/1310 隐藏** (100%) | **Auto** |
| | `Opus 5`（`188` 轮 · `63.3m` wall · `$17.41` · `24.9w` out） | **99.59 均分 \| 复杂 99.38 \| 1310/1310 隐藏** (100%) | **Auto** |
| **Tier 2 · 高性价比帕累托** | `Haiku 5.5 [NEW]`（`94` 轮 · `35.1m` wall · **`$0.33` 次低成本** · `45.3w` out） | **99.24 均分 (#4) \| 复杂 99.22 \| 1308/1310 (-2 隐藏)** (99%) ✕ | **Confirm** |
| | `Sonnet 5.5`（`65` 轮 · **`21.7m` 最快 wall** · `$2.89` · `16.1w` out） | **99.00 均分 \| 复杂 99.19 \| 1310/1310 隐藏** (99%) | **Auto** |
| | `GPT-6.1 Sol`（**`60` 最少轮次** · `27.4m` wall · `$1.71` · `9.3w` out） | **98.86 均分 \| 复杂 99.38 \| 1310/1310 隐藏** (99%) | **Auto** |
| | `HydraFusion`（`85` 轮 · `24.1m` wall · `$3.58` · `8.9w` out） | **98.45 均分 \| 复杂 98.75 \| 1310/1310 隐藏** (98%) | **Auto** |
| **Tier 3 · 高分主力与专精** | `Grok 4.7`（`143` 轮 · `181.2m` wall · `$12.22` · `51.5w` out） | **99.21 均分 (#5) \| 复杂 99.33 \| 1299/1310 (-11 隐藏)** (99%) ✕ | **Confirm** |
| | `GPT-6 Astra`（`62` 轮 · `32.7m` wall · `$9.91` · `9.8w` out） | **98.82 均分 \| 复杂 99.75 (#1) \| 1310/1310 隐藏** (99%) | **Auto** |
| | `Sonnet 5`（`190` 轮 · `53.2m` wall · `$7.87` · `23.9w` out） | **98.70 均分 \| 复杂 98.88 \| 1310/1310 隐藏** (99%) | **Auto** |
| | `Kimi K3`（`143` 轮 · `150.5m` wall · `$5.58` · `17.5w` out） | **98.68 均分 \| 复杂 98.81 \| 1305/1310 (-5 隐藏)** (99%) ✕ | **Confirm** |
| | `Gemini 4 Argon [NEW]`（`106` 轮 · `45.2m` wall · `$2.82` · `11.7w` out） | **98.59 均分 (#10) \| 复杂 98.06 \| 1310/1310 隐藏** (99%) | **Auto** |
| | `Grok 4.6`（`138` 轮 · `69.5m` wall · `$5.21` · `19.4w` out） | **98.57 均分 \| 复杂 98.06 \| 1305/1310 (-5 隐藏)** (99%) ✕ | **Confirm** |
| **Tier 4 · 低成本与轻量级** | `GPT-6 Luna`（`139` 轮 · `44.6m` wall · **`$0.17` 最低成本** · `14.5w` out） | **98.16 均分 \| 复杂 96.88 \| 1279/1310 (-31 隐藏)** (98%) ✕ | **Confirm** |
| | `Gemini 3.8 Flash`（`277` 轮 · `85.4m` wall · `$2.83` · `12.3w` out） | **98.00 均分 \| 复杂 97.00 \| 1276/1310 (-34 隐藏)** (98%) ✕ | **Confirm** |
| | `GPT-5.6 Luna`（`235` 轮 · `51.0m` wall · `$0.39` · `10.7w` out） | **97.88 均分 \| 复杂 96.42 \| 1293/1310 (-17 隐藏)** (98%) ✕ | **Confirm** |
| | `MAI-Code-1.1-Flash`（`192` 轮 · `56.5m` wall · `$0.53` · `23.3w` out） | **97.70 均分 \| 复杂 96.61 \| 1284/1310 (-26 隐藏)** (98%) ✕ | **Confirm** |
| | `DeepSeek-V4-Flash [BYOK]`（`420` 轮 · `179.0m` wall · `$1.95` · `29.0w` out） | **95.10 均分 \| 复杂 95.91 \| 1250/1310 (-60 隐藏)** (95%) ✕ | **Human** |
| | `Haiku 4.5`（`341` 轮 · `80.8m` wall · `$3.93` · `30.3w` out） | **93.96 均分 \| 复杂 89.64 \| 1239/1310 (-71 隐藏)** (94%) ✕ | **Human** |
| **Track B · SKY-001 CAD** | `SKY-001` vs `GPT-6 Astra`（`1,000` 零件 · `3.9s / $0.005` vs `199s / $0.75`） | **79.7% vs 79.1% IoU（+0.6 pt 统计持平；快 51.0x，省 150.0x）** (80%) | **Confirm** |
| **Track B · SKY-001 BIM** | `SKY-001` vs `Gemini 3.8 Flash` & `Astra`（`1,000` 平面图 · `1.22s / $0.0024`） | **43.6% vs 42.3% Flash & 40.6% Astra（快 118.5x，省 185.8x）** (44%) ✕ | **Confirm** |

> **门禁统计 Callout**：**19 个 Coding 模型中有 9 个实现 `1,310 / 1,310` 隐藏测试全通过且均分 `>= 98.45`（`Auto` 级）**：`Fable 5.1`、`Opus 5.5`、`Opus 5`、`Sonnet 5.5`、`GPT-6.1 Sol`、`GPT-6 Astra`、`Sonnet 5`、新增的 **`Gemini 4 Argon`** 以及 `HydraFusion`。
>
> **失误分析 Callout（`✕`）**：**`Claude Haiku 5.5` 以 `99.24` 分位列总榜第 4、成本仅 `$0.33`**，因 `C4-microvm` 漏掉 `2/296` 项语法错误检查（`1,308/1,310`）归入 `Confirm`；只需在 CI 管线挂载常规语法/单元测试守卫即可直接替代高价模型。

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`)

### Copilot CLI 70/15/15 评分协议 vs SKY-001 双阶段世界模型执行图

```json
{
  "track_A_copilot_cli_supplement_5": {
    "commit": "a191383571a13143685fd6f7787512c4e281a9ba",
    "cli_version": "1.0.98",
    "haiku_5_5_C4_microvm": {
      "wall_s": 278.8,
      "api_s": 250.5,
      "rounds": 14,
      "ai_credits": 5.13,
      "hidden_tests": "294/296 (2 test_parse_errors misses -> 69.61/70)",
      "total_score": 99.61
    },
    "gemini_4_argon_C3_microdb": {
      "wall_s": 1007.4,
      "api_s": 983.9,
      "rounds": 29,
      "ai_credits": 98.58,
      "cache_write_price_per_m": 0.0,
      "hidden_tests": "377/377 (58/58 + 12/12 self_test = 70/70)",
      "total_score": 96.0
    }
  }
}
```

`↓ 对比 SKY-001 分层零件树并行展开 + Matryoshka 双通道扩散构造（S=100 步/零件，W=128 并行 Worker）`

```xml
<sky_001_execution_graph steps_per_part="100" parallel_workers="128">
  Stage 1 (Hierarchical Composer): Coarse 3D DiT -> Parallel Tree Split (depth D) -> Leaf Refiner DiT
    Jaguar E-Type: L=103 leaves, N=139 nodes (36 splits), D=5
    Flat chain:   (N - L) + L * S = 36 + 103 * 100 = 10,336 sequential steps
    Tree rollout: D + ceil(L / W) * S = 5 + 1 * 100 = 105 sequential steps (98.44x shorter!)
  Stage 2 (Construction World Model):
    Pass 1: Roll out intermediate 3D solid states + 2D inverse sketches in leading Matryoshka latents
    Pass 2: Parallel full-resolution Refiner restores sharp edges, corners & vertices
</sky_001_execution_graph>
<answer>
```

> **底层机制 Callout**：为什么 `Haiku 5.5` 生成了 `45.3 万` 输出 Token 仅花费 `$0.33`，而 `Gemini 4 Argon` 生成 `11.7 万` Token 花费 `$2.82`？在 `C3-microdb` 中，`Haiku 5.5` 在 24 轮迭代中输出了 `263,769` Token，但因输出单价仅 `$0.50/M`、缓存读取仅 `$0.01/M`，单题仅耗费 `16.93` credits（`$0.17`）；`Argon` 输出单价为 `$10.00/M`、输入 `$2.00/M`，但凭借 `$0.00/M` 的 `cache_write` 免费写入机制，在 105 万上下文窗口下将 11 题总账单稳定在 `$2.82`。

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`)

### 跨代跃迁稳定性与跨模态敏感度（多轮 CLI 编程 vs 单次 3D CAD 脚本）

对比增补 5 新模型与其前代基线在 11 道编程题上的跃升，以及 6 个重叠模型家族在“无工具单次 3D CAD 生成”与“多轮 CLI 编程”之间的表现反转：

| 对比维度 / 模型家族 | 基线 / 单次 CAD | 演进后 / 多轮 CLI | 变化幅度 (PTS) |
|---|---:|---:|---:|
| **`Haiku 5.5` · 跨代演进（对比 `Haiku 4.5` 11 题均分与复杂题）**<br>复杂题均分 `89.64% -> 99.22%`（`+9.58` pts）；隐藏断言 `1,239 -> 1,308/1,310`；成本 `$3.93 -> $0.33`（`-91.6%`） | `94.0%` | `99.2%` | `+5.2` |
| **`Gemini 4 Argon` · 跨代演进（对比 `Gemini 3.8 Flash` 11 题均分）**<br>隐藏断言 `1,276/1,310`（`97.4%`）$\rightarrow$ `1,310/1,310`（`100.0%`）；总轮次 `277 -> 106`（`-61.7%`） | `98.0%` | `98.6%` | `+0.6` |
| **`Grok 4.7` · 模态反转（SKY-001 单次 CAD IoU vs Copilot CLI 多轮编程）**<br>CAD 基准：`0.0%` IoU（`1,250s` 超时无输出）$\rightarrow$ CLI 编程：`99.21%`（19 模型第 5） | `0.0%` | `99.2%` | `+99.2` |
| **`Kimi K3` · 模态反转（SKY-001 单次 CAD IoU vs Copilot CLI 多轮编程）**<br>CAD 基准：`9.5%` IoU（`439s`，`$0.13`）$\rightarrow$ CLI 编程：`98.68%`（`1,305/1,310` 隐藏通过） | `9.5%` | `98.7%` | `+89.2` |
| **`GPT-6 Astra` · 模态对比（SKY-001 单次 CAD IoU vs Copilot CLI 多轮编程）**<br>CAD 基准：`79.1%` IoU（仅落后 SKY-001 `0.6` pt）$\rightarrow$ CLI 编程：`98.82%`（复杂题 `99.75%` 全榜第 1） | `79.1%` | `98.8%` | `+19.7` |
| **`Opus 5.5` · 模态对比（SKY-001 着陆页 CAD IoU vs Copilot CLI 多轮编程）**<br>CAD 着陆页：`69.4%` IoU（博客包未展示）$\rightarrow$ CLI 编程：`99.68%`（全榜第 2，`1,310/1,310`） | `69.4%` | `99.7%` | `+30.3` |
| **`Gemini 4 / Argon` · 模态对比（SKY-001 博客 CAD IoU vs Copilot CLI 多轮编程）**<br>CAD 博客包：`76.9%` IoU（着陆页未展示）$\rightarrow$ CLI 编程：`98.59%`（`1,310/1,310` 隐藏满分） | `76.9%` | `98.6%` | `+21.7` |

> **鲁棒性 Callout**：`Grok 4.7`（`0.0% -> 99.21%`）与 `Kimi K3`（`9.5% -> 98.68%`）的极端反差证明：**通用前沿 LLM 在 3D 工程任务上的溃败并非因为缺乏代码生成能力，而是因为被强制在无几何求解器回传、无 3D 渲染观察的单次请求（One-Shot）中盲写 100 步空间构造代码**。一旦进入具备 `pytest` 与终端反馈的多轮 CLI 闭环，同款模型立即恢复 `98.6%+` 的工程准确率。

---

## Card 6 (`6 / 7` · `LATENCY`)

### Top 8 主力模型 11 题纯 API 推理耗时 vs 总 Wall 耗时（秒）

蓝条（HTML 卡片 `Batched` 槽位）表示 11 题累计**纯 API 推理耗时**（`task_inference_seconds`）；灰条（`One by one*` 槽位）表示 11 题累计**端到端总 Wall 耗时**（`task_wall_seconds`，含本地测试与工具执行）。

| 序号与模型（`11` 题串行累计，`repeat=1`） | 纯 API 推理耗时（蓝条） | 端到端总 Wall 耗时（灰条） | 工具与本地测试开销 | API 轮次 | 总成本 |
|---|---:|---:|---:|---:|---:|
| **1. `Sonnet 5.5`**（`99.00` 分） | **`995 s`（`16.6m`）** | **`1,301 s`（`21.7m`）** | `306 s`（`23.5%`） | `65` | `$2.89` |
| **2. `HydraFusion`**（`98.45` 分） | **`1,034 s`（`17.2m`）** | **`1,444 s`（`24.1m`）** | `410 s`（`28.4%`） | `85` | `$3.58` |
| **3. `GPT-6.1 Sol`**（`98.86` 分） | **`1,348 s`（`22.5m`）** | **`1,645 s`（`27.4m`）** | `297 s`（`18.1%`） | `60` | `$1.71` |
| **4. `Opus 5.5`**（`99.68` 分） | **`1,570 s`（`26.2m`）** | **`1,909 s`（`31.8m`）** | `339 s`（`17.8%`） | `92` | `$5.84` |
| **5. `GPT-6 Astra`**（`98.82` 分） | **`1,617 s`（`27.0m`）** | **`1,960 s`（`32.7m`）** | `343 s`（`17.5%`） | `62` | `$9.91` |
| **6. `Haiku 5.5 [NEW]`**（`99.24` 分） | **`1,852 s`（`30.9m`）** | **`2,104 s`（`35.1m`）** | `252 s`（`12.0%`） | `94` | `$0.33` |
| **7. `Gemini 4 Argon [NEW]`**（`98.59` 分） | **`2,512 s`（`41.9m`）** | **`2,710 s`（`45.2m`）** | `198 s`（`7.3%`） | `106` | `$2.82` |
| **8. `Fable 5.1`**（`99.77` 分） | **`2,210 s`（`36.8m`）** | **`3,355 s`（`55.9m`）** | `1,145 s`（`34.1%`） | `142` | `$14.45` |

> **延迟剖析 Callout**：`Haiku 5.5` 在简单题 `A1–A5` 上仅耗时 **`141.5s`（平均 `28.3s/题`），为全部 19 个模型中第 1 快**；其 11 题总耗时（`2,104s`）有 **`53.0%`（`1,116s`）集中在单题 `C3-microdb`**（在该题生成了 `26.4 万` 输出 Token）。而在 3D CAD 赛道中，`SKY-001` 通过两阶段并行将单件 100 步构造时间从 `GPT-6 Astra` 的 `199s` 压缩至 **`3.9s`（快 `51.0x`）**，将 BIM 平面图构造从 `144.6s` 压缩至 **`1.22s`（快 `118.5x`）**。

---

## Card 7 (`7 / 7` · `MY TAKE`)

### 生产选型指南：`Haiku 5.5`、`Gemini 4 Argon` 与 `SKY-001` 的适用边界

| ✅ 推荐使用场景（Good fit） | ⛔ 不适用或需谨慎场景（Not for） |
|---|---|
| • **`Claude Haiku 5.5`（`$0.33`，`99.24` 分）**：高频日常开发、原子/中等复杂度模块实现、以及挂载了单元测试门禁的 CI 自动修复首选（性价比之王）<br>• **`Gemini 4 Argon`（`$2.82`，`1,310/1,310` 隐藏通过）**：超长上下文（`1.05M`）多文件重构与跨模块分析，利用 `$0/M` `cache_write` 消除长提示预热成本<br>• **`Sonnet 5.5`（`$2.89`，`21.7m`）与 `GPT-6.1 Sol`（`$1.71`，`60` 轮）**：隐藏测试 `100%` 全过、低轮次高确定性的无人值守主力 Agent<br>• **`SKY-001` 分层世界模型架构**：粗粒度到细粒度的 3D 工业概念探索、多部件装配层级拆解、以及可视化的构造步骤规划 | • **将 `SKY-001` 当前输出直接等同于可加工的参数化 CAD 特征树（STEP/B-Rep）**：官方博客明确说明“将草图序列转化为带可编辑特征树的可执行操作”仍属未来路线图<br>• **用无工具单次盲写脚本评估通用 LLM 的 3D 工程能力**：脱离几何内核反馈与多视角渲染闭环的 One-Shot 评测会严重低估 Agent 形态的潜力<br>• **在无语法/边界测试守卫下直接用 `Haiku 5.5` 裸跑复杂解释器/虚拟机**：需防范类似 `C4-microvm` 中 `2/296` 的空块语法错误漏检<br>• **过度解读 `< 1.0` 分的单次运行（`repeat=1`）名次微差**：跨 CLI 版本（`1.0.84-3..1.0.98`）与主观质量评分存在固有波动 |

> **底部就绪度与溯源声明（Readiness & Provenance）**
> - **数据溯源状态**：`anonymized_reported`（`independently_reproduced=false`）+ 本地离线验证器套件（`simulator/sky001_and_19model_verifier.py`，`6/6` 单元测试通过）。
> - **上游证据锚点**：[`satomic/copilot-benchmark@a1913835`](https://github.com/satomic/copilot-benchmark/commit/a191383571a13143685fd6f7787512c4e281a9ba) · `skyfall.ai/assets/index-D5BqB7X_.js` · `skyfall.ai/assets/article-D6mnIEDb.js` · `benchmark-harness-engineering` 7-Card Visual Deck v1。
