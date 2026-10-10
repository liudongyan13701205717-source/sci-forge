"""真菌学学科论文支持：真菌分类/真菌生理体裁、Wiley 引用样式与真菌学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mycology",
    aliases=(
        "mycology", "真菌学", "Fungal biology", "fungal taxonomy",
        "真菌分类学", "fungal physiology", "真菌生理学",
        "lichenology", "地衣学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与真菌类群）",
            "methodology（菌株、培养与测定）",
            "results（形态/生理/分子数据）",
            "discussion（分类与生态意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（菌株与生态背景）",
            "analysis（形态与分子分析）",
            "results（分类结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述主题）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Wiley 样式（Mycol. Res. 遵循 Elsevier/Wiley 规范）",
    reporting_standards={
        "k1": "新种描述须遵循 ICN 命名法规",
        "k2": "分子系统学须报告序列登录号与分析方法",
        "k3": "生态研究须报告采样点、时间与生境描述",
    },
    conventions=(
        "学名用斜体（Aspergillus niger），首次出现给出命名人",
        "孢子测量格式（长 × 宽 μm）统一",
        "培养基缩写（PDA、MEA）首次出现处给出全称",
        "显微特征（孢子、菌丝、产孢结构）术语规范",
        "新种描述遵循 ICN 命名法规",
    ),
    key_venues=(
        "Mycologia",
        "Fungal Biology",
        "Persoonia",
        "Studies in Mycology",
        "Fungal Diversity",
    ),
    units_and_formulas_notes=(
        "孢子与结构尺寸用 μm",
        "温度用 °C；时间用 d（天）",
        "公式用 amsmath；生长速率与产孢量公式须明确",
        "数值结果给出均值 ± SD 与范围",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("光学显微镜 (Leica DM2500)", "荧光显微镜", "透射电镜 (TEM)", "PCR 仪 (Bio-Rad C1000)", "真菌恒温培养箱 (TSI)", "ITS 测序平台 (Illumina MiSeq)", "MALDI-TOF MS (Bruker)", "R (phangorn)", "MEGA X", "PhyML", "IQ-TREE", "RAxML", "BEAST 2", "Fungal Diversity Database", "UNITE ITS database", "GenBank", "EndNote", "Zotero", "ImageJ", "Python"),
    category="理学",
    databases=("PubMed", "OpenAlex", "bioRxiv", "Zenodo", "Europe PMC"),
)
