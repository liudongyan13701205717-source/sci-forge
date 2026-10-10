"""健康科学学科论文支持：临床与公共卫生体裁、Vancouver 引用样式与医学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="health_sciences",
    aliases=("health_sciences", "健康科学", "医学", "公共卫生", "生命科学", "临床科学", "流行病学", "预防医学", "生物医学"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver（作者-序号）",
    reporting_standards={
        "randomized_trial": "CONSORT 声明",
        "observational": "STROBE 声明",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "首字母缩写首次出现给出全称",
        "统计学报告 t/χ²/F/P 值",
        "数值结果给出均值±SD 与样本量",
        "临床试验遵循 CONSORT 图表规范",
        "伦理委员会批准号须报告",
    ),
    key_venues=(
        "The Lancet",
        "NEJM",
        "BMJ",
        "JAMA",
        "PLOS Medicine",
    ),
    units_and_formulas_notes=(
        "时间/温度/剂量用 SI 单位",
        "公式用 amsmath；临床公式须编号",
        "行内公式避免复杂分式",
        "数值结果给出均值±SD/SEM 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "STATA", "SAS", "Meta-Analyst", "RevMan", "ClinicalTrials.gov", "REDCap", "Qualtrics", "NVivo", "Atlas.ti", "VOSviewer", "PRISMA", "EndNote", "GraphPad Prism", "Microsoft Excel", "Python (SciPy)", "ImageJ", "UpToDate", "JBI Review Manager"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "PubMed", "MEDLINE", "Embase", "PubMed Central", "Web of Science", "Cochrane"),
)
