"""中医学学科论文支持：中医临床/方药体裁、GB/T 7714 与 J Ethnopharmacol 引用样式及中医记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="traditional_chinese_medicine",
    aliases=("traditional_chinese_medicine", "中医学", "中医", "中医药",
             "TCM", "traditional Chinese medicine", "中西医结合"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与中医问题）",
            "methods（研究设计与人群）",
            "results（证候与疗效数据）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法与统计）",
            "results（疗效与安全性终点）",
            "discussion（与既往试验对比）",
            "references",
        ),
        "pharmacology": (
            "abstract",
            "introduction",
            "methods（方药成分与模型）",
            "results（活性与机制数据）",
            "discussion（方药机理）",
            "references",
        ),
    },
    citation_style="GB/T 7714（中文期刊）或 J Ethnopharmacol 样式（英文期刊）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明（中医药扩展）",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "herbal_quality": "中药质量研究遵循 CONSORT 草药扩展",
    },
    conventions=(
        "方剂组成（药味、剂量、炮制）须完整报告",
        "证候诊断标准须注明来源（教材/指南）",
        "中药名用中文名并附拉丁学名（首次出现）",
        "辨证论治过程须可复现",
        "针灸等疗法操作规范（取穴、手法）须报告",
    ),
    key_venues=(
        "Journal of Ethnopharmacology",
        "Phytomedicine",
        "Chinese Medicine",
        "Journal of Traditional Chinese Medicine",
        "Frontiers in Pharmacology",
        "中国中西医结合杂志",
    ),
    units_and_formulas_notes=(
        "剂量用 g（中药饮片）或 mg（提取物）",
        "公式用 amsmath；方剂配比与提取率计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "疗效分析给出 RR/OR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("SPSS", "R", "中药成分分析平台（LC-MS）", "中药分子对接软件"),
    category="医学",
    databases=("PubMed", "CNKI", "OpenAlex", "万方", "PubChem"),
)