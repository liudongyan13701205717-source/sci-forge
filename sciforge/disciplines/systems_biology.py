"""Systems Biology 学科论文支持：系统生物学/组学整合体裁、Nature/ACS 引用样式与系统动力学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="systems_biology",
    aliases=(
        "systems_biology",
        "系统生物学",
        "组学整合",
        "生物网络建模",
        "systems biology",
        "multi-omics",
        "flux balance analysis",
        "ODE modeling",
        "network biology",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与系统生物学问题）",
            "methods（实验与建模方法）",
            "results（组学与模型数据）",
            "discussion（系统机理与涌现行为）",
            "data availability",
            "references",
        ),
        "computational_model": (
            "abstract",
            "introduction",
            "model（架构、方程、参数与初值）",
            "simulation（仿真、验证与灵敏度分析）",
            "discussion（与实验数据的对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "challenges and outlook",
            "references",
        ),
    },
    citation_style="Nature 系样式（Cell Systems 遵循 Nature 规范；Mol Syst Biol 遵循 Nature/EMBO Press 规范）",
    reporting_standards={
        "omics": "组学研究遵循 MIAME（转录组）、MINSEQE（单细胞）、MIVIA（蛋白组）、GEXPS（GEO）报告规范",
        "computational": "计算模型遵循 COMBINE ModelSetting 与 SBML Level 2/3 报告规范",
        "simulation": "仿真研究遵循 COSMOS/COSI 仿真报告与可复现性声明",
        "network_analysis": "网络分析须报告节点/边数、加权方式、聚类系数、模块度与显著性阈值",
        "systematic_review": "系统综述遵循 PRISMA 2020 声明",
    },
    conventions=(
        "组学数据来源、测序平台、测序深度与批次效应处理流程须完整报告",
        "模型参数估计方法（MCMC、SLSQP、网格搜索）、初值设定与不确定性须明确",
        "模型验证须包含交叉验证与独立数据集（时间、物种、扰动），并给出 R²、RMSE、AIC/BIC",
        "通路/网络数据库版本（KEGG、Reactome、STRING、BioCyc）须注明抓取日期",
        "统计显著性阈值与多重检验校正（BH-FDR、Bonferroni）须明确；FDR<0.05 为常见阈值",
        "SBML/CellML/CellDesigner 模型文件须作为 supplementary 提交",
    ),
    key_venues=(
        "Molecular Systems Biology",
        "Cell Systems",
        "PLOS Computational Biology",
        "BMC Systems Biology",
        "npj Systems Biology and Applications",
        "Bioinformatics",
    ),
    units_and_formulas_notes=(
        "浓度用 μM/mM、丰度用 log2FC、细胞计数用 cells/mL；时间尺度须明确（s、min、h）",
        "ODE 系统须显式声明：dx/dt = f(x, θ, t)；参数 θ 用希腊字母（α, β, k, k_d, k_a），Hill 方程 n 为 Hill 系数",
        "公式用 amsmath；负反馈用 -、正反馈用 +；抑制用 -k·x^n/(K_d^n + x^n)，激活用 +k·x^n/(K_d^n + x^n)",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式；ODE 系统按 \\begin{aligned} 对齐",
        "数值结果给出均值 ± SD 与样本量 n；多重检验校正给出 FDR/q 值；模型拟合给出 R²、RMSE、AIC/BIC",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("COBRApy", "MATLAB (OptiModel)", "PySB", "COPASI", "Bioconductor", "Seurat", "scanpy", "Cell Ranger", "NetworkX", "Cytoscape", "Cytoscape Cytoscape.js", "PyMC", "SUNDIALS (CVODES/IDAS)", "AMICI", "Dynamo", "scVelo", "R (limma/DESeq2)", "Galaxy Workbench", "Jupyter Notebook", "Docker / Singularity"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv", "bioRxiv", "GEO", "KEGG", "STRING"),
)
