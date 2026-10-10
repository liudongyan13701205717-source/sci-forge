"""乳制品零售学科论文支持：乳制品营销、供应链与零售管理研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dairy_retailing",
    aliases=(
        "dairy_retailing", "乳制品零售",
        "dairy retail", "乳品零售",
        "dairy marketing", "乳品营销",
        "dairy supply chain", "乳品供应链",
        "retail management", "零售管理",
        "dairy distribution", "乳品分销",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（零售问题与背景）",
            "method（研究设计、市场分析、销售数据）",
            "results（销售效果与市场评估）",
            "discussion（零售优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "market analysis（市场分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "market overview（市场综述）",
            "comparison（模式对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "data": "销售数据须注明来源与时间",
        "market": "市场分析须注明样本量与方法",
        "statistics": "统计检验须注明方法与显著性水平",
    },
    conventions=(
        "销售额用 元 表示",
        "时间用 年/月 表示",
        "市场份额用 % 表示",
        "增长率用 % 表示",
        "统计检验注明 t/F/χ² 值、p 值与 95% CI",
    ),
    key_venues=(
        "Journal of Retailing",
        "Journal of Business Research",
        "International Journal of Retail & Distribution Management",
        "Journal of Food Products Marketing",
        "British Food Journal",
        "Journal of Consumer Marketing",
    ),
    units_and_formulas_notes=(
        "销售额用 元 表示",
        "时间用 年/月 表示",
        "市场份额与增长率用 % 表示",
        "统计检验注明 t/F/χ² 值、p 值与 95% CI"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "Python (pandas, numpy)", "Excel", "Tableau", "Power BI", "Google Analytics", "POS System", "ERP System", "CRM Software", "Inventory Management Software", "Supply Chain Management Software", "Market Research Software", "SurveyMonkey", "Qualtrics", "Google Forms", "Social Media Analytics", "Customer Feedback Software", "NielsenIQ", "Winshoppers"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
