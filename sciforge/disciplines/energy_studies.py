"""能源研究学科论文支持：能源政策、能源经济与可持续能源研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="energy_studies",
    aliases=(
        "energy_studies", "能源研究", "能源政策",
        "energy studies", "能源研究",
        "energy policy", "能源政策",
        "energy economics", "能源经济",
        "sustainable energy", "可持续能源",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（能源问题与背景）",
            "methodology（研究设计、数据分析、政策评估）",
            "results（政策效果与能源影响）",
            "discussion（政策优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "policy analysis（政策分析）",
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
    citation_style="APA 7",
    reporting_standards={
        "policy": "政策分析须注明数据来源与时间",
        "data": "能源数据须注明来源（IEA、EIA 等）",
        "statistics": "统计检验须注明方法与显著性水平",
    },
    conventions=(
        "能源用 TWh 或 Mtoe 表示",
        "碳排放用 tCO₂ 表示",
        "时间用 年 表示",
        "统计检验注明 t/F/χ² 值、p 值与 95% CI",
        "数据来源须标注机构与年份",
    ),
    key_venues=(
        "Energy Policy",
        "Energy Economics",
        "Renewable and Sustainable Energy Reviews",
        "Energy",
        "Nature Energy",
        "Global Environmental Change",
    ),
    units_and_formulas_notes=(
        "能源用 TWh 或 Mtoe 表示",
        "碳排放用 tCO₂ 表示",
        "时间用 年 表示",
        "统计检验注明 t/F/χ² 值、p 值与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R (RStudio)", "Python (pandas, statsmodels)", "EViews", "MATLAB", "Excel", "SPSS", "IEA Data", "EIA Data", "World Bank Data", "IMF Data", "UN Data", "Our World in Data", "BP Statistical Review", "Global Energy Monitor", "LEAP", "MARKAL", "TIMES", "Dyna-World", "CGE Model"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
