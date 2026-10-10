"""配药学科论文支持：药学配药、处方审核与临床药学研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dispensing_pharmacy",
    aliases=(
        "dispensing_pharmacy", "配药", "药学配药",
        "pharmacy dispensing", "药物配药",
        "clinical pharmacy", "临床药学",
        "pharmaceutical care", "药学监护",
        "prescription review", "处方审核",
        "medication management", "用药管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（配药问题与临床背景）",
            "methods（研究设计、配药方案、评估指标）",
            "results（配药效果与安全性）",
            "discussion（配药优化建议）",
            "references",
        ),
        "clinical_study": (
            "abstract",
            "introduction",
            "methods（配药流程与干预方案）",
            "results（配药效果与安全性）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（配药理论综述）",
            "evidence summary（证据总结）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "RCT": "CONSORT 声明",
        "observational": "STROBE 声明",
        "systematic_review": "PRISMA 声明",
        "pharmacy": "配药流程须完整描述（审核、调配、核对、发放）",
    },
    conventions=(
        "药物名称须使用通用名（INN）与商品名",
        "剂量须注明规格、途径与频次",
        "配药错误须分类记录（ISMP 分类）",
        "不良反应须按 CIOMS 分类报告",
        "统计检验注明方法、效应量与置信区间",
    ),
    key_venues=(
        "American Journal of Health-System Pharmacy",
        "International Journal of Clinical Pharmacy",
        "Journal of Clinical Pharmacy and Therapeutics",
        "Pharmacy Practice",
        "Annals of Pharmacotherapy",
    ),
    units_and_formulas_notes=(
        "剂量用 mg/kg 或等效剂量表示",
        "药代动力学参数（t½、Cmax、AUC）须注明方法",
        "不良反应发生率用 % 表示",
        "统计检验注明 t/F/χ² 值、p 值与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "Excel", "Pharmacy Management Software", "Micromedex", "Lexicomp", "Epocrates", "DrugDex", "Clinical Pharmacokinetics Software", "Clinical Decision Support", "Drug Interaction Checker", "Dosing Calculator", "Body Surface Area Calculator", "Creatinine Clearance Calculator", "Drug Information Database", "Pharmacy Automation Software", "Electronic Health Record", "Pharmacy Labeling Software", "Pharmacy Benefits Manager", "Clinical Pharmacist Software"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
