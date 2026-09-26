"""真菌学学科论文支持：真菌分类/真菌生理体裁、Wiley 引用样式与真菌学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mycology",
    aliases=("mycology", "真菌学", "真菌分类学", "fungal taxonomy", "真菌生理学",
             "fungal physiology", "地衣学", "lichenology", "真菌生态学", "fungal ecology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与真菌类群）",
            "materials and methods（菌株、培养与测定）",
            "results（形态/生理/分子数据）",
            "discussion（分类与生态意义）",
            "references",
        ),
        "taxonomic": (
            "abstract",
            "introduction",
            "materials and methods（标本与分子系统学）",
            "taxonomic treatment（新种/新组合描述）",
            "discussion（系统位置）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按类群/主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Wiley 样式（作者-年份；Mycol. Res. 遵循 Elsevier/Wiley 规范）",
    reporting_standards={
        "strain_info": "菌株编号与保藏号（CBS、ATCC 等）须报告",
        "culture_conditions": "培养基、温度与培养时间须完整",
        "morphological_data": "形态描述（孢子、子实体）与显微测量须报告",
        "molecular_data": "序列数据与 GenBank 登录号须给出",
        "type_specimens": "新种须指定模式标本与保藏机构",
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
        "Mycological Progress",
    ),
    units_and_formulas_notes=(
        "孢子与结构尺寸用 μm",
        "温度用 °C；时间用 d（天）",
        "公式用 amsmath；生长速率与产孢量公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与范围",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "光学显微镜",
        "PCR 仪",
        "真菌恒温培养箱",
        "ITS 序列测序平台",
        "R (phangorn)",
    ),
    category="理学",
    databases=(
        "PubMed",
        "OpenAlex",
        "bioRxiv",
        "Zenodo",
        "Europe PMC",
    ),
)