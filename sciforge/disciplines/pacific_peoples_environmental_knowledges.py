"""太平洋人民环境知识学科论文支持：太平洋海洋生态、气候变化、地理空间与原住民环境知识研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pacific_peoples_environmental_knowledges",
    aliases=("Pacific Peoples Environmental Knowledges", "太平洋人民环境知识", "Pacific Environmental Science", "Pacific Marine Studies", "Pacific Climate Studies", "Pacific Remote Sensing", "Pacific Coastal Management", "Pacific Ecological Studies"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ESA / APA 7",
    reporting_standards={
        "k1": "传统环境知识遵循ICCF/ICCRD传统知识保护框架", "k2": "地理空间数据遵循ISO 19115元数据规范", "k3": "观测研究遵循STROBE与系统综述遵循PRISMA"
    },
    conventions=("地理空间数据须标注坐标系（如WGS84）与精度", "传统生态知识须获得原住民社区知情同意并注明归属", "海洋观测须标注采样点经纬度、水深与采集时间", "遥感影像须注明传感器、云量、分辨率与重访周期", "跨文化生态知识须说明本地术语的语义边界"),
    key_venues=("Journal Of Geographical Science", "Ocean & Coastal Management", "Marine Pollution Bulletin", "Ocean Science Journal", "Pacific Remote Sensing", "Coral Reefs"),
    units_and_formulas_notes=("地理坐标使用WGS84或本地投影并注明精度", "水温/盐度使用° C与PSU（实用盐度单位）", "遥感数据须标注传感器型号、空间分辨率与波段", "生态数据须区分原位测量、遥感反演与模型推算三类"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS Pro", "GRASS GIS", "GeoPandas", "PostGIS", "TerraScope", "Global Mapper", "SAGA GIS", "RadarSat", "Sentinel", "Landsat", "MODIS", "OceanSODA", "Argo Float", "OceanBuoy", "CtdSensor", "OceanographicModelTools", "PythOcean", "OceanDataViewer", "Tableau"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
