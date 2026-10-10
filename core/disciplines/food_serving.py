"""食品服务学科论文支持：餐饮服务管理、食品服务运营与服务品质。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_serving",
    aliases=("food_serving", "食品服务", "餐饮服务", "food service", "餐饮管理", "酒店餐饮", "食品供应", "餐饮服务管理"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "餐饮服务卫生标准（国标/FDA 规范）", "k2": "食品服务运营管理规范（SOP）", "k3": "顾客满意度调查规范（量表报告）"},
    conventions=("餐饮卫生指标须按国标或 FDA 规范检测", "服务品质须说明测量方法与量表", "运营成本须注明统计口径（食材/人工/能耗）", "案例须说明餐厅类型与规模", "讨论须结合餐饮行业实践"),
    key_venues=("International Journal of Hospitality Management", "Journal of Foodservice Management", "Cornell Hospitality Research", "International Journal of Food Science", "Journal of Restaurant and Foodservice Research"),
    units_and_formulas_notes=("运营成本以元/份或元/人/天计", "客流量以人/小时或人/天计", "食品损耗率用 %", "顾客满意度用 1-5 量表或百分制"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("餐饮 POS 收银系统", "餐饮库存管理软件", "餐饮食品温度记录仪", "餐饮 HACCP 食品安全管理软件", "顾客满意度调查平台", "餐饮 SaaS 预订系统", "餐饮排班管理软件", "餐饮外卖配送系统", "餐饮食品消毒检测设备", "餐饮食品安全快速检测仪", "餐饮厨房排烟设备", "餐饮食品保温设备", "餐饮食品冷链监控设备", "餐饮食品留样柜", "餐饮厨房电子温控仪", "餐饮食品留样快速培养仪", "餐饮食品安全检测试纸", "餐饮食品消毒超声波清洗机", "餐饮厨房食品离心脱水机", "餐饮食品离心喷雾干燥机"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
