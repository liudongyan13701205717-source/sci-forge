"""计量经济学学科论文支持：计量模型、因果推断与实证分析体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="econometrics",
    aliases=(
        "econometrics", "计量经济学", "计量学",
        "econometric modeling", "计量建模",
        "causal inference", "因果推断",
        "panel data", "面板数据",
        "time series econometrics", "时间序列计量",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与背景）",
            "method（计量模型与识别策略）",
            "results（实证结果与稳健性检验）",
            "discussion（经济含义与政策启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "model specification（模型设定）",
            "estimation（估计与检验）",
            "results（结果分析）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（计量理论综述）",
            "methodology comparison（方法对比）",
            "future directions",
            "references",
        ),
    },
    citation_style="Elsevier 样式",
    reporting_standards={
        "identification": "识别策略须明确（IV、DID、RDD等）",
        "data": "数据来源须注明",
        "robustness": "稳健性检验须完整",
    },
    conventions=(
        "变量定义须明确",
        "模型设定须注明（OLS、GMM、IV等）",
        "统计检验须注明（t检验、F检验等）",
        "数据来源须标注年份与机构",
        "异质性分析须报告不同群体差异",
    ),
    key_venues=(
        "Econometrica",
        "Journal of Econometrics",
        "Econometric Theory",
        "Review of Economics and Statistics",
        "Journal of Applied Econometrics",
        "Journal of Business & Economic Statistics",
    ),
    units_and_formulas_notes=(
        "系数估计值须给出标准误",
        "统计检验须注明 t/F 值、p 值与 95% CI",
        "效应量须报告",
        "数据来源须标注年份与机构",
        "异质性分析须报告不同群体差异",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R (RStudio)", "Python (statsmodels, linearmodels)", "EViews", "MATLAB", "SAS", "GAUSS", "TAMSTAT", "Mata", "Julia", "R (AER, plm, fixest)", "Python (pandas, numpy)", "Excel", "SPSS", "Origin", "RevMan", "JBI Review Manager", "EconometricA", "Dynare", "Julia (JuliaEconometrics)"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "Cochrane Library", "Embase", "PubMed"),
)
