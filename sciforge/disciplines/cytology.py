"""细胞学学科论文支持：细胞生物学、细胞病理学与细胞工程研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cytology",
    aliases=(
        "cytology", "细胞学", "细胞生物学",
        "cell biology", "细胞生物学",
        "cell pathology", "细胞病理学",
        "cytopathology", "细胞病理学",
        "cellular biology", "细胞生物学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（细胞问题与背景）",
            "materials and methods（细胞培养、染色、分析方法）",
            "results（细胞形态与功能数据）",
            "discussion（细胞机制与意义）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence summary（证据总结）",
            "future directions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例描述）",
            "cytological analysis（细胞学分析）",
            "outcome（效果评估）",
            "discussion",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "cell_culture": "细胞培养条件须完整（培养基、温度、CO₂ 浓度）",
        "staining": "染色方法须注明（HE、巴氏染色等）",
        "imaging": "显微镜成像须标注放大倍数与成像系统",
        "statistics": "统计检验须注明方法与显著性水平",
    },
    conventions=(
        "细胞系须注明来源、代数与鉴定方法",
        "染色方法须注明（HE、巴氏染色等）",
        "显微镜成像须标注放大倍数与成像系统",
        "细胞计数用 个/mL 表示",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "Cytopathology",
        "Journal of Cellular Biology",
        "Cell and Tissue Research",
        "Cytometry",
        "Journal of Histochemistry and Cytochemistry",
        "Diagnostic Cytopathology",
    ),
    units_and_formulas_notes=(
        "细胞计数用 个/mL 表示",
        "染色方法须注明（HE、巴氏染色等）",
        "显微镜成像须标注放大倍数与成像系统",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ImageJ", "Fiji", "CellProfiler", "Imaris", "Amira", "MetaMorph", "Volocity", "Zeiss ZEN", "Leica LAS", "Olympus CellS", "MATLAB", "Python (scipy, numpy)", "R (RStudio)", "SPSS", "Prism", "Flow Cytometer", "PCR Machine", "Gel Electrophoresis", "Western Blot", "Confocal Microscope"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref", "EMBL-EBI"),
)
