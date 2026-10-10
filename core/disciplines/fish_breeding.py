"""鱼类育种学科论文支持：遗传育种、分子标记与基因组选择。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fish_breeding",
    aliases=("fish_breeding", "鱼类育种", "fish genetics", "aquatic breeding",
             "fish genomics", "遗传育种", "fish molecular markers", "分子育种",
             "fish genomic selection"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="CSE (Council of Science Editors)",
    reporting_standards={
        "genetics": "遗传参数估计须报告样本量、家系结构与模型假设",
        "sequencing": "测序数据须说明平台、覆盖度、变异检测流程与过滤标准",
        "marker": "分子标记验证须报告等位基因频率与群体遗传统计量",
    },
    conventions=(
        "遗传力用 h² 表示（取值 0-1）",
        "近交系数用 F 表示",
        "遗传多样性用 Nei 杂合度（H_e）表示",
        "有效群体大小用 N_e 表示",
        "遗传距离用 Nei's D 或 F_ST 表示",
    ),
    key_venues=(
        "Aquaculture",
        "Journal of Applied Ichthyology",
        "Marine Biotechnology",
        "Journal of Heredity",
        "水生生物学报",
    ),
    units_and_formulas_notes=(
        "遗传力 h² = σ²_a / σ²_P，取值 [0, 1]",
        "遗传距离 D = 1 - (1 + F_ST)^(-1) 或使用 Nei's D",
        "杂合度 H_e = 1 - Σ p_i²",
        "选择反应 R = h² × S，单位同表型",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Geneious Prime", "MEGA (Molecular Evolutionary Genetics Analysis)", "DNASP", "R (adegenet, hierfstat)", "PLINK", "VCFtools", "SAMtools/BWA", "GATK (Genome Analysis Toolkit)", "SPSS", "Excel", "Illumina Sequencer", "qPCR仪", "电泳仪", "PCR仪", "显微注射仪", "水质检测仪", "流式细胞仪", "MATLAB", "CRISPR-Cas9编辑", "基因芯片平台"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)