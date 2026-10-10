"""供水学科论文支持：饮用水处理工艺、管网优化与水质量保障的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="water_supply",
    aliases=("water_supply", "供水", "供水工程", "自来水厂", "饮用水处理",
             "water supply", "water treatment plant", "drinking water",
             "water distribution", "water quality"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "engineering implications（工程意义）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "plant description（水厂概况）",
            "water source and quality（水源与水质）",
            "treatment process（处理工艺）",
            "performance evaluation（运行效果评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "water source development（水源开发综述）",
            "treatment technologies（处理技术综述）",
            "distribution system management（配水系统管理综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "water_quality": "水质指标须按 GB 5749 或 WHO 饮用水标准检测，标注方法编号与检出限",
        "network_analysis": "管网水力计算须采用 EPANET 或同等级模型，验证压力、流量与水质指标",
        "leakage_assessment": "漏损评估须给出 DMA（分区计量）数据与漏损率计算方法",
    },
    conventions=(
        "供水压力以 MPa 或 mH₂O 为单位",
        "浊度以 NTU 为单位，色度以度（Hazen）为单位",
        "余氯以 mg/L 标注，明确取样点与取样时间",
        "漏损率 = (供水量 - 售水量) / 供水量 × 100%",
        "管网图按 GB/T 13734 图例绘制",
    ),
    key_venues=(
        "Water Research",
        "Journal of Water Process Engineering",
        "Water Science and Technology",
        "Desalination",
        "Science of the Total Environment",
    ),
    units_and_formulas_notes=(
        "流量：m³/h 或 m³/d",
        "压力：MPa 或 mH₂O",
        "浊度：NTU",
        "余氯：mg/L",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("EPANET", "WaterGEMS", "Bentley Hammer", "MATLAB", "Python", "R", "SPSS", "Microsoft Excel", "Tableau", "ArcGIS Pro", "QGIS", "AutoCAD", "SolidWorks", "COMSOL Multiphysics", "SWMM", "Visual MINTEQ", "LaTeX", "OpenRefine", "WEKA", "GeoMedia"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
