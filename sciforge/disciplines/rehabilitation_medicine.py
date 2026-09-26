"""康复医学学科论文支持：康复临床/功能体裁、ACRM/APMR 引用样式与康复医学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="rehabilitation_medicine",
    aliases=("rehabilitation_medicine", "康复医学", "康复科", "物理医学与康复",
             "physical medicine and rehabilitation", "康复治疗"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与康复问题）",
            "methods（研究设计与人群）",
            "results（功能结局数据）",
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
    citation_style="ACRM/APMR 样式（作者-年份；Arch Phys Med Rehabil 遵循 ACRM 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "rehabilitation_trial": "康复试验遵循 CONSORT 康复扩展",
    },
    conventions=(
        "功能量表（FIM、BI、FMA 等）首次出现给出全称与范围",
        "干预方案（频率/强度/时长）须完整报告",
        "结局测量时间点须明确",
        "盲法（评估者盲等）须报告",
        "ICF 框架术语（活动/参与）使用须规范",
    ),
    key_venues=(
        "Archives of Physical Medicine and Rehabilitation",
        "Journal of Rehabilitation Medicine",
        "Neurorehabilitation and Neural Repair",
        "Physical Therapy",
        "Disability and Rehabilitation",
        "Annals of Physical and Rehabilitation Medicine",
    ),
    units_and_formulas_notes=(
        "量表分数无量纲；时间用周/月",
        "公式用 amsmath；量表评分与最小临床重要差异须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "疗效分析给出效应量与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("康复评定量表系统", "三维运动分析系统", "肌力与肌张力测定仪", "SPSS"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Europe PMC", "CNKI"),
)