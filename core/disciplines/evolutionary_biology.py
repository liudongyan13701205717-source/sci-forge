"""进化生物学学科论文支持：系统发育/群体遗传体裁、Wiley 引用样式与进化生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="evolutionary_biology",
    aliases=("evolutionary biology", "进化生物学", "系统发育", "phylogenetics", "群体遗传学",
             "population genetics", "进化生态学", "evolutionary ecology", "分子进化", "molecular evolution"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与进化问题）",
            "materials and methods（数据与分析方法）",
            "results（系统发育/遗传数据）",
            "discussion（进化意义）",
            "references",
        ),
        "phylogenetic": (
            "abstract",
            "introduction",
            "materials and methods（序列/性状数据与建树方法）",
            "results（系统发育树与支持度）",
            "discussion（分类与进化关系）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题/类群综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Wiley 样式（作者-年份；Evolution 遵循 Wiley 规范）",
    reporting_standards={
        "data_sources": "序列/性状数据来源与 GenBank 登录号须报告",
        "phylogenetic_methods": "建树方法（ML、Bayesian）、模型与软件须完整",
        "model_selection": "替代模型选择（AIC/BIC）须报告",
        "support_values": "分支支持度（bootstrap、posterior probability）须给出",
        "reproducibility": "分析参数与软件版本须可复现",
    },
    conventions=(
        "系统发育树标注支持度与比例尺（替换/位点）",
        "分类群名称规范（学名斜体）",
        "遗传多样性指标（π、F_ST、H_e）定义须给出",
        "软件与版本（RAxML、BEAST、MrBayes）首次出现处给出全称",
        "分子钟与分化时间估计方法须说明",
    ),
    key_venues=(
        "Evolution",
        "Molecular Biology and Evolution",
        "Systematic Biology",
        "Molecular Ecology",
        "Proceedings of the Royal Society B",
        "Evolution Letters",
    ),
    units_and_formulas_notes=(
        "遗传距离用替换/位点；时间用 Myr（百万年）",
        "群体遗传参数（F_ST、π）无量纲",
        "公式用 amsmath；进化模型与似然函数须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出置信区间与支持度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "R (ape/phangorn)",
        "Python (Biopython)",
        "MEGA X",
        "RAxML / IQ-TREE",
        "BEAST",
    ),
    category="理学",
    databases=(
        "PubMed",
        "OpenAlex",
        "bioRxiv",
        "Europe PMC",
        "Zenodo",
    ),
)