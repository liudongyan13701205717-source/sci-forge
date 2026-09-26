"""海洋学学科论文支持：物理/化学/生物海洋体裁、AGU 引用样式与海洋度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="oceanography",
    aliases=("oceanography", "海洋学", "物理海洋", "海洋科学"),
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
            "methods（分析方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "modeling_study": (
            "abstract",
            "introduction",
            "model description（模式描述）",
            "experiments（实验设计）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="AGU 样式（作者-年份；JGR-Oceans 遵循 AGU 规范）",
    reporting_standards={
        "observational": "观测研究遵循海洋观测数据报告规范",
        "modeling": "模式研究遵循模式评估报告规范",
        "experimental": "实验遵循海洋实验报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循数据描述符规范",
    },
    conventions=(
        "观测平台（船基/浮标/卫星）须报告",
        "时间与空间分辨率须说明",
        "数据来源与质量控制须报告",
        "模式配置与参数化须说明",
        "单位与参考系须一致",
    ),
    key_venues=(
        "Journal of Geophysical Research: Oceans",
        "Journal of Physical Oceanography",
        "Deep-Sea Research Part I/II",
        "Limnology and Oceanography",
        "Ocean Modelling",
        "Progress in Oceanography",
    ),
    units_and_formulas_notes=(
        "温度用 °C；盐度用 PSU；深度用 m",
        "流速用 m/s 或 Sv（10⁶ m³/s）",
        "公式用 amsmath；控制方程须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "坐标用经纬度（°N/°E）并注明基准",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("R", "Python", "CTD 剖面仪", "海洋浮标"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)