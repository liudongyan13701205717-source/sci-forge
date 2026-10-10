"""遗传学学科论文支持：分子遗传学、群体遗传学、功能基因组学与表观遗传学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="genetics",
    aliases=("genetics", "遗传学", "基因组学", "genomics", "分子遗传学", "群体遗传学", "表观遗传学", "医学遗传学"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver（编号），如 [1]",
    reporting_standards={"k1": "GWAS 须报告样本量/质控步骤/多重检验校正（GWAS 报告）", "k2": "测序须报告平台/深度/覆盖度/变异检测流程（测序报告）", "k3": "QTL 定位须报告作图群体/标记密度/LOD 阈值（QTL 报告）"},
    conventions=("基因名：人类用斜体大写（BRCA1），小鼠用斜体首字母大写（Brca1）", "变异命名用 HGVS 标准（如 c.35delG, p.Gly12Val）", "序列用 FASTA 格式；比对用标准参考基因组版本（hg38/GRCm39）", "Manhattan 图须注显著性阈值线；热图须注色标", "物种名首次出现用全称（Homo sapiens），后可用缩写（HS）"),
    key_venues=("Nature Genetics", "Genome Biology", "American Journal of Human Genetics", "PLoS Genetics", "Genetics"),
    units_and_formulas_notes=("MAF 用小数（0-0.5）", "测序深度用 ×（如 30×）", "LOD score 无量纲", "等位基因频率用 % 或小数", "连锁不平衡用 r² 或 D'（无量纲，0-1）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("PLINK（群体遗传分析）", "GATK（变异检测）", "Illumina 测序平台", "BLAST（序列比对）", "SAMTOOLS/BAM 处理工具", "R（GWAS 分析）", "Python（Pandas/Numpy）", "UK Biobank 数据平台", "GeneMANIA（基因调控网络）", "GWAS 芯片分型平台", "RNA-Seq（转录组）", "ChIP-Seq（表观遗传）", "CRISPR 基因编辑验证", "FISH 荧光原位杂交", "DNA 微阵列（基因芯片）", "Next-generation Sequencer（HiFi PacBio）", "Sanger 测序仪（毛细管电泳）", "光学显微镜（荧光显微观察）", "细胞培养与转染平台", "qPCR 仪（表达定量）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "ENSEMBL 数据库", "HapMap 数据库", "dbSNP 数据库", "GnomAD 变异数据库"),
)
