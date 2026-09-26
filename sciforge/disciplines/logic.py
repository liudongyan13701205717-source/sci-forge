"""逻辑学学科论文支持：数理逻辑/集合论体裁、AMS 引用样式与逻辑记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="logic",
    aliases=("logic", "逻辑", "数理逻辑", "集合论", "模型论", "证明论",
             "mathematical logic", "set theory", "model theory", "proof theory"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与主定理陈述）",
            "preliminaries（语言、结构、公理系统与记号）",
            "main results（定理/命题，按编号陈述）",
            "proofs（证明，长证明可移附录）",
            "examples and applications（示例与应用）",
            "concluding remarks（进一步问题）",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background and motivation",
            "main exposition（以例子驱动的定理-证明链）",
            "exercises（练习，可选）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview（问题源流与关键节点）",
            "main developments（按主题组织的定理-证明链与归属）",
            "open problems（未解决问题清单）",
            "references",
        ),
    },
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX，如 [Smi04]）",
    reporting_standards={
        "proof": "每个定理必须给出完整证明，或明确引用出处；不得以“显然”替代论证",
        "attribution": "定理归属必须准确：首次证明者与其发表出处须在陈述或证明处引用",
        "metatheory_explicitness": "证明所用的元理论（ZFC/PA/构造性框架等）须显式声明",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "逻辑记法全文一致：满足关系用 \\vDash，可证性用 \\vdash，否定用 \\lnot",
        "语言/结构/理论的三元组记法（\\mathcal{L}, \\mathfrak{A}, T）在首次出现处定义",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "独立性/一致性结果须注明所用公理系统与相对一致性框架",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "Journal of Symbolic Logic",
        "Annals of Pure and Applied Logic",
        "Transactions of the American Mathematical Society",
        "Notre Dame Journal of Formal Logic",
        "Archive for Mathematical Logic",
        "Bulletin of Symbolic Logic",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{Th} \\operatorname{Con}），不手打 \\mathrm 拼算子",
        "推导树/证明树用 prooftree 或 bussproofs 排版，避免手绘 ASCII",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("Coq", "Isabelle", "Prolog", "TLA+", "LaTeX"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)