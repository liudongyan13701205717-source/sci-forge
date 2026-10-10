"""食品科学学科论文支持：食品化学、食品安全、营养成分与感官评价。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_science",
    aliases=("food_science", "食品科学", "食品化学", "food science", "food chemistry", "食品安全", "食品营养", "食品感官"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ACS 样式（上标编号），如 ¹ 或 [1]",
    reporting_standards={"k1": "食品安全性须报告微生物指标（HACCP 报告）", "k2": "感官评价须报告方法（QDA/TC/9点标度）与评价员信息（感官报告）", "k3": "营养成分须报告分析方法（AOAC/国标）与检测值（营养报告）"},
    conventions=("食品添加剂用 INN 或 E 编号", "微生物用标准培养基与计数方法（平板计数/MPN/PCR）", "仪器分析须报告色谱/质谱条件（柱温/流动相/检测波长）", "感官描述词用标准词典（如 Sensory Wheel）", "所有实验至少三次独立重复"),
    key_venues=("Food Chemistry", "Journal of Agricultural and Food Chemistry", "Food Research International", "LWT - Food Science and Technology", "Journal of Food Science"),
    units_and_formulas_notes=("浓度用 mg/kg（ppm）或 mg/L", "水分活度 aw 无量纲（0-1）", "质构用 N（硬度）和 mm（弹性）", "色泽用 L*a*b* 值；色差用 ΔE"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("HPLC 高效液相色谱仪", "GC-MS 气相色谱质谱联用仪", "LC-MS/MS 液质联用仪", "食品质构仪 Texture Analyzer", "近红外光谱仪 NIR", "食品色度计", "电子鼻 E-nose", "食品流变仪", "食品 X 射线荧光仪 XRF", "FTIR 傅里叶变换红外光谱仪", "食品水分活度仪", "食品离心脱水机", "SPSS 统计软件", "Origin 绘图软件", "Python 数据分析", "R 统计分析", "MATLAB", "食品感官评价软件 Sensory Suite", "食品电子舌 E-tongue", "食品冷冻干燥机冻干机"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
