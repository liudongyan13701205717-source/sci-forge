"""环境工程学科论文支持：环境治理、污染控制与生态修复研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_engineering",
    aliases=(
        "environmental_engineering", "环境工程", "环境治理",
        "environmental engineering", "环境工程",
        "pollution control engineering", "污染控制工程",
        "ecological engineering", "生态工程",
        "environmental remediation", "环境修复",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（环境问题与背景）",
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
    citation_style="ACS",
    reporting_standards={
        "design": "设计参数须完整（流量、浓度、效率等）",
        "testing": "测试方法须注明（标准、仪器、环境）",
        "safety": "安全规程须声明",
    },
    conventions=(
        "流量用 m³/h 表示",
        "浓度用 mg/L 表示",
        "温度用 °C 表示",
        "pH 用 1-14 范围表示",
        "处理效率用 % 表示",
    ),
    key_venues=(
        "Environmental Science & Technology",
        "Water Research",
        "Journal of Hazardous Materials",
        "Chemical Engineering Journal",
        "Environmental Pollution",
        "Science of the Total Environment",
    ),
    units_and_formulas_notes=(
        "流量用 m³/h 表示",
        "浓度用 mg/L 表示",
        "温度用 °C 表示",
        "pH 用 1-14 范围表示",
        "处理效率用 % 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "Origin", "GC", "HPLC", "Spectrophotometer", "pH Meter", "COD Meter", "BOD Incubator", "Dissolved Oxygen Meter", "Turbidity Meter", "Conductivity Meter", "Environmental Monitoring Software", "AutoCAD Civil 3D", "EPANET", "SWMM", "ANSYS Fluent"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
