"""政治科学与公民学论文支持：政治理论、公民教育、政治参与与民主治理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="political_sciences_and_civics",
    aliases=("political_sciences_and_civics", "政治学与公民学", "政治科学", "公民学", "Political Sciences", "Civics", "政治学", "公民教育", "公民素养", "Civic Education"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"STROBE": "观察性研究规范", "CONSORT": "干预试验报告规范", "PRISMA": "系统综述规范"},
    conventions=("民调须报告样本量与置信区间", "公民教育课程须标注适用年级", "政治参与指标须给出操作化定义", "统计须报告效应量", "问卷须报告信度与效度"),
    key_venues=("Journal of Politics", "Political Science Research and Methods", "British Journal of Political Science", "政治学研究", "Journal of Political Science Education"),
    units_and_formulas_notes=("民调数据用 %", "置信区间 95%", "效应量 Cohen's d", "信度 Cronbach's α"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "Python", "SPSS", "NVivo", "ATLAS.ti", "QGIS", "ArcGIS Pro", "Tableau", "Power BI", "REDCap", "Qualtrics", "SurveyMonkey", "JASP", "Mplus", "SAS", "MATLAB", "Microsoft Excel", "EndNote", "Zotero"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "SSRN", "ICPSR"),
)