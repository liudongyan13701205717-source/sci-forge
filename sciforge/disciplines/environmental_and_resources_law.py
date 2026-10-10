"""环境与资源法学科论文支持：环境法、资源法与可持续发展法研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_and_resources_law",
    aliases=(
        "environmental_and_resources_law", "环境与资源法",
        "environmental and resources law", "环境与资源法",
        "environmental law", "环境法",
        "natural resources law", "自然资源法",
        "sustainable development law", "可持续发展法",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（法律问题与背景）",
            "methodology（法律分析、案例研究、比较法）",
            "results（法律效果与评估）",
            "discussion（法律优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "legal analysis（法律分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "legal": "法律分析须注明法规版本与时间",
        "case": "案例分析须注明法院与时间",
        "comparison": "比较法研究须注明国家与时间",
    },
    conventions=(
        "法律名称须使用官方名称",
        "法规版本须注明",
        "案例须注明法院与时间",
        "比较法研究须注明国家与时间",
    ),
    key_venues=(
        "Environmental Law",
        "Journal of Environmental Law",
        "Review of European, Comparative & International Environmental Law",
        "Land Use Policy",
        "Journal of Land Use & Environmental Law",
        "Environmental Law Review",
    ),
    units_and_formulas_notes=(
        "法律名称须使用官方名称",
        "法规版本须注明",
        "案例须注明法院与时间",
        "比较法研究须注明国家与时间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Legal Citation Software", "Case Analysis Software", "Juris", "ROSS Intelligence", "Vellum", "iManage", "Relativity", "Everlaw", "DocuSign", "Adobe Acrobat Pro", "Turnitin", "EndNote", "Zotero", "Mendeley", "NVivo", "MAXQDA", "Excel", "SPSS", "GIS (ArcGIS, QGIS)", "VOSviewer"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
