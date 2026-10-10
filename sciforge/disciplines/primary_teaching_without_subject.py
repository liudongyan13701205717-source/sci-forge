"""初等教学（不分学科）学科论文支持：小学通用教学、课堂管理与学习成效研究体裁、APA 引用样式与教学评估注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="primary_teaching_without_subject",
    aliases=("primary_teaching_without_subject", "初等教学（不分学科）", "初等教学", "primary teaching", "小学教学", "elementary teaching", "课堂管理", "primary education without subject", "小学通用教学"),
    paper_types={
        "research": ("abstract", "introduction（教学问题与背景）", "methodology（研究设计、教学干预与评估指标）", "results（学习成效与课堂行为结果）", "discussion（教学方法优化与推广建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（学校、班级与教学情境描述）", "analysis（教学过程、课堂管理与成效分析）", "results（学习结果与师生反馈）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（小学教学法理论综述）", "evidence synthesis（教学实践与实证证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "教学方案须完整描述（学段、课时、班级与教材）", "k2": "评估工具须注明版本与信效度", "k3": "涉及儿童数据须声明隐私保护与伦理审查"},
    conventions=("年龄用 岁 表示", "教学过程须记录关键活动与课时", "评估工具须注明版本与信效度", "教学效果须区分短期与长期", "统计检验注明效应量与置信区间"),
    key_venues=("Elementary School Journal", "Journal of Research in Childhood Education", "Teaching and Teacher Education", "Early Childhood Research Quarterly", "Educational Research"),
    units_and_formulas_notes=("年龄用 岁 表示", "教学效果用 标准分差/提升百分比 表示", "评估量表用 Likert 5 级表示", "统计检验注明 t/F/χ² 值、p 值与效应量 d 或 η²"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "NVivo", "Atlas.ti", "Google Classroom", "Moodle", "Blackboard", "Canvas LMS", "Microsoft Teams", "Zoom", "Kahoot!", "Canva", "PowerPoint", "H5P", "GeoGebra", "Desmos"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
