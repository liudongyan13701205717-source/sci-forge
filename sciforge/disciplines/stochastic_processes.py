"""随机过程学科论文支持：随机分析/鞅论体裁、AMS 引用样式与随机过程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stochastic_processes",
    aliases=("stochastic processes", "随机过程", "随机分析", "鞅", "布朗运动",
             "stochastic analysis", "martingale", "Brownian motion"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与主定理陈述）",
            "preliminaries（概率空间、过程记号与基本引理）",
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
        "过程记法全文一致：过程用 (X_t)_{t \\ge 0}，鞅用 (M_t, \\mathcal{F}_t)",
        "概率用 \\mathbb{P}，期望用 \\mathbb{E}，条件期望用 \\mathbb{E}[\\cdot | \\mathcal{F}_t]",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "随机积分/Itô 公式的使用须注明积分类型（Itô/Stratonovich）",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "Annals of Probability",
        "Stochastic Processes and their Applications",
        "Probability Theory and Related Fields",
        "Electronic Journal of Probability",
        "Annals of Applied Probability",
        "Journal of Theoretical Probability",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{Cov} \\operatorname{Var}），不手打 \\mathrm 拼算子",
        "随机微分方程用 dX_t = b(X_t)\\,dt + \\sigma(X_t)\\,dB_t 统一书写",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("R", "Python (NumPy, SciPy)", "MATLAB", "Julia"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)