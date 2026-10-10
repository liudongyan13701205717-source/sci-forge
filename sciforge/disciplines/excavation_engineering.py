"""挖掘工程学科论文支持：土方工程、地基处理与地下工程研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="excavation_engineering",
    aliases=(
        "excavation_engineering", "挖掘工程", "土方工程",
        "excavation engineering", "挖掘工程",
        "earthwork", "土方工程",
        "foundation engineering", "地基工程",
        "underground engineering", "地下工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程问题与背景）",
            "methodology（设计方法、实验条件、测试）",
            "results（工程效果与性能评估）",
            "discussion（技术改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "implementation（实现过程）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（技术对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="ASCE",
    reporting_standards={
        "design": "设计参数须完整（深度、坡度、承载力等）",
        "testing": "测试方法须注明（标准、仪器、环境）",
        "safety": "安全规程须声明",
    },
    conventions=(
        "深度用 m 表示",
        "坡度用 ° 或 % 表示",
        "承载力用 kPa 表示",
        "土方量用 m³ 表示",
        "安全系数用 比值 表示",
    ),
    key_venues=(
        "Journal of Geotechnical and Geoenvironmental Engineering",
        "Canadian Geotechnical Journal",
        "Engineering Geology",
        "Journal of Construction Engineering and Management",
        "Tunnelling and Underground Space Technology",
        "International Journal of Rock Mechanics and Mining Sciences",
    ),
    units_and_formulas_notes=(
        "深度用 m 表示",
        "坡度用 ° 或 % 表示",
        "承载力用 kPa 表示",
        "土方量用 m³ 表示",
        "安全系数用 比值 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "ANSYS", "Abaqus", "FLAC3D", "PLAXIS", "MIDAS", "SAP2000", "ETABS", "SAFE", "AutoCAD", "Revit", "Civil 3D", "MicroStation", "ArcGIS", "QGIS", "HEC-RAS", "SWAN", "Xbeach", "MIKE21"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ASCE Library"),
)
