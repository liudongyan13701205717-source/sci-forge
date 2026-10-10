"""餐饮业学科论文支持：餐饮管理/运营成本/食品安全/服务设计体裁与引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="catering",
    aliases=(
        "catering",
        "food service management",
        "F&B management",
        "banqueting",
        "hospitality management",
        "餐饮业",
        "餐饮管理",
        "餐饮服务",
        "宴会服务",
        "酒店管理",
        "食品饮料管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（行业背景与研究问题）",
            "literature review（理论与实证综述）",
            "method（抽样、问卷与数据分析）",
            "results（描述统计与假设检验）",
            "discussion（管理含义与理论贡献）",
            "conclusions",
            "references",
        ),
        "case study": (
            "abstract",
            "case description（门店/企业概况）",
            "data and method（财务、运营与客户数据）",
            "findings（成本、效率与客户体验）",
            "management implications",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "conceptual framework",
            "main developments",
            "future research directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "cost": "食品成本率（FCR）与人力成本率须报告并说明统计口径",
        "yield": "出成率（yield）须注明去皮/修整损耗与克重换算",
        "safety": "食品安全须按 HACCP 关键控制点报告温度与时间",
        "metrics": "客单价、翻台率定义须明确（时段、统计范围）",
        "satisfaction": "满意度调查须说明抽样方法、量表（Likert）与信度（Cronbach α）",
    },
    conventions=(
        "餐饮成本须区分食品成本率 FCR 与人力成本率；报告口径一致",
        "出成率（yield）须注明去皮/修整损耗并给出克重换算",
        "食品安全须按 HACCP 关键控制点报告温度与时间",
        "客单价与翻台率定义须明确（时段、统计范围）",
        "满意度调查须说明抽样方法与量表（Likert）并报告信度系数",
    ),
    key_venues=(
        "Cornell Hospitality Quarterly",
        "International Journal of Hospitality Management",
        "International Journal of Contemporary Hospitality Management",
        "British Food Journal",
        "Journal of Foodservice Business Research & Marketing",
        "Food Quality and Safety",
    ),
    units_and_formulas_notes=(
        "成本率用 %；客单价用 元/位 或 元/桌",
        "翻台率用 次/日；出成率用 %",
        "温度用 ℃；时间用 min/h",
        "财务比率须注明报告期与统计范围",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Toast POS", "Square for Restaurants", "MarketMan", "OpenTable", "Resy", "Marmalade 365", "SevenRooms", "Thermapen ONE 温度计", "TempFury 无线探针温度计", "Hygiena ATP 荧光检测仪", "D2Food 菜单设计", "Orderkey KDS 厨房显示系统", "BlueCart 餐饮分析", "Microsoft Power BI", "Tableau", "Microsoft Excel", "Molecul 厨房库存管理", "Zelle 食品安全追溯系统", "Yelp 评价分析", "HACCP 数字化平台"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
