"""Arts not further defined 学科论文支持：音乐、舞蹈、戏剧、影视与表演艺术等未另列表演与舞台艺术门类。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="arts_not_further_defined",
    aliases=(
        "arts_not_further_defined",
        "arts not further defined",
        "表演艺术",
        "performing arts",
        "音乐与舞蹈",
        "music and dance",
        "戏剧影视",
        "drama and film studies",
        "theatre studies",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "context and theoretical framing",
            "method / material and performance context",
            "analysis",
            "discussion",
            "conclusion",
            "references",
        ),
        "practice_based": (
            "abstract",
            "context and problem",
            "process (rehearsal, scoring, blocking)",
            "performance or composition description",
            "critical reflection",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical and stylistic overview",
            "current state of practice",
            "outlook",
            "references",
        ),
    },
    citation_style="Chicago 17th Notes-Bibliography（音乐/戏剧/影视通用）；引作品须给出作曲家/导演/编舞、标题、年份、演出方",
    reporting_standards={
        "work": "作品首次出现给出作者/创作者、标题、年份、演出/出版方与版本",
        "performance": "演出信息（日期、场地、演出方、导演/指挥/编舞、制作）须完整给出",
        "recording": "录音/影像须标注时长、发行方、ISRC 或视频 ID",
        "score": "乐谱/剧本引用须给出版本、页码与声部编号",
        "ethics": "现场记录、观众调查须报告伦理审查与知情同意",
    },
    conventions=(
        "乐谱用标准五线谱（Sibelius / Finale / LilyPond 输出）；术语用拉丁或意大利语（ Allegro, pp, sfz）",
        "戏剧文本用舞台指示斜体或括号；人物名首次出现标注角色缩写",
        "影像引用给出播放时长、时间码与帧率；截图配时间码图注",
        "录音/音高用 Hz 或 十二平均律音名（A = 440 Hz）",
        "演出方与制作人全称首次出现后缩写；馆藏/档案号须可核查",
        "批判段落须区分文本、演出与观众解读三个层次",
    ),
    key_venues=(
        "TDR: The Drama Review",
        "Theatre Research International",
        "Journal of Dramatic Theory and Criticism",
        "Dance Research Journal",
        "Organised Sound",
        "Music Theory Spectrum",
        "Performance: A Journal of Social and Political Theatre",
        "New Musical Quarterly",
    ),
    units_and_formulas_notes=(
        "音高用 Hz；音名按十二平均律（A = 440 Hz）",
        "速度用 bpm；节奏用拍号（4/4、6/8）",
        "演出时长用 h:mm:ss；画面帧率 fps（24 / 25 / 30）",
        "声部/角色编号用声部缩写（Soprano、Alt、Tenor、Bass 或 S/A/T/B）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Avid Pro Tools", "Apple Logic Pro", "Ableton Live", "FL Studio", "Steinberg Cubase", "Native Instruments Kontakt", "Adobe Audition", "Avid Sibelius", "Finale", "LilyPond", "MuseScore", "PRAAT", "SuperCollider", "MainStage", "DaVinci Resolve", "Adobe Premiere Pro", "Final Cut Pro", "Adobe After Effects", "Blender", "Unreal Engine", "TouchDesigner", "Processing", "openFrameworks", "ELAN", "Zotero", "EndNote"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "IMSLP", "BFI Collections", "Library of Congress", "Internet Archive"),
)
