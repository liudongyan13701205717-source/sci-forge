"""应用统计学科论文支持：数据驱动统计建模、贝叶斯/机器学习融合、实证分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="applied_statistics",
    aliases=(
        "applied statistics",
        "Applied statistics",
        "应用统计",
        "应用统计学",
        "统计建模",
        "statistical modelling",
        "机器学习",
        "machine learning",
        "数据科学",
        "data science",
        "贝叶斯统计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题背景与统计挑战）",
            "data and methodology（数据、模型、假设）",
            "results（估计、推断、预测）",
            "sensitivity and robustness",
            "conclusion",
            "references",
        ),
        "methodological": (
            "abstract",
            "introduction",
            "theory and assumptions",
            "algorithm and asymptotics",
            "simulation studies",
            "real data application",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "methodological landscape",
            "comparison table",
            "open problems",
            "references",
        ),
    },
    citation_style="Chicago 或 AMS（作者-字母编号）；期刊依投稿期刊而定",
    reporting_standards={
        "data": "数据来源、缺失值处理、样本量与随机种子须说明",
        "model": "模型假设、参数与正则化项须明确声明",
        "inference": "置信区间（95% CI）、p 值或后验区间必须报告",
        "simulation": "蒙特卡洛次数、参数网格与计算时间须报告",
        "software": "使用软件与包版本须注明；代码/数据须公开（建议 arXiv + Zenodo）",
    },
    conventions=(
        r"变量以 $X, Y, Z$ 表示随机变量；观测值用下标 $x_i, y_i$",
        r"统计量报告 $\hat{\theta}$、$\sigma$、$\mathrm{SE}$；置信区间用 $[\text{L}, \text{U}]$",
        r"模型拟合用 $\mathcal{L}$ 表示似然、$\ell$ 表示对数似然",
        r"贝叶斯模型给先验、后验；MCMC 报告迭代数、burn-in、链数",
        "图表标题中英对照；显著性标记 *p<.05 **p<.01",
    ),
    key_venues=(
        "Journal of the American Statistical Association (JASA)",
        "The Annals of Statistics",
        "Journal of Applied Statistics",
        "Biometrika",
        "Annals of Applied Statistics",
        "Journal of Statistical Planning and Inference",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsmath/amssymb；对齐用 align/gather",
        r"随机变量加粗 $\mathbf{X}$；期望 $\mathbb{E}$，方差 $\mathrm{Var}$",
        r"贝叶斯后验 $p(\theta \mid x)$；先验 $\pi(\theta)$",
        r"显著性 $p<.05/.01/.001$；效应量 $\eta^2, d, \hat{\rho}$",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "RStudio", "Python", "SAS", "Stata", "SPSS", "JMP", "Minitab", "JASP", "Jamovi", "LaTeX", "Overleaf", "Tableau", "Power BI", "Excel", "Stan（贝叶斯建模）", "JAGS", "INLA", "brms (R)", "scikit-learn", "PyTorch", "TensorFlow", "ggplot2", "ggstatsplot", "Shiny", "Zotero"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Web of Science", "JSTOR", "DBLP"),
)
