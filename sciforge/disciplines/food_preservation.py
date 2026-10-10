"""食品保藏学科论文支持：食品保鲜、防腐技术与贮藏条件研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_preservation",
    aliases=("food_preservation", "食品保藏", "食品保鲜", "食品防腐", "食品贮藏", "冷藏技术", "干燥保藏", "冷链物流"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "ISO 8361 食品干燥标准", "k2": "GB 14881 食品生产卫生标准", "k3": "Codex 食品保藏指南"},
    conventions=("贮藏条件须注明温度、相对湿度与气体组成", "保质期须注明试验温度条件", "水分活度须注明温度", "微生物指标须注明检测方法与计数单位", "干燥试验须注明初始含水量"),
    key_venues=("Postharvest Biology and Technology", "LWT - Food Science and Technology", "Food Control", "Journal of Food Engineering", "食品科学"),
    units_and_formulas_notes=("水分活度 aw（0-1）", "相对湿度：%RH", "水分含量：%（w/w）", "贮藏温度：℃"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("水分活度仪", "气调保鲜箱", "温湿度记录仪", "真空冷冻干燥机", "热风循环烘箱", "超高压处理装置 (HPP)", "微波干燥设备", "近红外光谱仪 (NIR)", "色差仪", "质构仪", "气相色谱仪 (GC)", "液相色谱仪 (HPLC)", "电子鼻 (E-Nose)", "SPSS（统计检验）", "Origin（数据绘图）", "RStudio", "LaTeX（排版）", "EndNote（文献管理）", "Python（数据处理）", "冷量计算软件"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
