"""生物化学学科论文支持：酶学/分子生物学体裁、ACS 引用样式与生化记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biochemistry",
    aliases=("biochemistry", "生物化学", "酶学", "enzymology", "蛋白质化学",
             "protein chemistry", "代谢", "metabolism", "分子生物学", "molecular biology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与生物分子体系）",
            "results（实验发现与数据）",
            "discussion（机理与意义）",
            "materials and methods（材料与方法）",
            "references",
        ),
        "enzymology": (
            "abstract",
            "introduction",
            "results（动力学、抑制与结构）",
            "discussion（催化机理）",
            "materials and methods（酶制备与测定）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按通路/分子综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；J. Biol. Chem. 亦可遵循其期刊样式）",
    reporting_standards={
        "kinetic_parameters": "酶动力学须报告 K_m、V_max、k_cat 与拟合方法",
        "protein_characterization": "蛋白质纯度（SDS-PAGE）、浓度（BCA/Bradford）与序列须报告",
        "replicates": "生物学重复与技术重复次数须报告，误差棒定义明确",
        "statistics": "统计检验（t 检验、ANOVA）与显著性水平须给出",
        "reagent_details": "试剂、缓冲液与供应商信息须完整",
    },
    conventions=(
        "酶命名遵循 IUBMB 命名法，给出 EC 编号",
        "蛋白质序列用单字母氨基酸代码；突变标注（如 S473A）",
        "动力学参数符号（K_m、V_max、k_cat）统一",
        "缓冲液与 pH 标注；温度与时间条件完整",
        "凝胶电泳与印迹图标注分子量标准",
    ),
    key_venues=(
        "Journal of Biological Chemistry",
        "Biochemistry",
        "Journal of Molecular Biology",
        "Nature Chemical Biology",
        "Cell Chemical Biology",
        "FEBS Journal",
    ),
    units_and_formulas_notes=(
        "浓度用 mol/L、mmol/L、μmol/L；酶活用 U/mg 或 kcat (s^-1)",
        "蛋白质浓度用 mg/mL 或 μM（注明分子量）",
        "公式用 amsmath；Michaelis-Menten 方程形式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集", "专利"),
    tools=("Python (Biopython/NumPy/SciPy)", "R", "Origin", "PyMOL", "LaTeX"),
    category="理学",
    databases=("PubMed", "Europe PMC", "OpenAlex", "Crossref", "UniProt", "GEO"),
)