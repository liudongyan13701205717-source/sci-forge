"""软件测试学科论文支持：测试方法/质量保障体裁、ACM 引用样式与测试记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_testing",
    aliases=("software_testing", "软件测试", "测试", "软件质量保障"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "method（方法）",
            "experiments（实验）",
            "conclusion（结论）",
            "references",
        ),
        "empirical_study": (
            "abstract",
            "introduction",
            "research questions（研究问题）",
            "study design（研究设计）",
            "results（结果）",
            "threats to validity（有效性威胁）",
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
    citation_style="ACM 样式（作者-年份；ICSE/ISSTA 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验遵循软件工程实证规范",
        "empirical": "实证研究遵循软件工程实证报告规范",
        "benchmark": "基准测试遵循标准基准报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性遵循软件工程可复现性清单",
    },
    conventions=(
        "被测系统与版本须报告",
        "测试套件与覆盖率须说明",
        "缺陷集与 oracle 须明确",
        "统计检验与效应量须报告",
        "有效性威胁须讨论",
    ),
    key_venues=(
        "ICSE",
        "ISSTA",
        "FSE",
        "IEEE Transactions on Software Engineering",
        "ACM Transactions on Software Engineering and Methodology",
        "Empirical Software Engineering",
    ),
    units_and_formulas_notes=(
        "覆盖率用 %；时间用 s/min；缺陷数用 n",
        "公式用 amsmath；算法与统计模型须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("JUnit", "pytest", "SonarQube", "Maven"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)