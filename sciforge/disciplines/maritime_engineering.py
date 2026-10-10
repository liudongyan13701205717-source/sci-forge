"""船舶工程学科论文支持：船体、推进、操纵、结构与船舶系统体裁、IACS/ISO 规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="maritime_engineering",
    aliases=("maritime_engineering", "船舶工程", "船舶与海洋工程", "航海工程", "轮机工程",
             "Maritime Engineering", "Naval Architecture", "Ship Design", "船舶与航海工程",
             "船体与轮机"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与工程问题）",
            "methodology（建模、试验水池、现场验证）",
            "results（船型性能、结构、操纵结果）",
            "discussion（工程意义与适用边界）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（船舶/系统描述）",
            "analysis（性能与工况）",
            "results（实测与仿真对比）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（船型、推进、结构与系统综述）",
            "evidence synthesis（多船型证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="IACS / ASME 样式（编号制，工程主流）",
    reporting_standards={
        "hull_and_hydro": "船体与阻力须遵循 ITTC 建议报告（1957/2017）",
        "propulsion": "推进须遵循 ITTC 推进系统报告规范",
        "structure": "船体结构须遵循 IACS Common Structural Rules",
        "seaworthiness": "适航性须遵循 SOLAS/ISO 12217/IMO Code",
        "navigation": "操纵性须遵循 IMO/ITTC 操纵模型规范",
    },
    conventions=(
        "采用 SI 单位，船长单位：m（LBP/LOA）",
        "阻力单位：kN；功率单位：kW",
        "尺度无量纲化须遵循 ITTC 系列模型试验准则",
        "船型分类须给出满载/轻载吃水、载重吨 DWT",
        "海况须给出有义波高、能量周期与方向分布",
    ),
    key_venues=(
        "Ocean Engineering",
        "Journal of Ship Research",
        "International Shipbuilding Progress",
        "Applied Ocean Research",
        "Ships and Offshore Structure",
        "Journal of Marine Science and Technology",
    ),
    units_and_formulas_notes=(
        "船型参数：LBP（船长垂直柱部）、B（船宽）、T（吃水）、C_B（方形系数）",
        "阻力和/功率：R（N）、P（kW）、F_T（摩擦阻力）、R_T（总阻力）",
        "ITTC 1957 换算：C_Tm = C_TM + (C_TS - C_TSm) · νm/νs",
        "推进功率 P_E = ½ ρ n⁴ D⁵ C_P J²（推进效率 C_P）",
        "航速单位：节（kn），1 kn = 0.514 m/s",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("船型设计与 CAE（Nemeh/Simship）", "船体结构有限元（ANSYS/ABAQUS）", "船体性能仿真（SEAHORN/Maxsurf）", "船舶操纵（MOTOM/SSA）", "阻力预测（SHIP-CON/DNVA）", "推进与螺旋桨（CAP/PROP）", "水池试验设备（拖曳水池）", "模型试验（Scale Model Test）", "CFD（OpenFOAM/WindS）", "船模试验（Potentials/Potential Flow）", "船舶操纵模型（Nomoto/Maneuverability）", "船体扫描与 3D 建模（Photogrammetry）", "轮机与控制系统（Siemens/ABB）", "航行与导航（Navis Works/ENC）", "船位与 GNSS/RTK 定位", "轮机试车台（Engine Testbed）", "噪声与振动测试（ Brüel & Kjær）", "海试数据采集（Ship Trial）", "数字孪生（Digital Twin）", "仿真软件（MATLAB/Simulink）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "ScienceDirect", "CNKI", "ITTC"),
)
