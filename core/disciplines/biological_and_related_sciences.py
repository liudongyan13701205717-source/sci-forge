"""生物学及相关学科（Biological and Related Sciences）论文支持：动植物、微生物、生态与形态学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biological_and_related_sciences",
    aliases=(
        "biological and related sciences", "生物学及相关学科",
        "biology", "生物学", "生命科学", "life sciences",
        "动物学", "zoology", "植物学", "botany", "生态学", "ecology",
        "微生物学", "microbiology", "形态学", "morphology",
    ),
    paper_types={
        "research": (
            "abstract", "introduction（背景与生物学问题）",
            "materials and methods（材料、方法、统计分析）",
            "results", "discussion", "references",
        ),
        "review": (
            "abstract", "introduction",
            "main developments（按主题/分类/系统综述）",
            "outlook", "references",
        ),
        "species_description": (
            "abstract", "背景与鉴别历史",
            "标本（正模、副模）描述",
            "分类与分布", "讨论", "references",
        ),
        "field_study": (
            "abstract", "研究区与样地", "材料与方法",
            "结果", "讨论", "参考文献",
        ),
    },
    citation_style="APA 7 或 Chicago；动物学遵循 Zootaxa 规范；植物学遵循 Botanische Jahrbücher 规范",
    reporting_standards={
        "species_description": "新种描述须遵循 ICZN 或 ICN（ICN 2018）规范",
        "specimens": "标本馆编号与保存地须报告",
        "fieldwork": "样地、时间、气候须交代",
        "statistics": "样本量、统计检验、显著性水平须报告",
        "conservation": "IUCN 受威胁等级须报告",
    },
    conventions=(
        "物种名（属+种加词）斜体；命名人与年须给出",
        "首次使用缩写须定义；学名首字母大写（属）小写（种）",
        "采样点 GPS 坐标须给出（可附附录）",
        "图版/照片须标尺度与拍摄条件",
        "分布图须用标准底图（如 ArcGIS、QGIS）",
    ),
    key_venues=(
        "Nature",
        "Science",
        "PNAS",
        "Current Biology",
        "Ecology Letters",
        "Ecology",
        "Journal of Animal Ecology",
        "Systematic Biology",
        "Zootaxa",
        "Zootaxa",
        "Zootaxa",
    ),
    units_and_formulas_notes=(
        "长度/质量按 SI 单位；体长用体长（mm）",
        "种群密度用 ind./m² 或 ind./ha",
        "公式用 amsmath；统计学指标须给定义",
        "数值结果给出均值 ± SD/SE 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Nikon Microscope（光学显微镜）", "Zeiss Stereo Microscope", "Zeiss LSM 共聚焦显微镜", "Olympus 显微镜", "Leica Stereo Microscope", "数码成像（Nikon D5 / Canon 5D）", "显微摄影（Z-mount / Nikon DSLR）", "PCR 仪（Thermo / Eppendorf）", "qPCR 仪（Bio-Rad / Thermo）", "Sanger 测序仪（Applied Biosystems 3730）", "Illumina MiSeq（高通量测序）", "GeneGun（基因枪）", "流式细胞仪（BD）", "Western blot 成像（Bio-Rad）", "ImageJ / Fiji", "MorphoJ（几何形态测量）", "Geomorph (R)", "TpsDig / TpsRelw（形态测量）", "R 语言（生态分析）", "Python (NumPy, SciPy, pandas)", "ArcGIS / QGIS（地理信息系统）", "GIS（地理信息系统）", "SPSS", "Minitab", "Origin", "GraphPad Prism", "SigmaPlot", "Excel", "LaTeX", "EndNote", "Zotero", "Bio-Protocol", "Bio-protocol", "Camera Trap（红外相机）", "eDNA 采样（环境 DNA）", "eDNA 分析", "DNA Barcoding（COI / ITS）", "COI PCR", "ITS PCR", "16S rRNA PCR", "18S rRNA PCR", "荧光显微镜", "荧光染色"),
    category="理学",
    databases=("PubMed", "Europe PMC", "OpenAlex", "iNaturalist", "GBIF", "BOLD", "NCBI"),
)
