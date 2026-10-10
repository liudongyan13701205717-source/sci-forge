"""医学诊断与治疗学科论文支持：临床病例报告与诊疗技术体裁、ICMJE 规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_diagnostic_and_treatment",
    aliases=("medical_diagnostic_and_treatment", "医学诊断与治疗", "clinical medicine", "clinical diagnosis", "临床诊断", "clinical practice", "disease treatment", "医学治疗", "诊疗技术"),
    paper_types={
        "research": ("abstract", "introduction（疾病背景与临床问题）", "methods（患者队列与诊断方法）", "results（诊断效能与治疗结果）", "discussion（临床意义与局限性）", "references"),
        "case_study": ("abstract", "introduction", "case description（病史与体征）", "analysis（辅助检查与鉴别诊断）", "results（治疗经过与转归）", "discussion（经验总结与文献回顾）", "references"),
        "review": ("abstract", "introduction", "clinical overview（临床综述）", "evidence synthesis（循证证据整合）", "future directions", "references"),
    },
    citation_style="Vancouver（ICMJE 推荐）",
    reporting_standards={
        "case_report": "病例报告遵循 CARE 2.1 声明",
        "diagnostic_study": "诊断试验研究遵循 STARD 2015 声明",
        "treatment_trial": "随机对照试验遵循 CONSORT 2010 声明",
        "prognostic_study": "预后研究遵循 TRIPOD 2015 声明",
        "systematic_review": "系统综述遵循 PRISMA 2020 声明",
    },
    conventions=(
        "病例报告须获得患者知情同意；伦理审批编号须注明",
        "诊断试验须报告灵敏度、特异度、阳性/阴性似然比",
        "治疗方案须遵循临床指南版本（注明年份）",
        "实验室检查须注明参考范围与检验方法",
        "影像描述须遵循 Radiological Society of North America (RSNA) 标准术语",
    ),
    key_venues=(
        "The Lancet",
        "New England Journal of Medicine",
        "JAMA",
        "BMJ",
        "Annals of Internal Medicine",
        "The Journal of Clinical Investigation",
        "Clinical Medicine",
    ),
    units_and_formulas_notes=(
        "体温用 °C；血压用 mmHg；心率用 bpm",
        "实验室指标须注明单位与参考范围",
        "药物剂量用 mg/kg 或 μg/kg；给药途径须注明",
        "影像学测量须注明方法（CT 值、SUV、B 值）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Stethoscope", "Otoscope", "Ophthalmoscope", "Tensimeter", "Pulse Oximeter", "ECG Machine", "Ultrasound Scanner", "CT Scanner", "MRI Scanner", "Digital X-ray Machine", "Endoscope", "Biopsy Needle", "Blood Collection Kit", "Blood Analyzer", "Chemistry Analyzer", "Coagulation Analyzer", "Microscope", "Laboratory Centrifuge", "Electrolyte Analyzer", "Blood Glucose Meter"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
