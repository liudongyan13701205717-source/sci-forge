"""Demolition 学科论文支持：爆破/拆除工程研究体裁、结构力学仿真规范与爆破设计工具。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="demolition",
    aliases=(
        "demolition", "爆破拆除", "结构拆除", "爆破工程",
        "implosion", "controlled demolition", "structural demolition",
        "explosive demolition", "机械拆除", "mechanical demolition",
        "demolition engineering", "拆除工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与工程需求）",
            "structure_analysis（结构特性与材料分析）",
            "method（拆除/爆破方案与方法）",
            "simulation（仿真与计算结果）",
            "results（实验/实施数据）",
            "safety_assessment（安全评估）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "project_background（项目背景）",
            "demolition_plan（拆除方案）",
            "execution（实施过程）",
            "outcome（效果评估）",
            "references",
        ),
        "methodology": (
            "abstract",
            "introduction",
            "theoretical_background（理论基础）",
            "numerical_model（数值模型与仿真）",
            "verification（验证与对比）",
            "applications（应用案例）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "materials": "结构材料属性须完整报告（混凝土强度等级、钢筋牌号、配筋率）",
        "explosives": "炸药/爆破参数须完整报告（炸药种类、装药量、起爆方式、传爆路线）",
        "simulation": "仿真模型须注明软件版本、网格划分参数、边界条件与材料本构模型",
        "safety": "安全措施（防护、疏散、监测）须作为独立章节报告",
        "experiments": "实验数据须报告置信区间与样本量；对比实验须说明控制变量",
    },
    conventions=(
        "结构材料属性须完整报告（混凝土强度等级、钢筋牌号、配筋率）",
        "炸药/爆破参数须完整报告（炸药种类、装药量、起爆方式、传爆路线）",
        "仿真模型须注明软件版本、网格划分参数、边界条件与材料本构模型",
        "安全措施（防护、疏散、监测）须作为独立章节报告",
        "实验数据须报告置信区间与样本量；对比实验须说明控制变量",
    ),
    key_venues=(
        "International Journal of Impact Engineering",
        "Journal of Applied Mechanics",
        "International Journal of Solids and Structures",
        "Engineering Fracture Mechanics",
        "Computers and Structures",
        "International Journal of Mechanical Sciences",
        "Applied Mathematical Modelling",
        "Journal of Materials in Civil Engineering",
    ),
    units_and_formulas_notes=(
        "混凝土强度用 MPa；钢筋强度用 MPa",
        "炸药参数用 kg（装药量）、ms（延时）",
        "应力用 MPa；应变用 mm 或 %",
        "仿真结果给出均值 ± 标准差",
        "公式用 amsmath；显示公式仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SolidWorks", "ANSYS", "ABAQUS", "LS-DYNA", "COMSOL Multiphysics", "MATLAB", "MATLAB Simulink", "AUTODYN", "SAP2000", "ETABS", "Robot Structural Analysis", "OpenSees", "RFEM", "DIANA", "PLAXIS", "FLAC3D", "CFAST", "CFX", "BlastWave"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
