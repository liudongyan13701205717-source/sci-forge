"""血液学学科论文支持：血液临床/实验体裁、ASH/Blood 引用样式与血液学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hematology",
    aliases=("hematology", "血液学", "血液科", "血液病学",
             "haematology", "血液肿瘤"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与血液问题）",
            "methods（研究设计与人群）",
            "results（血象与分子数据）",
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
        "translational": (
            "abstract",
            "introduction",
            "results（分子/免疫学发现）",
            "discussion（转化意义）",
            "materials and methods",
            "references",
        ),
    },
    citation_style="ASH/Blood 样式（作者-年份；Blood 遵循 ASH 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "biomarker": "生物标志物研究遵循 REMARK 指南",
    },
    conventions=(
        "血细胞计数单位（×10⁹/L）须规范",
        "血液肿瘤分类（WHO/ICC）须注明版本",
        "疗效标准（CR、MRD 等）首次出现给出定义",
        "分子检测（NGS、FISH）方法与阈值须报告",
        "凝血参数（INR、APTT）单位须规范",
    ),
    key_venues=(
        "Blood",
        "Blood Advances",
        "The Lancet Haematology",
        "Leukemia",
        "Haematologica",
        "Journal of Clinical Oncology",
    ),
    units_and_formulas_notes=(
        "血细胞用 ×10⁹/L；血红蛋白用 g/L",
        "公式用 amsmath；MRD 阈值与疗效定义式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "生存分析给出 HR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("血细胞分析仪", "流式细胞仪", "凝血分析仪", "SPSS"),
    category="医学",
    databases=("PubMed", "OpenAlex", "GEO", "CNKI"),
)