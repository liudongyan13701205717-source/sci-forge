"""音乐教师教育论文支持：音乐教育领域教师培养、教学法与课程设计的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_in_music",
    aliases=("teacher_training_in_music", "Teacher training in music", "音乐教师教育", "音乐教育培养", "音乐教学法"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "literature review（文献综述）",
            "methods（教学方法）",
            "results（教学成果）",
            "discussion（讨论与启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "teaching design（教学设计）",
            "implementation（实施过程）",
            "evaluation（教学效果评估）",
            "conclusion",
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
        "teaching_method": "音乐教学法须描述具体教学方法、适用年龄与乐器，区分集体教学与个别指导",
        "assessment": "音乐能力评估须包含技术练习、视谱、即兴演奏等维度，标注评分标准",
        "curriculum": "课程设计须说明音乐类型、教学顺序与课时分配，区分基础教学与高阶训练",
        "practice_integration": "实践环节须描述排练组织、演出机会与反馈机制",
    },
    conventions=(
        "乐谱引用须标注调性、速度与拍号，改编须注明改编者",
        "音名与音程记法须全文统一（字母数字或中文），不得混用",
        "音频材料须在附录或补充材料中提供访问方式与编号",
        "音乐能力评估须明确技术练习、视谱与即兴演奏的评分权重",
        "引用经典作品须标注作曲家、作品号与出版版本",
    ),
    key_venues=(
        "Journal of Music Teacher Education",
        "Music Education Review",
        "International Journal of Music Education",
        "Journal of Research in Music Education",
        "Music Education Journal",
    ),
    units_and_formulas_notes=(
        "音高记法使用标准音名（C D E F G A B）或首调唱名（Do Re Mi），须全文统一",
        "速度标记使用拍速（BPM）或意大利语速度术语，须明确标注单位",
        "频率以赫兹（Hz）标注，音分（cents）用于精确音程计算",
        "乐谱引用须标注作曲家全名、作品号（Op.）、出版年份与版本",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("MuseScore", "Sibelius", "Finale", "LilyPond", "Dorico", "Noteflight", "GarageBand", "Logic Pro", "Ableton Live", "Audacity", "Pro Tools", "Band-in-a-Box", "ChordPro", "Anvil Studio", "ScoreCloud", "Sequentia", "MuseClass", "Songsmith", "Guitar Pro", "Sonic Visualiser"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
