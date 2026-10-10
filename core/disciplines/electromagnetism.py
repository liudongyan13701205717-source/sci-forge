"""电磁学学科论文支持：电磁理论、电磁场与电磁波研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electromagnetism",
    aliases=(
        "electromagnetism", "电磁学", "电磁理论",
        "electromagnetic theory", "电磁理论",
        "electromagnetic field", "电磁场",
        "electromagnetic wave", "电磁波",
        "electrodynamics", "电动力学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（电磁问题与背景）",
            "methodology（理论推导、数值计算、实验验证）",
            "results（电磁性能与场分布）",
            "discussion（理论意义与应用前景）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "electromagnetic analysis（电磁分析）",
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
    citation_style="APS",
    reporting_standards={
        "theory": "理论推导须完整",
        "numerical": "数值计算须注明方法与精度",
        "experiment": "实验条件须完整（频率、功率、天线等）",
    },
    conventions=(
        "电场强度用 V/m 表示",
        "磁场强度用 A/m 表示",
        "磁感应强度用 T 表示",
        "频率用 Hz 表示",
        "波长用 m 表示",
    ),
    key_venues=(
        "Physical Review Letters",
        "Physical Review B",
        "IEEE Transactions on Antennas and Propagation",
        "Journal of Applied Physics",
        "Optics Express",
        "IEEE Transactions on Microwave Theory and Techniques",
    ),
    units_and_formulas_notes=(
        "电场强度用 V/m、磁场强度用 A/m 表示",
        "磁感应强度用 T 表示",
        "频率用 Hz 表示",
        "波长用 m 表示"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "Python (scikit-rf)", "COMSOL Multiphysics", "ANSYS HFSS", "CST Studio Suite", "FEKO", "MP Studio", "MWO (Microwave Office)", "Nec2++", "OpenEMS", "MEEP", "S4", "R (RStudio)", "Excel", "Origin", "Mathematica", "Maple", "SageMath", "Julia"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "CNKI", "APS Journals"),
)
