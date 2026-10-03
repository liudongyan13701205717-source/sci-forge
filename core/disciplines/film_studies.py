"""电影学学科论文支持：影片/作者/产业体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="film_studies",
    aliases=("film_studies", "电影学", "电影研究", "影视研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "analysis（分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "film_analysis": (
            "abstract",
            "introduction",
            "film（影片）",
            "analytical framework（分析框架）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
        "industry_study": (
            "abstract",
            "introduction",
            "industry context（产业背景）",
            "data（数据）",
            "analysis（分析）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Screen 遵循 Chicago 规范）",
    reporting_standards={
        "film": "影片分析遵循影片分析报告规范",
        "industry": "产业研究遵循产业数据报告规范",
        "historical": "历史研究遵循史料来源报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "影片信息（片名/导演/年份/版本）须完整",
        "帧与时间码须标注",
        "产业数据来源须注明",
        "引文给出页码",
        "分析框架须明确",
    ),
    key_venues=(
        "Screen",
        "Cinema Journal",
        "Film Quarterly",
        "Journal of Film and Video",
        "Historical Journal of Film, Radio and Television",
        "Film Criticism",
    ),
    units_and_formulas_notes=(
        "时间码用 时:分:秒:帧",
        "引文给出页码",
        "票房用统一币种并注明年份",
        "版本与版次须注明",
        "时间用统一纪年格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "艺术作品"),
    tools=(
        "FFmpeg 影像分析",
        "影像档案数据库检索工具",
    ),
    category="艺术学",
    databases=("DOAJ", "OpenAlex", "Crossref", "CNKI"),
)