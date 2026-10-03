# 获取支持

本文件说明 **sci-forge** 在哪里提问、如何提问，以及哪些渠道不适合提问。

---

## 先看这里

| 你要做的事 | 去哪里 |
| --- | --- |
| 报告缺陷 | [新建 issue](https://github.com/liudongyan13701205717-source/sci-forge/issues/new/choose)，选 **Bug 报告** |
| 提功能需求 | 同上，选 **功能请求** |
| 问使用方法 | [Discussions](https://github.com/liudongyan13701205717-source/sci-forge/discussions) |
| 报告安全漏洞 | **不要**开 issue，见 [SECURITY.md](../SECURITY.md) |
| 讨论方向与想法 | [Discussions](https://github.com/liudongyan13701205717-source/sci-forge/discussions) |
| 安装与接入问题 | 先读 [docs/installation.md](../docs/installation.md) 与 [docs/quickstart.md](../docs/quickstart.md) |
| 某个工具怎么用 | 先读 [docs/mcp-tools.md](../docs/mcp-tools.md) |
| 学科 / 连接器细节 | 先读 [docs/disciplines.md](../docs/disciplines.md) / [docs/connectors.md](../docs/connectors.md) |

---

## 提问之前

大部分「怎么用」的问题，在下面三处已有答案：

1. **[docs/installation.md](../docs/installation.md)** —— 安装、extras、MCP 客户端注册、常见安装故障。
2. **[docs/quickstart.md](../docs/quickstart.md)** —— 从零到产出一篇文档的完整流程。
3. **[docs/mcp-tools.md](../docs/mcp-tools.md)** —— 65 个工具的参数与行为。

问之前建议先：

- 搜一遍 [Discussions](https://github.com/liudongyan13701205717-source/sci-forge/discussions) 和 [已关闭的 issue](https://github.com/liudongyan13701205717-source/sci-forge/issues?q=is%3Aissue+is%3Aclosed)；
- 用 `sci-forge --version` 确认版本；
- 若是复现或检索类问题，先设置 `SCI_FORGE_OFFLINE=1` 跑一遍测试，确认本地环境本身正常。

---

## 提问时带上这些

好的问题能一次得到答案：

| 项目 | 例子 |
| --- | --- |
| 版本与平台 | `sci-forge 0.1.0`、Python 3.12.4、Windows 11 |
| 安装方式 | `pip install -e ".[reproduce,dev]"` |
| MCP 客户端 | opencode / Claude Code / Cursor |
| 你调用的工具与参数 | `science_search("openalex", "crispr", limit=5)` |
| 实际返回 | 完整返回内容或完整报错文本 |
| 你期望的结果 | 你以为会看到什么 |

**不要**在提问中贴出 API key、token，或 `.sci-forge/env` 的内容。

---

## 本项目能提供什么支持

请把预期放对：

- ✅ 缺陷确认、行为解释、安装故障排查、文档纠错；
- ✅ 对功能请求与设计方案的讨论；
- ✅ PR 的评审反馈。
- ❌ 24×7 值班支持；
- ❌ 保证某个具体外部数据库/接口在特定时刻可用；
- ❌ 代你完成论文写作、复现或数据分析；
- ❌ 论文投稿代理或代投服务。

---

## 社区约定

所有讨论与 issue 参与均须遵守 [行为准则（Contributor Covenant v2.1）](../CODE_OF_CONDUCT.md)。举报违反行为准则的情况时，请通过仓库私下联系维护者，**不要**在公开 issue 中写明经过。

---

## 赞助

本项目由个人维护，没有付费支持渠道。若你希望支持，可考虑：

- 提交代码、文档或学科数据（见 [CONTRIBUTING.md](../CONTRIBUTING.md)）；
- 提交 PR 时一并修正文档中的错误；
- 把你成功复现的案例写成 issue 反馈。

赞助渠道见 [.github/FUNDING.yml](./FUNDING.yml)（若为空表示当前未启用任何赞助平台）。
