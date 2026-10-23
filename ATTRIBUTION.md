# 归属与权利边界

本公开库由 **turbo998** 维护。Personal agents 的中文分析、比较组织、统一 benchmark 合同及 18 个合成案例为原创整理，使用 AI 辅助研究与独立另进程 AI 审阅；不冒称人工认证或产品实测。

## 本库专题引用

| 专题 / 内容 | 公开出处与归属 |
|---|---|
| **Agent Forge (FAF v2) vs. Microsoft AGENT-FORGE 架构对比与契约评测** | `customer-success-microsoft/faf-agents`（固定 commit `a740ad88afa0b054e656207e72205002ca6744f0`，MIT License，含源自 Anthropic Claude Code Skills 的文档技能声明）与公开仓库 [`microsoft/agent-forge`](https://github.com/microsoft/agent-forge/tree/655ff3401d18bd000252907a512a3f674114f708)（`@agent-forge-copilot/cli@0.3.0`，固定 commit `655ff3401d18bd000252907a512a3f674114f708`，MIT License）。完整核验台账见 [`docs/research/faf-vs-agent-forge/evidence.json`](docs/research/faf-vs-agent-forge/evidence.json) |
| **Agent 逆向工程 (`morluto/rea`)、机械解剖学 (`anatomy`) 与商业化 Skills 研究** | 上游开源仓库 [`morluto/rea`](https://github.com/morluto/rea)（MIT License，个人 Fork [`turbo998/rea`](https://github.com/turbo998/rea)）、[`wheresryan22/anatomy`](https://github.com/wheresryan22/anatomy) 及 Ryan Doser 公开产品页（`ryandoser.com` / `skills.ryandoser.com`）。被逆向 H5 游戏《废土斗机祭 (Scrap Swarm)》源自本账号自有开源仓库 [`turbo998/scrap-swarm`](https://github.com/turbo998/scrap-swarm) 与 [`turbo998/ai-gaming-lab`](https://github.com/turbo998/ai-gaming-lab) |
| **Omarchy agent 设计机制与契约评测** | 上游公开入口 `basecamp/omarchy`、规范仓库 `omacom/omarchy`，固定 commit [`9480d1b6a98156314dbabe6bfef08f39f8b9cd07`](https://github.com/omacom/omarchy/commit/9480d1b6a98156314dbabe6bfef08f39f8b9cd07)；原维护者及根 `LICENSE`（MIT）版权归属 David Heinemeier Hansson。轻量平台比较引用 Anthropic 与 GitHub 官方文档（W1–W7）。完整可复核台账见 [`docs/research/omarchy-agent-design/evidence.json`](docs/research/omarchy-agent-design/evidence.json) |
| **Personal agents：产品、资格、控制及政策声明** | Meta/Muse；x.ai 与 Cursor；OpenAI；Google/Gemini/Google Cloud；Spear Street Technology, Inc. d/b/a Instinct。准确页面与读取范围见 S1–S17 |
| **Personal agents：第三方比较与产品观察** | Every；Dhravya Shah / Supermemory；Personal Agent Bench / Zentor。商业利害、方法限制及未复算状态见 S18–S22 |
| **Personal agents：Benchmark 论文与文档** | GAIA 作者及 arXiv/Hugging Face；OSWorld 作者及 xlang-ai maintainers；τ 系列作者及 Sierra Research。版本、固定公开 commit 与访问边界见 B1–B9 |

完整可复核引用：[Omarchy evidence.json](docs/research/omarchy-agent-design/evidence.json) · [Personal agents evidence.json](docs/research/personal-agents/evidence.json) · [第三方声明](THIRD_PARTY_NOTICES.md)。保留研究所需且本就公开的 source attribution；不刊登上游私人会话、实际联系人、账号、媒体、题目库、完整上游代码或完整原文。

## 许可与再分发

本库以原创概述及必要公开链接引用来源。产品名称和商标属于各自权利人，不代表背书。公开可读不等于允许复制第三方素材；本站未将第三方网页、政策、数据、VM images、媒体或产品内部材料纳入任何统一开源许可。

上游 OSWorld root code 的 Apache-2.0、τ repositories root code 的 MIT，仅描述相应上游代码，**不覆盖**本库引用的其他素材或产品 benchmark 权利。GAIA 数据 gated/anti-resharing，未下载或再发布；Instinct Terms 对 benchmarking 的限制保持有效。

本库目前未授予统一的再分发许可；需要复用原创正文或合成案例时，应先确认相应许可。案例中的项目、人员角色、地址和 canary 都是合成 fixture，保留示例域只用于隔离 mock world，禁止据此对公共互联网执行动作。
