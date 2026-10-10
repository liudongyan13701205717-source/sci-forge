"""音乐史学科论文支持：乐谱考据、音源分析与音乐批评史体裁、Chicago 引用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="history_of_music",
    aliases=("history_of_music", "音乐史", "音乐学", "音乐史学", "乐谱史", "音乐批评史"),
    paper_types={
        "research": ("abstract", "introduction（作品与背景）", "methodology（乐谱与音源方法）", "results（发现）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（作品个案）", "analysis（乐谱与风格分析）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（音乐史综述）", "evidence synthesis（乐谱综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（注-书目）",
    reporting_standards={"score": "乐谱引用须给出页码与小节号", "recording": "录音引用须给出音轨与时间点", "performance": "演出史须给出时间与场馆"},
    conventions=("乐曲名用斜体或引号一致", "乐章与曲号须给出编号", "乐谱版本须给出印次", "音轨引用给出 mm:ss 时间点", "作曲家用国际通用译名"),
    key_venues=("Journal of the American Musicological Society", "19th Century Music", "Journal of Music Theory", "Music and Letter", "中国音乐学"),
    units_and_formulas_notes=("乐谱引用给出小节号与页码", "录音引用给出 mm:ss 时间点", "音高用标准 MIDI 编号或十二平均律", "演奏速度须给出 BPM 与速度术语"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "Tropy", "Omeka S", "Gephi", "Palladio", "Voyant Tools", "AntConc", "Verovio", "Music21", "R", "Python", "Juxta", "CollateX", "LaTeX", "Nodegoat", "Recogito", "Transkribus", "MuseScore", "Audacity", "Dia"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
