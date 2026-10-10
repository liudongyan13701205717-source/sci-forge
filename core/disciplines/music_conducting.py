"""音乐指挥学科论文支持：管弦乐/合唱指挥研究与教学法体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="music_conducting",
    aliases=(
        "music_conducting", "音乐指挥", "Music conducting",
        "orchestra conducting", "管弦乐指挥", "choral conducting",
        "合唱指挥", "band conducting",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（研究设计）",
            "results（发现）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（曲目/乐团背景）",
            "analysis（排练与诠释分析）",
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
    citation_style="APA 7",
    reporting_standards={
        "k1": "排练方法研究须报告排练时长与训练环节",
        "k2": "诠释研究须报告作品版本与表演立场",
        "k3": "教学法研究须报告课程设计与学生评估",
    },
    conventions=(
        "乐谱术语（tacet、coda、Da Capo）须使用德/意/法标准写法",
        "作品引用须给出作曲者全名、作品编号与版本",
        "排练时长与速度（bpm）须用统一记法",
        "术语首次出现须给出缩写与全称（如 CACM、GRM）",
        "引用指挥谱例须给出出版信息与页码",
    ),
    key_venues=(
        "Journal of Orchestra Research",
        "Conducting Review",
        "Conducting Quarterly",
        "Journal of Band Research",
        "Journal of Choral Literature",
    ),
    units_and_formulas_notes=(
        "速度用 bpm；练习节奏用 0.5x、1.5x 等",
        "排练时长给出累计时长与星期几",
        "乐谱引用给出乐章号与页码",
        "引用曲目须给出版权信息",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("MuseScore", "Sibelius", "Dorico", "Finale", "Notation Composer", "LilyPond", "Pianoteq", "Sforzando", "Logic Pro", "Pro Tools", "Reaper", "Audacity", "Melodyne", "MuseDirect", "VexFlow", "BPM (Beatbox Piano Master)", "Sibelius Playback", "EndNote", "Microsoft Excel", "Adobe Audition"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "RILM"),
)
