"""社区卫生学科论文支持：社区流行病学/公共卫生干预体裁、Vancouver 引用样式与社区健康度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hygiene_community",
    aliases=("hygiene_community", "社区卫生", "公共卫生", "社区健康", "社区卫生服务", "健康促进", "疾病预防", "妇幼保健", "社区流行病学"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与研究问题）", "methodology（人群、抽样与暴露评估）", "results（流行病学结果）", "discussion（公共卫生意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（社区与人群）", "analysis（健康分析）", "results（干预效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（公卫视角框架）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver 样式（公共卫生/医学期刊常用）",
    reporting_standards={
        "observational": "流行病学观察研究遵循人群/暴露/结局报告规范",
        "intervention": "公共卫生干预遵循 ITT 与 CONSORT 规范",
        "survey": "社区调查遵循抽样与问卷质量报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethics": "人体研究须报告伦理批准与知情同意",
    },
    conventions=(
        "抽样框与应答率须报告",
        "健康结局与暴露时点须明确",
        "风险指标与 95% CI 须给出",
        "混杂调整方法须说明",
        "单位（‰、每万、mg/L）须规范",
    ),
    key_venues=(
        "American Journal of Public Health",
        "Preventive Medicine",
        "BMC Public Health",
        "Journal of Public Health",
        "China Journal of Public Health",
        "Environmental Research",
    ),
    units_and_formulas_notes=(
        "发病率用 ‰ 或 每万人；患病率用 %",
        "暴露用 mg/L 或 μg/m³",
        "公式用 amsmath；风险模型须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "风险指标（OR、RR、95% CI）须定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R", "Python", "Stata", "SAS", "SPSS", "MATLAB", "Excel", "LaTeX", "EndNote", "Zotero", "NVivo", "QGIS", "ArcGIS", "OpenClinica", "REDCap", "JMP", "WinBUGS", "Git", "RStudio", "MedCalc"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
