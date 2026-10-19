# Agent 逆向工程 (`morluto/rea`)、机械解剖学 (`anatomy`) 与商业化 Skills 生态研究及互动 H5 套件

本专题收录了针对三大前沿 Agent Skills 与工具链的深度研究报告及 **2 套可离线交互的 H5 演示系统**：

1. **任务一 · 机械解剖学 (`wheresryan22/anatomy`) 互动 H5 演示**：**美嘉欣（MJX）Hyper Go 14303（1/14 全时四驱无刷拉力/漂移遥控车）底盘机械原理互动解剖台**（深色蓝图版 + 浅色印刷版 + 参数化生成源码）。
2. **任务二 · 独立创作者商业化闭环研究**：**Ryan Doser (`@RyanDoserAI`) 的 Claude Code Skills 覆盖范围（8 大类 60+ 技能）、技术深度（`anti-slop.md` 源码级拆解 + 4 子智能体质量门控）与 6 阶价值变现漏斗（$47 → $99 → $199 → $600 咨询 → $100K+ 代运营）**。
3. **任务三 · `morluto/rea` 逆向工程 Demo 与小游戏复刻**：基于已 Fork 的 [`turbo998/rea`](https://github.com/turbo998/rea)（`v6.4.0`），对 [`turbo998/ai-gaming-lab`](https://github.com/turbo998/ai-gaming-lab) 中已发布的 H5 小游戏 **《废土斗机祭 (Scrap Swarm)》** 生产构建包（`assets/index-BCy1aADK.js`，`433,836` 个 AST 节点）执行静态语义分析与密码学证据生成（6 条 `ev_<sha256>` 证据记录），并构建内置实时证据脉冲 HUD 的 **1:1 可玩 H5 复刻版**。

---

## 目录与交付物导航

### 一、 交互式 H5 演示系统（单文件零外部依赖，支持直接打开）

| 演示项目 | 适用任务 | 核心交互特性 | 入口链接 |
|---|---|---|---|
| **美嘉欣 MJX 14303 四驱底盘机械解剖台（深色版）** | 任务 1 (`anatomy` Demo) | 10 大可拆解机械总成、`E` 键弹簧阻尼爆炸视图、`S` 键油压绞牙避震下压、2S(7.4V)/3S(11.1V) 切换、FDR `8.54:1` 转速/车速遥测、阿克曼转向与 G3C 陀螺仪漂移反打仿真 | [`h5/mjx-14303-anatomy/mjx-14303-chassis.html`](h5/mjx-14303-anatomy/mjx-14303-chassis.html) / [`index.html`](h5/mjx-14303-anatomy/index.html) |
| **美嘉欣 MJX 14303 四驱底盘机械解剖台（浅色版）** | 任务 1 (`anatomy` Demo) | 浅色工程出版物配色（`--light`），完整保留全部 10 大总成交互与遥测能力 | [`h5/mjx-14303-anatomy/mjx-14303-chassis-light.html`](h5/mjx-14303-anatomy/mjx-14303-chassis-light.html) |
| **《废土斗机祭 (Scrap Swarm)》REA 6.4.0 逆向复刻可玩版** | 任务 3 (`rea` 逆向复刻 Demo) | 1:1 复刻 Xorshift32 确定性随机数、三把武器（爆铆拳炮/震磁圆阵/雷索连击）、三幕波次、避难所电磁中继站、BOSS「铁冠·赫克托」热能锁暴露 1.65× 暴击及 **右侧实时 `ev_<sha256>` 证据脉冲台账** | [`h5/rea-scrap-swarm-clone/index.html`](h5/rea-scrap-swarm-clone/index.html) |

### 二、 深度研究报告与密码学证据链

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
