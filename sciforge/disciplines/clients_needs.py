"""Clients' needs 学科论文支持：客户需求分析/客户管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="clients_needs",
    aliases=(
        "Clients' needs", "客户需求分析", "Client Needs", "Customer Needs",
        "客户需求", "Client Care", "Customer Care", "Client Centric",
        "客户需求管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "customer_satisfaction": "客户满意度指标须标注测量时点与置信区间",
        "needs_assessment": "需求分析须标注 Kano 模型与 MoSCoW 优先级方法",
        "data_privacy": "涉及个人数据须遵循 GDPR 或《个人信息保护法》",
    },
    conventions=(
        "使用 ISO 9001 客户满意度评估框架",
        "用户访谈遵循 ISO 20488 需求工程规范",
        "引用客户满意度数据时给出置信区间与样本量",
        "需求分析遵循 Kano 模型与 MoSCoW 优先级",
        "报告应遵循 GDPR/《个人信息保护法》要求",
    ),
    key_venues=(
        "Journal of Consumer Research",
        "Journal of Marketing",
        "Journal of Service Research",
        "Journal of Business Research",
        "Journal of Consumer Psychology",
        "Journal of Retailing and Consumer Services",
    ),
    units_and_formulas_notes=(
        "NPS = %推荐者 − %批评者，值域 −100 至 100，须注明样本量",
        "CSAT 评分区间须注明（如 1–5 或 1–10）并给出均值±标准差",
        "流失率 = 期间流失客户数 / 期初客户数 × 100%，须标注时间口径",
        "Kano 分类须注明各需求项的必备/期望/魅力归类及依据",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Excel", "Google Sheets", "SPSS", "RStudio", "SAS", "Tableau", "Power BI", "Salesforce", "HubSpot", "Zendesk", "Intercom", "Freshdesk", "Typeform", "SurveyMonkey", "Qualtrics", "Google Analytics", "Mixpanel", "Hotjar", "Amplitude", "CrazyListings"),
    category="管理学",
    databases=("OpenAlex", "Crossref"),
)
