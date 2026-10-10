"""表演艺术学科论文支持：戏剧、舞蹈、音乐等表演艺术体裁与创作方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="performing_arts",
    aliases=("performing_arts", "表演艺术", "戏剧艺术", "音乐表演", "舞蹈艺术", "performing arts", "drama", "musical performance", "舞蹈表演"),
    paper_types={
        "research": ("abstract", "introduction（艺术议题背景）", "methodology（研究方法/创作过程）", "results（作品/研究成果）", "discussion（美学与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（剧目/演出）", "analysis（形式与内容）", "results（演出效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（美学理论）", "evidence synthesis（艺术实践）", "future directions", "references"),
    },
    citation_style="Chicago 17",
    reporting_standards={"empirical": "遵循 CREATOR 艺术评价规范", "performance_study": "遵循表演研究方法论", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("术语使用须中英对照", "作品创作过程须说明", "演出语境须描述", "美学判断须给出依据", "参考文献含作品名与演出信息"),
    key_venues=("Theatre Research International", "MIME", "Journal of Dance Research", "Contemporary Theatre Review", "Asian Theatre Journal"),
    units_and_formulas_notes=("时长单位用分钟", "作品引用给出创作年份", "舞台说明使用斜体", "术语首次出现标注英文原文"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Premiere Pro", "Final Cut Pro", "DaVinci Resolve", "Ableton Live", "Logic Pro", "Pro Tools", "MuseScore", "LilyPond", "Sibelius", "Finale", "Digital Performer", "After Effects", "Blender", "Unity", "Unreal Engine", "OBS Studio", "Adobe Audition", "Lightroom", "Moodle", "Zoom"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
