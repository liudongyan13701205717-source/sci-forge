"""Commerce, Management, Tourism and Services 学科论文支持：商业管理/旅游/服务领域体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="commerce_management_tourism_and_services",
    aliases=("Commerce, Management, Tourism and Services", "商管旅游与服务", "商业管理",
             "旅游管理", "服务管理", "business management", "tourism management",
             "hospitality management", "service management", "商业管理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "literature review（文献综述）",
            "theoretical framework（理论框架）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusion（结论与建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "company/context overview（背景）",
            "case analysis（案例分析）",
            "findings（发现）",
            "implications（启示）",
            "references",
        ),
    },
    citation_style="APA 7（商业管理主流引用样式）",
    reporting_standards={
        "quantitative": "遵循 APA 量化研究报告规范（APA Publication Manual）",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
    },
    conventions=(
        "研究方法须明确数据类型（定量/定性/混合）与分析方法",
        "样本量、抽样方法与信效度须报告",
        "引用格式遵循目标期刊要求（APA 7 为主）",
        "商业术语与行业专有名词首次出现时给出中英文对照",
    ),
    key_venues=(
        "Journal of Business Research",
        "Tourism Management",
        "Annals of Tourism Research",
        "International Journal of Hospitality Management",
        "Journal of Service Research",
        "European Management Journal",
        "Tourism Management Perspectives",
        "Current Issues in Tourism",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量用 Cohen's d 或 η²",
        "显著性水平标注为 *p < .05, **p < .01, ***p < .001",
        "样本量须报告，百分比给出基数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "NVivo", "Qualtrics", "Tableau", "Minitab", "R", "Python", "AMOS", "EQS", "LISREL", "MAXQDA", "Google Analytics", "Salesforce", "Microsoft Project", "Power BI", "ArcGIS", "Excel", "WEKA", "SimPy"),
    category="管理学",
    databases=("OpenAlex", "Scopus", "WoS", "CNKI", "万方"),
)
