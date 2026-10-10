"""消费服务学科论文支持：服务质量、客户关系管理、渠道与运营。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="consumer_services",
    aliases=(
        "consumer services",
        "consumer service management",
        "customer service",
        "service management",
        "消费服务",
        "客户服务",
        "服务管理",
        "service quality",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与假设）",
            "theory and hypotheses",
            "study design（研究设计与量表）",
            "results",
            "discussion",
            "references",
        ),
        "case_study": (
            "abstract",
            "industry background",
            "service model",
            "operational design",
            "performance evaluation",
            "lessons learned",
            "references",
        ),
        "review": (
            "abstract",
            "historical overview",
            "current methods",
            "open challenges",
            "references",
        ),
    },
    citation_style="APA 7 样式，管理服务类主流",
    reporting_standards={
        "scale": "服务质量量表遵循 SERVQUAL、SERVPERF 或 RATER 标准",
        "data": "CRM 数据须报告来源、时间窗口、字段完整性",
        "measurement": "NPS/CSAT/CES 指标须报告计算口径与样本",
        "survey": "调查遵循 AAPOR 报告规范",
    },
    conventions=(
        "服务质量维度遵循 SERVQUAL 五维或 SERVPERF 简化版",
        "客户满意度用 NPS、CSAT、CES 三指标组合报告",
        "CRM 生命周期按 AARRR 或 RFM 分层",
        "渠道分析区分线上/线下/全渠道 (omnichannel)",
        "样本量报告 N、招募方式、响应率与置信区间",
    ),
    key_venues=(
        "Journal of Service Research",
        "Journal of Service Management",
        "Journal of Service Theory and Practice",
        "Journal of Retailing and Consumer Services",
        "International Journal of Service Industry Management",
        "服务科学",
        "管理评论",
        "南开管理评论",
        "中国流通经济",
    ),
    units_and_formulas_notes=(
        "满意度用 5/7 点 Likert；NPS 用 -100 到 +100",
        "转化率、留存率、复购率用 %",
        "生命周期价值 LTV 用 元或 万元",
        "获客成本 CAC 用 元/客户",
        "渠道贡献用营收占比 % 或毛利占比 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Salesforce Service Cloud", "Salesforce Sales Cloud", "Salesforce Marketing Cloud", "Salesforce Analytics", "HubSpot CRM", "HubSpot Marketing Hub", "HubSpot Service Hub", "Zoho CRM", "Zoho Desk", "Zoho Campaigns", "Microsoft Dynamics 365", "Microsoft Dynamics 365 Sales", "Microsoft Dynamics 365 Customer Service", "Oracle Service Cloud", "SAP Customer Experience", "SAP CX", "Zendesk", "Intercom", "Freshdesk", "Freshchat", "Freshworks", "LiveChat", "Tawk.to", "Kustomer", "ServiceNow", "ServiceNow Customer Service", "Pipedrive", "monday.com", "Salesloft", "Outreach", "Qualtrics XM", "Qualtrics Experience Management", "Medallia", "SurveyMonkey", "Qualtrics Panel", "SPSS", "R", "Python", "Tableau", "Power BI", "Qlik Sense", "Looker", "Salesforce Tableau CRM"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Web of Science", "Semantic Scholar"),
)
