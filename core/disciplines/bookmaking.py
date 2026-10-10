"""博彩/赔率学学科论文支持：博彩概率模型/赔率设计体裁、统计学引用样式与博彩记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bookmaking",
    aliases=(
        "bookmaking",
        "Bookmaking (horses etc)",
        "博彩",
        "博彩业",
        "赔率学",
        "博彩数学",
        "投注",
        "betting",
        "wagering",
        "gambling mathematics",
        "odds setting",
        "博彩建模",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "data and methods（样本、模型、方法）",
            "results（模型性能与赔率效率）",
            "discussion",
            "conclusion",
            "references",
        ),
        "empirical": (
            "abstract",
            "introduction",
            "literature review",
            "data and methodology",
            "results and analysis",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7（统计学/经济学引用样式）",
    reporting_standards={
        "data": "数据来源、样本期间、样本量须明确",
        "models": "模型设定与假设须完整列出",
        "efficiency": "市场效率指标（Kunreuther 检验、Sharpe 比率）须报告",
        "validation": "验证方法（交叉验证、样本外）须报告",
    },
    conventions=(
        "赔率符号用 decimal（1.5）或 fractional（1/2）并明确单位",
        "概率用小数（0.67）而非百分比",
        "期望值 E[X] 与方差 Var[X] 符号统一",
        "Kunreuther 检验须给出样本量与显著性水平",
        "回报指标以年化或赛季化表示",
    ),
    key_venues=(
        "Journal of Gambling Studies",
        "Journal of Gambling Behavior",
        "Journal of Applied Statistics",
        "Journal of the American Statistical Association",
        "International Journal of Forecasting",
        "SIAM Journal on Applied Mathematics",
        "Mathematical Operations Research",
    ),
    units_and_formulas_notes=(
        "赔率用 decimal（如 1.5）或 fractional（如 1/2）",
        "概率用小数（0.67）",
        "期望值 E[X] 与方差 Var[X]",
        "回报指标以年化或赛季化表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (pandas)", "Python (numpy)", "Python (scipy)", "R", "SQL", "Excel", "MongoDB", "Apache Kafka", "Apache Spark", "Tableau", "Power BI", "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "XGBoost", "LightGBM", "CatBoost", "AWS"),
    category="经济学",
    databases=("OpenAlex", "Google Scholar", "SSRN", "arXiv", "ScienceDirect"),
)
