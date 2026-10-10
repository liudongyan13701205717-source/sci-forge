"""其他环境科学学科论文支持：未被细类归入的环境监测、评估与生态学研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_environmental_sciences",
    aliases=(
        "other_environmental_sciences", "其他环境科学",
        "other environmental sciences", "其他环境科学",
        "environment not elsewhere classified", "环境科学未另分类",
        "environmental monitoring", "环境监测",
        "pollution assessment", "污染评估",
        "ecological modelling", "生态模型",
        "sustainability science", "可持续性科学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（环境问题与科学假说）",
            "methodology（采样、检测与建模方法）",
            "results（浓度、通量与生态效应）",
            "discussion（管理意义与不确定性）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（研究区与环境背景）",
            "analysis（时空格局与源解析）",
            "results（暴露与风险结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与方法综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="American Chemical Society (ACS)",
    reporting_standards={
        "k1": "监测须报告点位布局、频次、检出限与质控（QC）措施",
        "k2": "生态模型须报告参数来源、率度评估与情景设定",
        "k3": "风险评估须报告暴露假设、参考剂量与不确定度",
    },
    conventions=(
        "污染物浓度注明单位与是否含本底扣除",
        "时间序列须标注采样起止与缺失情况",
        "模型输入须给出空间分辨率与驱动数据年代",
        "统计检验注明方法、p 值与效应量",
        "术语使用 EPA 与 WHO 标准命名",
    ),
    key_venues=(
        "Environmental Science & Technology",
        "Environmental Pollution",
        "Ecological Indicators",
        "Science of the Total Environment",
        "Journal of Environmental Management",
        "《环境科学》",
    ),
    units_and_formulas_notes=(
        "浓度用 μg/m³ 或 mg/L 表示并注明气体/液体相态",
        "通量用 g/m²/d 表示",
        "检出限以下数据用 < LOD 标注并说明统计处理",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R (RStudio)", "Python (numpy, scipy)", "MATLAB", "ArcGIS", "QGIS", "GRASS GIS", "Google Earth Engine", "EPA SWMM", "MODFLOW", "MIKE 21", "EFSA", "AERMOD", "SCREEN 3D", "MaxEnt", "BioWin", "SPSS", "LAWA", "Zotero", "EndNote", "LaTeX"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
