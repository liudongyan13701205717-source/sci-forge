"""建筑（Building）学科：建筑设计、构造与性能评价的研究方法与写作约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="building",
    aliases=("building", "建筑", "Building architecture", "建筑设计", "architecture and building",
             "building science", "建筑学", "architecture", "building design"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题界定）",
            "literature review（既有研究与理论脉络）",
            "methodology（案例/实证/仿真的方法说明）",
            "results（数据、图纸、仿真结果的呈现）",
            "discussion（与既有研究对话）",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7th（建筑学系）或 Harvard 样式（英国建筑期刊）",
    reporting_standards={
        "case_selection": "案例样本须说明选取标准（年代、地域、功能、规模）与代表性",
        "simulation": "能耗/采光仿真给边界条件（气候文件、窗墙比、围护结构 U 值）",
        "field_data": "实测数据（温度、照度、CO2）给仪器型号、采样频率与测点布置",
        "post_occupancy": "使用后评价（POE）给问卷设计、回收率与信效度",
    },
    conventions=(
        "图纸（平立剖、轴测）按编号引用（Fig. 1 对应图 1 说明）；图纸比例与标注须完整",
        "性能指标区分设计值与实测值；围护结构给传热系数（U 值/W·m⁻²·K⁻¹）",
        "能耗与碳排结果给基准建筑（reference building）对比；方法学按 ASHRAE/ISO 标准标注",
    ),
    key_venues=(
        "Building & Environment",
        "Energy and Buildings",
        "Building Research & Information (RIBA BRANZ)",
        "Architectural Design (AD)",
        "Journal of Architectural Engineering (ASCE)",
        "Habitat International",
    ),
    units_and_formulas_notes=(
        "面积 m²、体积 m³；能耗 kWh/m²/yr、kWh/m²·yr；照度 lx、采光系数 %",
        "传热用 U（W/m²K）、k（W/m·K）；风荷载给基本风速与重现期",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "Revit", "ArchiCAD", "SketchUp", "Rhino", "Lumion", "D5 Render", "Enscape", "EnergyPlus", "DesignBuilder", "TRNSYS", "Ecotect/Tecsys", "Green Building Studio", "Plasticity", "Fusion 360", "BIM 360", "Navisworks", "Solibri", "Tekla", "BIM Track", "Autodesk VRED", "Blender", "Inkscape", "Adobe Illustrator", "Mapbox GL", "QGIS", "MicroStation"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Scopus"),
)
