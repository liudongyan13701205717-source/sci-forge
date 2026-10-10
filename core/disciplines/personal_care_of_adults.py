"""成人个人护理学科论文支持：老年护理、照护模式与临床照护研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="personal_care_of_adults",
    aliases=("personal_care_of_adults", "成人护理", "老年照护", "护理实践", "成人个人照护", "nursing care", "adult care", "老年护理", "成人照护"),
    paper_types={
        "research": ("abstract", "introduction（护理议题背景）", "methodology（研究设计/样本）", "results（临床数据）", "discussion（护理意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（个案照护）", "analysis（护理过程）", "results（干预效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（照护理论）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"clinical_trial": "遵循 CONSORT 声明", "qualitative": "遵循 COREQ 声明", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("纳入排除标准须明示", "样本量与统计检验力须报告", "伦理审批号须给出", "临床量表须注明来源", "结果给出 95% 置信区间"),
    key_venues=("Journal of Advanced Nursing", "International Journal of Nursing Studies", "Nursing in Critical Care", "Journal of Clinical Nursing", "Ageing and Health"),
    units_and_formulas_notes=("计量单位遵循 SI 标准", "生命体征给出单位（如 mmHg、bpm）", "统计结果保留 2 位小数", "量表信度系数（Cronbach α）须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Epic Systems", "Oracle Cerner", "Meditech", "Allscripts", "OpenMRS", "HL7 FHIR", "Epi Info", "STATA", "R", "SPSS", "Sage Research", "Qualtrics", "NVivo", "MAXQDA", "Excel", "Power BI", "Tableau", "Python", "Jupyter", "RStudio"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
