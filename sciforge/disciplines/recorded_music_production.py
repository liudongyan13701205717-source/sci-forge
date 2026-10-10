"""录音音乐制作学科论文支持：录音/混音/母带/电子音乐体裁、APA 引用样式与音频参数记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="recorded_music_production",
    aliases=(
        "recorded_music_production",
        "录音音乐制作",
        "音乐制作",
        "录音制作",
        "Recorded Music Production",
        "Music Production",
        "录音工程",
        "混音",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（制作方法与评估）", "results（音质与感知结果）", "discussion（技术与美学意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（制作过程分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；音乐技术研究与艺术学常用 APA）",
    reporting_standards={
        "k1": "音频质量评估须遵循 ITU-R BS.1770 规范",
        "k2": "感知实验须遵循 ISO 532 标准",
        "k3": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "音频参数（采样率、位深、延迟）须报告",
        "DAW 软件与插件版本须标注",
        "混音参数（EQ、压缩、混响）须给出",
        "感知评估须报告评分者数量与评分分布",
        "曲目与版权信息须注明",
    ),
    key_venues=(
        "Journal of New Music Research",
        "Music Perception",
        "Leonardo Music Journal",
        "Journal of the Audio Engineering Society",
        "Journal of Sound and Vibration",
    ),
    units_and_formulas_notes=(
        "音频参数用 Hz 与 dB",
        "延迟用 ms",
        "动态范围用 dB",
        "统计量给出 M/SD 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Pro Tools", "Logic Pro", "Ableton Live", "FL Studio", "Cubase", "Studio One", "Reaper", "GarageBand", "Adobe Audition", "Nuendo", "Bitwig", "Reason", "Samplitude", "WaveLab", "Sonar", "Digital Performer", "Tracktion T7", "iZotope RX", "FabFilter", "Waves Plugins"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
