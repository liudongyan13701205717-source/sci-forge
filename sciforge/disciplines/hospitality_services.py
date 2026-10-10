"""酒店管理学科论文支持：酒店运营、旅游服务与宾客体验研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hospitality_services",
    aliases=("hospitality_services", "酒店管理", "酒店管理与服务", "旅游服务", "餐饮管理", "Hospitality Services", "Hotel Management", "Tourism Management", "Restaurant Management", "Service Operations"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "AAHOPE 酒店管理研究规范", "k2": "WTA Tourism Research Guidelines", "k3": "GB/T 14308 星级旅游饭店标准"},
    conventions=("样本须标注入住/消费时段", "满意度评分须注明量表版本", "OTA 评价须注明抓取日期与语言", "案例须注明匿名化标识", "服务交互须注明触点（Moments of Truth）"),
    key_venues=("International Journal of Hospitality Management", "Tourism Management", "Journal of Travel Research", "Annals of Tourism Research", "Cornell Hospitality Quarterly"),
    units_and_formulas_notes=("房价：CNY/USD 每间夜", "入住率：%", "RevPAR：房价 × 入住率", "NPS：-100 到 +100"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R（统计建模）", "Stata", "Amos（结构方程建模）", "Mplus", "Harmon 量表信效度工具", "NVivo（质性分析）", "MAXQDA", "Qualtrics（宾客满意度）", "SurveyMonkey", "Google Forms", "PMS（Property Management System）", "Opera Cloud（酒店 PMS）", "Expedia 评论 API", "TripAdvisor API", "Bing Place API", "Tableau（可视化）", "Python（文本挖掘）", "EndNote", "Zotero"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
