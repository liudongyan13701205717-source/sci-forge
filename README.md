# sci-forge

> SciForge — 一条 MCP 从「构思」到「论文交付」的全流程编程工作台。

一个**完全本地自建**的 [MCP](https://modelcontextprotocol.io) server，提供论文领域的端到端自动化：

- 🧪 **复现线** — 拿到一篇论文 PDF，五步闭环复现：解析 → 方案 → 生成代码 → 沙箱运行比对 → 产出交付物
- ✍️ **写作线** — 按章节引导生成论文内容，导出 LaTeX / PDF / DOCX
- 🔬 **研究线** — 构思 → 选题 → 多视角假设辩论 → 实验设计 → 结果自旋门决策
- 🧭 **科研/论文线** — 研究计划书、文献综述、标题/摘要提炼、模拟同行评审、投稿匹配、论文润色
- 📦 **交付线** — 把复现/写作的全部实物（源码/数据/报告/图/导出物）分门别类交付

**特色：免 API key。** 文献检索用 OpenAlex 免鉴权接口（覆盖 arXiv 预印本），LLM 能力为**可选增强**——没有 LLM 时自动回退到本地模板，整条链路仍然可用。

> 独立自建、仅用公开材料，不附属于、不依赖 SciForge 官方站点或 API。

---

## 功能总览

| 工具 | 所属线 | 作用 |
| --- | --- | --- |
| `reproduce_paper` | 复现 | 解析 PDF → 复现方案 → 生成代码 → 沙箱运行比对 → 交付物 |
| `reproduce_status` | 复现 | 查询复现任务的异步状态与阶段进度 |
| `write_section` | 写作 | 按章节引导撰写（abstract/problem/…/results/references） |
| `export_document` | 写作 | 将已写 doc 导出为 LaTeX / PDF / DOCX |
| `ideate_paper` | 研究 | 构思→选题→研究缺口→候选假设→多视角评审→实验计划 |
| `inject_results` | 研究 | 把复现的真实实验结果并入论文对应章节 |
| `research_verdict` | 研究 | 结果自旋门：PROCEED / REFINE / PIVOT 决策建议 |
| `research_plan` | 科研/论文 | 完整研究计划书（RQ/假设/目标/贡献/方法/数据/里程碑/风险） |
| `literature_review` | 科研/论文 | 文献综述（OpenAlex 免 key 检索：代表文献/聚类/缺口/结构） |
| `auto_title_abstract` | 科研/论文 | 从正文提炼标题/摘要/关键词 |
| `peer_review` | 科研/论文 | 模拟同行评审（4 维评分 + 推荐 + 优缺点/修改建议） |
| `venue_suggest` | 科研/论文 | 投稿/期刊匹配（内置映射库 + 可选 LLM） |
| `paper_polish` | 科研/论文 | 润色/一致性/完整性检查 |
| `compare_metrics` | 科研/论文 | 多任务指标对比表 + Welch t / Mann-Whitney U 显著性检验 |
| `check_novelty` | 科研/论文 | 创新性检查：检索相似工作并给出候选差异点 |
| `citation_landscape` | 科研/论文 | 引文热度分析（年度分布/高被引代表/主要载体） |
| `project_memory` | 科研/论文 | 项目进度记账（里程碑/状态/备忘 timeline） |
| `package_submission` | 交付 | 投稿材料打包（zip + Cover Letter + Checklist） |
| `review_code` | 交付 | 复现代码静态点评（种子/硬编码/风险 + 可信度分） |
| `get_deliverables` | 交付 | 列出任务（复现/写作）的交付物清单，按类型分类 |
| `science_list_dbs` | 科学数据 | 列出可用数据库（按领域筛选） |
| `science_search` | 科学数据 | 单库搜索 |
| `science_fetch` | 科学数据 | 按 ID 获取记录 |
| `science_cross_lookup` | 科学数据 | 多库联合查询 |

### 全链路：从构思到论文

```
ideate_paper（构思/假设/实验计划）
      │
      ▼
reproduce_paper ──► reproduce_status（异步轮询，五步闭环）
      │
      ├────────────────────────────┐
      ▼                            ▼
research_verdict（PROCEED/REFINE/PIVOT）   write_section（撰写各章节）
      │                                   │
      ▼                                   ▼
inject_results（实验数据并入 results）      export_document（LaTeX/PDF/DOCX）
      │                                   │
      └──────────────► get_deliverables（交付全部实物）
```

---

## 快速开始

> 👉 **想让 MCP 在 opencode 里自动启动并在对话中自然调用？** 详见 [**USAGE.md**](./USAGE.md)
> （含：自启动验证脚本、opencode 连接步骤、对话式端到端论文生成示例、常见问题）。

### 安装

要求 Python ≥ 3.10。

```bash
git clone https://github.com/liudongyan13701205717-source/sci-forge.git
cd sci-forge
pip install -e .            # 最小安装（只带 MCP 本体）

# 需要复现线时，装上运行依赖（推荐）：
pip install -e ".[reproduce,dev]"
```

**依赖说明**：

| 依赖 | 用途 | 必需？ |
| --- | --- | --- |
| `mcp>=1.29.0` | MCP 协议与 FastMCP 运行 | ✅ 必需（base） |
| `pymupdf` | 论文 PDF 解析 | 复现线 |
| `numpy` / `matplotlib` | 沙箱执行复现代码、绘制收敛图 | 复现线 |
| 本机 `xelatex`/`pdflatex` | LaTeX→PDF 导出 | 可选（缺省时自动用内置 PyMuPDF 渲染出 PDF） |

**验证安装**：

```bash
python -m sciforge.server --help 2>&1 | Out-Null   # 能启动即安装成功（stdio server）
python -m pytest tests/ -q                              # 跑内置测试，应全绿
```

### 在 opencode / Claude Code 中配置

把 server 注册为本地 MCP（以 opencode 为例，`~/.config/opencode/opencode.json`）：

```jsonc
{
  "mcp": {
    "sci-forge": {
      "type": "local",
      "command": ["python", "-m", "sciforge.server"],
      "cwd": "<你的工作区路径>",
      "enabled": true,
      "timeout": 120000,
      "environment": {
        "PYTHONPATH": "<你的工作区路径>"
      }
    }
  }
}
```

> 用**绝对路径**指向解释器与工作区，避免命中系统自带的 Python Store 占位符。
> 建议显式加 `"timeout"`（毫秒），避免冷启动被误判为掉线而出现"需要手动 connect"。

重启客户端后即可看到全部 24 个工具。

---

## 真实使用示例

### 1. 让 MCP 写一篇论文

```text
paper_id = "demo"
write_section(paper_id, "abstract",   "为《边缘设备上的轻量推理》写摘要，主题=推理速度优化", "markdown")
write_section(paper_id, "problem",    "问题定义：边缘设备推理延迟与能耗瓶颈", "markdown")
write_section(paper_id, "modeling",   "建模：轻量化网络与量化方案", "markdown")
write_section(paper_id, "solution",   "求解：剪枝/蒸馏/量化组合策略", "markdown")
write_section(paper_id, "results",    "实验设置与评估指标", "markdown")
write_section(paper_id, "references", "参考文献", "markdown")

export_document(paper_id, "pdf")      # 产出 demo/doc.pdf + doc.tex + doc.html
```

### 2. 构思一个研究课题

```text
ideate_paper("大语言模型的轻量化可解释方法", "my_proj")
# 返回：研究缺口、候选假设、多视角评审（novelty/rigor/feasibility 加权）、实验计划
```

### 3. 复现一篇论文并注入结果

```text
tid = reproduce_paper("path/to/paper.pdf")["task_id"]
# 轮询 reproduce_status(tid) 直到 done

research_verdict(tid)             # 根据实验结果给出 PROCEED/REFINE/PIVOT
inject_results("my_proj", tid)    # 把真实指标表 + 收敛图写进 my_proj 的 results 章节

get_deliverables(tid)             # 拿到复现的全部交付物
```

### 4. 科研/论文全流程（无 key，agent 直接成文）

```text
ideate_paper(topic, paper_id)          # 选题与缺口
research_plan(topic, paper_id)         # 研究计划书
literature_review(topic, paper_id)     # 文献综述
# 由 agent 依 WRITING_PROTOCOL 用 write_section 写满各章完整正文（无 LLM 配置）
auto_title_abstract(paper_id)          # 提炼标题/摘要/关键词
peer_review(paper_id)                  # 模拟审稿，据意见修订
paper_polish(paper_id, "completeness") # 完整性检查
paper_polish(paper_id, "grammar")      # 语言润色
venue_suggest(topic, paper_id)         # 投稿建议
export_document(paper_id, "pdf")       # 终版导出
```

> 快速起一个可写作的论文项目：`python scripts/agent_write_paper.py <paper_id> --topic "..."`。

---

## 架构

```
sciforge/
├── server.py        # MCP stdio server，注册全部 24 个工具
├── core/            # 布局/存储/Layout + 可选 LLM 连接层（无 key 会回退模板）
├── parse/           # 论文 PDF 解析（PyMuPDF）
├── reproduce/       # 五步复现闭环：tasks/codegen/harness/pipeline + codereview 静态点评
│   ├── codegen.py   #   提取超参 + 生成 numpy/torch 复现代码
│   ├── harness.py   #   沙箱执行 + 自愈重试 + 指标/图采集
│   └── pipeline.py  #   编排五步，产出 results.json / plan.json / deliverables/
├── write/           # 写作：doc(DocStore)/templates/validate
├── export/          # 导出：md→latex/html/docx + PDF 渲染
├── research/        # 研究线：lit/ideate/hypoth/design/inject + stats/bench/novelty/community
│   └── (plan/survey/extract/review/venue/polish  # 科研/论文工具集)
├── deliver/         # 交付：get_deliverables + package_submission（投稿打包）
└── science/         # 科学数据查询：41 个连接器，覆盖文献/蛋白/化学/基因组/通路/组学/数据集
```

## 科学数据查询（science）

通过 41 个连接器，覆盖 7 大领域的公开科学数据库：

| 领域 | 连接器 |
| --- | --- |
| literature | openalex, arxiv, biorxiv, crossref, europepmc, pubmed, semantic-scholar |
| proteins | uniprot, rcsb-pdb, pdbe, alphafold, interpro, sifts |
| chemistry | chembl, pubchem, chebi, bindingdb, gtopdb, surechembl |
| genomics | ensembl, eutils, mygene, myvariant, clinvar, dbsnp, gnomad |
| pathways | biogrid, intact, kegg, opentargets, reactome |
| omics | arrayexpress, depmap, expression-atlas, geo, gtex, hpa |
| datasets | zenodo, doaj, openaire, huggingface |

提供 4 个 MCP 工具：

| 工具 | 描述 |
| --- | --- |
| `science_list_dbs(domain?)` | 列出可用数据库，可按领域筛选 |
| `science_search(database, query, limit)` | 单库搜索 |
| `science_fetch(database, id, format)` | 按 ID 获取记录 |
| `science_cross_lookup(query, databases?, limit)` | 多库联合查询 |

### 存储布局

```
.sci-forge/                  # 运行产物，已 gitignore
├── env                         # 本地配置（可选 LLM 端点），不提交
├── projects/{paper_id}/        # 写作项目：doc.md / doc.pdf / doc.tex / sections/
│   └── research/               #   研究产物：*.json + *.md（供后续复用/打包）
└── tasks/{task_id}/            # 复现任务：parse/ code/ runs/ deliverables/
```

### 可选增强：LLM

在 `.sci-forge/env` 写入 OpenAI 兼容端点即可启用 LLM 增强（更自然的章节生成/评审/构思）：

```
BASE_URL=https://.../v1
API_KEY=sk-...
MODEL=...
```

未配置时，所有线自动回退到**本地模板**，功能不受阻断。

---

## 测试

```bash
pip install -e ".[dev]"
python -m pytest tests/ -q      # 全量测试，全离线可跑（文献/复现用模拟数据）
```

测试覆盖四条线上的单元 + stdio 端到端（真实 spawn MCP server 并调用工具）+ 科学数据连接器。

---

## 反馈与贡献

遇到 bug、功能建议或有任何问题，欢迎通过 **GitHub Issues** 反馈：

👉 [https://github.com/liudongyan13701205717-source/sci-forge/issues](https://github.com/liudongyan13701205717-source/sci-forge/issues)

- 🐛 **Bug**：请附上复现步骤、报错信息（含 `File "...", line ...` 堆栈）与相关 `paper_id`/`task_id`。
- 💡 **Feature**：说明你的使用场景与期望行为。
- 🤝 **Contribute**：Fork 后提 PR 即可；请先运行 `python -m pytest tests/ -q` 确保全绿。

---

## License

[MIT](./LICENSE)

<sub>本项目为独立开发的教育/研究工作，与 SciForge 及其商标无关联。</sub>
