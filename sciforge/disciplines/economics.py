"""经济学学科论文支持：宏观/微观/计量经济学综合研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="economics",
    aliases=("economics", "经济学", "宏观经济学", "微观经济学",
             "计量经济学", "经济分析"),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "model or methods（模型或方法）",
            "results（实证结果）",
            "discussion（经济含义）",
            "references",
        ),
        "applied": (
            "abstract",
            "introduction",
            "theoretical framework",
            "empirical strategy",
            "results",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式",
    reporting_standards={
        "identification": "识别策略须明确",
        "data": "数据来源须注明",
        "robustness": "稳健性检验须完整",
    },
    conventions=(
        "变量定义须明确",
        "模型设定须注明",
        "统计检验须注明",
        "数据来源须标注年份与机构",
    ),
    key_venues=(
        "American Economic Review",
        "Journal of Political Economy",
        "Econometrica",
        "Quarterly Journal of Economics",
        "Review of Economic Studies",
        "Journal of Economic Literature",
    ),
    units_and_formulas_notes=(
        "系数估计值须给出标准误",
        "统计检验须注明 t/F 值、p 值与 95% CI",
        "效应量须报告",
        "数据来源须标注年份与机构",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R (RStudio)", "Python (pandas, statsmodels)", "EViews", "MATLAB", "SAS", "Excel", "SPSS", "Origin", "World Bank Data", "IMF Data", "UN Data", "Our World in Data", "FRED", "Bureau of Economic Analysis", "Federal Reserve Data", "OECD Data", "EUROSTAT", "Penn World Table", "Global Economic Model"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
