"""流行病学科论文支持：流行病学、疾病监测与公共卫生研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="epidemiology",
    aliases=(
        "epidemiology", "流行病学", "疾病监测",
        "epidemiology", "流行病学",
        "disease surveillance", "疾病监测",
        "public health", "公共卫生",
        "infectious disease epidemiology", "传染病流行病学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（流行病问题与背景）",
            "method（研究设计、数据收集、分析方法）",
            "results（发病率与风险因素）",
            "discussion（公共卫生建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "epidemiological analysis（流行病学分析）",
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
    citation_style="Vancouver",
    reporting_standards={
        "study_design": "研究设计须明确（队列、病例对照、横断面等）",
        "data": "数据来源须注明",
        "statistics": "统计检验须注明方法与显著性水平",
    },
    conventions=(
        "发病率用 1/10万 表示",
        "相对危险度用 RR 表示",
        "比值比用 OR 表示",
        "95% CI 须报告",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "American Journal of Epidemiology",
        "Epidemiology",
        "Journal of Clinical Epidemiology",
        "International Journal of Epidemiology",
        "Epidemiologic Reviews",
        "Lancet Infectious Diseases",
    ),
    units_and_formulas_notes=(
        "发病率用 1/10万 表示",
        "相对危险度用 RR 表示",
        "比值比用 OR 表示",
        "95% CI 须报告",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R (RStudio)", "SAS", "Stata", "SPSS", "Excel", "Epi Info", "ArcGIS", "QGIS", "SaTScan", "GeoDa", "WinBUGS", "OpenBUGS", "JAGS", "Stan", "Python (pandas, numpy)", "MATLAB", "Tableau", "Power BI", "GenStat", "OpenEPi"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
