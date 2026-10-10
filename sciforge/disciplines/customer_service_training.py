"""Customer service training 学科论文支持：客服技能训练/对话质检/体验管理体裁、管理学报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="customer_service_training",
    aliases=(
        "customer_service_training",
        "customer service training",
        "客户服务培训",
        "客服技能培训",
        "客户服务质量",
        "customer service management",
        "contact center training",
        "客服质检",
        "conversation quality assurance",
        "customer experience training",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "intervention_study": (
            "abstract",
            "introduction",
            "training design（培训课程设计）",
            "implementation（实施与保真度）",
            "outcome measures（结果指标：KPI/满意度/绩效）",
            "transfer and sustainability（迁移与持续效果）",
            "references",
        ),
        "quality_audit": (
            "abstract",
            "introduction（审计范围）",
            "sampling and instruments（抽样与量规）",
            "scoring results（评分结果）",
            "common deficiencies（共性缺陷）",
            "recommendations（改进建议）",
            "references",
        ),
    },
    citation_style="APA 第7版（服务管理与培训研究主流规范）",
    reporting_standards={
        "sampling": "会话抽样须报告抽样框、分层方式、样本量与置信水平",
        "scoring": "质检量规须公开评分锚点，报告评分者间信度（ICC 或 Cohen's κ）",
        "pre_post": "培训效果研究须报告前后测差值、效应量与对照条件",
        "privacy": "会话数据脱敏与录音告知须符合所在地法规，报告告知方式",
        "kpis": "核心指标定义须显式（首次解决率 FCR、平均处理时长 AHT、CSAT、NPS 的口径）",
    },
    conventions=(
        "指标首次出现须给出英文全称、缩写与计算公式（如 FCR、AHT、CSAT、NPS、QA 覆盖率）",
        "培训设计须标注所依理论（如 Kirkpatrick 四级评估、70-20-10、Kotter 变革模型、Kolb 经验学习）",
        "情景对话与话术示例须脱敏，客户信息用代号替换",
        "评分量表采用统一锚定（anchored scale），报告锚点与边界规则",
        "A/B 类对照研究须说明流量分配、分流随机化与最小样本量",
        "引用平台功能须标注系统名称与版本（如 Zendesk 版本、Genesys 云版本）",
    ),
    key_venues=(
        "Journal of Service Research",
        "Journal of Service Management",
        "European Journal of Training and Development",
        "Journal of Business and Industrial Training",
        "International Journal of Training and Development",
        "Journal of Retail and Consumer Services",
        "旅游学报（服务业专题）",
    ),
    units_and_formulas_notes=(
        "时延类指标用 s 或 min，给出均值与 P90/P95 分位数",
        "比率类指标给出分子/分母定义与统计周期",
        "满意度评分注明量表范围（如 1-5 分或 0-10 分 NPS）",
        "样本量与置信区间须报告；缺失数据说明处理方式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Zendesk", "Salesforce Service Cloud", "Freshdesk", "Intercom", "HubSpot Service Hub", "Genesys Cloud CX", "NICE CXone", "NICE Insights", "Verint Engage", "Five9 Contact Center", "Talkdesk", "Klaus", "Sapia.ai", "Observe.AI", "Cognigy", "Amazon Connect", "Twilio Flex", "Medallia", "Qualtrics XM", "Sprinklr", "Mursion", "iMocha", "Cornerstone OnDemand", "360Learning", "WorkRamp", "Degreed"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "Scopus", "Web of Science", "Google Scholar"),
)
