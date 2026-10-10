"""指挥（音乐）学科论文支持：指挥研究/排练方法论/作品诠释体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="conducting",
    aliases=(
        "conducting", "指挥", "音乐指挥", "orchestral conducting",
        "orchestra conducting", "合唱指挥", "choral conducting",
        "band conducting", "管弦乐指挥", "rehearsal pedagogy",
        "排练方法论",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work",
            "methodology（研究设计与数据收集）",
            "results（分析与发现）",
            "discussion（解释与启示）",
            "conclusion",
            "references",
        ),
        "pedagogical": (
            "abstract",
            "introduction",
            "literature review",
            "method（教学法/课程设计）",
            "implementation（实施过程）",
            "results（学生反馈/评估）",
            "conclusion",
            "references",
        ),
        "performance": (
            "abstract",
            "composer and work（作品背景）",
            "performance notes（诠释思路）",
            "rehearsal approach（排练方法）",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7（音乐研究通用）",
    reporting_standards={
        "empirical": "经验研究须报告样本量、抽样方法与信效度",
        "pedagogical": "教学法研究须报告课程设计、实施周期与学生评估",
        "performance": "表演诠释须明确版本来源（Urtext/校订本）与诠释立场",
    },
    conventions=(
        "作品引用须给出作曲者全名、作品编号与版本（如 Urtext、校订本编号）",
        "乐谱术语（tacet、coda、Da Capo）须使用标准德/意大利/法文写法",
        "排练时长、节拍器速度（bpm）与力度层级须用统一记法",
        "术语表首次出现即给出缩写与全称（如 CACM、GRM）",
    ),
    key_venues=(
        "Journal of Orchestra Research",
        "Conducting Review",
        "Conducting Quarterly",
        "Journal of Band Research",
        "Journal of Choral Literature",
        "BRIDGE: British Research in Performing Arts",
        "Music Education Review",
    ),
    units_and_formulas_notes=(
        "节拍器速度用 bpm（beats per minute）",
        "时长用分钟/秒；排练时段须标注星期几",
        "乐谱示例须给出出版信息（出版社、年、页码）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("MuseScore", "Dorico", "Finale", "Sibelius", "Notation Composer", "Pianoteq", "Sforzando", "Logic Pro", "Pro Tools", "Reaper", "Audition (Adobe)", "Sibelius Playback", "MuseDirect", "VexFlow", "LilyPond", "BPM (Beatbox Piano Master)", "Melodyne", "Audacity", "Ableton Live", "Notator"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "RILM"),
)
