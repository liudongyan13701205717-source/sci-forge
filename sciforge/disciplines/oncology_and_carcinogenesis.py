"""肿瘤发生学学科论文支持：癌变机制与肿瘤发生基础。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="oncology_and_carcinogenesis",
    aliases=("oncology_and_carcinogenesis", "肿瘤发生学", "癌变学", "Carcinogenesis", "Tumorigenesis", "肿瘤发生机制", "Cancer Biology", "Oncogenesis"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "细胞与动物实验报告", "k2": "分子生物学实验规范", "k3": "转化医学研究要求"},
    conventions=("基因/蛋白命名遵循人类基因命名规则", "细胞株鉴定采用STR分型", "肿瘤异质性描述", "通路图标注"),
    key_venues=("Cancer Cell", "Nature Cancer", "Molecular Cancer", "Carcinogenesis", "Cell"),
    units_and_formulas_notes=("细胞增殖用倍增时间h/d", "蛋白表达以相对定量", "突变频率以%", "肿瘤负荷以体积或计数"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (DESeq2)", "GraphPad Prism", "Bioinformatics (Galaxy)", "Sequencing (Illumina NovaSeq)", "RT-qPCR (ABI 7500)", "Western Blot (Bio-Rad)", "Flow Cytometer", "Confocal Microscope", "Proteomics (LC-MS/MS)", "TMA Analysis", "CRISPR (Cas9)", "Cell Proliferation Assay", "Python", "ImageJ", "EndNote", "Zotero", "Cytogenetics", "Animal Model (MDX Mouse)", "Pathology Scanner"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
