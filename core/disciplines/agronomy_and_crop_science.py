"""Agronomy and crop science 学科论文支持：作物栽培/遗传育种/育种学体裁、ASA-CSSA-SSSA 与作物注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agronomy_and_crop_science",
    aliases=(
        "agronomy and crop science",
        "作物栽培",
        "作物科学",
        "育种学",
        "agronomy",
        "crop science",
        "breeding",
        "crops",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（育种材料/田间设计）",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "field_trial": (
            "abstract",
            "introduction",
            "site description（土壤/气候/前茬）",
            "experimental design",
            "results",
            "yield and quality analysis",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope",
            "findings",
            "research gaps",
            "references",
        ),
    },
    citation_style="ASA-CSSA-SSSA style 或 Elsevier numbered",
    reporting_standards={
        "trial": "田间试验设计（随机区组/裂区）、重复数与小区面积须给出",
        "soil": "土壤类型、pH、有机质、前茬与基础肥力须报告",
        "climate": "试验季气象数据（降水/积温）须给出（来源写明）",
        "yield": "产量按标准含水率折算；统计用 ANOVA+多重比较（LSD/Tukey）",
        "breeding": "试验品种登记名与系谱（pedigree）须完整",
    },
    conventions=(
        "品种名给正式登记名；转基因材料注明转化事件与载体",
        "农艺性状给测定方法（SPAD、LAI、株高、穗长、结实率）与仪器型号",
        "产量按标准含水率折算；显著性字母标注法一致",
        "单位用 SI（kg/ha、t/ha、mm）；养分按 N-P2O5-K2O 折算",
    ),
    key_venues=(
        "Crop Science",
        "Agronomy Journal",
        "Field Crops Research",
        "Plant and Soil",
        "European Journal of Agronomy",
        "Field Crops Research (Elsevier)",
        "The Crop Journal",
        "Crop Research",
    ),
    units_and_formulas_notes=(
        "产量 t/ha 或 kg/ha；养分利用率（NUE/PFP）公式须给出",
        "水分利用效率 WUE = 产量/蒸散量；单位 kg/m³",
        "光能利用率 LUE = GPP/截获辐射；单位 g/MJ",
        "公式用 amsmath；显示公式仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("DSSAT", "APSIM", "STICS", "CERES", "WOFOST", "AquaCrop", "CropScape", "Spectroradiometer ASD FR", "Plant Spectrometer SPAD-501", "LAI Scanner LiCor", "Soil Texture Analyzer", "Soil Particle Analyzer", "Drone DJI Phantom", "Drone DJI Matrice", "ArcGIS", "QGIS", "ImageJ", "R", "SPSS", "Origin"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "USDA-ARS", "FAOSTAT", "NASA POWER", "CGIAR", "Crop Trust"),
)
