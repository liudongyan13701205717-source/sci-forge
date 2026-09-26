"""历史学学科论文支持：史学/档案/比较体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history",
    aliases=("history", "历史学", "史学", "历史研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "historiography（史学史回顾）",
            "sources（史料）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
        "archival_study": (
            "abstract",
            "introduction",
            "archival sources（档案史料）",
            "method（方法）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
        "review_essay": (
            "abstract",
            "introduction",
            "survey（综述）",
            "assessment（评析）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；American Historical Review 遵循 Chicago 规范）",
    reporting_standards={
        "archival": "档案研究遵循史料考证报告规范",
        "historical": "历史研究遵循史料来源报告规范",
        "comparative": "比较研究遵循比较研究报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "史料来源与版本须注明",
        "一手与二手史料须区分",
        "时间与纪年须统一",
        "史学史脉络须交代",
        "解释框架须明确",
    ),
    key_venues=(
        "American Historical Review",
        "Past & Present",
        "Journal of Modern History",
        "The Historical Journal",
        "History Workshop Journal",
        "Journal of Asian Studies",
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "古籍用卷/篇/页标注",
        "版本与版次须注明",
        "时间用统一纪年格式",
        "货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=(
        "EndNote 文献管理",
        "数字人文分析平台（Python/R）",
        "史料数据库检索工具",
        "LaTeX 排版",
    ),
    category="历史学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)