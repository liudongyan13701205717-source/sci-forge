"""医卫学科论文支持：医学卫生/临床卫生学体裁、Vancouver 引用样式与医卫度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hygiene_medical",
    aliases=("hygiene_medical", "医卫", "医学卫生", "医疗卫生", "临床护理", "医学", "卫生事业", "医学检验", "医院管理", "公共卫生"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与研究问题）", "methodology（人群、分组与流程）", "results（临床/卫生学结果）", "discussion（临床与公共卫生意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例与场景）", "analysis（诊断与处理）", "results（转归）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（临床/卫生学框架）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver 样式（国际医学期刊常用）",
    reporting_standards={
        "cohort": "队列研究遵循 STROBE 声明",
        "trial": "随机对照试验遵循 CONSORT 规范",
        "case_control": "病例对照研究遵循 STROBE 规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethics": "人体研究须报告伦理批准与知情同意",
    },
    conventions=(
        "分组、入排标准与失访须报告",
        "统计检验与效应量须给出",
        "风险指标（HR、OR、RR）须定义",
        "ICD-10 编码须使用",
        "单位（mmHg、mg/dL）须规范",
    ),
    key_venues=(
        "The Lancet",
        "BMJ",
        "JAMA",
        "NEJM",
        "The BMJ Open",
        "British Journal of Health Psychology",
    ),
    units_and_formulas_notes=(
        "血压用 mmHg；血糖用 mmol/L 或 mg/dL",
        "剂量用 mg/kg 或 μg",
        "公式用 amsmath；风险模型须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "风险指标（HR、OR、RR、95% CI）须定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R", "Python", "Stata", "SAS", "SPSS", "MATLAB", "Excel", "LaTeX", "EndNote", "Zotero", "MedCalc", "JMP", "WinBUGS", "OpenBUGS", "RStudio", "Git", "REDCap", "QGIS", "NVivo", "Minitab"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
