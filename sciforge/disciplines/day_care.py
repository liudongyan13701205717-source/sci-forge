"""Day care (adults) 学科论文支持：成人日间照料/日托研究体裁、教育评估规范与照护工具。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="day_care",
    aliases=(
        "day_care", "Day care (adults)", "成人日间照料", "日托", "日间照料中心",
        "adult day care", "nursing day centre", "day centre for adults",
        "respite care", "social care services", "elderly day care",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与照护问题）",
            "methods（研究设计、样本与评估工具）",
            "results（照护干预效果与生活质量数据）",
            "discussion（政策与实践意义）",
            "conclusion",
            "references",
        ),
        "policy_report": (
            "abstract",
            "introduction",
            "service_model（服务模式与配置）",
            "outcomes（成效评估与成本效益）",
            "recommendations（政策建议）",
            "references",
        ),
        "training_material": (
            "abstract",
            "introduction",
            "curriculum（课程与技能培训）",
            "assessment（考核标准）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "quality_of_life": "生活质量评估须使用标准化量表（SF-36/WHOQOL-BREF），报告效应量与置信区间",
        "care_intervention": "照护干预须报告实施流程、时长、频次与对照组设计",
        "ethics": "伦理审查与知情同意须声明；涉及认知障碍者须注明代理同意机制",
        "cost_effectiveness": "成本效益分析须注明货币单位、通胀调整与贴现率",
    },
    conventions=(
        "服务对象年龄分层须明确（老年/残障/儿童日托须区分），评估指标须注明工具来源",
        "生活质量评估须使用标准化量表（如SF-36、WHOQOL-BREF），评分须注明来源与时间",
        "照护干预方案须描述实施流程、时长与频次；对照实验须报告干预组/对照组设计",
        "伦理审查与知情同意须声明；涉及未成年人或认知障碍者须注明代理同意机制",
        "数据分析须报告效应量、置信区间与样本量",
    ),
    key_venues=(
        "Journal of Applied Gerontology",
        "Aging & Society",
        "Journal of the American Directors on Aging",
        "Journal of Advanced Nursing",
        "International Journal of Nursing Studies",
        "Journal of Geriatric Physical Therapy",
        "Journal of Health Care for the Poor and Underserved",
        "Ageing International",
    ),
    units_and_formulas_notes=(
        "生活质量评分使用标准化量表原始分；效应量用 Cohen's d 或 η²",
        "成本效益分析用货币单位（元/美元），注明通胀调整基准年与贴现率",
        "照护时长用分钟/小时；频率用次/天 或 次/周",
        "统计显著性用 α=0.05；95% 置信区间须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("IBM SPSS Statistics", "R (RStudio)", "Python (pandas, scikit-learn)", "Stata", "NVivo", "ATLAS.ti", "Tableau", "Power BI", "Qualtrics", "SurveyMonkey", "Moodle", "Blackboard", "Microsoft Excel", "Google Sheets", "Google Analytics", "Vitalscan", "CareZone", "SeniorConnect", "Electronic Health Records (EHR)", "GPS Tracking System"),
    category="教育学",
    databases=("PubMed", "CNKI", "万方", "OpenAlex", "Crossref"),
)
