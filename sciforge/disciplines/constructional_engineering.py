"""建构工程学科论文支持：结构分析、抗震、材料与施工一体化。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="constructional_engineering",
    aliases=(
        "constructional engineering",
        "structural engineering",
        "building engineering",
        "建构工程",
        "结构工程",
        "建筑工程",
        "building science",
        "建筑构造",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景与结构问题）",
            "materials and methods（材料、试验与建模）",
            "results（受力性能、破坏模式、抗震评估）",
            "discussion",
            "conclusions",
            "references",
        ),
        "design_report": (
            "abstract",
            "requirements（荷载、规范与设计边界）",
            "modeling（结构建模与荷载工况）",
            "analysis（内力求解与位移计算）",
            "verification（规范校核与抗震验算）",
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
    citation_style="APA 或 GB/T 7714 样式，遵循土木/结构行业惯例",
    reporting_standards={
        "modeling": "结构模型须报告单元类型、材料属性、边界条件与荷载工况",
        "testing": "材料试验须遵循 GB/T 50081 混凝土或 GB/T 228 钢材",
        "codes": "引用规范须标注 GB 50010、GB 50011 或 ACI/Eurocode",
        "analysis": "结果须报告应力、位移、配筋率与安全系数",
    },
    conventions=(
        "结构分析遵循 GB 50010、GB 50011 或 Eurocode 2/8",
        "配筋率与最小构造遵循规范强条",
        "荷载组合按 GB 50009 或 EN 1990 定义",
        "抗震设防遵循 GB 50011 等级",
        "结果单位遵循 SI，长度 mm、力 kN、应力 MPa",
    ),
    key_venues=(
        "Engineering Structures",
        "Journal of Constructional Steel Research",
        "Engineering Structures",
        "Earthquake Engineering & Structural Dynamics",
        "Bulletin of Earthquake Engineering",
        "土木工程学报",
        "建筑结构",
        "工业建筑",
        "建筑科学",
    ),
    units_and_formulas_notes=(
        "长度 mm；力 N 或 kN；应力 MPa；模量 GPa",
        "配筋率 %；位移 mm；挠度 mm",
        "荷载 kN 或 kPa；地震动加速度 g 或 cm/s²",
        "周期 T (s)；频率 f (Hz)",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Autodesk Revit Structure", "Autodesk Robot Structural Analysis", "MIDAS Civil", "MIDAS Gen", "MIDAS Building", "MIDAS FE", "SAP2000", "ETABS", "SAFE", "STAAD.Pro", "LUSAS", "RISA-3D", "CSi Bridge", "CSi Perform3D", "ABAQUS", "ANSYS Mechanical", "ANSYS LS-DYNA", "ADINA", "NASTRAN", "MSC Nastran", "Altair HyperWorks", "LS-DYNA", "Radioss", "PAM-Crash", "Tekla Structures", "Tekla Openings", "Tekla Fabrication", "Tekla Warehouse", "SolidWorks Simulation", "SolidEdge", "CATIA V5", "PTC Creo", "Siemens NX", "Autodesk Inventor", "MATLAB", "COMSOL Multiphysics", "OpenSees", "SeismoSoft", "Response2000", "Pushover"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "ScienceDirect", "IEEE Xplore", "CNKI", "万方"),
)
