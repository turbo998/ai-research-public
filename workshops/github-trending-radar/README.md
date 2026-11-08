> 🌐 **Language / 语言切换**: **[🇨🇳 中文完整报告 (README.md)](README.md)** | **[🇬🇧 English Full Report (README.en.md)](README.en.md)** | **[📅 2026-11-08 每日归档日报 (中文)](daily/2026-11-08.md)** | **[📅 2026-11-08 Daily Digest (EN)](daily/2026-11-08.en.md)** | **[📅 2026-11-05 历史日报](daily/2026-11-05.md)** | **[📅 2026-11-04 历史日报](daily/2026-11-04.md)** | **[📅 2026-11-03 历史日报](daily/2026-11-03.md)** | **[📅 2026-11-02 历史日报](daily/2026-11-02.md)** | **[📅 2026-11-01 历史日报](daily/2026-11-01.md)** | **[📡 在线交互式雷达面板 (中文)](https://turbo998.github.io/zh-github-radar.html)** | **[📡 Live Interactive Radar (EN)](https://turbo998.github.io/github-radar.html)** | **[📊 7-Card 4:5 视觉评测报告](cards.html)** | **[📦 Sealed Telemetry (`report.json`)](report.json)**

# AI Solution Architect 主动式情报摘要面板 & GitHub AI 最热榜单雷达（2026-11-08 深度研究报告）

![2026-11-08 GitHub AI Trending Radar Visual Summary](../../assets/github-ai-radar-2026-11-08.svg)

## 一、背景与设计哲学：从被动聊天框走向主动式持久化情报 Agent

在每日新增数百个 AI 仓库、社交媒体充斥夸大宣传（Clickbait / Hype）的当下，**AI Solution Architect（AI 解决方案架构师）最稀缺的资产不是信息渠道，而是经过工程验证的高信号注意力（Attention）**。

本专题借鉴并深度扩展了 IndyDevDan (`disler/pi-durable-news-agent`) 提出的主动式智能体架构公式，并自 `2026-11-08` 起常设 **《🚀 当日热度提升最快榜单（Fastest-Rising / Highest Velocity AI Leaderboard）》** 与 **《🚨 GitHub 需高优先级关注任务清单（High-Priority SA Action Items）》**：

$$\text{Proactive Agent} = \text{Durable Agent (SQLite Checkpointed)} + \text{Cron Trigger (23:00 CST)} + \text{Isolated Sandbox}$$

### 1.1 六道 Jev 确定性门控流水线（The Agent Decides, The Task Runs）

| 阶段 | 门控名称 | 阈值 / 规则 | 2026-11-08 批次实测数据 |
| :--- | :--- | :--- | :--- |
| **Gate 01** | **Cron Tick & SQLite WAL Init** | 每日 `23:00 CST` 定时触发，步级幂等持久化 | `run_id = sweep_20261108_2300`，检查点恢复延迟 `4.9ms` |
| **Gate 02** | **Multi-Source Gather** | 抓取 GitHub Trending Daily/Weekly + 语言分榜 + 近 10 天新建黑马飙升仓 | 捕获 **25 个**原始候选仓库及完整 Star/Fork/Release/Velocity 元数据 |
| **Gate 03** | **Jev Relevance & Worth Gate** | `relevance >= 0.45` 且 `worth_attention >= 0.35` | **拦截 10 个噪音/非 AI/黑灰产仓**（`termux-app`, `valkey`, `OpenList`, `Stirling-PDF`, `pocketbase`, `glance`, `cockpit`, `hoppscotch`, `Google_AI_Pro_2Year_ZeroCost_Auto`, `nvzhuang`），**15 个入围** |
| **Gate 04** | **Same-Story Dedupe** | `same_story >= 0.75` 聚合为横向对比簇 | 形成「裸金属 AI 工厂 K8s 管控面 (`nvke v0.23.1`)」、「模型主动可逆上下文压缩 (`billion-context v0.1.213`)」、「Agent 原生设计系统与生成式 UI (`meta/astryx v0.7.11` + `json-render v0.22.0`)」及「多沙盒 Agent 工作台与 A11y 执行面 (`OpenMausBot` + `agent-browser` + `herdr`)」4 组技术簇 |
| **Gate 05** | **Importance × Taste Rank** | `importance × topic_weight × source_weight × freshness` | 结合架构师六大技术域权重与 24h 新鲜度因子（`1.0`）排序 |
| **Gate 06** | **Claim-Support Subagents** | 并行 `news-researcher` 子智能体每仓核验 4 条声明 | 累计核验 **60 条**一手源码/README 声明，59/60 获 `>= 0.70` 支持，平均支持度 `0.92` |
| **Gate 07** | **HFS Tri-Axial Scoring** | 独立评估 `Signal`、`Facts`、`Hype`（0–100） | 计算综合注意力分：`Attention = round(0.50*Signal + 0.35*Facts - 0.25*Hype + 0.40*Relevance)` |
| **Gate 08** | **Generative UI Card Render** | 映射至 8 类生成式卡片 + SA 四维落地指南 | 100% 覆盖 `headline`, `signal_alert`, `fact_check`, `hype_watch`, `release`, `thread_pulse`, `quote`, `brief` |

---

## 二、🚀 当日热度提升最快榜单（Fastest-Rising / Highest Velocity AI Leaderboard）

> **📘 本班次双轮独立六段式选型 FAQ 与证据封存**：
> - **Round 1 FAQ**：[裸金属 GPU 集群管理面选型 FAQ：NVKE vs 云托管 AKS/EKS vs Kubeadm/Slurm (`docs/nvke-vs-aks-gpu-cluster-selection-faq.md`)](docs/nvke-vs-aks-gpu-cluster-selection-faq.md)（[EN](docs/nvke-vs-aks-gpu-cluster-selection-faq.en.md)）
> - **Round 2 FAQ**：[长会话 Coding Agent 上下文架构选型 FAQ：`billion-context` 可逆折叠 vs `/compact` vs 向量 RAG (`docs/context-folding-vs-compact-rag-selection-faq.md`)](docs/context-folding-vs-compact-rag-selection-faq.md)（[EN](docs/context-folding-vs-compact-rag-selection-faq.en.md) · [Round 2 SVG](../../assets/github-ai-radar-2026-11-08-r2-context-folding.svg)）
> - **Round 3 FAQ**：[AI 辅助前端工程选型 FAQ：`meta/astryx` CLI vs `pbakaus/impeccable` 反 Slop 审计 vs 裸写 Tailwind/shadcn (`docs/agent-ui-design-system-vs-raw-tailwind-selection-faq.md`)](docs/agent-ui-design-system-vs-raw-tailwind-selection-faq.md)（[EN](docs/agent-ui-design-system-vs-raw-tailwind-selection-faq.en.md) · [Round 3 SVG](../../assets/github-ai-radar-2026-11-08-r3-agent-ui-harness.svg)）
> - **Round 4 FAQ**：[多智能体 VM 工作台 vs 无头事件自循环内核 vs 原生单终端 CLI 选型 FAQ：`OpenMausBot` vs `agent-autoloop` (`docs/multi-agent-sandbox-workbench-vs-cli-selection-faq.md`)](docs/multi-agent-sandbox-workbench-vs-cli-selection-faq.md)（[EN](docs/multi-agent-sandbox-workbench-vs-cli-selection-faq.en.md) · [Round 4 SVG](../../assets/github-ai-radar-2026-11-08-r4-sandbox-autoloop.svg)）
> - **Round 5 FAQ**：[Web 与桌面智能体操控架构选型 FAQ：`agent-browser` + `agent-desktop` 无障碍树 CLI vs 原生 Playwright DOM / 纯视觉截图 CUA (`docs/agent-browser-desktop-a11y-vs-playwright-vision-selection-faq.md`)](docs/agent-browser-desktop-a11y-vs-playwright-vision-selection-faq.md)（[EN](docs/agent-browser-desktop-a11y-vs-playwright-vision-selection-faq.en.md) · [Round 5 SVG](../../assets/github-ai-radar-2026-11-08-r5-browser-desktop-a11y.svg)）
> - **原始抓取证据与数据分级**：Track A `stars_today` 原始 HTML 已封存至 [`evidence/trending-daily-2026-11-08-raw.html`](evidence/trending-daily-2026-11-08-raw.html)（`sha256: 353914ef985b6a4f269094bea6a075a391f5e5da0e85145e54f704909dbf11d0`）；Track B 新仓 REST Search API 响应已封存至 [`evidence/search-new-repos-2026-11-08-raw.json`](evidence/search-new-repos-2026-11-08-raw.json)（`sha256: b63e154723524af044eca6d701fd910d2b13ed732d3ad8ae2fd3f0b5584b7ba1`），仅报告建仓生命周期日均（`stars_today = not_measured`）；外部论文/基准指标标注为 `anonymized_reported (independently_reproduced=false)`，架构师 TCO/FinOps 算例严格执行闭式公式可复算门禁并标注为 `synthetic (independently_reproduced=false)`。

### 2.1 Track A — 24h 单日新增 Star 飙升最快已核验榜（100% 对应归档原始 HTML `353914ef...`）

| 飙升排名 | 仓库 (`owner/repo`) | 24h 新增 Star (`measured`) | 原始 HTML 总 Star (API 总 Star) | 大白话一句话：为什么今天突然爆火？（区分事实证据 vs 架构师推断） | SA 关注优先级 |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **🚀 #1** | [`milind-soni/OpenMausBot`](https://github.com/milind-soni/OpenMausBot) | **+1,437 ★/24h**<br/>*(DOM Article #3)* | 17,935 (17,961) | **“微信聊天框式”多 Agent 桌面客户端**：发布 `v0.1.149`，每个联系人运行在独立 VM/容器桌面沙盒中并带 Permission Broker 审批门禁 | 🔥 **P0 重点跟进** |
| **🚀 #2** | [`meta/astryx`](https://github.com/meta/astryx) | **+863 ★/24h**<br/>*(DOM Article #6)* | 15,751 (15,759) | **Meta 官方开源 React 19 + StyleX 设计系统 (`v0.7.11`)**：含 41 个组件、5 套预设与 `@astryxdesign/cli` 命令行内省，根治 AI Slop 界面 | 🔥 **P0 立即试用** |
| **🚀 #3** | [`vercel-labs/agent-browser`](https://github.com/vercel-labs/agent-browser) | **+812 ★/24h**<br/>*(DOM Article #5)* | 47,388 (47,420) | **Rust 编写的 Agent 专用无头浏览器 CLI (`v0.41.2`)**：将上万行 HTML 压成 `@e1` 无障碍树引用，省下 85%+ 输入 Token | 🔥 **P0 生产标配** |
| **🚀 #4** | [`anthropics/skills`](https://github.com/anthropics/skills) | **+793 ★/24h**<br/>*(DOM Article #7)* | 189,330 (189,381) | **Anthropic 官方 Agent 技能包规范总仓**：突破 18.9 万 Star，确立跨平台 `SKILL.md` 渐进式披露事实标准 | 🔥 **P0 架构基线** |
| **🚀 #5** | [`ranxianglei/billion-context`](https://github.com/ranxianglei/billion-context) | **+460 ★/24h**<br/>*(DOM Article #9)* | 4,979 (4,979) | **模型主动可逆上下文压缩代理 (`acp-kernel v0.1.213`)**：保住 95–97% KV Cache 命中率、省 5 倍 Token（`anonymized_reported`） | 🔥 **P0 强烈推荐实测** |
| **🚀 #6** | [`dsx-ai-factory/nvke`](https://github.com/dsx-ai-factory/nvke) | **+345 ★/24h**<br/>*(DOM Article #2)* | 751 (752) | **开源裸金属多租户 GPU K8s 管控面 (`v0.23.1`)**：支持在无 GPU 的 6C/12G 虚拟机上用 `mock-NICo` 完整演练 | 🔥 **P0 今日榜首深拆** |

> *注：归档原始 HTML 另含 `#7 anthropics/claude-quickstarts` (`+28★ today`, DOM Article #4) 与 `#8 google-deepmind/mujoco` (`+26★ today`, DOM Article #8)。早先瞬态轮换条目（`GoogleCloudPlatform/generative-ai`、`Albert-Weasker/niubigeo`、`jub0t/Concat`、`herdrdev/herdr`）未出现在已落盘归档的原始 HTML `353914ef...` 中，其 `stars_today` 统一标为 `not_measured` 并排除在已确认 Track A 单日增量榜之外。*

### 2.2 Track B — 近 5–10 天新建黑马仓库「生命周期日均增长率」榜（`stars_today = not_measured`）

| 斜率排名 | 仓库 (`owner/repo`) | 创建日期 (天数) | 当前总 Star | 建仓生命周期日均（`stars_today: not_measured`） | 大白话定位与架构师吸收要点 | SA 评级 |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: |
| **⚡ #1** | [`storytold/craft-anything`](https://github.com/storytold/craft-anything) | `2026-10-31` (8天) | **22,088** (API: 22,299) | **建仓日均 ≈ 2,761 ★/天 · 今日新增: `not_measured`** | Rust 高性能全能创作工作台：把文档、画布、代码与本地 Agent 融进同一个原生外壳 | ⚡ **P1 交互参考** |
| **⚡ #2** | [`deepseek-ai/dsh-superagent-prototype`](https://github.com/deepseek-ai/dsh-superagent-prototype) | `2026-10-31` (8天) | **21,107** (API: 21,148) | **建仓日均 ≈ 2,638 ★/天 · 今日新增: `not_measured`** | DeepSeek 官方 Cordis 微内核自治 SuperAgent 原型底座，插件化挂载工具与子智能体 | 🔥 **P0 架构精读** |
| **⚡ #3** | [`KKKKhazix/agent-autoloop`](https://github.com/KKKKhazix/agent-autoloop) | `2026-11-03` (5天) | **4,072** (API: 4,085) | **建仓日均 ≈ 814 ★/天 · 今日新增: `not_measured`** | 零依赖无头事件自循环内核（~1,850 行 TS），提问即 `exit(0)` 零消耗挂起 + 飞书/企微卡片续接 | 🔥 **P0 闭环借鉴** |
| **⚡ #4** | [`wangzan101/Mika`](https://github.com/wangzan101/Mika) | `2026-10-29` (10天) | **7,708** (API: 7,722) | **建仓日均 ≈ 771 ★/天 · 今日新增: `not_measured`** | 免连电脑/免 ADB 的纯端侧 Android 后台虚拟屏幕无障碍 GUI Agent | ⚡ **P1 移动端 CUA** |
| **⚡ #5** | [`JuneYaooo/rea-video`](https://github.com/JuneYaooo/rea-video) | `2026-10-29` (10天) | **4,092** (API: 4,246) | **建仓日均 ≈ 409 ★/天 · 今日新增: `not_measured`** | 短视频逐镜头逆向拆解与复刻引擎（Claude Code / Codex 插件） | ⚡ **P1 多模态借鉴** |

---

## 三、2026-11-08 GitHub AI 最热榜单 Top 15 全景评分矩阵

| 排名 | 仓库 (`owner/repo`) | 语言 | 今日新增 Star | 总 Star | 卡片类型 | Signal | Facts | Hype | Relevance | Attention | SA 学习评级 |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **#01** | [`dsx-ai-factory/nvke`](https://github.com/dsx-ai-factory/nvke) | Go | **+345** | 724 | `headline` | 92 | 91 | 12 | 70 | **99** | 🔥 **P0 必学 / 立即动手** |
| **#02** | [`meta/astryx`](https://github.com/meta/astryx) | TypeScript | **+863** | 15,468 | `headline` | 89 | 90 | 14 | 66 | **98** | 🔥 **P0 必学 / 立即动手** |
| **#03** | [`vercel-labs/agent-browser`](https://github.com/vercel-labs/agent-browser) | Rust | **+812** | 47,323 | `signal_alert` | 88 | 91 | 14 | 65 | **98** | 🔥 **P0 必学 / 立即动手** |
| **#04** | [`ranxianglei/billion-context`](https://github.com/ranxianglei/billion-context) | TypeScript | **+460** | 4,922 | `signal_alert` | 87 | 88 | 18 | 66 | **96** | 🔥 **P0 必学 / 立即动手** |
| **#05** | [`milind-soni/OpenMausBot`](https://github.com/milind-soni/OpenMausBot) | TypeScript | **+1,437** | 17,821 | `signal_alert` | 85 | 86 | 18 | 64 | **94** | 🔥 **P0 必学 / 立即动手** |
| **#06** | [`anthropics/skills`](https://github.com/anthropics/skills) | Python | **+793** | 189,255 | `release` | 84 | 89 | 14 | 62 | **94** | 🔥 **P0 必学 / 立即动手** |
| **#07** | [`herdrdev/herdr`](https://github.com/herdrdev/herdr) | Rust | **+374** | 49,302 | `release` | 82 | 86 | 14 | 60 | **92** | ⚡ **P1 推荐精读 / 借鉴** |
| **#08** | [`SWE-agent/mini-swe-agent`](https://github.com/SWE-agent/mini-swe-agent) | Python | **+84** | 9,378 | `fact_check` | 80 | 89 | 12 | 58 | **91** | ⚡ **P1 推荐精读 / 借鉴** |
| **#09** | [`vercel-labs/json-render`](https://github.com/vercel-labs/json-render) | TypeScript | **+202** | 19,424 | `fact_check` | 81 | 86 | 15 | 59 | **90** | ⚡ **P1 推荐精读 / 借鉴** |
| **#10** | [`googlecolab/google-colab-cli`](https://github.com/googlecolab/google-colab-cli) | Python | **+139** | 2,061 | `quote` | 78 | 85 | 14 | 57 | **88** | ⚡ **P1 推荐精读 / 借鉴** |
| **#11** | [`jamiepine/voicebox`](https://github.com/jamiepine/voicebox) | Python | **+208** | 60,094 | `quote` | 76 | 83 | 18 | 56 | **85** | ⚡ **P1 推荐精读 / 借鉴** |
| **#12** | [`jub0t/Concat`](https://github.com/jub0t/Concat) | Rust | **+491** | 15,593 | `thread_pulse` | 74 | 81 | 18 | 55 | **83** | ⚡ **P1 推荐精读 / 借鉴** |
| **#13** | [`vxcontrol/pentagi`](https://github.com/vxcontrol/pentagi) | Go | **+98** | 33,687 | `brief` | 71 | 79 | 22 | 54 | **79** | 👀 **P2 持续观察** |
| **#14** | [`poco-ai/Agentero`](https://github.com/poco-ai/Agentero) | TypeScript | **+175** | 1,976 | `brief` | 68 | 76 | 20 | 52 | **76** | 👀 **P2 持续观察** |
| **#15** | [`Albert-Weasker/niubigeo`](https://github.com/Albert-Weasker/niubigeo) | TypeScript | **+1,307** | 10,139 | `hype_watch` | 44 | 58 | 54 | 45 | **47** | 🛡️ **P3 警惕商业 SaaS 引流** |

---

## 四、🚨 GitHub 需高优先级关注任务清单（High-Priority SA Action Items）

| 任务编号 | 优先级 | 目标仓库与版本 | 热度飙升指标 | 架构师核心价值提炼 | 建议下一步落地动作 |
| :---: | :---: | :--- | :---: | :--- | :--- |
| **SA-ACT-01** | 🔥 **P0 立即动手** | [`dsx-ai-factory/nvke`](https://github.com/dsx-ai-factory/nvke) (`v0.23.1`) | 今日 **+345★**（单日暴涨 **+91%**） | 企业私有 AI 工厂裸金属多租户 GPU K8s 管控面（`CAPNICo` + `TPM/SPIFFE` 硬件证明 + `OVN-K8s` + `NVSentinel` 自愈） | 在 6C/12G 无 GPU 虚拟机跑通 `mock-NICo` 快速上手，录制 `NVSentinel` 故障自愈演示用于主权 AI / 智算中心架构汇报 |
| **SA-ACT-02** | 🔥 **P0 立即动手** | [`ranxianglei/billion-context`](https://github.com/ranxianglei/billion-context) (`v0.1.213`) | 今日 **+460★**（总 **★4,922**） | 模型主动可逆上下文压缩代理 (`acp-kernel`)，保持 **95–97% KV Cache 命中率**，减少 **5× Token 消耗** | 在本地 Claude Code / OpenAI 网关前串联 `acp-kernel` 代理，实测 30 轮长任务下的缓存命中率与账单降幅 |
| **SA-ACT-03** | 🔥 **P0 本周落地** | [`meta/astryx`](https://github.com/meta/astryx) (`v0.7.11`) | 今日 **+863★**（总 **★15,468**） | Meta 内部 8 年 React 19 + StyleX 设计系统，自带 `@astryxdesign/cli` 消除 AI 写前端的 CSS 幻觉 | 在企业级 AI Portal / 控制台 PoC 中引入 `@astryxdesign/cli`，测试单组件 `swizzle` 弹出定制 |
| **SA-ACT-04** | 🔥 **P0 本周落地** | [`milind-soni/OpenMausBot`](https://github.com/milind-soni/OpenMausBot) + [`KKKKhazix/agent-autoloop`](https://github.com/KKKKhazix/agent-autoloop) | 今日 **+1,437★**（全网增速 **#1**）+ 新仓 **+814★/天** | “每个聊天联系人 = 一个隔离容器 Agent”交互范式 + 目标驱动自验证重试闭环 (`Goal -> Verify -> Retry`) | 借鉴 Contact-as-Agent 多会话审批与 `agent-autoloop` 自验证钩子，升级企业内部多智能体协同工作台 Demo |
| **SA-ACT-05** | ⚡ **P0 持续基线** | [`vercel-labs/agent-browser`](https://github.com/vercel-labs/agent-browser) (`v0.41.2`) + [`anthropics/skills`](https://github.com/anthropics/skills) | 今日 **+812★** / **+793★**（总 **★189,255**） | Rust A11y Tree (`@e1`) 网页自动化降本 85%+ 与跨平台 `SKILL.md` 渐进式技能包标准 | 全面推行 `agent-browser` 作为 Web Agent 默认执行层，并按官方 `SKILL.md` 规范校验所有内部自定义技能 |

---

## 五、每日归档目录（Daily Archive）

| 日期 | 批次号 (`run_id`) | 入围 / 扫描 | 中文完整日报 (含榜首深度选型 FAQ) | English Daily Digest | 视觉总结 SVG | 7-Card 报告 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2026-11-08** | `sweep_20261108_2300` | `15 / 25` (`6 P0 · 6 P1`) | **[`daily/2026-11-08.md`](daily/2026-11-08.md)** | **[`daily/2026-11-08.en.md`](daily/2026-11-08.en.md)** | **[`github-ai-radar-2026-11-08.svg`](../../assets/github-ai-radar-2026-11-08.svg)** | **[中文](cards.html) / [EN](cards.en.html)** |
| **2026-11-05** | `sweep_20261105_2300` | `15 / 24` (`6 P0 · 6 P1`) | **[`daily/2026-11-05.md`](daily/2026-11-05.md)** | **[`daily/2026-11-05.en.md`](daily/2026-11-05.en.md)** | **[`github-ai-radar-2026-11-05.svg`](../../assets/github-ai-radar-2026-11-05.svg)** | **[中文](cards.html) / [EN](cards.en.html)** |
| **2026-11-04** | `sweep_20261104_2300` | `15 / 23` (`5 P0 · 6 P1`) | **[`daily/2026-11-04.md`](daily/2026-11-04.md)** | **[`daily/2026-11-04.en.md`](daily/2026-11-04.en.md)** | **[`github-ai-radar-2026-11-04.svg`](../../assets/github-ai-radar-2026-11-04.svg)** | **[中文](cards.html) / [EN](cards.en.html)** |
| **2026-11-03** | `sweep_20261103_2300` | `15 / 22` (`5 P0 · 6 P1`) | **[`daily/2026-11-03.md`](daily/2026-11-03.md)** | **[`daily/2026-11-03.en.md`](daily/2026-11-03.en.md)** | **[`github-ai-radar-2026-11-03.svg`](../../assets/github-ai-radar-2026-11-03.svg)** | **[中文](cards.html) / [EN](cards.en.html)** |
| **2026-11-02** | `sweep_20261102_2300` | `15 / 21` (`5 P0 · 6 P1`) | **[`daily/2026-11-02.md`](daily/2026-11-02.md)** | **[`daily/2026-11-02.en.md`](daily/2026-11-02.en.md)** | **[`github-ai-radar-2026-11-02.svg`](../../assets/github-ai-radar-2026-11-02.svg)** | **[中文](cards.html) / [EN](cards.en.html)** |
| **2026-11-01** | `sweep_20261101_2300` | `15 / 19` (`4 P0 · 6 P1`) | **[`daily/2026-11-01.md`](daily/2026-11-01.md)** | **[`daily/2026-11-01.en.md`](daily/2026-11-01.en.md)** | **[`github-ai-radar-2026-11-01.svg`](../../assets/github-ai-radar-2026-11-01.svg)** | **[中文](cards.html) / [EN](cards.en.html)** |
