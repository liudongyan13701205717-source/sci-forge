"""美容服务学科论文支持：服务业管理/美容行业研究体裁、APA 引用样式与行业研究约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cosmetic_services",
    aliases=(
        "美容服务", "美容行业", "美容服务业", "Cosmetic services",
        "Beauty Services", "Beauty Industry", "Cosmetology Services",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "industry_report": (
            "行业概述",
            "市场规模与趋势",
            "竞争格局",
            "消费者行为分析",
            "行业挑战与机遇",
            "结论与建议",
        ),
        "service_design": (
            "服务概述",
            "客户需求分析",
            "服务流程设计",
            "质量控制",
            "效果评估",
        ),
    },
    citation_style="APA 第 7 版",
    reporting_standards={
        "service_metrics": "服务质量须使用标准化模型评估（如 SERVQUAL）",
        "customer_satisfaction": "客户满意度须使用标准化量表（如 CSAT、NPS）",
        "regulatory_compliance": "须符合当地美容行业法规",
        "safety": "涉及操作安全的须符合 HACCP 或相关安全标准",
    },
    conventions=(
        "行业数据须注明来源（如 Statista、Euromonitor）",
        "客户满意度量表须注明版本与信效度",
        "服务流程描述须标注关键触点（customer touchpoints）",
        "市场规模数据须注明汇率与计价单位",
        "行业案例须注明地区与时间范围",
    ),
    key_venues=(
        "Journal of Marketing Management",
        "Journal of Retailing and Consumer Services",
        "International Journal of Cosmetic Science",
        "Cosmetic, Toiletry & Fragrance Journal",
        "Beauty Industry Insights",
        "国际美容化妆品科学技术学会",
    ),
    units_and_formulas_notes=(
        "市场份额以百分比表示",
        "客户满意度使用百分制或 1-10 标度",
        "财务指标使用当地货币并注明汇率",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("VISIA（皮肤分析仪）", "Cutometer（皮肤弹性质测仪）", "Corneometer（皮肤水分计）", "Cosmelight（肤色分析仪）", "MoxiLab（皮肤老化分析系统）", "PhisioDerm（皮肤微生物分析）", "DermDetect（皮肤图像分析）", "Skintific（皮肤检测仪）", "Beauty Salon Management System (BSMS)", "SalonBox（美容院管理软件）", "Timely（美容院预约系统）", "Zenoti（SPA 管理系统）", "FreshBooks（美容院财务软件）", "Google Analytics", "SurveyMonkey（客户满意度调查）", "Qualtrics", "Tableau（行业数据可视化）", "SPSS", "NVivo（质性分析）", "BeautyTech（美容技术平台）"),
    category="管理学",
    databases=("Scopus", "EBSCO", "ProQuest", "中国知网"),
)
