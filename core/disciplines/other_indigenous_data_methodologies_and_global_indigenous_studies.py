"""其他原住民数据方法论与全球原住民研究学科论文支持：社群主导数据治理与全球原住民比较研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_indigenous_data_methodologies_and_global_indigenous_studies",
    aliases=(
        "other_indigenous_data_methodologies_and_global_indigenous_studies", "其他原住民数据方法论与全球原住民研究",
        "indigenous data methodologies", "原住民数据方法论",
        "global indigenous studies", "全球原住民研究",
        "indigenous data sovereignty", "原住民数据主权",
        "community-led research", "社群主导研究",
        "CARE principles", "CARE 数据原则",
        "indigenous knowledge", "原住民知识",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题、伦理语境与社群授权）",
            "methodology（数据治理与研究方法）",
            "results（发现与社群影响）",
            "discussion（数据主权与治理意涵）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（社群、地点与项目背景）",
            "analysis（过程追踪与方法比较）",
            "results（数据产品与社群反馈）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（IDM 理论综述）",
            "evidence synthesis（跨社群证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "数据收集须遵循 CARE 原则（Collective benefit, Authority, Responsibility, Ethics）",
        "k2": "协议须按 OCAP 原则报告社群主权与利益共享安排",
        "k3": "数据共享须说明许可层级、开放范围与撤出机制",
    },
    conventions=(
        "研究者立场（positionality）与社群关系须置于方法章节开头",
        "地点与人群命名须遵循当地社群的自称（endonym）",
        "文化敏感内容须标注可公开范围与访问限制",
        "合作社群须署名并致谢其知识产权",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "International Journal of Indigenous Health",
        "American Indian and Alaska Native Mental Health Research",
        "AIATSIS (Australian Institute of Aboriginal and Torres Strait Islander Studies) Research",
        "Indigenous Studies Review",
        "Journal of Global Indigenous History",
        "《民族研究》",
    ),
    units_and_formulas_notes=(
        "地理信息须避免精确坐标以保护圣地与采集地",
        "人口数据须注明是否获社群同意公开",
        "时间线须同时标注公历与社群自有历法（如适用）",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "MAXQDA", "ArcGIS", "QGIS", "OpenRefine", "Omeka", "CONTENTdm", "Google Earth Pro", "Microsoft Excel", "R (RStudio)", "SPSS", "EndNote", "Zotero", "Mendeley", "LaTeX", "ODK (Open Data Kit)", "KoboToolbox", "DHIS2", "Power BI"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "ProQuest"),
)
