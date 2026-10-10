"""几何学学科论文支持：欧氏几何、仿射几何、射影几何、度量几何与非欧几何。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geometry",
    aliases=(
        "geometry",
        "几何学",
        "Euclidean_geometry",
        "欧氏几何",
        "affine_geometry",
        "仿射几何",
        "projective_geometry",
        "射影几何",
        "metric_geometry",
        "度量几何",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（记号与预备）",
            "results（定理与证明）",
            "discussion（讨论与应用）",
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
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX）",
    reporting_standards={
        "proof": "每个定理须给出完整证明，或明确引用出处",
        "notation": "记号全文一致；新符号在首次出现时定义",
        "attribution": "定理归属须准确，归属出处在陈述或证明处引用",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号",
        "记号全文一致：M^n 表示 n 维流形，切丛 TM，余切丛 T^*M",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma x.y)",
        "使用 amsmath/amsthm/amssymb；算子用 \\DeclareMathOperator 声明",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
    ),
    key_venues=(
        "Journal of Differential Geometry",
        "Geometriae Dedicata",
        "Journal of Geometry",
        "Advances in Geometry",
        "Mathematical Proceedings of the Cambridge Philosophical Society",
    ),
    units_and_formulas_notes=(
        "曲率用 Riemann 张量 R^\\lambda_{\\ \\mu\\nu\\rho}",
        "体积元用 dV；测地线用参数化形式",
        "使用 amsmath/amsthm/amssymb；对齐用 align/gather",
        "算子用 \\DeclareMathOperator 声明，不手打 \\mathrm 拼",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("LaTeX", "Mathematica", "Maple", "SageMath", "Jupyter Notebook", "GeoGebra", "Python", "SymPy", "Matplotlib", "Paraview", "Wolfram Alpha", "GAP", "Coq", "Lean", "Isabelle", " Singular 计算机代数", "Macaulay2", "3Blue1Brown manim", "MATLAB", "OpenSCAD"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
