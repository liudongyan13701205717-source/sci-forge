# MCP 工具清单（65 个）

> 本文档由 `sciforge/server.py` 自动生成，记录所有 `@mcp.tool()` 装饰的 MCP 工具。
> 静态计数 65，运行时 `mcp.list_tools()` 计数 65，两者一致。

## 工具总表

| # | 工具名 | 功能简述 | 参数 | 返回值 |
| --- | --- | --- | --- | --- |
| 1 | `reproduce_paper` | 论文复现五步闭环：解析 PDF → 复现方案 → 生成代码 → 沙箱运行比对 → 产出交付物。 | pdf_path: str, framework: str | dict |
| 2 | `reproduce_status` | 查询论文复现任务的异步状态与阶段进度。 | task_id: str | dict |
| 3 | `write_section` | 论文写作助力：按章节引导生成内容（摘要/问题/假设/符号/建模/求解/结果/参考文献/附录）。 | paper_id: str, section: str, prompt: str, format: str | dict |
| 4 | `export_document` | 论文写作助力：将已写 doc（markdown）导出为 LaTeX / PDF / docx。 | paper_id: str, target: str | dict |
| 5 | `get_deliverables` | 端到端交付：列出某任务（复现/写作）的交付物清单（图/数据/源码/报告）。 | task_id: str | dict |
| 6 | `ideate_paper` | 研究起点：由研究方向构思选题，产出研究缺口、候选假设、多视角评审与实验计划。 | topic: str, paper_id: str | dict |
| 7 | `inject_results` | 将复现任务的真实实验结果并入论文对应章节（实验数据→论文）。 | paper_id: str, task_id: str, section: str | dict |
| 8 | `research_verdict` | 结果分析自旋门：根据复现产物给出 PROCEED/REFINE/PIVOT 决策建议。 | task_id: str | dict |
| 9 | `research_plan` | 研究计划书：由选题展开成完整研究计划（RQ/假设/目标/贡献/方法/数据/ | topic: str, paper_id: str | dict |
| 10 | `literature_review` | 文献综述：基于免 key OpenAlex 检索生成综述框架（代表文献/主题聚类/ | topic: str, paper_id: str | dict |
| 11 | `auto_title_abstract` | 标题/摘要/关键词提炼：从已写正文自动生成投稿所需元数据。 | paper_id: str | dict |
| 12 | `peer_review` | 模拟同行评审：对已有论文生成结构化审稿意见（novelty/rigor/clarity/ | paper_id: str | dict |
| 13 | `venue_suggest` | 投稿建议：根据主题/关键词推荐目标期刊与会议（内置映射库 + 可选 LLM）。 | topic: str, paper_id: str | dict |
| 14 | `paper_polish` | 论文润色与检查：对已有正文做质量检查并产出建议。 | paper_id: str, mode: str | dict |
| 15 | `compare_metrics` | 对比表与显著性检验：汇总多个任务/基线的指标序列并做检验。 | paper_id: str, tasks: list[str], baseline: str, metric: str | dict |
| 16 | `check_novelty` | 创新性检查：从标题/摘要抽关键词检索相似工作，给出重叠与候选差异点。 | paper_id: str, max_papers: int | dict |
| 17 | `package_submission` | 投稿材料一键打包：把论文导出物与研究/复现产物打成 zip（含 cover letter）。 | paper_id: str, task_id: str | dict |
| 18 | `citation_landscape` | 引文邻域与热度分析：围绕 DOI 或主题分析热度/年度分布/高被引代表。 | paper_id: str, doi_or_topic: str | dict |
| 19 | `project_memory` | 项目进度记账：为论文/项目维护可回溯 timeline（备忘/里程碑/状态）。 | paper_id: str, action: str, note: str, milestone: str, status: str | dict |
| 20 | `review_code` | 复现代化码静态点评：对任务下的 .py 做风格/风险/可复现性检查。 | task_id: str | dict |
| 21 | `science_list_dbs` | 列出当前可用的科学数据库（跨 7 大领域，共 41 个），可按领域筛选。 | domain: str | dict |
| 22 | `science_search` | 在指定科学数据库中进行关键词检索。 | database: str, query: str, limit: int | dict |
| 23 | `science_fetch` | 按记录 ID 从指定科学数据库获取单条完整记录。 | database: str, id: str, format: str | dict |
| 24 | `science_cross_lookup` | 跨多个科学数据库联合查询同一关键词。 | query: str, databases: list[str] \| None, limit: int | dict |
| 25 | `science_batch_search` | 批量跨库检索：在多个数据库上并行执行同一查询并汇总结果。 | query: str, databases: list[str] \| None, limit: int | dict |
| 26 | `ref_to_bibtex` | 按 DOI 生成 BibTeX 条目。 | doi: str | dict |
| 27 | `batch_ref_export` | 批量导出参考文献：解析文本中的 DOI/引用，转成 BibTeX 条目。 | text: str | dict |
| 28 | `recommend_papers` | 围绕研究主题推荐论文。 | topic: str, limit: int, sources: list[str] \| None | dict |
| 29 | `run_panel` | 多视角同行评审面板（7 席位：field_analyst/eic/methodology_R1/domain_R2/perspective_R3/devils_advocate/editorial_synthesizer）。 | text: str, mode: str, journal: str, design: str, adjudications: dict \| None, author_response: str, gold_set: list \| None, paper_id: str, layout | dict |
| 30 | `validate_review_intake` | 评审准入门：校验评审请求是否满足本地评审前置条件（fail-closed）。 | intake: dict | dict |
| 31 | `select_reporting_guidelines` | 按研究设计选择报告指南并做覆盖审计（非计分、带日期）。 | design: str, text: str, as_of: str | dict |
| 32 | `validate_claims_evidence` | claim/evidence 对齐矩阵：每条 claim 判定 ALIGNED / PARTIAL / UNSUPPORTED。 | claims: list, evidence: list | dict |
| 33 | `review_panel_intake` | 评审准入门（兼容旧名，等同 validate_review_intake）。 | intake: dict | dict |
| 34 | `select_guidelines` | 报告指南选择（兼容旧名，等同 select_reporting_guidelines）。 | design: str, text: str, as_of: str | dict |
| 35 | `claims_evidence_matrix` | claim/evidence 对齐矩阵（兼容旧名，等同 validate_claims_evidence）。 | claims: list, evidence: list | dict |
| 36 | `verify` | claim→source 核验：解析 doc.md 中 claims + 引文（含锚点），5 类锚点分类，输出 gate_refuse。 | text: str, sources: dict \| None | dict |
| 37 | `gate_2_5` | 完整性门 Stage 2.5：代码生成 → 执行之间的完整性门。 | context: dict | dict |
| 38 | `gate_4_5` | 完整性门 Stage 4.5：结果 → 论文/交付之间的完整性门。 | context: dict | dict |
| 39 | `run_gates` | 一次性跑两道完整性门（2.5 + 4.5）。 | context: dict | dict |
| 40 | `request_bypass` | fail-closed bypass：无理由拒绝放行；有理由记录放行。 | gate: dict, reason: str | dict |
| 41 | `build_passport` | Material Passport（per-run artifact）：含 experiment provenance + claim 审计。 | task_id: str, results: dict \| None, runs: list \| None, claims: list \| None, gate_results: dict \| None, hypothesis: str, negative_results: list \| None, doc_text: str, as_of: str | dict |
| 42 | `journal_fit` | journal-fit 评分：论文与目标期刊/会议的匹配度（领域/体裁/方法/结构/合规）。 | paper_text: str, venue: str | dict |
| 43 | `list_disciplines` | 列出当前注册的学科（自动发现，零注册即可发现）。 | domain: str | dict |
| 44 | `get_discipline` | 获取指定学科的完整配置（结构体裁/引用样式/报告标准/顶刊/单位公式）。 | name: str | dict |
| 45 | `prisma_review` | PRISMA 系统综述：7 阶段协议（规划→多库检索→筛选→全文评估→主题综合→引文核验→文档生成），带流程计数。 | topic: str, hits: list[dict] \| None, databases: list[str] \| None, limit: int, include_keywords: list[str] \| None, exclude_keywords: list[str] \| None, paper_id: str, persist: bool | dict |
| 46 | `convert_citation` | 引用样式转换：解析 BibTeX 条目并渲染为指定样式。 | bibtex: str, style: str | dict |
| 47 | `convert_citation_all` | 引用样式一键转换：BibTeX → 全部 6 种样式（APA/Chicago×2/MLA/IEEE/Vancouver）。 | bibtex: str | dict |
| 48 | `revision_coach` | 修订教练：评审意见 → 结构化路线图（comment→类型 CRITICAL/MAJOR/MINOR→位置→回应计划）。 | comments_text: str, paper_id: str | dict |
| 49 | `rebuttal_audit` | rebuttal 审计：逐条检查 rebuttal 是否回应了每条评审意见（fail-closed）。 | rebuttal_text: str, comments: str, paper_id: str | dict |
| 50 | `detect_style` | 机器文风检测：hedging 密度 + 模板化句式 + 空洞连接词 → 0-100 分 + 证据列表。 | text: str | dict |
| 51 | `claim_strength` | claim-strength ladder：检测表述强度（associated<predicts<causes）与无授权的强度上移。 | text: str | dict |
| 52 | `calibrate_style` | 风格校准：从已有正文学习作者声音画像（句长分布/用词偏好/结构习惯）。 | text: str | dict |
| 53 | `score_style_text` | 文风评分：新文本与作者画像的相似度（0-100，越高越接近作者声音）。 | text: str, profile: dict | dict |
| 54 | `verify_citation` | 引用核验：核验单个 DOI 是否真实存在（Crossref）。离线可用、免 key。 | doi: str | dict |
| 55 | `verify_claim` | 主张核验：检索 OpenAlex 支持证据并判定 SUPPORTED/PARTIAL/UNSUPPORTED。离线可用、免 key。 | claim: str, topic: str, limit: int | dict |
| 56 | `verify_reference_list` | 批量引用核验：逐条核验参考文献 DOI。离线可用、免 key。 | refs: list[str] | dict |
| 57 | `paper_metadata` | 论文元数据：经 Crossref 获取标题/作者/年份/期刊/摘要。离线可用、免 key。 | doi: str | dict |
| 58 | `citation_graph` | 引用图谱：经 OpenAlex 获取被引数与参考文献。离线可用、免 key。 | doi: str, depth: int | dict |
| 59 | `download_paper_pdf` | 论文 PDF 下载：经 OpenAlex OA 定位并下载开放获取 PDF。离线可用、免 key。 | doi: str, out_dir: str | dict |
| 60 | `scout_topic` | 主题侦察：多源聚合检索 + 去重 + 评分排序（被引/新近度/关键词）。离线可用、免 key。 | topic: str, limit: int | dict |
| 61 | `scout_compare` | 主题对比：多主题横向对比（按命中数降序）。离线可用、免 key。 | topics: list[str], limit: int | dict |
| 62 | `rag_answer` | 检索增强问答：检索相关文献并用本地模板合成答案（无 LLM）。离线可用、免 key。 | question: str, topic: str, limit: int | dict |
| 63 | `rag_sources` | RAG 来源：仅检索并排序相关来源（按被引降序）。离线可用、免 key。 | question: str, limit: int | dict |
| 64 | `find_code_for_paper` | 论文找代码：定位论文并检索关联代码/数据集（HuggingFace/Zenodo）。离线可用、免 key。 | title: str, limit: int | dict |
| 65 | `link_papers_to_code` | 主题找代码：主题论文批量关联代码/数据集。离线可用、免 key。 | topic: str, limit: int | dict |

## 按功能线分组

### 复现线

| 工具名 | 功能简述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `reproduce_paper` | 论文复现五步闭环：解析 PDF → 复现方案 → 生成代码 → 沙箱运行比对 → 产出交付物。 | pdf_path: str, framework: str | dict |
| `reproduce_status` | 查询论文复现任务的异步状态与阶段进度。 | task_id: str | dict |

### 写作线

| 工具名 | 功能简述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `write_section` | 论文写作助力：按章节引导生成内容（摘要/问题/假设/符号/建模/求解/结果/参考文献/附录）。 | paper_id: str, section: str, prompt: str, format: str | dict |
| `export_document` | 论文写作助力：将已写 doc（markdown）导出为 LaTeX / PDF / docx。 | paper_id: str, target: str | dict |

### 研究线

| 工具名 | 功能简述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `ideate_paper` | 研究起点：由研究方向构思选题，产出研究缺口、候选假设、多视角评审与实验计划。 | topic: str, paper_id: str | dict |
| `inject_results` | 将复现任务的真实实验结果并入论文对应章节（实验数据→论文）。 | paper_id: str, task_id: str, section: str | dict |
| `research_verdict` | 结果分析自旋门：根据复现产物给出 PROCEED/REFINE/PIVOT 决策建议。 | task_id: str | dict |

### 科研/论文线

| 工具名 | 功能简述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `research_plan` | 研究计划书：由选题展开成完整研究计划（RQ/假设/目标/贡献/方法/数据/ | topic: str, paper_id: str | dict |
| `literature_review` | 文献综述：基于免 key OpenAlex 检索生成综述框架（代表文献/主题聚类/ | topic: str, paper_id: str | dict |
| `auto_title_abstract` | 标题/摘要/关键词提炼：从已写正文自动生成投稿所需元数据。 | paper_id: str | dict |
| `peer_review` | 模拟同行评审：对已有论文生成结构化审稿意见（novelty/rigor/clarity/ | paper_id: str | dict |
| `venue_suggest` | 投稿建议：根据主题/关键词推荐目标期刊与会议（内置映射库 + 可选 LLM）。 | topic: str, paper_id: str | dict |
| `paper_polish` | 论文润色与检查：对已有正文做质量检查并产出建议。 | paper_id: str, mode: str | dict |
| `compare_metrics` | 对比表与显著性检验：汇总多个任务/基线的指标序列并做检验。 | paper_id: str, tasks: list[str], baseline: str, metric: str | dict |
| `check_novelty` | 创新性检查：从标题/摘要抽关键词检索相似工作，给出重叠与候选差异点。 | paper_id: str, max_papers: int | dict |
| `citation_landscape` | 引文邻域与热度分析：围绕 DOI 或主题分析热度/年度分布/高被引代表。 | paper_id: str, doi_or_topic: str | dict |
| `project_memory` | 项目进度记账：为论文/项目维护可回溯 timeline（备忘/里程碑/状态）。 | paper_id: str, action: str, note: str, milestone: str, status: str | dict |
| `review_code` | 复现代化码静态点评：对任务下的 .py 做风格/风险/可复现性检查。 | task_id: str | dict |
| `ref_to_bibtex` | 按 DOI 生成 BibTeX 条目。 | doi: str | dict |
| `batch_ref_export` | 批量导出参考文献：解析文本中的 DOI/引用，转成 BibTeX 条目。 | text: str | dict |
| `recommend_papers` | 围绕研究主题推荐论文。 | topic: str, limit: int, sources: list[str] \| None | dict |
| `prisma_review` | PRISMA 系统综述：7 阶段协议（规划→多库检索→筛选→全文评估→主题综合→引文核验→文档生成），带流程计数。 | topic: str, hits: list[dict] \| None, databases: list[str] \| None, limit: int, include_keywords: list[str] \| None, exclude_keywords: list[str] \| None, paper_id: str, persist: bool | dict |
| `convert_citation` | 引用样式转换：解析 BibTeX 条目并渲染为指定样式。 | bibtex: str, style: str | dict |
| `convert_citation_all` | 引用样式一键转换：BibTeX → 全部 6 种样式（APA/Chicago×2/MLA/IEEE/Vancouver）。 | bibtex: str | dict |
| `revision_coach` | 修订教练：评审意见 → 结构化路线图（comment→类型 CRITICAL/MAJOR/MINOR→位置→回应计划）。 | comments_text: str, paper_id: str | dict |
| `rebuttal_audit` | rebuttal 审计：逐条检查 rebuttal 是否回应了每条评审意见（fail-closed）。 | rebuttal_text: str, comments: str, paper_id: str | dict |
| `detect_style` | 机器文风检测：hedging 密度 + 模板化句式 + 空洞连接词 → 0-100 分 + 证据列表。 | text: str | dict |
| `claim_strength` | claim-strength ladder：检测表述强度（associated<predicts<causes）与无授权的强度上移。 | text: str | dict |
| `calibrate_style` | 风格校准：从已有正文学习作者声音画像（句长分布/用词偏好/结构习惯）。 | text: str | dict |
| `score_style_text` | 文风评分：新文本与作者画像的相似度（0-100，越高越接近作者声音）。 | text: str, profile: dict | dict |
| `verify_citation` | 引用核验：核验单个 DOI 是否真实存在（Crossref）。离线可用、免 key。 | doi: str | dict |
| `verify_claim` | 主张核验：检索 OpenAlex 支持证据并判定 SUPPORTED/PARTIAL/UNSUPPORTED。离线可用、免 key。 | claim: str, topic: str, limit: int | dict |
| `verify_reference_list` | 批量引用核验：逐条核验参考文献 DOI。离线可用、免 key。 | refs: list[str] | dict |
| `paper_metadata` | 论文元数据：经 Crossref 获取标题/作者/年份/期刊/摘要。离线可用、免 key。 | doi: str | dict |
| `citation_graph` | 引用图谱：经 OpenAlex 获取被引数与参考文献。离线可用、免 key。 | doi: str, depth: int | dict |
| `download_paper_pdf` | 论文 PDF 下载：经 OpenAlex OA 定位并下载开放获取 PDF。离线可用、免 key。 | doi: str, out_dir: str | dict |
| `scout_topic` | 主题侦察：多源聚合检索 + 去重 + 评分排序（被引/新近度/关键词）。离线可用、免 key。 | topic: str, limit: int | dict |
| `scout_compare` | 主题对比：多主题横向对比（按命中数降序）。离线可用、免 key。 | topics: list[str], limit: int | dict |
| `rag_answer` | 检索增强问答：检索相关文献并用本地模板合成答案（无 LLM）。离线可用、免 key。 | question: str, topic: str, limit: int | dict |
| `rag_sources` | RAG 来源：仅检索并排序相关来源（按被引降序）。离线可用、免 key。 | question: str, limit: int | dict |
| `find_code_for_paper` | 论文找代码：定位论文并检索关联代码/数据集（HuggingFace/Zenodo）。离线可用、免 key。 | title: str, limit: int | dict |
| `link_papers_to_code` | 主题找代码：主题论文批量关联代码/数据集。离线可用、免 key。 | topic: str, limit: int | dict |

### 评审与核验线

| 工具名 | 功能简述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `run_panel` | 多视角同行评审面板（7 席位：field_analyst/eic/methodology_R1/domain_R2/perspective_R3/devils_advocate/editorial_synthesizer）。 | text: str, mode: str, journal: str, design: str, adjudications: dict \| None, author_response: str, gold_set: list \| None, paper_id: str, layout | dict |
| `validate_review_intake` | 评审准入门：校验评审请求是否满足本地评审前置条件（fail-closed）。 | intake: dict | dict |
| `select_reporting_guidelines` | 按研究设计选择报告指南并做覆盖审计（非计分、带日期）。 | design: str, text: str, as_of: str | dict |
| `validate_claims_evidence` | claim/evidence 对齐矩阵：每条 claim 判定 ALIGNED / PARTIAL / UNSUPPORTED。 | claims: list, evidence: list | dict |
| `verify` | claim→source 核验：解析 doc.md 中 claims + 引文（含锚点），5 类锚点分类，输出 gate_refuse。 | text: str, sources: dict \| None | dict |
| `gate_2_5` | 完整性门 Stage 2.5：代码生成 → 执行之间的完整性门。 | context: dict | dict |
| `gate_4_5` | 完整性门 Stage 4.5：结果 → 论文/交付之间的完整性门。 | context: dict | dict |
| `run_gates` | 一次性跑两道完整性门（2.5 + 4.5）。 | context: dict | dict |
| `request_bypass` | fail-closed bypass：无理由拒绝放行；有理由记录放行。 | gate: dict, reason: str | dict |
| `build_passport` | Material Passport（per-run artifact）：含 experiment provenance + claim 审计。 | task_id: str, results: dict \| None, runs: list \| None, claims: list \| None, gate_results: dict \| None, hypothesis: str, negative_results: list \| None, doc_text: str, as_of: str | dict |

### 交付线

| 工具名 | 功能简述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `get_deliverables` | 端到端交付：列出某任务（复现/写作）的交付物清单（图/数据/源码/报告）。 | task_id: str | dict |
| `package_submission` | 投稿材料一键打包：把论文导出物与研究/复现产物打成 zip（含 cover letter）。 | paper_id: str, task_id: str | dict |

### 科学数据线

| 工具名 | 功能简述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `science_list_dbs` | 列出当前可用的科学数据库（跨 7 大领域，共 41 个），可按领域筛选。 | domain: str | dict |
| `science_search` | 在指定科学数据库中进行关键词检索。 | database: str, query: str, limit: int | dict |
| `science_fetch` | 按记录 ID 从指定科学数据库获取单条完整记录。 | database: str, id: str, format: str | dict |
| `science_cross_lookup` | 跨多个科学数据库联合查询同一关键词。 | query: str, databases: list[str] \| None, limit: int | dict |
| `science_batch_search` | 批量跨库检索：在多个数据库上并行执行同一查询并汇总结果。 | query: str, databases: list[str] \| None, limit: int | dict |

### 期刊匹配与学科

| 工具名 | 功能简述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `journal_fit` | journal-fit 评分：论文与目标期刊/会议的匹配度（领域/体裁/方法/结构/合规）。 | paper_text: str, venue: str | dict |
| `list_disciplines` | 列出当前注册的学科（自动发现，零注册即可发现）。 | domain: str | dict |
| `get_discipline` | 获取指定学科的完整配置（结构体裁/引用样式/报告标准/顶刊/单位公式）。 | name: str | dict |

### 兼容别名

| 别名 | 等价于 |
| --- | --- |
| `review_panel_intake` | `validate_review_intake` |
| `select_guidelines` | `select_reporting_guidelines` |
| `claims_evidence_matrix` | `validate_claims_evidence` |

## MCP 资源

| URI | 类型 | 内容 |
| --- | --- | --- |
| `science://databases` | 静态资源 | 全部 46 个连接器清单 + 7 个领域 |
| `science://databases/{domain}` | 参数化模板 | 单个领域下的连接器清单 |

## 返回值详细说明

### 复现线

#### `reproduce_paper`
返回 `dict`，包含：
- `ok`: bool — 是否成功
- `task_id`: str — 复现任务 ID
- `stages`: dict — 各阶段状态（parse/plan/code/run/deliver）
- `deliverables`: list — 交付物清单

#### `reproduce_status`
返回 `dict`，包含：
- `ok`: bool
- `task_id`: str
- `status`: str — 当前状态（pending/running/completed/failed）
- `stage`: str — 当前阶段
- `progress`: float — 进度 0-1

### 写作线

#### `write_section`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `section`: str
- `content`: str — 生成的章节内容
- `format`: str — 输出格式

#### `export_document`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `target`: str — 导出目标格式
- `path`: str — 输出文件路径
- `size_bytes`: int

### 研究线

#### `ideate_paper`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `topic`: str
- `research_gaps`: list — 研究缺口
- `hypotheses`: list — 候选假设
- `experiment_plan`: dict — 实验计划

#### `inject_results`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `task_id`: str
- `section`: str
- `injected`: bool

#### `research_verdict`
返回 `dict`，包含：
- `ok`: bool
- `task_id`: str
- `verdict`: str — PROCEED/REFINE/PIVOT
- `reasoning`: str

### 科研/论文线

#### `research_plan`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `topic`: str
- `plan`: dict — 完整研究计划（RQ/假设/目标/贡献/方法/数据/指标/里程碑/风险）

#### `literature_review`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `topic`: str
- `framework`: dict — 综述框架（代表文献/聚类/缺口/结构）

#### `auto_title_abstract`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `title`: str
- `abstract`: str
- `keywords`: list[str]

#### `peer_review`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `scores`: dict — novelty/rigor/clarity/soundness 评分
- `recommendation`: str
- `strengths`: list
- `weaknesses`: list
- `suggestions`: list

#### `venue_suggest`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `topic`: str
- `venues`: list — 推荐期刊/会议列表

#### `paper_polish`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `mode`: str
- `issues`: list — 发现的问题
- `suggestions`: list — 修改建议

#### `compare_metrics`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `comparison`: dict — 对比表
- `statistics`: dict — 显著性检验结果

#### `check_novelty`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `similar_papers`: list — 相似论文
- `overlaps`: list — 重叠点
- `differentiators`: list — 候选差异点

#### `citation_landscape`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `doi_or_topic`: str
- `heat`: dict — 热度分析
- `yearly_distribution`: dict — 年度分布
- `top_cited`: list — 高被引代表

#### `project_memory`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `action`: str
- `timeline`: list — 时间线

#### `review_code`
返回 `dict`，包含：
- `ok`: bool
- `task_id`: str
- `findings`: list — 发现的问题
- `score`: float — 可信度评分

#### `ref_to_bibtex`
返回 `dict`，包含：
- `ok`: bool
- `doi`: str
- `bibtex`: str — BibTeX 条目

#### `batch_ref_export`
返回 `dict`，包含：
- `ok`: bool
- `entries`: list — BibTeX 条目列表

#### `recommend_papers`
返回 `dict`，包含：
- `ok`: bool
- `topic`: str
- `papers`: list — 推荐论文列表

#### `prisma_review`
返回 `dict`，包含：
- `ok`: bool
- `topic`: str
- `counts`: dict — 流程计数
- `included`: list — 纳入文献
- `themes`: list — 主题综合
- `verification`: dict — 引文核验
- `phases`: dict — 各阶段状态

#### `convert_citation`
返回 `dict`，包含：
- `ok`: bool
- `style`: str
- `citation`: str — 渲染后的引用
- `missing`: list — 缺失字段

#### `convert_citation_all`
返回 `dict`，包含：
- `ok`: bool
- `styles`: dict — {style: rendered} 6 种样式
- `missing`: list

#### `revision_coach`
返回 `dict`，包含：
- `ok`: bool
- `total`: int
- `roadmap`: list — 结构化路线图
- `summary`: dict

#### `rebuttal_audit`
返回 `dict`，包含：
- `ok`: bool
- `total`: int
- `addressed`: int
- `unaddressed`: int
- `coverage`: float
- `pass`: bool

#### `detect_style`
返回 `dict`，包含：
- `ok`: bool
- `score`: float — 0-100 分
- `sentences`: list
- `metrics`: dict
- `evidence`: list

#### `claim_strength`
返回 `dict`，包含：
- `ok`: bool
- `max_level`: int
- `claims`: list
- `escalations`: list

#### `calibrate_style`
返回 `dict`，包含：
- `ok`: bool
- `sentences`: int
- `tokens`: int
- `structure`: dict — 作者画像

#### `score_style_text`
返回 `dict`，包含：
- `ok`: bool
- `score`: float — 0-100
- `components`: dict
- `verdict`: str

#### `verify_citation`
返回 `dict`，包含：
- `ok`: bool
- `doi`: str
- `reason`: str
- `checked_at`: str

#### `verify_claim`
返回 `dict`，包含：
- `ok`: bool
- `claim`: str
- `evidence`: list
- `verdict`: str — SUPPORTED/PARTIAL/UNSUPPORTED
- `notes`: str

#### `verify_reference_list`
返回 `dict`，包含：
- `ok`: bool
- `total`: int
- `valid`: int
- `invalid`: int
- `notes`: list

#### `paper_metadata`
返回 `dict`，包含：
- `ok`: bool
- `title`: str
- `authors`: list
- `year`: int
- `venue`: str
- `doi`: str
- `url`: str
- `abstract`: str
- `notes`: str

#### `citation_graph`
返回 `dict`，包含：
- `ok`: bool
- `root`: dict
- `citing_count`: int
- `referenced`: list
- `notes`: str

#### `download_paper_pdf`
返回 `dict`，包含：
- `ok`: bool
- `path`: str
- `source`: str
- `size_bytes`: int
- `notes`: str

#### `scout_topic`
返回 `dict`，包含：
- `ok`: bool
- `topic`: str
- `total`: int
- `ranked`: list — 评分排序结果
- `notes`: str

#### `scout_compare`
返回 `dict`，包含：
- `ok`: bool
- `topics`: list
- `comparison`: dict — 横向对比
- `notes`: str

#### `rag_answer`
返回 `dict`，包含：
- `ok`: bool
- `question`: str
- `sources`: list
- `answer`: str
- `method`: str
- `notes`: str

#### `rag_sources`
返回 `dict`，包含：
- `ok`: bool
- `question`: str
- `sources`: list
- `notes`: str

#### `find_code_for_paper`
返回 `dict`，包含：
- `ok`: bool
- `paper`: dict
- `code_links`: list
- `notes`: str

#### `link_papers_to_code`
返回 `dict`，包含：
- `ok`: bool
- `topic`: str
- `links`: list
- `notes`: str

### 评审与核验线

#### `run_panel`
返回 `dict`，包含：
- `ok`: bool
- `verdict`: str
- `phases`: dict — {phase1, phase2}
- `decision`: str
- `panel`: list — 7 席位评审意见

#### `validate_review_intake`
返回 `dict`，包含：
- `ok`: bool
- `status`: str — READY_FOR_LOCAL_REVIEW/BLOCKED
- `paper_id`: str
- `mode`: str
- `blockers`: list
- `warnings`: list

#### `select_reporting_guidelines`
返回 `dict`，包含：
- `ok`: bool
- `selected`: str — 选中的报告指南
- `probe_source`: str
- `coverage`: dict — 覆盖审计
- `coverage_summary`: str
- `text_provided`: bool
- `note`: str
- `audit_date`: str

#### `validate_claims_evidence`
返回 `dict`，包含：
- `ok`: bool
- `n_claims`: int
- `n_evidence`: int
- `matrix`: list — 对齐矩阵
- `summary`: dict

#### `verify`
返回 `dict`，包含：
- `ok`: bool
- `gate_refuse`: bool
- `findings`: list
- `summary`: dict
- `offline`: bool

#### `gate_2_5`
返回 `dict`，包含：
- `stage`: str
- `passed`: bool
- `blocked_patterns`: list
- `checks`: list
- `bypassed`: bool

#### `gate_4_5`
返回 `dict`，包含：
- `stage`: str
- `passed`: bool
- `blocked_patterns`: list
- `checks`: list
- `bypassed`: bool

#### `run_gates`
返回 `dict`，包含：
- `"2.5"`: dict — gate_2_5 结果
- `"4.5"`: dict — gate_4_5 结果

#### `request_bypass`
返回 `dict`，包含：
- `allowed`: bool
- `stage`: str
- `bypassed`: bool
- `bypass_reason`: str
- `error`: str

#### `build_passport`
返回 `dict`，包含 Material Passport artifact：
- `task_id`: str
- `experiment_provenance`: dict
- `claim_audit`: dict
- `negative_results`: list

### 交付线

#### `get_deliverables`
返回 `dict`，包含：
- `ok`: bool
- `task_id`: str
- `deliverables`: list — 交付物清单（图/数据/源码/报告）

#### `package_submission`
返回 `dict`，包含：
- `ok`: bool
- `paper_id`: str
- `task_id`: str
- `zip_path`: str
- `contents`: list

### 科学数据线

#### `science_list_dbs`
返回 `dict`，包含：
- `ok`: bool
- `databases`: list — 数据库列表
- `domains`: list — 领域列表

#### `science_search`
返回 `dict`，包含：
- `ok`: bool
- `database`: str
- `query`: str
- `results`: list — 检索结果
- `total`: int

#### `science_fetch`
返回 `dict`，包含：
- `ok`: bool
- `database`: str
- `id`: str
- `record`: dict — 完整记录

#### `science_cross_lookup`
返回 `dict`，包含：
- `ok`: bool
- `query`: str
- `results`: dict — {database: results}
- `total`: int

#### `science_batch_search`
返回 `dict`，包含：
- `ok`: bool
- `query`: str
- `results`: dict — {database: results}
- `total`: int

### 期刊匹配与学科

#### `journal_fit`
返回 `dict`，包含：
- `ok`: bool
- `venue`: str
- `score`: float
- `breakdown`: dict — 各维度评分
- `gaps`: list
- `recommendations`: list

#### `list_disciplines`
返回 `dict`，包含：
- `ok`: bool
- `disciplines`: list — 学科名列表

#### `get_discipline`
返回 `dict`，包含：
- `ok`: bool
- `discipline`: dict — 学科完整配置（name/aliases/paper_types/citation_style/reporting_standards/conventions/key_venues/units_and_formulas_notes/paper_capable/contribution_forms/tools/category/databases）
