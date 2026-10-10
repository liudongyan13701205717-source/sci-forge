"""其他经济学学科论文支持：未被细类归入的经济学理论与实证研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_economics",
    aliases=(
        "other_economics", "其他经济学",
        "other economics", "其他经济学",
        "economics not elsewhere classified", "经济学未另分类",
        "applied economics", "应用经济学",
        "econometrics", "计量经济学",
        "macroeconomics", "宏观经济学",
        "microeconomics", "微观经济学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（经济问题与文献定位）",
            "methodology（模型设定与识别策略）",
            "results（估计结果与稳健性检验）",
            "discussion（政策含义与机制讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域/行业/制度背景）",
            "analysis（机制与计量分析）",
            "results（效应估计与反事实）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（实证证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "识别策略须说明外生性来源与平行趋势检验",
        "k2": "面板与固定效应模型须报告聚类层数与双向固定效应设定",
        "k3": "估计结果须报告标准误、置信区间与异方差稳健性",
    },
    conventions=(
        "变量定义须给出全称、符号与量纲",
        "价格与金额须注明币种、年份与实际/名义口径",
        "增长率用 % 表示并注明基期",
        "回归表须统一报告 t 值或标准误位置",
        "模型设定注明估计量（OLS/GMM/IV/Heckman）",
    ),
    key_venues=(
        "American Economic Review",
        "Quarterly Journal of Economics",
        "Journal of Econometrics",
        "Journal of Development Economics",
        "Econometrica",
        "《经济研究》",
    ),
    units_and_formulas_notes=(
        "金额注明币种与基准年（如 2018 年不变价）",
        "比率与弹性用无量纲数值表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
        "标准误须在表脚说明聚类层级",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R (RStudio)", "Python (pandas, statsmodels)", "MATLAB", "EViews", "Gauss", "RATS", "Ox", "SAS", "SPSS", "Gretl", "TARCH", "World Bank WDI", "Penn World Table (PWT)", "FRED", "IMF WEO", "OECD.Stat", "LaTeX", "EndNote", "Zotero"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
