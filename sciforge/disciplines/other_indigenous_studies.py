"""其他原住民研究学科论文支持：未被细类归入的原住民历史、语言、治理与文化研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_indigenous_studies",
    aliases=(
        "other_indigenous_studies", "其他原住民研究",
        "other indigenous studies", "其他原住民研究",
        "indigenous studies not elsewhere classified", "原住民研究未另分类",
        "indigenous histories", "原住民历史",
        "indigenous languages", "原住民语言",
        "indigenous governance", "原住民治理",
        "aboriginal studies", "原住民研究",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题、语境与研究者立场）",
            "methodology（方法、协议与授权）",
            "results（发现与证据）",
            "discussion（政治与文化意涵）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（社群、事件与档案个案）",
            "analysis（档案解读与叙述分析）",
            "results（比较与模式）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与学术史综述）",
            "evidence synthesis（档案与口述证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "研究须报告与社群的关系、协议与利益共享安排",
        "k2": "口述史料须记录讲述者、场合、语言与转录许可",
        "k3": "档案使用须标注馆藏编号与访问限制等级",
    },
    conventions=(
        "研究者立场（positionality）须在方法章节开头说明",
        "人名地名用社群自称（endonym）并附通行译名",
        "口述与仪式内容须遵守社群共享协议",
        "合作社群成员须在署名与致谢中体现",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "Journal of Aboriginal History",
        "Australian Aboriginal Studies",
        "The Australian Historical Review",
        "Indigenous Studies Review",
        "American Indian Culture and Research Journal",
        "《中国边疆史地研究》",
    ),
    units_and_formulas_notes=(
        "人口与统计须注明年份与统计口径来源",
        "历史地名须标注今名与地名变迁依据",
        "语言材料须标注方言点与记录日期",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "MAXQDA", "ArcGIS", "QGIS", "ArcGIS StoryMaps", "Omeka", "CONTENTdm", "OpenRefine", "AIATSIS Library", "Wikitopia", "Microsoft Excel", "R (RStudio)", "SPSS", "Python (pandas)", "EndNote", "Zotero", "Mendeley", "LaTeX", "Tableau"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "ProQuest"),
)
