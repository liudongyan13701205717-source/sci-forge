"""信息论学科论文支持：信道编码/率失真体裁、IEEE 引用样式与信息论记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_theory",
    aliases=("information theory", "信息论", "香农", "编码理论", "Shannon",
             "coding theory", "率失真"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与贡献）",
            "problem formulation（信道/信源模型与记号）",
            "main results（容量/率失真定理等）",
            "proofs（证明，长证明可移附录）",
            "examples and applications（示例与应用）",
            "conclusions",
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
    citation_style="IEEE 样式（编号引用，如 [1]）",
    reporting_standards={
        "proof": "容量/率失真等定理必须给出完整证明（含可达性与逆定理），或明确引用出处",
        "attribution": "定理归属必须准确：首次证明者与其发表出处须在陈述或证明处引用",
        "model_completeness": "信道/信源模型须完整定义：字母表、转移概率、失真度量与约束",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "信息量记法全文一致：熵 H(X)、互信息 I(X;Y)、条件熵 H(X|Y)",
        "随机变量用大写字母，取值用小写；分布用 p_X 或 P_X 统一书写",
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "可达性证明给出编码/解码方案与错误概率上界，逆定理给出下界",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "IEEE Transactions on Information Theory",
        "IEEE Transactions on Communications",
        "Entropy",
        "Problems of Information Transmission",
        "IEEE Journal on Selected Areas in Information Theory",
        "Foundations and Trends in Communications and Information Theory",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{KL} \\operatorname{supp}），不手打 \\mathrm 拼算子",
        "对数底数（2/e/10）在首次出现处声明，熵单位（bit/nat）随之确定",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Python (NumPy)", "MATLAB", "R"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)