"""食品处理与卫生学科论文支持：食品安全、食品卫生与卫生管理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_handlinghygiene",
    aliases=("food_handlinghygiene", "食品处理与卫生", "食品卫生", "食品安全卫生", "食品处理", "食品卫生管理", "食品安全规范", "餐饮卫生"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "HACCP 体系标准", "k2": "GB 31654 食品安全国家标准", "k3": "Codex 食品法典"},
    conventions=("微生物指标须注明检测方法与检出限", "菌落总数单位：CFU/g", "食品安全风险评估须注明暴露频率", "现场卫生评分须注明检查表", "农药残留须注明最大残留限量（MRL）"),
    key_venues=("Food Control", "International Journal of Food Microbiology", "Journal of Food Protection", "Food Safety and Quality", "中国食品卫生学"),
    units_and_formulas_notes=("菌落总数：CFU/g（或 CFU/mL）", "大肠菌群：MPN/100 mL", "农药残留：μg/kg（mg/kg）", "温度记录须注明 ℃"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ATP 生物荧光检测仪", "快速菌落检测仪", "微生物培养箱", "全自动血细胞计数仪", "PCR 仪（核酸检测）", "液相色谱仪 (HPLC)", "气相色谱-质谱联用仪 (GC-MS)", "免疫层析试纸条", "食品安全快速检测仪", "红外温度计", "温湿度记录仪", "SPSS（统计检验）", "RStudio", "Origin（数据绘图）", "LaTeX（排版）", "EndNote（文献管理）", "Python（数据分析）", "HACCP 评估软件", "QGIS（卫生分布制图）", "Sona 调查平台"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
