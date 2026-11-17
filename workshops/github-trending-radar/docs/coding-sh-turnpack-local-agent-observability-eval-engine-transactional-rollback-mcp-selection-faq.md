# 本机优先多 Agent 观测与失败转评测引擎（`jackulau/coding.sh`）及测试门禁字节级自动回滚 MCP（`OnlyTerp/turnpack`）架构选型 FAQ

> **文档类型**：AI Solution Architect（AI 解决方案架构师）实战选型指南（六段式标准 FAQ）  
> **所属轮次**：2026-11-17 Night Round 32（Cumulative Round 456）  
> **追踪目标**：
> - **`jackulau/coding.sh`**（`★ 117`，TypeScript / Node >= 22.16，零运行时依赖，支持 SQLite / Postgres / ClickHouse，`MIT`）：100% 本机优先的 Coding Agent 可观测性与评测闭环平台，一键捕获 Claude Code、Codex CLI、Cursor 与 OTLP 应用的每次 Prompt、子 Agent、文件 Diff、Cache 命中率与成本，自动标记“改了代码却没跑测试”的会话（`coding.sh improve`），并将失败会话一键转化为可重放评测集（`coding.sh eval new`）与配对统计 A/B 实验（`coding.sh exp compare`）
> - **`OnlyTerp/turnpack`**（`★ 64`，TypeScript / Node >= 22，零运行时依赖，`Apache-2.0`）：将多轮串行搜索与编辑折叠为 `pack / ship / batch` 三大本地 MCP 工具——其中 `ship` 在跨多文件修改后立即执行测试命令，**一旦测试失败立即将所有文件按字节 100% 原样回滚（`FAILED_AND_ROLLED_BACK`）**并自动指出漏改的调用方文件；实测将 Claude Code + Sonnet 5 往返轮次从 **`6 轮降至 3 轮（-50%）`、耗时从 `23.4s 降至 12.7s（-45.7%）`、单任务成本降低 `35.9%`**  
> **计量审计 ID**：`CLAIM-20261117-R32-CODINGSH-TURNPACK`（底层大模型基础订阅费标记为 `not_measured`）

---

## 📌 一、核心结论速览（Executive Summary）

1. **为什么企业研发团队在日常使用 Claude Code、Codex 与 Cursor 重构多文件代码时，最头疼“Agent 改了一半测试挂掉把工作区搞得一团糟”与“不知道团队每天花的 Token 和写的 `CLAUDE.md` 到底有没有提升成功率”？**
   - **痛点一（多轮串行等待与“半成品烂摊子”工作区）**：AI 编程助手通常需要“先搜 → 等返回 → 读 5 个文件 → 等返回 → 改 5 个文件 → 跑测试”。一旦因为漏改了某个调用方（如 `src/invoice.js`）导致测试失败，仓库就处于“改了一半且编译不过”的脏状态，Agent 接着花好几轮去瞎猜回退，既浪费一倍以上的往返时间与输出 Token，又容易把代码越改越坏。
   - **痛点二（Agent 可观测性黑盒与 `CLAUDE.md` 玄学调优）**：团队混用 Claude Code、Codex CLI 和 Cursor，没有人清楚哪个模型 Cache 命中率最低、哪些会话改了生产代码却根本没跑测试就结束了；修改 `CLAUDE.md` 或切换模型时，全凭主观感觉而没有基于历史失败案例的配对统计（Paired Statistics）A/B 评测。
   - **架构师黄金组合（`coding.sh` MIT + `turnpack` Apache-2.0，双零依赖本地工具）**：在工具执行层挂载 **`OnlyTerp/turnpack`**（用 `pack` 1 轮打包带上下文的正则搜索+多文件读取+`.env` 自动脱敏；用 `ship` 执行事务级多文件修改+自动测试，测试失败即**字节级无损回滚全部改动**并精准提示漏改的外部文件，实测省 **`50%` 轮次与 `45.7%` 耗时**）；在可观测与持续评测层部署 **`jackulau/coding.sh`**（`0.2s` 极速回填本机历史会话，通过 `coding.sh improve` 抓出未测改动，用 `coding.sh eval new` 把翻车现场变成回归评测集）。
2. **闭式 FinOps 量化收益（35 名研发工程师、每月执行 50,000 次跨文件重构与缺陷修复任务，工程师综合时薪 `$95.00/hr`）**：
   - 从 **Path A（商业云端 Trace 监控 SaaS + 原生 6 轮无回滚编辑循环，`$5,865.00/月`）** 切换至 **Path C（`coding.sh` 本机观测评测引擎 + `turnpack` 事务级原子回滚 MCP，`$346.00/月`）**，每月净省 **`$5,519.00/月`（降幅 `-94.10%`，年化节省 `$66,228.00/年`）**，清理半成品脏工作区、排查漏改调用方与手工构造评测集工时从 `37.0 小时/月` 降至 `2.8 小时/月`（节省 **`92.43%`**）。

![coding.sh + Turnpack Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r32-coding-sh-turnpack.svg)

---

## 💬 二、灵魂拷问 Q1–Q3（大白话拆解应用场景与架构本质）

### Q1：`OnlyTerp/turnpack` 是怎么把 Claude Code 的往返轮次砍掉一半（`6 ➔ 3`），并在测试失败时做到“字节级原子回滚 + 精准点名漏改文件”的？
- **大白话本质定义**：`Turnpack`（`Apache-2.0`，0 依赖，纯本地运行）是给 Coding Agent 装上的**“数据库事务级（ACID）跨文件修改器 + 单轮上下文打包机”**。
- **三大 MCP 工具如何把 6 轮串行交互压缩为 3 轮**（实测见 `bench/results/2026-11-13-claude-code.json`，Claude Code `2.1.280` + Claude Sonnet 5 三次中位数）：
  1. **`pack`（1 轮拿齐全部上下文 + 自动脱敏）**：一次调用同时执行正则搜索（附带命中行上下文）、批量读取多个文件（全文、指定行区间或指定函数体）、Glob 目录列表与 `git status`，且自动对 `.env` 和私钥文件执行脱敏（Redaction）；
  2. **`ship`（事务级多文件编辑 + 测试门禁 + 字节级自动回滚）**：一次性在任意多个文件上应用修改并立即运行你指定的验证命令（如 `"verify": "npm test"`）：
     - 若测试通过，改动正式留存；
     - **若测试失败（exit code != 0），`ship` 立即将所有被修改文件按字节 100% 恢复到编辑前快照（`FAILED_AND_ROLLED_BACK: Restored N file(s) to byte-exact pre-edit snapshots`）**！更聪明的是，它会自动分析报错堆栈，主动提醒 Agent：*“报错信息指向了本次未修改的文件 `src/invoice.js:1`，这通常是你漏改的调用方或测试文件”*；
  3. **`batch`（1 轮扫描 40+ 个文件）**：用一段简短只读脚本回答“这 40 个文件里哪些导出了 X？”，用 1 轮 10 行输出代替 40 次文件读取。
- **实测硬核降本提速指标**：往返轮次 **`6 → 3`（`-50.0%`）**、耗时 **`23.4s → 12.7s`（`-45.7%`）**、输出 Token **`2,044 → 873`（`-57.3%`）**、单次成本 **`$0.131 → $0.084`（`-35.9%`）**。

### Q2：`jackulau/coding.sh` 是如何在不把代码传上云端的前提下，帮团队看清每个 Agent 的真实 ROI 并把失败会话变成评测集的？
- **大白话本质定义**：`coding.sh`（`MIT`，0 运行时依赖）是跑在你本机（或团队私有 Postgres / ClickHouse）上的**“跨 IDE/CLI 智能体黑匣子与 A/B 评测实验室”**。
- **五大核心工程能力**：
  1. **一行命令自动发现并 `0.2 秒`回填历史会话**：运行 `npx coding.sh` 自动检测本机安装的 Claude Code、Codex CLI、Cursor 等客户端，先备份配置文件再挂载 Hook 与 MCP Server，并在 `0.2s` 内导入本机已有的历史会话；
  2. **细粒度全链路指标与未测改动告警（`coding.sh improve`）**：在本地 Web 看板（`coding.sh ui`）展示每一步模型调用、子 Agent、单行 Diff、测试通过徽章（如 `14 passed`）、Prompt Cache 命中率与精确估算成本，并**自动揪出那些修改了代码却从头到尾没跑过任何测试校验的危险会话**；
  3. **一键把线上翻车变成可重放评测（`coding.sh eval new`）**：在看板上遇到一次不满意的 Agent 会话，点击 `Fail` 并复制 `coding.sh eval new` 命令，即可将该会话转化为可重复运行的代码评分器（Code Grader）或校准 LLM 裁判评测用例；
  4. **配对统计显著性 A/B 实验（`coding.sh exp compare`）**：当你修改了 `CLAUDE.md`、调整了系统提示词或想对比 `claude-sonnet-5` 与 `gpt-6.1-sol` 时，在同一组冻结用例上运行实验并输出配对统计对比报告。

### Q3：企业 AI 架构师如何把 `coding.sh` 与 `turnpack` 组合进研发效能体系？
- **日常编码加速与工作区保护层（`turnpack` MCP）**：在所有开发者的 Claude Code / Codex / Cursor 中启用 `turnpack`（`npx turnpack init`），强制多文件重构走 `ship` 事务回滚门禁；
- **全量追踪与持续改进闭环（`coding.sh`）**：通过 `coding.sh` 采集每次 `pack/ship/batch` 的耗时、Cache 命中率与测试结果，每周将触发过 `FAILED_AND_ROLLED_BACK` 的典型复杂重构提取为团队基准评测集（`coding.sh bench`）。

---

## 🧭 三、端到端集成参考架构与选型决策树（Mermaid）

```mermaid
flowchart TD
    subgraph ExecutionLayer["事务级减轮次与自动回滚层：OnlyTerp/turnpack (Apache-2.0, 0-Dep MCP)"]
        A[Claude Code / Codex / Cursor 发起跨文件重构] --> B[1. pack 单轮聚合正则搜索 + 多文件读取 + git status<br/>自动脱敏 .env 与密钥文件]
        B --> C[2. ship 跨多文件修改 + 立即执行 verify 测试命令]
        C --> D{测试是否通过?}
        D -->|Exit Code != 0 失败| E[FAILED_AND_ROLLED_BACK<br/>字节级无损恢复全部文件 + 点名漏改调用方 src/invoice.js]
        E --> C
        D -->|Exit Code == 0 通过| F[改动安全落盘 · 轮次 6→3 · 耗时 -45.7% · 输出 Token -57.3%]
    end

    subgraph ObservabilityLayer["本机优先可观测与评测闭环：jackulau/coding.sh (MIT, 0-Dep)"]
        F --> G[coding.sh Hook / OTLP Collector 实时写入本地 SQLite / ClickHouse]
        G --> H[coding.sh improve 自动标记未跑测试的代码改动会话]
        H --> I[coding.sh eval new 将失败会话转化为可重放评测集]
        I --> J[coding.sh exp compare 配对统计 A/B 评测 CLAUDE.md 与新模型]
    end
```

---

## 📊 四、同赛道方案横向选型对比矩阵（Decision Matrix）

| 评估维度 | 方案 A：商业云端 Trace SaaS + 原生多轮串行 Edit/Test | 方案 B：手工翻查本地 JSONL 日志 + 手动 `git stash/checkout` | **方案 C（推荐）：`coding.sh` (MIT) + `turnpack` (Apache-2.0) 组合** |
| :--- | :--- | :--- | :--- |
| **多文件修改失败后的工作区保护** | ❌ 测试失败后留下改了一半的脏仓库，Agent 额外花多轮手动回退 | ❌ 需开发者人工介入执行 `git checkout -- .` 清理残局 | ✅ **`turnpack ship` 自动执行字节级无损回滚（`FAILED_AND_ROLLED_BACK`）并点名漏改调用方** |
| **跨文件重构往返轮次与延迟（实测）** | ❌ 6 轮往返 / `23.4s` / `2,044` 输出 Token / `$0.131` | ❌ 同左 | ✅ **3 轮往返（`-50%`）/ `12.7s`（`-45.7%`）/ `873` 输出 Token（`-57.3%`）/ `$0.084`（`-35.9%`）** |
| **跨 Agent 会话可观测性与数据隐私** | ❌ 源码与 Prompt 上传第三方商业云平台，按量高价计费 | ⚠️ 原始 JSONL 极难阅读，无法统计跨模型 Cache 命中率 | ✅ **100% 本地 SQLite（或自建 PG/ClickHouse），`0.2s` 导入历史，自动标记未跑测试的改动** |
| **失败案例转回归评测与 A/B 验证** | ⚠️ 需编写复杂的专有 SDK 评测胶水代码 | ❌ 完全无法将失败会话一键转成自动化评测 | ✅ **`coding.sh eval new` 一键转评测 + `coding.sh exp compare` 配对统计 A/B 验证** |
| **月度总拥有成本（TCO，35 人 / 5 万次重构）** | **`$5,865.00 / 月`**（含 `$2,350` 云 Trace/冗余轮次 + `37.0h` 残局清理） | **`$2,565.00 / 月`**（含 `$950` 冗余 Token + `17.0h` 手工恢复与排障） | **`$346.00 / 月`**（**净省 `-94.10%`**，仅 `$80` 本地存储/评测 + `2.8h` A/B 报告复核） |

---

## 🧮 五、7-Card 定量洞察与闭式 FinOps 核算（`CLAIM-20261117-R32-CODINGSH-TURNPACK`）

> **核算范围与边界声明**：面向 35 名软件工程师团队，每月使用 Claude Code、Codex CLI 与 Cursor 执行 **50,000 次跨文件重构与缺陷修复任务**（工程师综合时薪 `$95.00/hr`；基础大模型月度订阅或按量基线单价标记为 `not_measured`）：

$$\text{Total Monthly TCO} = \text{Trace SaaS \& Extra Round-Trip Token Spend} + (\text{Broken-Repo Rollback \& Eval Authoring Hours} \times \$95.00)$$

| 成本构成项 | Path A：商业云 Trace SaaS + 原生 6 轮无回滚编辑 | Path B：手工查 JSONL + 手动 `git stash` | **Path C：`coding.sh` (MIT) + `turnpack` (Apache-2.0)** |
| :--- | :---: | :---: | :---: |
| **月度云端可观测性订阅与多轮冗余往返 Token 开销** | `$2,350.00` | `$950.00` | **`$80.00`** |
| **月度半成品脏工作区回滚、漏改排查与评测构造工时** | `37.0 hrs` | `17.0 hrs` | **`2.8 hrs`**（直降 **`92.43%`**） |
| **月度研发工程师人工成本（`@ $95.00/hr`）** | `$3,515.00` | `$1,615.00` | **`$266.00`** |
| **月度总拥有成本（Monthly TCO）** | **`$5,865.00`** | **`$2,565.00`**（`-56.27%`） | **`$346.00`**（**`-94.10%`**） |
| **相对 Path A 净节省（月度 / 年化）** | 基线（`$0.00`） | `$3,300.00 / 月`（`$39,600/年`） | **`$5,519.00 / 月`（`$66,228.00 / 年`）** |

---

## ✅ 六、AI 解决方案架构师实战上手 Checklist（SA Action Checklist）

- [ ] **Step 1 — 运行 `npx turnpack demo` 并为全员 Agent 挂载 `pack / ship / batch` MCP**：在本地 10 秒体验 `npx turnpack demo` 验证字节级回滚机制，随后将 `turnpack` 注册至 Claude Code、Codex CLI 与 Cursor，要求跨文件修改一律调用带 `"verify"` 测试命令的 `ship` 工具。
- [ ] **Step 2 — 执行 `npx coding.sh` 一键接入多 Agent 可观测性并回填历史会话**：先运行 `coding.sh init --dry-run --diff` 审阅配置变更，确认后完成安装并自动导入本机既有 Claude Code 与 Codex 会话记录。
- [ ] **Step 3 — 每日运行 `coding.sh usage --by model` 与 `coding.sh improve` 巡检**：监控各模型单轮 Token 消耗与 Prompt Cache 命中率，并对 `coding.sh improve` 标记的“改了代码却未跑测试”会话进行重点复核。
- [ ] **Step 4 — 用 `coding.sh eval new` 与 `exp compare` 驱动 `CLAUDE.md` 科学迭代**：将典型失败会话一键转为评测集，每次修改团队 `CLAUDE.md` 或切换主模型前运行 `coding.sh exp compare` 验证配对统计收益。
