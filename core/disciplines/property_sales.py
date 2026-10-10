"""物业销售学科论文支持：案例/实证体裁、APA 引用样式与交易数据披露注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="property_sales",
    aliases=(
        "property_sales",
        "物业销售",
        "房地产销售",
        "房产经纪",
        "Real estate sales",
        "物业营销",
        "物业经纪",
        "物业估价",
        "房地产经纪",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与市场）",
            "methodology（研究设计）",
            "results（实证结果）",
            "discussion（市场启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（交易案例描述）",
            "analysis（销售与定价分析）",
            "results（成交结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与政策综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；中文期刊亦可接受 GB/T 7714）",
    reporting_standards={
        "empirical": "实证研究遵循 DSR 声明",
        "case_study": "案例研究遵循 DSR-CASE 规范",
        "valuation": "估价须遵循 USPAP 或 RICS Red Book",
        "survey": "问卷研究遵循 AERA/ASA 问卷报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "交易金额、面积与价格单位须统一并注明币种",
        "可比案例调整须逐项列出调整项与依据",
        "客户与业主个人信息须脱敏",
        "数据集来源、覆盖时段与采样口径须声明",
        "销售转化率等指标须给出计算公式",
    ),
    key_venues=(
        "Journal of Property Valuation and Cost Control",
        "Real Estate Economics",
        "Journal of Real Estate Finance",
        "Journal of Real Estate Research",
        "China Real Estate Journal",
        "Journal of Business Venturing",
    ),
    units_and_formulas_notes=(
        "货币单位须注明（元、万元、USD、HKD）",
        "面积单位须注明（平方米、亩、平方英尺）",
        "价格须区分单价与总价，并说明是否含税",
        "公式用 amsmath；估值模型假设须列出",
        "收益率与回报率须说明折现与年化口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("MRV", "Argus", "CREA", "Cushman & Wakefield REIS", "CoStar", "RISMedia", "Property Guru", "Zillow Research API", "Zillow Zestimate", "REIDIN", "CoreLogic", "ArcGIS", "QGIS", "PostGIS", "SPSS", "R", "Stata", "Excel", "SAS", "Python"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
