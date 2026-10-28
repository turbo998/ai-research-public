# Personal agents：五款产品、公开评测与统一测试协议

> 🌐 **Language / 语言切换**: **[🇨🇳 中文版 (README.md)](README.md)** | **[🇬🇧 English (README.en.md)](README.en.md)** | **[↩ 返回研究索引 (`../index.md`)](../index.md)**

> **Executive Summary / 核心结论概览**：
> Personal Agent 的范式跃迁不在于“更会聊天”，而在于**持续后台运行、跨应用主动交付、保留长期记忆上下文，并在触及高风险边界时把决定权交回用户**。本专题对比了 **Meta Muse、xAI Grok Bot、OpenAI dot/dots、Google Gemini Spark、Instinct** 五款代表性产品，并设计了包含 **18 个原创合成案例** 的统一测试协议（[`benchmark.md`](benchmark.md) / [`cases.json`](cases.json)）：
> 1. **模型分数不等于产品成功率**：五款产品的执行边界由各自的宿主机环境（独立 Secure VM vs 共享云端电脑 vs 本地电脑挂载）、连接器授权范围与安全哨兵（如 Muse Sentinel）决定，不能用底层 LLM 跑分替代产品级评测。
> 2. **角色分离不等于安全隔离**：如 `Grok Bot` 支持多命名 Bot 群聊协作，但同账户下共享电脑与插件权限；`Gemini Spark` 面向个人 Google 账号，不可混同于企业级 Gemini 的 IAM 治理；`Instinct` 主打短信/语音入口，但断开连接不等于删除历史数据。

![Personal Agents 五款产品架构与治理对比图](assets/overview.svg)

**研究 cutoff：2026-10-11；这是公开资料研究，不是产品实测。** 检索跨过北京时间午夜，实际读取日期为 2026-10-11 至 2026-10-12，详见[证据台账](evidence.json)。官网为读取时的 live version，不声称还原 cutoff 当日的全部历史网页。未采用明确晚于 cutoff 的发布事件；后续变更不能自动回填为当日状态。

主对象为 **Meta Muse、Grok Bot、OpenAI dot/dots、Google Gemini Spark、Instinct**。Google 的企业 Gemini agent 另列区别，不增加第六个主对象。中文分析保留 English terminology；本文的场景选择是研究建议，厂商承诺与外部观察分别标注。

**发布范围：本专题的原创分析、必要公开来源链接和合成测试设计。** 独立另进程 AI 事实/契约审阅及修正复核完成，无开放实质问题；公开候选另做隐私审查，状态见[审阅记录](review.md)。未产品实测、未付费、未登录私人账户、未部署、未创建真实自动化。[统一 benchmark 协议](benchmark.md)和[18 个原创合成案例](cases.json)均为 `not_executed`。

## 先看结论

Personal agent 的关键变化不是“更会聊天”，而是**持续运行、跨应用交付、保留上下文，并在需要时把决定交回用户**。但五款产品不是同一套 harness，也不拥有相同权限：同一底层模型的成绩不能代表消费产品的成功率。

- **生活目标与日常事务：Muse** 的 Goals/Ideas、WhatsApp、独立 Secure VM 和 Sentinel 是鲜明组合；US rollout、付费额度及未兑现路线图要分开。[S1–S4]
- **多人式分工：Grok Bot** 已有多个 named Bots、群聊与异步交接。账户内 Bots 共用电脑和插件，不能把角色分离误当安全隔离；模型选择由产品管理，不是只用 Grok。[S5–S8]
- **持续知识工作：dot** 深度复用 ChatGPT、插件、记忆及可选本地电脑。主动研究只读，不等于整个 dot 只读；自定义规则也不是可以取消内置安全要求。[S9–S10]
- **Google 数据与工作流：Gemini Spark** 的 Tasks/Skills/Schedules 与 Workspace 操作较完整。消费者帮助文档要求个人账号，不能把企业 Gemini 的身份、治理和套餐搬过来。[S11–S14]
- **不想增加界面：Instinct** 官方定位为 text/call 的生活助理。消息/电话入口清晰，但公开价目、地域及系统保证较薄；条款授权广，**断开连接不等于删除数据，benchmark 使用另有许可门槛**。[S15–S17]

**没有本库的五方同口径分数榜。** 已找到 Muse/Instinct 的第三方产品级数据和 Instinct 的黑箱记忆观察，不应写成“没有公开 benchmark”；但版本、任务样本、适配器和原始回执不足以支持五方排名。[S18–S22]

## 名称与产品身份

| 对象 | 本轮核验的身份 | 时间与不能混同的对象 |
|---|---|---|
| Muse by Meta | Meta Newsroom 的 personal AI agent；Muse Spark 是底层模型名 | 公告 2026-09-08、修改 2026-09-30；不是把模型 Muse Spark 单独列为产品。[S1] |
| Grok Bot by xAI | x.ai 公告及 Cursor 产品/帮助文档共同描述的 always-on AI teammates | 公告 2026-08-11；读取页面品牌为 SpaceXSI。只记录当前来源，不据此推断法人沿革、收购或成立时间。[S5–S8] |
| OpenAI dots / dot | URL 使用 introducing-dots；中文正文及界面称单个 **dot** | 公告 2026-09-29；首个 personal dot 与企业 specialist dot 的 pilot 不同。[S9] |
| Google Gemini Spark | Gemini Apps 的 24/7 personal AI agent | 不是一般 Gemini chat 的 scheduled actions，也不是企业 Gemini agent。当前 overview 未给明确发布日期，本轮不臆造 launch date。[S11–S12] |
| Instinct | instinct.com；条款运营方 Spear Street Technology, Inc. d/b/a Instinct | 2026-08-26 是 Terms 修订日，**不是 launch date**；不与其他同名项目混同。[S15–S16] |

## 五产品特点矩阵

以下均为官方描述，**不是本库验证功能已可用**。例子表达厂商定位，不表示任务成功率。

| 产品 | 定位与入口 | 主动性 / 长期上下文 | 工具、电脑与应用 | 交付与适合场景 | 不适合直接托付 |
|---|---|---|---|---|---|
| Muse | 生活目标、事务执行；iOS/Android/web/WhatsApp；当前官网还有 Mac | Goals、Ideas、事件/日程后台推进；跨对话记忆，Memory files 可读改 | 专属 Linux VM、browser/terminal、可写工具；Meta/第三方 connectors；Mac 入口描述本地文件/apps/tabs | 购物与行程草案、账单整理、家庭日历、长期目标追踪；Artifacts 不限文本 | 未核验地域/额度下的持续承诺；未经确认的支付、外发、重要合同；把 Confidential VM 当已经交付。[S1–S4] |
| Grok Bot | 工作伙伴团队；macOS/iOS；账户级插件，群聊与多个 Bots | per-Bot 偏好/事实/摘要；routines、交接、后台工作 | 账户共享持久云电脑，各 Bot screen 非安全边界；plugins/CLI/browser，支持接管；产品动态路由模型 | 研究→草稿→review、运营台账、bug reproduction、跨应用协作 | 不同敏感身份放在同一账户 Bots；把 Enterprise network/audit/model 控制泛化到个人或 Teams。[S5–S8] |
| dot | ChatGPT 内的持续助手；desktop/web 创建，mobile 后续交谈；Slack/Teams，SMS 有限 beta | ChatGPT memory + 自己的 memory；跨渠道；主动只读研究 + scheduled tasks | 自己的 cloud computer/browser；插件生态；可选本地电脑（默认关闭），可启动 Codex/工作任务 | 长期研究、内容制作、应用修复 PR、随新证据更新文档 | 把“超过 4000 应用”理解为本账户全部可用；把只读 proactive research 等同执行任务只读；依赖尚未交付的多-dot 团队。[S9–S10] |
| Gemini Spark | Gemini Apps 里的 Tasks/Skills/Schedules；web/mobile/Mac | Personal Intelligence、chats、skills；时间/事件 triggers；具体持久记忆内部实现未核验 | Gmail/Calendar/Drive/Docs/Sheets/Slides 等，custom apps；remote browser/computer、local Chrome 与 Mac connected folders | 邮件整理、Sheets 台账、跨 Google apps 的计划与周期摘要 | 在任务串输入密码/支付信息；敏感无人监督 schedules；混同本地 browser 与关机可继续的 remote 工作。[S11–S13] |
| Instinct | 不增加新交流界面的生活 assistant；text/call，官网导向 web login | 官方 privacy 描述基于上下文/既往交互个性化；持久记忆及主动 triggers 有第三方观察，非官方架构保证 | 官方称可像人使用 phone/computer；Google Workspace APIs 和其他 Connected Services 有政策依据 | 低门槛委托日常事务；电话/消息交互；先从合成/非敏感资料和可审查草稿开始 | 未确认的重大支付、不可逆行动；将 black-box 推测视为产品保证；未经许可运行 benchmark。[S15–S17,S19,S22] |

### 发布、价格、地域与资格

**套餐费不等于 agent 总成本**：要分别看基础订阅、包含工作量、重置周期、on-demand、第三方购买/短信和工具任务用量。以下不使用媒体价目代替官方核验。

| 产品 | 本轮可核验的 access / release 状态 | 价格及额度边界 | 地域、资格与未核验项 |
|---|---|---|---|
| Muse | 2026-09-08 公告 US rollout；当前官网有 Mac 和 Small Business 内容，但不据此宣布全球开放 | 官方 FAQ：free with usage limit；到限额可等刷新或订阅。具体美元价格、token 数、刷新周期本轮未核验 | US 为公告的明确地域；其他地区/年龄/付费方案细节未核验。AI glasses、1Password、Confidential VM 均不能由初始路线图认定已交付。[S1,S4] |
| Grok Bot | 公告 beta；**当前 plans** 比公告更广：paid Cursor individual/Teams，linked SuperGrok/Plus/Heavy/X Premium+，self-serve Grok Business seat；Enterprise 联系客户团队 | 不需 standalone subscription；weekly usage，超额可经 Cursor on-demand 收费。**Teams on-demand 默认开启；monthly limit 不是运行中 hard stop，已有任务可能超限完成。** Cursor+linked grant 不叠加，取较高额度；free trial 为 credit 且有 7-day window | macOS/iOS；SuperGrok Lite 不包含。地域/年龄和美元价目未核验。云电脑在 US **不等于**只有 US 用户，也不等于已获 US-only residency 合约。[S5–S7] |
| dot | Pro、Business Premium 逐步 rollout；Enterprise/Edu/Healthcare beta 需 admin enable，初始关闭 | 首个 dot 包含；有深度工作额度。对话不计 ChatGPT allowance，但其启动的 Codex/工作任务照常计费/计量；更高首月额度不是永久无限 | Pro 排除 EEA/UK/Switzerland；Business Premium 为 ChatGPT supported regions。SMS 仅 US Pro 限量 beta，不适用 Business/Enterprise；不能移动端创建，mobile web 不支持。基础套餐金额未核验。[S9–S10] |
| Gemini Spark | help/privacy 称 early experimental/beta；个人账号，Pro/Ultra、18+、Keep Activity on | 基于算力的用量限制，request 数与复杂度影响消耗；最多同时 15 tasks，满时 schedules 不运行。当前美元订阅金额未核验 | help：Gemini supported regions，排除 EEA/Nigeria/Switzerland/UK；work/school account 暂不支持。overview 又称 select business users，存在口径差异，**不能保证某企业账号可用**。[S11–S13] |
| Instinct | 官网有 Text Instinct 入口；本轮未在官方材料核验 public GA / invite 规则 | Terms 有 paid services，USD fees、价格可改、通常不退款；没有在已读官方页面核验具体金额，不能推断永久免费 | Terms 18+，不保证特定设备/地域可用；invite/private beta/free 由媒体或 hands-on 报告描述，非本轮官方 access 保证。[S15–S18] |

### Google 企业 Gemini agent：单列区别

2026-10-08 的 Google Cloud Gemini at Work 材料描述 Workspace 内个人协助、proactive delegation 和具独立 Workspace account 的 coworker agent，以及 agent identity、RBAC、audit、Agent Sandbox/Gateway 等组织治理。[S14] **这些是企业产品/治理宣称，不是 Spark 消费套餐能力、可用性或 privacy 的证据。** “Gemini Agent by Google”在本报告的主比较中明确解释为 Gemini Spark；企业材料只作为边界说明，不纳入五方 benchmark 分母，也不移用其客户性能数字。

## 审批、隐私与删除：先问“停止后留下什么”

| 产品 | 官方审批设计 | 训练、凭据与删除 | 不能推断的保证 |
|---|---|---|---|
| Muse | Sentinel 独立于 runtime cell；connector/egress 可 allow/deny/ask。结构化 approval 可一次/任务/时间范围等，具体 grant 受 scope 检查 | credential surrogate，agent 不看真实秘密；可 opt out interaction training；不进入 Meta ad systems；可要求 forget、读改 memory files | 不是所有动作必逐次人工批准；安全 blog 承认会出错。Secure VM 仍可按需向推理/telemetry 发有限数据；不是已经“连 Meta 都无法访问”的 Confidential VM。forget 不证明备份/全账号彻底删除。[S1–S3] |
| Grok Bot | Auto Review 为独立 review model，覆盖 shell/plugin/computer/trigger/delegation，可放行、要求批准、拒绝；Ask first personal rules 优先；Enterprise 可 enforce | Privacy Mode enabled 时 customer data 不训练；OAuth tokens 在 backend，browser session/files 在共享电脑。Delete Bot 不删除电脑文件和登录；需另清理/撤销 | Auto Review 不覆盖每个 side effect（如 memory writes）；Enterprise controls 不自动属于 Teams。当前 serving mix 可变，team model allowlist 不 govern Grok Bot；读取未延伸到全部 subprocessor 合约。[S6,S8] |
| dot | auto-review + Custom Rules；安全要求持续有效；改密码等需本人。Proactive research 使用不能外发/修改/控制电脑的只读工具 | Business/Enterprise/Edu 默认内容不改进模型；personal 可控制；主动研究/自己的笔记不直接训练，但进入 eligible conversations/tasks 后仍可能依设置使用。disconnect 不删已取得信息；reset 删除 dot、conversations、memory、schedules | 不把宣布的 password protection 泛化为全部网站；reset 不是对所有外部应用、ChatGPT memory、备份或历史已训练模型的删除证明。SMS 经第三方，慎传敏感信息。[S9–S10] |
| Gemini Spark | 某些外发、修改、购买、表单要求 confirmation；可 Stop/Take control；Chrome auto browse 每个 browsing task 先确认 | Spark 要求 Keep Activity；remote cookies/文件可能含敏感数据并按 Privacy Notice 处理。settings 可清理 browser/computer；关闭 Spark 不删 tasks/threads/schedules/已写文件；本地 Chrome 数据另清理 | **private Google Tasks bulk operations 可无需确认**，不是“每次写入必批准”。Keep Activity 与普通聊天的 off 模式不能混用。官网说设备关闭仍可后台，help 另说 device-off schedules 不运行：保留差异，不承诺所有离线 trigger 可用。[S11–S13] |
| Instinct | Terms 广泛授权 Connected Service actions、交易/承诺；可有 safeguards，但不保证防止错误，用户须独立监控。hands-on approval 不等于契约性一律确认 | Materials 可用于训练；opt-out 仅未来训练且有 safety-review 例外；Vault 不训练。Google Workspace API data 不训练、不用于广告，处理方限服务用途。disconnect 不自动删除 indexed data，需 workspace 请求删除/删除账号 | 非“默认全部不训练”，非“断开即忘记”。条款称 records 也可能不准确；没有本轮独立验证 retention/backups/物理删除。Terms §6 restrict benchmarking，未来实测先取许可。[S16–S17,S22] |

审批设计的好坏不能只数弹窗。合理的交付是“已准备、待批准、未发送/未购买”，**因正确停在边界而未产生现实交易不是失败**；反之，最终任务完成但未经批准越权，不应得高分。人类接管要区分审批、缺信息、身份校验和真正返工。

## 场景选择与试用门槛

| 场景 | 优先了解 | 选择依据与最小门槛 |
|---|---|---|
| 非敏感公开研究 → 对比 → 草稿 → 审阅 | dot；需多角色交接时 Grok Bot | 要 source IDs、实际交付文件、失败清单；外发/发布关闭。不是以“24/7”推断证据正确 |
| Gmail/Drive/Sheets 为工作中心的个人账号 | Gemini Spark | 先确认 supported region/Keep Activity 和 connector scopes；优先 private draft，不直接改共享资料 |
| 长期生活目标、家庭排期、购物候选 | Muse | 确认 US/access；支付、外发、地址分享逐任务批准；不用 Always allow 替代具体预算 |
| 简短消息/电话委托，拒绝学习新界面 | Instinct | 先明确 access、费用、训练 opt-out/Vault 和 indexed-data deletion；敏感判断/最终交易本人处理 |
| 销售/运营/工程多个角色并行 | Grok Bot | 一个 accountable owner，避免重复操作；同账户共享环境，不放彼此不能接触的凭据 |
| 组织员工身份、审计与政策治理 | 企业 Gemini / 各 Enterprise 产品另行评估 | 不按本消费者矩阵采购；需合同、region、data residency、admin controls 与实际验证 |

本轮**不授权任何试用**。未来执行先核验当时条款、账户资格、预算、个人数据同意及 benchmark 许可；尤其 Instinct 不能因为有公开 API/消息入口就视为允许评测。任何“统一适配器”不得暗加长期记忆、定时器、外部代理或替产品完成任务。

## 公开 benchmark：有什么、能说明什么

| 证据 | 类型与公开数字/观察 | 可解释范围 | 不可作出的结论 |
|---|---|---|---|
| Personal Agent Bench 当前展示 scorecard | **产品级第三方报告**；测量日期为 **2026-09-22**，page last verified 2026-10-09 不是测量日期。Instinct 43%，95% interval 36–50%，159 scored tasks；Muse 19%，13–25%，90。Grok 行未公布值 | stateful simulated errands；Muse adapter 修正后数字，另 83 tasks re-run。**这些 rates 尚未按9月28日至10月4日变更后的规则重评分**；不同任务样本非严格同口径，最新 aggregate batches 未公开。运营方 **Zentor 开发 agent 软件，主动披露商业利害并排除自身产品** | 不把 43/19 当五方榜；不把不等样本、删去 infra failures 的 rate 当全尝试成功率；不能将新方法说明误归为旧数字的执行版本；不是本库重算。[S20–S21] |
| 同站 older filtered batch | Instinct 52%，45–61%，380 attempts/114 tasks；Muse 40%，33–46%，637/114；测于 2026-09-22，旧 builds/旧规则 | 可显示“换批次/过滤/规则，数字会变”；站点说约 5600 attempts 经八项过滤，adapter/未到 exam 排除也影响判断 | 不能拼接 current row 与旧 114-task row。若把未到 exam 计为产品拒绝，站点说 Muse 约 24%；排除解释是研究问题，不是可忽略噪声。[S20] |
| 同站公开回执 | runs 索引称仅 Instinct，单 batch **7 runs**；方法为七类可复位 worlds，final state grading；money 只到 unpaid prepared order | 有局部可检查证据；方法区分 approval、takeover、infra、timeout、capability、wrong state，非单总分 | 7 run 不核验 159-task aggregate，也不证明所有 adapter、版本、预算/repeats 相同；本轮没读取完整运行轨迹/仓库。[S21–S22] |
| Supermemory 的 Instinct memory 文章 | 2026-09-20；black-box/vibe-test。作者报告 explicit recall 较好、implicit personalization 不稳、forgetting 不完整 | 产品表面观察与问题线索；作者明确未见源码、部分机制未知 | 不把 model 自述的 git/files/周期当内部架构认证；作者为 memory vendor founder，有商业利害；没有标准重复/分母与五方测试。[S19] |
| 厂商 launch/demos / dogfooding | Muse 安全架构、Grok 内部团队用例、dot 早期案例、Spark task 示例、Instinct 官网 | 定位、目标能力与控制设计的一手声明 | 不是随机样本，不是独立 task success rate，不将多倍效率 testimonial 写入分数。[S1–S17] |
| Every 产品比较 | 有来源和 hands-on/black-box 链接，自己声明未在全部产品跑相同 jobs | 发现候选来源与交叉检查；本文事实回到官方原文 | 不是其表格价格/工具数/排名都已经一手核验。[S18] |

本轮在 official product/help/policy、一次有界跨产品搜索及上表候选直接读取范围内，**未核验到 dot/Gemini Spark 的可复算产品级 benchmark，Grok Bot 只核验到 scorecard 的未公布行**。这是检索覆盖限制，**不是断言相关评测不存在**。首次搜索摘要声称没有产品 benchmark，已被直接网页证据纠正，未作为结论来源。

### GAIA / OSWorld / τ-bench 不等于消费产品成绩

| Framework | 已核验版本与用途 | 如何借鉴，不如何移植 |
|---|---|---|
| GAIA | arXiv `2311.12983v1`，2023-11-21；466 questions，166 developer / 300 held-out；短答案 normalized match，工具/浏览/多模态推理 | 借鉴答案与来源可检查；不覆盖发消息/预约等 consequential actions。原研究有可用 API 时三次取平均，不是 pass^3。数据 gated/有 anti-resharing，未下载。[B1–B2] |
| OSWorld / OSWorld-Verified | 原发布 2024-04-11，369 desktop tasks；Verified 2025-07-28 修复 300+ feedback/issues（不是新增 300 tasks）。固定仓库 commit 见台账 | 借鉴 initial state + execution-based evaluator；OS/VM/apps/fonts、website、observation/action space、max steps 均需固定。旧 OSWorld 与 Verified 条件不同，不平移分数。[B3–B5] |
| τ-bench / τ² / τ³ | 原 τ 2024-06-17，115 retail + 50 airline；τ² 2025-06-09 加 dual-control telecom。当前 tau2 仓库已称 τ³，`banking_knowledge` <1.0.1 与 ≥1.0.1 不可比较 | 借鉴 user simulator、policy、final DB、consistency。原 reward=1 仍可能漏 policy violation；pass^k（全成功）≠ pass@k（至少一成功）。runner 对 infra errors 的版本变化必须披露。[B6–B9] |

不引用模型/framework 数字填产品空格。论文、代码、dataset、VM images/外部 assets 各有权利边界：OSWorld root code Apache-2.0，τ repositories MIT；不推断整套第三方数据获同样授权。本库仅保存原创分析和链接，案例不是上游题目翻译或改写。

## 来源入口与阅读边界

[evidence.json](evidence.json)逐条记录 S1–S22、B1–B9 的 publisher、URL、实际读取方法/范围、时间、支持 claims、限制及稳定版本。重点入口：

| ID | 来源 |
|---|---|
| S1–S4 | [Meta launch](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) · [security](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) · [design](https://introducing.muse.ai/) · [FAQ](https://ai.meta.com/muse/) |
| S5–S8 | [Grok launch](https://x.ai/news/introducing-grok-bot) · [Cursor security](https://cursor.com/docs/grok-bot/security) · [plans](https://cursor.com/help/grok-bot/plans) · [work](https://cursor.com/docs/grok-bot/work) |
| S9–S10 | [OpenAI launch](https://openai.com/zh-Hans-CN/index/introducing-dots/) · [getting started](https://help.openai.com/zh-hans-cn/articles/20001530-getting-started-with-your-dot) |
| S11–S14 | [Spark overview](https://gemini.google/overview/agent/spark/) · [help](https://support.google.com/gemini/answer/17094507?hl=en) · [privacy](https://support.google.com/gemini/answer/13594961) · [enterprise](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026) |
| S15–S17 | [Instinct home](https://instinct.com/) · [Terms](https://instinct.com/terms) · [privacy](https://instinct.com/privacy-policy) |
| S18–S22 | [Every](https://every.to/personal-agents-comparison) · [memory report](https://supermemory.ai/blog/reverse-engineering-instinct-memory/) · [scorecard](https://personalagentbench.com/) · [exam](https://personalagentbench.com/how-the-exam-works/) · [runs](https://personalagentbench.com/runs/) |
| B1–B9 | [GAIA](https://arxiv.org/abs/2311.12983) · [OSWorld pinned README](https://github.com/xlang-ai/OSWorld/blob/b138d348256078fa634fc3b73567a7337c793e6b/README.md) · [Verified](https://xlang.ai/blog/osworld-verified) · [τ pinned README](https://github.com/sierra-research/tau-bench/blob/59a200c6d575d595120f1cb70fea53cef0632f6b/README.md) · [successor pinned README](https://github.com/sierra-research/tau2-bench/blob/4ce7c0397c1eb65c9bbe59aeacfe1ca44a1cd699/README.md) |

不发布官网原文/媒体、产品内部指令、第三方源码、私人运行轨迹、凭据或客户材料。AI 辅助整理与独立 AI 审阅不是法律意见、人工认证或产品认证；本专题属于 [Agent 类独立研究](../index.md#agent)，不代表已有产品实验或其他分类已完成。
