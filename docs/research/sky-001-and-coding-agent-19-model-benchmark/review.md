# 方法论审查与交付物校验记录 / Methodology Review & Deliverable Verification (`review.md`)

## 1. 审计范围与真值锚点（Scope & Ground-Truth Anchors）

本审查记录覆盖 `sky-001-and-coding-agent-19-model-benchmark` 研究专题的双轨数据源、算术一致性、7-Card 4:5 视觉卡片合规性以及中英双语完整性：

1. **Track A — Coding Agent 十九模型基准（增补报告 5）**：
   - 上游提交：`satomic/copilot-benchmark` @ `a191383571a13143685fd6f7787512c4e281a9ba` (`2026-10-15T08:28:58Z`)
   - 新增运行包：`22` 个目录（`reports/A1-cron-parser__claude-haiku-5.5` 至 `reports/C4-microvm__gemini-4-argon`），CLI 版本 `1.0.98`，`effort=medium`。
   - 历史基线零漂移：前 17 个模型（`187` 个运行包）在 `a1913835` 中的 `score.json` 总分与 `f4ebde7c` 完全一致（`0.00` 分漂移）。
2. **Track B — Skyfall AI `SKY-001` 工程世界模型**：
   - 着陆页生产包：`https://skyfall.ai/assets/index-D5BqB7X_.js`（`494,518` bytes，SHA-256 `1bc34257c0f2f1db82336d13f95f88c391950c0957655377f752954b4cd7199f`）
   - 技术博客生产包：`https://skyfall.ai/assets/article-D6mnIEDb.js`（`77,103` bytes，SHA-256 `8f22592c0d7f0bc1600158903685a5212ddb417499cde1c1e93754de5e6a9830`）

---

## 2. 离线验证与单元测试结果（Verification & Unit Test Results）

通过 `python simulator/test_sky001_and_19model_verifier.py` 执行 6 项确定性断言测试，全部通过（`Ran 6 tests in 0.003s — OK`）：

| 测试用例 | 验证目标 | 实测输出 | 状态 |
|---|---|---|---|
| `test_nineteen_model_counts_and_ranks` | 验证 19 模型排序、`Haiku 5.5` (#4, `99.24`)、`Gemini 4 Argon` (#11, `98.59`) 与 9 个 `1,310/1,310` 满分模型 | 全部精确匹配 | PASS |
| `test_supplement5_generational_deltas` | 验证 `Haiku 5.5 vs 4.5` (`+5.28` 分, `-91.6%` 成本, `-72.4%` 轮次) 与 `Argon vs 3.8 Flash` (`+0.59` 分, `+34` 隐藏断言) | 全部精确匹配 | PASS |
| `test_pareto_frontier_models` | 验证成本-得分帕累托前沿模型集（`GPT-6 Luna`, `Haiku 5.5`, `Opus 5.5`, `Fable 5.1`） | 全部精确匹配 | PASS |
| `test_sky001_critical_path_simulation` | 验证 4 个官方装配体在 $S=100, W=128$ 下的关键路径压缩比（Jaguar E-Type `98.44x`） | `10,336 -> 105` (`98.44x`) | PASS |
| `test_sky001_benchmark_discrepancies` | 验证 CAD (`51.0x` 快 / `150.0x` 省, `Gemini 4` vs `Opus 5.5` 包差异) 与 BIM (`Gemini 3.8 Flash` `42.3%` 第 2 名) | 全部精确匹配 | PASS |
| `test_summary_json_export` | 验证 `evidence/verifier-summary.json` 导出完整性 | 导出成功 (`17,868` bytes) | PASS |

---

## 3. 交付物清单与 SHA-256 校验和（Deliverable Checksums）

| 文件路径 | 字节数 | SHA-256 校验和 | 说明 |
|---|---:|---|---|
| `README.md` | `33,893` | `6eebabfb473962fcbd8a5f9afefd81e34a17d6407802caec2f5fafa04926b64e` | 中文完整研究主报告（含 `SKY-001` 调研 + 19 模型全表） |
| `README.zh-CN.md` | `33,893` | `6eebabfb473962fcbd8a5f9afefd81e34a17d6407802caec2f5fafa04926b64e` | 中文主报告镜像副本 |
| `README.en.md` | `21,042` | `8724ed2e73589074e1d636f5bcd7766424ae05f92f644a0f2863d8ebf549417f` | 英文完整研究主报告 |
| `test-report.md` | `22,836` | `2ae0a83c08d3a546f473ae1f8b3ba8fb0874d610c12abf3aebe2f6cc423b03b2` | 中文 7-Card 4:5 视觉基准评测报告 |
| `test-report.en.md` | `21,160` | `3537d61c0fa4fbcc71312384f326352ee9893b47c7a49520a59a5f3b7f102394` | 英文 7-Card 4:5 视觉基准评测报告 |
| `test-report-cards.html` | `99,778` | `1b0ecba53fa2964ac0ba821bc3573266a0a289ec2ed23804d8b0f8ddfb23c3f1` | 自包含 CSP 锁定 7-Card 4:5 交互式 HTML 卡片组 |
| `report.json` | `46,852` | `55a76c2e2f5cd53e6037d3da3d30951e6d715685eda71aefae2e5bf3b7c1d00f` | 7-Card 标准结构化数据源 + 4 张完整评测表 |
| `evidence.json` | `8,591` | `8ba9d2f9a15456d6f04c923339fbb801363df9fbc2a8949b39e0632ed78d8b1d` | 上游 Commit Hash、Bundle SHA-256 与关键指标锁 |
| `evidence/verifier-summary.json` | `17,868` | `15a902f4a6937ee115e9a3be63850f6aded4001ea4171dc5d31f87789293dd1b` | 离线验证器输出快照 |
| `simulator/sky001_and_19model_verifier.py` | `45,555` | `d1f510f2e8c780afbd17d31d69dfdd8abeff2f945573fac8efff1ffb78d25e16` | `SKY-001` 关键路径模拟器与 19 模型验证脚本 |
| `simulator/test_sky001_and_19model_verifier.py` | `5,645` | `12ae687d5b2fcbd8247757fc4a2b99f0300fa0d2faa0081815aa5b14e0b6fcf9` | 单元测试套件（兼容 `unittest` 与 `pytest`） |
| `simulator/generate_artifacts.py` | `37,864` | `7cf5cd340dcddd7588c39185dd7cf2b2d58b178425ff7016e2de29363afe8665` | `report.json` / `evidence.json` / `test-report-cards.html` 生成脚本 |
