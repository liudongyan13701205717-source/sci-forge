"""水土保持技术员课程学科论文支持：工程实践/技术管理/野外操作体裁、APA 7 样式与操作记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="soil_and_water_technician_programmes",
    aliases=(
        "soil_and_water_technician_programmes",
        "水土保持技术员",
        "水土保持工程",
        "水土保持技术",
        "水土保持管理",
        "soil conservation technician",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methods（方法）",
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
        "technical_report": (
            "abstract",
            "introduction",
            "technical overview（技术概述）",
            "implementation（实施）",
            "evaluation（评估）",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "experimental": "实验遵循水土保持实验报告规范",
        "case_study": "案例研究遵循水土保持案例报告规范",
        "technical": "技术报告遵循水土保持技术报告规范",
        "reproducibility": "可复现性遵循水土保持可复现性清单",
    },
    conventions=(
        "研究区地理位置与地形须报告",
        "采样点与采样深度须说明",
        "防治工程类型与参数须注明",
        "统计处理须说明",
        "单位须与国际单位一致",
    ),
    key_venues=(
        "Soil and Tillage Research",
        "Catena",
        "Journal of Hydrology",
        "Agricultural Water Management",
        "Land Degradation & Development",
    ),
    units_and_formulas_notes=(
        "土壤侵蚀模数用 t/(hm²·a)",
        "坡度用 %；坡长用 m",
        "公式用 amsmath；工程参数须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "Global Mapper", "HEC-RAS", "HEC-HMS", "SWAT", "WEAP", "R", "Python", "MATLAB", "SPSS", "ENVI", "AutoCAD", "Civil 3D", "MicroStation", "SketchUp", "Revit", "Total Station", "GPS/GNSS Receiver", "GIS Workbench"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
