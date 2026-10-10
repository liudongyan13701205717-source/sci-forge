"""乳品科学学科论文支持：乳品化学、微生物与加工技术研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dairy_science",
    aliases=(
        "dairy_science", "乳品科学", "乳品化学",
        "dairy chemistry", "乳品化学",
        "dairy microbiology", "乳品微生物学",
        "milk chemistry", "乳化学",
        "dairy processing", "乳品加工",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（乳品问题与背景）",
            "methodology（分析方法、实验条件、数据处理）",
            "results（成分分析与质量评估）",
            "discussion（工艺优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "process analysis（工艺分析）",
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
        "analysis": "分析方法须注明（HPLC、GC、质谱等）",
        "microbiology": "微生物培养条件须完整",
        "processing": "加工参数须完整（温度、时间、压力）",
    },
    conventions=(
        "温度用 °C 表示",
        "时间用 min 或 h 表示",
        "pH 用 1-14 范围表示",
        "蛋白质含量用 % 表示",
        "脂肪含量用 % 表示",
    ),
    key_venues=(
        "Journal of Dairy Science",
        "International Dairy Journal",
        "Dairy Science & Technology",
        "Journal of Food Science",
        "Food Chemistry",
        "LWT - Food Science and Technology",
    ),
    units_and_formulas_notes=(
        "温度用 °C 表示",
        "时间用 min 或 h 表示",
        "pH 用 1-14 范围表示",
        "蛋白质与脂肪含量用 % 表示"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "HPLC", "GC", "Spectrophotometer", "pH Meter", "Viscometer", "Texture Analyzer", "Colorimeter", "Microscope", "Centrifuge", "Homogenizer", "Pasteurizer", "Fermenter", "Drying Equipment", "Packaging Machine", "PCR Thermal Cycler"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
