"""系统生物学学科论文支持：系统生物学/组学整合体裁、APA 引用样式与系统生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="systems_biology",
    aliases=("systems_biology", "系统生物学", "组学整合", "生物网络建模", "systems biology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与系统生物学问题）",
            "methods（实验与建模方法）",
            "results（组学与模型数据）",
            "discussion（系统机理）",
            "references",
        ),
        "computational_model": (
            "abstract",
            "introduction",
            "model（模型架构与参数）",
            "simulation（仿真与验证）",
            "discussion（与实验对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Mol Syst Biol 遵循 Nature 系规范）",
    reporting_standards={
        "omics": "组学研究遵循 MIAME/MINSEQE 报告规范",
        "computational": "计算模型遵循模型设定报告规范",
        "simulation": "仿真研究遵循仿真实验报告规范",
        "network_analysis": "网络分析遵循网络研究报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "组学数据来源与处理流程须报告",
        "模型参数估计与不确定性须明确",
        "模型验证（交叉验证、独立数据）须报告",
        "通路与网络数据库版本须注明",
        "统计显著性阈值与多重检验校正须明确",
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
        "浓度用 μM/mM；表达量用 log2FC",
        "公式用 amsmath；动力学方程与 ODE 须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "多重检验校正给出 FDR/q 值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "数据集"),
    tools=(
        "Python 计算建模（COBRA Toolbox）",
        "MATLAB 动力学仿真",
        "Bioconductor 组学分析流程",
        "Flux Balance Analysis 工具",
    ),
    category="交叉学科",
    databases=("arXiv", "OpenAlex", "Crossref", "GEO", "Ensembl"),
)