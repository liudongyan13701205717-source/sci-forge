"""生物化学（Biological Chemistry）论文支持：生物有机化学、生物分析、仿生与药物化学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biological_chemistry",
    aliases=(
        "biological chemistry", "生物化学（化学方向）",
        "bio-organic chemistry", "生物有机化学",
        "bioanalytical chemistry", "生物分析化学",
        "bioconjugation", "生物偶联",
        "drug discovery", "药物发现", "药物化学",
        "bio-inspired chemistry", "仿生化学",
        "chemical biology", "化学生物学",
    ),
    paper_types={
        "research": (
            "abstract", "introduction（背景与化学/生物学问题）",
            "materials and methods（合成、表征、生物学测定）",
            "results", "discussion", "references",
        ),
        "review": (
            "abstract", "introduction",
            "main developments（按靶点/机理/方法综述）",
            "outlook", "references",
        ),
        "method": (
            "abstract", "introduction",
            "方法开发",
            "表征与验证",
            "应用",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份）",
    reporting_standards={
        "synthesis": "合成路线、试剂、溶剂、温度、时间须完整",
        "characterization": "NMR、MS、IR、单晶结构（CIF 附）须报告",
        "purity": "纯度（NMR、HPLC、MS）须报告",
        "biology_assay": "细胞/酶抑制活性（IC50、EC50）须报告",
        "kinetics": "酶动力学须报告 K_m、V_max、k_cat",
    },
    conventions=(
        "化合物名用 IUPAC 命名；编号用 R-1、R-2 等",
        "NMR 用 δ、多重峰标记（s、d、t、q、m）",
        "质谱用 m/z、分子式",
        "反应式用 ChemDraw 绘制，箭头与条件完整",
        "生物活性数据用 IC50 / EC50 / Ki 报告",
    ),
    key_venues=(
        "Journal of Organic Chemistry",
        "Journal of Medicinal Chemistry",
        "Angewandte Chemie",
        "Journal of the American Chemical Society",
        "Chemical Reviews",
        "Chemical Science",
        "ACS Catalysis",
        "Journal of Biological Chemistry",
    ),
    units_and_formulas_notes=(
        "浓度用 mmol/L、μmol/L；温度 °C",
        "酶活 U/mg 或 kcat (s^-1)",
        "NMR 频率 MHz（¹H/¹³C）",
        "公式用 amsmath；反应方程式须平衡",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ChemDraw", "MarvinSketch", "Marvin JS", "ChemOffice", "ACD/Labs", "Gaussian", "ORCA", "QM/MM 计算（Gaussian / AmberTools）", "AmberTools", "PyMOL", "ChimeraX", "UCSF Chimera", "Discovery Studio Visualizer", "AutoDock Vina", "MOE", "Schrodinger Glide", "Schrodinger Ligand Explorer", "Thermo Q Exactive (LC-MS)", "Thermo Orbitrap Exploris (LC-MS)", "Agilent 6550 Q-TOF (GC-MS)", "Waters ACQUITY UPLC (HPLC)", "Shimadzu LC-20A (HPLC)", "Agilent 1290 Infinity (HPLC)", "Cytiva ÄKTA Pure (层析)", "Cytiva AKTA Go (层析)", "Bio-Rad ChemiDoc (Western blot)", "Bio-Rad Gel Doc (凝胶成像)", "Thermo Sorvall 离心机", "Beckman Coulter Avanti (超速离心)", "NanoDrop (Thermo)", "Qubit (Thermo)", "Thermo GeneAmp PCR", "Bio-Rad CFX Opus qPCR", "BioTek Synergy 酶标仪", "SpectraMax M5 (酶标仪)", "Shimadzu UV-1800 (UV-Vis)", "Thermo Scientific NanoDrop (UV-Vis)", "Bruker 400 MHz NMR", "Bruker 600 MHz NMR", "Bruker Ascend 700 NMR", "XRD (Rigaku / Bruker)", "单晶衍射（Rigaku / Bruker）", "ImageJ / Fiji", "GraphPad Prism", "SigmaPlot", "Origin", "R", "Python (Biopython, NumPy, SciPy)", "LaTeX", "EndNote", "Zotero"),
    category="理学",
    databases=("PubMed", "Europe PMC", "OpenAlex", "Crossref", "UniProt", "GEO", "PDB", "ChEMBL"),
)
