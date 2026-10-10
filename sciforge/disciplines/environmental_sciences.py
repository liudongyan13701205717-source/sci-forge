"""环境科学学科论文支持：环境综合研究、环境系统分析与可持续发展体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_sciences",
    aliases=(
        "environmental_sciences", "环境科学", "环境学",
        "environmental sciences", "环境科学",
        "environmental studies", "环境研究",
        "environmental systems", "环境系统",
        "sustainability science", "可持续科学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（环境问题与背景）",
            "methodology（分析方法、实验条件、数据处理）",
            "results（成分分析与质量评估）",
            "discussion（环境优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "process analysis（过程分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（方法对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="ACS",
    reporting_standards={
        "analysis": "分析方法须注明（GC、HPLC、质谱等）",
        "sampling": "采样位置、深度与时间须完整记录",
        "statistics": "统计检验须注明方法与显著性水平",
    },
    conventions=(
        "浓度用 mg/L 表示",
        "温度用 °C 表示",
        "pH 用 1-14 范围表示",
        "生物量用 g/m² 表示",
        "统计检验注明方法、p 值与效应量",
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
        "生物量用 g/m² 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "Origin", "GC", "HPLC", "Spectrophotometer", "pH Meter", "COD Meter", "BOD Incubator", "Dissolved Oxygen Meter", "Turbidity Meter", "Conductivity Meter", "Environmental Monitoring Software", "ICP-OES", "Total Organic Carbon Analyzer", "Ion Chromatograph", "Atomic Absorption Spectrometer"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
