"""沙龙服务学科论文支持：美容美发/美甲/身体护理服务业体裁与案例研究规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="salon_services",
    aliases=("salon_services", "沙龙服务", "美发服务", "美甲服务", "美容服务", "salon services", "beauty salon", "职业美容"),
    paper_types={
        "research": ("abstract", "introduction（服务问题与动机）", "methodology（研究设计）", "results（服务效果数据）", "discussion（服务启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（沙龙服务案例）", "analysis（服务流程分析）", "results（顾客满意度）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（服务理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"case_study": "案例研究遵循 COREQ 规范", "survey": "顾客调查遵循 AAPOR 规范", "workplace": "职业研究遵循 ISO 11238 卫生规范"},
    conventions=("服务术语须定义（剪/染/烫/护理等）", "顾客样本须报告人口学特征", "满意度量表须报告 Cronbach's α", "职业风险须讨论（感染/化学品）", "化学产品须给出成分与浓度"),
    key_venues=("Journal of Cosmetic Dermatology", "Journal of the American Academy of Dermatology", "Cosmetic Science", "International Journal of Cosmetic Science", "Journal of Occupational Health", "Journal of Occupational Dermatology"),
    units_and_formulas_notes=("pH 值以无量纲记", "浓度以 % 或 mg/L 记", "温度以 °C 记", "样本量与置信区间须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Nail Polish Tester (UV)", "Salon Chemical pH Meter", "Hair Strength Tester", "Salon Air Purifier", "Steam Hair Dryer", "Permatron", "Salon Management Software (Lightspeed)", "Salon Suite", "MBS BeautySuite", "SpaSoft", "Adobe Photoshop", "Canva", "SPSS", "R", "Excel", "Tableau", "Qualtrics", "SurveyMonkey", "NVivo", "MAXQDA"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
