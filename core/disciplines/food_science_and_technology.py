"""食品科学与技术学科论文支持：食品科学技术、功能性与工艺创新。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_science_and_technology",
    aliases=("food_science_and_technology", "食品科学与技术", "食品科学", "食品工程", "food science and technology", "食品技术", "食品工艺", "食品创新"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "工艺参数须报告温度/时间/压力/pH（工艺报告）", "k2": "设备规格与型号须说明（设备报告）", "k3": "功能成分须报告定量方法与检出限（功能报告）"},
    conventions=("工艺参数（温度/时间/压力/pH）与设备规格须完整记录", "新型食品须说明工艺原理与关键控制点", "功能成分须报告定量方法与检出限", "营养成分须按国标或 AOAC 方法检测", "创新工艺须与对照工艺比较"),
    key_venues=("Innovative Food Science & Technology", "Food and Bioproducts Processing", "Journal of Food Engineering", "Trends in Food Science & Technology", "LWT - Food Science and Technology"),
    units_and_formulas_notes=("水分活度 aw 无量纲（0-1）", "杀菌强度用 F 值（°C·s）", "功能成分浓度用 mg/kg（ppm）或 μg/g", "能耗与得率用 kWh/t、g/kg 或 %"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("HPLC 高效液相色谱仪", "近红外光谱仪 NIR", "食品流变仪 Rheometer", "食品质构仪 Texture Analyzer", "食品电子鼻 E-nose", "食品电子舌 E-tongue", "食品冷冻干燥机冻干机", "超临界 CO₂ 萃取装置", "高压脉冲电场设备 PEF", "超声波食品处理设备", "食品离心喷雾干燥机", "食品真空冷冻干燥机", "3D 食品打印机", "食品微胶囊制备设备", "食品色度计", "食品离心脱水机", "FTIR 傅里叶变换红外光谱仪", "食品 X 射线荧光仪 XRF", "食品电子温度记录仪", "食品高压均质机"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
