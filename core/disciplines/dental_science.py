"""牙科学学科论文支持：口腔基础科学、组织学与材料学研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dental_science",
    aliases=(
        "dental_science", "牙科学", "口腔科学",
        "oral science", "oral biology", "口腔生物学",
        "oral pathology", "口腔病理学",
        "oral microbiology", "口腔微生物学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（科学问题与背景）",
            "materials and methods（实验设计与方法）",
            "results（实验数据与统计分析）",
            "discussion（机理探讨与意义）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围）",
            "main findings（主要发现）",
            "future directions（展望）",
            "references",
        ),
        "in_vitro": (
            "abstract",
            "introduction",
            "materials and methods（细胞/组织来源、培养条件、实验分组）",
            "results（细胞行为/组织变化数据）",
            "discussion",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "in_vitro": "实验条件须完整（培养液、温度、CO₂ 浓度）",
        "cell_line": "细胞系须注明来源、代数与鉴定方法",
        "statistical": "统计方法须明确（t检验、ANOVA等）",
        "ethics": "涉及动物/人体实验须声明伦理审批",
    },
    conventions=(
        "组织学切片染色方法须注明（HE、Masson、免疫组化等）",
        "细胞实验分组须注明处理因素与浓度",
        "显微镜成像须标注放大倍数与成像系统",
        "统计学分析注明软件版本与显著性阈值",
        "基因/蛋白名称遵循 HGNC 命名规范",
    ),
    key_venues=(
        "Journal of Dental Research",
        "Journal of Dental Sciences",
        "Archives of Oral Biology",
        "Journal of Oral Pathology and Microbiology",
        "Caries Research",
    ),
    units_and_formulas_notes=(
        "细胞活力用 % 表示",
        "基因表达用 fold change 表示",
        "蛋白定量用 μg/mL 或相对表达量",
        "p 值注明具体数值（p<0.05 或 p=0.xxx）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "GraphPad Prism", "R (RStudio)", "ImageJ", "Adobe Photoshop", "Flow Cytometer", "倒置显微镜", "共聚焦显微镜", "PCR 仪", "凝胶电泳系统", "酶标仪", "实时定量 PCR 系统", "细胞培养箱", "流式细胞仪", "Western Blot 系统", "qRT-PCR 分析软件", "GeneBank", "UniProt", "FlowJo 流式分析软件", "ImageLab 图像分析软件"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
