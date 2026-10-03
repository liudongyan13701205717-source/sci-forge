"""心脏病学学科论文支持：心血管临床/介入体裁、ACC/JACC 引用样式与心血管记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cardiology",
    aliases=("cardiology", "心脏病学", "心血管病学", "心血管内科", "心血管医学",
             "cardiovascular medicine", "心血管病"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与心血管问题）",
            "methods（研究设计与人群）",
            "results（主要终点与数据）",
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
    citation_style="ACC/JACC 样式（作者-年份；JACC 遵循 ACC 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=(
        "血压单位 mmHg；心率单位 bpm",
        "EF（射血分数）须注明测量方法（Simpson 双平面等）",
        "NYHA 心功能分级首次出现给出定义",
        "药物剂量与给药途径须完整报告",
        "心电图/超声参数缩写首次出现给出全称",
    ),
    key_venues=(
        "Journal of the American College of Cardiology",
        "Circulation",
        "European Heart Journal",
        "Circulation Research",
        "JAMA Cardiology",
        "Nature Reviews Cardiology",
    ),
    units_and_formulas_notes=(
        "血压用 mmHg；血脂用 mmol/L 或 mg/dL（须注明换算）",
        "公式用 amsmath；QTc 校正公式（Bazett 等）须注明",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "生存分析给出 HR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("心电监护仪", "超声心动图仪", "冠脉造影系统", "心脏 MRI 扫描仪", "SPSS", "R"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "Semantic Scholar"),
)