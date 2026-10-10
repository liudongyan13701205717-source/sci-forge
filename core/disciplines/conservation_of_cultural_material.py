"""文化遗产保护学科论文支持：材料分析、无损检测、修复与预防性保护。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="conservation_of_cultural_material",
    aliases=(
        "conservation of cultural material",
        "conservation science",
        "文化遗产保护",
        "文物保护",
        "文物修复",
        "cultural heritage conservation",
        "materials science for conservation",
        "预防性保护",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（样品、分析手段与无损检测）",
            "results（成分/结构/劣化机理分析）",
            "conservation intervention（干预方案与效果评估）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "object description（文物基本信息与保存状况）",
            "deterioration diagnosis（劣化机理）",
            "treatment procedure（修复步骤）",
            "post-treatment assessment",
            "references",
        ),
        "review": (
            "abstract",
            "historical background",
            "current methods and techniques",
            "open challenges",
            "references",
        ),
    },
    citation_style="Chicago/Turabian（编号），文物报告常用 ISO 11790",
    reporting_standards={
        "sampling": "采样须遵循最小干预原则，优先使用无损方法并记录取样点坐标",
        "analysis": "XRF/XRD/FTIR/Raman/HPLC 结果须报告设备型号、激发源、分辨率与检测限",
        "documentation": "修复前后须有高清影像、三维记录与劣化等级对照（如 EN 15757）",
        "reversibility": "所有干预材料须满足可逆性与相容性要求（ICCROM 准则）",
        "standards": "引用标准须标注 ISO 11790、EN 15757 或 GB/T 编号",
    },
    conventions=(
        "采用最小干预与可逆性原则（minimal intervention, reversibility）",
        "劣化分级使用标准化量表（如 AATCC 灰卡、EN 15757）",
        "成分分析报告必须含元素权重百分比、误差范围与检测限",
        "修复材料须注明品牌、批号、化学成分与老化测试结果",
        "三维数字化成果须附点云精度、覆盖率与坐标系统说明",
        "文献引用优先使用 ICCROM、Getty Conservation Institute 系列",
    ),
    key_venues=(
        "Journal of Cultural Heritage",
        "International Journal of Conservation Science",
        "Heritage Science",
        "Studies in Conservation",
        "Restaurator",
        "国际文物保护杂志",
        "文物",
        "考古与文物",
        "文物保护",
    ),
    units_and_formulas_notes=(
        "元素含量用 wt% 或 ppm；同位素 δ 值注明参考标准（SMOW/VSMOW）",
        "XRF 检测限给出 3σ 或 LOD；Raman 位移用 cm⁻¹",
        "色差用 CIE ΔE*（L*ab 空间）",
        "影像记录给出分辨率、色域与色卡参考",
        "年代结果用 BP 或 cal BP（Calib/INTCAL20）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("Leica BLK360", "Faro Focus", "Zeiss Contura", "Artec Space Spider", "Fotogrammetria ContextCapture", "Agisoft Metashape", "RealityCapture", "MeshLab", "Cloud Compare", "3D Slicer", "ImageJ/Fiji", "Oxford X-MET8000 (XRF)", "Horiba XGT-8000", "Thermo Scientific iCAP (ICP-MS)", "Bruker D8 ADVANCE (XRD)", "Thermo Nicolet iS50 (FTIR)", "Horiba LabRAM HR (Raman)", "JASCO BioRad HPLC", "Agilent 7900 ICP-MS", "Zeiss Sigma 300 (SEM)", "Malvern Mastersizer (粒径)", "Karl Fischer 水分仪", "DTS 数字热成像仪 (FLIR T1040)", "BenthoScan UV-Vis 光谱仪", "Zebraskop 数字显微镜", "SpectralWorks SWIR/HYDRA 多光谱", "DPS Hyperspec (高光谱成像)", "Artesia 数字化绘图", "Xenon Lightbox 灯箱", "Nikon DS-Dc2 显微镜相机", "Arches CMS (藏品管理)", "Teneo (馆藏系统)", "Emu (博物馆藏品)"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "Web of Science", "CNKI", "万方", "Zenodo", "Europeana"),
)
