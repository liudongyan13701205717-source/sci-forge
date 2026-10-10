"""Cultural geography 学科论文支持：文化空间/景观/地域差异体裁、地理学报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cultural_geography",
    aliases=(
        "cultural_geography",
        "cultural geography",
        "文化地理学",
        "文化景观",
        "文化空间",
        "regional culture",
        "区域文化",
        "cultural landscape",
        "geography of culture",
        "空间文化",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "theoretical framework（理论框架）",
            "methods（研究方法）",
            "findings（研究发现）",
            "discussion（讨论）",
            "conclusions",
            "references",
        ),
        "spatial_analysis": (
            "abstract",
            "introduction",
            "study area（研究区域）",
            "data and methods（数据与方法）",
            "spatial patterns（空间格局）",
            "drivers analysis（驱动机制）",
            "conclusions",
            "references",
        ),
        "ethnographic": (
            "abstract",
            "introduction",
            "fieldwork（田野调查）",
            "cultural practices（文化实践）",
            "analysis（分析）",
            "discussion",
            "references",
        ),
    },
    citation_style="Chicago 样式（人文地理学遵循 Chicago 规范）",
    reporting_standards={
        "spatial": "空间分析须报告投影坐标系、比例尺与数据分辨率",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "ethnography": "民族志研究遵循民族志报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "地名用中文正式地名，括注拼音/英文（如 西安 / Xi'an）",
        "空间尺度明确说明（国家级/省级/市级/村级）",
        "地图须标注比例尺、指北针与图例",
        "时间用统一纪年格式，标注统计口径",
        "田野资料须注明采集时间与地点坐标",
    ),
    key_venues=(
        "Journal of Cultural Geography",
        "Environment and Planning D: Society and Space",
        "GeoHumanities",
        "Transactions of the Institute of British Geographers",
        "Annals of the Association of American Geographers",
        "Area",
        "地理研究",
    ),
    units_and_formulas_notes=(
        "距离用 km/m；面积用 km² 或 km²",
        "比例尺用 1:X 或实际距离标注",
        "坐标用 WGS84 或地方投影坐标系",
        "频率/密度须注明分母口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS Pro", "Google Earth Pro", "gvSIG Desktop", "GRASS GIS", "PostGIS", "GeoPandas", "Mapbox", "Leaflet", "OpenLayers", "CartoDB", "OpenStreetMap", "Google Earth Engine", "sf (R spatial package)", "R", "RStudio", "Python", "Tableau", "FME (Feature Manipulation Engine)", "OSGeo Suite", "GDAL/OGR", "Shapely"),
    category="理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Web of Science", "Google Scholar"),
)
