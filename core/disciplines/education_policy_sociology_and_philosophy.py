"""教育政策、社会学与哲学学科论文支持：教育政策、教育社会学与教育哲学研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="education_policy_sociology_and_philosophy",
    aliases=(
        "education_policy_sociology_and_philosophy", "教育政策社会学与哲学",
        "education policy", "教育政策",
        "sociology of education", "教育社会学",
        "philosophy of education", "教育哲学",
        "education governance", "教育治理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（政策/社会问题与背景）",
            "method（研究设计、政策分析、社会调查）",
            "results（政策效果与社会影响）",
            "discussion（政策优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "policy analysis（政策分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "policy": "政策分析须注明数据来源与时间",
        "society": "社会调查须注明样本量与方法",
        "philosophy": "哲学论证须注明理论框架",
    },
    conventions=(
        "政策名称须使用官方名称",
        "统计数据须注明来源与年份",
        "哲学概念须定义清晰",
        "社会影响须区分短期与长期",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Educational Philosophy and Theory",
        "British Journal of Educational Sociology",
        "Journal of Education Policy",
        "Educational Administration Quarterly",
        "Comparative Education Review",
        "Journal of Philosophy of Education",
    ),
    units_and_formulas_notes=(
        "统计检验注明 t/F/χ² 值、p 值与效应量",
        "政策效果用 百分比/百分点 表示",
        "社会调查用 样本量/置信区间 表示",
        "哲学概念须定义清晰",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "NVivo", "Atlas.ti", "MAXQDA", "Google Forms", "Qualtrics", "SurveyMonkey", "ERIC", "World Bank Data", "OECD Data", "UNESCO Data", "Eurostat", "Statista", "Tableau", "Power BI", "LaTeX", "MS Word"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "JSTOR", "Google Scholar", "PubMed"),
)
