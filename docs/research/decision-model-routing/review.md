# 审查与归档边界

**本专题已做 AI 辅助事实/实现自查、202 个全库离线测试，并执行用户批准的四模型真实 pilot。** 精确阶段与结果见 [Results](results.md)，不将实测等同于独立人工审查、完整独立代码审查、账单对账或生产安全认证。Jev 仍明确未测待 key。

## 范围与证据

| 项目 | 状态与限定 |
| --- | --- |
| 一手事实 | TypeSafe、Microsoft Learn/模型卡/发布稿/Retail API、固定 Apache-2.0 Strands 源码与 Hub/base snapshots；vendor claims 单列 |
| 定价 | 用户授权核验的公开 Standard Global estimate；Sol numeric boundary 未猜，2.50 是 short cache-write 不是 ordinary input，采用全 context 上界；不是 account invoice |
| 数据与机器 gold | 原创 SYNTHETIC，EN/ZH 自然语言 criteria/instructions 本地化；机器 ID/order/gold 保持；gold 无独立人审 |
| 当前源验证 | LF code aggregate `d1fe177b6951b03e10db89fdbfc92b21fadc9a8d01f55d125d58c753b7bd73c6`；202 full / 118 topic tests通过；freeze后的实验Python不再变更 |
| 历史外部 AI probes | 协调会话独立 scratch 的 11 probes，绑定初始归档 `7cea27c...`，全部通过；2026-10-10T03:49:35Z，不覆盖新增 Entra 代码，不是 full/human review |
| Entra / local HTTP | 每 attempt/retry 五分钟刷新、scope/失败停发/轮换 redaction仍有效；新增本地数值回环、none auth、源/权重/health验证；未给本地发送云凭据 |
| 真实执行 | 新源码20/20 smoke；384 decision +160 e2e calibration、两split oracle与全部544个formal jobs完成，未尝试0；原账本累计1179模型调用/1307transport attempts；数值见Results及analysis |
| 生产组件/副作用 | 本扩展未改云资源/RBAC/网络/安全、未取key；仅用户批准的local runtime与模型请求，无automation/APIM/AI Search/agents/真实退款 |
| 发布 | 仅私有研究分支；不公开、不改 visibility/default branch、不 merge |

限定 probes 是初始 LF 归档的历史证明，取代更早 9-test/CRLF 记录；新增 Entra 代码依赖当前单独重跑的离线测试，不能将旧 hash 说成当前证明。可提交摘要只有公开/合成状态与源 hash，不归档 coordinator 私人路径、会话或凭据。

Strands runtime为ARM64主机上的隔离x64CPU环境，不是厂商RTX3090/H100。固定v1实际pointer_dim768/stacked-logit soup，不能沿用通用dim256或把历史v19的115/299ms赋给本轮。installed源码bytes、selected文件公开manifest与base safetensors hash核验；权重/venv/raw receipts保持忽略，不加入Git。

## 已检查的核心风险

协议解析拒绝重复 key、非有限数值、缺字段、无效概率/Score，不把非法分布修补为成功。固定Strands源码逐字段4dp serialization使用半单位数学区间验证，并保留原值；不归一化或用计算值替换原score/confidence。其它provider不借用该容差。原生vendor confidence保留但不当正确率；Noul不补造confidence。LLM label-only/probability分开，当前聊天不作为受测模型。

首次real smoke16/20失败及费用保留为历史：两个Strands响应因旧parser忽略显示舍入而误拒绝，两个mini自报Score与分布均值不一致是真实输出错误。仅在formal freeze前修正parser/为两个生成对照同等澄清算术，新20/20 smoke绑定新hash。新增回归证明合法舍入保留原数值、超界错误仍拒绝、LLM不一致Score不修补、失败smoke非零退出；118 topic tests还覆盖全部冻结决策输入的native wire与LLM prompt option order一致。

预算按 hard ceilings 预留全部 attempts/in-flight，用持久 SQLite 保留 unknown charges；reported ceiling 被推翻时保留观察费用并锁定，重启不恢复假余额。reasoning/output 与 cache categories 不双计；配置价格缺失时暂停。该设计依赖真实费率/上界，不能事后担保错误假设下的 provider 账单。

显式 `azure_identity` 只绑定所选 subscription/tenant/Cognitive Services audience；load/preflight不获取凭据。每次HTTP attempt前刷新检查，失败不回退旧token/key；TypeSafe静态bearer不变。CLI输出仅内存，轮换凭据在发送前加入raw/public（含base64）脱敏，无runtime monkey-patching。真实HTTP200已证明本轮三个Azure数据面可用；scoped role列表查询失败不是缺少权限证据，也未依其建议创建SP或扩权。

退款 acceptance 曾漏掉 EN/ZH 金额插入句，现有拒绝与 safe/negated regressions 关闭。schema、事实 ID/值、引用、部门/工具、权限、最小语言字符检查不等于完整自由文本语义/安全评估。Native router 错误与权限拒绝不能被正确 generator reply 隐藏；服务失败进入复核也仍记失败。

分母区分 API attempted、authentication-blocked、HTTP success、usable、schema valid、known gold、accepted、probability、safe/unsafe。未发送的认证失败仍保留失败/预算证据，但不冒充 API attempt。无 accepted 时成本 NA；模型选择缺 counterfactual gold 时未知，不猜复杂度。Score ECE 按 modal class 而不是 MAE acceptance；gate 报告用实际执行阈值。

同模板/翻译/source 不跨 calibration/test；本 pilot 不满足 2pp 非劣数量门槛、不启用速度/成本胜出。完整 calibration 才可选阈值；formal phase 一次性 claim，不能挑选重跑；partial 自动续跑尚未实现。

## 归档 allowlist

允许：本专题研究文档（含 `visual-report.html`、`visual-report-deck.json` 与 `charts/*.svg` 散点图）、实验Python/contract、空private-config example、原始原创data/manifest、审阅的脱敏真实records/analysis/validation摘要、专题tests、根README/research index导航。

禁止：`.cache`、private-config/env、预算数据库、真实endpoint/resource/deployment ID、认证值、私人会话/客户资料、供应商全文、raw live payload、model weights/venv、无关source catalog/lock/coverage修改。public model IDs、通用角色标签、公开retail meter ID和public model文件hash不是私人云资源。

公开归档保持与未公开材料隔离。中文研究文档延续仓库现有风格。导航链接、数据 hashes 与 allowlist 在 commit 前离线检查；remote SHA 和指定文件可取在 push 后核验。

## 仍需后续复核

Jev单列待外部key及适用访问/费用检查，不能在现有phase上重跑或自动激活。账户invoice未对账、实际推理地域不由resource region推出、本机CPU与云端不是硬件匹配实验；尾延迟和2pp非劣按预注册样本门槛保持NA/inconclusive。公开estimate不担保税费、折扣或未核验合同。local服务在本轮依赖结束后停止，不留watcher/automation。

真实结果显示客服 mini-only 2/16、strong-only 13/16、Decision-1 9/16、Strands 2/16；Strands CPU评分仅4/16通过，两原生router的small gates均不可行。没有隐藏这些不利结果或在test后调整gate。五个mini正式Score schema失败全部在ZH；native/LLM概率、失败分母和machine接受标准独立记录。全部配对比较仍inconclusive，不将RAG有限样本全正确或零ECE宣传为总体质量保证。

累计usage estimate US$1.332755984、unknown upper US$0.333570816、in-flight0；public conservative basis而非invoice settlement。所有run records的费用与原ledger一致，旧smoke未删除。owned local server已停止、回环8000无listener；未留后台automation。

人工需要复核数据语义/翻译、退款及其他自由文本风险、oracle/rubric 外推、模板依赖与正式 power design。生产前另审查数据合同、ZDR/驻留、RBAC/秘密生命周期和治理组件。**离线 tests 或私有归档不能代替这些工作。**
