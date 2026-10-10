"""环境保护技术学科论文支持：环保技术、污染控制与生态修复研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_protection_technology",
    aliases=(
        "environmental_protection_technology", "环境保护技术",
        "environmental protection technology", "环境保护技术",
        "environmental technology", "环境技术",
        "pollution control technology", "污染控制技术",
        "ecological restoration technology", "生态修复技术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（技术问题与背景）",
            "methodology（技术设计、实验条件、效果评估）",
            "results（技术效果与环境评估）",
            "discussion（技术改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "technology application（技术应用）",
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
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "Origin", "GC", "HPLC", "Spectrophotometer", "pH Meter", "COD Meter", "BOD Incubator", "Dissolved Oxygen Meter", "Turbidity Meter", "Conductivity Meter", "Environmental Monitoring Software", "Mass Spectrometer", "X-ray Fluorescence Spectrometer", "Infrared Gas Analyzer", "Gas Chromatograph-Mass Spectrometer"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
