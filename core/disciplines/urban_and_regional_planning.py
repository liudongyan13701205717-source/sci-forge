"""城乡规划学科论文支持：区域规划与空间治理体裁、APA 引用样式与空间计量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="urban_and_regional_planning",
    aliases=("urban and regional planning", "城乡规划", "区域规划", "国土空间规划", "城市规划与区域规划",
             "regional planning", "spatial planning", "town and country planning"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与规划问题）",
            "data and methods（数据、模型与分析）",
            "results（空间格局与模拟结果）",
            "discussion（规划机理与政策意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case selection（案例与范围）",
            "analysis（空间分析与规划评价）",
            "findings（发现）",
            "discussion（规划建议）",
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
    citation_style="APA 样式（作者-年份；JAPA/Urban Studies 遵循 APA/SAGE 规范）",
    reporting_standards={
        "spatial_analysis": "空间分析须报告坐标系、空间单元与空间权重矩阵",
        "land_use_model": "用地模型须报告参数、校准方法与验证指标",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "policy_analysis": "政策分析须报告政策背景、评估框架与数据来源",
    },
    conventions=(
        "研究尺度与空间单元须明确定义",
        "坐标系与数据年份须交代",
        "规划指标（容积率、密度）须给出计算口径",
        "政策背景与制度环境须说明",
        "模型校准与验证结果须报告",
    ),
    key_venues=(
        "Journal of the American Planning Association",
        "Urban Studies",
        "Regional Studies",
        "Environment and Planning A",
        "Landscape and Urban Planning",
        "Cities",
    ),
    units_and_formulas_notes=(
        "人口密度用 人/km²；建筑密度用 %",
        "容积率 (FAR) 用 无量纲比；绿地率用 %",
        "距离用 m/km；面积用 m²/ha/km²",
        "回归系数给出标准误与显著性；空间自相关用 Moran's I",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS Pro", "QGIS", "AutoCAD", "SketchUp", "CityEngine", "DepthmapX (Space Syntax)", "UrbanSim", "MATSim", "TransCAD", "VISSIM", "ENVI-met", "Rhino + Grasshopper", "Maptitude", "GeoDa", "Fragstats", "R (sf/spdep)", "Python (geopandas/OSMnx)", "GWR4", "SPSS", "Tableau"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Zenodo"),
)
