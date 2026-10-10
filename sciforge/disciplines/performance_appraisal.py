"""绩效评估学科论文支持：绩效评价量表、360 度反馈与人力资源数据研究方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="performance_appraisal",
    aliases=("performance_appraisal", "绩效评估", "绩效管理", "员工考核", "绩效测评", "performance management", "employee appraisal", "绩效考评", "人力资源评估"),
    paper_types={
        "research": ("abstract", "introduction（绩效议题背景）", "methodology（量表/模型/样本）", "results（评估数据）", "discussion（管理启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（企业实践）", "analysis（体系解析）", "results（改善效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（评价理论）", "evidence synthesis（实证证据）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"empirical": "遵循 EQUATOR 报告规范", "survey": "遵循 STROBE 声明", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("量表信效度须报告", "样本与测量工具须明示", "自评与他评数据分开报告", "构念效度用 CFA 报告", "结果给出置信区间"),
    key_venues=("Journal of Applied Psychology", "Human Resource Management Review", "Human Resource Management", "Journal of Management", "Personnel Psychology"),
    units_and_formulas_notes=("统计结果保留 3 位小数", "量表题项使用 Likert 5 点或 7 点", "回归系数用 β 或 B 并注显著性", "样本量与统计检验力须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SAP SuccessFactors", "Workday HCM", "Oracle HCM Cloud", "Lattice", "Betterworks", "Culture Amp", "360FeedbackPro", "BambooHR", "ADP Workforce Now", "Cornerstone OnDemand", "Mokahr", "盖雅工场", "北森 eHRS", "SPSS", "R", "STATA", "Mplus", "NVivo", "Python", "Jupyter"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
