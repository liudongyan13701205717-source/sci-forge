"""生化与细胞生物学（Biochemistry and Cell Biology）学科论文支持：细胞分子机制、信号通路与功能基因组。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biochemistry_and_cell_biology",
    aliases=(
        "biochemistry and cell biology", "生化与细胞生物学",
        "cell biology", "细胞生物学", "molecular cell biology", "细胞分子生物学",
        "cell signaling", "细胞信号", "cellular biochemistry", "细胞生化",
        "cytoskeleton", "细胞骨架", "cell death", "细胞死亡", "细胞凋亡",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与细胞学问题）",
            "results（分子/细胞/功能发现）",
            "discussion（机理与生物学意义）",
            "materials and methods（细胞、分子、功能学方法）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按通路/分子/细胞类型综述）",
            "outlook",
            "references",
        ),
        "case_study": (
            "abstract",
            "背景（细胞系、模型、临床相关）",
            "方法",
            "结果",
            "讨论",
            "references",
        ),
    },
    citation_style="ACS 或 Nature 系列；亦可遵循 GB/T 7714",
    reporting_standards={
        "cell_line": "细胞系来源、传代次数、STR 鉴定须交代",
        "crispr": "CRISPR/Cas9 编辑须报告 gRNA 序列、克隆筛选策略",
        "antibodies": "抗体克隆号、稀释度、供应商须报告（Antibody Validation 政策）",
        "western_blot": "Western blot 原始条带须上传（多数期刊要求）",
        "reproducibility": "生物学重复≥3，含误差棒定义",
        "controls": "阴性/阳性/等量对照须设置",
    },
    conventions=(
        "细胞系名用斜体；基因名用斜体（小鼠）或正体大写（人类）",
        "蛋白名首字母大写（人类）或斜体首字母大写（小鼠）",
        "细胞实验条件（血清、生长因子、时间）须交代",
        "Western blot 条带标注分子量；内参（β-actin、GAPDH、Loading Control）须报告",
        "细胞活性/凋亡用 Annexin V/PI 双染报告，含流式门设定",
    ),
    key_venues=(
        "Cell",
        "Molecular Cell",
        "Current Biology",
        "Journal of Cell Biology",
        "Cell Reports",
        "Nature Cell Biology",
        "EMBO Journal",
    ),
    units_and_formulas_notes=(
        "浓度用 μM、nM；时间 min/h；温度 °C",
        "细胞活性用 OD490、MTT、CFU 报告",
        "信号通路报告磷酸化水平（% relative to control）",
        "公式用 amsmath；速率方程形式须明确",
        "数值结果给出均值 ± SD 与样本量 n≥3",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Nikon Ti2 倒置荧光显微镜", "Zeiss LSM 880 激光共聚焦显微镜", "Olympus IX83 共聚焦", "Leica STED 超分辨显微镜", "BD FACSCanto 流式细胞仪", "BD FACSMelody 流式分选", "Thermo QuantStudio qPCR", "Bio-Rad CFX Opus qPCR", "Thermo GeneAmp PCR", "Eppendorf Mastercycler PCR", "Bio-Rad ChemiDoc Western blot 成像", "Bio-Rad Gel Doc 凝胶成像", "Bio-Rad SpectraMax M5 酶标仪", "NanoDrop (Thermo)", "Qubit (Thermo)", "Beckman Coulter Avanti 超速离心", "Thermo Sorvall 离心机", "Cytiva ÄKTA Go 层析", "CRISPR/Cas9 试剂盒 (Thermo / NEB / Takara)", "Lenti-CRISPR 慢病毒包装系统", "Accutase 胰蛋白酶替代 (Gibco)", "TruCount 细胞计数", "Trypan Blue 死细胞检测", "CellTiter-Glo (Promega)", "Annexin V apoptosis kit (BD / Beyotime)", "Western blot 试剂 (Thermo / Cell Signaling)", "ELISA 试剂盒 (RD Systems / R&D)", "Flow cytometry 试剂 (BD / BioLegend)", "流式抗体 (eBioscience)", "R", "Python (Biopython, NumPy, SciPy)", "FlowJo", "GraphPad Prism", "ImageJ / Fiji", "Origin", "LaTeX", "EndNote", "Prism 统计", "Antibody Validation (Abcam 抗体鉴定)"),
    category="理学",
    databases=("PubMed", "Europe PMC", "OpenAlex", "Crossref", "UniProt", "Cell Line Registry", "CCLE"),
)
