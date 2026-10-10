"""遗产档案与博物馆学学科论文支持：遗产/档案/馆藏研究体裁、Chicago 17 引用样式与档案记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="heritage_archive_and_museum_studies",
    aliases=("heritage_archive_and_museum_studies", "遗产档案与博物馆学", "博物馆学", "档案学", "遗产研究", "遗产管理", "档案研究", "博物馆研究", "遗产档案"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 17（作者-标题-年份）",
    reporting_standards={
        "curatorial": "馆藏研究规范",
        "archival": "档案研究规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "藏品编号须报告",
        "来源/年代须报告",
        "描述须客观",
        "引用须注明来源",
        "描述须给出上下文",
    ),
    key_venues=(
        "Museum Management and Curatorship",
        "International Journal of Heritage Studies",
        "Archives of American Art Journal",
        "Journal of Museum Education",
        "Journal of Curatorial Studies",
    ),
    units_and_formulas_notes=(
        "时间用公元/年前后",
        "尺寸用 cm/m",
        "公式用 amsmath",
        "数值结果给出均值±SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Omeka", "DSpace", "EAD", "AtoM", "CONTENTdm", "BePress", "PastPerfect", "PastMaster", "EMu", "Iris", "ArchivesSpace", "TMS", "EndNote", "Zotero", "Mendeley", "SPSS", "R", "Python (SciPy)", "NVivo", "Atlas.ti"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
