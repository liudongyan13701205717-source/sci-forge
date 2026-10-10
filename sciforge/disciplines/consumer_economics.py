"""消费经济学学科论文支持：需求分析、效用理论、计量与消费结构。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="consumer_economics",
    aliases=(
        "consumer economics",
        "consumption economics",
        "需求经济学",
        "消费经济学",
        "需求理论",
        "效用理论",
        "consumer theory",
        "household economics",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与贡献）",
            "theoretical framework（模型设定与假设）",
            "data and methodology（数据来源与计量方法）",
            "results（估计结果与稳健性检验）",
            "conclusion",
            "references",
        ),
        "empirical_study": (
            "abstract",
            "introduction",
            "model（需求函数或效用模型）",
            "data",
            "estimation",
            "results and robustness",
            "conclusion",
        ),
        "policy_analysis": (
            "abstract",
            "policy background",
            "analysis framework",
            "empirical evidence",
            "policy implications",
            "conclusion",
        ),
        "review": (
            "abstract",
            "historical overview",
            "current methods",
            "open challenges",
            "references",
        ),
    },
    citation_style="APA 或 Chicago 样式，经济学主流",
    reporting_standards={
        "data": "数据来源须报告口径、年份、地理范围与缺失处理",
        "estimation": "计量方法须报告估计量、标准误类型（异方差/聚类/Bootstrap）",
        "inference": "假设检验须报告检验统计量、p 值与置信区间",
        "identifying_assumption": "识别假设须显式陈述并说明稳健性检验",
    },
    conventions=(
        "需求函数形式遵循 AVER、AIDS、QUAIDS 或 QUAIDS-MAC",
        "效用理论符号遵循 Varian《Intermediate Microeconomics》",
        "标准误报告聚类/异方差稳健值，标注 cluster 层级",
        "显著性水平用 *** p<0.01, ** p<0.05, * p<0.1",
        "数据年份用 4 位数字，货币统一并注明基准年",
    ),
    key_venues=(
        "American Economic Review",
        "Journal of Political Economy",
        "Econometrica",
        "Journal of Econometrics",
        "Journal of Consumer Economics",
        "Review of Economics and Statistics",
        "Economic Journal",
        "经济学（季刊）",
        "经济研究",
        "中国工业经济",
    ),
    units_and_formulas_notes=(
        "价格指数化至基准年；名义/实际区分明确",
        "收入用对数 ln(Y)；支出份额用 %",
        "弹性用 ε 或 e；半弹性用 β",
        "t 统计量报告到 2 位小数，p 值报告到 3 位",
        "R²、调整 R² 与 Hausman 检验须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "R Commander", "Python", "NumPy", "SciPy", "pandas", "statsmodels", "linearmodels", "EViews", "GAUSS", "MATLAB", "Julia", "OxMetrics", "Gretl", "TASA", "Estata", "LIMDEP", "NLS", "EpiReg", "LimReg", "Tobit", "Heckit", "SAS", "SAS ETS", "SPSS", "Stata MP", "SAS/ETS", "JMP", "Minitab", "OriginLab", "Excel", "R Markdown", "LaTeX", "RStudio", "Quandl", "FRED", "CEIC Data", "Wind", "CSMAR", "国泰安 CSMAR"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "Web of Science", "NBER", "JEL", "RePEc", "CNKI", "中经网统计数据库"),
)
