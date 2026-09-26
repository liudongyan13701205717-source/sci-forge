"""运筹学学科论文支持：数学规划/排队论体裁、INFORMS 引用样式与 OR 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="operations_research",
    aliases=("operations research", "运筹学", "OR", "管理科学", "数学规划",
             "排队论", "mathematical programming"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与贡献）",
            "problem formulation（问题定义与数学模型）",
            "methodology（算法/方法设计与理论性质）",
            "computational experiments（计算实验与基准对比）",
            "case study（案例研究，可选）",
            "conclusions",
            "references",
        ),
        "expository": (
            "abstract",
            "introduction",
            "background and motivation",
            "main exposition（以例子驱动的建模-求解链）",
            "exercises（练习，可选）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview（问题源流与关键节点）",
            "main developments（按主题组织的模型-算法综述）",
            "open problems（未解决问题清单）",
            "references",
        ),
    },
    citation_style="INFORMS 样式（作者-年份，如 (Smith 2004)）",
    reporting_standards={
        "model_validation": "数学模型须给出假设、变量、参数与目标/约束的完整定义",
        "algorithm_reproducibility": "算法须给出伪代码、复杂度分析与可复现实现（代码/数据可用性）",
        "computational_evidence": "计算实验须说明硬件、求解器、实例生成方式与统计显著性",
        "attribution": "模型与算法的归属必须准确：首次提出者与其发表出处须引用",
        "novelty_statement": "须明确区分本工作的结果与已有文献结果的边界",
    },
    conventions=(
        "模型用标准形式书写：min/max 目标 + s.t. 约束，变量域（非负/整数/二元）显式声明",
        "复杂度分析用 O 记号并注明最坏情形/平均情形",
        "算法给出伪代码（编号步骤），并说明终止准则与复杂度",
        "计算实验报告实例规模、求解时间、gap 与最优性证明",
        "假设与未证明的断言必须显式标注（conjecture/question）",
    ),
    key_venues=(
        "Operations Research",
        "Management Science",
        "Mathematical Programming",
        "INFORMS Journal on Computing",
        "European Journal of Operational Research",
        "SIAM Journal on Optimization",
    ),
    units_and_formulas_notes=(
        "使用 amsmath/amsthm/amssymb：对齐用 align/gather，多行推导按 = 号对齐",
        "新增算子用 \\DeclareMathOperator 声明（如 \\operatorname{argmin} \\operatorname{s.t.}），不手打 \\mathrm 拼算子",
        "模型编号按 (P1)/(P2) 或 (1)/(2) 统一，约束引用用 (1a)/(1b)",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "括号尺寸用 \\bigl \\bigr \\Bigl 系列而非手动放大",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Python", "MATLAB", "Gurobi", "CPLEX"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)