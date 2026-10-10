"""建筑与城镇规划学科论文支持：镇域空间、土地用途、基础设施与规划实施。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="architecture_and_town_planning",
    aliases=(
        "architecture and town planning",
        "建筑与城镇规划",
        "城镇规划",
        "town planning",
        "rural planning",
        "乡村规划",
        "town and country planning",
        "城乡规划建设",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "context and literature",
            "methodology",
            "case analysis",
            "findings",
            "planning implications",
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
        "participation": (
            "abstract",
            "introduction",
            "participation design",
            "data collection",
            "findings",
            "planning integration",
            "references",
        ),
    },
    citation_style="作者-年份（APA 或 Chicago 均可）",
    reporting_standards={
        "gis": "空间分析给坐标系（CGCS2000/WGS84）、投影与栅格分辨率",
        "survey": "公众参与给量表、样本量与访谈转录方法",
        "simulation": "人口/用地模拟给参数与情景假设",
        "drawings": "规划图给图例、比例尺与图幅编号",
    },
    conventions=(
        "镇域边界与统计口径须明确（建成区/镇域/行政界）",
        "用地分类按现行《城乡用地分类与规划建设用地标准》GB 50137",
        "人口与就业指标给数据来源与年份",
        "规划图组含总平面、竖向、交通与管线综合",
    ),
    key_venues=(
        "Town Planning Review",
        "Landscape and Urban Planning",
        "Cities",
        "Journal of the American Planning Association",
        "Frontiers of Architectural Research",
        "Urban Studies",
    ),
    units_and_formulas_notes=(
        "用地面积 km² 或 ha；密度 人/km²",
        "用地比例 %；容积率无量纲",
        "坐标用 CGCS2000；比例尺 1:N",
        "人口总数 人；就业人数 人；GDP 元/平方公里",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "Revit", "Rhino", "Grasshopper", "SketchUp", "ArcGIS", "QGIS", "CityEngine", "3ds Max", "V-Ray", "Lumion", "Twinmotion", "DYNAMO", "Ladybug Tools", "EnergyPlus", "OpenSCAD", "Rhino.Inside Revit", "QGIS Model Builder", "D5 Render", "Blender"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "DOAJ"),
)
