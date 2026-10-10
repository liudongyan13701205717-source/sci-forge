"""个人技能学科论文支持：通用技能、软技能与职业胜任力研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="personal_skills",
    aliases=("personal_skills", "个人技能", "软技能", "沟通技能", "职业技能", "personal skills", "soft skills", "通用技能", "competencies"),
    paper_types={
        "research": ("abstract", "introduction（技能议题背景）", "methodology（量表/胜任力模型）", "results（技能评估）", "discussion（技能发展）", "references"),
        "case_study": ("abstract", "introduction", "case description（技能案例）", "analysis（技能应用）", "results（技能提升）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（胜任力理论）", "evidence synthesis（研究证据）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"empirical": "遵循 EQUATOR 报告规范", "survey": "遵循 STROBE 声明", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("技能定义须清晰", "量表信效度须报告", "胜任力模型须注明来源", "伦理审批须给出", "结果给出置信区间"),
    key_venues=("Journal of Occupational and Organizational Psychology", "Human Performance", "Journal of Vocational Behavior", "Research in Personnel and Human Resources Management", "Journal of Applied Psychology"),
    units_and_formulas_notes=("量表得分保留 2 位小数", "统计结果保留 3 位小数", "回归系数用 β 或 B 并注显著性", "样本量与检验力须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "STATA", "Mplus", "NVivo", "MAXQDA", "Qualtrics", "SurveyMonkey", "Google Forms", "Tableau", "Power BI", "Python", "Jupyter", "Excel", "Adobe Illustrator", "Photoshop", "Canva", "Notion", "Moodle", "Zoom"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
