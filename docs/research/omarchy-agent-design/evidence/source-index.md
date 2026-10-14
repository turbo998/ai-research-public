# 固定来源与证据索引

## 身份基线

入口 `basecamp/omarchy`；commit API返回规范 `omacom/omarchy`，不是两个研究项目。固定commit `9480d1b6a98156314dbabe6bfef08f39f8b9cd07`，tree `f1ef20f439289dc3cd1c968eb475a9750d64bc61`，2663条、truncated=false，commit time `2026-10-11T20:07:57Z`。

只读元数据入口：[commit API](https://api.github.com/repos/basecamp/omarchy/commits/9480d1b6a98156314dbabe6bfef08f39f8b9cd07)及[tree API](https://api.github.com/repos/basecamp/omarchy/git/trees/9480d1b6a98156314dbabe6bfef08f39f8b9cd07?recursive=1)。后者接受commit selector，响应的sha字段也为此selector，不误称为root tree身份。另将27个根entry按Git tree格式排序/重建对象bytes，所得SHA-1与commit API给出的root tree `f1ef20…` 一致；2663条/非截断是recursive返回范围。

公开raw材料以规范仓库、完整SHA、实际path获取；每个blob用 `SHA1("blob " + byte_length + NUL + bytes)` 和tree的size/sha核对。不运行、不跟随symlink、不提交上游正文；研究归档的中文分析不是上游原文翻译。

## 索引语义

[assertion-index.csv](assertion-index.csv)逐行记录claim、固定path/commit、inclusive行号、证据类别和状态。下表由其使用的path与已核验元数据机械关联；scope是**被引用范围的包络**，不自动证明整个文件都被语义阅读。各专题正文解释实际阅读与局限。所有源对象完整byte身份见[evidence.json](../evidence.json)。

缓存获取数量包括为定位入口而搜索的迁移等，不是语义覆盖率、测试覆盖率或历史分母；未被正文引用的获取对象不充当事实证据。本公开归档仅包含原创分析与固定版本源码引用元数据。

<!-- BEGIN GENERATED SOURCE INVENTORY -->

| 固定文件 / scope包络 | Blob SHA-1 | Bytes / lines | Assertions |
|---|---|---|---|
| [AGENTS.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/AGENTS.md#L1-L161) / 1–161 | `9ebefa7b9c128c122f14986f7dc80086a2564c78` | 11417 / 161 | E5-01 |
| [CLAUDE.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/CLAUDE.md#L1-L1) / 1–1 | `43c994c2d3617f947bcb5adf1933e21dabe46bb5` | 11 / 1 | E5-02 |
| [LICENSE](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/LICENSE#L1-L20) / 1–20 | `f12cfa766c55541c9d8e008e310c95a721e70a97` | 1063 / 20 | L1 |
| [agents/skills/acceptance-tests.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/agents/skills/acceptance-tests.md#L1-L46) / 1–46 | `b2fc49979823c43c5f70dadac348bab3f69a8bbf` | 2172 / 46 | E5-09 |
| [agents/skills/command-metadata.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/agents/skills/command-metadata.md#L1-L31) / 1–31 | `9b90cf5130bab9b7052d431280fbb456361f118a` | 1197 / 31 | E5-03 |
| [agents/skills/install-scripts.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/agents/skills/install-scripts.md#L1-L22) / 1–22 | `b117b19370f615a3b7c79ef073a759932910b24d` | 2415 / 22 | E5-04 |
| [agents/skills/migrations.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/agents/skills/migrations.md#L1-L172) / 1–172 | `5ed1d48909013aca925fc77d0802d17b0bee0031` | 6620 / 172 | E5-06 |
| [agents/skills/shell-dev.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/agents/skills/shell-dev.md#L1-L62) / 1–62 | `05faab5ea4c839569133dcb78c8b12e1948faaba` | 5707 / 62 | E5-05 |
| [agents/skills/visual-verification.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/agents/skills/visual-verification.md#L1-L41) / 1–41 | `a8ed63d7ae26438496c0870aa3f7ab606bbd5071` | 1924 / 41 | E5-10 |
| [bin/omarchy-agent](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent#L7-L168) / 7–168 | `151880544224f0ce5f88f3b70938d2737c8ea66e` | 5420 / 168 | E1-01、E1-02、E1-11、E1-M01、E1-M02、E1-M03、E1-M04、E1-M05、E1-M06、E1-M07、E1-M08、E1-M09、E1-M10、E1-M11、E1-M12、E1-M13、E1-M14 |
| [bin/omarchy-agent-account-exec](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-account-exec#L22-L43) / 22–43 | `28d123e40f5b09bf41c7b15a3ceeb972bdaa8443` | 1473 / 43 | E4-08、E4-76 |
| [bin/omarchy-agent-account-home](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-account-home#L18-L25) / 18–25 | `6e2eb3b874f6617bbf2596c38c5a523e8a039e30` | 1013 / 25 | E4-09 |
| [bin/omarchy-agent-account-state](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-account-state#L35-L710) / 35–710 | `0578b6cc967fca20f44770888f92a05624ac6495` | 30871 / 787 | E4-01、E4-03、E4-04、E4-05、E4-06、E4-07、E4-10、E4-11、E4-12、E4-13、E4-14、E4-15、E4-16、E4-55、E4-56、E4-58、E4-72、E4-75 |
| [bin/omarchy-agent-account-use](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-account-use#L26-L39) / 26–39 | `3103e953149d89f993b96f1d9b757191696499d7` | 1485 / 39 | E4-59 |
| [bin/omarchy-agent-crash](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-crash#L14-L52) / 14–52 | `49a1147e61333dda5bae8fa8c93c4fe4d7d80f3a` | 1573 / 52 | E3-12 |
| [bin/omarchy-agent-prompt](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-prompt#L7-L23) / 7–23 | `f5024b2f011bd3de453e2b59582c872f95f7882e` | 543 / 23 | E1-09 |
| [bin/omarchy-agent-usage-claude](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-usage-claude#L173-L1280) / 173–1280 | `e615c5836eb555f355055bcd5292b10b78642d18` | 49908 / 1286 | E4-19、E4-20、E4-21、E4-22、E4-23、E4-60、E4-61、E4-62、E4-68 |
| [bin/omarchy-agent-usage-codex](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-usage-codex#L241-L1077) / 241–1077 | `c76359943c04242383b2582e935c469b3f4942c0` | 41190 / 1077 | E4-24、E4-25、E4-26、E4-27、E4-28、E4-63、E4-64 |
| [bin/omarchy-agent-usage-fireworks](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-usage-fireworks#L58-L554) / 58–554 | `fe04bc1df38547351c56c027d6df4b0c3e1ed808` | 19419 / 558 | E4-32、E4-33、E4-34、E4-35、E4-66、E4-67、E4-77 |
| [bin/omarchy-agent-usage-grok](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-usage-grok#L86-L263) / 86–263 | `f2d4d7fe340c4c687b7f15e31f5c8c2a269f29ae` | 13894 / 361 | E4-29、E4-30、E4-31、E4-65 |
| [bin/omarchy-agent-usage-update](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-agent-usage-update#L42-L86) / 42–86 | `e759dc72459c2d9e2e43c25ae02fe4f11e89d762` | 2768 / 89 | E4-36、E4-37、E4-53 |
| [bin/omarchy-crash-mute](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-crash-mute#L12-L73) / 12–73 | `88229fead95d699b546952e92df47559895aeb7c` | 2143 / 73 | E3-14 |
| [bin/omarchy-crash-watch](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-crash-watch#L17-L109) / 17–109 | `d3e78d1662145a9c571cdddd1c984be481ef23e1` | 4804 / 109 | E3-04、E3-05 |
| [bin/omarchy-default-agent](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-default-agent#L13-L104) / 13–104 | `0fe9a237caf3e7e9716862e9030b983bc2376610` | 4175 / 104 | E1-04、E1-05 |
| [bin/omarchy-install-hermes-cli](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-install-hermes-cli#L190-L240) / 190–240 | `a5acd0fe7c81015e348dc73fd2fa8151458a4ff9` | 23056 / 544 | E1-08 |
| [bin/omarchy-install-openclaw-cli](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-install-openclaw-cli#L21-L271) / 21–271 | `17e5d0eb4c375c89b59ace29cbe4dce5632021aa` | 10177 / 271 | E1-12 |
| [bin/omarchy-launch-openclaw](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-launch-openclaw#L9-L91) / 9–91 | `13ab6c24765226fce8672b16b5a8a6a3409d42c4` | 3821 / 91 | E1-13 |
| [bin/omarchy-launch-tui](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-launch-tui#L1-L13) / 1–13 | `bd67c64ca94e067f2e98ce5243f9ab063aee9117` | 346 / 13 | E1-10 |
| [bin/omarchy-mise-install](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-mise-install#L6-L59) / 6–59 | `356c3324bf6a3958155935af7a841ba6ea1fa353` | 2106 / 59 | E1-06 |
| [bin/omarchy-notification-send](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-notification-send#L118-L211) / 118–211 | `9e7fd04996740a42e5944863b6f6192906da122a` | 6424 / 211 | E3-08 |
| [bin/omarchy-notification-wait](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-notification-wait#L9-L30) / 9–30 | `609dc3263503ecfc27be1b5bc2cc6c17ac1f6b96` | 751 / 30 | E3-06 |
| [bin/omarchy-openclaw-onboard](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-openclaw-onboard#L23-L134) / 23–134 | `d8665b3e1c385accfe10f1437a80f4e50c9b5435` | 5948 / 134 | E1-14 |
| [bin/omarchy-provision-user](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-provision-user#L58-L104) / 58–104 | `0545978f7e944bec2f6389c2bf5c78f5962df253` | 3972 / 131 | E2-01 |
| [bin/omarchy-snapshot](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-snapshot#L9-L49) / 9–49 | `34ac5cd19ad70dad6344a37adc0428e62ae36b4b` | 1414 / 49 | E6-01 |
| [bin/omarchy-toggle](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-toggle#L1-L42) / 1–42 | `a36f0e633d253267efe0c656e2ff7c4639688076` | 660 / 42 | E3-15 |
| [bin/omarchy-toggle-crash-capture](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-toggle-crash-capture#L8-L18) / 8–18 | `1b4fb8b652e7450d43a7763863469f8476679afe` | 659 / 18 | E3-13 |
| [bin/omarchy-toggle-enabled](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/bin/omarchy-toggle-enabled#L1-L6) / 1–6 | `dd4f58c61ca6347e2f9b83f14e77da6659c4715d` | 156 / 6 | E3-16 |
| [default/agents/skills/diagnose-crash/SKILL.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/diagnose-crash/SKILL.md#L1-L128) / 1–128 | `ea77300721c7b9e2ecb39fd03acb8d1a2e7427d7` | 5710 / 128 | E2-04 |
| [default/agents/skills/diagnose-crash/reporting.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/diagnose-crash/reporting.md#L1-L104) / 1–104 | `15bd08bc54d8dcb9c3b1085454434b2dfeab3452` | 3935 / 104 | E2-13 |
| [default/agents/skills/omarchy-app/SKILL.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/omarchy-app/SKILL.md#L1-L107) / 1–107 | `1a1c0fad2d507ad669920100a5bc30933e98399e` | 5430 / 107 | E2-03、E2-12 |
| [default/agents/skills/omarchy-app/templates.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/omarchy-app/templates.md#L1-L431) / 1–431 | `0d8e6934c399ee2a9c9b9551fe160015ca8fa9ec` | 10395 / 431 | E2-05 |
| [default/agents/skills/omarchy/SKILL.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/omarchy/SKILL.md#L1-L276) / 1–276 | `eb3cca877772d48c027395055406d3b37d2ee473` | 12350 / 276 | E2-02 |
| [default/agents/skills/omarchy/capture.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/omarchy/capture.md#L1-L59) / 1–59 | `9c242172cde074262381f80d4038ba67428551c0` | 2915 / 59 | E2-10 |
| [default/agents/skills/omarchy/contributing.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/omarchy/contributing.md#L1-L65) / 1–65 | `c76c12d61f88277ac5770916cd4764b054b97676` | 2503 / 65 | E2-11 |
| [default/agents/skills/omarchy/hooks.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/omarchy/hooks.md#L1-L30) / 1–30 | `5da16fcc1d77740996e2a66c412e40acfd911499` | 1759 / 30 | E2-09 |
| [default/agents/skills/omarchy/hyprland.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/omarchy/hyprland.md#L1-L80) / 1–80 | `fd0e1b623187cd09cead6d67fe564c2ad55d78e8` | 3937 / 80 | E2-06 |
| [default/agents/skills/omarchy/plugins.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/omarchy/plugins.md#L1-L71) / 1–71 | `ce6ab3f85e5de33e0f7c41cd4925449c4c94588e` | 3357 / 71 | E2-07 |
| [default/agents/skills/omarchy/theming.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/agents/skills/omarchy/theming.md#L1-L79) / 1–79 | `5212aa15b0ae37ea2ec732508803d59092274afd` | 3245 / 79 | E2-08 |
| [default/systemd/user/omarchy-crash-watch.service](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/default/systemd/user/omarchy-crash-watch.service#L1-L19) / 1–19 | `4c6a58c5a5a3dae1b45a67972734cb480f96999e` | 652 / 19 | E3-01 |
| [docs/testing.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/docs/testing.md#L1-L133) / 1–133 | `f8cd160e379d3a88b70699c2177235cc5ab655c6` | 7947 / 133 | E5-08 |
| [etc/mise/conf.d/omarchy-agent-accounts.toml](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/etc/mise/conf.d/omarchy-agent-accounts.toml#L1-L13) / 1–13 | `ffab5bb8954da2340e3ec0b0aa41a25ae701d100` | 368 / 13 | E4-57 |
| [install/user/first-run/enable-user-units.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/install/user/first-run/enable-user-units.sh#L16-L35) / 16–35 | `07534d4fee746d367c2cdbf0dd3d6841c191ca56` | 1376 / 35 | E3-02 |
| [install/user/first-run/setup-agent.hook](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/install/user/first-run/setup-agent.hook#L1-L11) / 1–11 | `90596b83e92ceebdc0d923b024ea81c12c974106` | 433 / 11 | E1-03 |
| [install/user/mise.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/install/user/mise.sh#L1-L29) / 1–29 | `6819e48e3c6828d217458ee70afccae042ba4540` | 1279 / 29 | E1-07 |
| [manual/47-system-snapshots.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/manual/47-system-snapshots.md#L1-L25) / 1–25 | `02f592f1a70c74f8826fe749491036bfce68fc31` | 2106 / 25 | E6-02 |
| [migrations/1786098807.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/migrations/1786098807.sh#L1-L7) / 1–7 | `6b2c2cc8138c83a4a7556e91ac8a8224a81e6d30` | 464 / 7 | E2-14 |
| [migrations/1786539345.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/migrations/1786539345.sh#L1-L31) / 1–31 | `09e34b1da88c033973de747a227ac345b5b28d63` | 1365 / 31 | E2-15、E3-03 |
| [migrations/1786719479.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/migrations/1786719479.sh#L1-L41) / 1–41 | `8a35e1a864123aabca3c3bf0db3eeb17b7ede7c9` | 1525 / 41 | E2-16 |
| [migrations/1787843905.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/migrations/1787843905.sh#L1-L22) / 1–22 | `e0e58cd5199992240b3fc18713754e6bbaa00ee5` | 645 / 22 | E2-17 |
| [migrations/1790702606.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/migrations/1790702606.sh#L1-L28) / 1–28 | `14036595c9312b7fed5622a2b2dd48d1b4fef5f4` | 873 / 28 | E2-18 |
| [plans/backup.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/plans/backup.md#L1-L123) / 1–123 | `f29e5e6df6df0d26e0a081fb44f333ad6c6a11a0` | 21979 / 133 | E5-11 |
| [plans/dots.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/plans/dots.md#L1-L100) / 1–100 | `07bfab02c4259ae77786598c059d810407c186cd` | 10796 / 206 | E5-12 |
| [shell/Commons/Util.qml](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/Commons/Util.qml#L61-L68) / 61–68 | `cacc98d25517f6fa6e9ad00ea111aeb457f12abd` | 5875 / 159 | E3-11 |
| [shell/plugins/agents/Agent.qml](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/plugins/agents/Agent.qml#L20-L51) / 20–51 | `843901fa0810dcaac5ffb537cd858784916b29cd` | 1566 / 53 | E4-38 |
| [shell/plugins/agents/Main.qml](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/plugins/agents/Main.qml#L24-L781) / 24–781 | `7c3bb625b549e56f5060c63438683a787e6746f1` | 30435 / 831 | E4-17、E4-18、E4-39、E4-40、E4-54、E4-69、E4-74 |
| [shell/plugins/agents/Panel.qml](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/plugins/agents/Panel.qml#L204-L777) / 204–777 | `4e40a2eab761c4acb445a3a719f83d5196e007df` | 71208 / 2003 | E4-41、E4-70、E4-71、E4-73、E4-78、E4-79 |
| [shell/plugins/agents/README.md](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/plugins/agents/README.md#L3-L118) / 3–118 | `26af2f72c6d8bb37646454f86a04eb71f094b1e5` | 11907 / 205 | E4-51、E4-52 |
| [shell/plugins/agents/manifest.json](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/plugins/agents/manifest.json#L20-L34) / 20–34 | `7ca52484b122ffb939bfbf11418b66314a651014` | 1986 / 41 | E4-02 |
| [shell/plugins/notifications/NotificationLogic.js](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/plugins/notifications/NotificationLogic.js#L118-L177) / 118–177 | `6ba2b6ab45a9aa01bf0f2b435e13de9b1f57d350` | 20088 / 511 | E3-07、E3-09 |
| [shell/plugins/notifications/Service.qml](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/shell/plugins/notifications/Service.qml#L394-L410) / 394–410 | `a239b19f6cf8e2e10b28b1ab7df0e4957b7b7da8` | 44961 / 1111 | E3-10 |
| [test/acceptance](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/acceptance#L1-L101) / 1–101 | `ef2da6b02e32106c867dbc477e2964059d7b8a0d` | 3369 / 101 | E5-13 |
| [test/all](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/all#L1-L23) / 1–23 | `7dae67c5796bba8dd6ad14a8fec0ecdd4538fcf1` | 529 / 23 | E5-07 |
| [test/shell.d/agent-account-autoswitch-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/agent-account-autoswitch-test.sh#L159-L202) / 159–202 | `f1b684521f1116bcad6500c78064ffce0b5d3712` | 8681 / 202 | E4-43 |
| [test/shell.d/agent-account-exec-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/agent-account-exec-test.sh#L76-L125) / 76–125 | `5886050f9ac413a8b88395597ca35ddc979ed20b` | 9446 / 206 | E4-42 |
| [test/shell.d/agent-account-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/agent-account-test.sh#L123-L297) / 123–297 | `c0201e3d38c23265a0df350659ffc960b9a69d93` | 23753 / 417 | T4-01、T4-02 |
| [test/shell.d/agent-usage-claude-limits-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/agent-usage-claude-limits-test.sh#L26-L413) / 26–413 | `df39f9d8707b105a5af526606b7ba9e2b577d889` | 22416 / 413 | E4-44、T4-03 |
| [test/shell.d/agent-usage-codex-notifications-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/agent-usage-codex-notifications-test.sh#L54-L79) / 54–79 | `ceeecaecd232d67ccb85bf723af189c5fb7cf541` | 3124 / 80 | E4-45 |
| [test/shell.d/agent-usage-fallback-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/agent-usage-fallback-test.sh#L24-L55) / 24–55 | `346d08072971bc74180789f56702735add3938b8` | 2712 / 56 | E4-49 |
| [test/shell.d/agent-usage-fireworks-scanner-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/agent-usage-fireworks-scanner-test.sh#L232-L280) / 232–280 | `6440ce1164f9935904e927ae8fe59a663f38849f` | 12104 / 280 | E4-47、T4-04 |
| [test/shell.d/agent-usage-grok-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/agent-usage-grok-test.sh#L89-L125) / 89–125 | `eeaf985eaf37c7100772bc627a818a244dc070f4` | 11392 / 180 | E4-46 |
| [test/shell.d/agent-usage-update-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/agent-usage-update-test.sh#L40-L65) / 40–65 | `ee3aaf0112e46ac0eafc8f011fad07526017d6cc` | 2157 / 65 | E4-48 |
| [test/shell.d/agents-panel-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/agents-panel-test.sh#L30-L36) / 30–36 | `e79ca3402290c1eef232344dc70a7bb59ef1e935` | 4907 / 44 | E4-50 |
| [test/shell.d/crash-capture-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/crash-capture-test.sh#L26-L396) / 26–396 | `1b7e93d05e27aa95ad36cf15dc9e99c3323f6731` | 15739 / 396 | T3-01、T3-02 |
| [test/shell.d/default-agent-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/default-agent-test.sh#L450-L941) / 450–941 | `dc523e9f928b93590a82d9354760bfea5b7a3f0d` | 43415 / 941 | T1-01 |
| [test/shell.d/hermes-skills-migration-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/hermes-skills-migration-test.sh#L7-L75) / 7–75 | `f1145bd71f0d1f6c1c7040d52d63333898c89aac` | 2973 / 75 | T2-01 |
| [test/shell.d/launch-openclaw-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/launch-openclaw-test.sh#L90-L189) / 90–189 | `4c443e07f49dd3639d8840188f20a8d1d7f93bde` | 8559 / 189 | T1-02 |
| [test/shell.d/openclaw-onboard-test.sh](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/test/shell.d/openclaw-onboard-test.sh#L215-L300) / 215–300 | `1c315fdd94b09efef2390e42ecd3e7f519a20bd5` | 13458 / 300 | T1-03 |

<!-- END GENERATED SOURCE INVENTORY -->

## 官方在线对照来源

W1–W4为Anthropic官方SDK overview/permissions/skills/cost-tracking；W5–W7为GitHub官方CLI、GitHub.com/cloud agent、risks/mitigations。访问日期统一2026-10-12；最终URL、重定向、读取章节及产品条件保存在[evidence.json](../evidence.json)。官网未冻结为Omarchy实际binary版本，外链不递归采集，未执行其示例。

## 许可及原创边界

固定[LICENSE](https://github.com/omacom/omarchy/blob/9480d1b6a98156314dbabe6bfef08f39f8b9cd07/LICENSE#L1-L20)为MIT文本，署名David Heinemeier Hansson（L1）。未逐一核验所有依赖、品牌或媒体权利，不外推统一许可；本库不复制完整源码、SKILL、模板或官网正文，只保存分析、少量参数/字段、固定链接与元数据。见[第三方声明](../../../../THIRD_PARTY_NOTICES.md)。
