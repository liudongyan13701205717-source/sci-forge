"""音乐学学科论文支持：音乐分析/历史/民族音乐体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="musicology",
    aliases=(
        "musicology", "音乐学", "Music studies", "民族音乐学",
        "ethnomusicology", "音乐分析", "music analysis",
        "music history", "音乐史",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "methodology（文献/分析/田野方法）",
            "results（发现）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（曲目/族群背景）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目）",
    reporting_standards={
        "k1": "音乐分析须遵循乐谱分析报告规范",
        "k2": "民族志研究须遵循民族志报告规范",
        "k3": "历史研究须遵循史料来源报告规范",
    },
    conventions=(
        "乐谱版本须注明（Urtext、校订本）",
        "音高用音名（C4 等）标注",
        "录音与田野须交代（地点、日期、许可）",
        "引文给出页码",
        "分析框架须明确（如 Schenker、Rhythmics）",
    ),
    key_venues=(
        "Journal of the American Musicological Society",
        "Music & Letters",
        "Journal of Musicology",
        "Early Music",
        "Music Theory Spectrum",
    ),
    units_and_formulas_notes=(
        "音高用音名（C4 等）标注",
        "速度用 BPM；力度用 pp/ff 记号",
        "时长用 分:秒",
        "引文给出页码",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("MuseScore", "Sibelius", "Dorico", "Finale", "LilyPond", "Notation Composer", "Sonic Visualiser", "Spectral Analysis Suite", "Adobe Audition", "Pro Tools", "Audacity", "Pianoteq", "SuperCollider", "Openmusic", "OpenMusic / OpenMSX", "Open Song Search", "EndNote", "Zotero", "Python", "RStudio"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "DOAJ", "CNKI"),
)
