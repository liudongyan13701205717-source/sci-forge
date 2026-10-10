"""城乡规划学科论文支持：规划评价/空间优化体裁、Landscape and Urban Planning 引用样式与规划记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="town_and_country_planning",
    aliases=("town_and_country_planning", "城乡规划", "城市规划", "乡村规划", "国土空间规划",
             "urban planning", "rural planning", "spatial planning", "土地利用规划"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与规划问题）",
            "methods（空间分析与模型方法）",
            "results（规划方案与评价）",
            "discussion（机制与政策建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例城市/乡村）",
            "analysis（空间结构与功能分析）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "data_sources": "数据来源与年份须注明",
        "spatial_methods": "空间分析方法（如空间计量、CA-马尔科夫链）须说明",
        "accuracy": "分类精度与几何精度须报告（Kappa 系数）",
        "stakeholder_involvement": "公众参与方式须声明",
    },
    conventions=(
        "土地利用类型遵循国标分类（GB/T 21010）",
        "面积单位：公顷（hm²）或平方公里（km²）",
        "密度单位：人/平方公里 或 栋/公顷",
        "坐标系统一用 CGCS2000 或 WGS-84",
        "规划年限须注明基准年与目标年",
    ),
    key_venues=(
        "Landscape and Urban Planning",
        "Cities",
        "Urban Studies",
        "Habitat International",
        "Land Use Policy",
    ),
    units_and_formulas_notes=(
        "面积单位：km² 或 hm²",
        "人口密度单位：人/km²",
        "绿化覆盖率单位：%",
        "公式用 amsmath 排版；空间自相关指数（Moran's I）须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "SuperMap", "MapInfo", "ENVI", "ERDAS Imagine", "Global Mapper", "Cavalier", "Autodesk AutoCAD", "SketchUp", "Rhino 3D", "Grasshopper", "MATLAB", "Python", "SPSS", "Origin Pro", "STATA", "R", "Google Earth Pro", "Drone Deploy"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
