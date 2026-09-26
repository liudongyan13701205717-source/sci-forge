"""现象学学科论文支持：意识/意向性/生活世界体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="phenomenology",
    aliases=("phenomenology", "现象学", "现象学哲学", "意识哲学"),
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
        "textual_analysis": (
            "abstract",
            "introduction",
            "text（文本）",
            "analysis（分析）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Husserl Studies 遵循 Chicago 规范）",
    reporting_standards={
        "theoretical": "理论论证遵循哲学论证报告规范",
        "textual": "文本分析遵循文本分析报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "核心概念须定义",
        "论证结构须清晰",
        "文本版本须注明",
        "引文给出页码",
        "术语用原文并注译",
    ),
    key_venues=(
        "Husserl Studies",
        "Continental Philosophy Review",
        "Phenomenology and the Cognitive Sciences",
        "Journal of the British Society for Phenomenology",
        "Research in Phenomenology",
        "Philosophy Today",
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
        "现象学转录与编码工具",
        "NVivo 质性编码",
        "Zotero 文献管理",
    ),
    category="哲学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)