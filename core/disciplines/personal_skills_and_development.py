"""个人技能与发展学科论文支持：职业技能、终身学习与胜任力发展研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="personal_skills_and_development",
    aliases=("personal_skills_and_development", "技能发展", "终身学习", "成人教育", "competency development", "lifelong learning", "技能提升", "成人学习", "职业发展"),
    paper_types={
        "research": ("abstract", "introduction（技能议题背景）", "methodology（量表/干预设计）", "results（技能发展）", "discussion（学习机制）", "references"),
        "case_study": ("abstract", "introduction", "case description（技能发展案例）", "analysis（发展过程）", "results（发展成效）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（学习理论）", "evidence synthesis（研究证据）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"empirical": "遵循 EQUATOR 报告规范", "qualitative": "遵循 COREQ 声明", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("技能定义须清晰", "量表信效度须报告", "干预方案须说明时长与剂量", "对照组设计须说明", "结果给出效应量"),
    key_venues=("International Journal of Lifelong Education", "Journal of Adult and Continuing Education", "Studies in Continuing Education", "Journal of Vocational Behavior", "Human Resource Development International"),
    units_and_formulas_notes=("量表得分保留 2 位小数", "效应量用 Cohen d 或 r", "统计检验双侧 p<0.05", "样本量与检验力须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Big Five Inventory", "Self-Determination Theory", "Ryff Psychological Wellbeing", "Self-Efficacy Scale", "MBTI", "DiSC Assessment", "SWOT Analysis", "GROW Model", "SPSS", "R", "STATA", "Mplus", "NVivo", "MAXQDA", "Qualtrics", "Excel", "Python", "Jupyter", "Tableau", "Moodle"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
