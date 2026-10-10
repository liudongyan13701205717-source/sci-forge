"""量子力学学科论文支持：量子理论、波函数与量子场论研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="quantum_mechanics",
    aliases=("quantum_mechanics", "量子力学", "quantum mechanics", "QM", "theoretical quantum", "quantum theory", "量子理论", "量子场论", "quantum field theory"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APS",
    reporting_standards={"k1": "哈密顿量表述须给出完备基与对称性", "k2": "数值方法须说明离散化与收敛性", "k3": "物理量纲分析遵循 SI 单位"},
    conventions=("物理量使用 Dirac 符号", "算符使用粗体或上标尖括号表示", "对称性用群记法说明", "单位系统采用 SI 或高斯制并标明", "参考文献按 APS 期刊风格著录"),
    key_venues=("Physical Review Letters", "Physical Review B", "Physical Review D", "Journal of Mathematical Physics", "Nuclear Physics B"),
    units_and_formulas_notes=("长度使用米（m）、纳米（nm）、埃（Å）", "能量使用电子伏特（eV）、焦耳（J）", "时间使用秒（s）、飞秒（fs）", "温度使用开尔文（K）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Mathematica", "Maple", "SymPy Quantum", "QuTiP", "PySCF", "Quantum Espresso", "ABINIT", "VASP", "Gaussian", "NWChem", "GAMESS", "Molpro", "Dalton", "MATLAB", "SciPy", "Octave", "gnuplot", "LaTeX", "Matplotlib", "PyTorch Scientific"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
