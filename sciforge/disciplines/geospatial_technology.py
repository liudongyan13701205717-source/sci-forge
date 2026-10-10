"""地理空间技术学科论文支持：GIS 技术、空间信息工程、位置智能与云地图。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geospatial_technology",
    aliases=(
        "geospatial_technology",
        "地理空间技术",
        "geospatial_technologies",
        "空间信息技术",
        "GIS_technologies",
        "地理信息技术",
        "spatial_information_science",
        "空间信息科学",
        "location_intelligence",
        "位置智能",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（系统设计与技术实现）",
            "results（结果与性能验证）",
            "discussion（讨论与推广）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（应用场景背景）",
            "analysis（系统实现与分析）",
            "results（结果与效果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（技术综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 或 APA 7（视方向而定）",
    reporting_standards={
        "architecture": "系统须报告架构、模块、数据流与接口协议",
        "validation": "精度/性能验证须报告 RMSE、样本量与检验方法",
        "data": "数据须报告来源、精度、时空覆盖与许可",
    },
    conventions=(
        "坐标系、投影、高程基准与时间基准须显式",
        "系统架构用 UML 图；流程图用统一符号",
        "API/协议用 WFS/WMS/OGC 标准命名",
        "性能指标报告：QPS、延迟、吞吐、并发",
        "算法报告复杂度、收敛判据与失败情形",
    ),
    key_venues=(
        "ISPRS International Journal of Geo-Information",
        "International Journal of Geographical Information Science",
        "Transactions in GIS",
        "Computers, Environment and Urban Systems",
        "Location-Based Services (Springer)",
    ),
    units_and_formulas_notes=(
        "坐标用 m 或 °；投影坐标用 m",
        "空间分辨率用 m/pixel；时间分辨率用 s/d/yr",
        "性能指标用 QPS、ms、MB/s、并发数",
        "精度用 RMSE 或位置精度 m",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS Pro", "PostGIS", "GDAL/OGR", "GeoServer", "MapServer", "Cesium", "OpenLayers", "Leaflet", "Mapbox GL", "Google Maps API", "Esri ArcGIS Online", "FME (Feature Manipulation Engine)", "GeoPandas", "Python", "Jupyter Notebook", "R", "SNAP", "SAGA GIS", "OpenStreetMap"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
