"""无机化学学科论文支持：配位化学/固体无机体裁、ACS 引用样式与无机化学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="inorganic_chemistry",
    aliases=("inorganic chemistry", "无机化学", "配位化学", "coordination chemistry",
             "金属有机", "organometallic", "固体化学", "solid state chemistry"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与目标化合物）",
            "results and discussion（合成、结构与性质）",
            "conclusion",
            "experimental section（合成细节与表征）",
            "references",
        ),
        "structural": (
            "abstract",
            "introduction",
            "synthesis（晶体生长与合成）",
            "crystal structure（晶体学数据与结构描述）",
            "properties（磁性、光学或电学性质）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按配体/金属/结构类型综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；晶体学数据引用 CCDC 编号）",
    reporting_standards={
        "crystallography": "单晶结构须报告 R 因子、CCDC 编号与键长键角精度",
        "characterization": "新化合物须提供元素分析、IR、UV-vis 等表征",
        "magnetic_data": "磁性数据须报告测量温度范围与拟合参数",
        "synthesis_conditions": "合成条件（惰性气氛、溶剂、温度）须完整",
        "oxidation_states": "金属氧化态与电子构型须明确",
    },
    conventions=(
        "配位几何用标准术语（八面体、四面体、平面四方等）",
        "晶体结构描述给出空间群与晶胞参数",
        "d 电子构型与自旋态（高自旋/低自旋）标注",
        "磁性用 \\chi T 或 \\mu_eff 表示，注明温度",
        "配体缩写首次出现处给出全称",
    ),
    key_venues=(
        "Inorganic Chemistry",
        "Journal of the American Chemical Society",
        "Angewandte Chemie International Edition",
        "Dalton Transactions",
        "Chemical Communications",
        "Chemistry of Materials",
    ),
    units_and_formulas_notes=(
        "键长用 Å，键角用 °；磁矩用 \\mu_B",
        "晶体学数据遵循 IUCr 标准（CIF 文件）",
        "公式用 amsmath；配位化合物化学式用方括号规范",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出精度与误差（如键长 2.045(3) Å）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("ChemDraw", "Origin", "Python (NumPy/SciPy)", "VESTA", "LaTeX"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "Semantic Scholar", "CNKI"),
)