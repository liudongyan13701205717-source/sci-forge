"""自然地理与环境地球科学学科论文支持：地貌/气候/水文体裁、AGU 引用样式与地球系统记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="physical_geography_and_environmental_geoscience",
    aliases=("physical_geography_and_environmental_geoscience", "自然地理学", "环境地球科学",
             "physical geography", "environmental geoscience", "地貌学", "geomorphology",
             "气候学", "climatology", "水文", "hydrology", "全球变化", "global change"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与环境问题）",
            "methodology（观测/遥感/模型方法）",
            "results（时空分布与量化）",
            "discussion（机理与人类活动影响）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域/事件描述）",
            "analysis（过程与驱动力）",
            "results（结果与不确定性）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（自然地理理论）",
            "evidence synthesis（关键观测与模型综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="AGU 样式（编号制；EGS/JGR 遵循 AGU 规范）",
    reporting_standards={
        "remote_sensing": "遥感研究遵循 ESRI Sentinel/Landsat 数据引用规范",
        "climate_model": "气候模型遵循 CMIP6 命名与数据规范",
        "field_measurement": "野外测量遵循 ISO 17025 计量校准规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_availability": "数据可用性声明须给出公开仓库与 DOI"
    },
    conventions=(
        "空间数据（坐标、投影、分辨率）须完整报告（WGS84/UTM 等）",
        "时间数据须注明时区（UTC）与年份格式",
        "遥感产品等级（Level-1/2A/2B）须区分标注",
        "模型参数（网格、时段、初始条件）须完整",
        "土地利用/土地覆盖（LULC）分类等级与来源须说明"
    ),
    key_venues=(
        "Earth-Science Reviews",
        "Global and Planetary Change",
        "Earth Surface Processes and Landforms",
        "Journal of Geophysical Research: Atmospheres",
        "Climatic Change",
        "Environmental Modelling & Software"
    ),
    units_and_formulas_notes=(
        "海拔用 m；经纬度用 °WGS84；时间用 UTC/ISO 8601",
        "温度用 °C 或 K；降水用 mm；风速用 m/s",
        "公式用 amsmath；通量、热平衡方程形式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "时空分辨率须与不确定性一并报告"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "GRASS GIS", "Google Earth Engine", "ENVI", "SNAP (Sentinel)", "R (sf/sp)", "Python (GeoPandas, Rasterio)", "MATLAB", "HEC-RAS", "SWMM", "MODFLOW", "Landsat 8/9 遥感平台", "Sentinel-2 遥感平台", "MODIS (NASA)", "GHCN 全球气候观测网络", "ERA5 再分析数据集", "IPCC 评估报告数据", "Copernicus 地球观测计划", "野外全站仪（RTK 测量）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "ESRI", "NCEI 气象数据库"),
)
