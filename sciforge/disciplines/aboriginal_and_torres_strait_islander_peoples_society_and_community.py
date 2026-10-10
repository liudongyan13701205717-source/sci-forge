"""Aboriginal And Torres Strait Islander Peoples, Society And Community 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aboriginal_and_torres_strait_islander_peoples_society_and_community",
    aliases=(
        "Aboriginal And Torres Strait Islander Peoples, Society And Community",
        "原住民社会与社区",
        "ATSI Society and Community",
        "Indigenous Community Studies",
        "First Nations Social Science",
        "Aboriginal Social Structure",
        "Torres Strait Islander Community",
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
    citation_style="APA",
    reporting_standards={
        "ocap": "原住民数据须遵循 OCAP 原则（所有权、控制权、获取权、占有权）",
        "care": "原住民研究须遵循 CARE 原则（集体性、代理权、互惠、伦理）",
        "community_consent": "社区研究须记录社区同意协议（Community Consent Protocols）",
        "mixed_methods": "混合方法研究须报告定量与定性数据整合策略",
    },
    conventions=(
        "社区研究须遵循社区同意协议（Community Consent Protocols）",
        "社会结构分析须考虑部落联盟与土地权传统",
        "定量调查须考虑社区规模与代表性限制",
        "民族志描述须避免刻板印象，尊重文化自主表述",
    ),
    key_venues=(
        "Australian Aboriginal Studies",
        "Aboriginal History",
        "Journal of Indigenous Policy Research",
        "Pacific Affairs",
        "AIATSIS Research Publications",
        "Australian Indigenous Studies",
    ),
    units_and_formulas_notes=(
        "人口统计数据须注明原住民归属分类（ABS 分类法）与统计地域（如 RGC）",
        "社区规模以户（n）与个体（n）分别计量，代表性须说明抽样方法与响应率（%）",
        "社会网络分析须报告节点数、边数与网络密度，中心性指标须注明计算方法",
        "民族志引语须标注说话者（经匿名化）、语言与翻译者，文化敏感内容须标注可公开性等级",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "SPSS", "R", "Stata", "JASP", "SurveyMonkey", "Qualtrics", "Google Forms", "Microsoft Excel", "EndNote", "AIATSIS", "QGIS", "Tableau", "Microsoft Power BI", "Adobe Lightroom", "Canva", "Zoom", "Microsoft OneNote", "ATLAS.ti", "Morpheus"),
    category="法学",
    databases=("OpenAlex",),
)
