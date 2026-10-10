"""初中教师培训学科论文支持：师范教育、教师专业发展与人培课程。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="lower_secondary_teacher_training",
    aliases=(
        "lower_secondary_teacher_training",
        "初中教师培训",
        "师范教育",
        "教师教育",
        "normal education",
        "teacher education",
        "初中教育",
        "teacher training",
        "professional development",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（案例分析）",
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
        "k1": "教学实验报告样本、时间与效果量",
        "k2": "培训课程评估使用 Kirkpatrick 四层",
        "k3": "教育公平研究须报告学校与地区样本",
    },
    conventions=(
        "研究对象标注地区、学校类型与人数",
        "课堂观察报告使用编码表",
        "问卷信度报告 Cronbach's α",
        "干预研究说明对照组与随机化",
        "教师案例匿名化处理",
    ),
    key_venues=(
        "Teachers College Record",
        "Journal of Teacher Education",
        "Teaching and Teacher Education",
        "Studies in Educational Evaluation",
        "教师教育研究",
    ),
    units_and_formulas_notes=(
        "教学效果以标准化测验分报告",
        "培训满意度以 5 级 Likert 计",
        "出勤率以百分比计",
        "教育成效以百分比提升报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "NVivo", "R", "Mplus", "HLM", "RQED", "ELAN", "Camtasia", "OBS Studio", "Zoom", "ClassIn", "雨课堂", "学习通", "Kahoot", "Padlet", "Prezi", "Scratch", "GeoGebra", "Word", "LaTeX"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
