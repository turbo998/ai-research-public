# LocalJev 独立 AI 复核记录

## 对象、方法与版本绑定

- 日期：2026-09-27。
- 对象：[研究正文](README.md)、[证据台账](evidence.json)及[研究索引](../index.md)。
- 上游 commit：`3f23e36e1a3bff46c7e83e8e3781d3512bc82021`。
- 上游 tree：`95c4a7409e1f78ef036594a71c1b83d3fd380344`，不是 commit SHA 的复用。
- 方法：协调研究者综合一次有界源码研究后，调用**新的独立上下文 research AI** 检查论断与出处；复核者没有阅读前一研究子任务报告，而是直接检查源文件、元数据与必要一手网页。不是独立人工认证，也不是运行验证或漏洞审计。

| 版本 | README SHA-256 | evidence.json SHA-256 |
|---|---|---|
| 独立初审实际读取的工作稿 | `6edb0ce8d41157674a4f28b6107a8b8d0dcad30d10d8c6b36151d6e8adecf1aa` | `56614f57fa364cfe7fd6ad393c03ce247809414068f5a070d4a41fe7bc3dcb25` |
| 修订后的归档字节 | `3c607f65ad34176984140bb07333aadb5dfb358cc7584555972b12a0a3b9f844` | `9fb1f4aeb7bd72fdeae42a9ea04d9c84e0168936a81109ed97469311f9f0232a` |

哈希按实际 UTF-8 文件字节计算。工作稿正文原为 CRLF；归档版按仓库规则统一 LF，同时修正下列出处。**初审哈希不代表复核者审过最终字节**；最终绑定及定向一致性检查由协调研究者完成，没有声称第二次独立复审。

## 初审结论与修订

实际返回结论为 **REVISIONS_REQUIRED**：未发现核心技术结论或十行结果表的实质错误，但需修正出处定位；另有一项台账清晰度建议。

| 编号 | 复核发现 | 实际处理 |
|---|---|---|
| R1a · 必修 | C16 将 cache-busting 指向 `run.ts:124-128`，实际是遥测初始化，不能支持缓存前缀论断 | 改为 `118-121` 的前缀构造及 `165` 的样例/条件 reference；保留“源码请求策略，不证明真实缓存状态”的边界 |
| R1b · 必修 | 约 23.5 分钟数值正确，但原 S16 从 manifest:1585 开始，漏掉 line 3 的 startedAt | 正文新增 S24 定位 `manifest:1-3`，与 S16 内的结束时间对应；C16 同步增加该范围，明确只是作者工件时间戳差 |
| R2 · 澄清 | `citation_index` 为空，而实际已有 23 条 claim 映射，易误认编号索引已完成 | 修正 CRLF 导致的解析遗漏，生成 S/O/W 编号到 URL 的索引；没有用“文件范围内”替代论断支持检查 |

以上修订未改动模型结果数值、概率公式、API 行为或评测分母。当前状态是**独立初审完成、指出的问题已由协调研究者修订并定向检查**，不是独立审查者对最终字节给出的 PASS。

## 复核者实际确认了什么

- 概率先检查有限 `[0,1]` 分量、精确长度与正总和，再归一化；choice 并列、score 索引期望、自然对数逆熵及无统一舍入的描述有源码支持。
- choice 2–128、score 2–10、四别名单上游模型、队列包含活跃、semaphore 在 body 解析前释放、按尝试 timeout，以及 HTTP/envelope/内容纠错的分层描述正确。
- 测试静态意图计数为 Engine 5、server 4、eval 10；没有把它们写成执行通过。
- 独立投影 summary 后，十行任务准确率、宏平均、MAE、p50/p95 和失败数与正文展示精度一致；E2B 长输入情感有效分母为 38，整组重试 21、额外尝试 28、最终失败 3。
- 独立重算 7 项运行代码/锁文件及 2 项报告代码 SHA-256，全部匹配；28 份所选主源/比较缓存的 Git blob SHA 与字节数也与台账一致。没有因此认定测量真实或环境可复现。
- OpenJev MLX 路径确有 decoder logits、log-softmax 与标签读取逻辑；直接读取 GitHub 元数据确认 vLLM 所引 PR 的合并状态，未外推到发布包。

## 独立阅读范围

以下全部为来源相对路径，不记录私人机器路径。行号含首尾。

| 范围 | 实际阅读 |
|---|---|
| 归档工作稿 | README 1–298、index 1–28；evidence 1–240、859–895、1238–1285，另投影全部 claims、comparison、阅读台账、metadata_checks、limitations、citation_index 与 web_sources 的 ID/URL/范围字段；不是 evidence 全文逐行审读 |
| LocalJev 核心 | `src/index.ts:1-32`、`config.ts:1-96`、`types.ts:1-191`、`server.ts:1-225`、`engine.ts:1-523` |
| LocalJev 测试 | `test/engine.test.ts:1-144`、`server.test.ts:1-106`、`eval.test.ts:1-126` |
| 评测实现 | `scripts/eval/common.ts:1-124`、`data.ts:1-128`、`metrics.ts:1-70`、`run.ts:1-202`、`report.ts:1-108` |
| 文档/配置 | 上游 `README.md:96-157,181-211`；`docs/evaluation.md:1-261`；`docs/evaluation-results-2026-09-18.md:1-118`；`eval/default.json:1-18`；`package.json:1-22`；`LICENSE:1-21` |
| 已提交评测 | `eval/reports/2026-09-18-bakeoff/report.md:1-136`、`manifest.json:1-35,1580-1667`；manifest 起止时间/样本 ID/task/gold/完成数/代码哈希及 summary cells/计数/准确率/MAE/延迟/重试/失败/缓存/paired 采用字段投影；`bun.lock` 仅哈希检查 |
| OpenJev 比较 | `openjev/engine.py:1-80,241-394,421-451`；`mlx_backend.py:1-235`；`encoders.py:1-33`，固定版本见 evidence |
| 一手网页 | TypeSafe API、confidence 页面前 10,000 字符、vLLM PR 指定元数据；另读协调者整理的网页观测笔记，但没有把该笔记当原网页存档 |

## 剩余限制与归档边界

未运行或导入上游代码、测试、评测/报告脚本，未下载模型/数据集、未启动服务或调用推理；没有检查原始 results/warmups 的逐请求真实性，没有验证权重、硬件、有效 runner 配置、SDK 互操作或发布包兼容矩阵。对排队、取消、body 时序和校准的讨论依然是静态分析或待执行建议。

本轮只对文档/元数据做 JSON、相对链接、固定源行号、源字节、论断映射、正文/审查哈希与四文件范围的一致性检查，不运行既有 baseline 全量门禁，也不修复其来源缺口。仅私有研究分支与 PR；未公开发布、未同步飞书，不自动合并。
