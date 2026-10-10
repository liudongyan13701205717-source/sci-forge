"""造船工程学科论文支持：船体设计与强度、船厂制造工艺体裁与船舶工程术语规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="shipbuilding",
    aliases=(
        "shipbuilding",
        "造船",
        "造船工程",
        "船舶工程",
        "船舶设计与制造",
        "Ship Building",
        "Ship Design",
        "Marine Engineering",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（设计/实验方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（船舶/船厂案例）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（数字编号，如 [1]、[2]）",
    reporting_standards={
        "experimental": "船模试验遵循 ITTC 水动力学试验规范",
        "numerical": "CFD/有限元分析须报告网格无关性、边界条件与求解器参数",
        "case": "船厂案例须披露设计规范、材料与检验记录",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "船型参数采用 ITTC/COT 推荐符号（LWL、T、C_B、C_M 等），首次出现给出中英对照",
        "所有量纲统一为 SI 单位；载荷与压力用 Pa/N·m 明示",
        "图表须标注试验/计算条件、比例尺与坐标原点",
        "规范引用须给出规范号与版本（如 CCS 2018 钢质海船入级规范）",
        "试验不确定度按 GUM/JCGM 100 报告，包含自由度与置信区间",
    ),
    key_venues=(
        "Ocean Engineering",
        "Journal of Ship Production and Design",
        "Marine Structures",
        "Journal of Marine Science and Technology",
        "船舶工程",
    ),
    units_and_formulas_notes=(
        "长度、面积、体积按 SI 单位（m、m²、m³）；船舶排水量用 t 或 tonne",
        "静水阻力系数 C_T = R_T / (0.5 ρ V² A)，动力系数 C_I 与摩擦系数 C_F 分层报告",
        "结构强度用许用应力 σ_allow 与局部/总纵弯曲力矩表达",
        "声学与振动报告 dB re 1 μPa、g 与 Hz 单位，注明测量点",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AVEVA Design 365", "NAPA Lines", "Maxsurf", "Fortran Designer", "TRIBON", "ANSYS Fluent", "OpenFOAM", "STAR-CCM+", "ABAQUS", "ANSYS Mechanical", "Hydrostar", "Miles/NAPA Hydro", "ShipMo", "SACS", "GIMS", "WINDO", "SolidWorks", "AutoCAD Marine", "HyperMesh", "MATLAB/Simulink"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ScienceDirect", "Scopus"),
)
