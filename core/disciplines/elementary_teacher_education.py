"""小学教师教育学科论文支持：小学教育、教学设计与儿童发展研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="elementary_teacher_education",
    aliases=(
        "elementary_teacher_education", "小学教师教育", "小学教育",
        "elementary teacher education", "小学教师教育",
        "primary education", "小学教育",
        "elementary teaching", "小学教学",
        "teacher training", "教师培训",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（教育问题与背景）",
            "method（研究设计、教学干预、评估指标）",
            "results（教学效果与儿童发展）",
            "discussion（教育优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "teaching process（教学过程）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（教育理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "intervention": "教学方案须完整描述",
        "assessment": "评估工具须注明信效度",
        "ethics": "涉及儿童数据须声明隐私保护",
    },
    conventions=(
        "年龄用 岁 表示",
        "教学过程须记录关键活动",
        "评估工具须注明版本与信效度",
        "教学效果须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Elementary School Journal",
        "Journal of Teacher Education",
        "Teaching and Teacher Education",
        "Early Childhood Research Quarterly",
        "Journal of Research in Childhood Education",
        "International Journal of Educational Research",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 表示",
        "教学效果用 标准分差/提升百分比 表示",
        "评估量表用 Likert 5 级表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "NVivo", "Atlas.ti", "Google Classroom", "Moodle", "Zoom", "Microsoft Teams", "Kahoot!", "Canva", "PowerPoint", "Desire2Learn", "Canvas LMS", "Blackboard", "H5P"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
