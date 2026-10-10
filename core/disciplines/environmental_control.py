"""环境控制学科论文支持：污染控制、环境监测与生态修复研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_control",
    aliases=(
        "environmental_control", "环境控制", "污染控制",
        "environmental control", "环境控制",
        "pollution control", "污染控制",
        "environmental monitoring", "环境监测",
        "ecological restoration", "生态修复",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（环境问题与背景）",
            "methodology（控制方法、实验条件、效果评估）",
            "results（控制效果与环境评估）",
            "discussion（技术改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "control process（控制过程）",
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
        "experiment": "实验条件须完整（温度、pH、浓度）",
        "analysis": "分析方法须注明（GC、HPLC 等）",
        "safety": "危险物质操作须声明安全规程",
    },
    conventions=(
        "浓度用 mg/L 表示",
        "温度用 °C 表示",
        "pH 用 1-14 范围表示",
        "处理效率用 % 表示",
        "统计检验注明效应量与置信区间",
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
        "浓度用 mg/L 表示",
        "温度用 °C 表示",
        "pH 用 1-14 范围表示",
        "处理效率用 % 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "Origin", "GC", "HPLC", "Spectrophotometer", "pH Meter", "COD Meter", "BOD Incubator", "Dissolved Oxygen Meter", "Turbidity Meter", "Conductivity Meter", "Environmental Monitoring Software", "Flue Gas Analyzer", "Particulate Matter Monitor", "VOC Analyzer", "CEMS"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
