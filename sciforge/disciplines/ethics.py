"""伦理学学科论文支持：规范/应用/元伦理体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ethics",
    aliases=("ethics", "伦理学", "道德哲学", "应用伦理学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "argument（论证）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "theoretical_paper": (
            "abstract",
            "introduction",
            "conceptual framework（概念框架）",
            "argument（论证）",
            "implications（启示）",
            "references",
        ),
        "case_analysis": (
            "abstract",
            "introduction",
            "case（案例）",
            "ethical analysis（伦理分析）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Ethics 遵循 Chicago 规范）",
    reporting_standards={
        "theoretical": "理论论证遵循哲学论证报告规范",
        "case": "案例分析遵循伦理案例报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "核心概念须定义",
        "论证结构须清晰",
        "对立观点须回应",
        "引文给出页码",
        "应用语境须交代",
    ),
    key_venues=(
        "Ethics",
        "The Journal of Ethics",
        "Journal of Medical Ethics",
        "Ethics & International Affairs",
        "Utilitas",
        "Journal of Moral Philosophy",
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "版本与版次须注明",
        "译文给出原文页码",
        "时间用统一纪年格式",
        "术语用原文并注译",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=(
        "LaTeX 哲学排版",
        "LogiCola 逻辑论证工具",
        "Zotero 文献管理",
        "Argdown 论证图谱",
    ),
    category="哲学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)