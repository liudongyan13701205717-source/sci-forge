"""营养治疗学科论文支持：临床营养干预、营养评估与膳食管理体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dietician_programmes",
    aliases=(
        "dietician_programmes", "营养治疗", "营养师培训",
        "nutrition therapy", "营养疗法",
        "clinical nutrition", "临床营养",
        "dietetics", "营养学",
        "dietary counselling", "膳食指导",
        "nutrition intervention", "营养干预",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（营养问题与临床背景）",
            "methods（研究设计、营养干预方案、评估指标）",
            "results（营养改善与临床效果）",
            "discussion（营养方案优化建议）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、营养干预方案、结局指标）",
            "results（疗效与安全性）",
            "discussion",
            "references",
        ),
        "case_study": (
            "abstract",
            "case presentation（患者营养状况与干预过程）",
            "intervention（营养干预方案）",
            "outcome（效果评估）",
            "discussion",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "RCT": "CONSORT 声明",
        "observational": "STROBE 声明",
        "systematic_review": "PRISMA 声明",
        "case_report": "CARE 指南",
        "nutrition": "膳食干预须描述能量、宏量营养素与微量营养素供给",
    },
    conventions=(
        "营养评估须注明评估工具（如 NRS-2002、PG-SGA）",
        "膳食记录须注明记录方式（24h回顾/膳食日记）",
        "营养干预须注明能量与蛋白质供给量",
        "生物标志物须注明检测方法与时机",
        "统计检验注明方法、效应量与置信区间",
    ),
    key_venues=(
        "Clinical Nutrition",
        "Journal of Clinical Gastroenterology",
        "American Journal of Clinical Nutrition",
        "Nutrition",
        "British Journal of Nutrition",
        "Journal of Parenteral and Enteral Nutrition",
    ),
    units_and_formulas_notes=(
        "能量用 kcal 或 kJ 表示",
        "蛋白质用 g/kg/d 表示",
        "微量元素用 mg/d 或 μg/d 表示",
        "BMI 用 kg/m² 表示",
        "生物标志物注明检测方法与参考范围",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "Excel", "Nutrition Care Software", "MediCarry", "Dietary Record Software", "Bioelectrical Impedance Analyser", "DEXA Scanner", "Skinfold Caliper", "Tape Measure", "Blood Pressure Monitor", "Glucose Meter", "Micronutrient Analyzer", "Clinical Nutrition Software", "Electronic Health Record", "Nutrition Database", "Food Composition Tables", "Body Composition Analyzer", "Nutrition Education Software", "Online Nutrition Assessment"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
