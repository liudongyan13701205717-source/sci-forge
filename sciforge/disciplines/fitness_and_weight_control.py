"""健身与体重控制学科论文支持：运动处方、体成分分析与营养干预。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fitness_and_weight_control",
    aliases=("fitness_and_weight_control", "健身与体重控制", "weight management",
             "exercise prescription", "body composition", "体重管理",
             "exercise physiology", "运动生理学", "nutrition and fitness"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={
        "intervention": "运动干预须报告强度（强度储备/心率储备）、频率、时间与方式",
        "measurement": "体成分测量须注明仪器型号、测量条件与重复性",
        "ethics": "涉及人体实验须声明伦理审查批准号与知情同意",
    },
    conventions=(
        "心率用次/min 表示",
        "运动强度用心率储备%或最大摄氧量%表示",
        "体脂率用%表示",
        "能量消耗用 kcal 或 kJ 表示",
        "体重用 kg 表示",
    ),
    key_venues=(
        "Journal of Obesity",
        "Obesity Reviews",
        "Obesity",
        "International Journal of Obesity",
        "中华肥胖与代谢杂志",
    ),
    units_and_formulas_notes=(
        "BMI = 体重(kg) / 身高(m)²，单位 kg/m²",
        "静息代谢率 RMR 用 kJ/d 或 kcal/d 表示",
        "最大摄氧量 VO₂max 用 mL/(kg·min) 表示",
        "体脂率用 DEXA 或 BIA 法测量，单位 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("InBody 体成分分析仪", "代谢测试仪 (间接量热法)", "心肺运动测试系统 (CPET)", "生物力学分析系统 (Vicon)", "肌电图仪 (EMG)", "心率监测器", "运动手环 (Garmin/Fitbit)", "智能体重秤", "营养分析软件 (Nutritionist Pro)", "运动处方式 (FIT-PRIME)", "SPSS", "R (RStudio)", "Excel", "Python (pandas)", "MATLAB", "NVivo", "Atlas.ti", "智能穿戴设备 (Apple Watch)", "运动APP (MyFitnessPal)", "膳食评估系统"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)