"""遗传密码研究学科论文支持：密码子、翻译、tRNA 与翻译调控。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="genetic_code_studies",
    aliases=("genetic_code_studies", "遗传密码研究", "密码子研究", "Genetic code", "Codon usage", "mRNA translation", "tRNA biology", "翻译调控"),
    paper_types={
        "research": ("abstract", "introduction（密码子与翻译背景）", "methodology（序列分析、tRNA 表达与翻译测定）", "results（密码子偏好、翻译效率）", "discussion（机理与应用）", "references"),
        "case_study": ("abstract", "introduction", "case description（物种/基因背景）", "analysis（密码子使用与翻译）", "results（翻译效率与蛋白表达）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（遗传密码、翻译机制综述）", "evidence synthesis（不同物种/基因对比）", "future directions", "references"),
    },
    citation_style="Vancouver 样式（编号引用）或 Nucleic Acids Research 规范",
    reporting_standards={"codon": "密码子分析须报告 CDS 长度、密码子使用频率、CAI 与 tRNA 丰度", "translation": "翻译测定须报告 ribosome profiling 深度与比对方法", "tRNA": "tRNA 表达须报告 RT-qPCR 或测序深度"},
    conventions=("密码子用标准 3 字母缩写", "氨基酸用 1 字母缩写", "CDS 用编号（如 cds.1）", "翻译效率用 A/U 比", "变异命名遵循 HGVS"),
    key_venues=("Nucleic Acids Research", "Molecular Biology and Evolution", "RNA", "Nature Communications", "Cell"),
    units_and_formulas_notes=("CAI 无量纲（0-1）", "tRNA 丰度用 reads per million", "翻译速率用 codons/s", "测序深度用 ×", "翻译效率用 A/U ratio"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("CAIcalculator", "Codon Usage Analysis（CUSA）", "GCC Calculator", "tRNAscan-SE", "Infernal（tRNA 搜索）", "RiboDiff（ribosome profiling）", "RiboQuant", "RiboCode（翻译速率）", "Ribosome Profiling Pipeline", "GenomeScope", "BWA", "STAR", "GATK", "FeatureCounts", "Salmon", "kallisto", "BLAST", "ClustalOmega", "MUSCLE", "HMMER"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
