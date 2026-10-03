"""精神病学学科论文支持：精神临床/流行病体裁、APA 引用样式与精神医学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="psychiatry",
    aliases=("psychiatry", "精神病学", "精神医学", "临床心理学",
             "clinical psychiatry", "精神科"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与精神问题）",
            "methods（研究设计与人群）",
            "results（量表与统计结果）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法与统计）",
            "results（疗效与安全性终点）",
            "discussion（与既往试验对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Am J Psychiatry 遵循 APA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "qualitative": "质性研究遵循 COREQ/SRQR 指南",
    },
    conventions=(
        "诊断标准（DSM-5/ICD-11）须注明版本",
        "量表（HAMD、HAMA、PANSS 等）首次出现给出全称与评分范围",
        "效应量（Cohen's d 等）须报告",
        "伦理审批与知情同意须声明",
        "药物剂量与滴定方案须完整报告",
    ),
    key_venues=(
        "American Journal of Psychiatry",
        "JAMA Psychiatry",
        "The Lancet Psychiatry",
        "Psychological Medicine",
        "World Psychiatry",
        "British Journal of Psychiatry",
    ),
    units_and_formulas_notes=(
        "量表分数无量纲；时间用周/月",
        "公式用 amsmath；量表总分与因子分计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "效应量与 95% CI 须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("精神科评定量表系统", "SPSS", "R", "心理量表录入与计分软件", "结构化临床访谈（SCID）"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "Semantic Scholar"),
)