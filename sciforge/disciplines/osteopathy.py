"""整骨疗法学科论文支持：手法治疗原则、随机对照试验与循证评价。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="osteopathy",
    aliases=(
        "osteopathy",
        "整骨疗法",
        "Osteopathic Medicine",
        "Osteopathy",
        "手动医学",
        "整脊",
        "Osteopathic Manipulative Treatment",
        "OMT",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与假设）",
            "methodology（样本与治疗流程）",
            "results（疗效与结果）",
            "discussion（机理与证据等级）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例与治疗描述）",
            "analysis（评估与调整）",
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
    citation_style="Vancouver（循证与手动医学期刊）/ GB/T 7714（中文）",
    reporting_standards={
        "clinical_trial": "CONSORT 声明",
        "systematic_review": "PRISMA 声明",
        "osteopathic_trial": "OSTEOMAT 报告规范",
        "risk_of_bias": "Cochrane RoB 2.0",
    },
    conventions=(
        "治疗手法须具体描述（部位、方向、幅度）",
        "盲法须说明对受试者/治疗师/评估者的处理",
        "疼痛/功能评分须给出量表与评分标准",
        "随访时间点须列出并报告脱落率",
        "试验须在 ClinicalTrials.gov 注册",
    ),
    key_venues=(
        "Journal of Osteopathic Medicine",
        "Journal of Bodywork and Movement Therapies",
        "Manual Therapy",
        "Journal of Manipulative and Physiological Therapeutics",
        "British Journal of Osteopathy",
    ),
    units_and_formulas_notes=(
        "疼痛评分 NRS 0–10 或 VAS 0–100 mm",
        "活动度用角度制 °",
        "统计方法给出 t/Mann-Whitney/重复测量方差分析",
        "疗效报告 MDC/SMC 与临床重要差值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("RevMan（Meta 分析）", "Stata（统计分析）", "SPSS 26", "R（统计分析）", "SPSSAU（云统计）", "Excel（数据整理）", "EndNote", "LaTeX", "Origin", "Photoshop", "Inclinometer Digital（活动度）", "Goniometer Digital", "Pressure Gauge 手法力测量", "Kinesiography 运动捕捉", "EMG 肌电仪（Delays Trigno）", "Pain Assessment Scales App", "Qualitative Research NVivo", "ClinicalTrials.gov Registry Tool", "PROformax（患者报告结局）", "TENS 经皮电神经刺激仪"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "Cochrane Handbook for Systematic Reviews"),
)
