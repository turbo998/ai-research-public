# 科学发现与行业场景 Harness Engineering 基准评测报告（7-Card 4:5 伴侣文档）

> **Provenance**: `anonymized_reported` (`independently_reproduced = false`；全部评测数据提取自已发表论文 `arXiv:2508.02789`、Microsoft TechCommunity ALE 官方报告及 `arXiv:2606.02618v1` 正文与补充材料 S1–S6，并由本地确定性验证器 `simulator/clio_industry_harness_verifier.py` 100% 校验复现)。
> **视觉卡片版**: [中文 7-Card 4:5 (`cards.zh.html`)](./cards.zh.html) | [English 7-Card 4:5 (`cards.html`)](./cards.html) | [English Markdown (`test-report.en.md`)](./test-report.en.md)

---

## Card 1 (`1 / 7` · `HANDS-ON · SCIENTIFIC & INDUSTRY HARNESS`) — 总览与工作台

**核心发现标题**：**CLIO 与校准遵从（Calibrated Deference）将物理科学智能体准确率推升至 75.2%，并在湿实验中完成 `+90 mV` 可逆电池分子闭环设计**

- **三大基准赛道全景对比**：
  1. **HLE Biology & Medicine ($n=152$, 无外部工具, Pass@1)**：`GPT-4.1 + CLIO` 达到 **`22.37% (34/152)`**，相比基座 `GPT-4.1`（`8.55%`）净增 **`+13.82%`（相对提升 `+161.64%`）**，超越推理模型 `o3 (high)`（`13.81%`）达 **`+61.98%`（相对）**。
  2. **Agent's Last Exam (ALE, 152 公开科研任务, 5 小时限时, Pass@1)**：基于 GitHub Copilot Base Harness + CLIO 模式 + 动态多模型路由的 Microsoft Discovery 在 **物理科学斩获 `75.2%`**（领先 Claude Code `Opus 5` `66.6%` 达 **`+8.6%`**，领先单模型 Codex `GPT-5.6 Sol` `56.9%` 达 **`+18.3%`**）。
  3. **AORFB 水系有机液流电池湿实验闭环 (`arXiv:2606.02618v1`)**：3 轮评估 17 个分子，识破预测器 **`~2.7 V`** 标度失准，发现 **Compound 3 (`-0.895 V`, `+133 mV`)**，诊断出 `pH 14` 下膦酸根–$\text{K}^+$ 离子对导致氧化波分裂，并闭环重设计出 **Compound 20 (`-0.854 V`, `+92 mV`)**，使峰值电流比 $|i_{\text{ox}}/i_{\text{red}}|$ 从 `0.18` 翻倍至 **`0.38`**。

---

## Card 2 (`2 / 7` · `SCENARIO: AORFB NEGOLYTE CLOSED-LOOP`) — 单例深度拆解

**核心发现标题**：**分级质疑 `2.7 V` 失准电位预测器，通过 3 项共识判别实验将氧化还原可逆性 $|i_{\text{ox}}/i_{\text{red}}|$ 从 `0.18` 翻倍修复至 `0.38`**

| 决策节点 | 任务类型 | 模型置信度 / 证据强度 | 动作门控 (Action Pill) | 关键量化指标与机理结论 |
| :--- | :---: | :---: | :---: | :--- |
| **1. Graphormer $E_{\text{red}}$ 标度失准审计** | `score` | `0.86` | `Confirm`（降级为软排序） | 母体分子预测 `-1.998 V` vs 提示词锚点 `+0.7 V`（偏差 **`2.698 V`**）；验证取代基位移（`+0.133 V`, `+0.258 V`）方向正确，在 Round 3 **将其移出硬门控**。 |
| **2. Compound 3 氧化波分裂机理诊断** | `choice` | `0.94` (3/3 共识 $\star$) | `Act automatically`（执行判别实验） | 宽扫速（`10–500 mV/s`）与 $[\text{OH}^-]$ 梯度（`0.1–1 M`）排除慢异构与亲核攻击；$\text{Li}^+/\text{Na}^+/\text{K}^+$ 阳离子替换证实 **双阴离子膦酸根–阳离子配位**。 |
| **3. Compound 20 苄基磺酸盐重设计** | `noul` | `0.91` | `Act automatically`（湿实验合成验证） | 替换为弱配位单阴离子 $-\text{SO}_3^-$：实测 $E_{\text{red}} = -0.854\text{ V}$（保留 **`+92 mV`** 增益），KOH 溶解度 `56.0 mM`，$|i_{\text{ox}}/i_{\text{red}}|$ 跃升至 **`0.38`（`2.11x`）**。 |

---

## Card 3 (`3 / 7` · `WHAT I TESTED`) — 全量评测矩阵与失误分析

**核心发现标题**：**6 大评测场景横跨 304 道公开基准题与 20 个湿实验分子，揭示 2 类关键未拦截边界（`✕`）**

| 场景 (SCENARIO) | 测试任务 (QUESTION / TASK) | 模型/系统表现 (MODEL ANSWER) | 门控动作 (ACTION) |
| :--- | :--- | :--- | :--- |
| **1. HLE Bio/Med ($n=152$)** | 无外部工具生物医学专家级问答 | **`22.37% (34/152)`** vs `o3 (high)` `13.81%` (`+61.98%` rel) | `Act automatically` |
| **2. ALE Physical Sciences** | 5 小时限时物理科学长程计算与推导 | **`75.2%`** vs Opus 5 `66.6%` (`+8.6%`) / Codex `56.9%` (`+18.3%`) | `Act automatically` |
| **3. ALE Life & Health Sci** | 生命科学 (`64.6%`) 与健康医学 (`61.6%`) 5h 评测 | 分别领先单模型 Codex Harness **`+3.8%`** 与 **`+4.4%`** | `Act automatically` |
| **4. AORFB 电位与溶解度筛选** | 识别 Graphormer `2.7 V` 偏移并筛选 `pH 14` 可溶分子 | 成功选出 Cmpd 3 (`-0.895 V`, `57.9 mM`) 与 Cmpd 20 (`-0.854 V`, `56.0 mM`) | `Confirm` |
| **5. ExLLM 2,500-Eval 湿实验对照** | 纯演化算法优化 `pH 7` $\log S$ 预测器 (`S1, S2, S3`) | **✕ 湿实验全部沉淀 (`< 1 mM`)**：碱性胺基在 `pH 14` 去质子化失效 | `Send to a human` |
| **6. RetroChimera 逆合成审计** | 审计 Compound 3 的逆合成路线与起始原料等价性 | **✕ CLIO 漏检母核偷换**：工具将苯并[c]噌啉偷换为喹啉（虚报 2 步 vs 实际 5 步） | `Send to a human` |

---

## Card 4 (`4 / 7` · `UNDER THE HOOD`) — 协议与评分机制

**核心发现标题**：**方程 S1–S5 多目标门控函数 $J(m)$、不确定性梯度 $\partial U/\partial t$ 与独立验证器三振熔断协议**

- **上代码块（Input Contract & Fitness Protocol）**：展示 `arXiv:2606.02618v1` 方程 S1–S5 的四维归一化得分（$s_{E_{\text{red}}}, s_{\log S}, s_{\text{SA}}, s_{\text{steps}}$）乘以硬门控指示函数 $\prod \mathbb{I}[\text{gate}_i(m)] \cdot \mathbb{I}[\text{core}(m)]$，以及校准遵从如何动态解除失准的 $\mathbb{I}[\text{gate}_{E_{\text{red}}}]$。
- **下代码块（Verifier & Telemetry Flow）**：展示 CLIO Algorithm 1 动态隐藏/注册 `Completion` $T(s)=0$、监控 $\partial U/\partial t < 0$ 与尖峰子通道派生（$\blacktriangle$），以及 Microsoft Discovery 独立验证器（`gpt-5.4`）在连续 `>=3` 次相同 `gap_fingerprints` 时触发 `Needs User Attention` 的确定性状态转移。

---

## Card 5 (`5 / 7` · `ROBUSTNESS CHECK`) — 扰动与灰盒/黑盒体制对比

**核心发现标题**：**从黑盒切换至灰盒领域知识使 CLIO Top-10 均值暴涨 `+14.7%`（`+7.4 pts`），并在 `pH 14` 真实工况下以 `57.9 mM` 完胜黑盒 `< 1 mM`**

| 评测维度 (QUESTION / ANSWER) | 原始/黑盒基线 (ORIGINAL / BLACK-BOX) | 灰盒/校准遵从体制 (GREY-BOX / CALIBRATED) | 变化幅度 (CHANGE) |
| :--- | :---: | :---: | :---: |
| **1. CLIO PMO Top-1 Score (500 evals, $n=6$)** | `0.544 ± 0.065` (Black-box) | **`0.599 ± 0.095`** (Grey-box) | **`+5.5 pts (+10.1%)`** |
| **2. CLIO (Efficiency) Top-1 Score ($n=6$)** | `0.541 ± 0.062` (Black-box) | **`0.602 ± 0.066`** (Grey-box) | **`+6.1 pts (+11.3%)`** |
| **3. CLIO PMO Mean Top-10 Score ($n=6$)** | `0.504 ± 0.059` (Black-box) | **`0.578 ± 0.103`** (Grey-box, 超越 ExLLM `0.543`) | **`+7.4 pts (+14.7%)`** |
| **4. ExLLM PMO Mean Top-10 Score ($n=6$)** | `0.525 ± 0.011` (Black-box) | `0.543 ± 0.008` (Grey-box, 增益有限) | `+1.8 pts (+3.4%)` |
| **5. `1 M KOH (pH 14)` 真实湿实验溶解度** | `ExLLM S1/S2/S3`: **`< 1.0 mM`** (不溶沉淀) | `CLIO Cmpd 3 / 20`: **`57.9 mM / 56.0 mM`** | **`+56.9 mM (>50x)`** |

---

## Card 6 (`6 / 7` · `LATENCY & SCALING`) — 推理深度与准确率-成本-时间（ACT）扩展曲线

**核心发现标题**：**认知递归（`+5.92%`）与 GraphRAG/DRIFT 归约（`+7.90%`）协同实现 `2.62x` 准确率跃升，并在 5 小时 ALE 预算内碾压单模型基线**

- **HLE Bio/Med 渐进式架构扩展（Pass@1 Accuracy）**：
  - `GPT-4.1 Base (Direct)`：`8.55%` vs `GPT-4.1 + CLIO Recursive Loop (Alg 1)`：`14.47%` vs `GPT-4.1 + CLIO Full (Alg 1 + Alg 2 GraphRAG/DRIFT)`：**`22.37%`**（相比 `o3 (high)` `13.81%` 提升 `+8.56 pts`）。
- **ALE 5 小时限时协议跨领域对比（Discovery CLIO + Multi-Model vs. Codex Single-Model）**：
  - **Physical Sciences**：**`75.2%`** vs `56.9%`（`+18.3 pts`）
  - **Life Sciences**：**`64.6%`** vs `60.8%`（`+3.8 pts`）
  - **Health & Medicine**：**`61.6%`** vs `57.2%`（`+4.4 pts`）
- **运行时限流微批次自适应**：当 `40–60` 分子并发批次因 API 限流失败时，自动降级为 **`6` 分子微批次**，将任务完成率从超时中断恢复至 `100%`。

---

## Card 7 (`7 / 7` · `MY TAKE`) — 适用场景 vs 不适用场景与工程就绪度

**核心发现标题**：**行业 Harness 必须从“盲信工具的流水线”升级为“校准遵从 + 独立验证 + 确定性结构门控”的认知系统**

- **✅ 极佳适用场景 (`Good Fit`)**：
  1. **预测器失准与分布外（OOD）科学/工业设计**：如新分子/新材料研发、半导体新工艺窗口探索、极端宏观体制下的量化风控。
  2. **三层异构目标共存的灰盒优化**：同时包含数值评分、流程步数约束与自然语言物理/合规边界（如 `pH 14` 电解液、晶圆厂跨工序污染）。
  3. **多小时至多周的异步人机协同闭环**：需要跨轮次持久化信念图（Accepted/Refuted/Open）、后悔反思与中途专家编辑信念节点的长程项目。
- **⛔ 不适用场景 (`Not For`)**：
  1. **毫秒级超低延迟在线微服务**：CLIO 多通道展开与 GraphRAG 聚类面向分钟至小时级深度决策（ACT 权衡），不适合 `<100 ms` 实时推理。
  2. **无结构不变量核验的盲目工具调用**：如 `RetroChimera` 偷换喹啉母核所示，若缺乏确定性子结构校验器（RDKit SMARTS / AST 规则），LLM 可能漏检底层工具的静默结构篡改。
  3. **纯黑盒、零领域语义的纯数值刷分**：在完全匿名的 `[0,1]` 黑盒函数上，轻量级演化算法（`ExLLM`）在单点极值搜索上比复杂认知循环更直接。
