"""化学学科总论：涵盖有机/无机/分析/物理化学/高分子化学交叉分支。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chemical_sciences",
    aliases=(
        "chemical sciences", "化学科学", "化学总论", "化学科学学",
        "chemistry science", "现代化学", "化学原理",
        "general chemistry", "基础化学",
        "chemical engineering related", "chemical research",
        "化学研究", "化学方法学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "results and discussion",
            "conclusion",
            "experimental section（合成步骤、表征方法与条件）",
            "supporting information",
            "references",
        ),
        "review": (
            "abstract",
            "introduction（领域范围与分类框架）",
            "main developments",
            "summary and outlook",
            "references",
        ),
        "communication": (
            "abstract",
            "introduction",
            "results and discussion",
            "conclusion",
            "references",
        ),
    },
    citation_style="ACS 样式（编号；期刊缩写按 CASSI）",
    reporting_standards={
        "nomenclature": "化合物命名遵循 IUPAC 命名法",
        "crystallography": "晶体结构以 CIF 存档并取得 CCDC 登记号",
        "spectra": "NMR/MS/IR 给出关键参数与谱图",
        "computation": "DFT 计算给出泛函、基组、软件版本与收敛判据",
    },
    conventions=(
        "化合物编号加粗（**1**、**2a**），反应式中保持一致",
        "反应机理用弯箭头表示电子转移",
        "缩写首次出现给出全称",
        "热力学/动力学数据给出单位与温度",
        "实验部分包含合成步骤、表征方法与条件",
    ),
    key_venues=(
        "Journal of the American Chemical Society",
        "Angewandte Chemie International Edition",
        "Nature Chemistry",
        "Chemical Science",
        "Chemical Reviews",
        "ChemPhysChem",
        "Chinese Journal of Chemistry",
        "Physical Chemistry Chemical Physics (PCCP)",
    ),
    units_and_formulas_notes=(
        "浓度 mol·L⁻¹ 或 M；波数 cm⁻¹；化学位移 δ（ppm）",
        "电位以 V vs 参比电极表示",
        "量子产率/转化率给百分数与测定方法",
        "热分析给升温速率与气氛",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Gaussian", "ORCA", "Q-Chem", "VASP", "Turbomole", "ChemDraw", "MarvinSketch", "ChemFig", "mhchem（LaTeX 化学式）", "Multiwfn", "Molekel", "Avogadro", "RDKit", "SMILES 处理库", "OriginLab", "ImageJ / Fiji", "Bruker Avance 核磁共振波谱仪", "Bruker D8 单晶衍射仪", "Thermo Fisher Q Exactive 质谱仪", "LC-MS 液相色谱-质谱联用仪", "Nicolet iS50 FTIR 红外光谱仪", "Shimadzu UV-2600 紫外可见分光光度计", "GCMS-QP2010 气相色谱-质谱", "原子吸收光谱仪 AAS", "BioLogic VMP3 电化学工作站", "JEOL JEM-2100 TEM 透射电镜", "Hitachi S-4800 SEM 扫描电镜", "TA Instruments Q600 TG/DSC", "XPS X 射线光电子能谱仪", "SHELXL 晶体结构精修", "OLEX2 晶体学软件", "CheckCIF 晶体学质量检查", "VMD 分子动力学可视化", "PyMOL 分子可视化", "LAMMPS 分子动力学", "GROMACS 分子动力学", "CP2K 第一性原理软件", "nwchem 计算化学软件", "CiteSpace 文献计量软件", "EndNote 文献管理", "Zotero 文献管理", "Adobe Illustrator", "BioRender", "Paraview 科学可视化", "LaTeX 排版", "R 数据分析", "Python（pandas/SciPy）", "MATLAB 数据处理"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "ChemSpider", "SciFinder", "CNKI", "Materials Project 材料数据库", "PubChem 化合物数据库", "ChemSpider 化合物数据库", "CCDC 晶体结构数据库", "Reaxys 化学数据库", "SciFinder 化学数据库"),
)
