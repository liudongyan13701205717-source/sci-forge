"""核与等离子体物理学科论文支持：等离子体物理/磁约束/聚变体裁、APS 引用样式与等离子体记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nuclear_and_plasma_physics",
    aliases=("nuclear_and_plasma_physics", "核与等离子体物理", "Nuclear And Plasma Physics",
             "plasma physics", "等离子体物理", "plasma confinement",
             "磁约束", "magnetic confinement", "聚变物理", "fusion physics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与等离子体问题）",
            "methodology（实验与仿真方法）",
            "results（等离子体参数）",
            "discussion（物理解释）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例与装置）",
            "analysis（等离子体行为分析）",
            "results（发现与优化）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（等离子体理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APS 样式（作者-年份，物理期刊规范）",
    reporting_standards={
        "experimental": "实验遵循等离子体实验报告规范",
        "simulation": "仿真遵循 SOLPS/EDGE2D 报告规范",
        "data": "数据集遵循 IAEA/IAEA 共享规范",
        "uncertainty": "统计与系统不确定度须分别报告",
        "safety": "装置安全遵循 IAEA 标准",
    },
    conventions=(
        "等离子体参数须标注 n_e/T_e/β",
        "磁场用 T 或 kG",
        "能量用 eV",
        "频率用 Hz 或 kHz",
        "公式用 amsmath；显示公式编号",
    ),
    key_venues=(
        "Physics of Plasmas",
        "Plasma Physics and Controlled Fusion",
        "Nuclear Fusion",
        "Physical Review Letters",
        "Journal of Plasma Physics",
        "Review of Scientific Instruments",
    ),
    units_and_formulas_notes=(
        "密度 n_e 用 10^20 m^-3；温度 T_e 用 keV",
        "磁场用 T；电流用 MA",
        "能量用 eV；时间用 s",
        "公式用 amsmath；显示公式编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("GENE", "NIMBUS", "M3D1", "TRANSP", "ONETOP", "MASTOR", "JUDY", "MARS", "MEGA", "ASTRA", "GYRO", "NUBEAM", "TRITON", "ORBIT", "TRAVIS", "NCOMPS", "SOLPS", "EDGE2D", "GECOM", "Python (NumPy, SciPy)"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)
