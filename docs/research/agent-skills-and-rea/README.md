# Agent 逆向工程 (`morluto/rea`)、机械解剖学 (`anatomy`) 与商业化 Skills 生态研究及互动 H5 套件

本专题收录了针对三大前沿 Agent Skills 与工具链的深度研究报告及 **2 套可离线交互的 H5 演示系统**：

1. **任务一 · 机械解剖学 (`wheresryan22/anatomy`) 互动 H5 演示 (V2.3 整车深度强化版)**：**美嘉欣（MJX）Hyper Go 14303（1/14 全时四驱无刷拉力/漂移遥控车）整车 12 总成机械原理互动解剖台**（涵盖宽体拉力车壳/双层尾翼/车顶四联探照灯排/FIA 防滚架/鲨鱼鳍导流片、CNC 二楼板防倾杆、CNC 转向节 C 座与黄铜主销、双出钛合金排气尾管与前置拖车钩、6 辐轮毂+打孔刹车盘+卡钳、行星差速齿轮、四滚筒测功机、8 套高饱和阳极氧化涂装、6 大动态工况演示与 60Hz 四通道实时示波器，深浅双版本均通过 `kit/audit.mjs` 91 状态 0 穿模审计）。
2. **任务二 · 独立创作者商业化闭环研究**：**Ryan Doser (`@RyanDoserAI`) 的 Claude Code Skills 覆盖范围（8 大类 60+ 技能）、技术深度（`anti-slop.md` 源码级拆解 + 4 子智能体质量门控）与 6 阶价值变现漏斗（$47 → $99 → $199 → $600 咨询 → $100K+ 代运营）**。
3. **任务三 · `morluto/rea` 逆向工程 Demo 与小游戏复刻 (V2.3 全档案热补丁实验台)**：基于已 Fork 的 [`turbo998/rea`](https://github.com/turbo998/rea)（`v6.4.0`），对 **《废土斗机祭 (Scrap Swarm)》** 生产构建包执行静态语义分析与密码学证据生成，并完整复刻 **实战竞技场（含推进残影冲刺、避难所 EMP 磁暴波、浮动暴击伤害跳字） + 五机甲整备库 (5 Units × 4 Poses) + 五章战役剧情与矢量立绘特写横幅 + 6 模块 REA AST 对照与运行时内存热补丁工作台 + 实时脉动 `ev_<sha256>` 证据台账 + 10 音效 Web Audio 双振荡器测试台**。

---

## 目录与交付物导航

### 一、 🌐 已发布公开访问的在线交互式 H5 页面（GitHub Pages，可直接发给外部客户演示）

| 在线演示项目 | 适用任务 | 公开访问 URL (GitHub Pages) | 仓库源码入口 |
|---|---|---|---|
| **🏠 专题总览门户 (Showcase Portal)** | 三大任务统一导航页 | **[👉 立即打开在线总门户](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/)** | [`index.html`](index.html) |
| **🏎️ 美嘉欣 MJX 14303 四驱底盘机械解剖台（深色版）** | 任务 1 (`anatomy` 客户演示) | **[👉 立即打开深色蓝图版 H5](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/h5/mjx-14303-anatomy/)** | [`h5/mjx-14303-anatomy/mjx-14303-chassis.html`](h5/mjx-14303-anatomy/mjx-14303-chassis.html) |
| **☀️ 美嘉欣 MJX 14303 四驱底盘机械解剖台（浅色版）** | 任务 1 (`anatomy` 出版物版) | **[👉 立即打开浅色出版物版 H5](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/h5/mjx-14303-anatomy/mjx-14303-chassis-light.html)** | [`h5/mjx-14303-anatomy/mjx-14303-chassis-light.html`](h5/mjx-14303-anatomy/mjx-14303-chassis-light.html) |
| **📊 Ryan Doser Skill 生态与 6 阶变现可视化报告** | 任务 2 (可视化交互报告 H5) | **[👉 立即打开可视化研究报告 H5](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/h5/ryan-doser-skills-report/)** | [`h5/ryan-doser-skills-report/index.html`](h5/ryan-doser-skills-report/index.html) |
| **🎮 《废土斗机祭 (Scrap Swarm)》REA 逆向复刻可玩版** | 任务 3 (`rea` 1:1 可玩复刻) | **[👉 立即在线试玩复刻版 H5](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/h5/rea-scrap-swarm-clone/)** | [`h5/rea-scrap-swarm-clone/index.html`](h5/rea-scrap-swarm-clone/index.html) |

### 二、 📐 专题配套高清矢量架构图（SVG Visual Atlas）

- [图 1：Ryan Doser 8 大垂直领域 Skills 矩阵与 4-Agent 质量门控架构图](assets/01-ryan-doser-8category-skill-architecture.svg)
- [图 2：Ryan Doser “卖铲子撬动包工程” 6 阶价值变现漏斗与营收结构图](assets/02-ryan-doser-6tier-monetization-funnel.svg)
- [图 3：AI Agent Skill 工程化演进四级光谱 (L1 提示词 → L2 Ryan Doser → L3 `anatomy` → L4 `rea`)](assets/03-agent-skill-l1-to-l4-depth-spectrum.svg)

### 三、 深度研究报告与密码学证据链

| 文档 / 数据资产 | 对应主题 | 核心内容摘要 |
|---|---|---|
| [`findings/01-morluto-rea-architecture.md`](findings/01-morluto-rea-architecture.md) | `morluto/rea` 架构与 H5 逆向实录 | 解析 REA v6.4.0 的四层 DDD 架构、64 项 CLI/MCP 能力、惰性 AST 语义分析器，以及对 `index-BCy1aADK.js`（1.28 MB）的逆向还原全过程 |
| [`findings/02-ryan-doser-skill-business.md`](findings/02-ryan-doser-skill-business.md) | Ryan Doser 技能生态与商业化拆解 | 梳理 8 大模块 60+ Skills 覆盖矩阵、拆解 `anti-slop.md` 真实源码与 4 层 Critic 子智能体门控，对比 L2 声明式 SOP 与 L4 确定性引擎型 Skill，还原 6 阶变现飞轮 |
| [`findings/03-anatomy-mechanical-skill.md`](findings/03-anatomy-mechanical-skill.md) | `wheresryan22/anatomy` 原理与 MJX 14303 建模 | 详解 `iso-kit.mjs` / `lathe.mjs` / `tube.mjs` / `audit.mjs` 引擎机制、MJX 14303 实车参数映射，以及 `8,864` 对空间重叠零冲突的 3D 审计过程 |
| [`evidence/rea-evidence-ledger.json`](evidence/rea-evidence-ledger.json) | REA `ev_<sha256>` 密码学证据台账 | 由 `rea@6.4.0` 的 `createEvidence` / `parseEvidence` 生成并校验的 6 条子系统逆向证据链与 AST/语义统计数据 |
| [`h5/mjx-14303-anatomy/build.mjs`](h5/mjx-14303-anatomy/build.mjs) | MJX 14303 等轴测生成脚本 | 基于 `wheresryan22/anatomy` 编写的参数化构建与光线投射审计源码 |

---

## 三、 关联 GitHub 仓库汇总

- **REA 个人 Fork 仓库**：[`https://github.com/turbo998/rea`](https://github.com/turbo998/rea)（Fork 自 [`morluto/rea`](https://github.com/morluto/rea)）
- **被逆向 H5 游戏线上部署库**：[`https://github.com/turbo998/ai-gaming-lab`](https://github.com/turbo998/ai-gaming-lab)（`public/demos/scrap-swarm/`）
- **被逆向 H5 游戏源码对照库**：[`https://github.com/turbo998/scrap-swarm`](https://github.com/turbo998/scrap-swarm)
- **机械解剖学上游 Skill 库**：[`https://github.com/wheresryan22/anatomy`](https://github.com/wheresryan22/anatomy)
- **Ryan Doser 官方站点矩阵**：[`ryandoser.com`](https://ryandoser.com/) · [`skills.ryandoser.com`](https://skills.ryandoser.com/) · [`engine.ryandoser.com`](https://engine.ryandoser.com/) · [`seo.ryandoser.com`](https://seo.ryandoser.com/)

[返回研究索引](../index.md) · [返回仓库首页](../../../README.md)
