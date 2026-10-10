"""综合项目学科论文支持：通用项目、跨学科教育与基础职业训练。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="generic_programmes_and",
    aliases=("generic_programmes_and", "综合项目", "通用项目", "跨学科教育", "Generic programmes", "Cross-disciplinary education", "基础职业训练", "职业与技能"),
    paper_types={
        "research": ("abstract", "introduction（跨学科教育与问题）", "methodology（课程设计、样本与评估）", "results（学习成效）", "discussion（教育意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（项目/机构概况）", "analysis（课程、教学与整合）", "results（成效数据）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（跨学科教育、技能框架综述）", "evidence synthesis（不同模式对比）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份）或 GB/T 7714 规范",
    reporting_standards={"curriculum": "课程须报告目标、内容、学时与学分", "assessment": "评估须报告量表、方法、效度", "outcome": "学习成效须报告前后测与统计检验"},
    conventions=("跨学科整合路径须图示", "样本描述（人数、背景）须报告", "伦理审查通过情况须报告", "评估指标分层（认知、技能、态度）", "数据报告 M/SD/95% CI"),
    key_venues=("Studies in Continuing Education", "Journal of Vocational Education", "Vocations and Learning", "Journal of Education and Work", "中国职业技术教育"),
    units_and_formulas_notes=("学时用 h", "学分用 CPD/CPU", "评估得分用 Likert 5 点", "通过率用 %", "成效差异用 % 或 p 值"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "NVivo", "Atlas.ti", "MAXQDA", "Qualtrics", "Blackboard Learn", "Canvas LMS", "Moodle", "Mathematica", "Jupyter", "GeoGebra", "G*Power", "Mplus", "AMOS", "SmartPLS", "LaTeX", "Zotero", "EndNote", "Turnitin"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "Web of Science"),
)
