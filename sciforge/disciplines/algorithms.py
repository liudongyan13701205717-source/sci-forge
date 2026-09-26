"""算法学科论文支持：算法设计与分析体裁、ACM 引用样式与算法记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="algorithms",
    aliases=("algorithms", "算法", "算法设计与分析", "计算复杂性"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "algorithm（算法）",
            "analysis（分析）",
            "experiments（实验）",
            "references",
        ),
        "theory_paper": (
            "abstract",
            "introduction",
            "preliminaries（预备知识）",
            "main results（主要结果）",
            "proofs（证明）",
            "discussion（讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；STOC/FOCS 遵循其规范）",
    reporting_standards={
        "theoretical": "理论结果遵循定理证明报告规范",
        "experimental": "实验遵循算法实证规范",
        "benchmark": "基准测试遵循标准基准报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性遵循可复现性清单",
    },
    conventions=(
        "问题定义与输入规模须明确",
        "复杂度分析（时间/空间）须完整",
        "近似比/竞争比须给出",
        "实验须与理论界对比",
        "随机化算法须说明概率保证",
    ),
    key_venues=(
        "STOC",
        "FOCS",
        "SODA",
        "Journal of the ACM",
        "SIAM Journal on Computing",
        "Algorithmica",
    ),
    units_and_formulas_notes=(
        "复杂度用 O(·)/Ω(·)/Θ(·) 记法",
        "公式用 amsmath；定理与引理须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "证明用引理-定理结构",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Python", "C", "LaTeX", "GAP"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)