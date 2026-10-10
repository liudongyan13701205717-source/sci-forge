"""Synthetic Biology 学科论文支持：合成生物学/基因回路体裁、ACS 引用样式与 SBOL/回路动力学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="synthetic_biology",
    aliases=(
        "synthetic_biology",
        "合成生物学",
        "基因回路",
        "生物工程",
        "synbio",
        "genetic circuits",
        "gene assembly",
        "DNA assembly",
        "metabolic engineering",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与合成生物学问题）",
            "methods（构建与表征方法）",
            "results（回路功能数据）",
            "discussion（设计原则与失效模式）",
            "data availability",
            "references",
        ),
        "design_study": (
            "abstract",
            "introduction",
            "design（回路设计与建模）",
            "construction（构建与表征）",
            "characterization（多参数表征）",
            "discussion（与设计对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "open problems",
            "outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；ACS Synth Biol 遵循 ACS 规范）",
    reporting_standards={
        "design": "基因回路设计遵循 SBOL（Synthetic Biology Open Language）报告规范",
        "characterization": "回路表征遵循 MIACARTA（Minimum Information About a Characterized Synthetic Gene Circuit）",
        "computational": "计算模型遵循 ModelSetting（COMSBIO/COMSYMBIOTICS）报告规范",
        "biosafety": "生物安全须报告 BSL 等级、机构审查（IACUC/IBC）与伦理批准",
        "systematic_review": "系统综述遵循 PRISMA 2020 声明",
    },
    conventions=(
        "菌株与质粒编号须注明（含宿主菌株感受态、质粒骨架、抗生素标记）",
        "启动子/终止子/RBS/编码序列等元件来源须报告并链接至 iGEM Registry 或 Addgene",
        "表征条件（培养基、温度、诱导物浓度、诱导时间）须完整列出",
        "荧光单位用 AU 且注明染料、激发/发射波长与仪器型号；表达量用 molecules/cell 或 a.u./cell",
        "生物安全等级（BSL-1/2/3）与合规声明须在材料与方法或致谢中明示",
        "基因符号遵循原核/真核命名规范（斜体、单斜杠斜线用于蛋白名）",
    ),
    key_venues=(
        "ACS Synthetic Biology",
        "Nature Communications",
        "Nucleic Acids Research",
        "Metabolic Engineering & Molecular Biology",
        "Nature Chemical Biology",
        "Cell Systems",
    ),
    units_and_formulas_notes=(
        "荧光用 AU（a.u.）；表达量用 molecules/cell 或 AU/cell；浓度用 μM、温度用 °C、诱导时间用 h 或 min",
        "回路动力学用 Hill 方程 dC/dt = V_max·[S]^n/(K_d^n + [S]^n) - k_deg·C；n 为 Hill 系数、K_d 为解离常数",
        "公式用 amsmath；ODE 系统须显式声明初值与参数；负号统一用 \\times 或斜体",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与生物学重复数 n≥3；剂量-响应给出 EC50、IC50 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SnapGene", "Benchling", "BenchDNA", "Geneious Prime", "SBOL-js", "Cell Designer", "COBRApy", "ModelSEED", "KBase", "Rosetta Design", "AlphaFold Protein Structure Database", "PyMOL", "Igor Pro", "Python (NumPy/SciPy)", "R (DESeq2)", "QIIME2", "FlowJo", "Q-PCR 定量分析软件（Cq Manager）", "ZymoResearch Gene Assembly Kit", "Agilent 2100 Bioanalyzer"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv", "bioRxiv", "Ensembl", "iGEM Registry"),
)
