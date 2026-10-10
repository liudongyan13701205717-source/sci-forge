"""政治学论文支持：政治理论、政治制度、国际关系与政治治理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="politics",
    aliases=("politics", "政治学", "政治", "公共政策", "Public Policy", "政治经济学", "政府治理", "政治治理", "Political Studies", "政治科学"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"STROBE": "观察性研究规范", "CONSORT": "干预试验报告规范", "PRISMA": "系统综述规范"},
    conventions=("数据来源须注明", "民调须报告样本量与置信区间", "变量定义须给出", "统计须报告效应量", "理论框架须明确"),
    key_venues=("Journal of Politics", "American Political Science Review", "British Journal of Political Science", "政治学研究", "Journal of Political Science Education"),
    units_and_formulas_notes=("民调数据用 %", "置信区间 95%", "效应量 Cohen's d", "统计须报告标准误"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "Python", "SPSS", "NVivo", "ATLAS.ti", "QGIS", "ArcGIS Pro", "Tableau", "Power BI", "REDCap", "Qualtrics", "JASP", "Mplus", "SAS", "MATLAB", "Microsoft Excel", "EndNote", "Zotero", "SurveyMonkey"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "SSRN", "ICPSR"),
)