"""办公管理学学科论文支持：办公管理/行政管理体裁、APA 引用样式与管理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="office_management",
    aliases=("office_management", "办公管理", "行政管理", "office administration", "secretarial studies", "office administration"),
    paper_types={
        "research": ("abstract", "introduction（背景与管理问题）", "methodology（数据与分析）", "results（发现）", "discussion（机制与启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例背景）", "analysis（流程与管理分析）", "results（成效评估）", "discussion（经验与改进）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"systematic_review": "遵循 PRISMA 声明", "case_study": "遵循 CBSE 报告", "mixed_method": "遵循 MMRE 报告"},
    conventions=("样本量须报告", "量表须注明来源与信度", "组织变量须清晰定义", "结果须给出 95% CI", "时间单位须一致"),
    key_venues=("Journal of Business and Industrial Marketing", "Journal of Business Economics and Management", "Administrative Sciences", "International Journal of Business Information Systems", "Public Administration Review"),
    units_and_formulas_notes=("时间用 天/小时", "货币用 元/USD", "比率给出%", "公式用 amsmath", "数值给出均值±SD"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Project", "Asana", "Monday.com", "Smartsheet", "SAP Concur", "SAP ERP", "Oracle NetSuite", "QuickBooks", "FileNet", "Adobe AEM", "SharePoint", "Confluence", "Qualtrics", "SPSS", "R", "NVivo", "Tableau", "Power BI", "Excel", "Jira"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
