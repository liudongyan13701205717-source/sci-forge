"""农村发展学科论文支持：乡村治理、产业与减贫研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="rural_development",
    aliases=(
        "rural_development",
        "农村发展",
        "rural",
        "乡村",
        "乡村振兴",
        "rural poverty",
        "agricultural extension",
        "乡村治理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methodology（调研/计量方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（乡村案例）",
            "analysis（机制/政策分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与文献综述）",
            "evidence synthesis（政策证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "survey": "抽样、量表信效度、样本量须完整",
        "policy_evaluation": "DID、RDD 或 PSM 方法须说明识别策略",
        "household_data": "贫困线口径与人口学变量须定义",
    },
    conventions=(
        "货币单位元/年；收入口径须注明（人均/户均）",
        "贫困标准按国家/世界银行/绝对/相对分层给出",
        "样本来源、时间跨度与村/户数量须报告",
        "政策名称与实施年份须准确列出",
        "变量操作化定义须列出",
    ),
    key_venues=(
        "Journal of Rural Studies",
        "World Development",
        "Land Use Policy",
        "China Agricultural Economic Review",
        "中国农村经济",
    ),
    units_and_formulas_notes=(
        "贫困发生率 %；Gini 系数；收入弹性",
        "土地面积亩/公顷须注明换算",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "SPSS", "EViews", "ArcGIS", "QGIS", "NVivo", "MAXQDA", "MATLAB", "Python Pandas", "Google Earth Engine", "Sentinel 2 Satellite Imagery", "China Household Financial Survey CHFS", "China Labor–Family Panel Studies CLPS", "World Bank PovcalNet", "World Bank DataBank", "FAOSTAT", "National Bureau of Statistics Data", "Redcap Survey System", "Qualtrics"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
