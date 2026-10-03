"""古典学学科论文支持：文献/语文学/考古体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="classics",
    aliases=("classics", "古典学", "古典语文学", "古希腊罗马研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "sources（文献）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
        "philological_study": (
            "abstract",
            "introduction",
            "textual tradition（文本传统）",
            "manuscripts（抄本）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
        "archaeological_study": (
            "abstract",
            "introduction",
            "site（遗址）",
            "finds（出土物）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Classical Quarterly 遵循 Chicago 规范）",
    reporting_standards={
        "philological": "语文学研究遵循文本考证报告规范",
        "archaeological": "考古研究遵循考古发掘报告规范",
        "archival": "档案研究遵循史料考证报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "原文与译文须对照",
        "抄本与版本谱系须说明",
        "引文给出标准编号",
        "纪年与历法须统一",
        "考古地层须交代",
    ),
    key_venues=(
        "The Classical Quarterly",
        "Classical Philology",
        "Journal of Hellenic Studies",
        "Journal of Roman Studies",
        "American Journal of Philology",
        "Transactions of the American Philological Association",
    ),
    units_and_formulas_notes=(
        "引文给出标准编号（如行号）",
        "古籍用卷/篇/行标注",
        "版本与版次须注明",
        "时间用统一纪年格式",
        "度量用统一单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "译文"),
    tools=(
        "古文献数据库检索工具",
        "语料库检索工具",
        "EndNote 文献管理",
        "LaTeX 排版",
    ),
    category="历史学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)