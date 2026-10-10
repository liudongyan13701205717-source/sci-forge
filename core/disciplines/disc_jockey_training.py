"""DJ 培训学科论文支持：DJ 技术、音乐表演与电子音乐体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="disc_jockey_training",
    aliases=(
        "disc_jockey_training", "DJ 培训", "DJ 训练",
        "DJ training", "DJ 训练",
        "DJ performance", "DJ 表演",
        "DJing", "打碟",
        "electronic music production", "电子音乐制作",
        "DJ culture", "DJ 文化",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（DJ 技术问题与背景）",
            "methodology（技术测试、用户研究、案例研究）",
            "results（技术效果与用户体验）",
            "discussion（DJ 技术改进方向）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（DJ 案例描述）",
            "technical analysis（技术分析）",
            "outcome（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview（DJ 发展史）",
            "current techniques（当前技术）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "technical": "设备型号、版本与设置须明确",
        "performance": "现场表演参数须记录",
        "analysis": "音乐分析须注明 BPM 与调性",
    },
    conventions=(
        "设备名称须注明品牌与型号",
        "软件须注明版本与平台",
        "音乐分析须使用标准 BPM 与 Camelot 调性",
        "效果器参数须注明具体数值",
        "现场表现须注明时长、场景与受众",
    ),
    key_venues=(
        "Journal of New Media",
        "Media, Culture & Society",
        "Popular Music",
        "Sound Studies",
        "Leonardo Music Journal",
    ),
    units_and_formulas_notes=(
        "BPM 用 beats per minute 表示",
        "音量用 dB 表示",
        "调性用 Camelot 系统表示",
        "混音过渡时间用秒表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Rekordbox", "Serato DJ Pro", "Traktor Pro", "VirtualDJ", "djay Pro AI", "Ableton Live", "FL Studio", "Serato Studio", "Mixed In Key", "Pioneer CDJ-3000", "Pioneer DDJ-1000", "Allen & Heath Xone", "Native Instruments Maschine", "Ableton Push", "Waves Audio Plugins", "iZotope RX", "Mixxx", "SoundSwitch", "Lexicon PMX", "RANE Seventy-Two"),
    category="艺术学",
    databases=("OpenAlex", "Crossref"),
)
