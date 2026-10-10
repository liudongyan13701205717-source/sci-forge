"""分子生物学学科论文支持：基因表达/分子克隆体裁、Cell Press 引用样式与分子生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="molecular_biology",
    aliases=(
        "molecular_biology", "分子生物学", "基因表达", "gene expression",
        "分子克隆", "molecular cloning", "转录调控", "transcriptional regulation", "表观遗传"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与分子机制）",
            "results（实验发现与数据）",
            "discussion（机制与意义）",
            "materials and methods（克隆、转染与测定）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（分子生物学案例）",
            "analysis（分子机制分析）",
            "results（分子数据与验证）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（分子机制理论）",
            "evidence synthesis（调控机制综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="Cell Press 样式（作者-年份；Mol. Cell 遵循 Cell Press 规范）",
    reporting_standards={
        "construct_details": "质粒构建（载体、插入片段、酶切位点）须完整",
        "primer_sequences": "引物序列与退火温度须报告",
        "assay_conditions": "qPCR、Western blot 等测定条件须完整",
    },
    conventions=(
        "基因名用斜体（TP53），蛋白名用正体（p53）",
        "引物序列 5'→3' 方向标注",
        "qPCR 数据用 2^-ΔΔCt 法，内参基因注明",
        "Western blot 标注分子量标准与抗体稀释",
        "载体缩写（pCDNA3.1、pLKO.1）首次出现处给出全称",
    ),
    key_venues=(
        "Molecular Cell",
        "Nucleic Acids Research",
        "Genes & Development",
        "EMBO Journal",
        "Nature Structural & Molecular Biology",
    ),
    units_and_formulas_notes=(
        "浓度用 ng/μL、nmol/L；时间用 min/h",
        "温度用 °C（退火、延伸温度）",
        "公式用 amsmath；ΔΔCt 与相对表达量公式须明确",
        "数值结果给出均值 ± SD/SEM 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("PCR 仪", "毛细管电泳仪", "BLAST", "Python (Biopython)", "Western blot 成像系统", "高通量测序仪 Illumina", "qPCR 仪", "凝胶成像系统", "细胞培养设备", "流式细胞仪", "CRISPR-Cas9", "RNA-seq 分析软件 STAR", "HISAT2", "DESeq2", "R (bioconductor)", "Cytoscape", "GeneMANIA", "Uniprot", "AlphaFold2", "PyMOL"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
