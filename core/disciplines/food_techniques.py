"""食品工艺学学科论文支持：食品原料处理、工艺方法与操作技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_techniques",
    aliases=("food_techniques", "食品工艺学", "食品加工技术", "food techniques", "食品工艺", "食品操作技术", "食品制备", "食品加工方法"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "食品工艺参数报告规范（工艺报告）", "k2": "食品质量检验规范（国标/AOAC）", "k3": "食品操作规程 SOP（SOP 报告）"},
    conventions=("工艺参数（温度/时间/转速/压力）须完整记录且可复现", "原料规格与产地须说明", "工艺步骤须编号并说明操作要点", "成品质量指标须按国标检测", "对比实验须说明对照组设置"),
    key_venues=("Journal of Food Processing and Preservation", "Food Technology and Biotechnology", "International Journal of Food Science & Technology", "Journal of Food Engineering", "LWT - Food Science and Technology"),
    units_and_formulas_notes=("水分活度 aw 无量纲（0-1）", "杀菌强度用 F 值（°C·s）", "干燥速率用 g/(m²·s)", "工艺能耗用 kWh/kg 或 MJ/kg"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("食品蒸汽灭菌釜 Retort", "食品离心喷雾干燥机", "食品冷冻干燥机冻干机", "食品真空冷冻干燥机", "食品高压均质机", "食品离心脱水机", "食品超声食品处理设备", "食品高压脉冲电场设备 PEF", "食品超临界 CO₂ 萃取装置", "食品 3D 打印机", "食品真空包装测试机", "食品质构仪 Texture Analyzer", "食品流变仪 Rheometer", "食品电子鼻 E-nose", "食品色度计", "食品电子温度记录仪", "食品真空包装机", "食品微胶囊制备设备", "食品食品X射线检测系统", "食品食品离心喷雾干燥机"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
