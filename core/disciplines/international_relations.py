"""国际关系学科论文支持：外交/安全/国际政治经济体裁、APSA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="international_relations",
    aliases=("international_relations", "国际关系", "国际政治", "外交学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "theory（理论框架）",
            "hypotheses（假设）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case selection（案例选择）",
            "analysis（分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy context（政策背景）",
            "analysis（分析）",
            "recommendations（建议）",
            "references",
        ),
    },
    citation_style="APSA 样式（作者-年份；International Organization 遵循 APSA 规范）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "comparative": "比较研究遵循比较研究报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "理论框架与假设须明确",
        "案例选择标准须说明",
        "数据来源须注明",
        "概念操作化须定义",
        "外部效度与局限须讨论",
    ),
    key_venues=(
        "International Organization",
        "International Security",
        "World Politics",
        "Journal of Conflict Resolution",
        "American Political Science Review",
        "International Studies Quarterly",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量用 Cohen's d 或 η²",
        "回归系数给出标准误与显著性",
        "样本量须报告",
        "货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=("NVivo（质性编码）", "EndNote（文献管理）", "Stata（计量分析）", "R（统计与可视化）",
           "案例比较方法工具（QCA）"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)