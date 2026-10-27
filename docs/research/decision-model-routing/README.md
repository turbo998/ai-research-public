# Jev / Microsoft-Decision-1 / Strands Decider 与 Foundry 多模型路由研究

## 结论与状态

**决策模型适合闭集分类、工具/模型选择、概率门控和 rubric 评分，不替代开放式生成、复杂推理或确定性的权限控制。** 本专题比较 TypeSafe Jev、Microsoft-Decision-1 与开源 Strands Decider，设计与 Foundry 中 `gpt-5.4-mini`、`gpt-6.1-sol` 组合的应用层路由。

2026-10-10 的零推理归档、2026-10-11 的逐 attempt Entra 刷新均为历史阶段。**2026-10-14 已完成用户批准的本地 Strands + Decision-1 + mini + Sol 四模型实测：384 decision +160 e2e formal rows，全矩阵已执行。** Jev 单列 `untested_missing_external_api_key`，不计四模型分母；真实请求而非 management GET/token 已核验三个 Azure 数据面。本地服务已停止。

主要观察：Decision-1 分类 13/16、Score MAE 0.0082，闭集 network p50 多为约 0.6–0.7s；Strands 本机 CPU 分类 13/16、评分 4/16 通过，客服 2/16、RAG 16/16，不能赋予厂商 GPU 速度。客服 strong-only 13/16 优于两个 native routing 的 9/16、2/16；RAG 多臂 16/16 仍不足以证明非劣。**没有质量匹配的路由速度/成本胜出结论。** 累计真实 usage 的公开保守费率 estimate US$1.332755984，未知失败收费上界 US$0.333570816；不是已对账 invoice。分母、语言/概率/延迟/区间和原累计预算见 [Results](results.md)。

本专题为独立实测研究。总模型/API 预算为 **US$50**，包含生成、决策、推理 token、辅助调用、失败、重试及在途预留；不重置账本，不执行真实退款或生产工具动作。本地模型零 API 费不等于硬件、电力、安装或运维免费。离线 fixture、供应商报告与实际测量是不同证据。

## 阅读入口

| 文档 | 内容 |
| --- | --- |
| [Architecture](architecture.md) | 外部 Jev、Azure Decision-1、本地/边缘 Strands 三架构与同一生成池 |
| [Benchmark](benchmark.md) | 920-row 母集、调用前冻结的双语分层子集、启用/未测模型和统计契约 |
| [Results (7-Card + Scatter)](results.md) | 7-Card 结论先行结构、3 张 SVG 散点图、全矩阵分母、样本限制和复算入口 |
| [7-Card Visual Report (HTML)](visual-report.html) | 自包含 4:5 视觉报告卡组（含内联 SVG 散点图、单案例四维解剖与水平延迟对比条） |
| [7-Card Deck JSON](visual-report-deck.json) | 绑定 `analysis.json` / `records.json` SHA256 的结构化 7 卡数据 |
| [Evidence ledger](evidence.json) | 一手 URL、版本、公开价格、供应商声明与未知项 |
| [Review](review.md) | 当前离线检查、历史限定回归证据和未完成的独立复核 |
| [实验说明](../../../experiments/decision-model-routing/README.md) | Python 3.12 CLI、私有配置字段和顺序恢复命令 |

## 模型事实

| 维度 | Jev | Microsoft-Decision-1 |
| --- | --- | --- |
| 供应商/规范来源 | TypeSafe；`typesafe.ai`、`docs.typesafe.ai` | Microsoft；Foundry 文档、目录模型卡、微软发布稿 |
| 固定模型 | `jev-1.13.0`；不使用移动 alias | `Microsoft-Decision-1`，目录 version `1`；请求使用实际部署名 |
| 公开架构/训练信息 | 供应商描述 System One、并行 sampler、RLCD；未取得参数规模或基础模型的一手确认 | 微软后训练 Qwen3.5-9B；2026-10-08 发布，只提供托管 API，不分发该模型权重 |
| 原生任务 | Choice、Score、Noul | Choice、Score、Noul |
| 输入/输出 | Text-only 的文本/JSON 状态；闭集概率与决策，不生成开放式答案 | Text-only；闭集概率/评分，不提供自由文本 rationale |
| 输入边界 | 每请求 64K tokens；state + 最长单个 question 不超过 32K；state 一次读入，多问题评估 | 最大输入 32,768 tokens；须核验实际端点约束 |
| API | `POST https://api.typesafe.ai/v1/systemone`，Authorization header | `<Foundry resource root>/providers/microsoft/v1/systemone`；Entra 或 `api-key` |
| 语言 | 官方称英语是主要训练语言、当前更强；CJK 不保证等效 | 英语优化，并评估多语言；目录支持不能证明中文任务质量 |
| advertised price | US$0.042 / 1M input tokens；output free | US$0.042 / 1M input tokens；output free |
| 未核验事项 | 账户适用价格、访问、响应 usage/延迟及企业合同 | 永久版本 pin/生命周期、账户账单和生产网络/驻留；所选管理与数据面已有实际验证 |

Jev 的 `jev-latest`、`jev-preview` 在调查时指向 `jev-1.13.0`，但 alias 可移动。官方 models 页列出 100K tokens/s、80 requests/s，并明确这些限制会动态调整；它们不是本项目测得的吞吐量或 SLA。[J1]

Decision-1 目录资产为 `azureml://registries/azureml-msr/models/Microsoft-Decision-1/versions/1`。目录存在不证明所选订阅可访问；目录与用法文档的 preview/GA、SKU/区域字段存在差异，必须核验用户选定部署。原生接口相似不代表模型身份、数据合同或概率校准可互换。[M1][M2]

用户最初提供的 `jevai.net` 声明是非官方社区站，仅作为发现入口；不采用其示例 `/v1/decide`、转介 provider 或社区价格作为接入依据。

## Strands Decider：可审计的本地决策层

研究绑定官方 Apache-2.0 源码 [`8b6faa553038a59e73fa7f16c4081f8ceb21d27e`](https://github.com/strands-labs/strands-decider/tree/8b6faa553038a59e73fa7f16c4081f8ceb21d27e)，受测 Hub checkpoint revision `216d1ccb46a9e9b036eb9187b248db98480f77d4`。[S1][S2] 模型名遵循 `strands-decider-<size>-<base>-v<N>-<YYMM>`；不以移动 `latest` 当版本。

**Torso + Pointer Head。** 保留 decoder torso，丢弃 LM 文本生成头；请求编码为 `<state>...</state><question type="...">...<options>...</options></question><answer>`。末尾 answer 隐藏态作 query，各 option 末 token 隐藏态作 key，经 LayerNorm、q/k 线性投影、缩放点积、`masked_log_softmax` 和 `temperature_by_kind` 得到分布。单题无自回归解码循环；多题共享前缀路径是一次 state forward 加 suffix batch forward，不能把整个多题请求误说成仅一次 forward。[S3]

通用 `PointerHead` 默认 `dim=256`，在 2B torso 上约 1M 参数、fp32；**选定 v1 soup 的实际 `pointer_dim=768`**。三 seed head 先折叠各自 LayerNorm，再堆叠 q/k，使同一 hidden features 上的 logit 等于三 head logit 均值，**不是直接平均 q/k 参数**。LoRA 也平均 `delta W=B@A` 而非独立平均 A/B，保存为 rank-48、alpha-96 adapter，再做题型温度校准。[S2][S4]

| 家族 | 一手发布信息；不是本项目结果 |
| --- | --- |
| `2B-qwen3.5-v1-2610` | 1.9B；Qwen3.5-2B-Base，18 层 Gated DeltaNet + 6 层全注意力；246,678 行商业友好平衡 mix，gemma-4-31B-it 蒸馏，v19 KL anchor 权重 0.3，三 seed soup |
| 同一 v1 的公开 JevBench | 180/231 = 77.9%，Brier 0.280、ECE 0.072；发布方在 L4/CPU 做 release checks，不是这里的 EN/ZH 任务 |
| Gemma 4 v1：E2B / E4B / 12B / 26B-A4B | 文本 decoder；135,602 行 mix、Qwen3.5-4B teacher；公开 JevBench 分别 180 / 187 / 200 / 207 of 231；H100 中位延迟 102 / 139 / 136 / 245 ms |
| 历史 `2B-hobson-v19` / `v21` | 不作为本轮模型替代；RTX 3090 的 115 ms median / 299 ms P95 属于历史 v19，不能写成选定 v1 的实测 |

上述 training/benchmark 均为供应商自述；v1 data builders 尚未完整进入 main，所以开源推理不等于本项目已复现训练。`--vision` 可保留原生冻结约 331M ViT，最多 4 张图片；**本实验 text-only，不启用 vision**。[S5][S6]

**Shared-prefix cache。** `infer.py` 同一 state 只编码一次，`_fork_layered_cache` 复制标准 attention KV 及 DeltaNet `conv_states` / `recurrent_states`，并行编码短 question suffix。上游 2,000-token state、16 questions 的 4,086→445 ms 是 **v14 / RTX 3090** 条件，不是当前 Windows CPU v1 的测量。选项动态定义：Choice 2–255、Score 2–10；architecture 文档的 option reversal 约 0.016 分布偏移不是顺序不变性保证。有效服务窗口为 4,096；本轮使用 `--strict-window`，超长输入报错，不截断后冒充等长比较。[S3][S6]

## 原生 primitive、confidence 与任务边界

**Choice** 返回有限选项的选择及概率分布。Jev 支持 2–255 个选项；原生 `confidence` 为：

```text
confidence = (p_max - 1/n) / (1 - 1/n)
```

这是分布统计量，不是额外测得的正确率，不能跨任务、选项数或供应商直接比较。[J2][J3]

**Score** 返回有序等级的概率加权分值及 `legend`，Jev 支持 2–10 个等级。均值、MAE 验收和 top-class ECE 不同；不能套用 Choice confidence 公式。Jev Score confidence 依据分布相对众数的绝对偏差及均匀基准计算，具体定义见原始来源。[J2][J3]

**Noul** 返回 yes 概率 `noul`，没有同样的原生 confidence 字段。harness 不补造该字段；概率指标与冻结的 operational gate 分开报告。[J2][J3]

**Strands 与 Jev 的 confidence 不能混同。** Choice 同为 `(N*p_max-1)/(N-1)`；Strands Score 采用归一化标准差并补偿 `ordinal_smoothing=0.1`，而非 Jev 的众数绝对偏差定义：[S7]

```text
mu = sum(p_i * i)
sigma = sqrt(sum(p_i * (i-mu)^2))
sigma_max = (L-1)/2
sigma_floor = sqrt(ordinal_smoothing)
confidence = clamp((sigma_max-sigma)/(sigma_max-sigma_floor), 0, 1)
```

相邻等级各 0.5 不应被最大概率规则简单当作低 ordinal confidence；这仍是分布统计量，不是经验正确率或跨供应商统一置信尺度。Strands Noul 也仅返回 `noul=P(true)`，无 native confidence。adapter 保留原字段并检查公式/legend，不归一化修补无效分布。

TypeSafe 定义 RLCD 为 **reinforcement learning for calibrated decisions**。这是供应商描述的训练目标；一组预测为 0.8 的事件应约有 80% 成立，不意味着单个 0.8 输出一定可靠，也不证明本中文任务已校准。[J4]

类型约束不保证语义正确、事实正确、抗注入或业务授权。Jev 官方披露数学、日期比较、间接推理、矛盾指令、无关长状态、对抗内容和选项顺序等边界。[J5] 金额/日期、身份/所有权、tool allowlist 和副作用必须由代码控制。

## “更快”的公告证明什么

| 来源 | 供应商报告 | 不能据此得出的结论 |
| --- | --- | --- |
| TypeSafe Jev 发布材料 | 70–500 ms；特定工作流中 193.6x latency、444.6x cost 比较 | 不等于当前客户端、中文或完整 RAG/客服链路的实测；其客户端位置、短输入和概率 adapter 影响对照 |
| Decision-1 微软发布稿 | P50 约 35x faster than **GPT-6 Sol**；约 4.5x vs Quyet-1.0-Large | 对照不是 GPT-6.1 Sol；不是与 Jev-1.13.0 的直接对照 |
| 同一微软发布稿 | 36 个 public/private benchmarks、近 150K 训练盲测问题，报告最高准确率 | 不是本项目复现；不能反推未公开数据与完整实验条件 |
| 同一微软发布稿 | 八种扰动平均 1.3% decision flips；部分选项改写/反转/shuffle 报告零 flips | 不证明所有扰动、对抗输入或本中文数据没有错误 |

微软还描述 Xbox feedback 分类、Copilot grading、incident retrieval 和 Discovery replanning。这些是供应商使用场景，不是本项目已集成的组件；本次可执行范围仍仅为客服与 RAG。[J6][M3]

公平比较保留生成模型的**最快 label/score-only 对照**，另设完整概率 JSON 对照。生成概率是模型生成的估计，不是原生 logits；额外概率输出开销不能全部归因为模型架构差异。主计时使用完整可解析结果和端到端总时长，不用 TTFT 代替完整决策延迟。

## Foundry 生成池与路由边界

生成池固定 `gpt-5.4-mini` / `2026-03-17` 与 `gpt-6.1-sol` / `2026-09-29`。GPT-6.1 Sol 官方支持 Chat Completions、Responses、structured outputs 和工具；能力页列最大 input 922,000、最大 output 128,000、总 context window 1,050,000 tokens。这些不是实验请求规模或用户可用额度；harness 采用更保守的完整服务上界预留。[G1][G2]

当前聊天模型身份不是受测 API 身份。缺少部署时不能静默换模型/provider。

**主方案是应用层路由。** 调查时 managed Model Router 的支持列表未包含 Jev、Decision-1、GPT-6.1 Sol，不能宣称原生支持本生成池或任意外部 API。已有 managed Router 的补充实验必须单列真实模型池；当前没有运行该补充实验。[G3]

三条架构只替换决策 provider，保持输入、生成池、检索、权限、规则和验收一致。Strands 仅在明确配置的 `http://127.0.0.1:<port>` 接受无认证本地 HTTP；云端继续强制 HTTPS，不把云 bearer 发给本地端点。APIM、Key Vault、AI Search、Content Safety、App Insights、Foundry Evaluation 是参考组件，不是已部署或已验证集成。

## 两个具体场景

| 场景 | 决策层 | 确定性边界 | 生成/验收 |
| --- | --- | --- | --- |
| 客服工单 | department、readonly tool、证据/意图充分性、small/strong/human | signed-in、ownership、只读 allowlist；退款与人审仅模拟 | 精确事实、部门/工具/status、所需文本值；拒绝有限规则覆盖的未批准退款承诺 |
| RAG 问答 | 段落 relevance、证据充分性、small/strong/human | 冻结原创语料、检索器、证据 ID、缺证据拒答 | 同一证据生成并核对事实/引用/拒答，不依赖被路由模型自评 gold |

低置信度、信息不足、任务不适用、协议无效和服务故障分别记录。模拟复核不是实际人审；服务失败即使进入安全分支也不计模型成功。机器验收不是完备自然语言语义、安全或流畅性评估。

## 公开价格与预算

2026-10-14 重核 Decision-1、mini、Sol 的公开零售 rates；Jev 为先前官方 advertised rates，单位 USD / 1M tokens；**不是用户账户报价或账单**。最新用户授权以该公开 basis 管控本轮预算：

| 模型/Global Standard 类别 | 普通 input | cache read | cache write | output |
| --- | ---: | ---: | ---: | ---: |
| Jev-1.13.0 | 0.042 | 未核验独立类别 | 未核验独立类别 | 0 |
| Microsoft-Decision-1 | 0.042 | 未核验独立类别 | 未核验独立类别 | 0 |
| GPT-5.4-mini | 0.75 | 0.075 | 未核验独立类别 | 4.5 |
| GPT-6.1 Sol short context | 2 | 0.1 | 2.5 | 10 |
| GPT-6.1 Sol long context | 4 | 0.2 | 5 | 15 |
| 本地 Strands | 0 API fee | 0 API fee | 0 API fee | 0 API fee |

Jev 由 TypeSafe models 确认；Decision-1 由微软发布稿 Pricing 和原生零售 token meter 交叉确认。早期“input/output semantics 未知”已被发布稿的 **input 0.042 / output free** 证据更新，但账户/SKU 适用性仍未核验。Sol 由 Retail API 与 Learn normalized-token 表交叉确认；mini 使用完整 model-labelled meter。[J1][M3][P1][P2]

DataZone、GlobalStandard、Flex、priority、batch 不能混价。零售 meter 的地区列表不证明可部署；Sol `armSkuName` 的遗留 `6-astraMI` 前缀不能认证调用模型。

**GPT-6.1 short/long 的数值边界仍未核验。** 不套用其他模型阈值。受测配置必须使用覆盖所选 SKU 所有 context 类别的保守费率及证据，设置 `context_price_policy="conservative_all_contexts"`；上界不是结算价。[P3]

用户给定 `2.50 input / 15 output` 示例不等于重核的 Sol 普通 input meter：2.50 是 short cache-write 单价。实际门禁保留一手支持的 all-context maxima **4 / 0.2 / 5 / 15**，不把示例误记为官方普通 input。local zero API fee 排除硬件、电力和托管；公开费率核算不声称“实际 Azure 账单已对账”。

Reasoning 是 total output 子集，只计一次；`max_completion_tokens` / `max_output_tokens` 同时限制 reasoning、可见和格式 token。普通 input、cache read、cache write 每个 token 只分入一次类别，cache-write 适用性需核验。HTTP error、空答案或 incomplete 不证明免费；未知 usage 保留预留。Azure budget alerts 和延迟入账不是硬上限。[G2][P2][P4]

每个请求前预留输入、总输出、所有重试和在途费用；价格、身份或收费上界未经核验则不调用。不能以免费 Playground 推断正式 API 免费。

### 仅价格算术的示例

假设 decision 与 generation 都为 1,000 input tokens，generation 为 256 **total billable output tokens**；无 cache、重试、失败、judge、额外核验/折扣，且两生成分支验收质量相同：

| 项目 | 示例单次费用 |
| --- | ---: |
| Decision | US$0.000042 |
| GPT-5.4-mini | US$0.001902 |
| GPT-6.1 Sol，假定适用 short rate | US$0.004560 |

```text
C_routed = C_decision + q*C_small + (1-q)*C_strong
q_break_even = C_decision / (C_strong-C_small) = 1.5801%
```

这是价格算术，**不是省钱比例、实测路由覆盖率、速度预测或质量结论**。实际长度、升级、错误与重试会改变结果。比较 `all_batch_cost / accepted_tasks`；accepted 为零时为 NA。

## Benchmark 证据边界

数据为 EN/ZH 翻译配对的 **balanced template pilot**，不是已批准计划中全部独立案例/多轮实测。中文自然语言 criteria、rubric、question instructions 和生成语言已本地化；English JSON keys、machine IDs、enum values、品牌及单位刻意一致，因此不称纯单语输入。

模型选择 gold 需要两生成模型真实 counterfactual 输出及独立机器验收/成本，不能靠“简单/复杂”作者标签。阈值只由 calibration 选择；实测阶段和 freeze 证据以 [Results](results.md) 为准。本轮在看到任何输出前按 paired-gold-stratified policy 冻结 CPU/RPM 可执行子集；保留完整 920-row 母集。

20 个真正独立同分布 Bernoulli trials 即使零错误，one-sided 95% 上界仍为 13.91%；60 trials 为 4.87%。零事件 149 trials 才达到 2% 上界，但**不是配对 2pp non-inferiority power calculation**。本数据有模板依赖，这些仅是推断边界示例，不是数据集置信区间。

失败不从质量分母删除。概率输出覆盖率、任务/语言分层、配对模板区间、latency/usage/cost 单列。当前模板数不足证明 2pp 非劣，p95/p99 按样本门禁报告；证据不足为 inconclusive。

## 未完成事项

Jev 仍需外部安全注入 `TYPESAFE_API_KEY` 后另行检查适用合同/费用，不混入本轮四模型分母。所选 Foundry 配置和 Entra 已准备；四模型的当前执行、可能的实际失败和恢复约束见 [Results](results.md)。不在聊天/Git/报告存密钥、真实资源 ID 或内部 endpoint，不扫描其他项目或订阅。

本专题是 AI 辅助一手研究与离线设计，未完成独立人工复核。Jev 官方“不用客户请求训练”和企业 ZDR 不代表所有账户合同相同；全 Azure 也不自动证明驻留或合规，应核验所选服务、SKU、身份和合同。

## 一手来源

J/M/G 基础来源获取日期 2026-10-10；S 系列及公开价格重核为 2026-10-14。只归档原创摘要与证据，不复制第三方全文：

| ID | 来源 | 支持范围 |
| --- | --- | --- |
| J1 | [TypeSafe Models](https://docs.typesafe.ai/models) | 版本/alias、pricing、context、动态限额、语言、数据处理 |
| J2 | [TypeSafe API](https://docs.typesafe.ai/api) | request/response、primitive 与协议限制 |
| J3 | [TypeSafe Confidence](https://docs.typesafe.ai/confidence) | confidence 定义与边界 |
| J4 | [TypeSafe primer / RLCD](https://docs.typesafe.ai/introduction/machine-learning-primer) | 供应商训练目标及群体校准 |
| J5 | [Jev 1.13 Jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) | 任务/鲁棒性限制 |
| J6 | [TypeSafe Jev launch](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | 供应商评测与条件 |
| M1 | [Decision-1 usage](https://learn.microsoft.com/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision) | endpoint、auth、payload、usage、部署 |
| M2 | [Decision-1 catalog](https://ai.azure.com/catalog/models/Microsoft-Decision-1) | 固定 asset/version、模型卡；动态 HTML 可能不含完整卡 |
| M3 | [Decision-1 launch](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/) | 供应商 bench、案例、架构与 input-only 价格 |
| G1 | [Foundry models sold by Azure](https://learn.microsoft.com/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure#gpt-61) | 生成模型 ID/版本/能力 |
| G2 | [Reasoning models](https://learn.microsoft.com/azure/foundry/openai/how-to/reasoning) | 参数、output caps、reasoning 计费 |
| G3 | [Model Router](https://learn.microsoft.com/azure/foundry/openai/concepts/model-router) | managed pool 边界 |
| P1 | [Retail Prices API](https://prices.azure.com/api/retail/prices?api-version=2023-01-01-preview) | model-labelled SKU/category/region meters |
| P2 | [Normalized token pricing](https://learn.microsoft.com/azure/foundry/openai/how-to/provisioned-throughput-sizing) | Sol short/long rates 和互斥类别，不是本次吞吐测量 |
| P3 | [Azure OpenAI pricing](https://azure.microsoft.com/en-us/pricing/details/azure-openai/) | 类别；动态数字/阈值未当已核验报价 |
| P4 | [Foundry costs and budgets](https://learn.microsoft.com/azure/foundry/concepts/manage-costs) | 错误计费、延迟入账、预算告警限制 |
| S1 | [Official Strands source](https://github.com/strands-labs/strands-decider/tree/8b6faa553038a59e73fa7f16c4081f8ceb21d27e) | Apache-2.0、固定源码，而非第三方介绍 |
| S2 | [Pinned selected checkpoint](https://huggingface.co/StrandsAgents/strands-decider-2B-qwen3.5-v1-2610/tree/216d1ccb46a9e9b036eb9187b248db98480f77d4) | pointer_dim=768、rank48、temperatures、provenance、安全权重 |
| S3 | [Architecture / infer](https://github.com/strands-labs/strands-decider/blob/8b6faa553038a59e73fa7f16c4081f8ceb21d27e/docs/architecture.md) | torso、pointer、动态选项、shared cache |
| S4 | [Weight soup source](https://github.com/strands-labs/strands-decider/blob/8b6faa553038a59e73fa7f16c4081f8ceb21d27e/training/soup.py) | 平均 LoRA 更新、堆叠 head logits，不直接平均参数 |
| S5 | [Versioned supplier results](https://github.com/strands-labs/strands-decider/blob/8b6faa553038a59e73fa7f16c4081f8ceb21d27e/evaluation/results.md) | v1/Gemma/v19 的独立版本归属与训练复现限制 |
| S6 | [Inference / vision](https://github.com/strands-labs/strands-decider/blob/8b6faa553038a59e73fa7f16c4081f8ceb21d27e/docs/inference.md) | CPU、严格窗口、v14 cache timings 与可选 vision |
| S7 | [Native schema / confidence](https://github.com/strands-labs/strands-decider/blob/8b6faa553038a59e73fa7f16c4081f8ceb21d27e/src/strands_decider/schema.py) | Score 标准差公式、primitive 边界 |

公开协议/价格有一手交叉支持；项目测量与供应商结论严格分离，账户 invoice settlement 和独立人审未完成。版本、限额和费率会变化；本文不是合同保证或生产安全认证。
