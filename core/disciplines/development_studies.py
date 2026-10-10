"""发展研究学科论文支持：发展政策、国际发展与发展评估研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="development_studies",
    aliases=(
        "development_studies", "发展研究", "发展政策研究",
        "development policy", "发展政策",
        "international development", "国际发展",
        "economic development", "经济发展",
        "development economics", "发展经济学",
        "sustainable development", "可持续发展",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（发展问题与政策背景）",
            "method（数据分析、模型设定与实证策略）",
            "results（发展指标与政策效果）",
            "discussion（政策含义与改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context（案例国家/地区背景）",
            "analysis（发展路径与政策分析）",
            "conclusion（经验总结）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence summary（证据总结）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "empirical": "模型设定与识别策略须明确（IV、DID、RDD等）",
        "data": "数据来源须注明（世界银行、IMF、UN等）",
        "statistics": "统计检验须注明效应量与置信区间",
        "ethical": "涉及敏感议题须声明伦理考虑",
    },
    conventions=(
        "发展指标须明确定义（GDP、Gini、HDI等）",
        "政策评估须区分干预组与对照组",
        "数据来源须标注年份与机构",
        "统计检验注明显著性水平与聚类稳健标准误",
        "异质性分析须报告不同群体差异",
    ),
    key_venues=(
        "World Development",
        "Journal of Development Economics",
        "Development and Change",
        "Journal of Development Studies",
        "Oxford Development Studies",
        "World Bank Economic Review",
    ),
    units_and_formulas_notes=(
        "GDP用 美元（购买力平价）表示",
        "Gini 系数用 0-1 范围表示",
        "HDI 用 0-1 范围表示",
        "统计检验注明 t/F/z 值、p 值与 95% CI",
        "政策效果用百分点（pp）表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R (RStudio)", "Python (pandas, statsmodels)", "MATLAB", "SPSS", "EViews", "Origin", "GIS (ArcGIS, QGIS)", "Tableau", "Power BI", "Google Earth", "NVivo", "Atlas.ti", "RefWorks", "EndNote", "Zotero", "World Bank Data", "IMF Data", "UN Data", "Our World in Data"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI", "World Bank Open Knowledge Repository"),
)
