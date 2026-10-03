"""图论学科论文支持：结构图论/极值图论体裁、AMS 引用样式与图论记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="graph_theory",
    aliases=("graph theory", "图论", "图", "网络科学", "graph", "极值图论",
             "结构图论"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与主定理陈述）",
            "preliminaries（图模型、记号与基本引理）",
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
        "图记法全文一致：图 G = (V, E)，顶点数 n = |V|，边数 m = |E|",
        "度、邻域、子图/诱导子图记法统一：d(v)、N(v)、G[S]",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "渐近记号 O/o/\\ll 的定义须在首次出现处给出，并注明常数是否可计算",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "Journal of Graph Theory",
        "Journal of Combinatorial Theory, Series B",
        "Combinatorica",
        "SIAM Journal on Discrete Mathematics",
        "Discrete Mathematics",
        "Random Structures & Algorithms",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{ex} \\operatorname{tw} \\operatorname{col}），不手打 \\mathrm 拼算子",
        "图用 tikz 绘制，顶点标签与边标注清晰可读",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Python (NetworkX)", "R", "MATLAB", "SageMath"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)