"""核物理学科论文支持：原子核物理/核结构体裁、APS 引用样式与核物理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nuclear_physics",
    aliases=("nuclear physics", "核物理", "原子核物理", "nuclear structure",
             "核结构", "核反应", "nuclear reactions", "核天体物理", "nuclear astrophysics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与核素）",
            "theoretical framework（模型或方法）",
            "methods（实验/计算设置）",
            "results（能级、截面或衰变性质）",
            "discussion（与理论/文献对比）",
            "conclusion",
            "references",
        ),
        "experimental": (
            "abstract",
            "introduction",
            "experimental setup（束流、靶与探测器）",
            "data analysis（事例选择与效率修正）",
            "results（截面、角分布或能谱）",
            "discussion（物理解释）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "nuclear models（壳模型、集体模型等）",
            "main developments（按主题综述）",
            "open problems",
            "references",
        ),
    },
    citation_style="APS 样式（Physical Review C，作者-年份，REVTeX 模板）",
    reporting_standards={
        "nuclide_notation": "核素用标准记号 ^A_Z X 表示，注明质量数与电荷数",
        "cross_sections": "截面须注明能量、角度区间与单位（barn）",
        "decay_data": "衰变数据（半衰期、分支比、Q 值）须引用 NNDC/ENSDF 来源",
        "beam_target": "实验须报告束流能量、强度、靶厚度与纯度",
        "uncertainty": "统计与系统不确定度须分别报告",
    },
    conventions=(
        "核素记号 ^A_Z X 统一；同位素/同中子素/同量异位素术语准确",
        "能级图标注自旋-宇称 J^\\pi 与激发能",
        "截面单位 barn（1 b = 10^-24 cm^2）",
        "衰变模式（\\alpha、\\beta^\\pm、\\gamma、裂变）符号统一",
        "质量过剩与结合能定义须给出",
    ),
    key_venues=(
        "Physical Review C",
        "Nuclear Physics A",
        "Physics Letters B",
        "European Physical Journal A",
        "Journal of Physics G: Nuclear and Particle Physics",
        "Physical Review Letters",
    ),
    units_and_formulas_notes=(
        "能量用 MeV/keV；截面用 barn/mb；半衰期用 s/min/y 视量级",
        "质量单位 u（1 u ≈ 931.494 MeV/c^2）换算须给出",
        "公式用 amsmath；核子数守恒与电荷守恒在反应式中显式",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出中心值与误差，衰变数据注明参考数据库",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("ROOT", "Geant4", "Python (NumPy, SciPy)", "LaTeX"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Zenodo"),
)