"""施工技术学科论文支持：BIM、施工方法、进度控制与质量安全。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="construction_technology",
    aliases=(
        "construction technology",
        "construction methods",
        "construction management",
        "施工技术",
        "建筑技术",
        "施工管理",
        "construction engineering",
        "建筑工业化",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景与施工问题）",
            "methodology（施工工艺/BIM/进度模型）",
            "case study / simulation（案例或仿真）",
            "results（工期、成本、质量、安全指标）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "project description",
            "construction methodology",
            "progress and cost analysis",
            "issues and solutions",
            "lessons learned",
            "references",
        ),
        "review": (
            "abstract",
            "historical overview",
            "current methods",
            "open challenges",
            "references",
        ),
    },
    citation_style="APA 或 IEEE 样式，遵循行业惯例",
    reporting_standards={
        "BIM": "BIM 交付须遵循 ISO 19650、BIMCO 或 GB/T 51301",
        "progress": "进度计划须报告工期、关键路径与资源负荷",
        "cost": "成本估算须遵循 GB/T 50500 或 SIA 203",
        "quality": "质量检验须遵循 GB 50300 或 ISO 9001",
        "safety": "安全标准遵循 GB 5036 或 ISO 45001",
    },
    conventions=(
        "BIM 模型遵循 GB/T 51301 或 ISO 19650 交付要求",
        "图纸标注遵循 GB/T 50001 或 ISO 1167",
        "施工进度采用横道图或双代号网络图，含关键路径",
        "成本数据按工程量清单（BOQ）分类",
        "质量检验遵循 GB 50300 系列或 ISO 9001",
    ),
    key_venues=(
        "Automation in Construction",
        "Journal of Construction Engineering and Management",
        "Construction Management and Economics",
        "Construction Innovation",
        "International Journal of Project Management",
        "土木工程学报",
        "建筑经济",
        "建筑施工",
        "施工机械",
        "建筑科学",
    ),
    units_and_formulas_notes=(
        "工期 d 或天；进度 % 或 CPI/SPI",
        "成本 元或 万元；单价 元/m² 或 元/m³",
        "面积 m²；体积 m³；长度 m",
        "安全系数 K 或 n",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Autodesk Revit", "Autodesk Revit Structure", "Autodesk Navisworks", "Autodesk AutoCAD", "Autodesk AutoCAD Civil 3D", "Autodesk InfraWorks", "Autodesk Forma", "Autodesk Construction Cloud", "Autodesk BIM 360", "Bentley OpenBuildings Designer", "Bentley OpenSite", "Bentley OpenRoads", "Bentley OpenBridge", "Bentley AECOsim Design Solutions", "Bentley MicroStation", "Trimble SketchUp Pro", "Trimble TSC", "Trimble TBC", "Trimble Access", "Trimble Earthworks", "Trimble Field Level", "Trimble Business Center", "Bluebeam Revu", "Procore", "PlanGrid", "Oracle Primavera P6", "Microsoft Project", "SMILE", "CYPE", "MIDAS Civil", "SAP2000", "STAAD.Pro", "ETABS", "SAFE", "LUSAS", "RISA-3D", "Robot Structural Analysis", "Tekla Structures", "ArchiCAD", "Vectorworks", "Rhino", "Grasshopper"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "ScienceDirect", "IEEE Xplore", "CNKI", "万方"),
)
