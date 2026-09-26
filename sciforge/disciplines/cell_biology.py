"""细胞生物学学科论文支持：细胞机制/细胞成像体裁、Cell Press 引用样式与细胞生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cell_biology",
    aliases=("cell biology", "细胞生物学", "细胞信号", "cell signaling", "细胞周期",
             "cell cycle", "细胞成像", "cell imaging", "细胞器", "organelles"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与细胞过程）",
            "results（实验发现与数据）",
            "discussion（机制与意义）",
            "materials and methods（细胞系、试剂与测定）",
            "references",
        ),
        "imaging": (
            "abstract",
            "introduction",
            "results（成像数据与定量）",
            "discussion（动态过程解释）",
            "materials and methods（显微镜与图像分析）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按通路/过程综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Cell Press 样式（作者-年份；Cell 遵循 Cell Press 规范）",
    reporting_standards={
        "cell_lines": "细胞系来源（ATCC 等）与培养条件须报告",
        "reagent_details": "抗体、抑制剂与试剂（克隆号、浓度）须完整",
        "imaging_parameters": "显微镜类型、物镜、荧光通道与图像处理须报告",
        "quantification": "图像定量方法与统计须给出",
        "replicates": "独立实验重复次数须报告",
    },
    conventions=(
        "细胞系名称规范（HeLa、HEK293T）",
        "蛋白名称用标准符号（p53、ERK1/2）",
        "荧光标记缩写（GFP、mCherry）首次出现处给出全称",
        "显微镜缩写（confocal、SIM、STED）给出定义",
        "统计显著性标注（*p<0.05, **p<0.01）统一",
    ),
    key_venues=(
        "Cell",
        "Journal of Cell Biology",
        "Molecular Biology of the Cell",
        "Nature Cell Biology",
        "EMBO Journal",
        "Journal of Cell Science",
    ),
    units_and_formulas_notes=(
        "浓度用 mol/L、μmol/L；时间用 min/h",
        "图像尺度用 μm；分辨率用 nm",
        "公式用 amsmath；定量指标（FRAP、FRET）公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "激光共聚焦显微镜",
        "ImageJ / Fiji",
        "流式细胞仪",
        "超分辨显微镜（STED/SIM）",
        "CRISPR 基因编辑",
    ),
    category="理学",
    databases=(
        "PubMed",
        "OpenAlex",
        "bioRxiv",
        "RCSB PDB",
        "Human Protein Atlas",
    ),
)