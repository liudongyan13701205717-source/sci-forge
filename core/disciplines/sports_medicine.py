"""运动医学学科论文支持：运动医学/运动科学体裁、BJSM 引用样式与运动医学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sports_medicine",
    aliases=("sports_medicine", "运动医学", "运动损伤", "运动康复",
             "sports medicine", "运动医学与科学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与运动医学问题）",
            "methods（研究设计与人群）",
            "results（损伤与功能数据）",
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
    citation_style="BJSM 样式（作者-年份；Br J Sports Med 遵循 BMJ 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "injury_surveillance": "损伤监测研究遵循 IOC 共识声明",
    },
    conventions=(
        "损伤定义与分类（ICD/Orchard 等）须注明",
        "损伤率单位（每 1000 运动员-小时等）须规范",
        "功能评分（Lysholm、IKDC 等）首次出现给出全称",
        "运动负荷（RPE、训练量）测量方法须报告",
        "重返运动标准须明确",
    ),
    key_venues=(
        "British Journal of Sports Medicine",
        "The American Journal of Sports Medicine",
        "Medicine & Science in Sports & Exercise",
        "Sports Medicine",
        "Journal of Science and Medicine in Sport",
        "Scandinavian Journal of Medicine & Science in Sports",
    ),
    units_and_formulas_notes=(
        "损伤率用每 1000 运动员-小时；负荷用 AU",
        "公式用 amsmath；损伤率与负荷计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "疗效分析给出 RR/OR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("运动心电图仪", "肌骨超声", "体成分分析仪", "SPSS", "R"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Europe PMC", "CNKI"),
)