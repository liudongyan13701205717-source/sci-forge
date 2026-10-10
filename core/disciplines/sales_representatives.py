"""销售代表学科论文支持：职业销售/销售技巧/客户关系体裁与 APA 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sales_representatives",
    aliases=("sales_representatives", "销售代表", "职业销售", "销售技巧", "sales representatives", "field sales", "客户销售", "销售管理"),
    paper_types={
        "research": ("abstract", "introduction（销售问题与研究动机）", "methodology（研究设计）", "results（销售绩效数据）", "discussion（技能与策略讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（销售代表案例）", "analysis（谈判与策略分析）", "results（业绩结果）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（销售理论综述）", "evidence synthesis（实证综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"case_study": "案例研究遵循 COREQ 规范", "survey": "销售代表调查遵循 AAPOR 规范", "mixed_method": "混合方法遵循 COREQ 与 SRQR"},
    conventions=("销售绩效指标须给出定义（成单率/客单价/复购率）", "样本须区分直销与直销代理", "谈判术语须统一", "访谈须编码并报告信度", "客户数据须匿名化"),
    key_venues=("Journal of Selling & Marketing", "Industrial Marketing Management", "Journal of Business & Industrial Marketing", "Journal of Personal Selling & Sales Management", "European Journal of Marketing", "Industrial Marketing Management Quarterly"),
    units_and_formulas_notes=("客单价以元/美元记", "成单率以 % 记", "销售漏斗转化率给出层级", "样本量与置信区间须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Salesforce", "HubSpot", "Zoho CRM", "Microsoft Dynamics CRM", "Pipedrive", "Apollo.io", "LinkedIn Sales Navigator", "ZoomInfo", "Ontraport", "Monday CRM", "SPSS", "R", "Stata", "Excel", "Tableau", "Power BI", "Qualtrics", "SurveyMonkey", "NVivo", "MAXQDA"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
