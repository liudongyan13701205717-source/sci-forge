"""Agricultural business/agribusiness 学科论文支持：农业经济/农业企业/供应链体裁、APA 引用样式与农业经济注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agricultural_businessagribusiness",
    aliases=("agricultural business/agribusiness", "农业经济", "农业企业",
             "农业经营", "农业商业", "农业经济管理", "agribusiness",
             "agricultural economics", "农业供应链", "农村经济"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "theory and hypotheses",
            "methodology",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context and background",
            "case description",
            "analysis",
            "findings",
            "implications",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy context",
            "data and method",
            "results",
            "implications",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_study": "案例研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "empirical": "实证研究遵循 APA 与 AAAAM 惯例",
        "survey": "农户调查遵循 AAPOR 报告规范",
    },
    conventions=(
        "农业经济术语全文一致：作物/农户/供应链/补贴/价格等核心概念须定义",
        "数据来源（USDA/FAO/国家统计局）须完整标注；口径须一致",
        "样本量、显著性水平、置信区间须完整给出；效应量须报告",
        "面板数据/时间序列须说明估计方法（FE/RE/OLS/ARIMA）",
        "案例研究须说明案例选择理由与三角验证方法",
    ),
    key_venues=(
        "American Journal of Agricultural Economics",
        "Agricultural Economics",
        "Agricultural Systems",
        "Food Policy",
        "Journal of Agribusiness",
        "Journal of Rural Studies",
        "Review of Agricultural Economics",
    ),
    units_and_formulas_notes=(
        "价格/产量/面积用国际单位（USD, t, ha）并注明统计口径",
        "样本量、显著性水平、置信区间须完整给出",
        "效应量报告 Cohen's d/η²/R² 等标准指标",
        "时间序列数据注明采样周期与季节性；名义/实际口径须区分",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Office (Excel)", "SPSS", "Stata", "R", "Python", "Tableau", "Power BI", "SAP", "Oracle", "Coupa", "Salesforce", "HubSpot", "Granular", "John Deere Operations Center", "FarmDrive", "AFS Enterprise", "ArcGIS", "QGIS", "USDA Data Hub", "FAOSTAT", "Weather Underground", "Bloomberg Terminal", "NVivo", "Qualtrics", "SurveyMonkey", "Google Forms", "Asana", "Trello"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "SSRN"),
)
