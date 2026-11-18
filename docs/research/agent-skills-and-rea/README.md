# Agent Skills 工程化四级光谱（L1–L4）、门控架构与 AST 逆向引擎 (`morluto/rea`) 深度研究

> 🌐 **Language / 语言切换**: **[🇨🇳 中文版 (README.zh-CN.md)](./README.zh-CN.md)** | **[🇬🇧 English (README.en.md)](./README.en.md)**

## 架构师执行摘要（SA Executive Summary）

企业在规模化构建 Claude Code / GitHub Copilot 自定义技能库（`SKILL.md`）时，最常见的反模式是将海量规则塞入单一提示词，导致上下文注意力稀释与输出质量失控。本专题从 **Enterprise Cloud & AI Solution Architect** 视角，提出并实证拆解了 **Agent Skill 工程化四级演进光谱（L1 → L4）**：

1. **L2 · 声明式 SOP 与 Critic 子智能体门控（Ryan Doser Skills 体系）**：拆解 8 大垂直领域 60+ Skills 的渐进式披露（Progressive Disclosure）契约、`anti-slop.md` 反套话确定性规则与 **4-Agent Critic Gatekeeper** 验收机制，可直接迁移至企业架构设计文档（SAD/ADR）与招投标方案自动审校管线。
2. **L3 · 声明式规范 + 零依赖确定性校验引擎（`wheresryan22/anatomy` 模式）**：剖析如何通过轻量级纯代码校验器（`15.9K LOC` ES Module + `audit.mjs` 三维光线投射无冲突验证）接管大模型不擅长的精确几何/拓扑约束，实现生成产物的确定性门禁（`0 collision / 0 broken invariants`）。
3. **L4 · AST 语义解析与密码学证据链 MCP 引擎（`morluto/rea` v6.4.0）**：基于四层 DDD 架构与 64 项 CLI/MCP 工具链，对混淆生产前端包（`1.28 MB`）执行惰性 AST 语义还原与 `ev_<sha256>` 密码学证据封存，适用于**企业遗留系统现代化重构（Legacy Modernization）**与前端资产审计。

---

## 一、 🌐 在线交互式 H5 工作台（GitHub Pages）

| 交互式交付物 | 架构定位 | 公开访问 URL (GitHub Pages) | 仓库源码入口 |
|---|---|---|---|
| **🏠 专题统一导航门户 (Showcase Portal)** | L1–L4 技能工程化总览入口 | **[👉 打开在线门户](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/)** | [`index.html`](index.html) |
| **📊 Ryan Doser Skill 架构与门控可视化报告** | L2 声明式 SOP + 4-Agent Critic 门控 | **[👉 打开可视化报告 H5](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/h5/ryan-doser-skills-report/)** | [`h5/ryan-doser-skills-report/index.html`](h5/ryan-doser-skills-report/index.html) |
| **🔍 REA AST 语义还原与运行时热补丁工作台** | L4 AST 逆向引擎 + `ev_<sha256>` 证据台账 | **[👉 打开 AST 还原实验台 H5](https://turbo998.github.io/ai-research-public/docs/research/agent-skills-and-rea/h5/rea-scrap-swarm-clone/)** | [`h5/rea-scrap-swarm-clone/index.html`](h5/rea-scrap-swarm-clone/index.html) |

---

## 二、 📐 高清矢量架构图（SVG Visual Atlas）

- [图 1：Ryan Doser 8 大垂直领域 Skills 矩阵与 4-Agent 质量门控架构图](assets/01-ryan-doser-8category-skill-architecture.svg)
- [图 2：Agent Skill 价值封装与 6 阶产品化商业飞轮图](assets/02-ryan-doser-6tier-monetization-funnel.svg)
- [图 3：AI Agent Skill 工程化演进四级光谱 (L1 裸提示词 → L2 SOP 门控 → L3 确定性校验器 → L4 AST/MCP 引擎)](assets/03-agent-skill-l1-to-l4-depth-spectrum.svg)

---

## 三、 深度研究报告与密码学证据链

| 文档 / 数据资产 | 架构维度 | SA 核心收获 |
|---|---|---|
| [`findings/01-morluto-rea-architecture.md`](findings/01-morluto-rea-architecture.md) | **L4 · AST 逆向与 MCP 引擎** | 解析 `rea@6.4.0` 四层 DDD 架构、64 项 CLI/MCP 能力、惰性 AST 语义分析器，以及生产级混淆 JS 包（`1.28 MB`）17 模块结构化还原方法论 |
| [`findings/02-ryan-doser-skill-business.md`](findings/02-ryan-doser-skill-business.md) | **L2 · 声明式门控与商业闭环** | 拆解 60+ Skills 输入/输出契约、`anti-slop.md` 硬规则与 4 层独立 Critic 子智能体门禁，提炼企业级文档与方案生成防幻觉标准 |
| [`findings/03-anatomy-mechanical-skill.md`](findings/03-anatomy-mechanical-skill.md) | **L3 · 确定性几何/拓扑校验器** | 剖析 `SKILL.md` 声明式意图层与 `audit.mjs` 确定性校验器分工模式：如何让代码验证器替代人工肉眼排查拓扑与遮挡错误 |
| [`evidence/rea-evidence-ledger.json`](evidence/rea-evidence-ledger.json) | **可验证密码学证据台账** | 由 `rea@6.4.0` `createEvidence` / `parseEvidence` 生成并校验的 6 条子系统 `ev_<sha256>` 证据链与 AST 统计元数据 |

---

## 四、 关联上游与参考仓库

- **REA 架构研究 Fork**：[`https://github.com/turbo998/rea`](https://github.com/turbo998/rea)（上游 [`morluto/rea`](https://github.com/morluto/rea)，MIT License）
- **确定性 SVG 构建与校验引擎参考**：[`https://github.com/wheresryan22/anatomy`](https://github.com/wheresryan22/anatomy)
- **AST 还原基准测试目标仓库（自有开源项目）**：[`https://github.com/turbo998/scrap-swarm`](https://github.com/turbo998/scrap-swarm)

[返回研究索引](../index.md) · [English Index](../index.en.md) · [返回仓库首页](../../../README.md)
