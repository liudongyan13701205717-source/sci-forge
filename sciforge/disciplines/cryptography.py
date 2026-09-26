"""密码学学科论文支持：安全证明/密码分析体裁、IACR 引用样式与密码记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cryptography",
    aliases=("cryptography", "密码学", "密码", "密码分析", "crypto",
             "安全协议", "security proofs"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与贡献）",
            "preliminaries（安全模型、假设与记号）",
            "construction（方案/协议构造）",
            "security analysis（安全证明/归约）",
            "efficiency analysis（效率与实现）",
            "conclusions",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background and motivation",
            "main exposition（以例子驱动的构造-证明链）",
            "exercises（练习，可选）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview（问题源流与关键节点）",
            "main developments（按主题组织的构造-攻击综述）",
            "open problems（未解决问题清单）",
            "references",
        ),
    },
    citation_style="IACR 样式（作者-年份，如 [Smi04] 或 (Smith 2004)，按会议惯例）",
    reporting_standards={
        "security_model": "安全模型（IND-CPA/IND-CCA/UC 等）须精确定义，包括敌手能力与优势",
        "reduction_proof": "安全归约须给出完整证明：敌手、模拟器、优势损失与运行时间",
        "assumption_statement": "所用困难性假设（DL/DDH/LWE 等）须显式陈述并注明参数",
        "attribution": "方案与攻击的归属必须准确：首次提出者与其发表出处须引用",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "安全参数用 \\lambda，敌手用 \\mathcal{A}，模拟器用 \\mathcal{S}，优势用 \\operatorname{Adv}",
        "安全游戏/实验用编号步骤描述，归约图用 tikz 绘制",
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "效率分析报告密钥/密文尺寸、计算开销与实现基准",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "Journal of Cryptology",
        "CRYPTO / EUROCRYPT（IACR 会议论文集）",
        "Designs, Codes and Cryptography",
        "IEEE Transactions on Information Theory",
        "IACR Transactions on Symmetric Cryptology",
        "IACR Communications in Cryptology",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{Adv} \\operatorname{Pr}），不手打 \\mathrm 拼算子",
        "概率与期望用 \\mathbb{P} 与 \\mathbb{E} 统一书写，注明概率空间",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Python", "SageMath", "OpenSSL (研究用)", "ProVerif", "C 密码库"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)