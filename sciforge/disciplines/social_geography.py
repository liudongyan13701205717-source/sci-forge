"""社会地理学学科论文支持：城市/区域/乡村空间体裁、APA 引用样式与空间统计规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_geography",
    aliases=("social_geography", "社会地理学", "人文地理", "人文与社科地理", "human geography", "urban geography", "regional studies", "spatial dynamics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与空间理论）",
            "methods（数据、尺度、模型、验证）",
            "results（结果与空间模式）",
            "discussion（讨论与尺度效应）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（研究区、尺度与语境）",
            "analysis（空间过程与机制）",
            "results",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（人文地理学理论综述）",
            "evidence synthesis（跨案例证据综合）",
            "future directions",
            "references"
        )
    },
    citation_style="APA 7（Progress in Human Geography、Area 遵循 APA；Geographical Review 遵循 Chicago）",
    reporting_standards={
        "quantitative": "空间分析须报告数据来源、空间单元（AOI）、尺度选择与尺度效应；空间权重矩阵（距离/邻接）透明",
        "qualitative": "质性地理研究遵循 COREQ 清单：田野点、访谈、地图叙事、反思性",
        "mixed_methods": "混合设计用联合展示表整合定量空间模式与定性叙事",
        "governance": "涉及人口敏感数据的空间单元须说明匿名化与空间聚合策略（避免小样本反推）"
    },
    conventions=(
        "空间单元（AOI）选择须报告：行政边界、网格、缓冲区、等值区域，并讨论尺度效应",
        "空间权重矩阵（W）报告类型（k-近邻、距离阈值、邻接）、标准化方式与稀疏度",
        "空间自相关用 Moran's I、Geary's C；局部用 LISA 与 Getis-Ord G*",
        "地图投影与坐标系统一声明（如 EPSG:4326 / CGCS2000）；制图符号遵循 Töpfer 化简原则",
        "定量表格三线制；类别变量给频数与百分比（注明基数 N）"
    ),
    key_venues=(
        "Annals of the Association of American Geographers",
        "Area",
        "Progress in Human Geography",
        "Environment and Planning A",
        "Geographical Review"
    ),
    units_and_formulas_notes=(
        "Moran's I = (n/S₀)·ΣΣ w_ij(x_i - x̄)(x_j - x̄) / Σ(x_i - x̄)²；报告 z 值与 p 值",
        "LISA 聚类用 Getis-Ord Gi*，报告显著性（95%/99%）与 Moran 象限（HH/LL/HL/LH）",
        "距离单位（米/公里）须声明；缓冲区半径给出选择依据",
        "百分比给出基数 N；加权数据注明权重变量与空间单元"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS Pro", "QGIS", "GRASS GIS", "SAGA GIS", "R", "RStudio", "Python", "PostGIS", "PDAL", "FME", "GMT", "Google Earth Pro", "DroneDeploy", "Pix4D", "SketchUp", "Tableau", "Power BI", "SPSS", "Stata", "NVivo"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
