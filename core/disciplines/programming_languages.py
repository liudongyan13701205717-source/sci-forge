"""程序设计语言学科论文支持：语言设计/类型系统体裁、ACM 引用样式与 PL 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="programming_languages",
    aliases=("programming_languages", "程序设计语言", "编程语言", "PL",
             "类型系统"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "formalization（形式化）",
            "implementation（实现）",
            "evaluation（评估）",
            "references",
        ),
        "language_design": (
            "abstract",
            "introduction",
            "design（语言设计）",
            "semantics（语义）",
            "type system（类型系统）",
            "implementation（实现）",
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
    citation_style="ACM 样式（作者-年份；POPL/PLDI 遵循 ACM 规范）",
    reporting_standards={
        "formal": "形式化研究遵循定理证明报告规范",
        "experimental": "实验遵循系统论文评估规范",
        "benchmark": "基准测试遵循标准基准报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性遵循可复现性清单",
    },
    conventions=(
        "语法与语义定义须完整",
        "类型规则须形式化（推导规则）",
        "实现与工具链须说明",
        "证明（soundness 等）须给出",
        "评估须与现有语言对比",
    ),
    key_venues=(
        "POPL",
        "PLDI",
        "ICFP",
        "OOPSLA",
        "ACM Transactions on Programming Languages and Systems",
        "Journal of Functional Programming",
    ),
    units_and_formulas_notes=(
        "类型规则用推导式；语义用操作语义/指称语义",
        "公式用 amsmath；规则与定理须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "证明用引理-定理结构",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("LLVM", "GCC", "Coq", "Python", "Rust"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)