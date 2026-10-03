"""海洋生物学论文支持：海洋生态、海洋生物多样性、珊瑚礁、深海生物学、渔业科学。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="marine_biology",
    aliases=("marine_biology", "海洋生物学", "ocean_biology", "marine_ecology"),
    paper_types={
        "research": ("abstract", "introduction", "study site", "methods", "results", "discussion", "conclusions", "references"),
        "ecology": ("abstract", "introduction", "site description", "sampling methods", "community analysis", "results", "discussion", "conclusions", "references"),
        "fisheries": ("abstract", "introduction", "stock assessment", "methods", "results", "management implications", "conclusions", "references"),
    },
    citation_style="Marine Ecology Progress Series style（编号），如 [1]；或 (Author Year)",
    reporting_standards={
        "sampling": "采样须报告站位坐标/深度、采样工具、网目尺寸与拖曳时间",
        "taxonomy": "分类鉴定须引权威分类数据库（WoRMS/AlgaeBase）、凭证标本存放地",
        "environmental": "环境参数须报告温度/盐度/溶解氧/pH/叶绿素a的测量方法与精度",
        "acoustics": "声学调查须报告频率、校准方法与目标强度模型",
    },
    conventions=(
        "物种名用拉丁学名（斜体），首次出现给中文名",
        "深度用 m（depth in meters）",
        "站位/样方编号用标准格式（Stn. A1/Quadrat 01）",
        "图：空间分布图须含等深线与比例尺",
        "群落分析用标准指数（Shannon/Simpson/Chao1）",
    ),
    key_venues=(
        "Marine Ecology Progress Series",
        "Marine Biology",
        "Coral Reefs",
        "Deep-Sea Research Part I/II",
        "ICES Journal of Marine Science",
    ),
    units_and_formulas_notes=(
        "深度用 m；距离用 km 或 nm（nautical miles）",
        "温度用 °C；盐度用 PSU（Practical Salinity Units）",
        "叶绿素a用 μg/L 或 mg/m²",
        "生物量用 g/m² 或 kg/km²",
        "丰度用 ind/m²（个体密度）或 ind/haul（每网次）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("R", "MATLAB", "ArcGIS", "CTD 采样仪"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Zenodo"),
)
