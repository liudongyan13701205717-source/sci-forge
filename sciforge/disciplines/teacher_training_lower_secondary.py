"""初中教师教育论文支持：初中阶段教师培养、课程设计与教学质量评估的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_lower_secondary",
    aliases=("teacher_training_lower_secondary", "Teacher training, lower secondary", "初中教师教育", "初中教师培养", "初中教学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "literature review（文献综述）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "teaching design（教学设计）",
            "implementation（实施）",
            "evaluation（评估）",
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
        "curriculum_design": "课程设计须说明学段衔接（小学→初中）、能力梯度与课时安排",
        "teaching_method": "教学方法须区分探究式、讲授式、合作学习等，标注适用场景",
        "assessment": "评估须包含形成性评价与终结性评价，标注评估工具与权重",
        "differentiation": "差异化教学须描述分层策略、支持措施与评估方式",
    },
    conventions=(
        "教学方法须标注适用学段（初一/初二/初三）与学科领域",
        "课程标准须引用国家课程标准或地方课程标准的版本与编号",
        "学生数据须匿名化处理，隐去姓名、学号等可识别信息",
        "课堂活动须描述组织形式、时长、材料准备与评估方式",
        "作业与练习须标注难度等级、预计完成时间与参考答案",
    ),
    key_venues=(
        "Journal of Teacher Education",
        "Journal of Curriculum and Instruction",
        "Educational Researcher",
        "Journal of Educational Psychology",
        "Theory Into Practice",
    ),
    units_and_formulas_notes=(
        "课时以45分钟为一标准课时，须明确标注总课时数与分配",
        "学生成绩须标注原始分、百分位与年级排名（匿名）",
        "评估工具须说明编制依据、信度系数与效度证据",
        "教学材料须标注版本、出版年份与作者，便于复现",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas", "Google Classroom", "Schoology", "Edmodo", "Blackboard", "PowerSchool", "Khan Academy", "Duolingo", "GeoGebra", "PhET", "Google Earth", "Coursera", "Newsela", "Kahoot", "Quizlet", "Socrative", "Quizizz", "Padlet", "Mentimeter"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
