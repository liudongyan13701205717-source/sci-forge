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
    from sciforge.science.api import science_list_dbs as _impl
    return _impl(domain=domain)


@mcp.tool()
def science_search(database: str, query: str, limit: int = 5) -> dict:
    from sciforge.science.api import science_search as _impl
    return _impl(database=database, query=query, limit=limit)


@mcp.tool()
def science_fetch(database: str, id: str, format: str = "") -> dict:
    from sciforge.science.api import science_fetch as _impl
    return _impl(database=database, id=id, format=format)


@mcp.tool()
def science_cross_lookup(query: str, databases: list[str] | None = None,
                        limit: int = 5) -> dict:
    from sciforge.science.api import science_cross_lookup as _impl
    return _impl(query=query, databases=databases, limit=limit)


def run() -> None:
    mcp.run()


if __name__ == "__main__":
    run()
