"""Agricultural sciences 学科论文支持：农业科学/作物-土壤-植物-资源综合研究体裁、ASA 样式与农艺注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agricultural_sciences",
    aliases=(
        "agricultural sciences",
        "农业科学",
        "农业科学综合",
        "大农学",
        "agricultural science",
        "农学科学",
        "农学总论",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（试验点/气候/土壤/处理）",
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
            "yield and nutrient analysis",
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
    citation_style="ASA-CSSA-SSSA style 或 Elsevier numbered（AJAE/APA 7 用于经济社会学分支）",
    reporting_standards={
        "trial": "田间试验设计（随机区组/裂区）、重复数与小区面积须给出",
        "soil": "土壤类型、pH、有机质、养分与前茬须报告",
        "climate": "试验季气象数据（降水/积温）须给出并标注来源",
        "statistics": "统计用 ANOVA+多重比较（LSD/Tukey）；效应量与置信区间须给",
        "protocol": "试验方案须遵循 FAIR 数据与 AAAAM 惯例",
    },
    conventions=(
        "试验地点、面积、年份、重复数与小区面积须完整报告",
        "土壤类型、pH、有机质、养分、前茬必须逐点说明",
        "农艺性状须给出测定方法与仪器型号（SPAD、LAI、株高、穗长）",
        "品种名给正式登记名；转基因材料注明转化事件",
    ),
    key_venues=(
        "Field Crops Research",
        "Agronomy Journal",
        "Plant and Soil",
        "European Journal of Agronomy",
        "Journal of Agricultural Science",
        "Nature Plants",
        "Agricultural Sciences (MDPI)",
    ),
    units_and_formulas_notes=(
        "产量 t/ha 或 kg/ha；养分按 N-P2O5-K2O 折算",
        "水分利用效率 WUE = 产量/蒸散量；单位 kg/m³",
        "氮素利用率 NUE = 籽粒吸氮/施氮量；光能利用率 LUE = GPP/截获辐射",
        "公式用 amsmath；显示公式仅在被引用时编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("DSSAT", "APSIM", "STICS", "CropScape", "AquaCrop", "WOFOST", "ArcGIS", "QGIS", "R", "SPSS", "Origin", "Microsoft Excel", "ImageJ", "Spectroradiometer ASD FR", "Plant Spectrometer SPAD-501", "LAI Scanner LiCor", "Soil Particle Analyzer", "Chorley Soil Texture Hydrometer", "Drone DJI Phantom", "Sentinel-2"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "FAOSTAT", "NASA POWER", "HLS", "USDA NRCS"),
)
