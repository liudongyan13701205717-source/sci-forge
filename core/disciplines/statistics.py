"""统计学论文支持：参数与非参数方法、假设检验、自助法、因果推断。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="statistics",
    aliases=("statistics", "biostatistics", "biometrika", "数理统计", "计量经济", "econometrics"),
    paper_types={
        "research": ("abstract", "introduction", "methods", "results", "discussion", "references"),
        "methods": ("abstract", "introduction", "methods", "simulation", "applications", "discussion", "references"),
        "review": ("abstract", "introduction", "topics", "future", "references"),
    },
    citation_style="APA 7th",
    reporting_standards={
        "power": "样本量计算（功效分析）须声明：效应量、α、功率、脱落率",
        "assumptions": "参数检验前提（正态性、方差齐性、独立性）须检验并报告",
        "multiple_comparisons": "多重比较须校正（Bonferroni/FDR），未校正时明示",
        "missing_data": "缺失机制（MCAR/MAR/MNAR）与处理方法须声明",
        "causal": "因果推断须明确定识别策略（RCT/IV/PIP/RDD）",
    },
    conventions=(
        "置信区间与效应量均报告，不仅给 p 值",
        "统计软件与版本须写明（R 4.x 带上包名版本）",
        "渐近结果标注条件；小样本用精确检验或自助法",
        "所有估计量定义为统计量（无偏、一致、有效）",
        "图示数据分布（直方图/箱线图），不仅给摘要统计",
    ),
    key_venues=(
        "Journal of the American Statistical Association",
        "Biometrika",
        "The Annals of Statistics",
        "Journal of the Royal Statistical Society Series B",
        "Biometrics",
    ),
    units_and_formulas_notes=(
        "量纲一致性：均值/标准差与原始量纲一致；方差为量纲平方",
        "对数时说明底数；百分比方差用 logit 或 arcsin 变换",
        "Bayes 推断给先验和后验；先验敏感性分析必做",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("R", "Python (NumPy/SciPy)", "LaTeX", "Stata", "MATLAB"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Zenodo", "CNKI"),
)