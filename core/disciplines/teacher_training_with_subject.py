"""学科教师教育论文支持：学科教学论领域教师培养、学科知识整合与课堂教学研究的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_with_subject",
    aliases=("teacher_training_with_subject", "Teacher training with subject", "学科教师教育", "学科教师培养", "学科教学论"),
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
            "classroom research（课堂研究）",
            "analysis（分析）",
            "results（结果）",
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
        "content_knowledge": "学科内容知识（PCK）须描述学科知识、教学法知识与学生认知知识的整合",
        "classroom_research": "课堂研究须描述研究设计、数据收集方法、分析策略与局限性",
        "professional_development": "学科教师专业发展须描述发展路径、关键阶段与影响因素",
        "curriculum_alignment": "学科课程须与国家/地方课程标准对齐，标注能力目标与课时安排",
    },
    conventions=(
        "学科教学术语须使用国家课程标准术语，首次出现时标注中英文对照",
        "PCK研究须区分学科内容知识、教学法知识与情境知识三个维度",
        "课堂观察须使用标准化观察工具，标注观察焦点、时长与编码方案",
        "学科教材分析须标注教材版本、出版社、修订年份与编写依据",
        "跨学科整合须描述学科关联点、能力迁移路径与课时分配",
    ),
    key_venues=(
        "Journal of Teacher Education",
        "Journal of Curriculum Studies",
        "Teaching and Teacher Education",
        "Journal of Research in Science Teaching",
        "Journal of Mathematical Behavior",
    ),
    units_and_formulas_notes=(
        "学科课时须按国家课程标准的周课时与年课时标注",
        "教师PCK评估须区分学科知识、教学法知识与情境知识三个维度的评分标准",
        "课堂观察编码须标注编码单位（时间间隔/事件）、编码者与一致性系数",
        "教材分析须标注教材版本、修订年份与编写依据",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas", "Google Classroom", "Schoology", "Edmodo", "Blackboard", "PowerSchool", "GeoGebra", "PhET", "Google Earth", "Duolingo", "Khan Academy", "Quizlet", "Kahoot", "Socrative", "Quizizz", "Padlet", "Mentimeter", "Nearpod", "Pear Deck"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
