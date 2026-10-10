"""生物学及相关学科（Not Elsewhere Classified）论文支持：未单列的生态、进化、保护与交叉生物学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biological_and_related_sciences_not",
    aliases=(
        "biological and related sciences not", "生物学及相关学科（未单列）",
        "biology not elsewhere classified", "生物学（NEC）",
        "ecology and evolution", "生态与进化",
        "conservation biology", "保护生物学",
        "behavioral ecology", "行为生态学",
        "environmental biology", "环境生物学",
        "population biology", "种群生物学",
    ),
    paper_types={
        "research": (
            "abstract", "introduction（背景与生态学/进化问题）",
            "materials and methods（样地、采样、统计）",
            "results", "discussion", "references",
        ),
        "review": (
            "abstract", "introduction",
            "main developments（按主题/系统综述）",
            "outlook", "references",
        ),
        "field_study": (
            "abstract", "研究区与样地", "材料与方法",
            "结果", "讨论", "参考文献",
        ),
        "case_study": (
            "abstract", "背景（物种、栖息地、人类活动）",
            "方法", "结果", "讨论", "references",
        ),
    },
    citation_style="APA 7 或 Chicago；生态学遵循 Ecological Society of America 样式",
    reporting_standards={
        "fieldwork": "样地、时间、气候、GPS 坐标须交代",
        "statistics": "样本量、统计检验、显著性水平须报告",
        "conservation": "IUCN 受威胁等级与栖息地状况须报告",
        "eDNA": "eDNA 采样方法、PCR 引物、测序深度须报告",
        "reproducibility": "数据与代码须公开（如 GitHub / Dryad）",
    },
    conventions=(
        "物种名（属+种加词）斜体；命名人与年须给出",
        "采样点 GPS 坐标须给出（可附附录）",
        "图版/照片须标尺度与拍摄条件",
        "分布图须用标准底图（如 ArcGIS、QGIS）",
        "生态学指标（Shannon、Simpson、Jaccard）须给定义",
    ),
    key_venues=(
        "Nature",
        "Science",
        "PNAS",
        "Ecology Letters",
        "Ecology",
        "Ecological Applications",
        "Journal of Animal Ecology",
        "Ecology and Evolution",
        "Conservation Biology",
        "Molecular Ecology",
    ),
    units_and_formulas_notes=(
        "长度/质量按 SI 单位；体长用体长（mm）",
        "种群密度用 ind./m² 或 ind./ha",
        "多样性指数（Shannon H、Simpson D）须给公式",
        "公式用 amsmath；统计学指标须给定义",
        "数值结果给出均值 ± SD/SE 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Nikon / Canon 数码相机", "Z-mount / Nikon DSLR（显微摄影）", "相机陷阱（Reconyx HyperFire）", "红外相机（Reconyx）", "eDNA 采样（EnviroDNA 试剂盒）", "eDNA 提取（QIAamp DNA Kit）", "PCR 仪（Thermo / Eppendorf）", "qPCR 仪（Bio-Rad / Thermo）", "Sanger 测序仪（Applied Biosystems 3730）", "Illumina MiSeq（高通量测序）", "Oxford Nanopore MinION（便携测序）", "GeneGun（基因枪）", "流式细胞仪（BD FACSCanto）", "Western blot 成像（Bio-Rad）", "ImageJ / Fiji", "MorphoJ（几何形态测量）", "Geomorph (R)", "TpsDig / TpsRelw（形态测量）", "R 语言（生态分析）", "Python (NumPy, SciPy, pandas)", "ArcGIS / QGIS（地理信息系统）", "SPSS", "Minitab", "Origin", "GraphPad Prism", "SigmaPlot", "Excel", "LaTeX", "EndNote", "Zotero", "Dryad（数据发布）", "GitHub", "Camera Trap Manager", "R Package: vegan（生态学）", "R Package: lme4（混合模型）", "R Package: glmmTMB（广义混合模型）", "R Package: phytools（系统发育）", "DNA Barcoding（COI / ITS）", "COI PCR", "ITS PCR", "16S rRNA PCR", "18S rRNA PCR", "荧光显微镜", "荧光染色"),
    category="理学",
    databases=("PubMed", "Europe PMC", "OpenAlex", "iNaturalist", "GBIF", "BOLD", "NCBI", "Dryad"),
)
