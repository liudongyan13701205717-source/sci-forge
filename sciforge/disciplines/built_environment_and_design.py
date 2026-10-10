"""建成环境与规划设计（Built environment and design）：城市尺度设计、规划与评价方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="built_environment_and_design",
    aliases=("built_environment_and_design", "建成环境与规划", "Built environment and design",
             "urban design", "城市设计", "urban planning", "城市规划",
             "spatial planning", "空间规划", "landscape architecture", "景观设计"),
    paper_types={
        "research": (
            "abstract",
            "introduction（城市/区域背景与研究问题）",
            "study area description（范围、数据年份与获取方式）",
            "methodology（GIS 分析、形态指标计算、空间句法、实证模型）",
            "results（指标图、模型拟合、情景对比）",
            "discussion（与规划实践/既有文献对话）",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7th（规划学系）或 Harvard 样式",
    reporting_standards={
        "gis_analysis": "数据源（OpenStreetMap/Landsat/普查）与年表写明；投影与分辨率标注",
        "morphology": "形态指标（容积率、密度、间距比）给计算口径与软件版本",
        "simulation": "情景对比给情景假设（新增量、用途变化）与边界条件",
        "social_data": "问卷调查给样本量、回收率、信效度；多水平模型给随机效应设定",
    },
    conventions=(
        "地图给指北针、比例尺与图例；行政边界与统计区划口径一致",
        "时间序列给起止年份；率值类指标给基数口径（每万人/每平方公里）",
        "引用规划文本给条款号；国际比较统一计量单位（m²、USD/当地货币标注）",
    ),
    key_venues=(
        "Landscape and Urban Planning",
        "Urban Studies",
        "Journal of Urban Design",
        "Environment and Planning B: Planning and Design",
        "Cities",
        "Urban Forestry & Urban Greening",
    ),
    units_and_formulas_notes=(
        "距离 m、面积 km²；密度人/km²；建成区占比 %；碳排 tCO₂e/万m²",
        "NDVI 等遥感指数给波段组合；空间句法集成值（integration）给深度与半径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS Pro", "GlobalMapper", "MapInfo", "Fusion Tables", "Google Earth Engine", "ENVI", "ERDAS Imagine", "DepthmapX (Space Syntax)", "TransCAD", "LEAP", "UrbanSim", "AnyLogic", "MATLAB", "R (sf/spdep)", "Python (geopandas/rasterio)", "Blender", "Revit", "SketchUp", "D5 Render", "Lumion", "Ladybug Tools", "Design Builder", "Energy Plus", "CityEngine"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Scopus"),
)
