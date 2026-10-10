"""生态学学科论文支持：种群/群落/生态系统研究体裁、生态学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ecology",
    aliases=("ecology", "生态学", "种群生态学", "群落生态学", "生态系统",
             "ecosystem ecology", "生态学研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与科学问题）",
            "study area and methods（研究区域与方法）",
            "results（数据分析与统计结果）",
            "discussion（生态机制与意义）",
            "references",
        ),
        "field_study": (
            "abstract",
            "introduction",
            "study site and methods（样地与方法）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "conceptual framework（理论框架）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "sample_size": "样本量须报告",
        "statistics": "统计方法须注明",
        "ethics": "动物实验须声明伦理审批",
    },
    conventions=(
        "物种名称须用拉丁学名",
        "群落指数（Shannon、Simpson）须定义",
        "生物量单位须统一（g/m²）",
        "统计检验须注明方法与显著性阈值",
    ),
    key_venues=(
        "Ecology",
        "Ecological Monographs",
        "Ecological Applications",
        "Journal of Ecology",
        "Oecologia",
        "Ecology Letters",
    ),
    units_and_formulas_notes=(
        "生物量用 g/m² 表示",
        "物种丰富度用 种 表示",
        "Shannon 指数 H' 用 bit 表示",
        "统计数据给出均值 ± SE",
        "p 值注明具体数值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R (RStudio)", "Python (pandas, scipy)", "MATLAB", "SPSS", "Excel", "Plant Ecology Software", "Quantitative植被分析软件", "Remote Sensing Software", "GIS (ArcGIS, QGIS)", "Bio-Rad Gel System", "PCR Machine", "Sequencer", "DNA Extraction Kit", "qRT-PCR", "Flow Cytometry", "Spectrophotometer", "Chromatography", "Electrophoresis", "ImageJ", "GraphPad Prism"),
    category="理学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
