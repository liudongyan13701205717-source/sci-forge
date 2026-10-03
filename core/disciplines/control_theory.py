"""控制理论学科论文支持：系统与控制体裁、IEEE 引用样式与控制记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="control_theory",
    aliases=("control theory", "控制理论", "控制", "自动控制", "系统与控制",
             "systems and control", "鲁棒控制"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与贡献）",
            "problem formulation（系统模型与控制目标）",
            "main results（稳定性/可控性/最优控制定理）",
            "proofs（证明，长证明可移附录）",
            "numerical examples（数值示例与仿真）",
            "conclusions",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background and motivation",
            "main exposition（以例子驱动的建模-设计链）",
            "exercises（练习，可选）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview（问题源流与关键节点）",
            "main developments（按主题组织的理论-方法综述）",
            "open problems（未解决问题清单）",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号引用，如 [1]）",
    reporting_standards={
        "model_completeness": "系统模型须完整定义：状态方程、输入/输出、扰动与约束",
        "proof": "稳定性/收敛性/最优性定理必须给出完整证明，或明确引用出处",
        "simulation_evidence": "仿真须说明模型参数、控制器参数、初值与时间步长",
        "attribution": "方法与定理的归属必须准确：首次提出者与其发表出处须引用",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "状态空间记法全文一致：\\dot{x} = Ax + Bu，输出 y = Cx + Du",
        "稳定性概念（Lyapunov/输入-状态/有限时间）在首次出现处定义并注明出处",
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "控制器设计给出显式参数与可复现的仿真设置",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "IEEE Transactions on Automatic Control",
        "Automatica",
        "SIAM Journal on Control and Optimization",
        "Systems & Control Letters",
        "International Journal of Control",
        "IEEE Control Systems Letters",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{diag} \\operatorname{tr}），不手打 \\mathrm 拼算子",
        "LMI/矩阵不等式用 \\succ \\succeq 表示正定/半正定，注明矩阵维度",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("MATLAB", "Simulink", "Python", "Scilab"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)