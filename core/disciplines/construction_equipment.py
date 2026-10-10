"""建筑设备学科论文支持：施工机械、液压系统、CAD/CAE 分析与结构仿真。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="construction_equipment",
    aliases=(
        "construction equipment",
        "construction machinery",
        "building equipment",
        "建筑设备",
        "施工机械",
        "工程机械",
        "construction plant",
        "重型机械",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景与设备选型动机）",
            "system description（设备结构与关键子系统）",
            "modeling and analysis（CAD/CAE 建模与仿真）",
            "results（性能/强度/效率评估）",
            "conclusions",
            "references",
        ),
        "design_report": (
            "abstract",
            "requirements（工况与设计输入）",
            "design development（方案对比与优化）",
            "structural analysis（有限元/静强度/疲劳）",
            "performance verification",
            "references",
        ),
        "review": (
            "abstract",
            "historical overview",
            "current technology status",
            "open challenges",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号），符合机械/土木行业惯例",
    reporting_standards={
        "modeling": "CAD 模型须声明几何精度、公差配合与材料属性",
        "FEA": "有限元分析须报告单元类型、网格密度、边界条件与载荷工况",
        "hydraulics": "液压系统须报告压力、流量、元件型号与工况曲线",
        "safety": "涉及结构安全须遵循 GB/T 3811、ISO 4301 或 EN 14399",
        "testing": "实测数据须给出设备编号、工况、传感器型号与量程",
    },
    conventions=(
        "设备参数遵循 ISO 15245 / ISO 4301 命名与标注",
        "CAD 图纸遵循 GB/T 14689 或 ASME Y14.5 尺寸公差与形位公差",
        "有限元结果须报告应力/位移单位（MPa/mm）与工况编号",
        "液压油标准遵循 GB/T 7631.1 或 ISO 11158",
        "材料牌号使用国标 GB/T 或国际标准 ASTM/EN 双标注",
    ),
    key_venues=(
        "Engineering Structures",
        "Construction and Building Materials",
        "Journal of Construction Engineering and Management",
        "Automation in Construction",
        "Archives of Civil and Mechanical Engineering",
        "机械工程学报",
        "土木工程学报",
        "施工机械",
        "工程机械",
    ),
    units_and_formulas_notes=(
        "长度 mm；力 N 或 kN；应力 MPa 或 GPa",
        "功率 kW；扭矩 N·m；液压压力 MPa",
        "质量 kg 或 t；体积 m³；流量 L/min",
        "转速 rpm；频响 Hz",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Autodesk CATIA V5", "Autodesk CATIA V6", "ANSYS Mechanical", "ANSYS Fluent", "ANSYS Motion", "SolidWorks", "SolidWorks Simulation", "Autodesk Inventor", "Autodesk AutoCAD", "Autodesk Revit", "PTC Creo", "Siemens NX", "Siemens NX Nastran", "Dassault SolidWorks Composer", "ABAQUS", "NASTRAN", "ADINA", "COMSOL Multiphysics", "LS-DYNA", "Radioss", "MATLAB", "Simulink", "Robot Structural Analysis", "MIDAS Civil", "MIDAS Gen", "SAP2000", "STAAD.Pro", "ETABS", "SAFE", "LUSAS", "RISA-3D", "Tekla Structures", "Autodesk Navisworks", "Autodesk Simulation Live", "MSC Adams", "MSC Nastran", "Altair HyperWorks", "Siemens STAR-CCM+", "OpenFOAM"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "IEEE Xplore", "ScienceDirect", "CNKI"),
)
