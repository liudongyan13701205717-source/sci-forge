"""建筑设计（Building design）：方案设计、性能模拟与空间评价的研究方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="building_design",
    aliases=("building_design", "建筑设计", "Building design",
             "architectural design", "建筑学设计", "spatial design",
             "interior architecture", "室内设计", "studio design"),
    paper_types={
        "research": (
            "abstract",
            "introduction（设计问题与场所语境）",
            "design methodology（设计推理、图式、性能目标）",
            "case / project presentation（设计过程、方案比较、关键决策）",
            "performance evaluation（能耗、采光、舒适度、人流模拟结果）",
            "discussion（设计意图与性能结果的对话）",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7th 或 Harvard 样式（建筑学/环境系）",
    reporting_standards={
        "performance_sim": "能耗/采光/通风仿真给软件版本、气候文件（TMY/EPW）、材料参数与边界条件",
        "case_review": "案例选择给功能类型、规模、年代与地域；图纸按图号引用",
        "user_study": "使用后评价/问卷给量表（如 5 点 Likert）、样本量与统计分析方法",
        "design_process": "设计过程研究给决策链记录（草图、模型、变更日志）",
    },
    conventions=(
        "图纸/渲染图按编号引用，图注写清比例、朝向与视图类型",
        "性能指标给单位与基准对比（同类建筑或 ASHRAE 基准）；节能率百分比标注基准",
        "人体尺度与流线分析配合平面图；日照/通风给模拟参数（太阳角度、风速）",
    ),
    key_venues=(
        "Building & Environment",
        "Architectural Research (Architype)",
        "Journal of Architectural Engineering (ASCE)",
        "Habitat International",
        "Design Studies",
        "Building Research & Information (RIBA BRANZ)",
    ),
    units_and_formulas_notes=(
        "采光系数 %、照度 lx；得热/冷负荷 W/m²；热舒适 PMV/PPD 给参数",
        "人流模拟给密度（人/m²）与通行时间；面积 m²、容积率无纲量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "Revit", "ArchiCAD", "SketchUp", "Rhino", "Grasshopper", "Ladybug Tools", "EnergyPlus", "DesignBuilder", "Ecotect/Tecsys", "D5 Render", "Lumion", "Enscape", "Blender", "Adobe Photoshop", "Adobe Illustrator", "Figma", "Space Syntax / DepthmapX", "MassHunter", "Vizact", "QGIS", "Plasticity", "Fusion 360", "Navisworks", "BIM Track"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Scopus"),
)
