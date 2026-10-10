"""计算理论学科论文支持：形式语言、图灵机、自动机与语言层级研究体裁、AMS 引用样式与形式化记号注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="theory_of_computation",
    aliases=(
        "theory_of_computation",
        "Theory Of Computation",
        "计算理论",
        "计算模型",
        "形式语言与自动机",
        "Turing computability",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题背景与动机）",
            "preliminaries（定义与记号）",
            "main results（定理与推论）",
            "proofs（证明）",
            "conclusions",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background",
            "main exposition（以例子驱动的定理-证明链）",
            "exercises",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview",
            "main developments",
            "open problems",
            "references",
        ),
    },
    citation_style="AMS 样式（作者-字母编号，如 [Hop00]）",
    reporting_standards={
        "definitions": "所有定义须给出完整形式化陈述（输入/输出/判定条件）",
        "proofs": "定理须给出完整证明，构造性证明须给出显式构造或归约",
        "attribution": "定理归属须准确（首次证明者与出处）",
        "boundaries": "须明确区分可判定性与可计算性的适用范围",
    },
    conventions=(
        "定义-定理-证明格式，编号一致（amsthm 环境）",
        "自动机转移函数给出完整映射（状态×输入→状态/输出）",
        "规约构造须给出映射函数并证明保持性",
        "图灵机须标明带子、头位置与停机条件",
        "猜想的结论须显式标注（conjecture / open problem）",
    ),
    key_venues=(
        "Journal of the ACM",
        "Theoretical Computer Science",
        "Information and Computation",
        "Logical Methods in Computer Science",
        "Mathematical Logic Quarterly",
    ),
    units_and_formulas_notes=(
        "时间/空间复杂度用大 O 记号并注明机器模型（Turing/RAM）",
        "语言层级关系用包含符号（⊆）与真包含（⊊）",
        "正则表达、文法与自动机之间的等价性须引用定理编号",
        "停机问题的判定性讨论须说明对角线或规约方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("LaTeX", "Coq", "Isabelle/HOL", "Lean 4", "Agda", "Haskell", "OCaml", "Python", "JFLAP", "Automata Studio", "SigmaSTL（可解释性语言）", "Mathematica", "SageMath", "SymPy", "Graphviz", "TikZ", "Sedna", "Axiom", "Zotero", "EndNote"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)
