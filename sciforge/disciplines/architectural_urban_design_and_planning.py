"""建筑城市设计与规划学科论文支持：城市形态、公共空间、街区肌理与规划实施。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="architectural_urban_design_and_planning",
    aliases=(
        "architectural urban design and planning",
        "建筑城市设计与规划",
        "建筑城市设计",
        "urban design and planning",
        "城市设计",
        "城市规划与设计",
        "urban morphology",
        "城市形态学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "context and literature",
            "methodology",
            "case analysis",
            "findings",
            "design implications",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "site context",
            "urban fabric analysis",
            "design proposal",
            "evaluation",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy background",
            "comparative analysis",
            "implementation review",
            "recommendations",
            "references",
        ),
    },
    citation_style="作者-年份（Chicago/Elsevier 系均可）",
    reporting_standards={
        "survey": "公众参与与问卷给量表、样本量与置信区间",
        "gis": "空间分析给坐标系（CGCS2000/WGS84）、投影、比例尺与栅格分辨率",
        "simulation": "交通/人流模拟给软件版本、需求预测口径与校准指标",
        "drawings": "图纸给比例尺与指北针；渲染区分示意图与效果图",
    },
    conventions=(
        "城市指标口径须明确（建成区/中心城区/统计区划）",
        "用地与建筑指标给容积率、建筑密度与绿地率",
        "空间分析附坐标系统、投影方式与比例尺说明",
        "公众参与过程、参与对象构成与样本量须交代",
    ),
    key_venues=(
        "Urban Studies",
        "Journal of Urban Design",
        "Landscape and Urban Planning",
        "Cities",
        "Journal of the American Planning Association",
        "Frontiers of Architectural Research",
    ),
    units_and_formulas_notes=(
        "容积率无量纲；建筑密度 %；绿地率 %",
        "人口密度 人/km²；路网密度 km/km²；步行距离 m",
        "坐标用 CGCS2000 或 WGS84；比例尺 1:N",
        "土地利用面积 km² 或 ha；道路长度 km",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "Revit", "Rhino", "Grasshopper", "SketchUp", "ArcGIS", "QGIS", "3ds Max", "V-Ray", "Lumion", "Twinmotion", "CityEngine", "DYNAMO", "Ladybug Tools", "EnergyPlus", "OpenSCAD", "ArcGIS Urban", "Karamba3D", "Rhino.Compute", "D5 Render"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "DOAJ"),
)
