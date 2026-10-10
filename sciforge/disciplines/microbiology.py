"""微生物学学科论文支持：微生物分类、生理与分子生物学研究体裁及实验规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="microbiology",
    aliases=("microbiology", "微生物学", "microorganism", "bacteriology", "microbial_science", "prokaryote", "microbe", "microbial", "microbiome", "microbial_genetics", "microbial_ecology"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（菌株、培养与实验方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（菌株与来源实例）", "analysis（表型与分子分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（微生物学与分类学综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 样式（微生物学常用 Microbiological Society 样式）",
    reporting_standards={
        "k1": "菌株须遵循伯杰氏手册分类规范并附保藏编号",
        "k2": "分子生物学实验遵循 MIAGE 声明",
        "k3": "基因组研究遵循 MIAGE / MINSEQE 规范",
    },
    conventions=(
        "菌株须以斜体学名加保藏编号标识（如 *Escherichia coli* K-12 ATCC 25922）",
        "培养条件（温度、时间、培养基）须说明",
        "测序数据须注明数据库（NCBI / GenBank）与登录号",
        "统计须注明检验方法与置信水平",
        "图表须标注放大倍数与标尺",
    ),
    key_venues=(
        "Microbiological Reviews",
        "Applied and Environmental Microbiology",
        "Microbes",
        "Nature Microbiology",
        "FEMS Microbiology Letters",
        "Environmental Microbiology",
    ),
    units_and_formulas_notes=(
        "菌体用 CFU/mL 或 OD600；干重以 mg 或 g 表示",
        "温度用 °C；pH 须注明缓冲体系",
        "基因大小以 bp / kb / Mb 表示",
        "相对表达量须注明内参基因与计算方法（2^-ΔΔCq）",
        "统计结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("PCR / qPCR", "Gel electrophoresis", "Microscope（光学/荧光/电镜）", "Spectrophotometer", "Sequencing (Illumina / Nanopore)", "Mass spectrometer", "Incubator", "Autoclave", "Centrifuge", "Cell viability assay", "Bioinformatics (BLAST, NCBI)", "R (统计)", "Python (pandas)", "GraphPad Prism", "ImageJ / Fiji", "Flow cytometer", "Colony counter", "Sterilization equipment", "Laminar flow hood", "Metagenomics pipeline (QIIME2 / Mothur)"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
