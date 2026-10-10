"""数论学科论文支持：解析/代数数论体裁、AMS 引用样式与数论记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="number_theory",
    aliases=(
        "number_theory",
        "数论",
        "Number Theory",
        "Elementary Number Theory",
        "Analytic Number Theory",
        "Algebraic Number Theory",
        "Prime Numbers",
        "Modular Forms",
        "解析数论",
    ),
    paper_types={
        "research": ("abstract", "introduction（引言与动机）", "preliminaries（预备知识）", "main results（主要结果）", "proofs（证明）", "applications（应用）", "references"),
        "expository": ("abstract", "introduction", "background（背景）", "statements（命题陈述）", "proofs（证明）", "conclusions（结论）", "references"),
        "survey": ("abstract", "introduction", "historical overview（历史综述）", "key theorems（关键定理）", "open problems（开放问题）", "references"),
    },
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX）",
    reporting_standards={
        "theorem": "定理陈述遵循 AMS 格式，证明须完整",
        "conjecture": "猜想须标注状态与已知结果",
        "numerical": "数值实验说明精度与可复现性",
    },
    conventions=(
        "命题以 Theorem/Lemma/Corollary 分级编号",
        "符号使用统一约定（Z、Q、F_p、p、q）",
        "证明以 QED 方块结束，嵌套证明标 Proof of Lemma",
        "开放问题与未证明断言显式标注",
        "数值结果说明验证范围与软件",
    ),
    key_venues=(
        "Inventiones Mathematicae",
        "Annals of Mathematics",
        "Journal of Number Theory",
        "Acta Arithmetica",
        "Duke Mathematical Journal",
    ),
    units_and_formulas_notes=(
        "渐近记号 O/Θ/o/ll 使用规范并注明常数",
        "素数分布给出精确公式",
        "数值结果说明精度与验证范围",
        "计算复杂度给出渐近界",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SageMath", "Magma", "PARI/GP", "GAP", "Wolfram Mathematica", "Maple", "Lean 4", "Coq", "Isabelle/HOL", "Mathlib", "SymPy", "Antimat", "LMFDB", "OEIS", "Wolfram Alpha", "yafu", "GNU MP", "Prime95", "NTL", "FLINT"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv"),
)
