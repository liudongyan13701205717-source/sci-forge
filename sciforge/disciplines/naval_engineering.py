"""船舶工程学科论文支持：船舶设计/性能/结构/水动力体裁、IEEE 样式与船舶工程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="naval_engineering",
    aliases=("naval_engineering", "船舶工程", "naval architecture", "marine engineering",
             "造船工程", "舰船设计", "船舶设计", "marine design", "ship design"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与船舶工程问题）", "methodology（建模与试验方法）", "results（性能与结构数据）", "discussion（工程启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（舰船案例与工况背景）", "analysis（设计与故障分析）", "results（改进与验证）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（设计与理论综述）", "evidence synthesis（工程证据综合）", "future directions", "references"),
    },
    citation_style="IEEE 样式或 APA 视期刊而定",
    reporting_standards={
        "hydrodynamic": "水动力试验须按 ITTC 1978/2002 报告规范（含 Froude 数与相似律）",
        "structural": "结构强度与疲劳试验须按 DNV/BS/ISO 标准报告",
        "simulation": "CFD 仿真须报告网格无关性与湍流模型设定",
    },
    conventions=(
        "船型与尺度用 LBP/B/D/T 定义并给出参考船型版本",
        "水动力系数（Ct、Ca、Cb、Cp）须给出定义与口径",
        "试验须注明静水/海况、速度与航行环境",
        "结构用钢等级（AH36、A36 等）与板厚给出",
        "术语与符号遵循 ITTC 与 IHO 手册并首次给全称",
    ),
    key_venues=(
        "Journal of Ship Research",
        "Ocean Engineering",
        "Journal of Naval Architecture and Marine Engineering",
        "Marine Structures",
        "Applied Ocean Research",
    ),
    units_and_formulas_notes=(
        "长度 m、速度节或 m/s、功率 kW 或 hp 须注明口径",
        "水动力系数无量纲并给出参考面积/参考速度",
        "应力 MPa、弯矩 kN·m；疲劳按 S-N 曲线并给出循环次数",
        "公式用 amsmath；主要系数须定义并显示计算式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CATIA", "AutoCAD Marine", "SolidWorks", "NAPA Hydrodynamics", "Maxsurf", "WAMIT", "Delft3D", "OpenFOAM", "STAR-CCM+", "ANSYS Fluent", "NEMOH", "SimScale", "Nastran", "Hypermesh", "Abaqus", "MATLAB", "Python (NumPy/SciPy)", "ModelMaker", "OrcaFlex", "DNV GL SEACOM"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
