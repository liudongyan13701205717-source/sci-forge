"""量子计算学科论文支持：量子算法、量子硬件与量子软件开发。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="quantum_computing",
    aliases=("quantum_computing", "量子计算", "quantum computation", "quantum software", "quantum algorithm", "quantum information", "量子算法", "quantum systems", "quantum hardware"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APS",
    reporting_standards={"k1": "量子电路使用 Qiskit 或 OpenQASM 2.0 规范", "k2": "基准测试报告含噪声模型与重复次数", "k3": "量子优势声明须列出对比经典基线"},
    conventions=("量子电路使用 Dirac 符号", "门操作使用 |q⟩ 与 U 表记", "噪声模型与硬件平台须列出", "实验数据须包含重复采样次数", "算法复杂度以 O(n) 形式给出"),
    key_venues=("Physical Review X", "Quantum", "IEEE Transactions on Quantum Engineering", "Nature Physics", "npj Quantum Information"),
    units_and_formulas_notes=("量子比特数用 qubit 单位", "门保真度以百分比或小数报告", "运行时间以纳秒（ns）与微秒（μs）为单位", "相干时间以毫秒（ms）与微秒（μs）为单位"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Qiskit", "Cirq", "PennyLane", "QuTiP", "Q# SDK", "Azure Quantum", "AWS Braket", "IBM Qiskit Aer", "IBM Qiskit Metal", "Qiskit Pulse", "Qiskit Optimization", "Qiskit Runtime", "ProjectQ", "OpenQASM", "Rigetti Forest SDK", "IQM Quantum SDK", "QuEra Neutral Atom Platform", "Google Sycamore Hardware", "QuTech QuEra Emulator", "Quantum Inspire Software"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
