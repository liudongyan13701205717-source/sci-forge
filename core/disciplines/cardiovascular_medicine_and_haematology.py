"""Cardiovascular Medicine And Haematology 学科论文支持：心血管与血液临床体裁、ACVA/HAS 报告标准与器材/软件注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cardiovascular_medicine_and_haematology",
    aliases=("cardiovascular medicine and haematology", "心血管医学与血液学",
             "心血管与血液", "血管内科", "血液病学", "心血管科",
             "cardiovascular haematology", "blood medicine", "血液科", "circulatory medicine"),
    paper_types={
        "research": (
            "abstract",
            "introduction（临床背景与问题）",
            "methods（设计、人群与评估）",
            "results（终点与数据）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "按主题综述",
            "展望",
            "references",
        ),
    },
    citation_style="ACVA/HAS 样式（Vancouver 数字编号）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=(
        "血压 mmHg、心率 bpm、血氧 % 须统一",
        "血液指标（Hb、PLT、INR 等）首现给出全称与单位",
        "血栓/出血事件定义须明确",
        "合并用药须完整报告",
        "试验注册信息须标注（NCT 号）",
    ),
    key_venues=(
        "Blood",
        "Haematologica",
        "Thrombosis and Haemostasis",
        "Journal of Thrombosis and Haemostasis",
        "Circulation",
        "European Heart Journal",
        "Cardiovascular Research",
        "Chest",
    ),
    units_and_formulas_notes=(
        "血容量/浓度用 SI 单位",
        "凝因/PT/INR 须注明检测试剂与校准",
        "生存分析给出 HR 与 95% CI",
        "数值结果给出均值 ± SD 与样本量",
        "公式用 amsmath，仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("血细胞分析仪", "凝血分析仪", "流式细胞仪", "超声心动图", "冠脉 CT", "Holter 动态心电图", "心电监护仪", "血气分析仪", "SpO2 血氧仪", "血栓弹性图仪", "骨髓穿刺/活检器械", "PCR 仪", "基因测序仪", "SPSS", "R", "Python", "Excel", "GraphPad Prism", "FlowCast 流式分析", "Cryo-TEM 冷冻透射电镜"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "Semantic Scholar"),
)
