# E5 · 方法、历史统计与证据缺口

## 本轮方法

固定 Omarchy commit → 非截断递归 tree → 必要公开 raw blobs → 每个对象长度及 Git blob SHA-1 核验 → 带行号的静态阅读 → assertion 映射 → 中文机制分析。公开官网材料另记访问日期、最终 URL 与读取章节；不伪装成该 Omarchy commit 的依赖版本。

来源 hash只用于确认身份。测试中的 fake HOME、stub、fixtures 仅静态阅读，未执行；e3 prompt是源码模板；没有真实账号、usage sample、core、journal 或 VM log。

## 历史统计为何不报比例

**实际缺口：未完整获取固定 SHA 的祖先 commit DAG。** 本轮仅获取 target commit 元数据与 tree，没有克隆 Git 历史，没有把首页数量或 commit API 的部分分页当分母。这是范围/证据限制，不是已发生两次网络失败，也不是零 agent 使用率。

若后续单独做统计，须先明确：

| 项目 | 可复现契约 |
|---|---|
| 起点 | 固定 target commit，拒绝浮动 main |
| 分母 | 其可达祖先中约定范围的全部唯一 commit SHA；写明是否含 merge、是否日期过滤及使用 author/committer date |
| 分子 | 分母中含至少一个目标 `Co-authored-by` trailer 的唯一 commits；多个 trailer 不重复计数 |
| 分类 | 事先冻结目标 agent/harness trailer 字符串及大小写规则；不要以所有 coauthors 当 agent |
| 完整性 | 分页直到空/终止，并确认 parents traversal 无缺失；API 日期分页与完整 DAG不是天然等价 |
| 输出 | numerator、denominator、范围、获取日期、去重方法、trailer-only 限定一起给出 |
| 禁止外推 | 不叫实际 agent 使用率、代码行贡献率、效率、模型身份或独立复核通过率 |

本次 numerator/denominator 均为 **not_collected**，不是 `0`，不提供百分比。

## 非随机设计样本

`plans/backup.md:1–133` 与 `plans/dots.md:1–100` 是代表性文档，不是全部 plans 的随机样本。选择它们因为包含 revision-review 自述、明确 threat model、拒绝方案和边界。其 review claim 只作为文档声明；不声称本研究见过对应独立 reviewer session。

证据：[backup](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/plans/backup.md#L1-L23)、[dots](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/plans/dots.md#L1-L100)，`E5-11`、`E5-12`。

## 验证等级

| 等级 | 本轮能说 | 本轮不能说 |
|---|---|---|
| 源码事实 | 文件/分支/状态路径/传参在固定 bytes 中存在 | 已在目标机器正确运行 |
| 文档声明 | skill/guide/manual/官网这样描述 | 行为已被强制执行，产品在用户租户可用 |
| 测试契约（未运行） | fixture 与断言表达预期性质 | 上游测试通过、stub 实验完成 |
| 分析推断 | 从调用/数据流得出的设计解释 | 已测量因果收益或可靠性 |
| 待实验验证 | 指定可观察的验证缺口 | 用缺口默认为成功或零结果 |

最终文档检查只覆盖归档完整性、链接、JSON/CSV/来源映射及格式；不升级以上静态研究的运行等级。缺口汇总见[blockers](blockers.md)。
