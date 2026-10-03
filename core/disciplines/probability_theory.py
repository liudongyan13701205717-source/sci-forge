"""概率论学科论文支持：测度论/极限定理体裁、AMS 引用样式与概率记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="probability_theory",
    aliases=("probability", "概率论", "概率", "随机", "probability theory",
             "随机过程", "极限定理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与主定理陈述）",
            "preliminaries（概率空间、记号与基本引理）",
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
        "integrability_conditions": "矩条件、可积性与正则性假设须显式列出，并说明是否可放宽",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "概率记法全文一致：概率用 \\mathbb{P}，期望用 \\mathbb{E}，方差用 \\operatorname{Var}",
        "随机变量用大写字母，取值用小写；分布收敛用 \\xrightarrow{d}，依概率收敛用 \\xrightarrow{p}",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "收敛模式（a.s./依概率/分布/L^p）在首次出现处定义并全文一致",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "Annals of Probability",
        "Probability Theory and Related Fields",
        "Electronic Journal of Probability",
        "Annals of Applied Probability",
        "Stochastic Processes and their Applications",
        "Journal of Theoretical Probability",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{Cov} \\operatorname{Var}），不手打 \\mathrm 拼算子",
        "期望/概率的积分形式用 \\mathbb{E}[f(X)] = \\int f \\, d\\mu 统一书写",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("R", "Python", "MATLAB"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)