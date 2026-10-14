# E4 · 状态、collector与UI契约

**源码事实及未运行测试契约。** 路径是上游Linux语义，非本研究机器状态；没有真实JSON sample或credentials。

## Registry与home

| 位置/字段 | 合约 | Assertion |
|---|---|---|
| state root | XDG_STATE_HOME优先，否则~/.local/state；omarchy/agents/accounts与usage | E4-55 |
| registry | active、switch、threshold、alert、accounts | E4-03 |
| account | id、label、home、primary；身份摘要accountId/email/org/plan | E4-56 |
| provider defaults | `.claude`/`.codex`/`.grok`，primary路径不从provider override推导 | E4-01、E4-05 |
| exec env | 非空CLAUDE_CONFIG_DIR/CODEX_HOME/GROK_HOME优先 | E4-08 |
| Omarchy pin | OMARCHY_AGENT_CLAUDE_HOME/CODEX_HOME/GROK_HOME的provider-specific完整名；存在的空pin代表Main | E4-09 |
| account home | credentials独立，settings/history/skills等provider配置的项目shared；不是强隔离 | E4-06、E4-07 |
| publish | 账号目录0700、registry0600、provider flock、临时文件后replace | E4-04 |
| lifecycle | pending login → identity验证/去重 →正式home；use仅新session，rename不搬home，remove检查运行home | E4-10、E4-11、E4-58、E4-59 |

pin完整变量名分别为 `OMARCHY_AGENT_CLAUDE_HOME`、`OMARCHY_AGENT_CODEX_HOME`、`OMARCHY_AGENT_GROK_HOME`；不要误写成通用 `OMARCHY_AGENT_HOME` 或修改 `$HOME`。系统mise dispatcher见[E4-57源配置](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/etc/mise/conf.d/omarchy-agent-accounts.toml#L1-L13)。

## 大型 collector 函数定位

| Provider | 真实来源/schema函数 | Cache/failure/window上下文 | 读取边界 |
|---|---|---|---|
| Claude | transcript解析173–274；stats/cache/history458–519；pi/omp528–638；opencode643–728；credential/plan803–869；OAuth/scoped limits924–1031 | scan/index133–171,387–452；limits1036–1143；multi-account1150–1209；main1215–1286 | 不把头注释当唯一证据 |
| Codex | CLI解析105–147；pi/omp/opencode241–433；native435–536；windows802–823；credits852–863；RPC882–982 | scan/cache539–748；multi-account989–1028；main1030–1077 | app-server会运行CLI，仅读源码不探测 |
| Grok | native86–150；plan173–183；credits186–195,246–259 | scan154–164,294–314；credential/cache/failure198–263；multi-account/main317–361 | refreshable旧cache的live不是fresh请求 |
| Fireworks | local stats映射58–176；key179–294；日期296–316；HTTP334–359；discovery376–388；billing394–413；balance415–486 | main489–554，无cache；force/limits-only接口兼容535–554 | 账户级usage，20页上限，估算明确标记 |

每个区间的固定SHA/path/hash由[assertion-index.csv](assertion-index.csv)与[evidence.json](../evidence.json)连接。范围是阅读/证据定位，不是测试覆盖率。

## 四套 freshness 不能混为一个

| 项目 | Claude | Codex | Grok | Fireworks |
|---|---|---|---|---|
| 活动scan | 普通20s，limits-only900s；append/index与timezone检查；force重扫 | 普通20s，limits-only900s；schema/date/file cache；incomplete不cache | 普通重扫，limits-only900s且校验home/date | 每次API账户统计 |
| 限额probe | 成功15s复用；force绕过 | 每次app-server；无持久limits fallback | 正常60s复用；force绕过 | 没有rate-limit windows |
| 网络失败 | 保留cache，900s内可current；transport可retryAdvised | 空limits + status/help | 可保留cache；401/403/auth状态单独处理 | valid unavailable record或保留token但balance unavailable |
| 过期credential | paused/expired与auth区别；保留cache语义 | CLI自己判定/刷新，未运行 | refreshable在规定30天判据内可沿用旧cache并roll weekly | 没有此订阅window状态 |
| 时间戳 | limitsFetchedAt独立于updatedAt | 当前无同等limits fetchedAt | fetchedAt可对应旧probe | updatedAt不是完整余额审计 |

证据：`E4-22`、`E4-26`、`E4-31`、`E4-35`、`E4-60`–`E4-68`。limits `percent`通常统一为0–1，但Claude对payload尺度做heuristic判断；这个统一值不是provider政策一致的证明。

## 发布JSON与Panel消费

| 字段组 | 主要字段 | 消费及限制 |
|---|---|---|
| envelope | schemaVersion/id/name/updatedAt/ready | 本版本updater+QML没有完整schema/version校验 |
| status | usageStatusText/authHelpText/tierLabel | unavailable、paused、Waiting for auth、Sign-in expired不是同态 |
| limits | label/percent/resetsAt/可选title | 过期显示0；title优先；取最高window；不用模型名猜窗口 |
| freshness | limitsStale/limitsFetchedAt；accounts的stale/fetchedAt | stale只hover年龄，不以dim证明stale；updatedAt不是measurement |
| accounts | accounts/accountSwitch | active与各账号limits；Panel有use/mode等动作 |
| reset credits | resetCredits.available/nextExpiresAt | Codex available credits |
| balance | remaining/funded/spent/currency/estimated | Fireworks真实余额与估算分开 |
| stats/scope | today*/recentDays/total*/activeDates/modelUsage/scope/hasPromptStats/hasLocalStats | account scope不计prompt次数；本地与账户统计分开 |

证据：`E4-36`–`E4-41`、`E4-68`–`E4-71`。

updater验证成功exit、非空stdout与jq可解析，临时文件mv后再autoswitch。valid error-state JSON会替换旧record，collector异常则留旧文件；后续策略仍可能读旧record。FileView watch加updater退出reload；bad JSON清空，未变文本保留对象。不是完整schema或identity authenticity保证。

## Autoswitch状态机

| 阶段 | 条件/动作 |
|---|---|
| refresh | QML默认900s，下限30；Panel open limits-only，manual force |
| 加快 | 多账号active达到min(80%,threshold−15点)；周期min(180, configured interval) |
| 计算peak | 最大未reset窗口；全部已reset为0，unknown不是0 |
| admission | active >= threshold（默认95，范围50–100）才开始 |
| 候选 | known peak < threshold；Waiting for auth排除，stale不完全排除 |
| ranking | 接近threshold−15点 → stale → usage → next reset，依次升序 |
| manual | 可点击建议，不修改active |
| auto | 写active；新session采用，旧sessionpin不漂移；重采provider |
| 去重/恢复 | alert去重；healthy active清alert，不因旧账号reset自动切回 |
| exhausted | 全部known且超阈值才报；每账号恢复取阻塞窗口最晚reset，账号间再取最早 |

证据：`E4-12`–`E4-18`、`E4-37`、`E4-72`、`E4-73`。

## 未运行fixtures

账号路由/explicit override与session pin（E4-42）、fresh/stale排序（E4-43）、Claude scoped/fraction（E4-44）、Codex cumulative去重（E4-45）、Grokrefreshable expiry/weekly reset（E4-46）、Fireworks余额fallback（E4-47）、updater filtering/nonJSON（E4-48）、QMLreload/badJSON恢复（E4-49）、stale tooltip（E4-50）。它们是合成fixture/断言，不是真实provider响应，**没有VM、stub或上游测试运行结果**。
