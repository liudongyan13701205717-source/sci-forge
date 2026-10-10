"""传统互补与整合医学学科论文支持：中西医结合临床研究体裁、PRISMA/CONSORT 与中药网络药理学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="traditional_complementary_and_integrative_medicine",
    aliases=("traditional_complementary_and_integrative_medicine", "传统互补与整合医学",
             "中西医结合", "整合医学", "互补医学",
             "integrative medicine", "complementary medicine", "中西医结合医学",
             "TCM-integrated medicine"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、理论依据与研究目的）",
            "methods（研究设计、人群、干预方案与统计方法）",
            "results（证候改善、生化指标与疗效数据）",
            "discussion（机理阐释与整合医学意义）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "search strategy and inclusion criteria",
            "results（纳入研究特征与合并结果）",
            "discussion（证据质量与不确定性）",
            "conclusion",
            "references",
        ),
        "network_pharmacology": (
            "abstract",
            "introduction",
            "methods（成分预测、靶点注释、网络构建与验证）",
            "results（网络拓扑与通路富集）",
            "discussion（实验验证与转化前景）",
            "references",
        ),
    },
    citation_style="GB/T 7714（中文）或 Vancouver（英文）",
    reporting_standards={
        "randomized_trial": "RCT 遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "network_pharmacology": "网络药理学研究须报告数据库版本与检索日期",
        "safety": "不良事件须完整记录并报告发生率",
    },
    conventions=(
        "中药名称用中文名并附拉丁学名（首次出现）",
        "方剂组成（药味、剂量、炮制）须完整报告",
        "整合治疗方案须说明中西医方案的衔接与主次关系",
        "统计方法须报告主要终点、效应量与置信区间",
        "网络药理学结果须配合至少一项实验验证",
    ),
    key_venues=(
        "Journal of Integrative Medicine",
        "Journal of Ethnopharmacology",
        "Frontiers in Pharmacology",
        "Phytomedicine",
        "中国中西医结合杂志",
        "中华中医药杂志",
    ),
    units_and_formulas_notes=(
        "剂量用 g（饮片）或 mg（提取物），配方颗粒标注规格",
        "方剂配比与提取率计算式须明确",
        "网络拓扑指标须注明节点/边数与算法",
        "统计结果给出均值 ± SD/SEM 与样本量",
        "效应量报告 RR/OR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("中医体质辨识仪", "红外热像仪", "微循环检测仪", "经络仪", "艾灸器具", "拔罐器具", "刮痧器具", "推拿手法采集系统", "心电监护仪", "经皮神经电刺激仪", "Cytoscape", "NetworkX", "R", "SPSS", "Stata", "RevMan（Cochrane）", "PRISMA 筛选工具", "Python", "Excel", "NVivo"),
    category="医学",
    databases=("PubMed", "CNKI", "万方", "OpenAlex", "TCMSP"),
)
