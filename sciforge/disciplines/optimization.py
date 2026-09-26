"""最优化学科论文支持：凸优化/算法体裁、AMS 引用样式与优化记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="optimization",
    aliases=("optimization", "最优化", "优化", "数学规划", "凸优化",
             "convex optimization", "非光滑优化"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与贡献）",
            "problem formulation（问题定义与假设）",
            "algorithm（算法设计与理论性质）",
            "convergence analysis（收敛性/复杂度分析）",
            "numerical experiments（数值实验与基准对比）",
            "conclusions",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background and motivation",
            "main exposition（以例子驱动的建模-算法链）",
            "exercises（练习，可选）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview（问题源流与关键节点）",
            "main developments（按主题组织的算法-理论综述）",
            "open problems（未解决问题清单）",
            "references",
        ),
    },
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX，如 [Smi04]）",
    reporting_standards={
        "problem_assumptions": "目标函数与约束的凸性/光滑性/正则性假设须显式列出",
        "convergence_analysis": "收敛率（线性/超线性/次线性）与复杂度须给出严格证明或明确引用出处",
        "algorithm_reproducibility": "算法须给出完整描述、参数选择与可复现实现",
        "computational_evidence": "数值实验须说明硬件、软件、求解器、实例与统计显著性",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "问题用标准形式书写：min f(x) s.t. g_i(x) \\le 0, h_j(x) = 0，变量域显式声明",
        "收敛性记法全文一致：迭代点 x_k，最优值 f^*，最优解集 X^*",
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "复杂度分析注明 oracle 模型（一阶/二阶/随机）与常数依赖",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "SIAM Journal on Optimization",
        "Mathematical Programming",
        "Journal of Optimization Theory and Applications",
        "Optimization Methods and Software",
        "Computational Optimization and Applications",
        "Mathematics of Operations Research",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{prox} \\operatorname{dom}），不手打 \\mathrm 拼算子",
        "次梯度/共轭函数用 \\partial f 与 f^* 统一书写，注明定义域",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Gurobi", "CPLEX", "MATLAB", "Python (SciPy)", "OR-Tools"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)