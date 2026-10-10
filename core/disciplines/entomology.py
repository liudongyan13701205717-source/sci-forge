"""昆虫学学科论文支持：昆虫分类、生态与害虫防治研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="entomology",
    aliases=(
        "entomology", "昆虫学", "昆虫",
        "insect science", "昆虫科学",
        "insect ecology", "昆虫生态",
        "pest control", "害虫防治",
        "insect taxonomy", "昆虫分类",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（昆虫问题与背景）",
            "method（研究设计、标本采集、分析方法）",
            "results（昆虫分类与生态数据）",
            "discussion（昆虫机制与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "insect analysis（昆虫分析）",
            "outcome（效果评估）",
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
        "taxonomy": "物种名称须用拉丁学名",
        "ecology": "生态数据须注明采样地点与时间",
        "control": "防治效果须注明方法与评估指标",
    },
    conventions=(
        "物种名称须用拉丁学名",
        "生态数据须注明采样地点与时间",
        "防治效果用 % 表示",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "Annual Review of Entomology",
        "Journal of Insect Science",
        "Entomologia Experimentalis et Applicata",
        "Pest Management Science",
        "Journal of Economic Entomology",
        "Insect Conservation and Diversity",
    ),
    units_and_formulas_notes=(
        "物种名称须用拉丁学名",
        "生态数据须注明采样地点与时间",
        "防治效果用 % 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R (RStudio)", "Python (pandas, numpy)", "MATLAB", "SPSS", "Excel", "Insect Collection Software", "MEGA (Molecular Evolutionary Genetics Analysis)", "GIS (ArcGIS, QGIS)", "Remote Sensing Software", "ImageJ", "Fiji", "Microscope", "Dissection Kit", "Insect Trap", "Pheromone Trap", "Light Trap", "Sweep Net", "Berlese Funnel", "Malaise Trap", "Scanning Electron Microscope"),
    category="农学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
