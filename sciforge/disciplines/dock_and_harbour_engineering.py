"""码头与港口工程学科论文支持：港口设计、水工结构与航运工程体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dock_and_harbour_engineering",
    aliases=(
        "dock_and_harbour_engineering", "码头与港口工程",
        "harbour engineering", "港口工程",
        "port engineering", "港口工程",
        "coastal engineering", "海岸工程",
        "marine construction", "海洋建筑",
        "breakwater design", "防波堤设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（港口问题与背景）",
            "methodology（设计方法、模型试验、分析）",
            "results（结构安全与工程效果）",
            "discussion（设计优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（技术/经济分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "design comparison（设计对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="ASCE",
    reporting_standards={
        "model_test": "模型试验须注明缩尺比与相似条件",
        "analysis": "结构分析须注明荷载与边界条件",
        "survey": "水文测量须注明仪器与精度",
    },
    conventions=(
        "水位用 米 表示并注明基准面",
        "波浪要素（Hs、Tp、Tm）须定义",
        "流速用 m/s 表示",
        "承载力用 kPa 表示",
        "工程经济分析注明货币与年份",
    ),
    key_venues=(
        "Journal of Waterway, Port, Coastal, and Ocean Engineering",
        "Coastal Engineering",
        "Ocean Engineering",
        "Ports",
        "Marine Structures",
        "Journal of Marine Science and Engineering",
    ),
    units_and_formulas_notes=(
        "长度用 m 表示",
        "水位用 m 表示",
        "流速用 m/s 表示",
        "波浪要素 Hs 用 m 表示，Tp 用 s 表示",
        "承载力用 kPa 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "ANSYS", "Abaqus", "FLAC3D", "PLAXIS", "MIDAS", "SAP2000", "ETABS", "SAFE", "AutoCAD", "Revit", "Civil 3D", "MicroStation", "ArcGIS", "QGIS", "HEC-RAS", "SWAN", "Xbeach", "MIKE21"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ASCE Library"),
)
