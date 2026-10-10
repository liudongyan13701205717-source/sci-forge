"""餐饮与酒店服务学科论文支持：餐饮管理、酒店运营与服务质量管理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_and_hospitality_services",
    aliases=("food_and_hospitality_services", "餐饮与酒店服务", "酒店管理", "餐饮服务", "餐饮管理", "酒店运营", "宴会服务", "食品安全服务"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "ISO 9001 服务质量标准", "k2": "中国餐饮行业服务规范", "k3": "酒店业 AAA 评定标准"},
    conventions=("顾客满意度须注明样本量与量表", "运营成本须注明统计周期", "服务质量须注明评估维度（TQM/ServQual）", "案例须匿名化处理", "财务数据须注明口径"),
    key_venues=("Cornell Hospitality Research", "International Journal of Hospitality Management", "Tourism Management", "Journal of Foodservice Business Research", "中国餐饮学报"),
    units_and_formulas_notes=("客流量单位：人次/天", "坪效：元/㎡·月", "翻台率：次/天", "顾客满意度：1-5 分（Likert）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS（问卷调查分析）", "NVivo（访谈质性分析）", "AMOS（结构方程）", "Mplus（结构方程）", "SurveyMonkey（在线问卷）", "Pos 餐饮管理系统", "Tableau（数据可视化）", "Power BI", "LaTeX（排版）", "EndNote（文献管理）", "RStudio", "Excel 数据分析", "Google Forms（问卷）", "Credible（网络口碑抓取）", "Python 爬虫（评价分析）", "TextBlob（情感分析）", "Origin（数据绘图）", "Adobe Photoshop（图表美化）", "QGIS（门店选址分析）", "Sona 调查平台"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
