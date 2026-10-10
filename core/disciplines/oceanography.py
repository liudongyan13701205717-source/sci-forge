"""海洋学学科论文支持：物理/化学/生物海洋体裁、AGU 引用样式与海洋度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="oceanography",
    aliases=("oceanography", "海洋学", "物理海洋", "海洋科学", "物理海洋学", "海洋物理"),
    paper_types={
        "research": ("abstract", "introduction（背景与科学问题）", "methodology（观测与建模方法）", "results（结果与量化）", "discussion（机理与讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（观测/事件描述）", "analysis（分析方法）", "results（结果）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="AGU 样式",
    reporting_standards={"observational": "遵循观测数据报告规范", "modeling": "遵循模式评估规范", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("观测平台须报告（船基/浮标/卫星）", "时空分辨率须说明", "数据来源与质量控制须报告", "坐标须用经纬度并注明基准", "模式参数化须说明"),
    key_venues=("Journal of Geophysical Research: Oceans", "Journal of Physical Oceanography", "Deep-Sea Research Part I", "Limnology and Oceanography", "Ocean Modelling"),
    units_and_formulas_notes=("温度用 °C", "盐度用 PSU", "流速用 m/s 或 Sv", "深度用 m", "公式用 amsmath"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("CTD 剖面仪", "ADCP 声学多普勒流速仪", "Argo 剖面浮标", "Slocum Glider", "Seaglider", "Underwater ROV", "卫星测高技术", "Jason 卫星雷达高度计", "Argos 传输系统", "Del Mar Wirewalker", "Ocean Mooring 系统", "Hydrophone", "SBE 9plus", "Wet Labs fluorometer", "Python", "MATLAB", "NetCDF", "CFD 建模软件", "MITgcm", "NEMO"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
