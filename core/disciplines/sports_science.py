"""运动科学学科论文支持：运动科学体裁、APA 引用样式与运动科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sports_science",
    aliases=("sports_science", "运动科学", "运动训练学", "运动表现",
             "sport science", "运动生理学与训练"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与运动科学问题）",
            "methods（研究设计与受试者）",
            "results（表现与生理数据）",
            "discussion（机理与训练意义）",
            "references",
        ),
        "performance_analysis": (
            "abstract",
            "introduction",
            "methods（测试方案与指标）",
            "results（表现指标数据）",
            "discussion（与既往研究对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Sports Medicine 等期刊遵循 APA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "meta_analysis": "荟萃分析遵循 PRISMA 声明",
        "performance_analysis": "运动表现测试报告遵循标准测试报告规范",
    },
    conventions=(
        "受试者特征（年龄、训练状态、样本量）须报告",
        "测试方案与负荷设定须可复现",
        "生理指标（VO2max、乳酸阈等）首次出现给出全称",
        "训练干预（频率、强度、时长）须完整描述",
        "数据缺失与脱落受试者须说明",
    ),
    key_venues=(
        "Sports Medicine",
        "International Journal of Sports Physiology and Performance",
        "Journal of Sports Sciences",
        "European Journal of Sport Science",
        "Scandinavian Journal of Medicine & Science in Sports",
        "Journal of Science and Medicine in Sport",
    ),
    units_and_formulas_notes=(
        "功率用 W/kg；VO2max 用 ml/kg/min",
        "训练负荷用 AU；主观强度用 RPE（6-20 或 CR-10）",
        "公式用 amsmath；相对强度与负荷计算式须明确",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "效应量给出 Cohen's d 或 η²",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "体成分分析仪（InBody）",
        "心率与生理监测仪（Polar）",
        "气体分析仪与代谢车",
        "R 语言统计分析",
        "G*Power 样本量估算",
    ),
    category="教育学",
    databases=("CNKI", "万方", "OpenAlex", "PubMed"),
)