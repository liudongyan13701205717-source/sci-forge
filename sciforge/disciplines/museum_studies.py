"""博物馆研究学科论文支持：观众研究、策展与藏品研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="museum_studies",
    aliases=(
        "museum_studies", "博物馆研究", "Museum studies",
        "curatorial studies", "策展研究", "museum governance",
        "博物馆治理", "public museums",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（研究设计与样本）",
            "results（发现）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（博物馆案例）",
            "analysis（观众/藏品/展览分析）",
            "results（结果）",
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
    citation_style="Chicago 样式",
    reporting_standards={
        "k1": "观众研究须报告样本量、抽样方法与信效度",
        "k2": "策展研究须报告创作过程、评审标准与反馈",
        "k3": "机构研究须报告治理结构与运营数据",
    },
    conventions=(
        "博物馆名称与所在地须首次出现即说明",
        "藏品描述遵循 ICOM 分类与命名规范",
        "观众访谈须报告知情同意与伦理审查",
        "展览评估须报告开放时间与参观时段",
        "引用馆藏文件须给出藏品编号与来源",
    ),
    key_venues=(
        "Museum Management and Curatorship",
        "Curator: The Museum Journal",
        "Museum International",
        "Journal of Material Culture",
        "《博物馆研究》",
    ),
    units_and_formulas_notes=(
        "参观人数按日/月/年口径分组",
        "藏品规模用件数/套数并说明口径",
        "观众停留时长用分钟；展项停留用秒",
        "引用馆藏编号须遵循博物馆内部编码",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "MAXQDA", "SPSS", "RStudio", "Tableau", "Power BI", "SketchUp", "Adobe InDesign", "Adobe Illustrator", "Omeka", "Axiell AX", "Cohesion", "EndNote", "Zotero", "Microsoft Excel", "KoboToolbox", "Google Analytics", "Python", "JMP"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
