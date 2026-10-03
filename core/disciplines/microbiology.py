"""微生物学学科论文支持：微生物生理/微生物组体裁、ASM 引用样式与微生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="microbiology",
    aliases=("microbiology", "微生物学", "细菌学", "bacteriology", "微生物组",
             "microbiome", "病毒学", "virology", "真菌学", "mycology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与微生物体系）",
            "results（实验发现与数据）",
            "discussion（机理与意义）",
            "materials and methods（菌株、培养与测定）",
            "references",
        ),
        "genomic": (
            "abstract",
            "introduction",
            "results（基因组特征、系统发育与功能注释）",
            "discussion（进化与生态意义）",
            "materials and methods（测序与生信流程）",
            "data availability（数据与菌株保藏号）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按类群/机制综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="ASM 样式（作者-年份；J. Bacteriol. 遵循 ASM 规范）",
    reporting_standards={
        "strain_info": "菌株编号（ATCC、DSMZ 等保藏号）须报告",
        "culture_conditions": "培养基、温度、通气与培养时间须完整",
        "growth_measurements": "生长曲线与 OD 测量条件须报告",
        "replicates": "生物学重复与技术重复次数须报告",
        "sequence_accession": "基因组/序列数据须给出 GenBank/ENA 登录号",
    },
    conventions=(
        "菌名用斜体（Escherichia coli），首次出现给出全称",
        "菌株编号与保藏号规范书写",
        "OD 测量注明波长（OD600）",
        "MIC/MBC 等药敏指标定义须给出",
        "培养基缩写（LB、TSB）首次出现处给出全称",
    ),
    key_venues=(
        "Journal of Bacteriology",
        "Applied and Environmental Microbiology",
        "mBio",
        "Microbiology Spectrum",
        "Nature Microbiology",
        "Cell Host & Microbe",
    ),
    units_and_formulas_notes=(
        "菌浓度用 CFU/mL；OD 无量纲",
        "温度用 °C；时间用 h/min",
        "公式用 amsmath；生长速率与倍增时间关系式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "PCR 仪",
        "流式细胞仪",
        "16S rRNA 测序平台",
        "厌氧培养箱",
        "Python (Biopython)",
    ),
    category="理学",
    databases=(
        "PubMed",
        "OpenAlex",
        "bioRxiv",
        "Europe PMC",
        "Zenodo",
    ),
)