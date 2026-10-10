"""博弈论学科论文支持：非合作/合作博弈体裁、均衡概念与博弈建模。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="game_theory",
    aliases=("game_theory", "博弈论", "博弈", "机制设计", "mechanism design", "均衡", "equilibrium", "non-cooperative game", "cooperative game"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="作者-年份样式（如 Smith (2004)）",
    reporting_standards={"k1": "博弈模型须完整定义玩家/策略/支付（模型报告）", "k2": "均衡概念须定义并说明选择理由（均衡报告）", "k3": "证明须完整或明确引用出处（证明报告）"},
    conventions=("博弈记法全文一致：玩家 i ∈ N，策略 s_i ∈ S_i，支付 u_i(s)", "均衡概念（Nash/SPE/PBE/CE）在首次出现处定义并注明出处", "定理环境按 theorem/lemma/proposition/corollary 分级编号", "证明以 QED 方块结束", "机制设计结果须给出激励相容/个体理性约束的显式形式"),
    key_venues=("Games and Economic Behavior", "International Journal of Game Theory", "Journal of Economic Theory", "Mathematics of Operations Research", "Theoretical Economics"),
    units_and_formulas_notes=("使用 amsmath/amsthm：对齐用 align/gather，多行推导按 = 号对齐", "策略剖面用 s = (s_1, ..., s_n)，对手剖面用 s_{-i} 统一书写", "显示公式仅在被正文引用时编号", "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{BR} \\operatorname{NE}）", "括号尺寸用 \\bigl \\bigr 系列而非手动放大"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Python（NashPy）", "Gambit 博弈分析平台", "MATLAB 优化求解器", "R（ggplot2）", "LaTeX（amsmath/amsthm）", "Python（NumPy/SciPy）", "Python（SimPy）", "Java（jGAP）", "SageMath", "Python（Nash2）", "R（Econometrics）", "Python（Gambit 模拟器）", "MATLAB（optimization toolbox）", "Python（QuantEcon）", "LaTeX（amsthm）", "Python（JAX）", "R（shiny）", "MATLAB（Statistics and Machine Learning Toolbox）", "Python（SymPy）", "SAS（博弈数据分析）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
