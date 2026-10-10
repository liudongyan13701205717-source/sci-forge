"""水力学学科论文支持：水力学/明渠/管道流研究体裁、ASCE/IAHR 引用样式与水力度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hydraulics",
    aliases=("hydraulics", "水力学", "流体力学", "明渠流", "管道流", "水工水力学", "湍流", "水力设计", "水工结构"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与水力问题）", "methodology（试验/计算/理论方法）", "results（水力量测与模拟结果）", "discussion（机理与工程意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（工程与流态）", "analysis（水力学分析）", "results（安全/设计评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（控制方程与准则）", "evidence synthesis（研究综合）", "future directions", "references"),
    },
    citation_style="ASCE 样式（作者-年份；Journal of Hydraulic Engineering 遵循其规范）",
    reporting_standards={
        "experimental": "水力学试验遵循 IAHR 试验规程与 Froude 相似准则",
        "numerical": "CFD 研究遵循网格无关性与湍流模型报告规范",
        "theoretical": "解析研究须给出控制方程与边界条件",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "dimensional": "无量纲化须报告 Froude/Reynolds 数",
    },
    conventions=(
        "控制方程须列出并编号",
        "试验几何与边界条件须报告",
        "模拟网格无关性与收敛准则须给出",
        "无量纲参数须定义",
        "单位与量纲须一致",
    ),
    key_venues=(
        "Journal of Hydraulic Engineering",
        "Journal of Fluid Mechanics",
        "International Journal for Numerical Methods in Fluids",
        "Flow, Turbulence and Combustion",
        "Water Resources Research",
        "Journal of Hydraulic Research",
    ),
    units_and_formulas_notes=(
        "流量用 m³/s；流速用 m/s；水深用 m",
        "水头损失用 m；雷诺数 Re 无量纲",
        "公式用 amsmath；Navier-Stokes 与能方程须编号",
        "数值结果给出均值 ± 不确定度与样本量",
        "湍流量（湍动能、耗散率）须给出单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("HEC-RAS", "OpenFOAM", "ANSYS Fluent", "STAR-CCM+", "CFX", "MATLAB", "Python", "R", "LS-DYNA", "SolidWorks", "AutoCAD", "FLUENT UDF", "Paraview", "QGIS", "ArcGIS", "Surfer", "LaTeX", "Excel", "EndNote", "Git"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
