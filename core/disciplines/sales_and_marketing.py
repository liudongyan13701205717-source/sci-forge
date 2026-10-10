"""销售与营销学科论文支持：营销/销售管理/消费者行为体裁与 APA 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sales_and_marketing",
    aliases=("sales_and_marketing", "销售与营销", "销售营销", "市场营销", "sales management", "marketing management", "消费者行为", "品牌管理"),
    paper_types={
        "research": ("abstract", "introduction（营销问题与假设）", "methodology（研究设计与样本）", "results（数据结果）", "discussion（营销启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（营销案例背景）", "analysis（策略与效果分析）", "results（业务结果）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（营销理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"case_study": "案例研究遵循 COREQ 报告规范", "survey": "消费者调查遵循 AAPOR 规范", "meta_analysis": "元分析遵循 PRISMA 声明"},
    conventions=("消费者术语须全文一致", "样本量与抽样方法须报告", "效应量须与显著性一同报告", "营销实验须给出效应量", "品牌与产品信息须匿名化"),
    key_venues=("Journal of Marketing", "Journal of Marketing Research", "Journal of Consumer Research", "Journal of the Academy of Marketing Science", "Marketing Science", "MIS Quarterly"),
    units_and_formulas_notes=("转化率以 % 记", "ROI 计算式给出公式", "样本量公式与置信度须明确", "统计显著性阈值 α=0.05 默认"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "Excel", "Tableau", "Power BI", "Google Analytics (GA4)", "Google Ads", "Google Trends", "Facebook Ads Manager", "Salesforce", "HubSpot", "CRM Analytics", "Adobe Analytics", "Nielsen", "Comscore", "Qualtrics", "SurveyMonkey", "NVivo", "MAXQDA"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
