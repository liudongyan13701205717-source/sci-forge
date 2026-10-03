"""遗传学论文支持：分子遗传学、群体遗传学、功能基因组学、表观遗传学、医学遗传学。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="genetics",
    aliases=("genetics", "遗传学", "基因组学", "genomics"),
    paper_types={
        "research": ("abstract", "introduction", "materials and methods", "results", "discussion", "conclusions", "references"),
        "gwas": ("abstract", "introduction", "cohort", "genotyping/imputation", "association analysis", "results", "discussion", "conclusions", "references"),
        "functional": ("abstract", "introduction", "gene description", "experimental approach", "results", "functional interpretation", "discussion", "conclusions", "references"),
    },
    citation_style="Vancouver（编号），如 [1]；或 Genetics/Genome Biology 风格",
    reporting_standards={
        "gwas": "GWAS 须报告样本量、基因型质控步骤、MAF 阈值、群体分层校正与多重检验校正方法",
        "sequencing": "测序须报告平台、测序深度、覆盖度、比对/变异检测流程与版本",
        "qtl": "QTL 定位须报告作图群体、标记密度、LOD 阈值（permutation）与置信区间",
        "gene_editing": "基因编辑须报告 sgRNA 序列、脱靶分析与验证方法",
    },
    conventions=(
        "基因名：人类用斜体大写（BRCA1），小鼠用斜体首字母大写（Brca1）",
        "变异命名用 HGVS 标准（如 c.35delG, p.Gly12Val）",
        "序列用 FASTA 格式；比对用标准参考基因组版本（hg38/GRCm39）",
        "图：Manhattan 图须注显著性阈值线；热图须注色标",
        "物种名首次出现用全称（Homo sapiens），后可用缩写（HS）",
    ),
    key_venues=(
        "Nature Genetics",
        "Genome Biology",
        "American Journal of Human Genetics",
        "PLoS Genetics",
        "Genetics",
    ),
    units_and_formulas_notes=(
        "MAF 用小数（0-0.5）",
        "测序深度用 ×（如 30×）",
        "LOD score 无量纲",
        "等位基因频率用 % 或小数",
        "连锁不平衡用 r² 或 D'（无量纲，0-1）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("BLAST", "PLINK", "测序仪", "PCR 仪"),
    category="理学",
    databases=("PubMed", "Europe PMC", "Ensembl", "ClinVar"),
)
