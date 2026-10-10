"""康复医学学科论文支持：康复临床/功能体裁、ACRM/APMR 引用样式与功能评估记注。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="rehabilitation_medicine",
    aliases=(
        "rehabilitation_medicine",
        "康复医学",
        "康复科",
        "物理医学与康复",
        "Physical Medicine and Rehabilitation",
        "PM&R",
        "康复治疗学",
        "康复工程"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与康复问题）",
            "methods（研究设计与人群）",
            "results（功能结局数据）",
            "discussion（机理与临床意义）",
            "references"
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法与统计）",
            "results（疗效与安全性终点）",
            "discussion（与既往试验对比）",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references"
        ),
    },
    citation_style="ACRM/APMR 样式（作者-年份；Arch Phys Med Rehabil 遵循 ACRM 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南"
    },
    conventions=(
        "功能量表（FIM、BI、FMA 等）首次出现给出全称与范围",
        "干预方案（频率/强度/时长）须完整报告",
        "结局测量时间点须明确",
        "盲法（评估者盲等）须报告",
        "ICF 框架术语（活动/参与）使用须规范"
    ),
    key_venues=(
        "Archives of Physical Medicine and Rehabilitation",
        "Journal of Rehabilitation Medicine",
        "Neurorehabilitation and Neural Repair",
        "Physical Therapy",
        "Disability and Rehabilitation"
    ),
    units_and_formulas_notes=(
        "量表分数无量纲；时间用周/月",
        "公式用 amsmath；量表评分与最小临床重要差异须明确",
        "显示公式仅在被引用时编号",
        "数值结果给出均值 ± SD/SEM 与样本量"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("FIM Scale", "Barthel Index", "Fugl-Meyer Scale", "SPM Scale", "Berg Balance Scale", "Tinetti Balance Scale", "Timed Up and Go Test", "6-Minute Walk Test", "Vicon Motion Analysis", "InBody Composition Analyzer", "MyoBot EMG System", "FES System", "Robotic Exoskeleton", "Gait Trainer", "Kinect Motion Capture", "MyoWare EMG Sensor", "SPSS", "STATA", "R", "Qualtrics/REDCap"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Europe PMC", "CNKI"),
)
