"""个人发展学科论文支持：自我提升、成长理论与个人效能研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="personal_development",
    aliases=("personal_development", "个人发展", "自我提升", "自我成长", "personal growth", "self-development", "个人效能", "自我实现", "成长理论"),
    paper_types={
        "research": ("abstract", "introduction（发展议题背景）", "methodology（量表/干预设计）", "results（发展评估）", "discussion（发展机制）", "references"),
        "case_study": ("abstract", "introduction", "case description（个人发展案例）", "analysis（成长过程）", "results（发展成效）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（发展理论）", "evidence synthesis（研究证据）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"empirical": "遵循 EQUATOR 报告规范", "qualitative": "遵循 COREQ 声明", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("发展量表信效度须报告", "干预方案须说明时长与剂量", "对照组设计须说明", "伦理审批号须给出", "结果给出效应量"),
    key_venues=("Journal of Positive Psychology", "Personality and Individual Differences", "Journal of Happiness Studies", "Psychology of Consciousness", "Journal of Personality"),
    units_and_formulas_notes=("量表得分保留 2 位小数", "效应量用 Cohen d 或 r", "统计检验双侧 p<0.05", "样本量与检验力须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Big Five Inventory", "Self-Determination Theory", "Ryff Psychological Wellbeing", "Self-Efficacy Scale", "MBTI", "DiSC Assessment", "SWOT Analysis", "GROW Model", "SPSS", "R", "STATA", "Mplus", "NVivo", "MAXQDA", "Qualtrics", "Excel", "Python", "Jupyter", "Tableau", "Moodle"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
