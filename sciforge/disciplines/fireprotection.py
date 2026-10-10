"""消防工程学科论文支持：火灾动力学、消防安全设计与灭火技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fireprotection",
    aliases=("fireprotection", "消防工程", "fire protection", "fire safety engineering",
             "fire engineering", "fire prevention", "火灾科学", "消防安全",
             "firefighting"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714",
    reporting_standards={
        "fire_model": "火灾模型须说明网格划分、湍流模型、辐射模型与边界条件设置",
        "experiment": "火灾试验须报告可燃物类型与载荷、点火方式、环境温度与通风条件",
        "detection": "探测器试验须声明响应时间与阈值、安装位置与环境模拟条件",
    },
    conventions=(
        "热通量用 kW/m² 表示",
        "烟气浓度用 mg/m³ 或 ppm 表示",
        "温度用 °C 表示",
        "火灾荷载用 MJ/m² 表示",
        "灭火剂用量用 kg 或 L 表示",
    ),
    key_venues=(
        "Fire Safety Journal",
        "Building and Environment",
        "International Journal of Wildland Fire",
        "Journal of Fire Sciences",
        "消防科学与技术",
    ),
    units_and_formulas_notes=(
        "热通量 q = Q/A，单位 kW/m²",
        "雷诺数 Re = ρvL/μ，无量纲",
        "热释放速率 HRR = m × ΔHc，单位 kW",
        "烟气层高度 H_s = H - ΔT·H/(ΔT+T_amb)·(g·H)/(v²)，单位 m",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("FDS (Fire Dynamics Simulator)", "PyroSim", "ANSYS Fluent", "COMSOL Multiphysics", "MATLAB", "Python (SciPy/NumPy)", "AutoCAD", "SolidWorks", "SketchUp", "Revit (Autodesk)", "Rhino + Grasshopper", "SPSS", "R (RStudio)", "FLIR Thermal Camera", "Testo Thermal Imager", "烟气分析仪", "红外热像仪", "气体检测仪", "火灾试验炉", "GIS (ArcGIS)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)