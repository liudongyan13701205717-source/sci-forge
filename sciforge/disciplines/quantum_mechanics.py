"""量子力学学科论文支持：量子理论/量子信息体裁、APS 引用样式与量子记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="quantum_mechanics",
    aliases=("quantum mechanics", "量子力学", "量子理论", "quantum theory",
             "量子信息", "quantum information", "量子光学", "quantum optics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与主要结果）",
            "formalism（Hilbert 空间、算符与态空间设定）",
            "main results（定理/公式推导与证明）",
            "applications（物理应用或数值验证）",
            "discussion（与实验/文献对比）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical framework（量子力学基本公设回顾）",
            "main developments（按主题组织的进展综述）",
            "open problems（未解决问题）",
            "references",
        ),
        "pedagogical": (
            "abstract",
            "introduction",
            "background（公设与基本例子）",
            "main exposition（逐步推导与例题）",
            "exercises（练习）",
            "references",
        ),
    },
    citation_style="APS 样式（Physical Review 系列，作者-年份，REVTeX 模板）",
    reporting_standards={
        "hilbert_space": "态空间、内积与算符定义须明确；连续谱与离散谱须区分处理",
        "approximations": "近似方法（微扰、WKB、变分）须说明适用条件与误差估计",
        "units_convention": "自然单位（\\hbar=c=1）或原子单位须在开头声明并给出换算",
        "measurement": "测量与可观测量定义须符合公设；不确定性关系须注明态",
        "numerical_evidence": "数值结果须说明基组/截断与收敛性检查",
    },
    conventions=(
        "Dirac 记法统一：态用 |\\psi\\rangle，内积 \\langle\\phi|\\psi\\rangle，算符用 \\hat{A}",
        "对易子 [\\hat{A},\\hat{B}] 与反对易子 \\{\\hat{A},\\hat{B}\\} 记号全文一致",
        "单位约定（\\hbar=1 或保留 \\hbar）在引言处声明并全文遵守",
        "本征方程写作 \\hat{A}|a\\rangle = a|a\\rangle，注明简并情形",
        "密度算符 \\hat{\\rho} 与纯态/混合态区分须显式说明",
    ),
    key_venues=(
        "Physical Review Letters",
        "Physical Review A",
        "New Journal of Physics",
        "Journal of Physics A: Mathematical and Theoretical",
        "Reviews of Modern Physics",
        "Quantum (open access)",
    ),
    units_and_formulas_notes=(
        "常用自然单位 \\hbar=c=1；原子单位（Hartree、a_0）用于原子/分子计算时须声明",
        "能量单位 eV 与 Hartree 换算（1 Hartree ≈ 27.2114 eV）须给出",
        "公式用 amsmath；算符与态矢量用 \\hat 与 \\rangle 系列保持排版一致",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出基组大小、截断维度与收敛判据",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("Python (QuTiP)", "MATLAB", "Mathematica"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)