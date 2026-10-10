"""环境生物技术学科论文支持：生物修复、生物降解与生物能源研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_biotechnology",
    aliases=(
        "environmental_biotechnology", "环境生物技术",
        "environmental biotechnology", "环境生物技术",
        "bioremediation", "生物修复",
        "biodegradation", "生物降解",
        "bioenergy", "生物能源",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（生物技术问题与背景）",
            "methodology（实验设计、菌种筛选、测试方法）",
            "results（生物效果与评估）",
            "discussion（技术改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "biotech process（生物技术过程）",
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
        "experiment": "实验条件须完整（温度、pH、菌种等）",
        "analysis": "分析方法须注明（GC、HPLC 等）",
        "safety": "生物安全须声明",
    },
    conventions=(
        "温度用 °C 表示",
        "pH 用 1-14 范围表示",
        "菌种须注明来源与编号",
        "降解率用 % 表示",
        "生物量用 g/L 表示",
    ),
    key_venues=(
        "Biotechnology and Bioengineering",
        "Applied Microbiology and Biotechnology",
        "Journal of Biotechnology",
        "Bioresource Technology",
        "Biotechnology for Biofuels",
        "Environmental Biotechnology",
    ),
    units_and_formulas_notes=(
        "温度用 °C 表示",
        "pH 用 1-14 范围表示",
        "菌种须注明来源与编号",
        "降解率用 % 表示",
        "生物量用 g/L 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "Origin", "GC", "HPLC", "Spectrophotometer", "pH Meter", "COD Meter", "BOD Incubator", "Dissolved Oxygen Meter", "Turbidity Meter", "Conductivity Meter", "Environmental Monitoring Software", "PCR Thermocycler", "qPCR Instrument", "DNA Sequencer", "Bioreactor"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
