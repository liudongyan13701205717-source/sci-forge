"""制图学学科论文支持：地图制图/地理信息系统/空间数据体裁与引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cartography",
    aliases=(
        "cartography",
        "map making",
        "map design",
        "geographic information science",
        "geospatial science",
        "制图学",
        "地图学",
        "地图制图",
        "地理信息系统",
        "空间信息科学",
        "测绘",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（制图问题与空间数据来源）",
            "data and methods（数据获取、处理与空间模型）",
            "results（制图结果与精度评价）",
            "discussion（制图综合、表达与局限）",
            "conclusions",
            "references",
        ),
        "methods": (
            "abstract",
            "introduction",
            "method（算法与制图模型）",
            "experiments（数据集、评价指标与实现）",
            "results and discussion",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical development",
            "main developments（按主题综述）",
            "open challenges",
            "references",
        ),
    },
    citation_style="APA 7 或 Elsevier 样式；引用须含数据集 DOI 与坐标参考系统信息",
    reporting_standards={
        "projection": "地图须标注投影、坐标系（EPSG 代码）、比例尺与指北方向",
        "datum": "基准与坐标系转换须说明（WGS84 / CGCS2000）及转换参数",
        "generalization": "制图综合规则须可复现；标注避让策略须说明",
        "sources": "数据源须注明生产者、年份与更新时效",
        "accuracy": "精度评价须报告 RMSE 与残差分布",
    },
    conventions=(
        "地图须标注投影、坐标系（EPSG 代码）、比例尺与指北方向",
        "坐标系转换须说明基准（WGS84 / CGCS2000）与转换参数",
        "图例须与地图要素一一对应；配色使用色盲友好方案",
        "数据源须注明生产年份与更新时效；引用须含数据集 DOI",
        "制图综合（概括）规则须可复现；标注避让策略须说明",
    ),
    key_venues=(
        "Cartography and Geographic Information Science",
        "International Journal of Geographical Information Science",
        "Photogrammetric Engineering and Remote Sensing",
        "ISPRS Journal of Photogrammetry and Remote Sensing",
        "The Cartographic Journal",
        "Journal of Maps",
    ),
    units_and_formulas_notes=(
        "坐标用度分秒或十进制度数，须标注坐标参考系统",
        "高程用 m；距离用 km；面积用 km²",
        "比例尺用 1:n 形式；分辨率用 m/px",
        "引用空间数据集须附 DOI 与坐标参考系统",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS Pro", "QGIS", "AutoCAD Map 3D", "MapInfo", "Global Mapper", "GRASS GIS", "PostGIS", "sf (R)", "GeoPandas (Python)", "OpenLayers", "Mapbox Studio", "Mapnik", "ERDAS IMAGINE", "ENVI", "LAStools", "Orfeo ToolBox", "Google Earth Engine", "MMQGIS 制图综合", "Mapus 三维建模平台", "PDAL 点云处理库"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
