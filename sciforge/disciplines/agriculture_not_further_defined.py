"""Agriculture not further defined 学科论文支持：农业资源与生态综合体裁、Elsevier/ASA 与遥感注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agriculture_not_further_defined",
    aliases=(
        "agriculture not further defined",
        "农业资源",
        "农业生态",
        "agricultural resources",
        "agroecology",
        "农业环境",
        "agronomy resources",
        "农学未定义",
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
        "remote_sensing": (
            "abstract",
            "introduction",
            "data and preprocessing",
            "model and validation",
            "results",
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
    citation_style="Elsevier numbered 或 ASA-CSSA-SSSA style",
    reporting_standards={
        "spatial": "空间分辨率、坐标系统与投影须给出",
        "trial": "田间试验设计、重复数与小区面积须给出",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data": "实验数据遵循 FAIR 与 AAAAM 惯例",
    },
    conventions=(
        "研究区地理位置、行政归属、经纬度范围须完整给出",
        "遥感数据（Sentinel/Landsat/MODIS）须给出获取时间、级别与云量",
        "生态指标（NDVI/NPP/生物量）须给出计算式与阈值",
        "统计显著性 p 值与效应量并列报告",
    ),
    key_venues=(
        "Agricultural Systems",
        "Agriculture, Ecosystems & Environment",
        "Computers and Electronics in Agriculture",
        "Remote Sensing",
        "Agricultural Water Management",
        "Plant and Soil",
        "Ecological Indicators",
    ),
    units_and_formulas_notes=(
        "遥感产品（NDVI/NPP/ET）须给出传感器、光谱波段与计算式",
        "作物模型输入（气象/土壤/管理）须给出数据源与插值方法",
        "面积单位 km² 或 ha；产量 t/ha",
        "公式用 amsmath；显示公式仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("DSSAT", "APSIM", "STICS", "WOFOST", "AquaCrop", "SWAT", "WEPP", "InVEST", "ArcGIS", "QGIS", "Google Earth Engine", "Sentinel-2", "Landsat", "Sentinel-1", "MODIS", "Spectroradiometer ASD FR", "LAI Scanner LiCor", "Plant Spectrometer SPAD-501", "Drone DJI Matrice", "Drone DJI Phantom"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "FAOSTAT", "NASA POWER", "HLS", "USGS Earth Explorer"),
)
