"""经济学与商业学科论文支持：企业战略、市场分析与商业研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="economics_business",
    aliases=(
        "economics_business", "经济学与商业",
        "business economics", "商业经济学",
        "business strategy", "企业战略",
        "market analysis", "市场分析",
        "financial economics", "金融经济学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（商业问题与背景）",
            "method（研究方法、数据分析、案例）",
            "results（研究结果与商业启示）",
            "discussion（策略优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（商业分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "market overview（市场综述）",
            "comparison（竞争对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "data": "数据来源须注明",
        "method": "研究方法须明确",
        "robustness": "稳健性检验须完整",
    },
    conventions=(
        "货币用 美元/人民币 表示",
        "时间用 年/季度 表示",
        "统计检验须注明 t/F 值、p 值与 95% CI",
        "数据来源须标注机构与年份",
    ),
    key_venues=(
        "Journal of Business Finance and Accounting",
        "Journal of Economic Perspectives",
        "American Economic Review",
        "Quarterly Journal of Economics",
        "Review of Financial Studies",
        "Journal of Finance",
    ),
    units_and_formulas_notes=(
        "货币用 美元/人民币 表示",
        "时间用 年/季度 表示",
        "收益率用 % 表示",
        "统计检验须注明 t/F 值、p 值与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R (RStudio)", "Python (pandas, statsmodels)", "Excel", "SPSS", "EViews", "MATLAB", "SAS", "Origin", "Tableau", "Power BI", "Bloomberg", "Reuters Eikon", "Capital IQ", "FactSet", "Wind", "Bloomberg Terminal", "Yahoo Finance", "Google Finance", "World Bank Data"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
