"""作曲学科论文支持：作曲/音乐创作体裁、APA 引用样式与音乐创作注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="composition",
    aliases=(
        "composition", "作曲", "composition", "musical composition",
        "音乐创作", "music composition", "art music composition",
        "艺术音乐创作", "electroacoustic composition", "电声音乐创作",
        "contemporary music", "当代音乐", "film scoring",
        "影视配乐", "choral composition", "合唱创作",
        "electronic music composition",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与创作问题）",
            "literature review（文献综述）",
            "analysis（分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "analysis": (
            "abstract",
            "introduction",
            "work overview（作品概述）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
        "process": (
            "abstract",
            "introduction",
            "creative process（创作过程）",
            "result（作品）",
            "reflection（反思）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Contemporary Music Review 遵循 APA 规范）",
    reporting_standards={
        "analysis": "作品分析须遵循作品分析报告规范",
        "process": "创作过程报告须遵循过程报告规范",
        "ethnomusicology": "民族音乐学研究报告须遵循田野报告规范",
    },
    conventions=(
        "乐谱须遵循标准记谱规范（拍号、调号、力度记号）",
        "电声/电子音乐须注明电子手段与采样来源",
        "分析须引用标准和声理论或指定分析框架",
        "作品首演须记录首演日期、演出团体与演出场所",
        "引用乐谱须注明来源与版权信息",
    ),
    key_venues=(
        "Contemporary Music Review",
        "Music Theory Spectrum",
        "Music Analysis",
        "Journal of the Royal Musical Association",
        "Music Theory Journal",
        "Leonardo Music Journal",
    ),
    units_and_formulas_notes=(
        "音高用科学记音法（C4 = 中央 C）；音程用半音数",
        "节拍用数字表示（如 4/4、3/8）",
        "速度用 BPM（每分钟拍数）",
        "频率用 Hz；振幅用 dB",
        "引用乐谱须注明出版商、版本与页码",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Sibelius", "Finale", "MuseScore", "Dorico", "Cakewalk by Bandlab", "Noteflight", "LilyPond", "Ooverturn", "Ableton Live", "FL Studio", "Logic Pro", "Pro Tools", "Cubase", "GarageBand", "Reaper", "SuperCollider", "Max/MSP", "Bitwig Studio", "LaTeX", "Overleaf"),
    category="艺术学",
    databases=("OpenAlex", "CNKI", "万方", "Crossref", "RILM Music Abstracts"),
)
