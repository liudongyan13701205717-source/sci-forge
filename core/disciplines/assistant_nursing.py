"""Assistant nursing 学科论文支持：护理助理、助理护士的临床实践、患者照护、生命体征监测与护理信息化。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="assistant_nursing",
    aliases=(
        "assistant_nursing",
        "assistant nursing",
        "护理助理",
        "助理护士",
        "enrolled nursing",
        "health care assistant",
        "护理实务",
        "patient care assistant",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methods（设计、样本、工具、伦理、数据收集）",
            "results（描述性与推断统计）",
            "discussion",
            "conclusions",
            "references",
        ),
        "clinical_report": (
            "abstract",
            "background",
            "case / intervention description",
            "clinical outcomes",
            "discussion",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "search strategy",
            "selection criteria",
            "findings",
            "implications for practice",
            "references",
        ),
    },
    citation_style="APA 7th（护理学期刊通用）；临床报告遵循 CARE 声明",
    reporting_standards={
        "case_report": "个案报告遵循 CARE 2.1 声明；须报告知情同意",
        "cohort": "队列研究遵循 STROBE；报告样本量、随访率、缺失数据",
        "randomized": "随机对照试验遵循 CONSORT；报告随机化与盲法",
        "outcome_measures": "临床结局工具（疼痛、压疮、谵妄等量表）报告版本、信效度与截断值",
        "safety": "不良事件、护理差错、跌倒/压疮率须按机构口径报告",
        "documentation": "护理文书、观察表与电子病历字段须按规范填写；伦理审批编号给出",
    },
    conventions=(
        "生命体征首次出现给出符号与单位：BP mmHg、HR bpm、RR breaths/min、SpO₂ %、T ℃、BPAP mmHg",
        "疼痛评分用 NRS / VAS（0–10）；压疮用 Braden 量表；跌倒风险用 Morse 量表；均报告截断值",
        "给药记录按 5 Rights（right patient, drug, dose, route, time）或 7 Rights 完整填写",
        "护理流程按 SBAR / SBAR-R 交接（Situation, Background, Assessment, Recommendation）",
        "表格：分组/时间/指标/均值±SD 或中位数(IQR)；P 值与效应量完整；置信区间 95%",
        "伦理审批号、IRB 编号、Trial registration 号（ClinicalTrials.gov / ChiCTR）须报告",
    ),
    key_venues=(
        "Journal of Advanced Nursing",
        "Nurse Education Today",
        "International Journal of Nursing Studies",
        "Journal of Clinical Nursing",
        "Nursing Outlook",
        "Journal of Nursing Regulation",
        "BMJ Open",
    ),
    units_and_formulas_notes=(
        "血压 mmHg；心率 bpm；呼吸频率 breaths/min；体温 ℃ 或 ℉；SpO₂ %",
        "给药剂量 mg/kg 或 mL/kg；静脉输注 mL/h 或 μg/kg/min",
        "疼痛评分 0–10；压疮分期 I–IV 或 1–4；伤口面积 cm²",
        "P 值格式统一；效应量报告 Cohen's d 或 η²p；95% CI 附于均值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Epic (EHR)", "Oracle Health / Cerner", "MEDITECH Expanse", "Allscripts Epicemr", "OpenEHR", "HL7 FHIR Toolkit", "IBM SPSS Statistics", "RStudio / R (survival, lme4)", "Stata", "JASP", "Jamovi", "PSPP", "REDCap", "OpenClinica", "NVivo", "MAXQDA", "CARE Checklist", "CONSORT Checklist", "PRISMA", "Cochrane Risk of Bias 2 (RoB 2)", "CARESIM", "Laerdal SimMan 3G", "Laerdal SimSkills", "Philips IntelliVue", "GE Healthcare Carescape", "B. Braun Infusomat", "Accu-Chek", "Zotero", "EndNote"),
    category="医学",
    databases=("OpenAlex", "PubMed", "CINAHL", "Cochrane Library", "NICE Clinical Evidence", "CNKI"),
)
