"""量子物理学科论文支持：量子现象、量子材料与量子实验。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="quantum_physics",
    aliases=("quantum_physics", "量子物理", "quantum physics", "量子学", "量子现象", "quantum phenomena", "quantum materials", "量子材料", "quantum optics"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APS",
    reporting_standards={"k1": "实验参数须给出误差棒与重复次数", "k2": "理论结果与实验结果须在同一坐标系比较", "k3": "量子态制备须说明保真度"},
    conventions=("物理量使用 SI 单位与 Dirac 符号", "实验装置须以示意图标注", "数据曲线须列出拟合方法与残差", "样品参数须给出批量与重复次数", "误差分析采用不确定度传播规则"),
    key_venues=("Physical Review Letters", "Physical Review A", "Nature Physics", "Nature Physics", "PRL Rapid Communications"),
    units_and_formulas_notes=("长度使用米（m）、纳米（nm）、埃（Å）", "能量使用电子伏特（eV）、焦耳（J）", "时间使用秒（s）、飞秒（fs）", "磁场使用特斯拉（T）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Mathematica", "Maple", "SymPy Quantum", "QuTiP", "PySCF", "Quantum Espresso", "ABINIT", "VASP", "Gaussian", "NWChem", "GAMESS", "Molpro", "Dalton", "MATLAB", "SciPy", "Octave", "gnuplot", "LaTeX", "Matplotlib", "QwikStim"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
