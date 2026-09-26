"""中国哲学学科论文支持：经学/诸子/比较体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chinese_philosophy",
    aliases=("chinese_philosophy", "中国哲学", "中国思想史", "国学"),
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
        "textual_analysis": (
            "abstract",
            "introduction",
            "text（文本）",
            "analysis（分析）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
        "comparative_study": (
            "abstract",
            "introduction",
            "traditions（比较对象）",
            "framework（框架）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Philosophy East and West 遵循 Chicago 规范）",
    reporting_standards={
        "textual": "文本分析遵循文本分析报告规范",
        "comparative": "比较研究遵循比较研究报告规范",
        "historical": "历史研究遵循史料来源报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "版本与校勘须注明",
        "引文给出页码",
        "古籍用卷/篇/页标注",
        "术语用原文并注译",
        "思想史脉络须交代",
    ),
    key_venues=(
        "Philosophy East and West",
        "Journal of Chinese Philosophy",
        "Dao: A Journal of Comparative Philosophy",
        "Asian Philosophy",
        "Frontiers of Philosophy in China",
        "哲学研究",
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "古籍用卷/篇/页标注",
        "版本与版次须注明",
        "译文给出原文页码",
        "时间用统一纪年格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "译文"),
    tools=(
        "中国哲学书电子化计划（CTP）古文献检索",
        "国学大师古籍全文检索",
        "LaTeX 古籍注释排版",
        "Zotero 文献管理",
    ),
    category="哲学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)