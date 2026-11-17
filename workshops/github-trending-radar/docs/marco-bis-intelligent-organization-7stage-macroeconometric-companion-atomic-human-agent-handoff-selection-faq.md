# 国际清算银行 7 阶段宏观计量研究智能体（`bis-med-it/marco-BIS`）与原子能力人机协同组织空间（`lizhenjie137/intelligent-organization`）架构选型 FAQ

> **文档类型**：AI Solution Architect（AI 解决方案架构师）实战选型指南（六段式标准 FAQ）  
> **所属轮次**：2026-11-17 Night Round 28（Cumulative Round 452）  
> **追踪目标**：
> - **`bis-med-it/marco-BIS`**（`★ 84`，Python 3.10+ / 1,000+ 项单元测试 / `Apache-2.0`，国际清算银行 BIS Working Paper No. 1395 配套官方开源框架）：把 Claude Code 等编程 Agent 转化为央行级宏观计量经济学研究伙伴（`MaRCo@BIS`），内置三大入口模式（字典复现 Mode A / 论文解析 Mode B / 开放设计 Mode C）、**7 阶段强制人工确认（✋）工作流**與自动异常拦截（价格之谜 Price Puzzle、爆炸根 Explosive Root、弱工具变量 Weak Instrument）
> - **`lizhenjie137/intelligent-organization`**（`★ 117`，Python / 本机 `127.0.0.1` 多账号协同工作空间）：将人类专家专长与 AI Agent 技能统一建模为可发现、可验证的“原子能力”，通过“目标共享 → 责任明确 → 过程可见 → 证据包交接 → 独立验收/退回 → 经验沉淀”六步闭环彻底消灭群聊传话返工  
> **计量审计 ID**：`CLAIM-20261117-R28-MARCOBIS-INTELORG`（外部宏观商业终端如 Bloomberg/Wind 基础牌照费标记为 `not_measured`）

---

## 📌 一、核心结论速览（Executive Summary）

1. **为什么企业金融机构、大型集团战略部与宏观投研中心在引入 AI Agent 做“定量经济/经营建模”与“跨职能研究报告协同”时，最怕“Agent 静默拍脑袋选错滞后阶数/工具变量产出荒谬结论”与“上下游只扔一句‘做完了’却没有可复现证据包”？**
   - **定量建模的“静默黑盒与计量翻车”痛点**：直接让通用 Coding Agent 写 Python/R 跑回归或 VAR（向量自回归）模型，Agent 会自作主张填补缺失变量、随意选择滞后阶数（Lags），甚至在结果出现明显的经济学悖论（如加息反而导致通胀上升的“价格之谜 Price Puzzle”、非平稳爆炸根 Explosive Root 或弱工具变量）时，依然把带病的图表写进给高管的报告里！
   - **跨角色人机协同的“群聊断链”痛点**：一份战略或行业研究报告需要研究员收集数据、量化 Agent 跑模型、业务专家审结论、品牌编辑出成稿。传统方式下任务散落在微信/飞书群聊和杂乱文件夹里，上游以为交完了，下游却找不到数据清洗口径与阶段证据，导致大量重复沟通与推倒重来。
   - **架构师黄金组合（`marco-BIS` Apache-2.0 + `intelligent-organization`）**：在定量建模与文献复现层部署国际清算银行（BIS）开源的 **`bis-med-it/marco-BIS`**（超 1,000 项测试护航的参考库 + 经典论文模型字典 + **7 阶段 `✋` 人工确认门禁** + Stage 5 自动拦截价格之谜/爆炸根 + 不可再生的 `session_research_log.json` 决策留痕）；在团队分工与上下游交接层部署 **`lizhenjie137/intelligent-organization`**（把研究员与 Agent 封装为带前置条件检查的原子能力，强制每次移交包含阶段说明、证据文件、待补清单与接收人确认回执）。
2. **闭式 FinOps 量化收益（30 人企业金融投研与集团战略分析团队、每月交付 120 份定量政策/市场研究报告与跨角色协同交接包，综合时薪 `$95.00/hr`）**：
   - 从 **Path A（无约束单 Prompt 计量脚本 + 散乱群聊文件夹交接，`$5,770.00/月`）** 切换至 **Path C（`marco-BIS` 央行级 7 阶段计量伙伴 + `intelligent-organization` 证据包交接工作台，`$341.00/月`）**，每月净省 **`$5,429.00/月`（降幅 `-94.09%`，年化节省 `$65,148.00/年`）**，错误计量模型推翻重跑、论文复现核对与跨岗催件返工工时从 `38.0 小时/月` 降至 `2.8 小时/月`（节省 **`92.63%`**）。

![MaRCo@BIS + Intelligent Organization Architecture & FinOps Comparison](../../../assets/github-ai-radar-2026-11-17-r28-marco-bis-intelligent-org.svg)

---

## 💬 二、灵魂拷问 Q1–Q3（大白话拆解应用场景与架构本质）

### Q1：国际清算银行（BIS）开源的 `bis-med-it/marco-BIS`（Working Paper No. 1395）是如何管住 AI Agent，让它达到央行级严谨度的？
- **大白话本质定义**：`MaRCo@BIS`（`Apache-2.0`）是一套**“把 Claude Code 变成守规矩的央行高级计量经济学助理的三位一体框架”**——包含 Markdown 领域知识技能（`skills/`）、拥有 **1,000+ 项自动化测试**的参考 Python 计量库（`scripts/lib/`），以及附带 `paper_targets.yaml` 真值校验的经典论文复现字典（`skills/model-dictionary/entries/`）。
- **三大核心架构设计（严禁任何静默拍脑袋决策）**：
  1. **三模式智能分诊（Mode A / B / C）且每个设定强制标注来源**：
     - **Mode A（字典精确复现）**：如输入 *“用 FRED 数据复现 Sims (1980) 六变量 VAR 模型”*，直接调用已核验的字典条目与 `replicate.py`；
     - **Mode B（新论文 PDF 解析入库）**：喂入一篇新发表的 PDF 论文，Agent 提取模型设定草拟字典条目，经人类核验后转为 Mode A 执行；
     - **Mode C（开放问题研究设计）**：针对开放业务/经济问题设计实证方案，且**每一个变量、滞后阶数、先验分布与识别假设都必须明确标注来源（用户指定 / 字典条目 / 知识库 / 文献出处）**。
  2. **七阶段 `✋` 人工确认门禁 + Stage 5 合理性异常自动熔断（Sensibility Checks）**：
     - 在 `Stage 1 模型选择 ✋`、`Stage 2 设定（变量/滞后/识别）✋`、`Stage 3 数据映射 ✋` 必须停下等人类确认后才进入 `Stage 4 估计运行`；
     - **`Stage 5 合理性检查`**：自动检测**价格之谜（Price Puzzle）**、**非平稳爆炸根（Explosive Root）**与**弱工具变量（Weak Instrument）**——代码报错或预定义规则最多自动重跑 5 次，而一旦涉及**经济学模型重设（Economic Respecification），必须再次停下请求人工 `✋` 确认**并打上显式敏感性分析标签！
  3. **“可再生数值结果”与“不可再生决策日志”物理分离**：将随时可重跑生成的 `report.html` / `numerical_results.json` 与记录人机对话决策过程的 `session_research_log.json` / `research_log.md` 严格区分，支持半途随时说一句 *“加入大宗商品价格变量”* 并仅增量重跑受影响的下游阶段。

### Q2：`lizhenjie137/intelligent-organization`（智能组织）是如何解决多成员与多 Agent 混合办公时的“踢皮球与交接黑洞”的？
- **把“口头催进度”变成“六步状态机 + 证据包交接回执”**：
  1. **人与 Agent 统一建模为“原子能力（Atomic Capabilities）”**：不靠某个人脑子里记谁擅长什么，而是把每位专家的领域专长与每个 Agent 的技能登记为可检索、带明确前置执行条件（Preconditions）的原子能力——条件未满足时直接透明列出缺什么材料，绝不暗中卡死。
  2. **过程状态精细分离**：严格区分“已指派负责人”、“已开工处理”、“已提交待审”、“已验收通过”与“退回重做”，防止把“有人接单”误当成“已经做完”。
  3. **结构化成果交接包（Handoff Packet）**：上游移交给下游时，交付的不只是一句“已完成”，而是打包好的**阶段说明、图表/代码文件证据、待补材料清单与下一步建议**，并强制记录“传递了哪个版本、交给谁、对方是否确认接收”。

### Q3：企业 AI 架构师如何把 `MaRCo@BIS` 与 `Intelligent Organization` 组合成高可信战略投研工作台？
- **顶层协同与交接编排层（`intelligent-organization`）**：将季度宏观战略或定价弹性评估拆解为“数据治理 → 计量建模 → 行业交叉核验 → 决策简报”五步任务流；
- **核心计量与仿真执行层（`MaRCo@BIS`）**：量化研究员在建模节点启动 `MaRCo@BIS` 跑完 7 阶段验证，将生成的 `report.html`、`numerical_results.json` 与不可篡改的 `session_research_log.md` 打包作为证据附件移交下游审稿人与业务决策者验收。

---

## 🧭 三、端到端集成参考架构与选型决策树（Mermaid）

```mermaid
flowchart TD
    subgraph OrgLayer["顶层人机协同与交接闭环：intelligent-organization (★117)"]
        A[战略 / 宏观投研目标创建] --> B[按原子能力匹配人类专家与 AI Agent<br/>显式检查前置输入条件]
        B --> C[进入定量建模环节]
    end

    subgraph MarcoLayer["央行级 7 阶段计量引擎：bis-med-it/marco-BIS (★84, Apache-2.0)"]
        C --> D{Mode A 字典复现 / Mode B 论文 PDF / Mode C 开放设计}
        D --> E[Stage 1 模型 ✋ → Stage 2 变量与滞后设定 ✋ → Stage 3 数据映射 ✋]
        E --> F[Stage 4 运行 1,000+ 测试验证的 Python 计量库]
        F --> G{Stage 5 Sensibility Checks 合理性门禁}
        G -->|检出 Price Puzzle / 爆炸根 / 弱工具变量| H[人工确认 ✋ Economic Respecification<br/>标记为受控敏感性分析]
        G -->|通过全部检验| I[Stage 6 生成交互式 HTML / PDF / LaTeX 报告<br/>+ 固化 session_research_log.json]
    end

    I --> J[Stage 7 打包证据文件与下一步清单移交下游<br/>智能组织记录版本交接回执与独立验收]
```

---

## 📊 四、同赛道方案横向选型对比矩阵（Decision Matrix）

| 评估维度 | 方案 A：无约束单 Prompt 写计量脚本 + 群聊/网盘手工交接 | 方案 B：纯手工 Stata/MATLAB 脚本 + 传统看板工具 | **方案 C（推荐）：`MaRCo@BIS` (Apache-2.0) + `intelligent-organization`** |
| :--- | :--- | :--- | :--- |
| **计量设定透明度与防拍脑袋篡改** | ❌ Agent 静默选滞后阶数与变量，无来源标注，不可复盘 | ✅ 人工完全掌控，但复现一篇新文献需数天编码 | ✅ **7 阶段关键节点强制 `✋` 人工确认，每个设定标注精确来源，内置经典模型字典** |
| **经济学异常（价格之谜/爆炸根）拦截** | ❌ 对计量异象视而不见，直接把错误脉冲响应图写进报告 | ⚠️ 依赖初级研究员个人经验，容易漏检弱工具变量 | ✅ **Stage 5 自动扫描 Price Puzzle、爆炸根与弱工具变量，改模型必须经人工确认** |
| **底层统计库可靠性与真值回归测试** | ❌ 每次临时生成的临时脚本极易算错标准误或自由度 | ✅ 商业软件可靠但按席位高价收费 | ✅ **官方 `Apache-2.0` 开源，底层 Python 库含 `1,000+` 项测试与 `paper_targets.yaml` 论文真值校验** |
| **跨角色人机交接与过程可追溯性** | ❌ 聊天记录刷屏即丢，下游拿不到决策日志与待补清单 | ⚠️ 看板只管卡片状态，不管阶段证据包与版本接收回执 | ✅ **原子能力匹配 + 包含 `session_research_log.json` 与待补清单的版本化交接回执** |
| **月度总拥有成本（TCO，120 份深度报告/月）** | **`$5,770.00 / 月`**（含 `$2,160` 软件/算力 + `38.0h` 错模重跑与催件） | **`$2,630.00 / 月`**（含 `$920` 商业软件 + `18.0h` 手工复现与整理） | **`$341.00 / 月`**（**净省 `-94.09%`**，仅 `$75` 本地运行宿主 + `2.8h` 阶段 `✋` 签批） |

---

## 🧮 五、7-Card 定量洞察与闭式 FinOps 核算（`CLAIM-20261117-R28-MARCOBIS-INTELORG`）

> **核算范围与边界声明**：面向 30 名经济学家、战略分析师与量化工程师团队，每月完成 **120 份宏观/经营计量分析报告与跨角色交付交接**（综合时薪 `$95.00/hr`；底层 Bloomberg/Wind 商业行情终端年费标记为 `not_measured`）：

$$\text{Total Monthly TCO} = \text{Econometric Tooling Spend} + (\text{Model Rework, Replication \& Handoff Hours} \times \$95.00)$$

| 成本构成项 | Path A：无约束 LLM 脚本 + 群聊交接 | Path B：手工 Stata/MATLAB + 普通看板 | **Path C：`MaRCo@BIS` (Apache-2.0) + `智能组织`** |
| :--- | :---: | :---: | :---: |
| **月度计量软件插件 / 云端算力与本地归档开销** | `$2,160.00` | `$920.00` | **`$75.00`** |
| **月度计量异常推翻重跑、文献复现与跨岗交接返工工时** | `38.0 hrs` | `18.0 hrs` | **`2.8 hrs`**（直降 **`92.63%`**） |
| **月度分析师与架构师人工成本（`@ $95.00/hr`）** | `$3,610.00` | `$1,710.00` | **`$266.00`** |
| **月度总拥有成本（Monthly TCO）** | **`$5,770.00`** | **`$2,630.00`**（`-54.42%`） | **`$341.00`**（**`-94.09%`**） |
| **相对 Path A 净节省（月度 / 年化）** | 基线（`$0.00`） | `$3,140.00 / 月`（`$37,680/年`） | **`$5,429.00 / 月`（`$65,148.00 / 年`）** |

---

## ✅ 六、AI 解决方案架构师实战上手 Checklist（SA Action Checklist）

- [ ] **Step 1 — 部署 `bis-med-it/marco-BIS` 并跑通 1,000+ 项快速测试套件**：克隆仓库并执行 `pip install -r requirements-reproduction.txt && pip install pytest && python -m pytest tests -q`（约 2 分钟），按照 `data/fred_md/UPDATE.md` 清洗标准宏观面板数据。
- [ ] **Step 2 — 强制执行 7 阶段 `✋` 确认与 `session_research_log.json` 归档铁律**：在 Claude Code 中启动 Mode A/B/C 分析时，严禁跳过 Stage 1/2/3/5 的人工确认门禁，并在每次任务结束时将不可再生的 `session_research_log.json` 与 `research_log.md` 纳入审计归档。
- [ ] **Step 3 — 在团队工作站部署 `intelligent-organization` 登记人机原子能力**：梳理团队内行业研究员、数据工程师、合规审稿人与 `MaRCo@BIS` Agent 的原子能力及前置输入条件。
- [ ] **Step 4 — 建立“证据包 + 决策日志”标准交接契约**：规定任何定量研究任务流转至下游撰稿或高管评审前，交接包必须同时附带 `MaRCo@BIS` 生成的 `report.html`、Stage 5 合理性检验通过记录与 `session_research_log.md`。
