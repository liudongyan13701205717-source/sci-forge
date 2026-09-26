"""遥感学科论文支持：遥感反演/分类/变化检测体裁、IEEE 引用样式与遥感度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="remote_sensing",
    aliases=("remote_sensing", "遥感", "遥感科学", "对地观测"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "algorithm_paper": (
            "abstract",
            "introduction",
            "data（遥感数据）",
            "method（算法）",
            "validation（验证）",
            "results（结果）",
            "references",
        ),
        "application_study": (
            "abstract",
            "introduction",
            "study area（研究区）",
            "data（数据）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号制；TGRS 遵循 IEEE 规范）",
    reporting_standards={
        "experimental": "实验遵循遥感算法评估规范",
        "validation": "验证遵循地面真值报告规范",
        "observational": "观测研究遵循遥感观测报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循遥感数据规范",
    },
    conventions=(
        "传感器与平台须报告",
        "影像预处理流程须说明",
        "地面真值数据须描述",
        "精度评价（OA/Kappa 等）须报告",
        "辐射与几何校正须说明",
    ),
    key_venues=(
        "IEEE Transactions on Geoscience and Remote Sensing",
        "Remote Sensing of Environment",
        "ISPRS Journal of Photogrammetry and Remote Sensing",
        "IEEE Geoscience and Remote Sensing Letters",
        "Remote Sensing",
        "International Journal of Remote Sensing",
    ),
    units_and_formulas_notes=(
        "空间分辨率用 m；波段用 nm 或 μm",
        "精度用 %（OA/Kappa）；误差用 RMSE",
        "公式用 amsmath；反演公式须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "坐标用投影坐标系并注明 EPSG",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("ENVI/IDL", "QGIS", "Python（Rasterio/GDAL/NumPy）", "ArcGIS Pro", "GEE（Google Earth Engine）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "Zenodo"),
)