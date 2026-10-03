"""数值分析学科论文支持：数值方法/误差分析体裁、AMS 引用样式与数值记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="numerical_analysis",
    aliases=("numerical analysis", "数值分析", "数值方法", "科学计算",
             "numerical methods", "scientific computing"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与贡献）",
            "problem setting（问题定义与离散化）",
            "numerical method（算法设计与理论性质）",
            "error analysis（收敛性/稳定性/复杂度分析）",
            "numerical experiments（数值实验与基准对比）",
            "conclusions",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background and motivation",
            "main exposition（以例子驱动的算法-分析链）",
            "exercises（练习，可选）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview（问题源流与关键节点）",
            "main developments（按主题组织的算法-分析综述）",
            "open problems（未解决问题清单）",
            "references",
        ),
    },
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX，如 [Smi04]）",
    reporting_standards={
        "algorithm_reproducibility": "算法须给出完整描述、复杂度分析与可复现实现（代码/数据可用性）",
        "error_analysis": "收敛阶、误差界与稳定性分析须给出严格证明或明确引用出处",
        "computational_evidence": "数值实验须说明硬件、软件、精度、网格与统计显著性",
        "attribution": "方法与定理的归属必须准确：首次提出者与其发表出处须引用",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "离散化记法全文一致：网格步长 h、时间步长 \\Delta t、数值解用下标或上标区分",
        "误差记法统一：\\lVert e_h \\rVert 表示离散误差，注明范数类型",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "数值实验报告收敛阶（实测 vs 理论）、CPU 时间与内存",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "SIAM Journal on Numerical Analysis",
        "SIAM Journal on Scientific Computing",
        "Numerische Mathematik",
        "Mathematics of Computation",
        "BIT Numerical Mathematics",
        "Journal of Computational Physics",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{cond} \\operatorname{flop}），不手打 \\mathrm 拼算子",
        "浮点运算用 \\operatorname{fl}(\\cdot) 表示，注明舍入模型",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("MATLAB", "Python (NumPy/SciPy)", "Julia"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)