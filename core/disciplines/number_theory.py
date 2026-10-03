"""数论学科论文支持：解析/代数数论体裁、AMS 引用样式与数论记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="number_theory",
    aliases=("number theory", "数论", "解析数论", "代数数论", "算术几何",
             "analytic number theory", "algebraic number theory",
             "arithmetic geometry"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与主定理陈述）",
            "preliminaries（记号：数域/模形式/L-函数等基本对象）",
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
        "computational_evidence": "数值/计算实验须说明软件、精度与可复现性，且不作为严格证明的替代",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "数论记法全文一致：素数用 p/q，整数环用 \\mathbb{Z}，有限域用 \\mathbb{F}_q",
        "渐近记号 O/o/\\ll 的定义须在首次出现处给出，并注明常数是否可计算",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "L-函数/模形式的归一化（权重、水平、特征）须显式声明",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "Inventiones Mathematicae",
        "Annals of Mathematics",
        "Journal of Number Theory",
        "Acta Arithmetica",
        "Mathematische Annalen",
        "Duke Mathematical Journal",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\ord \\v_p \\operatorname{Li}），不手打 \\mathrm 拼算子",
        "渐近式与估计式链用 \\ll 或显式常数，注明常数是否可计算",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("PARI/GP", "SageMath", "Mathematica", "LaTeX"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)