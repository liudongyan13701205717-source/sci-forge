"""水文地质学科论文支持：地下水/水化学/同位素研究体裁、GS/AGU 引用样式与水文地质记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hydrogeology",
    aliases=("hydrogeology", "水文地质", "地下水", "地下水动力学", "水化学", "同位素示踪", "含水层", "地下水污染", "地质勘探"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（钻孔、抽水与采样）", "results（水动力与水化学结果）", "discussion（机理与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（含水层与场地）", "analysis（水文地质分析）", "results（资源/污染评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（水动力学理论）", "evidence synthesis（文献综合）", "future directions", "references"),
    },
    citation_style="AGU 样式（作者-年份；Ground Water 遵循 GSA/AGU 规范）",
    reporting_standards={
        "pumping_test": "抽水试验遵循 IASH 抽水试验报告规范",
        "water_chemistry": "水化学遵循地下水水质报告规范",
        "isotope": "同位素分析遵循 δD/δ¹⁸O 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "numerical": "数值模拟遵循模型率定验证报告规范",
    },
    conventions=(
        "钻孔深度与含水层参数须报告",
        "采样点与测点标高须一致",
        "抽水试验恢复段须分析",
        "同位素标注‰与偏差标准",
        "单位换算（m、L/s、mg/L）须规范",
    ),
    key_venues=(
        "Ground Water",
        "Hydrogeology Journal",
        "Journal of Hydrology",
        "Hydrology and Earth System Sciences",
        "Applied Geochemistry",
        "Water Resources Research",
    ),
    units_and_formulas_notes=(
        "水位用 m；渗透系数用 m/d",
        "浓度用 mg/L 或 μmol/L；总溶解固体 TDS 用 mg/L",
        "同位素 δ 用 ‰（VSMOW）；公式用 amsmath 并编号",
        "数值结果给出均值 ± 标准差与样本量",
        "等水位线步长与流向须注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MODFLOW", "GMS", "TOUGH2", "Python", "R", "MATLAB", "QGIS", "ArcGIS", "Surfer", "GMSW", "PHREEQC", "Isotope Ratio Mass Spectrometer", "GC-MS", "原子吸收光谱仪", "LaTeX", "Excel", "EndNote", "Zotero", "SolidWorks", "Git"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
