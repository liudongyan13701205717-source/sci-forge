"""程序设计语言学科论文支持：语言设计/类型系统体裁、ACM 引用样式与 PL 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="programming_languages",
    aliases=(
        "programming_languages",
        "程序设计语言",
        "编程语言",
        "Programming languages",
        "PL",
        "语言设计",
        "语言理论",
        "编译原理",
        "PLDI",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（形式化方法）",
            "results（实现与评估）",
            "discussion（语义与局限）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（语言/案例描述）",
            "analysis（设计与语义分析）",
            "results（性能与正确性结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（类型与语义综述）",
            "evidence synthesis（证据综合）",
            "future directions",
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
        "语法须给出 BNF/EBNF 或归纳定义，且形式化定义与实现一致",
        "类型规则须以推导规则呈现，soundness/completeness 须证明",
        "操作语义与指称语义取其一并注明选择理由",
        "实现代码、工具链与第三方依赖版本须公开",
        "评估须与既有语言/工具在相同基准下对比",
    ),
    key_venues=(
        "ACM SIGPLAN Notices",
        "POPL",
        "PLDI",
        "ICFP",
        "OOPSLA",
        "PACMPL",
        "Journal of Functional Programming",
    ),
    units_and_formulas_notes=(
        "类型规则用推导式书写，语义用操作语义或指称语义",
        "公式用 amsmath；规则与定理须编号",
        "复杂度用 O(·) 记法并注明摊销口径",
        "运行时性能以微秒/毫秒计并标注硬件与编译器版本",
        "代码行数/基准吞吐量须标注基准名称与版本",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("Coq", "Lean 4", "Isabelle/HOL", "MLIR", "LLVM", "GCC", "GHC", "OCaml", "TypeScript", "MyPy", "Z3", "Roslyn", "Dart", "Racket", "Rustc", "SBT", "Bazel", "Valgrind", "Docker", "GitHub Actions"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)
