"""大地测量学学科论文支持：GNSS/重力/参考框架体裁、AGU 引用样式与测地度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geodesy",
    aliases=("geodesy", "大地测量学", "GNSS", "测量学"),
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
            "data（观测数据）",
            "processing（数据处理）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "reference_frame_paper": (
            "abstract",
            "introduction",
            "data（数据）",
            "method（参考框架实现方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="AGU 样式（作者-年份；JGR-Solid Earth 遵循 AGU 规范）",
    reporting_standards={
        "observational": "观测研究遵循大地测量观测报告规范",
        "processing": "数据处理遵循 GNSS 处理报告规范",
        "modeling": "建模研究遵循地球物理反演报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循测地数据规范",
    },
    conventions=(
        "参考框架（ITRF 等）须注明",
        "处理软件与策略须报告",
        "误差与不确定性须报告",
        "时间序列须注明时段与采样",
        "坐标基准须一致",
    ),
    key_venues=(
        "Journal of Geodesy",
        "Journal of Geophysical Research: Solid Earth",
        "Geophysical Journal International",
        "GPS Solutions",
        "Journal of Geodynamics",
        "Geophysical Research Letters",
    ),
    units_and_formulas_notes=(
        "坐标用 m；速度用 mm/a；重力用 mGal",
        "精度用 mm 或 ppb",
        "公式用 amsmath；平差方程须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "时间用 GPS 周或历元并注明系统",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("GNSS 接收机与数据采集系统", "Bernese GPS Processing Software", "MATLAB", "Python（NumPy/PyGMTSAR）",
           "精密重力仪（超导/绝对重力仪）", "参考框架处理软件（ITRF 实现）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Zenodo", "Semantic Scholar"),
)