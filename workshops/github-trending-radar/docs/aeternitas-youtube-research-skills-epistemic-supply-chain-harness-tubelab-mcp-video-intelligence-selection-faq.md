# 四层认识论隔离的算力供应链投研底座（`Aeternitasoo/Aeternitas`）与基于 TubeLab MCP 实证数据的六角色视频调研技能（`TubeLabHQ/youtube-research-skills`）选型与架构拆解 FAQ

> **所属专题**：GitHub AI 热榜与新晋高星项目选型内参 · 2026-11-14 Night Round 71（累计第 254 轮 / R254）  
> **对标标杆**：`ib-vs-ethernet-roce-selection-faq.md`（大白话本质定义 + 第一性原理 + 六段式结构 + 闭式 FinOps 审计）  
> **审计编号**：`CLAIM-20261114-R71-AETERNITAS-TUBELABSKILLS`  
> **配套架构大图**：[`assets/github-ai-radar-2026-11-14-r71-aeternitas-tubelabskills.svg`](../../../assets/github-ai-radar-2026-11-14-r71-aeternitas-tubelabskills.svg)  
> **English Version**: [Read in English (`aeternitas-youtube-research-skills-epistemic-supply-chain-harness-tubelab-mcp-video-intelligence-selection-faq.en.md`)](./aeternitas-youtube-research-skills-epistemic-supply-chain-harness-tubelab-mcp-video-intelligence-selection-faq.en.md)

---

## 📌 一、核心结论速览（30 秒看懂：它们到底是什么？解决什么痛点？）

1. **用大白话讲透这两个项目**：
   - **`Aeternitasoo/Aeternitas`（`★ 50`，Python 3.13.18）** 是一套专为**电力、AI 算力/半导体与云计算供应链研究**打造的**四层认识论隔离 Agentic 投研基础设施（Epistemic Supply-Chain Research Harness）**。普通 Deep Research Agent 最大的问题是“把事实、推理和模型脑补混为一谈，甚至缺失遥测时静默填 0、或者让递归自改进脚本随便篡改工具权限”。`Aeternitas` 强制在六阶段工作流（`Discover → Plan → Gather → Analyze → Critique → Synthesize`）中把每一条结论拆解并标注为 **`Facts（事实） / Inferences（推论） / Hypotheses（假设） / Unknowns（未知）`** 四类；所有 `SKILL.md` 均带版本与 SHA 指纹锁且**严禁扩大运行时工具权限**；`Mem0 2.2.1` 被隔离在严格的 Sidecar 适配器边界后；`FailureDiagnostics` 拒绝将未知 token/成本静默归零（`unknown ≠ 0`）；自改进（`Controlled RSI`）必须经过人类审批门禁才能晋升。
   - **`TubeLabHQ/youtube-research-skills`（`★ 85`，JavaScript，MIT 协议）** 是一套由 **`TubeLab MCP`（`https://public-api.tubelab.net/mcp`）实时视频数据库驱动的六角色 YouTube 内容调研技能组**（覆盖 `content-ideation`、`niche-research`、`channel-audit`、`competitor-analysis`、`script-writer`、`seo-packaging`）。普通提示词写视频选题只会吐出“做一期 AI 趋势盘点”的空泛套话；而 `youtube-research-skills` 规定**任何一条选题、标题或竞品结论都必须附带真实可点击的频道链接、爆款视频标题、播放量、异常爆发倍数（Outlier Ratio）与发布日期**，一键兼容 Claude Code、Cursor、Codex 与 Windsurf。
2. **核心量化收益（闭式 FinOps 方程 `CLAIM-20261114-R71-AETERNITAS-TUBELABSKILLS`）**：
   - 按团队每月执行 **25 次深度行业供应链投研与视频爆款实证策划工作流**、AI SA 时薪 **$95.00/hr** 核算（本地硬件测量标注：`not_measured`）：
   - **Path A（非结构化长提示词链 + 人工逐条核查幻觉与手动扒取 YouTube 爆款表格）**：月度无效搜索/API 与商业爬虫费 **$1,820.00** + 人工核验事实与拉取异常播放数据 **40.0 小时（$3,800.00）** = **$5,620.00/月**。
   - **Path B（通用 Deep Research 封装 + 无数据引用的通用选题 Prompt）**：月度工具与 API 费 **$860.00** + 人工二次求证工时 **18.0 小时（$1,710.00）** = **$2,570.00/月**。
   - **Path C（`Aeternitas` 四层认识论投研底座 + `youtube-research-skills` TubeLab MCP 实证技能组）**：月度精准检索与 MCP 调用费 **$110.00** + 人工复核工时 **4.0 小时（$380.00）** = **$490.00/月**，**每月净省 $5,130.00（降本 91.28%，年化节省 $61,560.00，工程核验工时压缩 90.00%）**。

![2026-11-14 Night Round 71 Architecture Summary](../../../assets/github-ai-radar-2026-11-14-r71-aeternitas-tubelabskills.svg)

---

## 🔍 二、灵魂拷问 Q1–Q3（从第一性原理看透架构差异）

### Q1：为什么通用“Deep Research Agent”在电力/AI 算力供应链投研里容易翻车？`Aeternitasoo/Aeternitas` 是怎么从架构上根治的？
- **通用方案的致命短板**：
  1. **认识论污染（Epistemic Blur）**：模型把“财报披露的真实资本开支（Fact）”、“分析师根据晶圆产能做的推算（Inference）”和“未证实的传闻（Hypothesis）”揉成一段通顺的话，决策者根本无法分辨哪些结论有硬证据支撑。
  2. **技能越权与自进化失控（Unbounded RSI & Privilege Creep）**：许多 Agent 框架允许动态加载外部 `SKILL.md` 或让 Agent 自动改写自身代码，导致恶意或有缺陷的技能直接获取 Shell/网络高危工具权限。
  3. **遥测静默归零（Zero-Coercion）**：当上游 API 未返回 token 或耗时指标时，普通监控直接记为 `0`，彻底扭曲成本核算。
- **`Aeternitas` 的四大硬核防线**：
  1. **四层认识论强类型分离（`Facts / Inferences / Hypotheses / Unknowns`）**：在 `Discover → Plan → Gather → Analyze → Critique → Synthesize` 全链路中，强类型 Schema 强制区分已证实事实与待验证假设，并把信息缺口显式列入 `Unknowns` 触发下一轮检索。
  2. **SHA 指纹锁定的无越权技能层（SHA-Pinned `SKILL.md`）**：所有工作流技能均记录版本号与 SHA 哈希，且技能层只能约束工作流步骤，**绝对不能突破底层 Runtime 的工具权限白名单**。
  3. **Sidecar 记忆隔离与 `FailureDiagnostics`**：`Mem0 2.2.1` 被封装在独立 Sidecar 适配器后，无法绕过主工作流直接污染真值库；`FailureDiagnostics` 严格区分 `unknown` 与 `0`。
  4. **人类门禁的受控递归自改进（Controlled RSI）**：系统仅能基于不可篡改的执行遥测（Immutable Execution Telemetry）提出提示词或路由优化建议，必须通过人工审批门禁与基准回归测试后才能晋升上线。

### Q2：做技术传播与产品视频策划时，为什么直接问 LLM“给我 10 个爆款选题”毫无实战价值？`TubeLabHQ/youtube-research-skills` 改变了什么？
- **裸调 LLM 的痛点**：LLM 训练语料滞后且没有实时播放量/粉丝基数比值（Outlier Ratio），给出的标题往往是平庸的行业老生常谈，既不知道哪个小频道靠哪个切入点实现了 10 倍异常播放（Outlier），也不知道同类竞品最近 30 天的断层爆款规律。
- **`TubeLabHQ/youtube-research-skills` 的实证闭环**：
  - 它将 `TubeLab MCP`（`https://public-api.tubelab.net/mcp`）作为唯一真值底座，把内容团队拆解为 **6 个高度专业化的 `SKILL.md`**：
    1. `content-ideation`：基于跨赛道高 Outlier 倍数视频挖掘已验证选题；
    2. `niche-research`：评估细分赛道的供需缺口、头部垄断度与爆发天花板；
    3. `channel-audit`：对任意目标频道做包装（缩略图/标题）与留存诊断；
    4. `competitor-analysis`：拆解竞品频道矩阵的选题节奏与爆款公式；
    5. `script-writer`：结合高留存黄金前 30 秒 Hook 结构撰写逐字稿；
    6. `seo-packaging`：生成高点击率标题变体、缩略图视觉 Brief 与检索标签。
  - **强制实证锚定铁律**：每一条技能输出都必须附带 **频道链接 + 视频标题 + 真实播放量 + Outlier 异常倍数 + 发布日期**，彻底杜绝无凭无据的玄学建议。

### Q3：AI Solution Architect 如何把 `Aeternitas` 与 `youtube-research-skills` 组合进日常技术洞察与内容输出流水线？
- **前店后厂协同模式**：
  - **后厂（深度硬核投研与技术尽调）**：用 `Aeternitas` 跑通 AI 算力、光模块、数据中心电力与云厂商资本开支的六阶段深潜，输出严格区分 `Facts / Inferences / Hypotheses / Unknowns` 的架构与供应链内参。
  - **前店（高传播力技术解读与 Demo 视频包装）**：将 `Aeternitas` 提炼出的核心硬核事实喂给 `youtube-research-skills`，通过 `TubeLab MCP` 检索当前科技/AI 赛道高 Outlier 倍数的切入角度、标题结构与脚本留存钩子，实现“底层事实零幻觉、外层传播有爆款数据支撑”。

---

## 🧭 三、Mermaid 选型决策树与架构协同图

```mermaid
flowchart TD
    A["AI SA 深度调研与传播任务入口"] --> B{"核心目标是底层供应链/架构事实求证，<br/>还是外部技术视频爆款实证策划？"}
    B -->|"AI 算力/电力/云供应链深度投研"| C["选用 Aeternitasoo/Aeternitas<br/>(Python 3.13.18 · 6-Stage Workflow)"]
    B -->|"YouTube/科技视频爆款选题与脚本包装"| D["选用 TubeLabHQ/youtube-research-skills<br/>(TubeLab MCP · 6 Specialized Skills)"]
    B -->|"硬核投研内参 + 爆款技术视频双轮驱动"| E["后厂 Aeternitas + 前店 youtube-research-skills"]

    C --> C1["Discover → Plan → Gather → Analyze → Critique → Synthesize"]
    C1 --> C2["四层认识论强类型分离:<br/>Facts / Inferences / Hypotheses / Unknowns"]
    C2 --> C3["SHA-Pinned SKILL.md (零越权) + Sidecar Mem0 2.2.1<br/>+ FailureDiagnostics (unknown ≠ 0) + Controlled RSI"]

    D --> D1["连接 https://public-api.tubelab.net/mcp"]
    D1 --> D2["6 大角色技能: content-ideation / niche-research /<br/>channel-audit / competitor-analysis / script-writer / seo-packaging"]
    D2 --> D3["强制携带: 频道链接 + 视频标题 + 播放量 + Outlier 倍数 + 日期"]

    E --> F["闭式 FinOps 收益: $5,620.00/月 → $490.00/月 (-91.28%)"]
```

---

## 📊 四、同类方案对比矩阵（Peer Comparison Matrix）

| 评估维度 | `Aeternitasoo/Aeternitas` | `TubeLabHQ/youtube-research-skills` | 通用开源 Deep Research（如 GPT-Researcher） | 裸调 LLM 写投研报告与视频选题 |
| :--- | :--- | :--- | :--- | :--- |
| **核心定位** | 面向电力/AI 算力/云供应链的四层认识论投研底座 | 基于 `TubeLab MCP` 实时异常数据的六角色视频调研技能组 | 通用网页摘要与长文生成 Agent | 零外部状态约束的单轮/多轮对话生成 |
| **事实与幻觉隔离机制** | **原生强制区分 `Facts / Inferences / Hypotheses / Unknowns`** | **强制每条建议绑定真实频道、播放量、Outlier 倍数与日期** | 仅附带网页 URL，事实与推论混写 | 无，极易编造数据或给出空洞套话 |
| **技能安全与权限边界** | **SHA 锁版本 `SKILL.md` + 严禁扩大运行时工具权限** | 标准只读 MCP 查询 + 6 个模块化 `SKILL.md` | 插件/工具权限边界较宽松 | 依赖人工复制粘贴 |
| **遥测诚实度与自进化** | **`FailureDiagnostics`（`unknown ≠ 0`）+ 人工门禁 `Controlled RSI`** | 实时返回 TubeLab 数据库精确播放与异常比值 | 缺失 token/成本常被静默记为 0 | 无遥测审计 |
| **月度 TCO（25 次工作流）** | **组合方案 Path C：$490.00/月（含人工复核 4.0h）** | **组合方案 Path C：$490.00/月（含人工复核 4.0h）** | Path B：$2,570.00/月（含 18.0h 复核） | Path A：$5,620.00/月（含 40.0h 核查） |

---

## 🧮 五、7-Card 定量洞察与闭式 FinOps 审计（`CLAIM-20261114-R71-AETERNITAS-TUBELABSKILLS`）

> **方法论与硬件口径声明**：本节遵循闭式 FinOps 核算规范（`workshops/github-trending-radar/evidence/trending-daily-2026-11-14-audit.json`），用于量化对比不同投研与内容实证工作流的 API/工具支出与工程核验成本；本地工作站 GPU/CPU 物理功耗标记为 `not_measured`，严禁将未知硬件指标静默归零。

| 路径方案 | 月度 API / 爬虫 / MCP 支出 (USD) | 月度工程核验工时 (Hours @ $95.00/hr) | 月度工程人力成本 (USD) | 月度总成本 TCO (USD) | 相对 Path A 净节省 (USD / %) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Path A：非结构化提示词链 + 人工逐条查证事实与手动扒取爆款视频** | `$1,820.00` | `40.0 hrs` | `$3,800.00` | **`$5,620.00`** | Baseline (`0.00%`) |
| **Path B：通用 Deep Research 封装 + 无实证引用的视频选题生成** | `$860.00` | `18.0 hrs` | `$1,710.00` | **`$2,570.00`** | `-$3,050.00` (`-54.27%`) |
| **Path C：`Aeternitas` 四层认识论底座 + `youtube-research-skills` MCP 技能组** | **`$110.00`** | **`4.0 hrs`** | **`$380.00`** | **`$490.00`** | **`-$5,130.00` (`-91.28%`)** |

- **闭式校验恒等式**：
  - $\text{Path A Total} = \$1,820.00 + 40.0 \times \$95.00 = \$1,820.00 + \$3,800.00 = \$5,620.00/\text{mo}$
  - $\text{Path B Total} = \$860.00 + 18.0 \times \$95.00 = \$860.00 + \$1,710.00 = \$2,570.00/\text{mo}$
  - $\text{Path C Total} = \$110.00 + 4.0 \times \$95.00 = \$110.00 + \$380.00 = \$490.00/\text{mo}$
  - $\text{Monthly Savings} = \$5,620.00 - \$490.00 = \$5,130.00/\text{mo}\ (-91.28\%)$，$\text{Annualized Savings} = \$61,560.00/\text{yr}$

---

## 🛠️ 六、AI SA 实战上手 Checklist（15 分钟落地验证）

1. **部署 `Aeternitasoo/Aeternitas` 并验证四层认识论输出与 `FailureDiagnostics`**：
   ```bash
   git clone https://github.com/Aeternitasoo/Aeternitas.git
   cd Aeternitas
   uv venv --python 3.13 && uv sync
   uv run pytest
   ```
   - **架构检查点**：确认 `SKILL.md` 的 SHA 指纹校验处于开启状态，检查 `Analyze` 与 `Synthesize` 阶段输出 JSON 中是否严格拆分了 `facts`、`inferences`、`hypotheses` 与 `unknowns` 四个数组，且缺失 token 统计时返回显式诊断而非 `0`。
2. **安装 `TubeLabHQ/youtube-research-skills` 并接入 `TubeLab MCP`**：
   ```bash
   npx skills add TubeLabHQ/youtube-research-skills
   claude mcp add --transport http tubelab https://public-api.tubelab.net/mcp \
     --header "Authorization: Bearer YOUR_TUBELAB_API_KEY"
   ```
   - **实证检查点**：在 Claude Code 或 Cursor 中触发 `niche-research` 与 `content-ideation` 技能，验证返回的每一条视频选题是否均包含真实频道 URL、播放量、Outlier Ratio 倍数与发布日期。
3. **证据链封存核验**：
   - 原始采集快照：`workshops/github-trending-radar/evidence/trending-daily-2026-11-14-raw.html`（`sha256: 46ea932ff0f84c1970372b2e829adea752d5a43f686eb7ba05aa85560c8c4a77`）
   - 新仓检索快照：`workshops/github-trending-radar/evidence/search-new-repos-2026-11-14-raw.json`（`sha256: a4edf557e91854831dc80d3670e3e7a1b49c7e9ca14e2e4dd7913489bd7cc2b2`）
