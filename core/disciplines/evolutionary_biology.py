"""进化生物学科论文支持：进化理论、系统发育与进化发育研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="evolutionary_biology",
    aliases=(
        "evolutionary_biology", "进化生物学", "进化论",
        "evolutionary biology", "进化生物学",
        "evolution", "进化",
        "phylogenetics", "系统发育",
        "evo-devo", "进化发育",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（进化问题与背景）",
            "methodology（实验设计、系统发育分析、模型）",
            "results（进化模式与机制）",
            "discussion（进化意义与展望）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "evolutionary analysis（进化分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "phylogenetics": "系统发育分析方法须注明（ML、BI 等）",
        "model": "进化模型须注明参数与假设",
        "statistics": "统计检验须注明方法与显著性水平",
    },
    conventions=(
        "物种名称须用拉丁学名",
        "进化时间用 Ma 表示",
        "系统发育树须注明支持率",
        "进化速率用 替换/位点/年 表示",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "Evolution",
        "Systematic Biology",
        "Molecular Phylogenetics and Evolution",
        "Journal of Evolutionary Biology",
        "Trends in Ecology & Evolution",
        "Nature Ecology & Evolution",
    ),
    units_and_formulas_notes=(
        "进化时间用 Ma 表示",
        "系统发育树须注明支持率",
        "进化速率用 替换/位点/年 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R (RStudio)", "Python (pandas, numpy)", "MATLAB", "SPSS", "Excel", "MEGA", "BEAST", "MrBayes", "RAxML", "PhyML", "PAUP*", "Mesquite", "FigTree", "DendroPy", "Biopython", "BLAST", "ClustalW", "MUSCLE", "MAFFT", "IQ-TREE"),
    category="理学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI"),
)
