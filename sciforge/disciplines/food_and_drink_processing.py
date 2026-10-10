"""食品与饮料加工学科论文支持：食品工艺技术、饮料制备与食品工程研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_and_drink_processing",
    aliases=("food_and_drink_processing", "食品与饮料加工", "食品加工", "饮料生产", "食品工艺", "乳品加工", "烘焙工程", "食品工程"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "ICH Q3B 食品接触材料", "k2": "GB 14881 食品生产卫生标准", "k3": "Codex 食品工艺标准"},
    conventions=("工艺参数须注明温度、时间、压力等条件", "食品组分须标注质量分数（g/kg）", "pH 值须注明测量温度", "感官评价须注明评分人数与量表", "样品批次须注明生产日期"),
    key_venues=("Food Chemistry", "Journal of Food Science", "LWT - Food Science and Technology", "Food and Bioproducts Processing", "Innovative Food Science and Emerging Technologies"),
    units_and_formulas_notes=("含水量：%（w/w）", "pH 值须注明温度（25 ℃）", "质构参数：N·mm", "保质期试验须注明储存条件（温度/湿度）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("质构仪 (Texture Analyzer)", "色差仪 (Colorimeter)", "气相色谱仪 (GC)", "液相色谱仪 (HPLC)", "近红外光谱仪 (NIR)", "扫描电子显微镜 (SEM)", "傅里叶变换红外光谱 (FTIR)", "流变仪 (Rheometer)", "水分活度仪 (Water Activity Meter)", "高压均质机", "超高压处理装置 (HPP)", "微波处理系统", "电子鼻 (E-Nose)", "SPSS（感官统计）", "Origin（数据绘图）", "RStudio", "LaTeX（排版）", "EndNote（文献管理）", "Sensory Evaluation Software", "Python（数据处理）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
