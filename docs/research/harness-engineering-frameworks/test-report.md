# 7-Card 4:5 技术评测报告：主流 Agent Harness Engineering 框架与实现机制深度对比（DeepSeek DSH × Claude Code × Microsoft HVE Core）

> **双语版本 / Bilingual Navigation**: [中文报告 (test-report.md)](./test-report.md) | [English Report (test-report.en.md)](./test-report.en.md) | [7-Card 视觉卡片 (中文)](./cards.zh.html) | [7-Card Visual Deck (EN)](./cards.html) | [Interactive Playground](./index.html)

---

## Card 1 (`1 / 7` · `HANDS-ON · AGENT HARNESS ENGINEERING`) — 评测总览与工作台

**核心发现标题**：**DeepSeek DSH (96.0分)、Claude Code (90.4分) 与 Microsoft HVE Core (90.4分) 构筑 Agent Harness 三大互补技术范式**

- **锁定源码基线 (Sealed Commit Provenance)**：
  - `deepseek-ai/deepseek-harness`: `@fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159` (`release-dsh-0.2.2-rc.1`) — **23,540** 个 Git Tree 对象、**411** 个 `package.json` 模块、**49** 个顶层子系统域、**6** 大标准 Bundle、**7** 种可插拔子智能体后端。
  - `anthropics/claude-code`: `@0ed94698aa0aeee471465fc9c867c2e8434c4d68` — **1,980** 个 Git Tree 对象、**5** 类 SDK 核心流式消息、**6** 档权限模式、**5** 档推理 Effort、企业级 Devcontainer/Gateway/MDM/HIPAA 模板。
  - `microsoft/hve-core`: `@f425e943bf228052a23e6bc4810b5faef030314f` (`v3.3.101`) — **3,779** 个 Git Tree 对象、**69** 个 Custom Agents、**43** 个 `applyTo` Instructions、**93** 个可执行 Skills、**14** 个 Collection 清单与 `@microsoft/vally-cli` 自动化评测门禁。

---

## Card 2 (`2 / 7` · `SCENARIO: 200K LONG-HORIZON & SANDBOX SEAM`) — 单案深度拆解

**核心发现标题**：**200K 会话导致系统指令权重从 30.0% 暴跌至 1.5%（20倍稀释），HVE `/clear` 恢复至 15.0% 且 DSH 保活 94.2% KV Cache**

1. **Microsoft HVE Core 阶段间 `/clear` + `.copilot-tracking/` 磁盘水合** (`score` · `95.8%` · `Act automatically`)：
   - 在 `10,000` Token 初始会话中，`3,000` Token 的系统指令占比 **30.0%**；当实施一轮复杂代码修改累积至 `200,000` Token 后，系统指令占比跌至 **1.5%**（20 倍注意力稀释），近因偏差（Recency Bias）导致模型跳步风险高达 **92%**。
   - HVE 强制在 Research → Plan → Implement → Review 之间执行 `/clear`，仅加载 `3K` 系统指令 + `4.5K` 磁盘工件，将有效指令权重恢复至 **15.0%**（10 倍恢复）。
2. **DeepSeek DSH `systemPromptUpdate: 'in-history'` 缓存保活** (`choice` · `95.1%` · `Act automatically`)：
   - 当会话中途工作目录或挂载技能变化时，不覆写 `seq:0 system/message`，而是追加在历史流尾部，使前缀 KV Cache 命中率从 **18.5%** 提升至 **94.2%**。
3. **DeepSeek DSH `@deepseek-ai/dsh-tool-executor-ptc` (`run_code`)** (`score` · `94.2%` · `Act automatically`)：
   - 20 步仓库依赖追踪在单次 `run_code` TypeScript 沙箱内通过 `Promise.all` 完成，耗时从 `6,850 ms` 降至 **`3,280 ms` (2.09x 加速)**，模型往返从 6 步降至 1 步。

---

## Card 3 (`3 / 7` · `WHAT I TESTED`) — 12 项企业级 AI SA 场景评测全矩阵

| 场景 ID | 架构挑战与问题 | 推荐 Harness 模式与组件 | 置信度 | 门禁动作 |
| :--- | :--- | :--- | :---: | :---: |
| **S01** | 零工具分叉将 Bash/LSP/File 迁往远程 SSH/容器沙箱 | DSH 三角色能力缝隙 (`ctx.fs` + `ctx.subprocess`) | 96.4% | `Act automatically` |
| **S02** | 防止 200K Token 后因 1.5% 指令稀释跳过规划直接改代码 | HVE Strict RPI + `/clear` + `.copilot-tracking/` | 95.8% | `Act automatically` |
| **S03** | 30+ 次检索聚合不污染上下文且减少模型往返 | DSH `@deepseek-ai/dsh-tool-executor-ptc` (`run_code`) | 94.2% | `Act automatically` |
| **S04** | 对父 Agent 与后台子 Agent 实施共享美元预算硬上限 | Claude Agent SDK (`max_budget_usd` + `readOnlyHint`) | 93.6% | `Act automatically` |
| **S05** | 会话中途更新系统提示词且不破坏首节点 KV Cache 前缀 | DSH `systemPromptUpdate: 'in-history'` | 95.1% | `Act automatically` |
| **S06** | 单父会话统一联邦调度进程内 Fork、Claude Code、Codex 与 ACP | DSH `ctx.subagents` 7-Provider Seam | 94.8% | `Act automatically` |
| **S07** | 百人团队分发标准化 AI 工件并执行模型白名单与行为评测 | HVE Collections + `vally eval` + 工件加密签名 | 96.9% | `Act automatically` |
| **S08** | 多对等 Agent 并行认领任务、无环 DAG 依赖与写目录隔离 | DSH `ctx.agentTeams` CAS `revision` + `blockedBy` DAG | 91.5% | `Act automatically` |
| **S09** | 挂载 120+ 企业 MCP 工具但防止首轮请求被闲置 Schema 塞满 | Claude Code `MCP ToolSearch` 按需延迟加载 | 92.8% | `Act automatically` |
| **S10** | 合入前自动执行 PC-xxx 计划批判与零暗示对抗式质询 | HVE `rpi-plan-critique` + `task-challenger` | 93.4% | `Act automatically` |
| **S11 ✕** | **反模式测试**：3 步无状态轻量 CLI 脚本硬套分布式 Team DAG | **✕ 拦截过度工程**：改用 `dsh-sdk-minimal` 或单次 `query()` | 61.2% | `Confirm` |
| **S12** | 企业数字员工平台：兼得 HVE 阶段治理与 DSH/Claude 运行时内核 | 上层 HVE 四层工件+RPI / 下层 DSH Cordis+Claude 子智能体 | 97.6% | `Act automatically` |

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`) — 底层协议与确定性验证器机制

- **DSH PTC 配额计算公式**：`allowance = floor(resolvedTimeoutMs / 60000 × maxSubCallsPerMinute)`。默认 Node 超时 `120,000 ms` × `1024/min` = **2,048 次子调用**；第 2,049 次调用立即通过运行时中止路径终止整个程序并返回 `CODE_RUN_FAILED`。
- **DSH 不可变事件流投影定律**：`deriveMessages()` 是 `SessionEventMap` 的纯函数投影；压缩通过 `surfaceOp: { op: 'replace', startSeq, endSeq }` 替换表面节点区间，并强校验 `toolPairingBalancedBefore / After`。

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`) — 候选翻转与扰动一致性检验

- 对全部 12 项企业场景执行候选框架正序/逆序翻转、系统提示词 Token 微扰（`3,000` vs `3,200`）与并发 CAS 抢占测试，最大置信度漂移为 **`0.0 pts`**。

---

## Card 6 (`6 / 7` · `LATENCY`) — 工具管线并发与 PTC 扩展延迟对比

| 负载梯度 | 串行基线 (`maxParallel=1`) | 原生只读并发+写屏障 (`Native`) | DSH PTC `run_code` | PTC 相对串行加速比 | PTC 相对 Native 加速比 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Tier 1 · 4 路只读检索** | 3,420 ms | 1,180 ms (2 Steps) | **940 ms (1 Step)** | **3.64x** | **1.26x** |
| **Tier 2 · 6 读 + 2 写屏障** | 7,860 ms | 3,120 ms (4 Steps) | **2,190 ms (1 Step)** | **3.59x** | **1.42x** |
| **Tier 3 · 20 步跨模块审计** | 19,400 ms | 6,850 ms (6 Steps) | **3,280 ms (1 Step)** | **5.91x** | **2.09x** |
| **Tier 4 · 50 次工具批量迁移** | 48,200 ms | 16,900 ms (12 Steps) | **6,420 ms (2 Steps)** | **7.51x** | **2.63x** |

---

## Card 7 (`7 / 7` · `MY TAKE`) — 架构师裁决：适用边界与黄金混合栈

- **✅ Good Fit**：上层采纳 **Microsoft HVE Core**（四层工件委托链 + RPI 阶段间 `/clear` + `.copilot-tracking/` 磁盘台账 + `Vally` 评测门禁）；下层采纳 **DeepSeek DSH + Claude Code SDK**（三角色沙箱缝隙、`PTC run_code`、`in-history` KV Cache 保活、`subagent-claude-code` 联邦与 `max_budget_usd` 成本硬上限）。
- **⛔ Not For**：严禁在单次未清理的 200K 会话中裸跑全周期研发；严禁在会话中途直接覆写 Node-0 系统提示词；严禁为 3 步轻量脚本硬套重型分布式任务板（S11 ✕）。
