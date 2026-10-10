"""数学与统计（未分类）学科论文支持：数学与统计交叉领域、统计计算与数据科学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mathematics_and_statistics_not",
    aliases=("mathematics and statistics not", "数学与统计未分类", "数学与统计综合",
             "统计数学", "应用统计", "computational statistics", "数据科学",
             "数据科学与统计", "统计计算", "计量经济学"),
    paper_types={
        "research": ("abstract", "introduction（问题背景与统计/数学模型）", "model and methodology（模型假设、方法与记号）", "results（数值结果、模拟验证或实证分析）", "discussion（结论、局限与应用）", "references"),
        "case_study": ("abstract", "introduction", "case description（数据集与模型选择）", "analysis（模型诊断与结果分析）", "results（拟合与预测）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（方法分类与比较）", "evidence synthesis", "future directions", "references"),
    },
    citation_style="APA 7（统计学与数据科学常用）",
    reporting_standards={
        "model_specification": "模型设定须明确：分布假设、参数化、链接函数",
        "inference": "推断给置信区间、p 值与检验假设",
        "reproducibility": "代码与数据可获取；给随机种子、版本与环境",
    },
    conventions=(
        "变量命名统一：X 为自变量、Y 为因变量、β 为参数",
        "假设编号（H0、H1）并在检验中引用",
        "模型比较给 AIC/BIC/BF/LOO 等指标",
        "数值结果以表格给出，含估计值、SE、CI、p 值",
        "图表标注单位、样本量与显著性水平",
    ),
    key_venues=(
        "Journal of the American Statistical Association",
        "Annals of Statistics",
        "Journal of Computational and Graphical Statistics",
        "Biometrika",
        "Statistical Science",
    ),
    units_and_formulas_notes=(
        "p 值保留四位有效数字；R²/调整 R² 保留三位",
        "置信区间给水平（如 95%）与宽度",
        "信息准则（AIC/BIC）给具体数值与比较基准",
        "残差/散点/拟合图标注置信带与预测带",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "Python (NumPy/SciPy)", "Python (scikit-learn)", "Python (statsmodels)", "Python (PyMC)", "MATLAB", "Stata", "SAS", "SPSS", "JMP", "Minitab", "Julia", "Bayesian Model Building (R)", "Jupyter Notebook", "LaTeX", "Tableau", "GraphPad Prism", "Origin Pro", "Microsoft Excel", "BibTeX/Zotero"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "CNKI"),
)
