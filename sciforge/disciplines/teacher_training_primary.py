"""小学教师教育论文支持：小学阶段教师培养、全科教学与学习评估的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_primary",
    aliases=("teacher_training_primary", "Teacher training, primary", "小学教师教育", "小学教师培养", "小学教学"),
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
        "whole_person_education": "全科教育须描述道德、智育、体育、美育、劳育的整合方案",
        "teaching_method": "教学方法须区分学科教学与跨学科主题，标注教学目标与活动设计",
        "assessment": "评估须包含课堂评价、作业评价与期末评价，标注评估工具与权重",
        "inclusive_education": "融合教育须描述特殊教育需求识别、支持策略与个别化教育计划",
    },
    conventions=(
        "教学方法须区分低年级（1-2年级）与高年级（3-6年级）的适用差异",
        "课程标准须引用国家课程标准或地方课程标准的版本与编号",
        "学生作品与评估须匿名化处理，隐去姓名与学号",
        "课堂活动须描述组织形式、材料准备、安全注意事项与评估方式",
        "跨学科主题须标注学科关联点、能力目标与课时分配",
    ),
    key_venues=(
        "Journal of Teacher Education",
        "Journal of Curriculum and Instruction",
        "Elementary School Education",
        "Teaching and Teacher Education",
        "Journal of Educational Research",
    ),
    units_and_formulas_notes=(
        "课时以40-45分钟为一标准课时，须明确标注总课时数与分配",
        "学生成绩须标注原始分、百分位与年级排名（匿名）",
        "评估工具须说明编制依据、信度系数与效度证据",
        "教学材料须标注版本、出版年份与作者，便于复现",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas", "Google Classroom", "Schoology", "Edmodo", "Blackboard", "PowerSchool", "Kahoot", "Quizlet", "Socrative", "Quizizz", "Raz-Kids", "Star Reading", "DreamBox", "Istation", "MAP", "Lexile", "Storyline", "Epico", "Canva Education"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
