"""微纳机械学学科论文支持：微纳尺度力学、材料与结构研究、案例与综述体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="micromechanics",
    aliases=("micromechanics", "微纳机械学", "micro_mechanics", "nanomechanics", "micro_mechanical", "nano_mechanics", "micro_scale_mechanics", "micro_structural_mechanics", "micro_electro_mechanical", "micro_actuators", "flexoelectric"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（材料/结构/测试方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（微纳结构实例）", "analysis（力学响应分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（微纳力学理论与方法综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"k1": "微纳结构尺寸须遵循 SI 单位（μm / nm）", "k2": "力学测试须报告不确定度与重复性", "k3": "模拟须报告网格无关性验证与模型参数"},
    conventions=("微纳结构尺度须先定义并说明测量方法", "边界条件须明确（自由/固定/滑动）", "应力应变曲线须注明加载速率与路径", "模拟结果须附网格收敛验证", "结果须给置信区间与样本量"),
    key_venues=("Extreme Mechanics Letters", "Acta Mechanica", "Journal of the Mechanics and Physics of Solids", "Nano Letters", "Advanced Materials"),
    units_and_formulas_notes=("尺寸用 μm / nm；应力用 MPa / GPa", "应变无量纲；模量用 GPa", "能量密度用 J/m³；公式用 amsmath 并编号", "模拟结果须给验证试验对照"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("COMSOL Multiphysics", "ANSYS", "ABAQUS", "Nanoindentation tester", "Atomic force microscope", "Scanning electron microscope", "Transmission electron microscope", "SEM-FIB", "E-beam lithography", "MEMS fabrication cleanroom", "Microfabrication lab", "In-situ tensile testing", "Micro-tensile testing rig", "Python (NumPy, SciPy)", "MATLAB", "LAMMPS", "Molecular dynamics code", "Machine learning tool (sklearn)", "Finite element code (deal.II)", "Spectral element method code"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
