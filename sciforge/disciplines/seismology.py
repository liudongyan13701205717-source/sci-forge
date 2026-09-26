"""地震学学科论文支持：震源/波传播/工程地震体裁、AGU 引用样式与地震度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="seismology",
    aliases=("seismology", "地震学", "震源机制", "地震波"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "observational_study": (
            "abstract",
            "introduction",
            "data（地震目录与波形数据）",
            "methods（分析方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "modeling_study": (
            "abstract",
            "introduction",
            "model description（模型描述）",
            "inversion（反演方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="AGU 样式（作者-年份；JGR-Solid Earth 遵循 AGU 规范）",
    reporting_standards={
        "observational": "观测研究遵循地震观测数据报告规范",
        "modeling": "震源建模研究遵循反演报告规范",
        "hazard": "地震危险性遵循概率危险性评估报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循数据描述符规范",
    },
    conventions=(
        "台网与数据来源须报告",
        "震源参数（矩震级/深度/机制）须说明",
        "反演方法与不确定性须报告",
        "速度模型须注明",
        "目录完整性须评估",
    ),
    key_venues=(
        "Journal of Geophysical Research: Solid Earth",
        "Bulletin of the Seismological Society of America",
        "Geophysical Journal International",
        "Seismological Research Letters",
        "Earthquake Spectra",
        "Geophysical Research Letters",
    ),
    units_and_formulas_notes=(
        "震级用 Mw/Ml；距离用 km；深度用 km",
        "加速度用 g 或 cm/s²；频率用 Hz",
        "公式用 amsmath；波动方程须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "坐标用经纬度并注明基准",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("MATLAB", "R", "ObsPy", "地震台网"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)