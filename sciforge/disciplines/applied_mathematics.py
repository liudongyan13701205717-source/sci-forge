"""应用数学学科论文支持：建模/渐近分析体裁、AMS 引用样式与应用记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="applied_mathematics",
    aliases=("applied mathematics", "应用数学", "应用分析", "数学建模",
             "applied math", "渐近分析"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与主结果陈述）",
            "model formulation（模型建立与无量纲化）",
            "mathematical analysis（适定性、渐近与主要结果）",
            "numerical experiments（数值实验与验证）",
            "discussion（物理解释与局限）",
            "concluding remarks",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background and motivation",
            "main exposition（以例子驱动的建模-分析链）",
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
    citation_style="AMS 样式（作者-字母编号，amsrefs/BibTeX，如 [Smi04]）",
    reporting_standards={
        "model_validation": "模型须给出推导过程、无量纲化与适用域；数值结果须与解析/实验对照验证",
        "proof": "分析性定理必须给出完整证明，或明确引用出处",
        "attribution": "模型与方法的归属必须准确：首次提出者与其发表出处须引用",
        "reproducibility": "数值实验须说明软件、参数、网格与可复现性",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "定理环境按 theorem/lemma/proposition/corollary 分级编号（连号或分节）",
        "无量纲化在模型建立后立即进行，并说明各无量纲数的物理含义",
        "物理量符号全文一致：时间 t、空间 x、参数在首次出现处定义",
        "证明以 QED 方块（\\qedsymbol）结束；嵌套证明标 (Proof of Lemma 2.3)",
        "数值实验给出收敛阶、误差与参数表，并与解析结果对照",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "SIAM Journal on Applied Mathematics",
        "SIAM Review",
        "Journal of Mathematical Biology",
        "Studies in Applied Mathematics",
        "European Journal of Applied Mathematics",
        "Applied Mathematics Letters",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{div} \\operatorname{curl}），不手打 \\mathrm 拼算子",
        "无量纲数（Reynolds、Péclet 等）用标准符号并注明定义式",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("MATLAB", "Mathematica", "Python"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)