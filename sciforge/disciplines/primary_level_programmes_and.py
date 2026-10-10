"""初等教育项目与教学学科论文支持：小学课程体系、教学设计与学习成效研究体裁、APA 引用样式与教学评估注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="primary_level_programmes_and",
    aliases=("primary_level_programmes_and", "初等教育项目与教学", "初等教育", "primary level programmes", "初等教育项目", "primary level instruction", "初等教学", "elementary education programmes", "小学教育项目"),
    paper_types={
        "research": ("abstract", "introduction（教育问题与背景）", "methodology（研究设计、教学干预与评估指标）", "results（教学成效与学习结果）", "discussion（教学优化与课程设计建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（课程项目与教学情境描述）", "analysis（教学设计、课堂活动与成效分析）", "results（学习结果与教师反馈）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（初等课程与教学理论综述）", "evidence synthesis（课程实践与实证证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "课程与教学干预方案须完整披露（课时、学段、班级与教材版本）", "k2": "评估工具须注明版本、编制者与信效度指标", "k3": "涉及学生数据须声明伦理审查与匿名化处理"},
    conventions=("学段与年龄用 岁 与 年级 表示", "教学过程须记录关键活动与课时安排", "教学效果须区分短期与长期成效", "评估量表用 Likert 5 级表示", "统计检验注明 t/F/χ² 值、p 值与效应量（d/η²）与置信区间"),
    key_venues=("Elementary School Journal", "Journal of Teacher Education", "Teaching and Teacher Education", "Educational Research", "International Journal of Educational Research"),
    units_and_formulas_notes=("年龄用 岁 表示，学段按 年级 标注", "教学成效用 标准分差/提升百分点 表示", "课时用 学时 或 分钟 计", "评估量表用 Likert 5 级表示"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Jamovi", "Excel", "Qualtrics", "Google Forms", "SurveyMonkey", "NVivo", "Atlas.ti", "MAXQDA", "Google Classroom", "Moodle", "Canvas LMS", "Microsoft Teams", "Zoom", "Kahoot!", "Canva", "PowerPoint", "H5P"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
