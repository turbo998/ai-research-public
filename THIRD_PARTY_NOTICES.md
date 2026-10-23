# 第三方声明

## Agent Forge (FAF v2) vs. Microsoft AGENT-FORGE 研究

- **`customer-success-microsoft/faf-agents` (Agent Forge / FAF v2.0.1)**：固定 commit `a740ad88afa0b054e656207e72205002ca6744f0`，上游根 `LICENSE` 为 MIT License（其中 `docx`、`pptx`、`xlsx`、`pdf` 技能包含源自 Anthropic Claude Code Skills 的许可与归属声明）。本公开库仅保留脱敏后的架构机制分析、量化评分权重公式摘要与元数据（[`docs/research/faf-vs-agent-forge/`](docs/research/faf-vs-agent-forge/README.zh-CN.md)），不复制或再分发上游插件源码、完整提示词正文或任何内部客户材料。
- **[`microsoft/agent-forge`](https://github.com/microsoft/agent-forge/tree/655ff3401d18bd000252907a512a3f674114f708) (`@agent-forge-copilot/cli@0.3.0`)**：固定 commit `655ff3401d18bd000252907a512a3f674114f708`，上游根 `LICENSE` 为 MIT License。本库仅保留原创中英双语对比分析、契约评测统计与已核验 blob 元数据，不重新分发完整 CLI 源代码。

## Omarchy Agent 设计机制研究

- **上游仓库**：[omacom/omarchy](https://github.com/omacom/omarchy/tree/9480d1b6a98156314dbabe6bfef08f39f8b9cd07)（请求入口别名 `basecamp/omarchy`），固定 commit `9480d1b6a98156314dbabe6bfef08f39f8b9cd07`。
- **上游许可证**：固定 [LICENSE](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/LICENSE#L1-L20) 为 MIT 文本，`Copyright (c) David Heinemeier Hansson`。
- **本公开库处理边界**：[本研究](docs/research/omarchy-agent-design/README.md)与[测试报告](docs/research/omarchy-agent-design/test-report.md)不重新分发完整上游源码、技能文件、模板、官网正文或媒体，仅保存原创中文分析、固定 SHA/行号链接、参数/字段契约摘要与已核验来源元数据；不将上游根 MIT 许可证外推至第三方 CLI 二进制、商标、模型或云服务条款。
- **官方对比资料（W1–W7）**：Anthropic 与 GitHub 官方文档各自受其服务与文档条款约束；在线访问日期与产品适用条件记录于 [`docs/research/omarchy-agent-design/evidence.json`](docs/research/omarchy-agent-design/evidence.json)。

## Personal Agents 五产品比较研究

- 相关消费级/企业级 Agent 产品声明、第三方观察与公开 Benchmark 论文（GAIA、OSWorld、τ-bench）的归属与权利边界见 [归属与权利边界](ATTRIBUTION.md) 与 [`docs/research/personal-agents/evidence.json`](docs/research/personal-agents/evidence.json)。

## Agent 逆向工程 (`morluto/rea`)、机械解剖学 (`anatomy`) 与商业化 Skills 研究

- **`morluto/rea`**：上游仓库 [`morluto/rea`](https://github.com/morluto/rea) 采用 MIT 许可证。本库收录其架构分析及对自有开源游戏 [`turbo998/scrap-swarm`](https://github.com/turbo998/scrap-swarm) 生成的 `ev_<sha256>` 证据台账（[`docs/research/agent-skills-and-rea/evidence/rea-evidence-ledger.json`](docs/research/agent-skills-and-rea/evidence/rea-evidence-ledger.json)）。
- **`wheresryan22/anatomy`**：上游仓库 [`wheresryan22/anatomy`](https://github.com/wheresryan22/anatomy) 提供等轴测 SVG 几何构建器；本库中的美嘉欣 MJX 14303 机械解剖图（[`docs/research/agent-skills-and-rea/h5/mjx-14303-anatomy/`](docs/research/agent-skills-and-rea/h5/mjx-14303-anatomy/)）为原创参数化建模产出。
- **Ryan Doser Skills 分析**：仅基于其公开网页与免费公开示例 `anti-slop.md` 进行结构与商业模式分析，不收录或分发任何付费私有仓库内容。

