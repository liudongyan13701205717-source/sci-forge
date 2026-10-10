"""植物学学科论文支持：植物生理/植物分类体裁、Wiley 引用样式与植物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="botany",
    aliases=("botany", "植物学", "植物生理学", "plant physiology", "植物分类学",
             "plant taxonomy", "植物生态学", "plant ecology", "植物解剖学", "plant anatomy",
             "植物遗传学", "plant genetics", "分子植物学", "molecular plant biology",
             "plant molecular biology", "系统植物学", "systematic botany"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与植物体系）",
            "materials and methods（材料、生长条件与测定）",
            "results（生理/形态/分类数据）",
            "discussion（机理与意义）",
            "references",
        ),
        "taxonomic": (
            "abstract",
            "introduction",
            "materials and methods（标本与形态测量）",
            "taxonomic treatment（分类处理与检索表）",
            "discussion（系统位置）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按类群/过程综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Wiley 样式（作者-年份；New Phytol. 遵循 Wiley 规范）",
    reporting_standards={
        "plant_material": "植物材料（物种、品种、生长阶段）须报告",
        "growth_conditions": "光照、温度、湿度与营养条件须完整",
        "measurement_methods": "生理指标测定方法（光合、蒸腾、叶绿素）须报告",
        "statistics": "统计检验与重复数须给出",
        "voucher_specimens": "分类研究须给出凭证标本与馆藏编号",
    },
    conventions=(
        "学名用斜体（Arabidopsis thaliana），首次出现给出命名人",
        "品种名用单引号（'Col-0'）",
        "光合参数符号（A、g_s、E、Fv/Fm）统一",
        "生长条件（光周期、PPFD）规范报告",
        "标本馆缩写（K、PE 等）遵循 Index Herbariorum",
        "分类等级按界-门-纲-目-科-属-种顺序列示",
    ),
    key_venues=(
        "New Phytologist",
        "Plant Physiology",
        "Plant Cell",
        "Annals of Botany",
        "American Journal of Botany",
        "Journal of Experimental Botany",
        "Plant Journal",
        "Plant Cell & Environment",
        "Molecular Plant",
        "Plant Molecular Biology",
    ),
    units_and_formulas_notes=(
        "光合速率用 μmol CO2 m^-2 s^-1；蒸腾用 mmol H2O m^-2 s^-1",
        "光强用 μmol m^-2 s^-1（PPFD）",
        "公式用 amsmath；光合与水分关系式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SE 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("光学显微镜", "共聚焦显微镜", "扫描电子显微镜（SEM）", "透射电子显微镜（TEM）", "LI-6400 便携式光合测定仪", "LI-6800 光呼吸测定仪", "植物标本数字化扫描仪", "气相色谱-质谱（GC-MS）", "液相色谱-质谱（LC-MS）", "高分辨质谱（HRMS）", "核磁共振（NMR）", "ImageJ / Fiji", "ZEN (Zeiss)", "NIS-Elements (Nikon)", "QuPath", "CellProfiler", "CellPose", "Python", "R (ggplot2)", "QGIS"),
    category="理学",
    databases=(
        "PubMed",
        "OpenAlex",
        "bioRxiv",
        "Zenodo",
        "CNKI",
        "GBIF",
        "iDigBio",
        "World Plants",
    ),
)
