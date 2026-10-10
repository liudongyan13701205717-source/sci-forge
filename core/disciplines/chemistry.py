"""化学学科论文支持：IUPAC 命名、反应机理与晶体数据（CIF）规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chemistry",
    aliases=(
        "chemistry", "化学", "化学学科", "化学总论",
        "organic chemistry", "无机化学", "inorganic chemistry",
        "analytical chemistry", "分析化学",
        "physical chemistry", "物理化学",
        "chemical synthesis", "化学合成", "高分子化学", "高分子",
        "electrochemistry", "电化学", "催化化学",
    ),
    paper_types={
        "communication": (
            "abstract",
            "introduction（简短动机）",
            "results and discussion（结果与机理讨论，可交叉组织）",
            "conclusion",
            "experimental section（实验部分，常入 SI）",
            "supporting information",
            "references",
        ),
        "research": (
            "abstract",
            "introduction",
            "results and discussion",
            "conclusion",
            "experimental section（合成步骤、表征方法与条件）",
            "supporting information（谱图、晶体数据、计算细节）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction（领域范围与分类框架）",
            "main developments（按反应类型/机理组织的进展）",
            "summary and outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（编号，如 [1]；期刊缩写按 CASSI）",
    reporting_standards={
        "nomenclature": "化合物命名遵循 IUPAC 命名法；俗名/商品名首次出现给 IUPAC 名",
        "crystallography": "晶体结构数据以 CIF 存档并取得 CCDC 登记号，写明空间群、R 因子与键长键角",
        "spectra": "¹H/¹³C NMR 给出 δ、溶剂、J 值与峰形；MS 给出 m/z 与电离方式；产率给分离产率",
        "safety": "涉及危险反应/试剂须给出安全注意事项与废弃物处理",
        "computation": "DFT/计算化学给出泛函、基组、软件版本与收敛判据",
    },
    conventions=(
        "化合物编号加粗（**1**、**2a**），反应式中保持一致",
        "反应机理用弯箭头表示电子转移；催化循环按步编号",
        "图表优先：TOC graphic（目录图）、反应式用 ChemDraw 导出",
        "缩写首次出现给出全称（如 DMSO、TLC）",
        "热力学/动力学数据（ΔG‡、kobs）给出单位与温度",
    ),
    key_venues=(
        "Journal of the American Chemical Society",
        "Angewandte Chemie International Edition",
        "Nature Chemistry",
        "Chemical Science",
        "Chemical Reviews",
        "Journal of Organic Chemistry",
        "Chemistry of Materials",
        "Chinese Journal of Chemistry",
    ),
    units_and_formulas_notes=(
        "浓度记作 mol·L⁻¹（或 M）；波数 cm⁻¹；化学位移 δ（ppm，相对 TMS）",
        "电位以 V vs 参比电极表示（如 vs SCE/Ag/AgCl/Fc⁺/Fc）",
        "色谱分离参数（柱型、流动相梯度、检测波长）须可复现",
        "量子产率/转化率给百分数与测定方法（内标/参比）",
        "热分析（TGA/DSC）给升温速率与气氛",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Gaussian", "ORCA", "ChemDraw", "VASP", "Gaussian View", "Multiwfn", "MOLUSPES / Avogadro", "Molekel", "MarvinSketch", "InChI Key / SMILES 处理库（RDKit）", "OriginLab", "ImageJ / Fiji（谱图处理）", "SDD 单晶衍射仪（Bruker D8）", "核磁共振波谱仪（Bruker Avance）", "质谱仪（Thermo Fisher Q Exactive）", "液相色谱-质谱联用仪（LC-MS）", "红外光谱仪（Nicolet iS50 FTIR）", "紫外-可见分光光度计（Shimadzu UV-2600）", "气相色谱仪（GCMS-QP2010）", "原子吸收光谱仪（AAS）", "电化学工作站（BioLogic VMP3）", "透射电子显微镜（TEM JEOL JEM-2100）", "扫描电子显微镜（SEM Hitachi S-4800）", "热重分析仪（TG/DSC TA Q600）", "X 射线光电子能谱仪（XPS）", "量子化学软件 Q-Chem", "分子动力学软件 LAMMPS", "分子动力学软件 GROMACS", "计算化学平台 Turbomole", "计算化学平台 CP2K", "计算化学平台 nwchem", "晶体结构精修 SHELXL", "晶体结构精修 OLEX2", "晶体结构解析 CheckCIF", "分子动力学可视化 VMD", "分子动力学可视化 PyMOL", "文献计量软件 CiteSpace", "文献管理 EndNote", "文献管理 Zotero", "绘图软件 Adobe Illustrator", "绘图软件 BioRender（结构示意）", "科学可视化 Paraview", "化学绘图 Chemfig", "化学绘图 mhchem（LaTeX）", "LaTeX 排版", "数据处理 R", "数据分析 Python（pandas）", "数据分析 MATLAB"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "ChemSpider", "SciFinder", "CNKI", "Web of Science", "化合物数据库 PubChem", "化合物数据库 ChemSpider", "化合物数据库 Reaxys", "化合物数据库 SciFinder", "化合物数据库 CCDC", "晶体结构数据库 Materials Project", "催化数据库 CatKing"),
)
