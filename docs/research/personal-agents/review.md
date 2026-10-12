# 审阅、修正与公开发布边界

## 事实与测试契约审阅

成稿由不同于作者和 framework 研究者的独立另进程 AI reviewer 进行只读检查，随后核对修正。审阅覆盖五产品正文、31 条证据、测试协议、18 个案例及 72 条断言、引用和归属边界。最终结论为**可接受，无开放实质问题**；这不是独立人工审阅、法律意见、安全认证或产品测试通过。

实际检索跨 2026-10-11 至 2026-10-12，研究 cutoff 仍为 2026-10-11。本次公开整理不声称重新检索了产品页面，也不把 live 页面当作 cutoff 当日的不可变快照。来源的发布日期、评测日期、规则版本与读取日期分别保留。

关键直接复核包括 Meta 公告及安全设计、x.ai/Cursor access 与 security/work、OpenAI 公告及 help、Google Spark overview/help/privacy 及企业文章发布日期、Instinct Terms/privacy、Personal Agent Bench 方法/scorecard/公开 runs 索引、Supermemory 观察、GAIA/τ 论文选段、OSWorld/Verified 及 τ successor 文档和三份真实 Git commit object。具体读取范围与限制见 [evidence.json](evidence.json)。

| 严重度 | 发现 | 修正与关闭 |
|---|---|---|
| Medium | Grok monthly limit 可能被误读为 hard spending cap | 明确 Teams on-demand 默认开启；运行中任务可超 monthly limit 完成；拟议测试仍要求合法额度与 on-demand off |
| Medium | benchmark page last verified 与测量/规则日期混淆 | 当前展示数字测于 2026-09-22，未按 9 月 28 日至 10 月 4 日新规则重评分；保留样本不等与 aggregate 回执缺失限制 |
| Medium | gold 类型推导 schema 会泄露 null 答案 | 18 题独立 schema，可空字段用完整 union；禁止 gold-derived const/default/examples |
| Medium | whole-input 会泄露未来事件、故障与评测脚本 | 当前 prompt/turn 与 schema 显式投影；fixtures 按 scope 读取，其余只留评测端；PA18 禁止内容不进入初始 context |
| Low | benchmark publisher 商业利害未披露 | 明确 Zentor 开发 agent 软件、披露利害并排除自身产品；不据此篡改分数 |
| Medium（修正复核） | PA15 初始 prompt 预告取消事件 | 初始只请求 tick10 提醒，tick6 才发送取消及不恢复指令；独立 reviewer 确认关闭 |

作者自查另修正 PA12：允许至多 3 次同 id/key 的幂等重试，timeout 后核对最终状态，避免惩罚合法恢复。该自查不替代独立 reviewer。

## 公开候选隐私审查

**状态：新的独立另进程 AI 已完整审查实际八文件候选；未发现开放的隐私或发布阻塞问题。** 该进程不同于先前事实 reviewer，逐字检查全部 Markdown/JSON、25 个本地链接/锚点和 47 个公开 HTTPS URL。公开目录只含本专题五文件、研究索引、根 README 和 ATTRIBUTION。仅发布原创分析、必要公开来源链接与合成案例；不附未公开资料、上游全文/媒体、私有仓库链接、内部路径、会话标识、进程秒级时间或旧 Git 历史。

公开准备阶段已移除内部 reviewer 标识及精确过程时间，重写仅与本研究有关的索引/归属/审阅记录，添加合成数据声明。研究 cutoff、来源 publication/modified/measurement/commit 日期和必要公开作者归属不作匿名化替换，以免破坏事实与署名。

## 本公开包的验证范围

验证只针对实际公开八文件：JSON 重复键、31 source IDs、引用闭包、18 cases 六维各 3、72 assertions 与 expected state、独立 schemas/nullable unions、`not_executed` 状态、UTF-8/LF、本地链接和文件 allowlist，均通过。schema 检查覆盖此文件实际使用的关键字子集，不声称通用 JSON Schema 标准认证。额外比对确保来源事实/日期及完整案例契约未因脱敏改变。

独立隐私审查完整检查私有上下文、凭据样式、邮件/域名及全部链接，无开放问题。Git 发布门禁另核验单个无父 initial commit、仅公开 handle/noreply 身份、无私有会话 trailer 和八文件 tree；远端公开性及固定 commit 匿名读取/hash 比对属于发布核验，不以正文静态检查代替。

不将其他项目的测试、生成器或来源覆盖率写为此公开库的通过证据。本库没有产品运行成绩；协议为设计，world/harness 尚未实现。

## 限制

隐私审查与静态规则不能证明绝对无泄露或未来输入安全。公开网页为 live versions；部分价格/发布日期未核验，最新评测原始 aggregate 未核验。Muse FAQ 的精确 refresh 文本来自作者实际浏览，独立 reviewer 只复核相关公告与订阅边界，不冒称逐字独立复核。全部价目、retention/subprocessor 合约、完整 papers/evaluators/licenses、gated GAIA 题目及运行轨迹未穷尽读取。

Instinct benchmark 许可门槛仍有效。研究发布不授权产品实测、现实交易、私人账户访问或部署。
