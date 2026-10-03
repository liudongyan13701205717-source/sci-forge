"""外科学学科论文支持：外科临床/技术体裁、AMA/JAMA Surgery 引用样式与外科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="surgery",
    aliases=("surgery", "外科学", "外科", "普通外科", "手术学",
             "general surgery", "外科临床"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与外科问题）",
            "methods（研究设计与人群）",
            "results（手术结局与并发症）",
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
        "technical": (
            "abstract",
            "introduction",
            "surgical technique（手术步骤详述）",
            "results（病例系列与结局）",
            "discussion（技术要点与局限）",
            "references",
        ),
    },
    citation_style="AMA 样式（数字上标；JAMA Surgery 遵循 AMA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_series": "病例系列报告遵循 PROCESS 指南",
        "case_report": "病例报告遵循 CARE 指南",
    },
    conventions=(
        "手术名称与术式（如腹腔镜胆囊切除术）须规范书写",
        "并发症分级（Clavien-Dindo）须注明版本",
        "围手术期结局（住院时间、失血量）须报告",
        "随访时间与失访率须报告",
        "伦理审批与知情同意须声明",
    ),
    key_venues=(
        "Annals of Surgery",
        "JAMA Surgery",
        "The Lancet",
        "British Journal of Surgery",
        "Surgery",
        "Journal of the American College of Surgeons",
    ),
    units_and_formulas_notes=(
        "失血量用 mL；时间用 min/h；住院时间用天",
        "公式用 amsmath；并发症分级与评分计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "生存/复发分析给出 HR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("手术机器人（达芬奇系统）", "腹腔镜摄像系统", "手术录像分析软件", "高强度聚焦超声（HIFU）设备", "SPSS", "R"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "Semantic Scholar"),
)