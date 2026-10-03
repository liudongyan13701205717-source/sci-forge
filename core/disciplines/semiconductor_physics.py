"""半导体物理学科论文支持：半导体材料/器件物理/能带体裁、APS 引用样式与半导体记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="semiconductor_physics",
    aliases=("semiconductor_physics", "半导体物理", "半导体", "能带理论",
             "半导体材料", "半导体器件物理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与半导体问题）",
            "methods（理论、实验与参数）",
            "results（能带/输运数据）",
            "discussion（机理与物理意义）",
            "references",
        ),
        "theoretical_study": (
            "abstract",
            "introduction",
            "theory（理论框架）",
            "methods（计算方法）",
            "results（计算结果）",
            "discussion（物理讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="APS 样式（作者-年份；Physical Review 系列遵循 APS 规范）",
    reporting_standards={
        "experimental": "半导体实验遵循 APS 实验报告规范",
        "theoretical": "第一性原理计算遵循 APS 计算报告规范",
        "characterization": "材料表征遵循 ASTM F 系列标准",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "simulation": "器件仿真遵循 IEEE 仿真报告规范",
    },
    conventions=(
        "材料体系与掺杂浓度须注明",
        "计算方法（DFT、GW、TB）与赝势须说明",
        "能带/态密度计算参数须报告",
        "实验温度与测量条件须明确",
        "载流子浓度/迁移率定义须一致",
    ),
    key_venues=(
        "Physical Review B",
        "Physical Review Applied",
        "Applied Physics Letters",
        "Journal of Applied Physics",
        "Physical Review Materials",
        "Semiconductor Science and Technology",
    ),
    units_and_formulas_notes=(
        "能量用 eV；浓度用 cm⁻³；迁移率用 cm²/V·s",
        "公式用 amsmath；薛定谔方程与输运方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "带隙用 eV；温度用 K",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利", "数据集"),
    tools=("Silvaco TCAD", "Vienna AB initio Simulation Package（VASP）",
           "MATLAB", "Python（NumPy/SciPy）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "万方"),
)