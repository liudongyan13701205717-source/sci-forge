"""建筑金属加工学科论文支持：金属构件、焊接、连接与结构制造。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="constructional_metalwork",
    aliases=(
        "constructional metalwork",
        "building metalwork",
        "structural steelwork",
        "建筑金属加工",
        "建筑金属工程",
        "金属结构",
        "steel construction",
        "钢结构工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景与金属构件问题）",
            "materials and methods（材料、加工与试验）",
            "results（连接强度、焊接质量、疲劳评估）",
            "discussion",
            "conclusions",
            "references",
        ),
        "design_report": (
            "abstract",
            "requirements（荷载、规范与设计边界）",
            "modeling（构件建模与连接设计）",
            "analysis（应力、应变、刚度验算）",
            "verification（规范校核与制造工艺）",
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
    citation_style="APA 或 IEEE 样式，符合机械/结构行业惯例",
    reporting_standards={
        "material": "材料性能须遵循 GB/T 228 拉伸或 GB/T 229 冲击",
        "welding": "焊接工艺须遵循 GB/T 50205 或 ISO 3834",
        "connection": "连接设计须遵循 GB 50017 或 EN 1993",
        "quality": "无损检测须遵循 GB/T 3323 或 EN ISO 17636",
        "standards": "引用标准须标注 GB/T、EN、ISO 或 ASTM 编号",
    },
    conventions=(
        "钢结构设计遵循 GB 50017 或 Eurocode 3",
        "焊接质量遵循 GB 50205 或 EN 1090",
        "无损检测遵循 GB/T 3323 或 EN ISO 17636",
        "材料牌号使用 GB/T 或 EN 双标注",
        "连接件规格遵循 GB/T 或 EN 1090",
    ),
    key_venues=(
        "Journal of Constructional Steel Research",
        "Engineering Structures",
        "Journal of Structural Engineering",
        "International Journal of Steel Structures",
        "Steel Construction",
        "土木工程学报",
        "建筑结构",
        "钢结构",
        "建筑钢结构",
    ),
    units_and_formulas_notes=(
        "长度 mm；力 N 或 kN；应力 MPa",
        "焊接热输入 kJ/mm；熔敷金属体积 cm³",
        "疲劳循环次数 N；应力幅 Δσ MPa",
        "扭矩 N·m；拧紧力矩 N·m",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Autodesk Revit Structure", "Autodesk AutoCAD", "Autodesk Inventor", "SolidWorks", "SolidWorks Simulation", "SolidWorks Composer", "CATIA V5", "CATIA V6", "PTC Creo", "Siemens NX", "Siemens NX Nastran", "Siemens Teamcenter", "PTC Windchill", "ArchiCAD", "Tekla Structures", "Tekla Openings", "Tekla Fabrication", "Tekla Warehouse", "Bentley MicroStation", "Trimble SketchUp Pro", "Autodesk Fusion 360", "Onshape", "MIDAS Civil", "MIDAS Gen", "MIDAS FE", "SAP2000", "ETABS", "STAAD.Pro", "LUSAS", "RISA-3D", "ABAQUS", "ANSYS Mechanical", "ANSYS LS-DYNA", "ADINA", "MSC Nastran", "Altair HyperWorks", "LS-DYNA", "Radioss", "COMSOL Multiphysics", "MATLAB", "SolidCAM", "Mastercam", "Fanuc Roboguide", "ABB Robot Studio", "Siemens Robot", "KUKA Robot", "Fanuc CNC", "Mazak CNC", "Okuma CNC", "DMG MORI CNC"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "ScienceDirect", "IEEE Xplore", "CNKI"),
)
