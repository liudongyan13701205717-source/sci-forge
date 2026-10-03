"""音乐学学科论文支持：分析/历史/民族音乐体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="musicology",
    aliases=("musicology", "音乐学", "音乐研究", "民族音乐学"),
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
        "musical_analysis": (
            "abstract",
            "introduction",
            "repertoire（曲目）",
            "analytical method（分析方法）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
        "ethnographic_study": (
            "abstract",
            "introduction",
            "fieldwork（田野）",
            "data（数据）",
            "analysis（分析）",
            "findings（发现）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Journal of the American Musicological Society 遵循 Chicago 规范）",
    reporting_standards={
        "musical": "音乐分析遵循乐谱分析报告规范",
        "ethnography": "民族志研究遵循民族志报告规范",
        "historical": "历史研究遵循史料来源报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "乐谱版本须注明",
        "音高用音名标注",
        "录音与田野须交代",
        "引文给出页码",
        "分析框架须明确",
    ),
    key_venues=(
        "Journal of the American Musicological Society",
        "Music & Letters",
        "Journal of Musicology",
        "Early Music",
        "Music Theory Spectrum",
        "Ethnomusicology",
    ),
    units_and_formulas_notes=(
        "音高用音名（C4 等）标注",
        "速度用 BPM",
        "时长用 分:秒",
        "引文给出页码",
        "时间用统一纪年格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品"),
    tools=(
        "MuseScore 乐谱分析",
        "Sonic Visualiser 声学分析",
        "乐谱数据库检索工具",
        "EndNote 文献管理",
    ),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "DOAJ", "CNKI"),
)