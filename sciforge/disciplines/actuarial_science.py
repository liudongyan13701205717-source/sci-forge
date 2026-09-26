"""精算学学科论文支持：保险数学/风险管理体裁、作者-年份引用样式与精算记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="actuarial_science",
    aliases=("actuarial science", "精算", "精算学", "保险数学", "actuarial",
             "风险管理", "寿险精算"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与贡献）",
            "model formulation（保险/风险模型与假设）",
            "main results（定价/准备金/风险度量定理）",
            "proofs（证明，长证明可移附录）",
            "numerical illustrations（数值示例与敏感性分析）",
            "conclusions",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background and motivation",
            "main exposition（以例子驱动的建模-定价链）",
            "exercises（练习，可选）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview（问题源流与关键节点）",
            "main developments（按主题组织的模型-方法综述）",
            "open problems（未解决问题清单）",
            "references",
        ),
    },
    citation_style="作者-年份样式（如 Smith (2004)）",
    reporting_standards={
        "model_assumptions": "死亡率/退保率/利率等假设须显式列出并注明数据来源",
        "proof": "定价/准备金/风险度量定理必须给出完整推导，或明确引用出处",
        "regulatory_context": "涉及监管要求（偿付能力、IFRS 17 等）时须注明适用框架",
        "computational_evidence": "数值示例须说明软件、参数与敏感性分析",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "精算记法全文一致：x 岁生命用 l_x、d_x，年金用 a_x，寿险用 A_x",
        "利率假设用 i 或 v = 1/(1+i)，注明名义/实际与计息频率",
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "风险度量（VaR/TVaR）在首次出现处定义并注明置信水平",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "ASTIN Bulletin",
        "Insurance: Mathematics and Economics",
        "North American Actuarial Journal",
        "Scandinavian Actuarial Journal",
        "Journal of Risk and Insurance",
        "European Actuarial Journal",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{VaR} \\operatorname{TVaR}），不手打 \\mathrm 拼算子",
        "精算符号用标准上标/下标（如 \\ddot{a}_x^{(m)}），首次出现处解释含义",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("R", "Python", "Excel", "LaTeX"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "CNKI"),
)