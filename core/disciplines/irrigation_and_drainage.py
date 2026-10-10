"""灌溉与排水工程学科论文支持：水工、管网、渠道与排灌系统。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="irrigation_and_drainage",
    aliases=("irrigation and drainage", "灌溉排水", "灌排工程", "水利工程", "管网", "渠道", "排水工程", "水利管网"),
    paper_types={
        "research": ("abstract", "introduction（问题与工程背景）", "methodology（设计、模型与实验）", "results（水力、排水与能耗结果）", "discussion（对比与推广）", "references"),
        "case_study": ("abstract", "introduction", "case description（区域、管网或渠系）", "analysis（水力模拟与运行评估）", "results（发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（灌排工程理论）", "evidence synthesis（工程与运行证据）", "future directions", "references"),
    },
    citation_style="ASCE 样式（编号引用）或 GB/T 7714（中文稿）",
    reporting_standards={
        "k1": "工程参数（流量、坡度、管径）给完整",
        "k2": "模拟软件、边界条件与网格给出",
        "k3": "现场实测与仿真结果对应",
    },
    conventions=(
        "水力公式（Manning、Darcy-Weisbach）给符号定义",
        "管网与渠道断面给图与尺寸",
        "单位以 SI 或工程惯例注明（mmH2O、L/s、m³/h）",
        "模型边界与初始条件说明",
        "工程对比给同条件与同参数"
    ),
    key_venues=(
        "Irrigation and Drainage",
        "Journal of Irrigation and Drainage Engineering",
        "Water Resources Research",
        "Journal of Hydraulic Engineering",
        "Agricultural Water Management"
    ),
    units_and_formulas_notes=(
        "流量以 m³/s 或 L/s，坡降 %",
        "管径 mm 或 DN，压力 kPa 或 mmH2O",
        "水位差 m，流速 m/s",
        "面积 m² 或 公顷，时间 s 或 h"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("EPA SWMM", "MIKE SHE", "MIKE 21", "HEC-RAS", "HEC-HMS", "EPANET", "MODFLOW", "HYDRUS", "AquaCrop", "CROPSIM", "FAO-56 Penman-Monteith Calculator", "ArcGIS", "QGIS", "AutoCAD", "AutoCAD Civil 3D", "Rhino 3D", "SolidWorks", "MATLAB", "Python", "OpenDrainage"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
