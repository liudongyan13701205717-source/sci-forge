"""景观建筑学科论文支持：城市设计、生态环境、场地规划与公共空间。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="landscape_architecture",
    aliases=(
        "landscape_architecture",
        "景观建筑",
        "Landscape Architecture",
        "Urban Design",
        "Environmental Design",
        "Landscape Design",
        "Public Space Design",
        "Open Space Planning",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（绪论）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
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
    citation_style="APA",
    reporting_standards={
        "k1": "GB 50352 城市居住区规划设计标准",
        "k2": "CJJ/T 144 城市绿地分类标准",
        "k3": "EN 1996 砌体结构设计（景观工程部分）",
    },
    conventions=(
        "设计说明须包含用地性质、功能分区与面积指标",
        "植物配置须注明拉丁名、科属与生态习性",
        "分析图须标注图例、比例尺与北向",
        "生态评估须采用LACI/Landscape EBI等量化指标",
        "历史与文化遗产须按GB/T 25299 评估等级",
    ),
    key_venues=(
        "Landscape and Urban Planning",
        "Landscape Research",
        "Journal of the American Planning Association",
        "Urban Forestry & Urban Greening",
        "风景园林",
    ),
    units_and_formulas_notes=(
        "绿化率=绿化面积/总面积×100%",
        "人均绿地面积以m²/人表示",
        "雨水渗透率以m³/(m²·h)表示",
        "NDVI植被指数：(NIR-Red)/(NIR+Red)",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SketchUp", "Rhino", "Grasshopper", "Revit", "AutoCAD", "Enscape", "Lumion", "V-Ray", "D5 Render", "Adobe Illustrator", "Adobe Photoshop", "Adobe InDesign", "ArcGIS", "QGIS", "Houdini", "Unity", "Ecotone", "Global Illumination", "MATLAB", "R"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
