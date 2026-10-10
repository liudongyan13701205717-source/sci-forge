"""开放科学学科论文支持：开放获取、数据共享与科研透明度。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="open_science",
    aliases=("open_science", "开放科学", "Open Research", "Open Access", "开放获取", "开放数据", "Open Data", "Research Transparency"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "开放数据共享规范", "k2": "FAIR原则（可发现、可访问、可互操作、可重用）", "k3": "开放获取出版政策"},
    conventions=("数据DOI标注", "代码仓库链接", "CC BY许可声明", "预注册信息引用"),
    key_venues=("Journal of Open Research", "PLoS One", "Scientific Data", "开放科学评论", "F1000Research"),
    units_and_formulas_notes=("开放获取率以%", "引用计量用H指数", "数据引用次数", "出版延迟天数"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R (OpenCRAN)", "Python", "Zenodo", "Figshare", "GitHub", "OSF (Open Science Framework)", "DataCite", "Semantic Scholar", "CiteULike", "Mendeley", "Zotero", "EndNote", "JOS (Journal of Open Science)", "OpenRefine", "Citable Data (DSpace)", "PeerJ", "BioRxiv", "Dataverse", "OpenAIRE", "PRISMA（系统综述流程工具）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scholar (Google Scholar)", "OpenAlex API", "Crossref API"),
)
