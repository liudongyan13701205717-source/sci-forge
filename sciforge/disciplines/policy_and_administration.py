"""政策与行政管理论文支持：政策制定、公共管理、行政改革与治理评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="policy_and_administration",
    aliases=("policy_and_administration", "政策与行政管理", "公共政策", "公共管理", "Public Policy", "Public Administration", "行政管理", "政策分析", "政策与治理", "公共治理"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"STROBE": "观察性研究规范", "PRISMA": "系统综述规范", "CONSORT": "干预试验报告规范"},
    conventions=("政策评估须使用准实验设计（DID/RD/IV）", "政策文本须标注文号与版本", "利益相关者分析须列出", "成本效益分析须给出货币单位与折现率", "统计须报告置信区间与效应量"),
    key_venues=("Public Administration Review", "Journal of Public Administration Research and Theory", "Journal of Public Policy", "Public Administration", "公共管理与政策评论"),
    units_and_formulas_notes=("成本效益分析用万元或亿美元", "折现率须注明", "政策评估效应量 Cohen's d", "统计须报告置信区间"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "Python", "SPSS", "NVivo", "ATLAS.ti", "MAXQDA", "QGIS", "ArcGIS Pro", "Tableau", "Power BI", "REDCap", "Qualtrics", "JASP", "Mplus", "SAS", "MATLAB", "EndNote", "Zotero", "Microsoft Excel"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "SSRN", "ICPSR"),
)