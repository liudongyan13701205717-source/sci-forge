"""城市规划学科论文支持：城市设计与空间规划体裁、APA 引用样式与规划制图记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="urban_planning",
    aliases=("urban planning", "城市规划", "城市设计", "城市空间规划", "建成环境规划",
             "city planning", "urban design", "town planning"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与规划问题）",
            "data and methods（数据、设计与分析）",
            "results（空间方案与评价结果）",
            "discussion（规划机理与设计意义）",
            "references",
        ),
        "design_study": (
            "abstract",
            "introduction",
            "site and brief（场地与设计任务）",
            "design proposal（设计方案）",
            "evaluation（方案评价）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；城市规划期刊多用 APA/Chicago）",
    reporting_standards={
        "spatial_analysis": "空间分析须报告坐标系、空间单元与分析工具",
        "design_documentation": "设计方案须报告用地、指标与制图比例",
        "simulation": "仿真研究须报告模型参数、边界条件与验证",
        "survey": "调查研究遵循 AAPOR 报告规范",
    },
    conventions=(
        "用地分类须采用国标或明确分类体系",
        "规划指标（容积率、绿地率、路网密度）须给出计算口径",
        "制图须注明比例尺与指北针",
        "数据年份与来源须交代",
        "方案评价标准须明确",
    ),
    key_venues=(
        "Journal of the American Planning Association",
        "Urban Studies",
        "Landscape and Urban Planning",
        "Cities",
        "Environment and Planning B",
        "Journal of Urban Design",
    ),
    units_and_formulas_notes=(
        "用地面积用 ha/km²；容积率 (FAR) 用无量纲比",
        "路网密度用 km/km²；绿地率用 %",
        "距离用 m/km；建筑高度用 m",
        "制图比例尺用 1:N；坐标用 CGCS2000 或注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS Pro", "QGIS", "AutoCAD Civil 3D", "SketchUp", "Rhino", "Grasshopper", "CityEngine", "DepthmapX (Space Syntax)", "VISSIM", "TransCAD", "ENVI-met", "Adobe Illustrator", "Adobe Photoshop", "Maptitude", "GeoDa", "Python (geopandas)", "R (sf)", "SPSS", "Tableau", "Stata"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
