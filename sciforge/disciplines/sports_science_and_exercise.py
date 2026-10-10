"""运动科学与运动学科论文支持：运动生理学/锻炼医学/运动处方体裁、APA 引用样式与运动生理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sports_science_and_exercise",
    aliases=("sports_science_and_exercise", "运动科学与运动", "运动生理学",
             "锻炼医学", "exercise science", "exercise physiology"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7th（运动生理学与锻炼医学主流）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "exercise_prescription": "运动处方遵循 ACSM 运动测试与处方指南",
    },
    conventions=(
        "受试者特征（年龄、性别、BMI、训练状态）须报告",
        "运动处方要素须完整（FITT-VP：频率、强度、时长、类型、总量、进度）",
        "心肺运动试验报告最大代谢当量、%VO2max、乳酸阈",
        "主观疲劳度用 RPE（6-20 或 CR-10）",
        "统计分析与样本量估算方法须声明",
    ),
    key_venues=(
        "Medicine & Science in Sports & Exercise",
        "Journal of Applied Physiology",
        "British Journal of Sports Medicine",
        "Sports Medicine",
        "European Journal of Applied Physiology",
    ),
    units_and_formulas_notes=(
        "运动强度以 %VO2max、%HRR、MET 或 RPE 报告",
        "VO2max 用 ml/kg/min 或 ml/kg/min（绝对/相对）",
        "FITT-VP 处方要素逐项列出并可量化",
        "公式用 amsmath；相对强度与能量消耗换算须明确",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("K5 代谢车", "CPET 心肺运动试验系统", "运动心电超声心动图", "心脏磁共振 (CMR)", "Holter 24 小时心电", "Omron 血压监测仪", "Dinamap 无创血压", "运动心电图仪", "血乳酸分析仪 Lactate Pro", "NDIR 呼气气体分析", "Radiometer 血气分析仪", "体成分分析仪 InBody", "DXA 双能 X 射线吸收法", "体脂钳", "关节活动度量尺", "GaitRite 步态分析", "Catapult 惯性传感器", "Polar 心率监测", "R", "SPSS"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI"),
)
