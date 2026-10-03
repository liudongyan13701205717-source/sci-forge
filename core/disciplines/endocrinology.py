"""内分泌学学科论文支持：内分泌临床/代谢体裁、Endocrine Society/JCEM 引用样式与内分泌学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="endocrinology",
    aliases=("endocrinology", "内分泌学", "内分泌科", "代谢病学",
             "metabolism", "内分泌与代谢"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与内分泌问题）",
            "methods（研究设计与人群）",
            "results（激素与代谢数据）",
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
    citation_style="Endocrine Society/JCEM 样式（作者-年份；JCEM 遵循 Endocrine Society 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=(
        "激素单位（pmol/L、ng/dL 等）须规范并注明换算",
        "血糖用 mmol/L 或 mg/dL（须注明换算）",
        "HbA1c 单位 % 或 mmol/mol（须注明）",
        "诊断标准（ADA、WHO 等）须注明版本",
        "检测方法（免疫测定/质谱）须报告",
    ),
    key_venues=(
        "Journal of Clinical Endocrinology & Metabolism",
        "Diabetes",
        "Diabetes Care",
        "Endocrinology",
        "The Lancet Diabetes & Endocrinology",
        "Nature Reviews Endocrinology",
    ),
    units_and_formulas_notes=(
        "血糖用 mmol/L；HbA1c 用 % 或 mmol/mol",
        "公式用 amsmath；HOMA-IR 等指数计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "疗效分析给出 RR/OR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("血糖仪", "化学发光免疫分析仪", "连续血糖监测系统", "SPSS"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Europe PMC", "CNKI"),
)