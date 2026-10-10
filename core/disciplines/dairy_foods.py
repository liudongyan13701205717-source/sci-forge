"""乳制品学科论文支持：乳制品加工、质量控制与营养研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dairy_foods",
    aliases=(
        "dairy_foods", "乳制品", "乳制品科学",
        "dairy science", "乳品科学",
        "dairy technology", "乳品技术",
        "milk processing", "乳品加工",
        "dairy products", "乳制品",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（乳制品问题与背景）",
            "methodology（加工工艺、实验条件、分析方法）",
            "results（产品质量与营养评估）",
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
            "comparison（工艺对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="ACS",
    reporting_standards={
        "processing": "加工参数须完整（温度、时间、压力）",
        "analysis": "分析方法须注明（HPLC、GC 等）",
        "safety": "食品安全须注明标准（ISO、GB 等）",
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
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "HPLC", "GC", "Spectrophotometer", "pH Meter", "Viscometer", "Texture Analyzer", "Colorimeter", "Microscope", "Centrifuge", "Homogenizer", "Pasteurizer", "Fermenter", "Drying Equipment", "Packaging Machine", "Kjeldahl Nitrogen Analyzer"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
