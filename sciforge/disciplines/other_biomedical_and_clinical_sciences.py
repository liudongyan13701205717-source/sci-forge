"""其他生物医学与临床科学学科论文支持：跨方向临床与转化研究规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_biomedical_and_clinical_sciences",
    aliases=(
        "other_biomedical_and_clinical_sciences",
        "其他生物医学与临床科学",
        "Other Biomedical and Clinical Sciences",
        "临床医学交叉",
        "转化医学",
        "Translational Medicine",
        "Public Health 交叉",
        "Clinical Research",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究假设）",
            "methodology（样本与临床方案）",
            "results（临床与机制结果）",
            "discussion（机理与转化意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例与治疗描述）",
            "analysis（分析）",
            "results（随访结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver（临床期刊）/ GB/T 7714（中文）",
    reporting_standards={
        "clinical_trial": "CONSORT 声明",
        "cohort": "STROBE 声明",
        "case_report": "CARE 声明",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "样本纳入排除标准须列出",
        "随访时间与失访率须报告",
        "并发症按 Clavien-Dindo 或 CTCAE 分级",
        "统计学给出检验方法、α=0.05 与多因素模型",
        "临床试验须在 ClinicalTrials.gov 注册并报告伦理编号",
    ),
    key_venues=(
        "The Lancet",
        "Journal of Clinical Investigation",
        "BMJ Open",
        "Journal of Translational Medicine",
        "中华医学杂志",
    ),
    units_and_formulas_notes=(
        "生命体征单位使用标准 SI（mmHg, ℃, bpm）",
        "实验室指标用国际单位（SI units）",
        "疼痛 NRS 0–10，功能量表注明出处",
        "生存分析给出 HR、95% CI 与中位生存期",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("SPSS 26（统计）", "R / RStudio", "Stata", "SAS（临床统计）", "Python（SciPy/Pandas）", "Excel", "Origin", "EndNote", "LaTeX", "Photoshop", "PACS 影像", "LIS（临床实验室信息系统）", "EMR 电子病历", "MetaVision 生命体征监测", "RevMan（Meta 分析）", "ClinicalTrials.gov Registry", "PROformax（患者结局）", "ELISA 试剂平台", "Cryostat 冷冻切片", "流式细胞仪 BD FACSCanto"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "Cochrane Library"),
)
