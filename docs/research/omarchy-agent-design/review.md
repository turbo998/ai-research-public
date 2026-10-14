# 归档检查与待独立复核

**状态：AI辅助静态研究；待独立复核。** E4大型collector阅读委派属于研究分工，不是对最终产物的独立审查。没有运行上游tests、installers、migrations、agent、provider API或桌面/VM实验。

## 检查范围

覆盖本专题目录下的正文章节、证据索引、7 页 4:5 视觉卡片测试报告及仓库级研究索引/归属/第三方声明增量。

## 本代理归档检查

检查日期 **2026-10-12**。初次归档自查通过；检查的是以下文档/来源身份，不是运行功能。目录18个文件，加3个已有入口/来源声明，共21个本次文档增量；初次检查时未stage或commit。

| 实际检查 | 结果与范围 |
|---|---|
| 必要产物/变更边界 | 18个归档文件全部存在且无额外归档文件；仅研究索引、ATTRIBUTION、THIRD_PARTY_NOTICES另改；原根README和固定学习基线未改 |
| 本次local links | 21文件中的70个本地链接全部存在且位于worktree；0个本地fragment链接，没有把不存在的anchor样本说成已测 |
| JSON/CSV | UTF-8 JSON可解析；174条唯一assertion，正文/索引ID全部可解；JSON source/range与CSV完全对应；7份官网资料有日期/读取范围/条件 |
| 固定外链 | 117个Omarchy blob引用逐个检查完整commit、path和inclusive line范围；基线commit/tree链接另核对；不伪称已验证所有互联网外链可达 |
| 原始blob身份 | 272个获取对象重新算Git blob SHA-1、bytes与lines，与固定tree/metadata匹配；其中87个被引用对象，获取数量不是语义阅读覆盖率 |
| Root tree | 从27个根entry重建Git tree对象SHA-1，匹配commit API的root tree；recursive tree 2663条、非截断；API commit selector不是root tree SHA |
| Launcher矩阵 | 静态从实际adapter case提取14个harness、28组无/有prompt字面argv，逐参数与矩阵比较一致；没有eval或运行上游脚本 |
| 章节与图 | 六章各有问题/机制/状态/结论/复用/缺口；7个Mermaid fence及diagram type完整；本代理人工对照调用/数据流，未渲染图 |
| 术语与证据等级 | 14 harness / 3 account / 4 default usage / 3 deployed skill分开；95%切换、90%告警、80%上限、900/180/30s和provider pin对照；19条test-contract均为not_run |
| 隐私/来源边界 | 人工检查原创分析、参数/字段摘要与来源元数据；没有真实凭据/账号/core/provider返回、私人会话路径或完整上游正文；不作正式敏感信息扫描认证 |
| 格式与Git | 21文件UTF-8无BOM、LF、末尾newline、无trailing whitespace；`git diff --check`退出0（覆盖3个tracked增量），18个untracked新文件另作同等空白检查 |

执行使用既有link helper与本worktree忽略缓存中的一次性标准库检查，不新增仓库采集/验证框架，不安装依赖。初轮发现部分引用行界和Windows换行，修正后重新检查；临时helper的模块路径与adapter case范围也已修正，未把早先失败当作通过。检查输出保留在本地忽略缓存，归档此表记录最后结果，不复制完整临时源码。

静态人工自查特别保留以下差异：watcher用`_UID`而非`COREDUMP_UID`；Node `vm`不是操作系统VM；OpenClaw30轮不是总30秒；Panel有动作而非绝对strict display；stale tooltip不等于dim；Fireworks collector选一个account不等于API只支持一个账号；Claude/Grok旧cache可能仍current。自查不是独立复核，也不证明这些机制实际运行。

## 不被检查升级的状态

源码/文档/测试契约仍是静态证据；无真实CLI、skill、journal、额度、pin、sandbox或VM成功结论。共同署名全历史未采集，不报告比例。官网资料是访问时版本，不直接解释Omarchy实际binary权限。

## 署名、归档与发布

源作者/维护者归属保留；仅归档原创分析、固定链接和来源元数据，不保存整份上游原文到Git。2026-10-13 用户追加授权提交至本私有 GitHub 仓库，分类为 **Agent 与编排 → Agentic OS 与本地 Harness 集成**。授权仅改变版本化归档方式，不改变研究或复核等级；不合并、不公开发布，不创建飞书或其他外部副本。上述2026-10-12检查记录保留为初次归档快照，GitHub提交前另外复查分类、更新后的状态文字和来源映射。

### 2026-10-13 · GitHub提交前复查

本代理复查通过：21份文档、174条唯一assertion、87个引用blob、272个获取blob重新核验；既有link helper扫描270份Markdown，0错误；新增分类入口后本次本地链接为71个，固定blob链接117个。JSON/CSV/正文ID与来源范围映射一致，UTF-8/LF/空白检查及 `git diff --check` 通过。分类在索引、README与机器台账一致；私有GitHub归档授权与公开发布/合并授权分开，待独立复核和全部not_run状态保留。缓存、原始材料与本地完成回执不进入Git；7个图仍只检查fence/静态数据流，未运行或渲染。

### 2026-10-14 · 7 页 4:5 视觉测试报告与公开仓库发布复查

按用户追加要求，基于 [`turbo998/benchmark-harness-engineering`](https://github.com/turbo998/benchmark-harness-engineering) 的 7-Card 4:5 Visual Report Format（`cards.py`）新增静态契约与机制评测报告：
- 新增 [`test-report.md`](test-report.md)、[`test-report-cards.html`](test-report-cards.html)、[`evidence/test-report.json`](evidence/test-report.json)、[`evidence/test-scenarios.csv`](evidence/test-scenarios.csv)、[`evidence/test-robustness.csv`](evidence/test-robustness.csv) 与 [`evidence/test-batch-latency.csv`](evidence/test-batch-latency.csv)。
- 全部 7 张卡片坐标与百分比严格绑定 174 条断言、14 个 harness（28 条分支）、87 个引用源文件及本机 CPython 3.12.10 对固定缓存源码执行 7 次重复契约核验的实测耗时（`measured`）；上游 bash/VM/Agent 运行仍显式标注为 `not_run`。
- HTML 卡片包含严格的 `Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'`，无外部脚本、字体或网络请求；同步将脱敏后的 `docs/research/omarchy-agent-design/` 成果发布至公开分类仓库 [`turbo998/ai-research-public`](https://github.com/turbo998/ai-research-public) 的 `Agent` 分类下。
