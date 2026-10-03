"""数学学科论文支持：定理/证明体裁、AMS 引用样式与 amsmath 注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mathematics",
    aliases=("math", "数学", "定理", "证明", "代数", "几何", "拓扑", "数论",
             "algebra", "geometry", "topology", "number theory", "analysis", "分析"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与主定理陈述）",
            "preliminaries/notation（定义、记号与预备引理）",
            "main results（定理/命题，按编号陈述）",
            "proofs（证明，长证明可移附录）",
            "examples and applications（示例与应用）",
            "concluding remarks（进一步问题与猜想）",
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
        "numerical_evidence": "数值/计算实验须说明软件、精度与可复现性，且不作为严格证明的替代",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "definition 环境正文用斜体；remark/example 用罗马体",
        "proof 环境以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "重要结果首次出现时同时给出非正式陈述与形式化陈述",
        "引用已有定理时在定理陈述处或证明开头注明出处",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "Annals of Mathematics",
        "Inventiones Mathematicae",
        "Acta Mathematica",
        "Duke Mathematical Journal",
        "Journal of the American Mathematical Society",
        "Publications Mathématiques de l'IHÉS",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明，不手打 \\mathrm 拼算子",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "所有符号在首次出现处定义；集合/空间/映射记法全文一致",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("LaTeX", "Mathematica", "SageMath", "MATLAB", "Python (NumPy/SciPy)"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar", "CNKI"),
)
