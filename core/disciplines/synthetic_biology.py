"""合成生物学学科论文支持：合成生物学/基因回路体裁、ACS 引用样式与合成生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="synthetic_biology",
    aliases=("synthetic_biology", "合成生物学", "基因回路", "生物工程", "synbio"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与合成生物学问题）",
            "methods（构建与表征方法）",
            "results（回路功能数据）",
            "discussion（设计原则）",
            "references",
        ),
        "design_study": (
            "abstract",
            "introduction",
            "design（回路设计与建模）",
            "construction（构建与表征）",
            "discussion（与设计对比）",
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
    citation_style="ACS 样式（作者-年份；ACS Synth Biol 遵循 ACS 规范）",
    reporting_standards={
        "design": "基因回路设计遵循 SBOL 报告规范",
        "characterization": "回路表征遵循 MIACARTA 报告规范",
        "computational": "计算模型遵循模型设定报告规范",
        "biosafety": "生物安全遵循机构审查报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "菌株与质粒编号须注明",
        "启动子/终止子等元件来源须报告",
        "表征条件（培养基、温度、时间）须明确",
        "荧光/表达单位须规范",
        "生物安全等级与合规声明须注明",
    ),
    key_venues=(
        "ACS Synthetic Biology",
        "Nature Communications",
        "Nucleic Acids Research",
        "Synthetic Biology (Oxford)",
        "Metabolic Engineering",
        "Nature Chemical Biology",
    ),
    units_and_formulas_notes=(
        "荧光用 AU；表达用蛋白/细胞；浓度用 μM",
        "公式用 amsmath；回路动力学与 Hill 方程须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与生物学重复数",
        "剂量-响应给出 EC50 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利", "数据集"),
    tools=(
        "基因设计软件（SnapGene）",
        "分子克隆与实验记录工具",
        "生物信息学流程（Python/Biopython）",
        "蛋白质结构设计工具",
    ),
    category="交叉学科",
    databases=("arXiv", "OpenAlex", "Crossref", "bioRxiv", "Ensembl"),
)