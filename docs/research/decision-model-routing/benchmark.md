# Benchmark 契约：四模型 paired stratified pilot

**2026-10-14 用户批准四模型实测；20/20 新源码 smoke 通过，03:52:15Z 按 exact contract/code/config hashes 冻结，完整 calibration 后于06:09:50Z完成全部544个formal logical jobs。** 实际数值和失败见 [Results](results.md)。这是翻译配对、一轮、少模板的 pilot，不冒充大规模独立案例实验；Jev 明确未测。

规范文件为 [`contract.json`](../../../experiments/decision-model-routing/contract.json)、[`manifest.json`](../../../experiments/decision-model-routing/data/manifest.json)和[runner 说明](../../../experiments/decision-model-routing/README.md)。US$50 不因数据规模、重试或辅助评估而扩额；不看模型结果后缩小失败分母。

## 数据、gold 与切分

原创合成数据共 **920 rows、460 bilingual semantic base cases、52 task/scenario template clusters、10 shared global source families**。全部为 SYNTHETIC；不使用第三方数据集、客户资料或私人文本。

| 每个任务/场景 | calibration rows / base cases / templates | test rows / base cases / templates |
| --- | --- | --- |
| classification | 80 / 40 / 4 | 120 / 60 / 6 |
| selection | 80 / 40 / 4 | 120 / 60 / 6 |
| gating | 80 / 40 / 4 | 120 / 60 / 6 |
| scoring | 80 / 40 / 4 | 120 / 60 / 6 |
| support | 20 / 10 / 2 | 40 / 20 / 4 |
| rag | 20 / 10 / 2 | 40 / 20 / 4 |

每格 EN/ZH rows 各半。同一 base case 翻译对、模板改写和 source family 不跨 calibration/test。跨任务的不同 cluster 可以共享一个 source family，不能把 52 clusters 池化成 52 独立来源。重复/翻译不扩大独立样本数。

### 本轮预先冻结的 CPU/RPM 子集

保留以上完整母集及原始 hashes。Windows ARM64 主机通过隔离 x64 PyTorch CPU 运行指定 1.9B 模型；Azure 生成部署有低 RPM/TPM 配额。本轮在**任何模型输出之前**采用 `paired-gold-stratified-round-robin`、seed `20261014`，每任务/场景、每 split 选 **8 base cases / 16 rows**；四决策任务各 32 rows，两场景各 32 rows，总计 **192 个选定输入 rows**。

选择按 gold stratum（selection 再分 model/tool）保留语义类型，在 strata 内轮转模板，整对保留 EN/ZH；不读取模型输出、拒答、费用或正确率来删选案例。`freeze.json` / run manifest 固定 exact case IDs；test/calibration 不重叠，selection 的子任务数量按实际 frozen IDs 报告，不称每个子任务标签频次完全相等。母集并未被重写成 192 rows。

中文的自然语言 criteria、等级、gating labels、routing question instructions、LLM wrapper 和生成语言均已本地化；machine IDs、JSON schema/keys、enum、单位与品牌刻意保持相同、选项顺序相同。**这是匹配本地化提示，不是纯中文-only 字节输入。** 400 条中文决策 criteria 及两个 e2e question graph 有自动回归检查。

| 任务 | 独立 gold | 指标 |
| --- | --- | --- |
| 分类 | 合成主意图/部门，含 unknown/域外/无主次 | Accuracy、固定标签 Macro-F1、confusion、失败与覆盖率 |
| 工具/模型选择 | 只读工具权限规则；模型 gold 初始 null，必须由实际两生成模型 counterfactual 输出形成 | tool applicability、错误分支、route quality/cost regret |
| 概率门控 | 明确事实支持/未批准承诺的合成 bool | binary Brier、NLL、ECE、误放行/误拦截、risk-coverage |
| 质量/相关性评分 | 四个确定性事实支持比例的五级 rubric | MAE、Spearman、top-class ECE、阈值行为 |
| support / rag | 精确 status/department/tool、事实值、证据位置、权限、有限承诺检查 | 机器 acceptance、escalation、latency、accepted 单位成本 |

Gold 为 AI 编写的确定性构造，**未经独立人工复核**。selection 中 100 rows 是模型选择，另 100 是工具选择；前者不能拿作者复杂度标签当 oracle。两生成调用任一个不可用时 gold 保持 null/inconclusive；都可用但都不通过验收才设 human。counterfactual 使用实际验收与 usage-based 成本，不含免费/虚构模型输出。

自由文本只检查结构化事实、所需值提及、引用、状态、权限、有限 EN/ZH 退款承诺及最小语言字符存在性；不完整评估语义、流畅性、所有幻觉或注入。金额/日期运算和副作用由代码处理。

## 对照和调用计划

| 类型 | 固定对照臂 |
| --- | --- |
| 全能力槽位 | 七个决策臂、六个 e2e 臂；包括待 key 的 Jev |
| 本轮决策六臂 | Strands-native、Decision-1-native、mini-label、mini-probability、Sol-label、Sol-probability |
| 本轮 e2e 五臂 | small-only、strong-only、deterministic rule、Strands routing、Decision-1 routing |

启用模型固定 `StrandsAgents/strands-decider-2B-qwen3.5-v1-2610` checkpoint `216d1ccb46a9e9b036eb9187b248db98480f77d4`、`Microsoft-Decision-1` version `1`、`gpt-5.4-mini` version `2026-03-17`、`gpt-6.1-sol` version `2026-09-29`。`jev-1.13.0` 仅保留接入槽，标记 `untested_missing_external_api_key`，不进入四模型分母。不采用未批准 provider、不用 Copilot 会话答案、不默换生成池。native primitive 与 LLM 生成概率分开，label-only 不补造概率/calibration。

全部主实验同 state、rubric、gold、生成参数和固定检索；随机 seed `20261010`，配对 jobs 随机交错，一轮、顺序低并发 `1`，无应用 response cache。原生 prompt-cache usage 如有返回则记录。

| 阶段 | 计划逻辑任务/调用，不含重试 |
| --- | ---: |
| 独立 smoke | 20 calls：12 decision 请求 + 8 generation 请求 |
| calibration decision | 4 × 16 × 6 = 384 logical rows |
| calibration e2e | 2 × 16 × 5 = 160 logical rows |
| test decision | 4 × 16 × 6 = 384 logical rows |
| test e2e | 2 × 16 × 5 = 160 logical rows |
| 独立 generator oracle | 每 split 4 个 model-selection rows × 2；合计 16 generation calls |
| 额外消融 | 本 bounded CPU pilot cap=0，不另花 API 费用或借供应商图表补结果 |

e2e native arm 每任务最多一 decision 和一 generation；policy-only 可无模型调用。logical rows 不是 API attempts 或 accepted 数。所有阶段、旧失败 smoke 和重试共享同一原始累计 US$50 账本。冻结时投影含 safety factor `2` 为 **US$8.098310208**，只是规划，不替代 atomic reservations。先前 16/20 smoke 的错误与费用保留：原 Strands parser 未考虑供应商 4dp display rounding；mini 两个生成概率 Score 与自报分布均值不一致。修正前者、为两个生成对照同时澄清 Score 算术后，新的 20/20 smoke 绑定新代码；未修补模型输出或删除旧账单。

## 激活与参数冻结

先限定配置/凭据，再对**三个选定部署**做只读 account/deployment GET 核验（management API `2024-10-01`），每次显式指定其订阅，不扫描其他资源。预检需完整 identity、region/SKU、credential/env、适用 pricing、cache applicability 和 hard token ceilings；配置只能位于忽略的 `.cache\decision-model-routing`。可选 `azure_identity` 只接受明确的现有 CLI scope；offline preflight 不获取 token，不能证明 data-plane RBAC。

smoke 成功且 identity/schema/usage 可用后，freeze 绑定 code、dataset、corpus、contract、config hashes、启用模型/禁用原因、exact selected case IDs 和 smoke receipt。此次用户已授权配置和运行，因此记录该 approved contract SHA；不是从较早“确认部署”推断推理批准。正式 test 还需完整 calibration matrix 和被冻结 thresholds。本地 `/health`、checkpoint/base revision、strict window 与 installed source hashes 单独核验；health 本身没有推理。

候选固定值：Score absolute error `<=0.5`；calibration 初始 evidence gate `0.5`、small route gate `0.8`。各 probability arm 只在 calibration 上按**经验误放行 <=1%**选择覆盖率最大的阈值；无可行阈值或无 unsafe gold 时自动 abstain。label-only 使用自身 bool，不伪造概率。test 报告使用实际执行的 frozen gate，而不是事后固定成 0.5。

Formal phase 使用一次性 `phase-claims` 防止重复/选择性重跑。**没有自动 crash-resume 的未完成 phase 续跑**；发生中断保留原证据、未知费用与未尝试数，不删账本/claims 再跑。干净起点的顺序命令见[实验说明](../../../experiments/decision-model-routing/README.md#私有配置与真实恢复)。

## 严格协议、计时与证据

schema/类型、问题键、选项集、有限数值、概率 [0,1]/总和、Score 均值/legend、返回模型版本必须符合契约；重复 JSON key、NaN/overflow、无效分布不能修补/归一化成成功。LLM probabilities 是生成估计，不是 logits；native confidence 保留但不称 measured correctness。

**固定 Strands 源码 `infer._to_answer` 独立 `round(...,4)` 每个概率、score、confidence。** 按每项半单位 `0.00005` 对总和、均值和 confidence 的合法序列化误差作区间检查；例如 sum=0.9999 可合法，但 0.99 仍拒绝。Score sigma/confidence 检查使用保守 pre-rounding interval。**保持原始返回值，不 renormalize、不重算替换 score/confidence，也不把容差用于其它供应商。** Brier/NLL/ECE 使用 as-displayed 概率；显示为 0 的 gold mass 可能是舍入，不声称已知道隐藏 logits 的 NLL。native confidence 尺度差异详见研究 README。

客户端 Python 3.12、标准库 HTTP/1.1；云端 TLS，本地只有显式数值回环例外。服务允许时复用连接；实际 socket reuse 单列。本机 Windows ARM64、12 logical CPUs、31.6 GiB RAM、无 CUDA；隔离 x64 CPython 3.12.10 / torch 2.14.1+cpu、6 CPU threads，所在地不披露。资源区域/SKU 不推断物理推理位置；首个连接不称服务端 cold start。最多 2 attempts、socket timeout 300s，非严格 end-to-end SLA。

`network_elapsed_ms` 从 HTTP POST 到读完响应计时；`elapsed_ms` 另含 attempt 内认证/解析和 pacing，不能称模型计算时间。Strands response `latency_ms` 单独保存为 server-reported latency，不与 client network 或厂商 GPU 数字混称。Azure mini/Sol 每角色至少 7s 请求间隔，Decision-1 至少 1.1s；rate wait 单列并包含在 logical/e2e 时间，网络成功 attempt 单列。e2e 另含固定检索、mock/验收和分支。TTFT 未采集，未代理完整决策速度；跨本机 CPU/托管服务不是硬件匹配实验。

Entra headers 在每次 HTTP attempt 前刷新检查；剩余有效期 `<=300s` 则显式 scoped CLI 取新 token，重试也不复用即将过期 token。首次预留前的认证准备不属于 HTTP elapsed；retry 内的刷新会进入 logical-call elapsed，不能混称模型计算时间。轮换 token 先登记到脱敏表，取得失败暂停且不发送请求；本轮在真实 Azure 调用路径使用该机制，未另测刷新性能或生产身份保证。

本地原始证据包含每次请求/响应、credential-redacted exact bytes、native fields、requested/responded identity、call/attempt ID、usage、延迟、retry/error、estimate/unknown-cost。提交时隐藏真实 endpoint/deployment/resource ID/认证；semantic route labels 不被身份脱敏破坏。读取 evidence 时核验 raw hashes 和 case/arm/phase/repeat，拒绝 mock/replay 混入 live 分析。

## 分母与统计

报告分别列：planned/unattempted logical jobs、started tasks、API attempts、authentication-blocked attempts、HTTP success、usable calls、schema valid、known gold、accepted、probability cases、safe/unsafe gold、escalation。进入 HTTP transport 才标记 `http_attempted=true`；认证刷新失败的未发送记录单列，不计为 API attempts，保守预算保留不表示供应商收费。失败留在任务质量分母；无概率不加入 calibration 分母且不补值。gate 的服务失败按 abstain，但仍在 safe/unsafe gold 分母。accepted=0 的单位成本为 NA。

多类 Brier 使用 sum-of-squares；binary gating 另报通常的二元 Brier。NLL gold mass=0 记录 infinite-case 数，JSON NLL 为 null，epsilon-clipped 值仅辅助。ECE 为 10 个 equal-width bins：Choice selected class、Noul p>=0.5、Score modal level，**不是 MAE 通过即 class correct**。risk-coverage 是有限机器验收风险，不是生产安全保证。

配对 acceptance difference 按 template cluster bootstrap 2,000 次、seed `20261010`。候选 noninferiority margin `2pp`，只有完整 pairing、至少 30 templates 和 200 base cases 才能通过证据数量门槛；本轮每场景仅 4 test templates / 8 base cases，**预先为 inconclusive，不启用速度/成本胜出声明**。不能以这些数量门槛代替正式 power calculation。

p50 描述性报告；p95 要求至少 40 base cases，p99 至少 500，且仍披露模板依赖。因此本 e2e 场景不报告可靠 p95/p99；翻译/重复不会使门槛变大。未启用额外 McNemar 或容量结论。

即使 20 或 60 个真正 i.i.d. trials 零错误，one-sided 95% Bernoulli upper bound 为 13.91% 或 4.87%。本模板依赖数据不适用该独立假设；149 个零事件的 2% 示例不是配对非劣 power。校准零误放行不能声称总体误放行 <=1%。

## US$50 费用门禁

[`budget.py`](../../../experiments/decision-model-routing/budget.py) 使用 Decimal 和 SQLite 原子累计预留：输入按适用类别最大费率 × hard ceiling；total output（含 reasoning）按 verified cap 预留；一次逻辑调用在首个 attempt 前预留全部重试，在途请求也计入。

Reasoning 不额外双计；ordinary/cache-read/cache-write 输入互斥。无 cache breakdown 时保守计费。失败即使 HTTP 401/429/5xx 也不能自动视为免费，unknown usage 保留最坏预留；已明确未使用的 retry 才释放。reported usage 超过 ceiling 保留观察费用并 halt，重启不能消除锁。错费率/上界不能事后保证 provider 账单，必须人工核对，不自动继续。

用户授权以核验的公开 Standard Global 单价核算，而非等待账户报价：Decision-1 **input 0.042 / output free**、mini 0.75 / 4.5；Sol 不猜 short/long boundary，使用 4 / 0.2 / 5 / 15 的 per-category maxima。输入 cache-write breakdown 未返回时保守计费，不把用户给的 2.50 cache-write 示例误作统一 ordinary input。Strands 明确 `local_self_hosted_zero_api_fee`，不计硬件/电力。详见 [pricing evidence](evidence.json)。这不是 invoice-settled “实际 Azure 账单”；`invoice_settled_usd=null`。

## 单独的限定消融

代码保留 fan-out/options/context/connection/order/concurrency 接入能力，**本轮明确 cap=0，未运行这些消融**。上游 GPU cache/speed 数字仅在 supplier research 中引用，不放入本项目 live results。不把原始多个问题共享前缀这一实现机制当作已测的服务器容量。

## 当前 hash

| 工件 | SHA256 |
| --- | --- |
| cases.jsonl | `a445498d5a09673e6990dcc325845312c20edb600d6f1ab3627149cf76ebec6c` |
| corpus.json | `0c80929f2ab49689543508a6af8a9756822d8c96952a71761bbad070819ef97b` |
| contract.json | `fe062d33c0bafa037d71379c293ede59010a01a6444bc77232836f9e824bcbb1` |
| harness code aggregate / live freeze | `d1fe177b6951b03e10db89fdbfc92b21fadc9a8d01f55d125d58c753b7bd73c6` |

中文提示修正早于任何模型调用；本扩展保留 cases/corpus/data.py hashes，更新 contract/code 并在新 smoke 后冻结。首次失败 smoke 的旧 code hash 与 raw/费用仍留存，不冒充当前 parser 证据。源码/契约采用 LF；版本/配置不得在 formal 输出后悄改。精确执行状态见 [Results](results.md)。
