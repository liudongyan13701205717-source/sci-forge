"""其他历史、遗产与考古学学科论文支持：未被细类归入的历史、文化遗产与考古研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_history_heritage_and_archaeology",
    aliases=(
        "other_history_heritage_and_archaeology", "其他历史遗产与考古学",
        "other history, heritage and archaeology", "其他历史遗产与考古学",
        "archaeology", "考古学",
        "heritage studies", "遗产研究",
        "historical research", "历史研究",
        "palaeontology", "古生物学",
        "historical geography", "历史地理学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与史料状况）",
            "methodology（史料/遗迹/科技方法）",
            "results（分期、复原与解释）",
            "discussion（历史意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（遗址/文书/遗物个案）",
            "analysis（器物学与地层学分析）",
            "results（年代与归属判定）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与学派综述）",
            "evidence synthesis（史料与实证综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago Notes-Bibliography",
    reporting_standards={
        "k1": "考古发掘须按《田野考古操作规程》报告探方、地层与出土关系",
        "k2": "碳十四年代须报告 ¹⁴C 年龄、校准区间（IntCal 版本）与不确定度",
        "k3": "史料须注明馆藏、编号与版本，译文须标注译者与出处",
    },
    conventions=(
        "年表须标注公元前后及本世纪/年/月口径",
        "遗址坐标用 WGS84 并注明高程基准",
        "器物描述使用标准形制术语并附图版编号",
        "引文须注明页码；二手文献须注明原始出处",
        "术语中英并列且全文统一",
    ),
    key_venues=(
        "Antiquity",
        "World Archaeology",
        "Archaeological and Anthropological Sciences",
        "The Journal of Archaeological Method and Theory",
        "International Journal of Heritage Studies",
        "《考古》",
    ),
    units_and_formulas_notes=(
        "¹⁴C 年代用 ka BP 表示并附校准区间",
        "遗址坐标用经纬度（WGS84）与海拔 m 表示",
        "器物尺寸用 cm 表示并说明测量部位",
        "统计检验注明方法、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("EndNote", "Zotero", "Mendeley", "LaTeX", "ArcGIS", "QGIS", "OpenRefine", "Omeka", "CONTENTdm", "Heritage Gateway", "ArchaeologicalGIS (AGIS)", "SketchUp", "Autodesk ReCap", "Agisoft Metashape", "CloudCompare", "Meshroom", "Google Earth Pro", "Microsoft Excel", "NVivo", "Autodesk Maya"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI", "ProQuest"),
)
