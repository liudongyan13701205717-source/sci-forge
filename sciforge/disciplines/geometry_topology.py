"""几何与拓扑学科论文支持：微分几何、代数拓扑、几何拓扑、曲面与流形理论。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geometry_topology",
    aliases=(
        "geometry_topology",
        "几何与拓扑",
        "differential_geometry",
        "微分几何",
        "algebraic_topology",
        "代数拓扑",
        "geometric_topology",
        "几何拓扑",
        "manifold_theory",
        "流形理论",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与主定理）",
            "methodology（流形/复形/纤维丛等基本对象与记号）",
            "results（定理/命题，按编号陈述）",
            "discussion（证明、示例与应用）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（几何对象与设定）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（历史综述与关键节点）",
            "evidence synthesis（定理-证明链与归属）",
            "future directions",
            "references",
        ),
    },
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX，如 [Smi04]）",
    reporting_standards={
        "proof": "每个定理必须给出完整证明，或明确引用出处；不得以“显然”替代论证",
        "attribution": "定理归属必须准确：首次证明者与其发表出处须在陈述或证明处引用",
        "smoothness_conditions": "流形/映射的光滑性、紧性与定向假设须显式列出，并说明退化情形",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "流形记法全文一致：M^n 表示 n 维流形，切丛用 TM，余切丛用 T^*M",
        "同调/同伦群记法统一：H_k(X)、\\pi_k(X)，基点的选择须显式声明",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "Geometry & Topology",
        "Journal of Differential Geometry",
        "Algebraic & Geometric Topology",
        "Inventiones Mathematicae",
        "Annals of Mathematics",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\Hom \\Ext \\Sym \\wedge），不手打 \\mathrm",
        "交换图用 tikz-cd 或 amscd，避免手绘 ASCII 图",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("LaTeX", "Mathematica", "Maple", "SageMath", "Jupyter Notebook", "GeoGebra", "Python", "SymPy", "Matplotlib", "3Blue1Brown manim", "GAP", "Coq", "Lean", "Isabelle", "Singular", "Macaulay2", "Toric Geometry", "Topos 拓扑学库", "MATLAB", "OpenSCAD"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
