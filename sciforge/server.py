"""MCP stdio server 入口：注册三条功能线的工具集。

阶段 0：仅注册工具签名（空实现 stub），打通 opencode MCP 通道；
后续阶段在各自模块内填充真实实现。
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from sciforge import __version__

mcp = FastMCP(
    "sci-forge",
    instructions=(
        "SciForge：论文复现五步闭环、论文写作助力、端到端交付。"
        "所有工具均本地自建，不依赖任何官方站点。"
    ),
)


@mcp.tool()
def reproduce_paper(
    pdf_path: str,
    framework: str = "pytorch",
) -> dict:
    """论文复现五步闭环：解析 PDF → 复现方案 → 生成代码 → 沙箱运行比对 → 产出交付物。

    Args:
        pdf_path: 论文 PDF 的本地绝对路径。
        framework: 生成代码框架，`pytorch` 或 `tensorflow`，默认 pytorch。
    """
    from sciforge.reproduce.api import reproduce_paper as _impl

    return _impl(pdf_path=pdf_path, framework=framework)


@mcp.tool()
def reproduce_status(task_id: str) -> dict:
    """查询论文复现任务的异步状态与阶段进度。"""
    from sciforge.reproduce.api import reproduce_status as _impl

    return _impl(task_id=task_id)


@mcp.tool()
def write_section(
    paper_id: str,
    section: str,
    prompt: str,
    format: str = "latex",
) -> dict:
    """论文写作助力：按章节引导生成内容（摘要/问题/假设/符号/建模/求解/结果/参考文献/附录）。

    Args:
        paper_id: 论文/项目标识。
        section: 章节名，如 abstract/introduction/problem/assumptions/notation/
            modeling/solution/results/references/appendix。
        prompt: 该章节的写作引导/要点。
        format: 输出格式，`latex` 或 `markdown`。
    """
    from sciforge.write.api import write_section as _impl

    return _impl(paper_id=paper_id, section=section, prompt=prompt, format=format)


@mcp.tool()
def export_document(
    paper_id: str,
    target: str = "pdf",
) -> dict:
    """论文写作助力：将已写 doc（markdown）导出为 LaTeX / PDF / docx。

    Args:
        paper_id: 论文/项目标识。
        target: 导出目标，`pdf` 或 `docx`（LaTeX 源始终生成）。
    """
    from sciforge.export.api import export_document as _impl

    return _impl(paper_id=paper_id, target=target)


@mcp.tool()
def get_deliverables(task_id: str = "") -> dict:
    """端到端交付：列出某任务（复现/写作）的交付物清单（图/数据/源码/报告）。

    Args:
        task_id: 复现任务 ID（或写作项目 ID，二者其一）。
    """
    from sciforge.deliver.api import get_deliverables as _impl

    return _impl(task_id=task_id)


@mcp.tool()
def ideate_paper(
    topic: str,
    paper_id: str,
) -> dict:
    """研究起点：由研究方向构思选题，产出研究缺口、候选假设、多视角评审与实验计划。

    Args:
        topic: 研究方向/主题/关键词。
        paper_id: 论文/项目标识（产物存 projects/{paper_id}/research/）。
    """
    from sciforge.core import get_layout
    from sciforge.research.api import ideate_paper as _impl

    return _impl(topic=topic, paper_id=paper_id, layout=get_layout())


@mcp.tool()
def inject_results(
    paper_id: str,
    task_id: str,
    section: str = "results",
) -> dict:
    """将复现任务的真实实验结果并入论文对应章节（实验数据→论文）。

    Args:
        paper_id: 论文/项目标识。
        task_id: 已完成复现闭环的任务 ID。
        section: 注入目标章节，`results` 或 `experiments`。
    """
    from sciforge.core import get_layout
    from sciforge.research.api import inject_results as _impl

    return _impl(paper_id=paper_id, task_id=task_id, layout=get_layout(), section=section)


@mcp.tool()
def research_verdict(task_id: str) -> dict:
    """结果分析自旋门：根据复现产物给出 PROCEED/REFINE/PIVOT 决策建议。

    Args:
        task_id: 已完成复现闭环的任务 ID。
    """
    from sciforge.core import get_layout
    from sciforge.research.api import decision_readout as _impl

    return _impl(task_id=task_id, layout=get_layout())


@mcp.tool()
def research_plan(
    topic: str,
    paper_id: str,
) -> dict:
    """研究计划书：由选题展开成完整研究计划（RQ/假设/目标/贡献/方法/数据/
    基线/指标/消融/里程碑/风险），可复用已有 ideation/experiment plan。

    Args:
        topic: 研究方向/主题/关键词。
        paper_id: 论文/项目标识（产物存 projects/{paper_id}/research/research_plan.*）。
    """
    from sciforge.core import get_layout
    from sciforge.research.plan import research_plan as _impl

    return _impl(topic=topic, paper_id=paper_id, layout=get_layout()).to_dict()


@mcp.tool()
def literature_review(
    topic: str,
    paper_id: str,
) -> dict:
    """文献综述：基于免 key OpenAlex 检索生成综述框架（代表文献/主题聚类/
    研究缺口/综述结构），可直接作为 related work 素材。

    Args:
        topic: 综述主题/关键词。
        paper_id: 论文/项目标识（产物存 projects/{paper_id}/research/literature_review.*）。
    """
    from sciforge.core import get_layout
    from sciforge.research.survey import literature_review as _impl

    return _impl(topic=topic, paper_id=paper_id, layout=get_layout()).to_dict()


@mcp.tool()
def auto_title_abstract(paper_id: str) -> dict:
    """标题/摘要/关键词提炼：从已写正文自动生成投稿所需元数据。

    Args:
        paper_id: 论文/项目标识（产物存 projects/{paper_id}/research/metadata.*）。
    """
    from sciforge.core import get_layout
    from sciforge.research.extract import auto_title_abstract as _impl

    return _impl(paper_id=paper_id, layout=get_layout()).to_dict()


@mcp.tool()
def peer_review(paper_id: str) -> dict:
    """模拟同行评审：对已有论文生成结构化审稿意见（novelty/rigor/clarity/
    soundness 评分 + 推荐 + 优点/缺点/修改建议）。

    Args:
        paper_id: 论文/项目标识（产物存 projects/{paper_id}/research/peer_review.*）。
    """
    from sciforge.core import get_layout
    from sciforge.research.review import peer_review as _impl

    return _impl(paper_id=paper_id, layout=get_layout()).to_dict()


@mcp.tool()
def venue_suggest(
    topic: str,
    paper_id: str,
) -> dict:
    """投稿建议：根据主题/关键词推荐目标期刊与会议（内置映射库 + 可选 LLM）。

    Args:
        topic: 研究方向/主题/关键词。
        paper_id: 论文/项目标识（产物存 projects/{paper_id}/research/venue_suggest.*）。
    """
    from sciforge.core import get_layout
    from sciforge.research.venue import venue_suggest as _impl

    return _impl(topic=topic, paper_id=paper_id, layout=get_layout()).to_dict()


@mcp.tool()
def paper_polish(
    paper_id: str,
    mode: str = "completeness",
) -> dict:
    """论文润色与检查：对已有正文做质量检查并产出建议。

    Args:
        paper_id: 论文/项目标识。
        mode: 检查模式，`completeness`(完整性) / `consistency`(一致性) /
            `grammar`(语言润色)，默认 completeness。
    """
    from sciforge.core import get_layout
    from sciforge.research.polish import paper_polish as _impl

    return _impl(paper_id=paper_id, layout=get_layout(), mode=mode).to_dict()


@mcp.tool()
def compare_metrics(
    paper_id: str,
    tasks: list[str],
    baseline: str = "",
    metric: str = "",
) -> dict:
    """对比表与显著性检验：汇总多个任务/基线的指标序列并做检验。

    Args:
        paper_id: 论文/项目标识。
        tasks: 一个或多个复现任务 ID（读取各自 results.json 的指标序列）。
        baseline: 作为对照组的任务 ID，默认取 tasks[0]。
        metric: 可选，仅统计名称含该子串的指标；留空则全部。
    """
    from sciforge.core import get_layout
    from sciforge.research.bench import compare_metrics as _impl

    return _impl(paper_id=paper_id, task_ids=list(tasks),
                 layout=get_layout(), baseline=baseline, metric=metric).to_dict()


@mcp.tool()
def check_novelty(paper_id: str, max_papers: int = 8) -> dict:
    """创新性检查：从标题/摘要抽关键词检索相似工作，给出重叠与候选差异点。

    Args:
        paper_id: 论文/项目标识（需已有 doc.md 或 metadata.json）。
        max_papers: 检索的相似论文数量上限，默认 8。
    """
    from sciforge.core import get_layout
    from sciforge.research.novelty import check_novelty as _impl

    return _impl(paper_id=paper_id, layout=get_layout(), limit=max_papers).to_dict()


@mcp.tool()
def package_submission(
    paper_id: str,
    task_id: str = "",
) -> dict:
    """投稿材料一键打包：把论文导出物与研究/复现产物打成 zip（含 cover letter）。

    Args:
        paper_id: 论文/项目标识。
        task_id: 可选，一并打包该复现任务的代码/数据/图表。
    """
    from sciforge.core import get_layout
    from sciforge.deliver.package import package_submission as _impl

    return _impl(paper_id=paper_id, layout=get_layout(), task_id=task_id)


@mcp.tool()
def citation_landscape(paper_id: str, doi_or_topic: str) -> dict:
    """引文邻域与热度分析：围绕 DOI 或主题分析热度/年度分布/高被引代表。

    Args:
        paper_id: 论文/项目标识。
        doi_or_topic: 目标 DOI（含 10.xxxx）或主题关键词。
    """
    from sciforge.core import get_layout
    from sciforge.research.community import citation_landscape as _impl

    return _impl(paper_id=paper_id, layout=get_layout(),
                 doi_or_topic=doi_or_topic).to_dict()


@mcp.tool()
def project_memory(
    paper_id: str,
    action: str = "read",
    note: str = "",
    milestone: str = "",
    status: str = "",
) -> dict:
    """项目进度记账：为论文/项目维护可回溯 timeline（备忘/里程碑/状态）。

    Args:
        paper_id: 论文/项目标识。
        action: `read`(读取) / `note`(备忘) / `milestone`(里程碑) / `status`(状态)。
        note: 备忘/说明文本。
        milestone: 里程碑标识（如 1.0.0、方案评审）。
        status: 状态描述（如 构思/实验/写作/已投稿/返修）。
    """
    from sciforge.core import get_layout
    from sciforge.core.memory import project_memory as _impl

    return _impl(paper_id=paper_id, layout=get_layout(), action=action,
                 note=note, milestone=milestone, status=status).to_dict()


@mcp.tool()
def review_code(task_id: str) -> dict:
    """复现代化码静态点评：对任务下的 .py 做风格/风险/可复现性检查。

    Args:
        task_id: 已生成代码的复现任务 ID。
    """
    from sciforge.core import get_layout
    from sciforge.reproduce.codereview import review_code as _impl

    return _impl(task_id=task_id, layout=get_layout()).to_dict()


@mcp.tool()
def science_list_dbs(domain: str = "") -> dict:
    """列出当前可用的科学数据库（跨 7 大领域，共 41 个），可按领域筛选。

    Args:
        domain: 可选领域筛选，如 literature/proteins/chemistry/genomics/
            pathways/omics/datasets；留空则列出全部。
    """
    from sciforge.science.api import science_list_dbs as _impl
    return _impl(domain=domain)


@mcp.tool()
def science_search(database: str, query: str, limit: int = 5) -> dict:
    """在指定科学数据库中进行关键词检索。

    Args:
        database: 数据库标识（如 openalex/uniprot/chembl），先用
            science_list_dbs 查看全部。
        query: 检索关键词。
        limit: 返回条数上限，默认 5。
    """
    from sciforge.science.api import science_search as _impl
    return _impl(database=database, query=query, limit=limit)


@mcp.tool()
def science_fetch(database: str, id: str, format: str = "") -> dict:
    """按记录 ID 从指定科学数据库获取单条完整记录。

    Args:
        database: 数据库标识。
        id: 记录 ID（如 P53_HUMAN / 1ABC / W123456789）。
        format: 期望返回格式，留空用默认。
    """
    from sciforge.science.api import science_fetch as _impl
    return _impl(database=database, id=id, format=format)


@mcp.tool()
def science_cross_lookup(query: str, databases: list[str] | None = None,
                         limit: int = 5) -> dict:
    """跨多个科学数据库联合查询同一关键词。

    Args:
        query: 检索关键词。
        databases: 可选，限定查询的数据库列表；留空则全库搜索。
        limit: 每个库返回条数上限，默认 5。
    """
    from sciforge.science.api import science_cross_lookup as _impl
    return _impl(query=query, databases=databases, limit=limit)


@mcp.tool()
def science_batch_search(query: str, databases: list[str] | None = None,
                         limit: int = 10) -> dict:
    """批量跨库检索：在多个数据库上并行执行同一查询并汇总结果。

    Args:
        query: 检索关键词。
        databases: 可选，要检索的数据库列表；留空则覆盖主要库。
        limit: 每个库返回条数上限，默认 10。
    """
    from sciforge.science.api import science_batch_search as _impl
    return _impl(query=query, databases=databases, limit=limit)


@mcp.resource("science://databases")
def science_databases_resource() -> dict:
    from sciforge.science import DOMAINS
    from sciforge.science.api import science_list_dbs
    return {"databases": science_list_dbs()["databases"], "domains": DOMAINS}


@mcp.resource("science://databases/{domain}")
def science_domain_resource(domain: str) -> dict:
    from sciforge.science.api import science_list_dbs
    return science_list_dbs(domain=domain)


@mcp.tool()
def ref_to_bibtex(doi: str) -> dict:
    """按 DOI 生成 BibTeX 条目。

    Args:
        doi: DOI 标识（含 10.xxxx 前缀）。
    """
    from sciforge.research.references import ref_to_bibtex as _impl
    return _impl(doi=doi)


@mcp.tool()
def batch_ref_export(text: str) -> dict:
    """批量导出参考文献：解析文本中的 DOI/引用，转成 BibTeX 条目。

    Args:
        text: 一段任意文本，内含一个或多个 DOI 或引用信息。
    """
    from sciforge.research.references import batch_ref_export as _impl
    return _impl(text=text)


@mcp.tool()
def recommend_papers(topic: str, limit: int = 5, sources: list[str] | None = None) -> dict:
    """围绕研究主题推荐论文。

    Args:
        topic: 研究方向/主题/关键词。
        limit: 返回条数上限，默认 5。
        sources: 可选来源过滤，留空用默认源。
    """
    from sciforge.research.recommender import recommend_papers as _impl
    return _impl(topic=topic, limit=limit, sources=sources)


@mcp.tool()
def run_panel(
    text: str,
    mode: str = "full",
    journal: str = "",
    design: str = "",
    adjudications: dict | None = None,
    author_response: str = "",
    gold_set: list | None = None,
    paper_id: str = "",
    layout=None,
) -> dict:
    """多视角同行评审面板（7 席位：field_analyst/eic/methodology_R1/domain_R2/perspective_R3/devils_advocate/editorial_synthesizer）。

    Args:
        text: 论文全文（必填）。
        mode: 运行模式，`full`/`quick`/`re-review`/`methodology_focus`/`calibration`，默认 full。
        journal: 目标期刊名（用于 eic journal-fit），可选。
        design: 研究设计描述（如 "randomized controlled trial"），用于 validators 指南选择，可选。
        adjudications: CRITICAL 裁决字典 {issue_id: adjudication}，adjudication ∈ {addressed, countered, unaddressed, wontfix}。
        author_response: 作者回应文本（re-review 模式用）。
        gold_set: calibration 模式用的金标准集合 [{text, verdict}, ...]。
        paper_id / layout: 给定时落盘 projects/{paper_id}/research/review_*.

    Returns:
        dict：{ok, verdict, phases: {phase1, phase2}, decision, ...}。
    """
    from sciforge.review.panel import run_panel as _impl
    from sciforge.core import get_layout

    return _impl(
        text=text,
        mode=mode,
        journal=journal,
        design=design,
        adjudications=adjudications,
        author_response=author_response,
        gold_set=gold_set,
        paper_id=paper_id,
        layout=layout or get_layout(),
    )


@mcp.tool()
def validate_review_intake(intake: dict) -> dict:
    """评审准入门：校验评审请求是否满足本地评审前置条件（fail-closed）。

    Args:
        intake: 评审请求字典，含 paper_id, mode, authorization, conflict_of_interest, external_services。

    Returns:
        dict：{ok, status (READY_FOR_LOCAL_REVIEW/BLOCKED), paper_id, mode, blockers, warnings}。
    """
    from sciforge.review.validators import validate_review_intake as _impl

    return _impl(intake)


@mcp.tool()
def select_reporting_guidelines(design: str, text: str = "", as_of: str = "") -> dict:
    """按研究设计选择报告指南并做覆盖审计（非计分、带日期）。

    Args:
        design: 研究设计描述（如 "randomized controlled trial"），空则从 text 前 2000 字探测。
        text: 论文正文（用于覆盖审计）。
        as_of: 审计日期（ISO 格式），缺省取今天。

    Returns:
        dict：{ok, selected, probe_source, coverage, coverage_summary, text_provided, note, audit_date}。
    """
    from sciforge.review.validators import select_reporting_guidelines as _impl

    return _impl(design=design, text=text, as_of=as_of)


@mcp.tool()
def validate_claims_evidence(claims: list, evidence: list) -> dict:
    """claim/evidence 对齐矩阵：每条 claim 判定 ALIGNED / PARTIAL / UNSUPPORTED。

    Args:
        claims: [{"id", "text", "requires_evidence?"}] 或纯字符串列表。
        evidence: [{"id", "text"}] 或纯字符串列表。

    Returns:
        dict：{ok, n_claims, n_evidence, matrix, summary}。
    """
    from sciforge.review.validators import validate_claims_evidence as _impl

    return _impl(claims=claims, evidence=evidence)


@mcp.tool()
def review_panel_intake(intake: dict) -> dict:
    """评审准入门（兼容旧名，等同 validate_review_intake）。

    Args:
        intake: 同 validate_review_intake。

    Returns:
        dict：同 validate_review_intake。
    """
    from sciforge.review.validators import validate_review_intake as _impl

    return _impl(intake)


@mcp.tool()
def select_guidelines(design: str, text: str = "", as_of: str = "") -> dict:
    """报告指南选择（兼容旧名，等同 select_reporting_guidelines）。

    Args:
        design: 研究设计描述。
        text: 论文正文。
        as_of: 审计日期。

    Returns:
        dict：同 select_reporting_guidelines。
    """
    from sciforge.review.validators import select_reporting_guidelines as _impl

    return _impl(design=design, text=text, as_of=as_of)


@mcp.tool()
def claims_evidence_matrix(claims: list, evidence: list) -> dict:
    """claim/evidence 对齐矩阵（兼容旧名，等同 validate_claims_evidence）。

    Args:
        claims: claim 列表。
        evidence: evidence 列表。

    Returns:
        dict：同 validate_claims_evidence。
    """
    from sciforge.review.validators import validate_claims_evidence as _impl

    return _impl(claims=claims, evidence=evidence)


@mcp.tool()
def verify(text: str, sources: dict | None = None) -> dict:
    """claim→source 核验：解析 doc.md 中 claims + 引文（含锚点），5 类锚点分类，输出 gate_refuse。

    Args:
        text: 待核验文本（doc.md 全文）。
        sources: 可选，外部来源索引 {anchor_key: source_text}。

    Returns:
        dict：{ok, gate_refuse, findings, summary, offline}。
    """
    from sciforge.claims.verify import verify as _impl

    return _impl(text=text, sources=sources)


@mcp.tool()
def gate_2_5(context: dict) -> dict:
    """完整性门 Stage 2.5：代码生成 → 执行之间的完整性门。

    Args:
        context: {code, plan}。

    Returns:
        dict：{stage, passed, blocked_patterns, checks, bypassed}。
    """
    from sciforge.claims.gates import gate_2_5 as _impl

    return _impl(context)


@mcp.tool()
def gate_4_5(context: dict) -> dict:
    """完整性门 Stage 4.5：结果 → 论文/交付之间的完整性门。

    Args:
        context: {results, runs, claims, doc_text, negative_results}。

    Returns:
        dict：{stage, passed, blocked_patterns, checks, bypassed}。
    """
    from sciforge.claims.gates import gate_4_5 as _impl

    return _impl(context)


@mcp.tool()
def run_gates(context: dict) -> dict:
    """一次性跑两道完整性门（2.5 + 4.5）。

    Args:
        context: 同时包含 gate_2_5 和 gate_4_5 所需字段。

    Returns:
        dict：{"2.5": ..., "4.5": ...}。
    """
    from sciforge.claims.gates import run_gates as _impl

    return _impl(context)


@mcp.tool()
def request_bypass(gate: dict, reason: str) -> dict:
    """fail-closed bypass：无理由拒绝放行；有理由记录放行。

    Args:
        gate: gate_2_5/gate_4_5/run_gates 返回的 gate 字典。
        reason: 放行理由（必填，fail-closed）。

    Returns:
        dict：{allowed, stage, bypassed, bypass_reason, error}。
    """
    from sciforge.claims.gates import request_bypass as _impl

    return _impl(gate=gate, reason=reason)


@mcp.tool()
def build_passport(
    task_id: str,
    results: dict | None = None,
    runs: list | None = None,
    claims: list | None = None,
    gate_results: dict | None = None,
    hypothesis: str = "",
    negative_results: list | None = None,
    doc_text: str = "",
    as_of: str = "",
) -> dict:
    """Material Passport（per-run artifact）：含 experiment provenance + claim 审计。

    Args:
        task_id: 任务标识。
        results: 实验结果 dict。
        runs: 运行记录列表。
        claims: claim 列表。
        gate_results: run_gates 返回的双门结果。
        hypothesis: 初始假设。
        negative_results: 反面证据列表。
        doc_text: 论文全文（用于 claim 审计）。
        as_of: 生成日期（ISO），缺省今天。

    Returns:
        dict：Material Passport artifact。
    """
    from sciforge.claims.gates import build_passport as _impl

    return _impl(
        task_id=task_id,
        results=results,
        runs=runs,
        claims=claims,
        gate_results=gate_results,
        hypothesis=hypothesis,
        negative_results=negative_results,
        doc_text=doc_text,
        as_of=as_of,
    )


@mcp.tool()
def journal_fit(paper_text: str, venue: str) -> dict:
    """journal-fit 评分：论文与目标期刊/会议的匹配度（领域/体裁/方法/结构/合规）。

    Args:
        paper_text: 论文全文。
        venue: 目标期刊/会议名（如 Nature, Cell, NeurIPS）。

    Returns:
        dict：{ok, venue, score, breakdown, gaps, recommendations}。
    """
    from sciforge.venue.fit import journal_fit as _impl

    return _impl(paper_text=paper_text, venue=venue)


@mcp.tool()
def list_disciplines(domain: str = "") -> dict:
    """列出当前注册的学科（自动发现，零注册即可发现）。

    Args:
        domain: 可选领域筛选，预留参数（当前忽略，供未来按领域分组）。

    Returns:
        dict：{ok, disciplines: [学科名列表]}。
    """
    from sciforge.disciplines import list_disciplines as _impl

    return {"ok": True, "disciplines": _impl()}


@mcp.tool()
def get_discipline(name: str) -> dict:
    """获取指定学科的完整配置（结构体裁/引用样式/报告标准/顶刊/单位公式）。

    Args:
        name: 学科名（如 mathematics, physics, medicine）。

    Returns:
        dict：学科配置对象。
    """
    from sciforge.disciplines import get_discipline as _impl

    d = _impl(name)
    if d is None:
        return {"ok": False, "error": f"未知学科: {name}"}
    return {"ok": True, "discipline": d.__dict__}


@mcp.tool()
def prisma_review(topic: str, hits: list[dict] | None = None,
                  databases: list[str] | None = None, limit: int = 10,
                  include_keywords: list[str] | None = None,
                  exclude_keywords: list[str] | None = None,
                  paper_id: str = "", persist: bool = False) -> dict:
    """PRISMA 系统综述：7 阶段协议（规划→多库检索→筛选→全文评估→主题综合→引文核验→文档生成），带流程计数。

    Args:
        topic: 综述主题（检索查询语句）。
        hits: 预取检索结果（可选，给定则跳过检索阶段）。
        databases: 检索库列表（不足 3 个自动补默认库）。
        limit: 每库检索条数上限，默认 10。
        include_keywords: title/abstract 纳入关键词（未命中即排除）。
        exclude_keywords: title/abstract 排除关键词（命中即排除）。
        paper_id: 项目标识（persist=True 时落盘）。
        persist: 是否落盘 prisma.json/md，默认 False。

    Returns:
        dict：{ok, topic, counts, included, themes, verification, queries, phases, notes, offline}。
    """
    from sciforge.core import get_layout
    from sciforge.research.prisma import flow as _impl

    layout = get_layout() if (persist and paper_id) else None
    return _impl(topic=topic, hits=hits, databases=databases, limit=limit,
                 include_keywords=include_keywords, exclude_keywords=exclude_keywords,
                 paper_id=paper_id, layout=layout, persist=persist)


@mcp.tool()
def convert_citation(bibtex: str, style: str = "apa") -> dict:
    """引用样式转换：解析 BibTeX 条目并渲染为指定样式。

    Args:
        bibtex: BibTeX 条目文本（@article{...} 等）。
        style: 目标样式，可选 apa / chicago-notes / chicago-author-date /
            mla / ieee / vancouver，默认 apa。

    Returns:
        dict：{ok, style, citation, missing}。missing 为缺字段清单（优雅降级标注 (missing)）。
    """
    from sciforge.research.styles import parse_bibtex, render

    cit = parse_bibtex(bibtex or "")
    return render(cit, style)


@mcp.tool()
def convert_citation_all(bibtex: str) -> dict:
    """引用样式一键转换：BibTeX → 全部 6 种样式（APA/Chicago×2/MLA/IEEE/Vancouver）。

    Args:
        bibtex: BibTeX 条目文本。

    Returns:
        dict：{ok, styles: {style: rendered}, missing}。
    """
    from sciforge.research.styles import parse_bibtex, render_all

    return render_all(parse_bibtex(bibtex or ""))


@mcp.tool()
def revision_coach(comments_text: str, paper_id: str = "") -> dict:
    """修订教练：评审意见 → 结构化路线图（comment→类型 CRITICAL/MAJOR/MINOR→位置→回应计划）。

    Args:
        comments_text: 评审意见原文（多条意见用编号/空行分隔）。
        paper_id: 可选，给定时落盘 rebuttal_plan.json。

    Returns:
        dict：{ok, total, roadmap, summary}。
    """
    from sciforge.core import get_layout
    from sciforge.research.rebuttal import revision_coach as _impl

    layout = get_layout() if paper_id else None
    return _impl(comments_text, paper_id=paper_id, layout=layout)


@mcp.tool()
def rebuttal_audit(rebuttal_text: str, comments: str, paper_id: str = "") -> dict:
    """rebuttal 审计：逐条检查 rebuttal 是否回应了每条评审意见（fail-closed）。

    Args:
        rebuttal_text: rebuttal 草稿全文。
        comments: 评审意见原文。
        paper_id: 可选，给定时落盘 rebuttal_audit.json。

    Returns:
        dict：{ok, total, addressed, unaddressed, coverage, pass}。
    """
    from sciforge.core import get_layout
    from sciforge.research.rebuttal import rebuttal_audit as _impl

    layout = get_layout() if paper_id else None
    return _impl(rebuttal_text, comments, paper_id=paper_id, layout=layout)


@mcp.tool()
def detect_style(text: str) -> dict:
    """机器文风检测：hedging 密度 + 模板化句式 + 空洞连接词 → 0-100 分 + 证据列表。

    Args:
        text: 待检文本（论文正文或章节）。

    Returns:
        dict：{ok, score, sentences, metrics, evidence}。分数越高越像机器生成。
    """
    from sciforge.research.quality import detect_style as _impl

    return _impl(text)


@mcp.tool()
def claim_strength(text: str) -> dict:
    """claim-strength ladder：检测表述强度（associated<predicts<causes）与无授权的强度上移。

    Args:
        text: 待检文本。

    Returns:
        dict：{ok, max_level, claims, escalations}。
    """
    from sciforge.research.quality import claim_strength as _impl

    return _impl(text)


@mcp.tool()
def calibrate_style(text: str) -> dict:
    """风格校准：从已有正文学习作者声音画像（句长分布/用词偏好/结构习惯）。

    Args:
        text: 已有正文（如 doc.md 全文）。

    Returns:
        dict：{ok, sentences, tokens, structure}。画像可用于 score_style_text 评分。
    """
    from sciforge.research.stylecal import learn_style as _impl

    return _impl(text)


@mcp.tool()
def score_style_text(text: str, profile: dict) -> dict:
    """文风评分：新文本与作者画像的相似度（0-100，越高越接近作者声音）。

    Args:
        text: 待评文本。
        profile: calibrate_style 产出的画像 dict。

    Returns:
        dict：{ok, score, components, verdict}。
    """
    from sciforge.research.stylecal import score_text as _impl

    return _impl(text, profile)


def run() -> None:
    mcp.run()


if __name__ == "__main__":
    run()
