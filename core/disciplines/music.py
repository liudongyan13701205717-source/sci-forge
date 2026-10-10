"""音乐学科论文支持：音乐创作/表演/演奏实践研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="music",
    aliases=(
        "music", "音乐", "Music studies", "music education",
        "音乐教育", "music performance", "音乐表演",
        "music theory", "音乐理论",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（研究方法）",
            "results（发现）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景）",
            "analysis（分析与讨论）",
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
    citation_style="Chicago 样式（Journal of Music Theory 采用 Chicago）",
    reporting_standards={
        "k1": "音乐教育研究须报告样本量、抽样方法与信效度",
        "k2": "表演研究须报告版本、录音时间与诠释立场",
        "k3": "听感研究须报告样本、任务设计与评分量表",
    },
    conventions=(
        "乐谱版本须注明（Urtext、校订本）",
        "术语首次出现须给出缩写与全称（如 CACM）",
        "引用音乐须给出作者、作品编号与版本",
        "演奏录像须给出录制信息（时间、地点、录音师）",
        "音高术语遵循国际通用记法",
    ),
    key_venues=(
        "Journal of Music Theory",
        "Journal of the American Musicological Society",
        "Music Education Review",
        "Journal of Music Pedagogy",
        "《中央音乐学院学报》",
    ),
    units_and_formulas_notes=(
        "音高用音名标注（C4 等）",
        "速度用 bpm；力度用 pp/ff 记号",
        "时长用 mm:ss；音高距离用半音",
        "引用乐谱须给出页码与乐章号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("MuseScore", "Sibelius", "Dorico", "Finale", "Notation Composer", "LilyPond", "Pianoteq", "Sforzando", "Pro Tools", "Logic Pro", "Reaper", "Audacity", "Melodyne", "Sonic Visualiser", "SuperCollider", "Ableton Live", "EndNote", "Zotero", "Adobe Audition", "RStudio"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "RILM"),
)
