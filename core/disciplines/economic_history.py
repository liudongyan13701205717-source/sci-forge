"""经济史学科论文支持：经济史研究、计量分析与历史档案体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="economic_history",
    aliases=(
        "economic_history", "经济史", "经济史学",
        "history of economics", "经济史",
        "cliometrics", "新经济史",
        "historical economics", "历史经济学",
        "long-term economic change", "长期经济变迁",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与历史背景）",
            "method（数据来源与计量方法）",
            "results（实证结果与历史解释）",
            "discussion（经济含义与政策启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "historical context（历史背景）",
            "analysis（计量分析与解释）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence summary（证据总结）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式",
    reporting_standards={
        "data": "数据来源须注明（档案、年鉴、统计）",
        "method": "计量方法须明确",
        "robustness": "稳健性检验须完整",
    },
    conventions=(
        "历史地名须使用当时名称",
        "货币须注明年份与购买力平价",
        "数据来源须标注机构与年份",
        "统计检验须注明方法与显著性水平",
        "异质性分析须报告不同时期差异",
    ),
    key_venues=(
        "Journal of Economic History",
        "Economic History Review",
        "Cliometrica",
        "Explorations in Economic History",
        "Journal of Interdisciplinary History",
        "Historical Research",
    ),
    units_and_formulas_notes=(
        "货币用 美元（购买力平价）表示",
        "时间用 年 表示",
        "统计检验须注明 t/F 值、p 值与 95% CI",
        "数据来源须标注机构与年份",
        "异质性分析须报告不同时期差异",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R (RStudio)", "Python (pandas, statsmodels)", "EViews", "MATLAB", "SAS", "Excel", "SPSS", "Origin", "EndNote", "Zotero", "Mendeley", "RefWorks", "World Bank Data", "IMF Data", "Maddison Database", "Penn World Table", "IMF IFS", "UN Comtrade", "Economic Complexity Database"),
    category="经济学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "PubMed", "Cochrane Library", "Embase"),
)
