"""发育生物学学科论文支持：胚胎发育/模式形成体裁、Wiley 引用样式与发育生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="developmental_biology",
    aliases=("developmental biology", "发育生物学", "胚胎学", "embryology", "模式形成",
             "pattern formation", "形态发生", "morphogenesis", "干细胞分化", "stem cell differentiation"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与发育过程）",
            "results（实验发现与数据）",
            "discussion（机制与意义）",
            "materials and methods（模式生物与实验）",
            "references",
        ),
        "genetic": (
            "abstract",
            "introduction",
            "results（突变表型与基因功能）",
            "discussion（调控网络）",
            "materials and methods（遗传操作）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按过程/机制综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Wiley 样式（作者-年份；Development 遵循 Company of Biologists 规范）",
    reporting_standards={
        "model_organism": "模式生物（物种、品系、发育阶段）须报告",
        "staging": "发育分期标准（somite、Theiler、Hamburger-Hamilton）须注明",
        "genetic_manipulation": "遗传操作（敲除、敲低、过表达）方法须完整",
        "imaging": "活体/固定成像条件与时间点须报告",
        "replicates": "胚胎/个体数量与重复次数须报告",
    },
    conventions=(
        "发育阶段用标准分期系统并注明",
        "基因名与突变等位基因符号规范（如 Wnt3a^-/-）",
        "形态测量与模式定量方法须给出",
        "原位杂交与免疫染色缩写（ISH、IHC）给出定义",
        "谱系追踪标记（Cre-loxP）首次出现处给出全称",
    ),
    key_venues=(
        "Development",
        "Developmental Cell",
        "Developmental Biology",
        "Nature Cell Biology",
        "Current Biology",
        "eLife",
    ),
    units_and_formulas_notes=(
        "时间用 hpf/dpf（受精后小时/天）",
        "浓度用 ng/μL、μmol/L",
        "公式用 amsmath；形态发生与梯度模型公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "激光共聚焦显微镜",
        "原位杂交（ISH）",
        "ImageJ / Fiji",
        "CRISPR/Cas9 基因编辑",
        "活体成像系统",
    ),
    category="理学",
    databases=(
        "PubMed",
        "OpenAlex",
        "bioRxiv",
        "GEO",
        "Zenodo",
    ),
)