"""历史学学科论文支持：历史研究与档案体裁、Chicago 17 引用样式与历史记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="historical_studies",
    aliases=("historical_studies", "历史学", "历史研究", "历史档案", "历史档案研究", "历史档案学", "历史档案研究", "历史档案学研究", "历史研究"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 17（作者-标题-年份）",
    reporting_standards={
        "historical": "历史研究规范",
        "archival": "档案研究规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "历史事件须给出年代",
        "引用须注明来源",
        "描述须给出上下文",
        "档案须给出来源",
        "描述须客观",
    ),
    key_venues=(
        "American Historical Review",
        "Past & Present",
        "Annales",
        "Journal of Modern History",
        "Journal of World History",
    ),
    units_and_formulas_notes=(
        "时间用公元/年前后",
        "公式用 amsmath",
        "行内公式避免复杂分式",
        "数值结果给出均值±SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Tropy", "Transkribus", "eScriptorium", "Omeka S", "Nodegoat", "Recogito", "Gephi", "Palladio", "Cytoscape", "Voyant Tools", "AntConc", "R", "Python", "QGIS", "Juxta", "CollateX", "FairCopy", "OxGarage", "Zotero", "LaTeX"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "ProQuest", "EBSCO", "JSTOR"),
)
