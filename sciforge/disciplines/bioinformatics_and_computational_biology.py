"""生物信息与计算生物学（Bioinformatics and Computational Biology）论文支持：算法、模型、网络与AI。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bioinformatics_and_computational_biology",
    aliases=(
        "bioinformatics and computational biology", "生物信息与计算生物学",
        "computational biology", "计算生物学", "systems biology", "系统生物学",
        "mathematical biology", "数学生物学", "quantitative biology",
        "生物网络", "biological networks", "分子动力学", "molecular dynamics",
        "深度学习生物", "deep learning biology", "AI4Science",
    ),
    paper_types={
        "research": (
            "abstract", "introduction", "methods（算法/模型/实验设计）",
            "results", "validation/benchmark", "discussion",
            "code and data availability", "references",
        ),
        "software": (
            "abstract", "introduction", "implementation", "availability",
            "benchmark", "use cases", "references",
        ),
        "method": (
            "abstract", "introduction", "method",
            "benchmark experiments", "case study", "discussion", "references",
        ),
    },
    citation_style="Oxford 或 Nature style；算法类亦可遵循 IEEE 或 ACM 样式",
    reporting_standards={
        "algorithm": "算法复杂度、参数与随机种子须报告",
        "benchmark": "基准数据集来源、划分与评估指标（AUROC/F1/AUC/MCC）须定义",
        "reproducibility": "代码（GitHub/Zenodo DOI）+ 环境（conda/docker 镜像）+ 数据须齐",
        "stats": "多重检验校正（BH-FDR）与显著性水平须说明",
        "model": "模型架构、超参数、训练细节（损失、优化器、学习率、早停）须报告",
    },
    conventions=(
        "算法/工具名首字母大写；命令行参数给完整调用",
        "流程图/架构图/DAG 必须出现；版本锁定（workflow 锁文件）",
        "热图/火山图/网络图给阈值线与标注节点",
        "网络拓扑与节点属性须定义",
        "训练/验证/测试集划分须说明",
    ),
    key_venues=(
        "Nature Computational Science",
        "Cell Systems",
        "Nature Methods",
        "Genome Biology",
        "PLOS Computational Biology",
        "BMC Bioinformatics",
        "Briefings in Bioinformatics",
        "Journal of Molecular Biology",
        "Bioinformatics",
    ),
    units_and_formulas_notes=(
        "表达量单位 TPM/FPKM/counts 口径统一；差异倍数 log2FC",
        "网络图节点/边数与度分布须报告",
        "模型精度用 AUROC/AUPRC/F1/MCC/命中率等",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("C++ / CUDA", "Julia / JuliaBio", "Python (NumPy, SciPy, pandas, scikit-learn)", "R (Bioconductor)", "PyTorch", "TensorFlow", "Keras", "scikit-bio", "NetworkX", "igraph", "Cytoscape", "STRING", "Reactome", "KEGG Mapper", "Cytoscape NetworkAnalyst", "PySB", "COPASI", "SBML", "SBOL", "Cell Designator", "BiGG Models", "OptForce", "MATLAB / SimBiology", "COMSOL Multiphysics", "GROMACS", "AMBER", "CHARMM", "NAMD", "MDAnalysis", "MDWeb", "OpenMM", "LAMMPS", "VASP", "CP2K", "GROMACS-Web", "Galaxy", "Jupyter / JupyterLab", "Docker / Singularity", "Snakemake / Nextflow", "BLAST+ / DIAMOND", "HMMER", "HETION", "CellProfiler", "Ilastik", "StarDist", "Cellpose", "LaTeX", "Git / GitHub"),
    category="理学",
    databases=("PubMed", "Ensembl", "GEO", "OpenAlex", "SRA", "ENA", "Kegg", "Reactome", "STRING"),
)
