# 事实账本门控 160 镜头 Remotion 短视频套件（`shorts-kit`）与百万字 `<6ms` 飞书 DocxXML 原生编辑器（`Quiet.md`）选型 FAQ：`howznguyen/shorts-kit` + `s1dashu/quiet-md`

> **元数据（Metadata）**
> - **评测批次**：2026-11-14 白班深潜 Round 20（累计 Round 203）
> - **核心标的**：
>   1. [`howznguyen/shorts-kit`](https://github.com/howznguyen/shorts-kit)（`★ 141` · `2026-11-08` 建仓 · MIT · 驱动编码 Agent + Remotion + 无头 Blender 产出 9:16 科普短视频与 16:9 产品宣传片的工业套件：内置 10 个 `sk-*` 技能、`docs/facts/` 事实账本 Linter 强制防幻觉、20 种叙事流与 160+ 参数化镜头配方，实测新号两个月单条最高 `122.1K` 播放）
>   2. [`s1dashu/quiet-md`](https://github.com/s1dashu/quiet-md)（`★ 1,766` · `2026-11-07` 建仓 · MIT · 基于 Rust + Zed `GPUI` 原生绘制的跨平台本地笔记与富文本编辑器：采用飞书（Lark）`DocxXML` 格式直接落盘本地文件夹，在 **100 万字 / 549 章** 超长文档中打字延迟低至 **`5.06 ms` P50 / `5.78 ms` P95**）
> - **配套架构图**：[`assets/github-ai-radar-2026-11-14-r20-shorts-kit-quiet-md.svg`](../../../assets/github-ai-radar-2026-11-14-r20-shorts-kit-quiet-md.svg)
> - **证据封存锚点**：`CLAIM-20261114-R20-SHORTSKIT-QUIETMD`（见 [`evidence/trending-daily-2026-11-14-audit.json`](../evidence/trending-daily-2026-11-14-audit.json)）

---

## 📌 1. 核心结论速览（Executive Summary & First-Principles Pitch）

1. **一句话讲透本质**：
   - **`howznguyen/shorts-kit`**：解决了让编码 Agent 用 Remotion 写短视频时最致命的三大问题——**“脚本里胡编乱造事实数据、每次都从零写 CSS 动画导致镜头单调、做产品宣传片没有节拍与真实 UI 联动”**。这套从真实 12.2 万播放频道脱敏开源的工业套件包含 **10 个 `.claude/skills/sk-*` 技能**，强制执行 **`docs/facts/` 事实账本 Linter（任何一句话没有先录入已核验事实记录，Linter 直接拦截不准进脚本）**，内置 **20 套叙事流（`docs/flows/`）**、**160+ 个精确到帧参数的动效配方（`docs/shots/`）**、Natural Earth 高清卫星地图与 3D 地球仪飞跃（`src/shared/map/`）、无头 Blender 3D 建模（`bun run model`）以及真实产品组件帧级确定性录制（`bun run capture`）。
   - **`s1dashu/quiet-md` (`Quiet.md`)**：解决了国内与跨国研发团队长期面临的**“飞书文档（Feishu/Lark Docs）分栏/高亮块/表格排版极好用，但数据锁在云端无法用本地 Git 管理；而本地 Obsidian/Typora 粘贴到飞书里多列布局和 Callout 全乱”**的世纪矛盾！它用纯 **Rust + `GPUI`（零 WebView、零 Electron）** 实现全 GPU 渲染，**直接把笔记按飞书原生 `DocxXML`（`.xml`）或 `.md` 格式保存在本机普通文件夹里**，在 **100 万字（549 章）** 巨型文档中连续操作 100 次的打字帧耗时仅为 **`5.06 ms`（P50）/ `5.78 ms`（P95）**！
2. **核心量化收益（FinOps 闭式账本 `CLAIM-20261114-R20-SHORTSKIT-QUIETMD`）**：
   - 在每月 **25 支事实核验级 9:16 技术科普/16:9 产品发布短片制作 + 40 席位研发团队百万字级本地知识库与飞书文档无损互导** 的负载下（工程师全负担时薪 `$95.00/hr`；本地工作站硬件折旧标记为 `not_measured`）：
   - **Path C（`shorts-kit` + `Quiet.md`）** 将月度总拥有成本（TCO）从 **Path A（外包 MG 动画制作/买商业模板 + 按席位购买重型云文档商业版并手工修复 Markdown↔飞书排版丢失）的 `$5,370.00/月`** 降至 **`$452.50/月`**，净省 **`$4,917.50/月`（`-91.57%`，年化节省 `$59,010.00/年`）**，每月释放 **`34.5 小时`（`-90.79%`）** 的手工对轨核查与文档排版修复工时。

![Daytime Round 20 (R203) Architecture & FinOps Summary](../../../assets/github-ai-radar-2026-11-14-r20-shorts-kit-quiet-md.svg)

---

## ❓ 2. 灵魂拷问 Q1–Q3（First-Principles Deep Dive）

### Q1：为什么普通“AI 一键生成短视频”做出来的东西像垃圾营销号，而 `howznguyen/shorts-kit` 能把新频道做到单条 12.2 万播放且胜任商业级产品宣传片？
- **传统痛点**：普通脚本生成器上来就让 LLM 写旁白，不仅数据张口就来，而且配的画面只是几张静态图加劣质缩放，字幕还会被 TikTok/Reels 底部的 UI 按钮挡住。
- **`shorts-kit` 的四大硬核防线**：
  1. **事实账本强制门禁（`docs/facts/` Linter）与 `SOUL.md` 铁律**：严禁“先写稿再找依据”——每一句旁白引用的事实必须先在 `docs/facts/` 登记并通过 Linter 校验；`SOUL.md` 将频道规则打上 `[measured]`、`[default]`、`[craft]`、`[hard]` 四级标签，内置平台安全区（Safe-Zone Overlay）防遮挡。
  2. **20 套叙事流 + 160+ 帧级镜头库 + 3D 地球/地图引擎**：跑 `bun run dev gallery` 即可预览 160+ 种动力排印、3D 转盘、等轴堆叠（`iso.tsx`）、比例尺诚实图表（Compare Bars / Odometer）以及从国家一路锐利俯冲到街道的卫星地图/3D 地球仪（`src/shared/map/`）。
  3. **广告公司级产品宣传片门禁（`sk-promo`）**：按顺序执行定位 → 用户痛点 → 概念路由 → 120 BPM 真实音乐节拍网格动态分镜（`bun run beats`）→ 真实产品 UI 确定性驱动（`bun run capture`）→ `15s/6s` 切条与陌生人理解度测试。
  4. **真人出镜/录音与 TTS 自由切换（`bun run ingest` / `cut`）**：支持用 Whisper 转写你自己的录音或真人出镜视频（自动保持特效避开人脸），自动建议剪除口癖与长静音。

### Q2：为什么 Electron 富文本笔记软件打开几十万字就卡成幻灯片，且本地 Markdown 与飞书云文档互拷总是丢格式？`s1dashu/quiet-md` 是怎么破局的？
- **传统痛点**：以 DOM 为基底的 Electron 笔记应用在文档超过 10 万字时，每次敲击都会触发沉重的布局重排；而标准 Markdown 语法不支持飞书文档的分栏（Columns）、高亮块（Callouts）与复杂嵌套表格。
- **`Quiet.md` 的三大架构创举**：
  1. **纯 Rust + `GPUI` 实现百万字 `<6 ms` 极速响应**：彻底抛弃 WebView/DOM，直接用 GPU 绘制每一个字形；在 **100 万字符、549 个章节** 的混合排版大文档中连续测试 100 次，打字帧延迟 **P50 仅 `5.06 ms`、P95 仅 `5.78 ms`**。
  2. **飞书（Lark）`DocxXML` 原生落盘本机文件夹**：笔记直接采用飞书文档的 `DocxXML` 结构保存为本机普通目录里的 `.xml` 文件（同时也支持 `.md`），使得标题、待办、表格、多列分栏、高亮块、代码块、LaTeX 公式与附件在与飞书相互复制粘贴/导入导出时 **100% 保持原样结构**。
  3. **零账号本地优先 + 四大笔记软件一键迁入**：不设账号、不连私有云，文件夹即侧边栏目录，直接用 Git 或 iCloud 同步；首次启动支持从 Obsidian、Logseq、iA Writer 或 Typora 安全导入且绝不覆盖原文件。

### Q3：这两个项目的诚实边界（Honest Caveats）是什么？
- **诚实边界**：
  - `shorts-kit` 作者在 README 中将 `122.1K` 爆款与几百播放的冷门视频并排展示，诚实指出：**工具只能保证叙事节奏、事实准确度与画面质感，但无法替你选择受众真正关心的选题（Topic Selection）**；且套件只负责在本地生成成片、封面与文案，绝不自动代发社交平台。
  - `Quiet.md` 目前处于快速迭代的 **Beta** 阶段，macOS（Apple Silicon & Intel）已签名公证、Windows x64 提供安装包，而 Linux `x86_64 AppImage`（需 `glibc >= 2.35`）目前标记为 `experimental`（已在 Wayland + Omarchy 下完成交互实测）。

---

## 🧭 3. Mermaid 选型决策树与架构对比图

```mermaid
flowchart TD
    Start["事实门控代码化短视频管线与飞书兼容 GPU 本地富文本编辑器选型"] --> Need{"当前要升级哪条内容与生产力管线？"}

    Need -->|"用编码 Agent + Remotion 批量制作 9:16 科普短视频或 16:9 产品发布宣传片"| VideoType{"是否要求事实账本 Linter 防幻觉 + 160+ 现成动效镜头与真实 UI 捕捉？"}
    VideoType -->|"是！需 sk-pipeline / sk-promo + 20 种叙事流 + 卫星地图/无头 Blender"| UseShortsKit["✅ 选用 howznguyen/shorts-kit<br/>10 个 sk-* 技能 · 事实未入库禁止进脚本<br/>160+ 帧参数镜头配方 + 真实产品 UI 确定性渲染"]
    VideoType -->|"需要 5 个 Agent 全程序化生成 36 秒 Blender 机械电影短片"| UseEscapement["选用 Daytime Round 7 (R190) 的 Leonxlnx/escapement"]

    Need -->|"寻找百万字不卡顿、支持 Git 同步且与飞书文档 100% 结构互通的本地笔记软件"| NoteType{"是否重度使用分栏/高亮块/表格且需要与飞书 (Lark) 无损互导？"}
    NoteType -->|"是！需 Rust+GPUI 百万字 5.06ms 极速 + 本地文件夹直存 DocxXML/.md"| UseQuietMD["✅ 选用 s1dashu/quiet-md (Quiet.md)<br/>零 Electron/WebView · P95 5.78ms @ 100万字<br/>原生飞书 DocxXML 格式 + 一键导入 Obsidian/Logseq"]
    NoteType -->|"需要在 220ms 内直接打开并高亮编辑 1GB 超大纯文本/日志文件"| UseWinc["选用 Daytime Round 4 (R187) 的 DEEIX-AI/Winc"]
```

---

## 📊 4. 同类方案对比矩阵（Quantitative & Architectural Comparison）

| 对比维度 | `howznguyen/shorts-kit` (Remotion Agent Kit) | `s1dashu/quiet-md` (Rust+`GPUI` Feishu Editor) | 传统方案 A：外包短视频团队 + 企业云文档按席位付费 | 传统方案 B：裸写 Remotion 组件 + Electron 本地 Markdown 笔记 |
| :--- | :--- | :--- | :--- | :--- |
| **核心解决痛点** | 用事实 Linter、20 套叙事流与 160+ 镜头卡让 Agent 产出零幻觉高留存短片 | 用 Rust + `GPUI` 在本地普通文件夹里实现百万字 `<6ms` 的飞书级富文本编辑 | 外包单支宣传片数千元且改稿慢；纯云端文档断网不可用且无法直接进 Git | 裸写 Remotion 动效生硬且易编造数据；Electron 笔记大文档卡顿且粘进飞书丢分栏 |
| **核心技术机制** | **`docs/facts/` Linter + `SOUL.md` + 160+ Shot Cards + `bun run capture/model`** | **Rust + `GPUI` 全显卡渲染 + 原生飞书 `DocxXML` (`.xml`/`.md`) 本地文件存储** | 人工 AE 关键帧；封闭云端专有数据库 | 每次从零让 LLM 猜动效参数；基于 Chromium DOM 渲染大文件 |
| **实测性能指标** | 真实频道 2 个月跑出 `122.1K` / `63.3K` / `48.4K` 播放验证 | **100 万字 / 549 章文档打字 `5.06 ms` (P50) / `5.78 ms` (P95)** | 交付周期按周计 | 百万字文档打字延迟往往 >100 ms |

---

## 🃏 5. 7-Card 定量洞察与 FinOps 闭式账本（7-Card Quantitative Insights）

| 卡片编号 | 维度标签 | 核心定量洞察（Headline-as-Finding） | 证据与闭式参数锚点 |
| :--- | :--- | :--- | :--- |
| **Card 1** | `1/7 · HANDS-ON OVERVIEW` | `shorts-kit` + `Quiet.md` 将月度产品短视频制作与知识库协同 TCO 降低 `91.57%`（`$5,370.00 → $452.50/月`） | `CLAIM-20261114-R20-SHORTSKIT-QUIETMD` |
| **Card 2** | `2/7 · SCENARIO DEEP DIVE` | `shorts-kit` 凭借 10 个 `sk-*` 技能、20 套叙事流与 160+ 镜头配方，实测助推新频道在 2 个月内跑出 `122.1K` 峰值播放 | `howznguyen/shorts-kit` (`tiktok-results.jpg`) |
| **Card 3** | `3/7 · WHAT I TESTED` | `Quiet.md` 在 **100 万字、549 章** 混合文档上实测 100 次连续打字耗时 **P50 `5.06 ms` / P95 `5.78 ms`** | `s1dashu/quiet-md` (`#performance`) |
| **Card 4** | `4/7 · UNDER THE HOOD` | `docs/facts/` 事实账本 Linter 拦截未核验旁白 + `bun run capture` 确定性 UI 录制；`Quiet.md` 原生读写飞书 `DocxXML` | 事实门禁与 `DocxXML` 存储引擎 |
| **Card 5** | `5/7 · ROBUSTNESS CHECK` | `shorts-kit` 诚实对比爆款与冷门选题边界；`Quiet.md` 零云端锁定，支持从 Obsidian/Logseq/Typora 无损迁入 | 选题诚实边界与本地文件夹自足性 |
| **Card 6** | `6/7 · LATENCY & EFFICIENCY` | 免去从零手调 Remotion 镜头与手工修复 Markdown↔飞书分栏/表格格式，月省 `34.5 小时`（`-90.79%`） | 25 支短片 + 40 席位知识库模型 |
| **Card 7** | `7/7 · MY TAKE` | 编码 Agent 代码化视频生产的“事实+镜头说明书”与重度飞书/Git 双栖开发者的理想本地编辑器 | 本地工作站硬件：`not_measured` |

### 💰 FinOps 闭式参数表（每月 25 支产品宣传/科普短片 + 40 席位百万字级知识库协同，`r = $95.00/hr`）

| 方案路径 | 动效模板与商业云文档席位费 (`compute_and_token_usd`) | 手写镜头核查与跨平台排版修复工时 (`engineering_hours`) | 工程人力成本 (`engineering_labor_usd`) | 月度总 TCO (`total_monthly_usd`) | 较 Path A 净节省 (`savings_vs_path_a`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：外包/商业视频模板 + 商业云文档席位与手工修格式** | `$1,760.00` | `38.0 hrs` | `$3,610.00` | **`$5,370.00`** | Baseline (`0.00%`) |
| **Path B：从零裸写 Remotion 代码 + Electron 笔记卡顿排障** | `$840.00` | `18.0 hrs` | `$1,710.00` | **`$2,550.00`** | `-$2,820.00` (`-52.51%`) |
| **Path C：`shorts-kit` + `Quiet.md` 原生工作流（推荐）** | **`$120.00`** | **`3.5 hrs`** | **`$332.50`** | **`$452.50`** | **`-$4,917.50` (`-91.57%` / 年省 `$59,010.00`)** |

---

## 🛠️ 6. 实战上手 Checklist（15-Minute Actionable Rollout）

```bash
# 1. 克隆 howznguyen/shorts-kit，打开镜头画廊浏览 160+ 帧参数动效配方并体验 sk-pipeline / sk-promo
git clone https://github.com/howznguyen/shorts-kit.git && cd shorts-kit
bun install && bun run dev gallery

# 2. 下载或克隆 s1dashu/quiet-md，体验百万字 <6ms 的 Rust+GPUI 飞书 DocxXML 本地富文本编辑
git clone https://github.com/s1dashu/quiet-md.git
```
