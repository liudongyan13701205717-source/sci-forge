"""综合项目与资格学科论文支持：职业项目、终身学习、认证与职业发展。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="general_programmes_and_qualification",
    aliases=("general_programmes_and_qualification", "综合项目与资格", "通用教育项目", "终身教育", "General programmes and qualification", "Vocational training", "成人教育", "继续教育"),
    paper_types={
        "research": ("abstract", "introduction（项目背景与问题）", "methodology（设计、学员样本、评估方法）", "results（学习成效与评估数据）", "discussion（教育意义与改进）", "references"),
        "case_study": ("abstract", "introduction", "case description（项目/院校概况）", "analysis（课程、教学与认证机制）", "results（成效与影响）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（终身学习、职业教育理论综述）", "evidence synthesis（不同项目对比）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份）或 GB/T 7714 规范",
    reporting_standards={"project": "项目须报告目标、周期、参与者与课程结构", "evaluation": "学习评估须报告方法、量表与效度", "certification": "认证与考核须报告标准与通过率"},
    conventions=("课程结构按模块或学时标注", "评估指标分层：认知、技能、态度", "样本量与招募方式须报告", "伦理审查与知情同意", "效果数据报告前后测差异"),
    key_venues=("Studies in Continuing Education", "Journal of Workplace Learning", "Education and Training", "中国成人教育", "教育研究"),
    units_and_formulas_notes=("学时/学分用 h 或 CPD", "学习效果用百分比或量表分", "通过率用 %", "满意度用 Likert 5 点", "时间跨度用 d/周"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Moodle（学习管理）", "Blackboard", "Canvas", "Open edX", "Coursera", "Kahoot（互动学习）", "Socrative", "Google Classroom", "Learning Management（企业 LMS）", "e-Campus", "SPSS", "R", "Excel", "Google Forms", "Jingyun（问卷）", "WJX（问卷星）", "RefWorks", "EndNote", "NVivo（质性分析）", "Origin", "Principles for Adult Learning（研究框架）"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
