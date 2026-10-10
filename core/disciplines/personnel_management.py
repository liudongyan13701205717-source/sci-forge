"""人事管理学科论文支持：人力资源管理、人才发展与组织行为研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="personnel_management",
    aliases=("personnel_management", "人事管理", "人力资源管理", "人才管理", "human resource management", "HR management", "员工管理", "人才发展", "组织管理"),
    paper_types={
        "research": ("abstract", "introduction（人事议题背景）", "methodology（量表/组织数据）", "results（人事数据）", "discussion（管理启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（企业案例）", "analysis（体系解析）", "results（管理效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（管理理论）", "evidence synthesis（研究证据）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"empirical": "遵循 EQUATOR 报告规范", "survey": "遵循 STROBE 声明", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("量表信效度须报告", "样本与测量工具须明示", "构念效度用 CFA 报告", "组织层级须说明", "结果给出置信区间"),
    key_venues=("Human Resource Management Review", "Journal of Management", "Academy of Management Journal", "Organization Science", "Journal of Organizational Behavior"),
    units_and_formulas_notes=("统计结果保留 3 位小数", "量表题项使用 Likert 5 点或 7 点", "回归系数用 β 或 B 并注显著性", "样本量与检验力须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SAP SuccessFactors", "Workday HCM", "Oracle HCM Cloud", "Lattice", "Betterworks", "Culture Amp", "BambooHR", "ADP Workforce Now", "Cornerstone OnDemand", "Mokahr", "盖雅工场", "北森 eHRS", "SPSS", "R", "STATA", "Mplus", "NVivo", "MAXQDA", "Python", "Jupyter"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
