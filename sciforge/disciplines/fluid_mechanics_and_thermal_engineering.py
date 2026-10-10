"""流体与热工程学科论文支持：流体力学、传热学、燃烧与热机研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fluid_mechanics_and_thermal_engineering",
    aliases=("fluid_mechanics_and_thermal_engineering", "流体与热工程", "流体力学", "传热学", "热力学", "燃烧科学", "涡轮机械", "CFD"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago Author-Date",
    reporting_standards={"k1": "ASME 报告规范", "k2": "AIAA 实验报告指南", "k3": "E31 传热实验报告标准"},
    conventions=("流体参数须标注压力、温度、密度与黏度", "Reynolds 数须注明计算基准（弦长/水力直径）", "数值解法须注明求解器、离散格式与残差收敛准则", "网格无关性须给出 3 套以上网格对比", "无量纲化须注明参考量"),
    key_venues=("Journal of Fluid Mechanics", "International Journal of Heat and Mass Transfer", "AIAA Journal", "Combustion and Flame", "Physics of Fluids"),
    units_and_formulas_notes=("速度单位：m/s；压力：Pa", "雷诺数 Re = ρUL/μ", "努塞尔特数 Nu = hL/k", "无量纲化须给出参考长度与速度"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS Fluent", "OpenFOAM", "COMSOL Multiphysics", "MATLAB / Simulink", "Tecplot（CFD 后处理）", "Paraview（CFD 后处理）", "热线风速仪 (Dantec)", "PIV 激光诱导荧光系统", "Schlieren 光学系统", "Kistler 压力传感器", "Type K 热电偶", "热流传感器 (Gauge)", "低速风洞", "高速摄像机 (Phantom)", "Flame Emission Spectrum 分析", "LaTeX（排版）", "Python NumPy（数值计算）", "R（统计检验）", "Origin（数据绘图）", "OpenVSC"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
