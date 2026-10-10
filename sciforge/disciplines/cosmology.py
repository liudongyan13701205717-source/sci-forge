"""宇宙学学科论文支持：物理宇宙学/宇宙微波背景体裁、APS 引用样式与宇宙学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cosmology",
    aliases=(
        "宇宙学", "物理宇宙学", "宇宙微波背景", "Cosmology",
        "Physical Cosmology", "CMB Cosmology", "暗能量", "Dark Energy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与宇宙学问题）",
            "framework（FLRW 度规与场方程）",
            "methods（理论/观测/数值方法）",
            "results（参数约束、功率谱或演化）",
            "discussion（与观测/文献对比）",
            "conclusion",
            "references",
        ),
        "observational": (
            "abstract",
            "introduction",
            "data（巡天/卫星数据与选择函数）",
            "analysis（统计方法与系统误差）",
            "results（宇宙学参数约束）",
            "discussion（物理解释）",
            "references",
        ),
        "theoretical": (
            "abstract",
            "introduction",
            "framework（模型设定）",
            "calculations（扰动理论或数值求解）",
            "predictions（可观测预言）",
            "discussion（与现有约束对比）",
            "references",
        ),
    },
    citation_style="APS 样式（Physical Review D，REVTeX；天文期刊亦可遵循 AAS 样式）",
    reporting_standards={
        "metric_convention": "度规符号约定（-+++ 或 +---）须声明",
        "parameter_values": "宇宙学参数（H_0、\\Omega_m、\\Omega_\\Lambda 等）须注明来源与误差",
        "distance_measures": "光度距离/角直径距离定义与红移范围须给出",
        "statistical_methods": "参数估计须报告似然、先验与置信区间",
        "survey_details": "观测数据须报告巡天、红移范围与系统误差",
    },
    conventions=(
        "Hubble 常数 H_0 常用 h 参数化（H_0 = 100 h km/s/Mpc）",
        "红移 z 与尺度因子 a 的关系（1+z = 1/a）须明确",
        "\\Lambda CDM 模型为基准模型，偏离须显式声明",
        "功率谱 P(k) 与谱指数 n_s 定义须给出",
        "CMB 温度各向异性用球谐展开 a_{\\ell m} 与 C_\\ell",
    ),
    key_venues=(
        "Physical Review D",
        "Journal of Cosmology and Astroparticle Physics (JCAP)",
        "Monthly Notices of the Royal Astronomical Society",
        "Astronomy & Astrophysics",
        "The Astrophysical Journal",
        "Physical Review Letters",
    ),
    units_and_formulas_notes=(
        "距离用 Mpc/Gpc；H_0 用 km/s/Mpc；红移 z 无量纲",
        "自然单位 c=1 常用；Planck 质量与约化 Planck 质量定义须给出",
        "公式用 amsmath；张量指标与 Einstein 求和约定统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出中心值与置信区间（如 H_0 = 67.4 ± 0.5 km/s/Mpc）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("CAMB（Code for Linear Perturbation Theory）", "CLASS（Cosmic Linear Anisotropy Solving System）", "CosmoMC（宇宙学参数估计工具）", "CosmoSIS（宇宙学参数估计工具）", "CMBFast（快速 CMB 计算）", "CosmoSim（宇宙学模拟）", "Boltzmann code（Boltzmann 方程求解器）", "CosmoGridAgility（宇宙网格生成器）", "MCMCPack（MCMC 采样工具）", "CMBAnalyze（CMB 数据分析）", "Healpix（球面数据处理库）", "Ntrepid（大尺度结构模拟）", "Gadget（N 体模拟）", "AREPO（流体与引力模拟）", "RAMSES（自适应网格模拟）", "CosmoSIS（宇宙学参数估计）", "CMBPower（CMB 功率谱计算）", "Planck Cosmology（普朗克宇宙学工具）", "CosmoLib（宇宙学数值库）", "PyMC（贝叶斯推断框架）", "NumPy（数值计算）", "SciPy（科学计算）", "Astropy（天文数据工具）", "Matplotlib（科学可视化）", "LaTeX（科学排版）", "Mathematica（符号计算）", "R（统计分析）"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar", "Zenodo"),
)
