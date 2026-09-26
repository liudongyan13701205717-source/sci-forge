"""统计力学学科论文支持：统计物理/系综理论体裁、APS 引用样式与统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="statistical_mechanics",
    aliases=("statistical mechanics", "统计力学", "统计物理", "statistical physics",
             "系综理论", "ensemble theory", "相变", "phase transitions"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与模型）",
            "model（Hamiltonian 与系综设定）",
            "methods（解析/数值方法）",
            "results（配分函数、序参量或临界指数）",
            "discussion（与实验/文献对比）",
            "conclusion",
            "references",
        ),
        "computational": (
            "abstract",
            "introduction",
            "model（格点模型或连续模型）",
            "numerical method（Monte Carlo/MD、有限尺寸标度）",
            "results（热力学量、关联函数与临界行为）",
            "validation（与解析解对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical framework（系综与涨落理论）",
            "main developments（按主题综述）",
            "open problems",
            "references",
        ),
    },
    citation_style="APS 样式（Physical Review 系列，作者-年份，REVTeX 模板）",
    reporting_standards={
        "ensemble": "所用系综（微正则/正则/巨正则）须声明，并给出配分函数定义",
        "thermodynamic_limit": "热力学极限与有限尺寸效应须讨论",
        "critical_behavior": "临界指数与普适类结论须给出标度分析与误差",
        "simulation_details": "Monte Carlo/MD 须报告样本数、热化时间、步长与误差棒",
        "ergodicity": "遍历性假设与破缺情形须说明",
    },
    conventions=(
        "配分函数 Z 与自由能 F 的关系（F = -k_B T ln Z）须明确",
        "Boltzmann 常数 k_B 保留或取 k_B=1 须声明并全文一致",
        "系综平均用 \\langle \\cdot \\rangle 记号，注明系综类型",
        "序参量（磁化强度、密度差等）定义须给出",
        "关联函数与结构因子定义须与模型一致",
    ),
    key_venues=(
        "Physical Review E",
        "Physical Review Letters",
        "Journal of Statistical Mechanics: Theory and Experiment (JSTAT)",
        "Journal of Statistical Physics",
        "Journal of Chemical Physics",
        "Physical Review X",
    ),
    units_and_formulas_notes=(
        "常用单位制：k_B=1 或保留 k_B；温度以 K 或能量单位给出",
        "格点模型能量单位（如 J）须声明；连续模型给出势参数",
        "公式用 amsmath；系综平均与配分函数排版统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出统计误差（标准误）与样本独立性说明",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("Python (NumPy, SciPy)", "MATLAB", "LAMMPS"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)