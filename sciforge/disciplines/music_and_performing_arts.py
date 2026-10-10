"""音乐与表演艺术学科论文支持：表演艺术研究与教学法体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="music_and_performing_arts",
    aliases=(
        "music_and_performing_arts", "音乐与表演艺术", "Music and performing arts",
        "表演艺术", "Performing arts", "music and theatre",
        "音乐与戏剧", "sound art",
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
            "case description（作品/项目）",
            "analysis（创作与表演分析）",
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
    citation_style="APA 7（结合 Chicago 用于乐谱/文本引用）",
    reporting_standards={
        "k1": "表演研究须报告作品版本、演出时间与排练时长",
        "k2": "受众研究须报告样本量、抽样方法与信效度",
        "k3": "创作研究须报告创作过程与评审标准",
    },
    conventions=(
        "作品引用须给出作曲者、作品编号与版本",
        "乐谱示例须给出出版信息与页码",
        "引用剧本/歌词须遵循标准版权规范",
        "术语首次出现须给出缩写与全称",
        "视频/音频引用须给出 URL 与访问时间",
    ),
    key_venues=(
        "New Theatre Quarterly",
        "Theatre Research International",
        "Journal of Dramatic Theory and Criticism",
        "BRIDGE: British Research in Performing Arts",
        "《戏剧》",
    ),
    units_and_formulas_notes=(
        "演出时长用分钟；录制时长用 mm:ss",
        "观众数量给出场次与总人次",
        "排练时长给出累计时长",
        "引用剧本须给出版权与版本信息",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("MuseScore", "Sibelius", "Dorico", "Notation Composer", "Logic Pro", "Pro Tools", "Reaper", "Adobe Audition", "Adobe Premiere Pro", "DaVinci Resolve", "ProPresenter", "NVivo", "ATLAS.ti", "MAXQDA", "EndNote", "Zotero", "Microsoft Excel", "Python", "RStudio", "Google Docs"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
