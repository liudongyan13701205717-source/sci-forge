# 快速开始

本页用一个具体课题，串起 sci-forge 的完整使用流程。**不假设你有任何 API key。**

---

## 你将做出什么

从零开始，最终得到：

- 一份研究计划（RQ / 假设 / 贡献 / 方法 / 指标 / 里程碑）
- 一篇含摘要、引言、方法、结果、讨论的论文文档
- 一份 Material Passport，标注每个 claim 的证据来源
- 一个可导出的 PDF / DOCX 文件（LaTeX 源同时生成）

示例课题（下文统称「本课题」）：**边缘设备上的大模型轻量推理**。

---

## 第 0 步：确认工具已就位

在 MCP 客户端的对话里直接问，或手动调用：

```text
list_disciplines()               # 内置 1538 门学科
science_list_dbs()               # 全部可用科学数据库
science_list_dbs("literature")   # 只看文献域
```

若客户端提示找不到 `sci-forge` 工具，回到 [安装 · 注册到 MCP 客户端](installation.md#注册到-mcp-客户端)。

---

## 第 1 步：找到一个值得做的研究

### 1.1 主题侦察

```text
scout_topic("large language model on-device inference", limit=10)
scout_compare(["on-device LLM inference", "edge LLM compression"], limit=5)
```

返回按命中数降序的论文列表。`scout_compare` 用于横向比较两个主题的拥挤程度。

### 1.2 文献综述框架

```text
literature_review("边缘设备上的大语言模型轻量化推理", "demo")
```

两个参数都是必填：`topic`（主题）与 `paper_id`（项目标识）。产物落在 `.sci-forge/projects/demo/research/`，含代表文献、主题聚类、研究缺口与综述结构，可直接作为 related work 素材。

### 1.3 完整构思

```text
ideate_paper("边缘设备上的大语言模型轻量化推理", "demo")
```

这是**一次调用走完五步**：

```
选题 → 研究缺口 → 候选假设 → 多视角评审 → 实验计划
```

之后可反复调用 `project_memory` 追加里程碑。

> **没有 LLM 也能跑。** `ideate_paper` 在未配置端点时走本地模板与规则引擎，产出结构相同、措辞更模板化。配置方式见本页末尾。

---

## 第 2 步：写正文

### 2.1 查清该学科怎么写

```text
get_discipline("machine_learning")
```

返回 v2 字段全量：`paper_types`（体裁 → 章节结构）、`citation_style`、`reporting_standards`、`conventions`、`key_venues`、`contribution_forms`、`tools`、`databases`。

写作前先看这一眼，能避免大部分「格式不对被退稿」的问题。

### 2.2 逐章节写

`write_section(paper_id, section, prompt, format="latex")`，`format` 只接受 `latex` 或 `markdown`。

```text
write_section("demo", "abstract",   "为《边缘设备上的轻量推理》写摘要",   "markdown")
write_section("demo", "problem",    "问题定义与挑战",                      "markdown")
write_section("demo", "modeling",   "INT4 量化 + 蒸馏 + 层跳过联合方案",   "markdown")
write_section("demo", "solution",   "求解流程与实现细节",                  "markdown")
write_section("demo", "results",    "评测集、设备、基线与指标",            "markdown")
write_section("demo", "references", "参考文献占位",                        "markdown")
```

`section` 的可用取值：`abstract`、`introduction`、`problem`、`assumptions`、`notation`、`modeling`、`solution`、`results`、`references`、`appendix`。

> 学科专属章节结构以 `get_discipline` 返回的 `paper_types` 为准；上面是通用骨架。

### 2.3 从正文提炼标题与摘要

```text
auto_title_abstract("demo")
```

**在正文写完之后**跑这个，顺序反了效果差。

---

## 第 3 步：守住学术诚信（可跳过，但建议做）

这是 sci-forge 与普通写作工具的主要区别。

### 3.1 完整性门

两道门各有明确的 context 结构，**不要往里塞 `stage` 字段**：

```text
gate_2_5({"code": "...", "plan": "..."})                        # 代码生成 → 执行
gate_4_5({"results": {...}, "runs": [...], "claims": [...],
          "doc_text": "...", "negative_results": [...]})        # 结果 → 论文 / 交付
run_gates({...同时含两门所需字段...})                            # 一次跑完，返回 {"2.5": ..., "4.5": ...}
```

设计取向是 **fail-closed**：证据不足即拒绝，返回 `gate_refuse` 类的结果是**预期行为**，不是故障。

### 3.2 claim → source 核验

```text
verify("本文声称 INT4 量化在 4-bit 下可将显存占用降至 1/4")
verify_reference_list(["10.1038/nature12373", "10.48550/arXiv.2301.00001"])
```

`verify(text, sources=None)` 解析正文中的 claim 与引文锚点，判定 SUPPORTED / PARTIAL / UNSUPPORTED。`verify_reference_list(refs)` 批量核验 DOI，返回 valid / invalid 列表。

### 3.3 Material Passport

```text
build_passport(task_id="demo", results={...}, claims=[...], gate_results={...})
```

产出一份 per-run 产物档案：实验出处（provenance）+ claim 审计 + 反面证据。这份档案可直接作为投稿的 provenance 附件。

---

## 第 4 步：投稿前自查

```text
peer_review("demo")                                                # 4 维评分 + 推荐
revision_coach(comments_text="评审意见原文……")                      # 评审意见 → 修订路线图
rebuttal_audit(rebuttal_text="回应草稿……", comments="评审意见原文……")
```

多视角评审面板的**第一个参数是论文全文**，不是主题：

```text
run_panel(text=<论文全文>, journal="Nature Machine Intelligence",
          design="quantitative empirical study")
```

`run_panel` 是 7 席面板（`field_analyst` / `eic` / `methodology_R1` / `domain_R2` / `perspective_R3` / `devils_advocate` / `editorial_synthesizer`）。`mode` 可取 `full` / `quick` / `re-review` / `methodology_focus` / `calibration`。

### 期刊匹配

```text
journal_fit(paper_text="<论文全文>", venue="Nature Machine Intelligence")
venue_suggest("边缘设备上的大语言模型轻量化推理", "demo")   # topic + paper_id，两个都必填
```

---

## 第 5 步：导出与交付

```text
export_document("demo", "pdf")     # target 只接受 pdf 或 docx
get_deliverables(task_id="demo")
package_submission("demo")
```

- `export_document` 的 `target` 仅支持 `pdf` / `docx`；**LaTeX 源始终生成**。有 LaTeX 引擎时走真实编译，否则回退到内置 PyMuPDF 渲染。
- `package_submission(paper_id, task_id="")` 打包 zip，附 cover letter 与投稿 checklist。

> **打包前人工检查。** `.sci-forge/projects/*/research/` 里会积累中间产物；`.sci-forge/env`（含凭据）已被 gitignore，但仍需确认不会被打进包里。

---

## 常见问题

| 现象 | 说明 |
| --- | --- |
| 文本生成很模板化 | 没配 LLM 端点。配置后自然度提升，不配也能用。见本页末尾 |
| 检索类工具没结果 | 检查网络；或设 `SCI_FORGE_OFFLINE=1` 走离线（此时不会发起外部请求） |
| `science_fetch` 报「不支持」 | 46 个库里**仅 `uniprot` 实现了 `fetch`**，其余只能用 `science_search` |
| `write_section` 报格式错 | `format` 只接受 `latex` / `markdown`；`export_document` 的 `target` 只接受 `pdf` / `docx` |
| 完整性门一直拒绝 | 正常。补齐证据，或用 `request_bypass` 走带理由的审批 |
| `list_disciplines` 的 `domain` 传了没效果 | 该参数当前为预留位，未参与过滤，属已知限制 |
| `citation_graph` 的 `depth` 传 2 没变化 | 当前实现只展开一层，属已知限制 |
| 复现线报缺 `pymupdf` | 需装 `reproduce` extra，见 [安装](installation.md#extras-说明) |

---

## 可选增强：接入 LLM

在工作区根目录建 `.sci-forge/env`：

```
BASE_URL=https://your-endpoint/v1
API_KEY=sk-...
MODEL=your-model
```

**不配置则全部功能照常可用**，只是生成文本走本地模板。数据会转发到你指定的 OpenAI 兼容服务，数据流向由该端点决定。

---

## 离线跑一遍

```bash
export SCI_FORGE_OFFLINE=1        # Windows PowerShell: $env:SCI_FORGE_OFFLINE = "1"
python -m pytest tests/ -q        # 268 个用例应全绿
```

---

## 下一步

- 想知道每个工具的参数细节 → [MCP 工具清单](mcp-tools.md)
- 想按自己的学科查规范 → [学科体系](disciplines.md)
- 想查具体某个数据库能返回什么 → [科学数据连接器](connectors.md)
- 装不上 → [安装](installation.md)

---

<sub>观测日期 2026-09-26。以上流程对应的工具集合为 75 个工具 + 2 个资源。</sub>
