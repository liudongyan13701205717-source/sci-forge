"""神学学科论文支持：系统/圣经/历史神学体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="theology",
    aliases=("theology", "神学", "系统神学", "圣经研究"),
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
        "exegetical_study": (
            "abstract",
            "introduction",
            "text（经文）",
            "exegesis（释经）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
        "historical_study": (
            "abstract",
            "introduction",
            "sources（史料）",
            "analysis（分析）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Journal of Theological Studies 遵循 Chicago 规范）",
    reporting_standards={
        "exegetical": "释经研究遵循经文考证报告规范",
        "historical": "历史研究遵循史料来源报告规范",
        "archival": "档案研究遵循史料考证报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "经文版本须注明",
        "原文与译文须对照",
        "教义脉络须交代",
        "引文给出标准编号",
        "解释框架须明确",
    ),
    key_venues=(
        "Journal of Theological Studies",
        "Theology Today",
        "Modern Theology",
        "International Journal of Systematic Theology",
        "Scottish Journal of Theology",
        "Harvard Theological Review",
    ),
    units_and_formulas_notes=(
        "引文给出标准编号（如章节）",
        "经文用卷/章/节标注",
        "版本与版次须注明",
        "时间用统一纪年格式",
        "译文给出原文页码",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=(
        "经文数据库检索工具",
        "EndNote 文献管理",
        "LaTeX 排版",
    ),
    category="哲学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)