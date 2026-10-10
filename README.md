<div align="center">

# sci-forge

**一条 MCP，从「构思」到「论文交付」的全流程科研工作台**

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](./pyproject.toml)
[![MCP Tools](https://img.shields.io/badge/MCP%20tools-75-green.svg)](./docs/mcp-tools.md)
[![Disciplines](https://img.shields.io/badge/disciplines-1538-green.svg)](./docs/disciplines.md)
[![Connectors](https://img.shields.io/badge/connectors-46-green.svg)](./docs/connectors.md)

[English](README_EN.md) · [安装](docs/installation.md) · [快速开始](docs/quickstart.md) · [MCP 工具清单](docs/mcp-tools.md) · [学科体系](docs/disciplines.md) · [科学数据连接器](docs/connectors.md) · [贡献指南](CONTRIBUTING.md) · [行为准则](CODE_OF_CONDUCT.md) · [安全策略](SECURITY.md) · [变更日志](CHANGELOG.md)

</div>

---

## 这是什么

`sci-forge` 是一个**完全本地自建**的 [Model Context Protocol](https://modelcontextprotocol.io) server，把「读一篇论文」到「交出一篇可投稿论文」之间的整段路，压缩成一组可以被 AI 客户端直接调用的工具。

它不是聊天机器人，不是一段提示词模板，而是一个常驻进程：**1538 门学科的论文规范知识**、**46 个公开科学数据库的直连连接器**、**五步复现闭环**、**fail-closed 的完整性与引用核验门**，全部以 MCP 工具的形式暴露出来。

### 价值主张

| 你要做的事 | sci-forge 提供的 |
| --- | --- |
| 复现一篇论文的实验 | 拿到 PDF → 解析 → 抽超参 → 生成 numpy/torch 代码 → 沙箱运行 → 与论文数值比对 → 交付 `results.json` + 图 + 源码 |
| 从零写一篇论文 | 学科感知的章节结构模板（按 1538 门学科的 `paper_types`）+ 引导式撰写 + LaTeX/PDF/DOCX 导出 |
| 找选题、找缺口 | 免 key 的 OpenAlex/arXiv 检索 → 主题侦察 → 聚类 → 研究缺口 → 候选假设 → 实验计划 |
| 投出去之前自查 | 模拟同行评审（4 维评分）、期刊匹配度评分、修订教练、rebuttal 审计、期刊/会议推荐 |
| 守住学术诚信底线 | claim→source 核验、参考文献 DOI 批量核验、Stage 2.5 / 4.5 完整性门、Material Passport |
| 查跨库科学数据 | 46 个连接器、7 大领域，单库检索 / 跨库联查 / 并行批量检索 |

### 三个设计取向

1. **免 API key 可用。** 核心链路（文献检索、DOI 核验、元数据、引文图谱）走 OpenAlex / Crossref 的免鉴权公开接口。LLM 是**可选增强**：在 `.sci-forge/env` 写入 OpenAI 兼容端点即可启用；未配置时全部功能回退到本地模板，链路不中断。
2. **fail-closed 优先。** 评审准入门、完整性门、bypass 审批都遵循「证据不足即拒绝」而非「尽量放行」。
3. **声明式学科知识。** 学科 registry 全是数据不是逻辑，新增一门学科 = 新增一个 `.py` 文件，无需改动发现机制。

> 独立自建，仅使用公开材料与公开接口，不附属于、不依赖 SciForge 官方站点或 API，与 SciForge 及其商标无关联。

---

## 目录

- [快速开始](#快速开始)
- [架构](#架构)
- [MCP 工具清单](#mcp-工具清单75-个)
- [学科覆盖概览](#学科覆盖概览1538-门)
- [科学数据连接器](#科学数据连接器46-个)
- [与桌面版的关系](#与桌面版的关系双仓)
- [路线图](#路线图)
- [开发与测试](#开发与测试)
- [参与贡献](#参与贡献)
- [许可证](#许可证)

---

## 快速开始

### 前置条件

- Python **≥ 3.10**（CI 覆盖 3.11 / 3.12 / 3.13）
- 一个支持 MCP stdio transport 的客户端（opencode、Claude Code、Cursor 等）

### 安装

```bash
# 方式一：直接从 Git 装（最简）
pip install "git+https://github.com/liudongyan13701205717-source/sci-forge.git"

# 方式二：克隆后以可编辑模式安装（推荐用于开发）
git clone https://github.com/liudongyan13701205717-source/sci-forge.git
cd sci-forge
pip install -e ".[reproduce,dev]"

# 方式三：只要 MCP 本体，不带复现线的数值依赖
pip install -e .
```

| extra | 内容 | 何时需要 |
| --- | --- | --- |
| （无） | 仅 `mcp>=1.29.0` | 只想用学科 registry / 连接器 / 写作 / 评审 |
| `reproduce` | `pymupdf>=1.24`、`numpy>=1.26`、`matplotlib>=3.8` | 需要 PDF 解析、复现代码运行、绘图 |
| `export` | 目前无硬依赖；装了 LaTeX 引擎（`xelatex`/`pdflatex`）时用它，否则自动回退到内置 PyMuPDF 渲染 | 需要 PDF 导出 |
| `dev` | `pytest>=8.0` | 跑测试 |

### 注册为 MCP server

安装后得到 `sci-forge` 命令。它以 stdio transport 启动，因此配置里**不需要** `PYTHONPATH`，也**不需要**指定 `cwd`：

```jsonc
{
  "mcp": {
    "sci-forge": {
      "type": "local",
      "command": ["sci-forge"],
      "enabled": true
    }
  }
}
```

也可以直接用模块入口：`command` 设为 `["python", "-m", "sciforge"]`。

### 验证安装

```bash
sci-forge --version      # 打印 sci-forge 0.1.0
sci-forge --help         # 显示用法
SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q    # 268 个用例应全绿
```

### 60 秒试一次

在 MCP 客户端的对话里直接说，或手动调用工具：

```text
list_disciplines()                    # 看看内置了哪些学科
science_list_dbs("literature")        # 看看文献域有哪些库
ideate_paper("大语言模型的轻量化可解释方法", "demo")   # 选题 → 缺口 → 假设 → 实验计划
write_section("demo", "abstract", "为《边缘设备上的轻量推理》写摘要", "markdown")
export_document("demo", "pdf")        # 产出 .sci-forge/projects/demo/doc.pdf
```

更完整的端到端示例见 [docs/quickstart.md](./docs/quickstart.md) 与 [USAGE.md](./USAGE.md)。

---

## 架构

```
                        ┌─────────────────────────────────────────┐
                        │   MCP 客户端 (opencode / Claude Code…)    │
                        └───────────────────┬─────────────────────┘
                                            │ stdio (JSON-RPC)
                        ┌───────────────────▼─────────────────────┐
                        │  sciforge/server.py                      │
                        │  FastMCP("sci-forge")                    │
                        │  75 @mcp.tool  +  2 @mcp.resource        │
                        └──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┘
       ┌────────────────────┘   │   │   │   │   │   │   │   │   └──────────────┐
       ▼                        ▼   │   │   │   │   │   │   ▼                  ▼
 ┌───────────┐  ┌───────────┐  ┌────▼─┐ │ ┌─────▼─┐ │ ┌─────▼──┐  ┌──────────────────┐
 │reproduce/ │  │research/  │  │write/ │ │ │export/ │ │ │deliver/│  │  disciplines/    │
 │ 五步复现   │  │ 研究线     │  │DocStore│ │ │md→tex  │ │ │投稿打包 │  │  1538 门学科       │
 │ 闭环+点评  │  │ 工具集     │  │模板   │ │ │/pdf    │ │ │交付清单 │  │  零注册自动发现    │
 └───────────┘  └───────────┘  └───────┘ │ └───────┘ │ └────────┘  └──────────────────┘
                                           │ ┌─────▼──┐
                                           │ │review/ │ 7 席评审面板 + 准入门 + 报告指南
                                           │ └────────┘
                                           │ ┌─────▼──┐
                                           │ │claims/ │ claim→source 核验 + Stage2.5/4.5
                                           │ └────────┘   完整性门 + Material Passport
                                           │ ┌─────▼──┐
                                           │ │venue/  │ 期刊模板 + journal-fit 匹配
                                           │ └────────┘
                                           │ ┌─────▼──┐
                                           └─│science/│ 46 连接器 / 7 领域 / 5 工具
                                             └────────┘
                        ┌────────────────────────┴────────────────────────┐
                        │  core/  workspace_root() + Layout(.sci-forge)     │
                        │         + 可选 LLM 连接层（无端点则回退模板）      │
                        └─────────────────────────────────────────────────┘

 sciforge/parse/       PDF 解析（PyMuPDF，reproduce 线的前置）
 sciforge/__main__.py  python -m sciforge
 sciforge/cli.py       sci-forge 命令入口（stdio / --version / --help）
```

### 存储布局

运行产物统一落在工作区根目录下的 `.sci-forge/`（已 gitignore）：

```
.sci-forge/
├── env                          # 可选 LLM 端点配置（BASE_URL / API_KEY / MODEL），不提交
├── projects/{paper_id}/
│   ├── doc.md / doc.tex / doc.html / doc.pdf
│   ├── sections/                # 分章节中间产物
│   └── research/                # 研究产物 *.json / *.md，供复用与投稿打包
└── tasks/{task_id}/
    ├── parse/  code/  runs/     # 解析结果 / 生成代码 / 每次运行记录
    └── deliverables/            # 图、数据、源码、报告
```

### 可选增强：LLM

在 `.sci-forge/env` 写入 OpenAI 兼容端点：

```
BASE_URL=https://your-endpoint/v1
API_KEY=sk-...
MODEL=...
```

未配置时，`ideate_paper` / `write_section` / `peer_review` / `venue_suggest` 等工具自动回退到**本地模板**与规则引擎，全部功能保持可用，只是文本自然度下降。

---

## MCP 工具清单（75 个）

> 静态 `@mcp.tool()` 装饰器计数 75，运行时 `mcp.list_tools()` 计数 75，两者一致。另有 2 个 resource：静态 `science://databases` 与参数化模板 `science://databases/{domain}`。
> 逐个工具的参数签名与行为细节见 [docs/mcp-tools.md](./docs/mcp-tools.md)。

### 复现线（2）

| 工具 | 作用 |
| --- | --- |
| `reproduce_paper` | 论文复现五步闭环：解析 PDF → 方案 → 生成代码 → 沙箱运行比对 → 交付物 |
| `reproduce_status` | 查询复现任务异步状态与阶段进度 |

### 写作线（2）

| 工具 | 作用 |
| --- | --- |
| `write_section` | 按章节引导生成论文内容（abstract / problem / modeling / solution / results / references 等） |
| `export_document` | 将已写 doc 导出为 PDF / DOCX（LaTeX 源始终生成） |

### 研究线（3）

| 工具 | 作用 |
| --- | --- |
| `ideate_paper` | 构思选题 → 研究缺口 → 候选假设 → 多视角评审 → 实验计划 |
| `inject_results` | 把复现任务的真实实验结果并入论文对应章节 |
| `research_verdict` | 结果自旋门：PROCEED / REFINE / PIVOT 决策建议 |

### 科研/论文线（35）

| 工具 | 作用 |
| --- | --- |
| `research_plan` | 完整研究计划书（RQ / 假设 / 目标 / 贡献 / 方法 / 数据 / 指标 / 里程碑 / 风险） |
| `literature_review` | 基于 OpenAlex 免 key 检索生成综述框架（代表文献 / 聚类 / 缺口 / 结构） |
| `auto_title_abstract` | 从已写正文提炼标题 / 摘要 / 关键词 |
| `peer_review` | 模拟同行评审（novelty / rigor / clarity / soundness 4 维评分 + 推荐） |
| `venue_suggest` | 按主题推荐目标期刊 / 会议（内置映射库 + 可选 LLM） |
| `paper_polish` | 论文质量检查（completeness / consistency / grammar 三模式） |
| `compare_metrics` | 多任务 / 多基线指标对比表 + Welch t / Mann-Whitney U 检验 |
| `check_novelty` | 检索相似工作，给出重叠与候选差异点 |
| `citation_landscape` | 引文邻域与热度分析（年度分布 / 高被引代表 / 主要载体） |
| `project_memory` | 项目进度记账 timeline（note / milestone / status） |
| `review_code` | 复现代码静态点评（随机种子 / 硬编码 / 风险 + 可信度分） |
| `ref_to_bibtex` | 按 DOI 生成 BibTeX 条目 |
| `batch_ref_export` | 解析文本中的 DOI / 引用批量转 BibTeX |
| `recommend_papers` | 围绕研究主题推荐论文（可按 sources 过滤） |
| `prisma_review` | PRISMA 系统综述流程（识别 → 去重 → 筛选 → 资格 → 纳入 → 综合 → 文档） |
| `convert_citation` | BibTeX → 单一样式（apa / chicago-author-date / chicago-note-bibliography / mla / ieee / vancouver） |
| `convert_citation_all` | BibTeX 一次转全部 6 种样式 |
| `revision_coach` | 评审意见 → 结构化修订路线图（CRITICAL / MAJOR / MINOR） |
| `rebuttal_audit` | rebuttal 逐条回应审计（fail-closed） |
| `detect_style` | 机器文风检测（hedging 密度 + 模板句式 + 空洞连接词 → 0-100 分） |
| `claim_strength` | 表述强度阶梯（7 级）检测与无授权强度上移标记 |
| `calibrate_style` | 从已有正文学习作者声音画像（9 维） |
| `score_style_text` | 新文本与作者画像相似度评分（0-100） |
| `verify_citation` | 核验单个 DOI 真实性（Crossref，免 key） |
| `verify_claim` | 主张核验：检索证据判定 SUPPORTED / PARTIAL / UNSUPPORTED |
| `verify_reference_list` | 批量核验参考文献 DOI，返回 valid / invalid |
| `paper_metadata` | 经 Crossref 取标题 / 作者 / 年份 / 期刊 / 摘要 |
| `citation_graph` | 经 OpenAlex 取被引数与参考文献 |
| `download_paper_pdf` | 经 OpenAlex OA 定位并下载开放获取 PDF |
| `scout_topic` | 主题侦察：多源聚合 + 去重 + 评分排序 |
| `scout_compare` | 多主题横向对比（按命中数降序） |
| `rag_answer` | 检索增强问答（本地模板合成，无 LLM 依赖） |
| `rag_sources` | 仅检索并排序 RAG 来源（按被引降序） |
| `find_code_for_paper` | 论文找代码 / 数据集（HuggingFace / Zenodo） |
| `link_papers_to_code` | 主题论文批量关联代码 / 数据集 |

### 评审与核验线（10，其中 3 个为兼容别名）

| 工具 | 作用 |
| --- | --- |
| `run_panel` | 多视角同行评审面板（7 席，含 Devil's Advocate + 编辑综合） |
| `validate_review_intake` | 评审准入门 fail-closed 校验（授权 / 利益冲突 / 外部服务） |
| `select_reporting_guidelines` | 按研究设计选报告指南并做覆盖审计（带日期） |
| `validate_claims_evidence` | claim / evidence 对齐矩阵（ALIGNED / PARTIAL / UNSUPPORTED） |
| `verify` | claim → source 核验：解析 claims + 引文锚点，输出 gate_refuse |
| `gate_2_5` | 完整性门 Stage 2.5：代码生成 → 执行之间 |
| `gate_4_5` | 完整性门 Stage 4.5：结果 → 论文 / 交付之间 |
| `run_gates` | 一次性跑 2.5 + 4.5 两道门 |
| `request_bypass` | fail-closed bypass：无有效理由即拒绝放行 |
| `build_passport` | Material Passport：per-run 产物档案（experiment provenance + claim 审计 + 反面证据） |

兼容别名（功能与上表对应项一致，为旧客户端保留）：

| 别名 | 等价于 |
| --- | --- |
| `review_panel_intake` | `validate_review_intake` |
| `select_guidelines` | `select_reporting_guidelines` |
| `claims_evidence_matrix` | `validate_claims_evidence` |

### 交付线（2）

| 工具 | 作用 |
| --- | --- |
| `get_deliverables` | 列出某任务的交付物清单（图 / 数据 / 源码 / 报告） |
| `package_submission` | 投稿材料打包 zip（+ cover letter + checklist） |

### 科学数据线（5）

| 工具 | 作用 |
| --- | --- |
| `science_list_dbs` | 列出可用科学数据库，可按 7 大领域筛选 |
| `science_search` | 在指定数据库关键词检索 |
| `science_fetch` | 按记录 ID 取单条完整记录 |
| `science_cross_lookup` | 跨多库联合查询同一关键词 |
| `science_batch_search` | 多库并行执行同一查询并汇总 |

### 期刊匹配与学科（3）

| 工具 | 作用 |
| --- | --- |
| `journal_fit` | 论文与目标期刊 / 会议匹配度评分（领域 / 体裁 / 方法 / 结构 / 合规） |
| `list_disciplines` | 列出全部注册学科（`domain` 参数为预留位，当前不参与过滤） |
| `get_discipline` | 获取指定学科完整 v2 配置 |

### MCP 资源（2）

| URI | 类型 | 内容 |
| --- | --- | --- |
| `science://databases` | 静态资源 | 全部 46 个连接器清单 + 7 个领域 |
| `science://databases/{domain}` | 参数化模板 | 单个领域下的连接器清单 |

### 已知限制

- `science_fetch` 名义上覆盖 46 个库，**当前仅 `uniprot` 实现了 `fetch` 回调**，其余 45 个库只能通过 `science_search` 使用。
- `list_disciplines` 的 `domain` 参数当前被忽略，尚未实现按领域过滤。
- `citation_graph` 的 `depth` 参数当前只展开一层。

---

## 学科覆盖概览（1538 门）

`sciforge/disciplines/` 内置 **1538 门学科**的论文支持 registry，采用零注册自动发现：新增学科 = 在该包内新增一个模块文件并声明一个模块级 `Discipline` 实例（或 `Discipline` 数据类子类），发现机制会自动收录，无需修改 registry 代码。

### 门类分布

`category` 字段取中国学科门类命名，共 14 个取值，**精确计数**如下：

| 门类 | 学科数 | 门类 | 学科数 |
| --- | --- | --- | --- |
| 理学 | 87 | 军事学 | 5 |
| 工学 | 56 | 农学 | 4 |
| 医学 | 30 | 历史学 | 4 |
| 交叉学科 | 23 | 教育学 | 4 |
| 法学 | 12 | 经济学 | 3 |
| 文学 | 11 | **合计** | **1538** |
| 哲学 | 9 | | |
| 管理学 | 7 | | |
| 艺术学 | 6 | | |

> ⚠️ 统计口径提示：`list_by_category()` 使用**子串**匹配，`list_by_category("理学")` 会一并命中 `管理学`（其字面包含「理学」），返回数大于上表的精确值。做门类统计时请用精确相等，或对结果自行去重。

### 产出形式

`contribution_forms` 字段取 10 个固定取值（`sciforge/disciplines/contribution_forms.py`）：

| 产出形式 | 包含该形式的学科数 | 产出形式 | 学科数 |
| --- | --- | --- | --- |
| 论文 | 1538（100%） | 报告 | 27 |
| 数据集 | 95 | 艺术作品 | 7 |
| 软件与代码 | 49 | 文学作品 | 5 |
| 学术专著 | 41 | 译文 | 4 |
| 专利 | 35 | 教案与教材 | 3 |

形式数量分布：1 种 37 门、2 种 182 门、3 种 42 门；无学科超过 3 种。

### 优先论文库绑定

`databases` 字段共 22 个取值，覆盖度呈长尾分布：

| 数据库 | 学科数 | 数据库 | 学科数 |
| --- | --- | --- | --- |
| OpenAlex | 255 | DOAJ | 11 |
| Crossref | 213 | HuggingFace | 6 |
| CNKI | 162 | Ensembl | 4 |
| arXiv | 94 | ChEMBL | 2 |
| 万方 | 68 | UniProt | 2 |
| PubMed | 63 | ClinVar | 1 |
| Semantic Scholar | 58 | Expression Atlas | 1 |
| Zenodo | 58 | Human Protein Atlas | 1 |
| Europe PMC | 31 | RCSB PDB | 1 |
| PubChem | 16 | Reactome | 1 |
| GEO | 13 | | |
| bioRxiv | 12 | | |

### 字段清单

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `name` | `str` | 学科主键，英文小写 snake_case |
| `aliases` | `tuple[str, ...]` | 别名与检索关键词（中英文） |
| `paper_types` | `dict[str, tuple[str, ...]]` | 体裁 → 章节结构 |
| `citation_style` | `str` | 主引用样式 |
| `reporting_standards` | `dict[str, str]` | 报告规范路由（设计/主题 → 标准名） |
| `conventions` | `tuple[str, ...]` | 写作约定（定理环境、符号、图表、术语） |
| `key_venues` | `tuple[str, ...]` | 代表性顶刊 / 顶会 |
| `units_and_formulas_notes` | `tuple[str, ...]` | 单位与公式注记 |
| `paper_capable` | `bool` | 是否以论文为主要产出 |
| `contribution_forms` | `tuple[str, ...]` | 产出形式（可多值） |
| `tools` | `tuple[str, ...]` | 该学科用到的软件 / 仪器 / 方法平台 |
| `category` | `str` | 学科门类 |
| `databases` | `tuple[str, ...]` | 优先论文库 / 数据库 |

### Python API

```python
from sciforge.disciplines import (
    DISCIPLINES,                 # dict[str, Discipline]，键为小写学科名
    list_disciplines,            # 全部学科，按名排序
    get_discipline,              # 按名或别名查（大小写不敏感）
    list_by_category,            # 按门类过滤（子串匹配）
    list_by_contribution_form,   # 按产出形式过滤
    list_by_tool,                # 按工具过滤
    list_by_database,            # 按优先数据库过滤
)

len(DISCIPLINES)                    # 1538
d = get_discipline("machine_learning")
d.contribution_forms               # ('论文', '软件与代码', '数据集')
list_by_contribution_form("专利")   # 可产出专利的学科
list_by_tool("PyTorch")            # 绑定 PyTorch 的学科
list_by_database("PubMed")         # 优先 PubMed 的学科
```

字段级细节与扩编指引见 [docs/disciplines.md](./docs/disciplines.md)。

---

## 科学数据连接器（46 个）

`sciforge/science/` 通过 46 个连接器覆盖 7 个领域的公开科学数据库，均以公开接口访问；其中 3 个可选地读取环境变量以启用额外能力。

| 领域 | 数量 | 连接器 id |
| --- | --- | --- |
| `literature` | 12 | `openalex`、`arxiv`、`biorxiv`、`crossref`、`europepmc`、`pubmed`、`semantic-scholar`、`unpaywall`、`core`、`opencitations-coci`、`cnki`、`wanfang` |
| `proteins` | 6 | `uniprot`、`rcsb-pdb`、`pdbe`、`alphafold`、`interpro`、`sifts` |
| `chemistry` | 6 | `chembl`、`pubchem`、`chebi`、`bindingdb`、`gtopdb`、`surechembl` |
| `genomics` | 7 | `ensembl`、`eutils`、`mygene`、`myvariant`、`clinvar`、`dbsnp`、`gnomad` |
| `pathways` | 5 | `biogrid`、`intact`、`kegg`、`opentargets`、`reactome` |
| `omics` | 6 | `arrayexpress`、`depmap`、`expression-atlas`、`geo`、`gtex`、`hpa` |
| `datasets` | 4 | `zenodo`、`doaj`、`openaire`、`huggingface` |
| **合计** | **46** | |

### 可选环境变量

| 变量 | 影响的连接器 | 未配置时 |
| --- | --- | --- |
| `CORE_API_KEY` | `core` | 返回空结果，不报错 |
| `CNKI_API_URL` | `cnki` | 返回空结果，不报错 |
| `WANFANG_API_URL` | `wanfang` | 返回空结果，不报错 |
| `SCI_FORGE_OFFLINE=1` | 全部 | 强制离线，测试与 CI 使用 |

逐个连接器的检索端点、返回字段与已知缺口见 [docs/connectors.md](./docs/connectors.md)。

---

## 与桌面版的关系（双仓）

本仓库 `sci-forge` 是 **MCP 版**（核心库 + server），与并列的 **桌面版** `sciforge-desktop`（PySide6 客户端）构成一对双仓工程。

| 维度 | `sci-forge`（本仓，MCP 版） | `sciforge-desktop`（桌面版） |
| --- | --- | --- |
| 定位 | 核心库 + MCP stdio server | 桌面 GUI 客户端 + 本地 agent 工具 |
| 提供能力 | 75 个 MCP 工具、2 个 MCP 资源、1538 门学科、46 个连接器 | 6 个本地 agent 工具、会话存储、GUI 外壳 |
| Python 依赖 | `mcp>=1.29.0` | `PySide6>=6.6` |
| 命令 | `sci-forge` | `sciforge-desktop` |
| 通信方式 | 被调用方（stdio server） | 调用方（JSON-RPC 2.0 over stdio） |

### 协作约定：共享核心，默认一起改

- **共享核心。** 两仓面向同一套领域模型：学科 registry、连接器目录、工具语义、`.sci-forge` 存储布局。桌面版通过 MCP 协议消费核心能力，而不是复制一份实现。
- **默认一起改。** 凡是会改变工具签名、工具语义、返回结构、学科字段或存储布局的改动，**默认同时在两个仓库落地**，以免两侧漂移。
- **单仓改动的例外。** 仅 UI 层、GUI 交互、打包与平台相关的改动可以只在一侧进行；这类 PR 需在描述中注明「不影响 MCP 契约」。

> 观测记录（盘点日期 2026-09-26）：截至该日期两仓尚未建立代码级同步机制 —— `sciforge-desktop` 的 `pyproject.toml` 未声明对 `sci-forge` 的依赖，其 `core/` 目录为空占位，核心一致性目前靠约定而非机制保证。建立该同步机制属于后续工作项。

---

## 路线图

以下为**计划方向**，不代表已排期或已承诺的时间点。

### 已具备

- 1538 门学科 registry（Discipline v2 字段体系）
- 46 个科学数据库连接器 / 7 领域
- 75 个 MCP 工具 + 2 个 MCP 资源
- 复现 / 写作 / 研究 / 评审核验 / 交付 / 科学数据 六条线闭环
- 268 个 pytest 用例（v2 回归基线）
- 免 key 可用的核心链路 + 可选 LLM 增强

### 进行中

- 文档体系：README 双语化、`docs/` 面向用户文档、贡献与安全流程、CI 与发布自动化
- 双仓契约（桌面版消费 MCP 核心）落地

### 计划中

- `science_fetch` 覆盖率从 1/46 扩到主流库可用
- 学科工具名归一化（当前 597 个不同工具字符串中有 504 个只出现 1 次，命名碎片化明显）
- `list_disciplines` 的 `domain` 过滤与 `citation_graph` 的多层展开
- 覆盖率与静态类型配置（`ruff` / `mypy` / `coverage`）纳入 CI 门禁
- PyPI 发布流程

### 明确不做

- 不依赖任何闭源商业检索服务作为默认后端
- 不在无 LLM 配置时阻断任何工具调用

---

## 开发与测试

```bash
git clone https://github.com/liudongyan13701205717-source/sci-forge.git
cd sci-forge
pip install -e ".[reproduce,dev]"

# 全量测试（离线可跑：文献与复现用桩数据）
SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q

# 只收集不执行
SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q --collect-only

# 只跑某个文件
SCI_FORGE_OFFLINE=1 python -m pytest tests/test_science_api.py -q
```

CI（`.github/workflows/ci.yml`）在 Python 3.11 / 3.12 / 3.13 上执行 `ruff` lint 与上述 pytest 命令。

当前测试布局：26 个测试文件、268 个被 pytest 收集的用例，覆盖四条线的单元测试、真实 spawn MCP server 的 stdio 端到端测试、以及科学数据连接器测试。

贡献流程、分支规范、提交信息规范与双仓同步约定见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

---

## 参与贡献

- **报告 bug / 提需求**：走 [GitHub Issues](https://github.com/liudongyan13701205717-source/sci-forge/issues)，或使用 `.github/ISSUE_TEMPLATE/` 下的模板。
- **安全漏洞**：**不要**开公开 issue，按 [SECURITY.md](./SECURITY.md) 走私下报告渠道。
- **提交代码**：Fork → 分支 → PR。提交前请确保 `SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q` 全绿。
- **参与讨论**：所有人须遵守 [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)（Contributor Covenant v2.1）。
- **赞助与支持**：见 [.github/SUPPORT.md](./.github/SUPPORT.md)。

---

## 许可证

[Apache License 2.0](./LICENSE) — Copyright 2026 liudongyan13701205717

<sub>本项目为独立开发的教育 / 研究工作，与 SciForge 及其商标无关联。所有外部数据库与 API 的版权归各自权利人所有；本项目仅通过公开接口访问其数据。</sub>
