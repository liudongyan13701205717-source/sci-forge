"""泌尿外科学学科论文支持：泌尿临床/肿瘤体裁、AUA/The Journal of Urology 引用样式与泌尿外科记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="urology",
    aliases=("urology", "泌尿外科学", "泌尿外科", "泌尿科", "男科学",
             "andrology", "泌尿肿瘤"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与泌尿问题）",
            "methods（研究设计与人群）",
            "results（功能与肿瘤结局数据）",
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
    citation_style="AUA/The Journal of Urology 样式（作者-年份；J Urol 遵循 AUA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=(
        "肿瘤分期（TNM）与分级（ISUP）须注明版本",
        "PSA 单位 ng/mL；肾功能（eGFR）单位须规范",
        "尿动力学参数（Qmax、Pdet）缩写首次出现给出全称",
        "手术方式（机器人/腹腔镜/开放）须报告",
        "功能结局（尿控、勃起功能）评估工具须注明",
    ),
    key_venues=(
        "The Journal of Urology",
        "European Urology",
        "Urology",
        "BJU International",
        "Nature Reviews Urology",
        "Journal of Endourology",
    ),
    units_and_formulas_notes=(
        "PSA 用 ng/mL；eGFR 用 mL/min/1.73m²",
        "公式用 amsmath；eGFR 计算式（CKD-EPI 等）须注明",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "生存分析给出 HR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("膀胱镜", "尿动力学仪", "SPSS", "前列腺穿刺活检设备"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Europe PMC", "CNKI"),
)