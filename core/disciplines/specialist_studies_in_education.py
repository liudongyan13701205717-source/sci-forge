"""教育专门研究学科论文支持：教育政策/教育领导力/教育经济/教育测量体裁、APA 7 与政策分析注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="specialist_studies_in_education",
    aliases=("specialist_studies_in_education", "教育专门研究", "Specialist Studies in Education", "教育政策", "教育领导力", "教育经济", "比较教育", "education policy", "education leadership", "education economics"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "policy_analysis": "明确政策文本、时点、发文主体与适用层级（CARE 精神 + 政策研究框架）",
        "econometric_study": "报告识别策略、样本与权重、稳健性检验（DiD/RDD/IV）",
        "qualitative": "COREQ/SRQR，须说明资料饱和与三角互证",
    },
    conventions=(
        "政策引用标文件名、文号、发文单位与发布日期",
        "教育统计口径注明年份、层级（幼儿园/义务教育/高中阶段）",
        "跨国比较研究须标注数据源（UIS/EDstats/PISA）与年份",
        "教育财政数据以生均公用经费/财政性教育经费口径分列",
        "伦理批准与受访者匿名化须说明",
    ),
    key_venues=(
        "Educational Research Review",
        "Journal of Educational Evaluation, Policy & Administration",
        "Comparative Education Review",
        "Education Economics",
        "Higher Education Quarterly",
    ),
    units_and_formulas_notes=(
        "生均经费标元/人·年并注明价格基期",
        "教育回报率标年数与对数工资弹性 β（Mincer 方程）",
        "教育统计报 95% CI 与稳健标准误",
        "跨国数据标当年值/不变值并注明汇率基准年",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R", "Stata", "SPSS", "SAS", "NVivo", "ATLAS.ti", "MaxQDA", "PolicyMap", "Tableau", "Power BI", "GIS (ArcGIS)", "QGIS", "LaTeX", "EndNote", "Zotero", "Mendeley", "SurveyMonkey", "Microsoft Excel", "JASP", "SAS Enterprise Guide"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
