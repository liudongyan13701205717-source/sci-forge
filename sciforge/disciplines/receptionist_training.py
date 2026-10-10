"""接待员培训学科论文支持：前厅服务/客户服务/沟通技能体裁、APA 引用样式与培训成效评估口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="receptionist_training",
    aliases=(
        "receptionist_training",
        "接待员培训",
        "前台培训",
        "客户服务培训",
        "Receptionist Training",
        "Front Desk Training",
        "客户服务",
        "接待实务",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（培训设计与评估）", "results（培训成效）", "discussion（技能发展与应用）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（培训过程分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；服务业教育与培训研究常用 APA）",
    reporting_standards={
        "k1": "培训研究须报告前后测设计",
        "k2": "技能评估须说明评分量表",
        "k3": "案例须注明行业与规模",
    },
    conventions=(
        "培训时长与课时须注明",
        "技能评分给出量表与评分者",
        "前后测结果报告效应量",
        "服务流程步骤须可复述",
        "多语言场景须标注语种",
    ),
    key_venues=(
        "Journal of Hospitality and Tourism Education",
        "International Journal of Hospitality Management",
        "Education + Training",
        "Culinary Science and Hospitality Management",
        "Journal of Services Marketing",
    ),
    units_and_formulas_notes=(
        "通过率/结业率给出分母口径",
        "满意度评分注明制式",
        "培训时长单位统一为学时",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office", "Microsoft Outlook", "Salesforce", "Zendesk", "HubSpot", "Zoho", "Freshdesk", "Qualtrics", "SPSS", "Excel", "Tableau", "Power BI", "Zoom", "Microsoft Teams", "MISHAWAK", "Mistral Training", "Kaltura", "Endnote", "Yelp 点评", "TripAdvisor 点评"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
