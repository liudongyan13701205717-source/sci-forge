"""海关与关税学科论文支持：国际贸易、关税政策与海关管理研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="customs_programmes",
    aliases=(
        "customs_programmes", "海关与关税", "海关管理",
        "customs administration", "海关行政",
        "tariff policy", "关税政策",
        "international trade", "国际贸易",
        "customs brokerage", "报关",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（贸易问题与政策背景）",
            "method（研究设计、数据分析、政策评估）",
            "results（政策效果与贸易影响）",
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
        "trade": "贸易数据须注明来源（WTO、UN Comtrade 等）",
        "statistics": "统计检验须注明方法与显著性水平",
    },
    conventions=(
        "关税用 % 表示",
        "贸易额用 美元 表示",
        "时间用 年 表示",
        "统计检验注明 t/F/χ² 值、p 值与 95% CI",
        "数据来源须标注机构与年份",
    ),
    key_venues=(
        "Journal of International Economics",
        "World Trade Review",
        "Journal of World Trade",
        "International Trade Journal",
        "World Bank Economic Review",
    ),
    units_and_formulas_notes=(
        "关税用 % 表示",
        "贸易额用 美元 表示",
        "时间用 年 表示",
        "统计检验注明 t/F/χ² 值、p 值与 95% CI",
        "数据来源须标注机构与年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R (RStudio)", "Python (pandas, statsmodels)", "EViews", "MATLAB", "Excel", "SPSS", "SAS", "JMP", "GAMS", "Gurobi", "Julia", "GTAP", "Tariff Analysis Online (ITC)", "R (fixest)", "R (ppmlhdfe)", "R (plm)", "PyMC", "Stan", "R (Aster)"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
