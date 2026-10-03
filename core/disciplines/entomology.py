"""昆虫学学科论文支持：昆虫分类/昆虫生态体裁、Wiley 引用样式与昆虫学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="entomology",
    aliases=("entomology", "昆虫学", "昆虫分类学", "insect taxonomy", "昆虫生态学",
             "insect ecology", "昆虫生理学", "insect physiology", "害虫防治", "pest management"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与昆虫类群）",
            "materials and methods（采集、饲养与实验）",
            "results（形态/生态/生理数据）",
            "discussion（进化与应用意义）",
            "references",
        ),
        "taxonomic": (
            "abstract",
            "introduction",
            "materials and methods（标本与形态测量）",
            "taxonomic treatment（新种描述与检索表）",
            "discussion（系统关系）",
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
    citation_style="Wiley 样式（作者-年份；Insect Sci. 遵循 Wiley 规范）",
    reporting_standards={
        "specimen_info": "标本数量、采集地点与日期须报告",
        "rearing_conditions": "饲养条件（温度、光周期、寄主）须完整",
        "bioassay_methods": "生物测定（毒力、行为）方法须报告",
        "statistics": "统计检验与样本量须给出",
        "voucher_specimens": "凭证标本与保藏机构须给出",
    },
    conventions=(
        "学名用斜体（Drosophila melanogaster），首次出现给出命名人",
        "发育阶段（卵、幼虫、蛹、成虫）术语统一",
        "形态测量与翅脉术语规范",
        "生物测定指标（LC50、LT50）定义须给出",
        "新种描述遵循 ICZN 命名法规",
    ),
    key_venues=(
        "Insect Science",
        "Journal of Insect Physiology",
        "Ecological Entomology",
        "Systematic Entomology",
        "Journal of Economic Entomology",
        "Annual Review of Entomology",
    ),
    units_and_formulas_notes=(
        "体长用 mm；体重用 mg",
        "温度用 °C；光周期用 L:D（如 16:8）",
        "公式用 amsmath；毒力回归与生命表公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SE 与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "R (stats)",
        "体视显微镜",
        "昆虫标本针插与烘箱",
        "杀虫剂生测设备",
        "GIS (QGIS)",
    ),
    category="理学",
    databases=(
        "PubMed",
        "OpenAlex",
        "bioRxiv",
        "Zenodo",
        "CNKI",
    ),
)