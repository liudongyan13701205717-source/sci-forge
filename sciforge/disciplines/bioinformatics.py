"""生物信息学论文支持：组学流程、基准数据集、可复现流程。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bioinformatics",
    aliases=("bioinformatics", "genomics", "transcriptomics", "omics",
             "生物信息", "组学", "测序", "pipeline"),
    paper_types={
        "research": ("abstract", "introduction", "methods（流程与参数）", "results",
                     "validation", "discussion", "code and data availability", "references"),
        "software": ("abstract", "introduction", "implementation", "availability",
                     "benchmark", "use cases", "references"),
        "database": ("abstract", "introduction", "data sources", "database design",
                     "web interface", "use cases", "references"),
    },
    citation_style="Oxford 或 Nature style",
    reporting_standards={
        "pipeline": "工具版本与参数全列出（如 STAR 2.7.x；--quantMode）；随机种子固定",
        "benchmark": "基准数据集来源与划分；评估指标（AUROC/F1/FDR）须定义",
        "reproducibility": "代码（GitHub/Zenodo DOI）+ 环境（conda/docker 镜像）+ 数据（GEO/SRA）须齐",
        "stats": "多重检验校正（BH-FDR）说明；样本量与生物学重复数报告",
        "annotation": "参考基因组版本（GRCh38/mm10）与注释来源（GENCODE 版本）",
    },
    conventions=(
        "流程图（Snakemake/Nextflow DAG）必须出现；版本锁定（workflow 锁文件）",
        "热图/火山图给阈值线与标注基因；UMAP 标注颜色映射",
        "工具名斜体或代码体；命令行参数给完整调用",
        "细胞类型注释给 marker 基因依据与参考数据集",
    ),
    key_venues=(
        "Bioinformatics",
        "Genome Biology",
        "Genome Research",
        "Nucleic Acids Research",
        "Nature Methods",
    ),
    units_and_formulas_notes=(
        "表达量单位 TPM/FPKM/counts 口径统一；差异倍数 log2FC",
        "测序深度 Gb/Mreads；质量分 Q30 比例",
    ),
)
