"""植物生物学学科论文支持：植物发育/分子/生态/基因组学体裁、ASM/Elsevier 引用样式与植物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="plant_biology",
    aliases=("plant_biology", "植物生物学", "植物学", "botany", "植物生理学", "plant physiology", "植物分子生物学", "molecular plant biology", "植物基因组学", "plant genomics", "植物生态学", "plant ecology", "作物科学", "crop science"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与科学问题）", "materials and methods（材料、实验与测定）", "results（分子/表型数据）", "discussion（机制与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（物种/群体案例）", "analysis（表型与分子分析）", "results（关联与功能）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（按系统/机制综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ASM 样式（作者-年份；Plant Cell、Mol. Plant 遵循 Elsevier/ASM 规范）",
    reporting_standards={"nomenclature": "物种名称须遵循 ICBN 命名法", "genotype": "材料基因型（突变体、近等基因系）须报告", "experimental_protocol": "实验方案（培养条件、处理、检测）须完整", "statistics": "统计检验与生物学重复数须给出", "data_availability": "基因表达/基因组数据须给出公共库号"},
    conventions=("物种学名用斜体（属名首字母大写）", "基因符号（拟南芥大写、番茄小写斜体）遵循各物种规范", "处理条件（光、温、水、养分）须完整", "分子标记与引物序列须给出", "统计显著性标注统一"),
    key_venues=("Plant Cell", "Molecular Plant", "Plant Physiology", "Plant Journal", "Nature Plants"),
    units_and_formulas_notes=("光强 μmol m^-2 s^-1；温度 ℃", "浓度 μM、mM、mol/L", "基因表达用 FC（fold change）", "公式用 amsmath；代谢通量与遗传模型须明确"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ABI 7500", "ABI 7900 HT", "Roche LightCycler 480 II", "Bio-Rad CFX96", "QIAGEN QIAamp DNA Plant Mini Kit", "QIAGEN DNeasy Plant Mini Kit", "Thermo Fisher Plant RNA Plus", "Illumina MiSeq", "Illumina NovaSeq 6000", "Geneious Prime", "CLC Genomics Workbench", "MEGA X", "MEGA12", "NCBI BLAST", "MrBayes", "RAxML", "IQ-TREE", "Zeiss LSM 980", "Leica SP8", "R/Bioconductor"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
