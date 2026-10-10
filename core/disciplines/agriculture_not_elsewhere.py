"""Agriculture not elsewhere 学科论文支持：农业未分类方向体裁、ASA/Elsevier 与综合农业注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agriculture_not_elsewhere",
    aliases=(
        "agriculture not elsewhere",
        "农业其他",
        "农业未分类",
        "agriculture NEC",
        "农学其他",
        "农业综合",
        "agricultural other",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods",
            "results",
            "discussion",
            "conclusions",
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
        "field_study": (
            "abstract",
            "introduction",
            "site and data",
            "methods",
            "findings",
            "references",
        ),
    },
    citation_style="ASA-CSSA-SSSA style 或 Elsevier numbered",
    reporting_standards={
        "trial": "田间试验设计（随机区组/裂区）、重复数与小区面积须给出",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data": "实验数据遵循 FAIR 与 AAAAM 惯例",
        "field": "调查点数、取样密度与重复数须报告",
    },
    conventions=(
        "研究区地理位置、行政归属、经纬度范围须完整给出",
        "品种名给正式登记名；转基因材料注明转化事件",
        "农艺性状须给出测定方法与仪器型号",
        "单位用 SI（kg/ha、t/ha、mm）；养分按 N-P2O5-K2O 折算",
    ),
    key_venues=(
        "Agriculture (MDPI)",
        "Sustainability",
        "Journal of Agriculture and Food Science",
        "Journal of Agricultural Science",
        "Agricultural Systems",
        "Land Use Policy",
        "Journal of Rural Studies",
    ),
    units_and_formulas_notes=(
        "产量 t/ha 或 kg/ha；面积 ha 或 km²",
        "生态指标（NDVI/NPP）须给出计算式与阈值",
        "统计显著性 p 值与效应量并列报告",
        "公式用 amsmath；显示公式仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("DSSAT", "APSIM", "STICS", "AquaCrop", "SWAT", "InVEST", "ArcGIS", "QGIS", "Google Earth Engine", "Sentinel-2", "Landsat", "Drone DJI Phantom", "R", "Python", "MATLAB", "SPSS", "ImageJ", "Meteostat", "FAOSTAT", "World Bank WDI"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "FAOSTAT", "NASA POWER", "HLS", "World Bank Open Data"),
)
