"""船舶建造（非机动）学科论文支持：船体结构/流体力学体裁、SNAME/ISO 引用样式与船舶工程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="boat_building",
    aliases=(
        "boat_building",
        "boat building",
        "Boat building (non-motor)",
        "船舶建造",
        "船体设计",
        "造船工程",
        "非机动船舶",
        "shipbuilding",
        "marine craft",
        "naval architecture",
        "船舶工程",
        "木船建造",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（船模试验、CFD 或结构分析）",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "design": (
            "abstract",
            "design brief",
            "hull form and geometry",
            "hydrostatics and seakeeping",
            "structural design",
            "appendices（图纸与数据表）",
            "references",
        ),
    },
    citation_style="SNAME/ISO 样式（作者-年份，船舶工程学会引用规范）",
    reporting_standards={
        "geometry": "船体主尺度与型线图须完整给出",
        "hydrostatics": "静水力参数按标准表列（CB、CL、CP、CM 等）",
        "experiment": "船模试验须报告缩尺比、边界条件与不确定度",
        "materials": "材料牌号与力学性能须明确",
    },
    conventions=(
        "主尺度符号：L（船长）、B（船宽）、T（吃水）、D（型深）全文一致",
        "船体静水力系数用 CB、CL、CP、CM 标准符号",
        "波浪条件用 Hs（有效波高）、Tp（主峰周期）、θ（方向）报告",
        "流体力学结果以无量纲化形式给出（Fn、Ct、Cp、Ci）",
        "结构图遵循 IACS/IMO 编号规则",
    ),
    key_venues=(
        "Journal of Ship Research",
        "Ocean Engineering",
        "Ships and Offshore Structures",
        "Applied Ocean Research",
        "Marine Structures",
        "Proceedings of IMACOOS",
        "Journal of Offshore Mechanics and Arctic Engineering",
    ),
    units_and_formulas_notes=(
        "长度用 m；速度用 kn 或 m/s 并标明",
        "功率用 kW 或 hp",
        "波浪参数 Hs（有效波高）、Tp（主峰周期）、θ（方向）",
        "阻力系数 Ct = T/(0.5·ρ·V²·A)",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Rhino", "SolidWorks", "Autodesk Fusion 360", "FreeCAD", "Autodesk 3ds Max", "CATIA V5", "SolidWorks Simulation", "ANSYS Fluent", "Star-CCM+", "OpenFOAM", "SU2", "XFOIL", "Maxsurf", "RISA-3D", "NASTRAN", "Abaqus", "MATLAB", "Tecplot", "ParaView", "OpenVPA"),
    category="工学",
    databases=("OpenAlex", "Google Scholar", "ScienceDirect", "arXiv"),
)
