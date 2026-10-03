# 变更日志

本文件记录 **sci-forge** 的重要变更。

格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### 新增
- 双语文档套件：`README.md`（中文）与 `README_EN.md`（英文，结构一一对应）
- 面向用户的文档集：`docs/index.md`、`docs/installation.md`、`docs/quickstart.md`、`docs/mcp-tools.md`、`docs/disciplines.md`、`docs/connectors.md`
- 社区治理文件：`CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`（Contributor Covenant v2.1）、`SECURITY.md`
- GitHub 协作配置：issue 模板（bug / feature / question）、PR 模板、`CODEOWNERS`、`SUPPORT.md`、`FUNDING.yml`、`dependabot.yml`
- 持续集成与发布工作流：`.github/workflows/ci.yml`、`.github/workflows/release.yml`

### 变更
- 许可证由 MIT 更换为 **Apache License 2.0**（Copyright 2026 liudongyan13701205717）
- README 重写：补充架构图、存储布局、完整工具表、学科门类与产出形式统计、连接器清单、双仓关系、路线图
- 明确对外表述：独立自建，与 SciForge 官方站点 / API / 商标无关联

### 文档
- 补充已知限制章节：`science_fetch` 当前仅 `uniprot` 实现回调；`list_disciplines` 的 `domain` 参数当前未参与过滤；`citation_graph` 的 `depth` 当前只展开一层
- 标注 `list_by_category()` 为子串匹配，`list_by_category("理学")` 会一并命中 `管理学`
- 所有会随时间变化的观测均附观测日期（当前为 2026-09-26）

## [2.0.0] - 2026-09-26

Discipline v2 与科研工具链成型：学科 registry 全量重写，科学数据连接器成体系，复现 / 写作 / 评审 / 交付四条线闭环。

### 新增

#### 学科体系（Discipline v2）
- 学科 registry 扩展至 **261 门学科**，覆盖 14 个学科门类
- 引入 v2 字段体系：`name`、`aliases`、`paper_types`、`citation_style`、`reporting_standards`、`conventions`、`key_venues`、`units_and_formulas_notes`、`paper_capable`、`contribution_forms`、`tools`、`category`、`databases`
- 固定 10 个产出形式取值：论文、数据集、软件与代码、学术专著、专利、报告、艺术作品、文学作品、译文、教案与教材
- 22 个优先论文库绑定取值，OpenAlex（255 门）与 Crossref（213 门）为覆盖面最广的两个
- 零注册自动发现：新增学科 = 新增一个模块文件，无需改动发现机制
- 查询 API：`list_disciplines`、`get_discipline`、`list_by_category`、`list_by_contribution_form`、`list_by_tool`、`list_by_database`
- 对应 MCP 工具：`list_disciplines`、`get_discipline`

#### 科学数据连接器
- 新增 **46 个连接器 / 7 个领域**：`literature`(12)、`proteins`(6)、`chemistry`(6)、`genomics`(7)、`pathways`(5)、`omics`(6)、`datasets`(4)
- 领域聚合能力：`science_cross_lookup`（跨库联查）、`science_batch_search`（并行批量检索）
- 新增 2 个 MCP 资源：静态 `science://databases` 与参数化模板 `science://databases/{domain}`
- 3 个连接器支持可选环境变量：`CORE_API_KEY`、`CNKI_API_URL`、`WANFANG_API_URL`；未配置时返回空结果而非抛异常
- `SCI_FORGE_OFFLINE=1` 强制离线模式，供测试与 CI 使用

#### MCP 工具面
- 工具总数达到 **65 个**（`@mcp.tool()` 静态计数与运行时 `list_tools()` 计数一致），另有 **2 个 resource**
- 复现线：`reproduce_paper`（五步闭环）、`reproduce_status`、`review_code`、`inject_results`
- 写作线：`write_section`（学科感知模板）、`export_document`（LaTeX / PDF / DOCX / HTML）
- 研究线：`ideate_paper`、`literature_review`、`research_plan`、`scout_topic`、`scout_compare`、`rag_answer`、`rag_sources`
- 评审核验线：`run_panel`（7 席评审面板，含 Devil's Advocate 与编辑综合）、`validate_review_intake`、`select_reporting_guidelines`、`validate_claims_evidence`、`verify`、`gate_2_5`、`gate_4_5`、`run_gates`、`request_bypass`
- 期刊匹配：`journal_fit`、`venue_suggest`
- 引文与文献管理：`ref_to_bibtex`、`batch_ref_export`、`convert_citation`、`convert_citation_all`、`verify_citation`、`verify_reference_list`、`paper_metadata`、`citation_graph`、`download_paper_pdf`、`citation_landscape`、`check_novelty`、`recommend_papers`、`prisma_review`
- 文风与论证：`detect_style`、`claim_strength`、`calibrate_style`、`score_style_text`
- 交付：`get_deliverables`、`package_submission`（含 cover letter 与 checklist）
- 复现后处理：`research_verdict`（PROCEED / REFINE / PIVOT）
- 论文润色与统计：`paper_polish`、`compare_metrics`（Welch t / Mann-Whitney U）、`auto_title_abstract`、`project_memory`、`revision_coach`、`rebuttal_audit`
- 代码与数据关联：`find_code_for_paper`、`link_papers_to_code`
- 3 个兼容别名保留给旧客户端：`review_panel_intake`、`select_guidelines`、`claims_evidence_matrix`

#### 完整性门与诚信核验
- Stage 2.5 完整性门：代码生成 → 执行之间
- Stage 4.5 完整性门：结果 → 论文 / 交付之间
- `run_gates` 一次跑完两道门
- `request_bypass` 采用 fail-closed：无有效理由即拒绝放行
- Material Passport 记录产物的来源与可追溯信息
- `verify_reference_list` 批量核验参考文献 DOI，返回 valid / invalid

#### 存储与工程
- 统一存储布局 `core/Layout`：`.sci-forge/env`、`projects/{paper_id}/`、`tasks/{task_id}/`（`parse/`、`code/`、`runs/`、`deliverables/`）
- 可选 LLM 增强层：读取 `.sci-forge/env` 中的 OpenAI 兼容端点；**未配置时全部功能回退本地模板，链路不中断**
- 免 API key 可用的核心链路：文献检索、DOI 核验、元数据、引文图谱走 OpenAlex / Crossref 公开接口
- 发行包名 `sci-forge`，导入包名 `sciforge`，命令行入口 `sci-forge = "sciforge.cli:main"`
- `python -m sciforge` 模块入口
- `sci-forge --version` / `sci-forge --help`
- 可选 extras：`reproduce`（pymupdf / numpy / matplotlib）、`export`、`dev`（pytest）
- Python 要求 `>=3.10`；构建后端 setuptools>=68
- 26 个测试文件、**268 个 pytest 用例**作为 v2 回归基线，含真实 spawn MCP server 的 stdio 端到端测试

### 已知限制（v2.0.0 时点）
- `science_fetch` 名义覆盖 46 个库，实际仅 `uniprot` 实现了 `fetch` 回调
- `list_disciplines` 的 `domain` 参数未参与过滤
- `citation_graph` 的 `depth` 参数只展开一层
- 学科 `tools` 字段存在 597 个不同字符串，其中 504 个只出现 1 次，命名碎片化明显
- 学科门类统计需注意 `list_by_category()` 为子串匹配

### 破坏性变更
- 许可证：MIT → Apache-2.0
- 3 个工具更名为带语义前缀的名称，原名保留为兼容别名：`review_panel_intake` → `validate_review_intake`、`select_guidelines` → `select_reporting_guidelines`、`claims_evidence_matrix` → `validate_claims_evidence`

---

## 关于版本号

- 本变更日志按**发布线**组织：`2.x` 表示 Discipline v2 与当前工具契约，`1.x` 为其之前的发布线。
- `pyproject.toml` 与 `sciforge.__version__` 中的 `version` 字段是**打包版本**，当前为 `0.1.0`，与发布线编号并非同一套编号。
- 两者的对齐属于待办事项（见 [路线图](./README.md#路线图)），本次未修改源码版本。

[Unreleased]: https://github.com/liudongyan13701205717-source/sci-forge/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/liudongyan13701205717-source/sci-forge/releases/tag/v2.0.0
