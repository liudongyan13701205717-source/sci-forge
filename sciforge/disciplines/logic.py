"""逻辑学（Logic）学科论文支持：形式逻辑、非经典逻辑与计算逻辑研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="logic",
    aliases=(
        "logic",
        "逻辑学",
        "formal logic",
        "非经典逻辑",
        "modal logic",
        "propositional",
        "predicate logic",
        "computational logic",
        "mathematical logic",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景）",
            "methodology（方法）",
            "results（结果与定理）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（文献综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago",
    reporting_standards={
        "k1": "证明报告给出形式系统或证明框架",
        "k2": "模型论结果须给出反例或模型",
        "k3": "计算逻辑说明复杂度类别",
    },
    conventions=(
        "定理环境使用 theorem/definition/remark",
        "符号定义遵循标准逻辑符号表",
        "引理与定理按出现顺序编号",
        "证明以 ∎ 或 Q.E.D. 结尾",
        "反例给出具体构造与验证",
    ),
    key_venues=(
        "Journal of Symbolic Logic",
        "Archive for Mathematical Logic",
        "Annals of Pure and Applied Logic",
        "Logic Journal of the IGPL",
        "Studia Logica",
    ),
    units_and_formulas_notes=(
        "复杂度类别使用标准 P/NP 符号",
        "模型大小以基数报告",
        "证明长度以符号数计",
        "量化算子使用 ∀/∃ 标准符号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("Coq", "Isabelle/HOL", "Lean 4", "Agda", "Mizar", "Prover9", "Mace4", "OTTER", "Vampire", "E (Equation solver)", "SAT solver (MiniSat)", "SAT solver (Glucose)", "Z3 (Theorem Prover)", "Yices", "T-Prover (Tableau)", "LaTeX", "Gödel's Proof Assistant", "KISSproof", "CoqIDE", "Twelf"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
