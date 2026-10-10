"""地理信息科学学科论文支持：GIScience、空间数据科学与时空信息理论。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geoinformatics",
    aliases=(
        "geoinformatics",
        "地理信息科学",
        "geo-informatics",
        "geographic_information_science",
        "GIScience",
        "spatial_informatics",
        "空间信息学",
        "spatial_data_science",
        "空间数据科学",
        "spatiotemporal_data_analysis",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（理论模型与方法）",
            "results（结果）",
            "discussion（讨论与理论贡献）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；括号式）",
    reporting_standards={
        "model": "空间模型须报告数学形式、参数、假设与验证",
        "data": "数据须报告来源、精度、时空覆盖与许可",
        "algorithm": "算法须报告复杂度、收敛条件与鲁棒性测试",
    },
    conventions=(
        "数学符号与英文缩写统一；首次出现给全称",
        "坐标系、投影、分辨率与精度须显式说明",
        "图表须自明：图注含单位、样本量与图例",
        "算法伪代码用 Algorithm 环境编号",
        "理论贡献须与已有工作对比说明",
    ),
    key_venues=(
        "GeoInformatica",
        "International Journal of Geographical Information Science",
        "Transactions in GIS",
        "International Journal of Geoinformation",
        "ISPRS International Journal of Geo-Information",
    ),
    units_and_formulas_notes=(
        "坐标用 m 或 °；投影坐标用 m",
        "空间分辨率用 m/pixel；时间分辨率用 s/d/yr",
        "距离用 km；面积用 km²/ha/m²",
        "统计检验报告 p 值、效应量与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS Pro", "PostGIS", "GDAL/OGR", "GeoPandas", "Python", "R", "GRASS GIS", "GeoServer", "MapServer", "Whitebox GEP", "SNAP", "SAGA GIS", "FME", "Cesium", "OpenLayers", "Jupyter Notebook", "GeoDa", "MATLAB", "TerraScan"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
