"""其他物理科学学科论文支持：凝聚态、量子、光学、等离子体、生物物理等跨分支物理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_physical_sciences",
    aliases=("Other Physical Sciences", "其他物理科学", "Condensed Matter Physics", "Quantum Physics", "Nuclear Physics", "Astrophysics", "Biophysics", "Physical Chemistry"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Nature / SI Unit (Elsevier)",
    reporting_standards={
        "k1": "实验测量遵循ISO 17025计量规范", "k2": "系统综述遵循PRISMA筛选流程", "k3": "观测研究遵循STROBE报告规范"
    },
    conventions=("使用SI单位且国际单位符号遵循ISO 80000", "公式编号遵循期刊层级编号（定理X.Y，公式(1)(2)）", "图表数据须标注误差棒、显著性水平与数据来源", "实验方法学必须明确可复现性声明与开源数据仓库", "跨学科符号约定须区分上标/下标与斜体正体用法"),
    key_venues=("Physical Review Letters", "Nature Physics", "Science", "Physical Review B", "Journal Of Applied Physics", "Nature Communications"),
    units_and_formulas_notes=("SI单位系统：长度m、质量kg、时间s、电流A、温度K", "有效数字遵循ISO 80000-1：测量值有效位与不确定度量级匹配", "统计显著性水平标注p值或置信区间（95% CI默认）", "量纲分析遵循M-L-T基础量纲标注以避免量纲混淆"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python", "Julia", "Mathematica", "MAPLE", "COMSOL Multiphysics", "LAMMPS", "VASP", "Gaussian", "ORCA", "GROMACS", "GMX Viewer", "MDAnalysis", "ParaView", "VMD", "Avogadro", "OriginPro", "SciPy", "NumPy", "PyTorch"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
