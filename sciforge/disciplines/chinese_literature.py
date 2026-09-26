"""中国文学学科论文支持：文本/批评/比较体裁、MLA 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chinese_literature",
    aliases=("chinese_literature", "中国文学", "中国现当代文学", "中国古代文学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "textual analysis（文本分析）",
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
            "corpus（比较对象）",
            "framework（框架）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="MLA 样式（作者-页码；文学评论类期刊遵循 MLA 规范）",
    reporting_standards={
        "textual": "文本分析遵循文本分析报告规范",
        "archival": "档案研究遵循史料考证报告规范",
        "comparative": "比较研究遵循比较研究报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "版本与校勘须注明",
        "引文给出页码",
        "作品标题用书名号/斜体",
        "理论框架须明确",
        "文学史脉络须交代",
    ),
    key_venues=(
        "文学评论",
        "中国现代文学研究丛刊",
        "文学遗产",
        "Journal of Chinese Literature and Culture",
        "Chinese Literature: Essays, Articles, Reviews",
        "文艺研究",
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "古籍用卷/篇/页标注",
        "版本与版次须注明",
        "译文给出原文页码",
        "时间用统一纪年格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品"),
    tools=(
        "语料库检索工具",
        "EndNote 文献管理",
        "LaTeX 排版",
    ),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)