"""博弈论学科论文支持：非合作/合作博弈体裁、作者-年份引用样式与博弈记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="game_theory",
    aliases=("game theory", "博弈论", "博弈", "机制设计", "mechanism design",
             "均衡", "equilibrium"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与贡献）",
            "model（博弈模型：玩家、策略、支付）",
            "main results（均衡存在性/刻画定理）",
            "proofs（证明，长证明可移附录）",
            "discussion（经济/计算含义与扩展）",
            "concluding remarks",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background and motivation",
            "main exposition（以例子驱动的模型-均衡链）",
            "exercises（练习，可选）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview（问题源流与关键节点）",
            "main developments（按主题组织的模型-结果综述）",
            "open problems（未解决问题清单）",
            "references",
        ),
    },
    citation_style="作者-年份样式（如 Smith (2004)）",
    reporting_standards={
        "model_completeness": "博弈模型须完整定义玩家集合、策略空间、支付函数与信息结构",
        "equilibrium_justification": "均衡概念（Nash/子博弈完美/贝叶斯等）须定义并说明选择理由",
        "proof": "均衡存在性与刻画定理必须给出完整证明，或明确引用出处",
        "attribution": "均衡概念与定理的归属必须准确：首次提出者与其发表出处须引用",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "博弈记法全文一致：玩家 i \\in N，策略 s_i \\in S_i，支付 u_i(s)",
        "均衡概念在首次出现处定义（Nash/SPE/PBE/CE 等），并注明出处",
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "机制设计结果给出激励相容/个体理性约束的显式形式",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "Games and Economic Behavior",
        "International Journal of Game Theory",
        "Journal of Economic Theory",
        "Mathematics of Operations Research",
        "Theoretical Economics",
        "Games",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{BR} \\operatorname{NE}），不手打 \\mathrm 拼算子",
        "策略剖面用 s = (s_1, \\dots, s_n)，对手剖面用 s_{-i} 统一书写",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("Python", "R", "LaTeX"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)