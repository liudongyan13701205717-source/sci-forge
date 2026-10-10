"""人事行政学科论文支持：人事制度、劳动合规与人力资源行政研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="personnel_administration",
    aliases=("personnel_administration", "人事行政", "人力资源行政", "人事管理", "labor administration", "HR administration", "劳动行政", "人事制度", "组织人事"),
    paper_types={
        "research": ("abstract", "introduction（人事议题背景）", "methodology（制度/组织分析）", "results（人事数据）", "discussion（行政启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（机构案例）", "analysis（制度解析）", "results（行政效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（行政理论）", "evidence synthesis（研究证据）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"empirical": "遵循 EQUATOR 报告规范", "survey": "遵循 STROBE 声明", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("制度条款须准确引用", "样本来源须说明", "劳动合规数据须注明来源", "研究伦理审批须给出", "结果给出置信区间"),
    key_venues=("Human Resource Management", "Journal of Business and Psychology", "International Journal of Human Resource Management", "Public Administration Review", "Personnel Psychology"),
    units_and_formulas_notes=("统计结果保留 3 位小数", "回归系数用 β 或 B 并注显著性", "样本量与检验力须报告", "劳动合规用百分比表示"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SAP SuccessFactors", "Workday HCM", "Oracle HCM Cloud", "Lattice", "BambooHR", "ADP Workforce Now", "Cornerstone OnDemand", "Mokahr", "盖雅工场", "北森 eHRS", "SPSS", "R", "STATA", "Mplus", "NVivo", "MAXQDA", "Qualtrics", "Python", "Jupyter", "Tableau"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
