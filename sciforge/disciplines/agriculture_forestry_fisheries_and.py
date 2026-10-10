"""Agriculture, forestry, fisheries and 学科论文支持：农林牧渔与土地利用综合体裁、Elsevier numbered 与土地利用注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agriculture_forestry_fisheries_and",
    aliases=(
        "agriculture forestry fisheries and",
        "农林牧渔",
        "农林牧渔业",
        "agriculture forestry and fisheries",
        "land use and rural development",
        "土地利用与农村发展",
        "农林牧渔综合",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "study area and data",
            "materials and methods",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "land_use_change": (
            "abstract",
            "introduction",
            "spatial-temporal analysis",
            "drivers",
            "implications",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope",
            "findings",
            "research gaps",
            "references",
        ),
    },
    citation_style="Elsevier numbered 或 APA 7（农林牧渔多刊遵循 Elsevier）",
    reporting_standards={
        "spatial": "空间分辨率、坐标系统与投影须给出",
        "time_series": "土地利用变化序列须给出起止年份与变化率",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "field_study": "调查点位数、取样密度与重复数须报告",
    },
    conventions=(
        "研究区地理位置、行政归属、经纬度范围须完整给出",
        "土地利用分类须遵循 FAO 或 GB/T 官方标准；给出制图比例尺",
        "数据来源（FAOSTAT、USDA、WorldFish）须标注版本与年份",
        "生态指标（NPP、NDVI、生物量）须给出计算式与阈值",
    ),
    key_venues=(
        "Agriculture, Ecosystems & Environment",
        "Land Use Policy",
        "Forest Ecology and Management",
        "Aquaculture",
        "Aquaculture International",
        "Journal of Agricultural and Rural Development Studies",
        "Agricultural Systems",
    ),
    units_and_formulas_notes=(
        "土地利用面积用 km² 或 ha；变化率 %",
        "产量 t/ha；渔获 kg/t 或 g/mesh",
        "生态指标（NPP/NDVI/生物量）单位须明确",
        "公式用 amsmath；显示公式仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AIMS", "LEAP", "Global Forest Watch", "LandSIT", "CropScape", "DSSAT", "APSIM", "SWAT", "HEC-RAS", "InVEST", "ArcGIS", "QGIS", "Google Earth Engine", "Global Fishing Watch", "FAO Fishstat", "WorldFish Center", "World Fisheries", "FishStat-Commander", "R", "Python", "MATLAB"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "FAOSTAT", "WorldFish", "USDA ERS", "NASA POWER", "HLS"),
)
