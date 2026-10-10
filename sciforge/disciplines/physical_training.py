"""体能训练学科论文支持：力量/耐力/技术训练体裁、APA 引用样式与体能记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="physical_training",
    aliases=("physical_training", "体能训练", "physical training", "力量训练",
             "strength training", "运动训练", "sports training", "运动表现", "performance",
             "体能发展", "physical development", "运动表现评估"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与训练问题）",
            "methodology（训练方案与研究设计）",
            "results（训练效果终点）",
            "discussion（训练学意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（运动员/队伍描述）",
            "analysis（训练方案与实施）",
            "results（表现提升）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（训练学理论）",
            "evidence synthesis（训练干预综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；Strength & Conditioning Journal 遵循 APA 规范）",
    reporting_standards={
        "training_protocol": "训练方案须完整报告（负荷、组数、次数、休息、频率）",
        "intervention": "干预研究遵循 CONSORT/SPORT 声明",
        "biomechanics": "生物力学研究遵循 ISB 运动学/动力学规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "monitoring": "训练监控遵循 Acute:Chronic Workload Ratio (ACWR) 框架"
    },
    conventions=(
        "负荷用 1RM 或 %1RM 表示；功率用 W 或 W/kg",
        "训练监控指标（HRV、HR、GPS 距离、RPE、sRPE）须完整报告",
        "样本按性别、年龄、水平分组报告",
        "测试工具（力量/爆发/耐力）须注明来源与信效度",
        "统计显著性阈值与效应量须明确"
    ),
    key_venues=(
        "Journal of Strength and Conditioning Research",
        "Sports Medicine",
        "British Journal of Sports Medicine",
        "International Journal of Sports Physiology and Performance",
        "Journal of Sport and Health Science",
        "Strength & Conditioning Journal"
    ),
    units_and_formulas_notes=(
        "速度用 m/s；功率用 W；力量用 N 或 kgf；耐力用 mL/kg/min",
        "公式用 amsmath；功率、负荷、ACWR 计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "效应量给出 Cohen's d 或 η² 与 95% CI"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("EliteFTS 力量训练软件", "Catapult GPS 追踪系统", "Polar 心率带", "Garmin Forerunner", "Fitbit", "WHOstep", "Kinesys 肌电信号系统", "SMART 运动分析系统", "Dartfish 视频分析", "Kinovea", "Tracker 视频分析", "体成分分析仪 (InBody)", "Biodex 等速力量测试仪", "Isomed 2000 功率车", "Cybex 力量训练器", "VO2max 测试平台", "弹力带与哑铃训练器材", "Stronglifts 训练记录软件", "MyFitnessPal", "Excel 训练记录表"),
    category="教育学",
    databases=("CNKI", "万方", "OpenAlex", "PubMed"),
)
