"""海洋工程学科论文支持：海洋平台、结构、波浪与可再生能源体裁、SI 与 API/DNV 规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="marine_engineering",
    aliases=("marine_engineering", "海洋工程", "海洋工程与技术", "近海工程", "海洋能源工程",
             "Marine Engineering", "Ocean Engineering", "Offshore Engineering",
             "Offshore Renewable", "海洋与极地工程"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与工程挑战）",
            "methodology（建模、试验、现场验证）",
            "results（结构、动力、性能结果）",
            "discussion（工程意义与适用边界）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（平台/阵列/设施描述）",
            "analysis（荷载、响应与控制策略）",
            "results（现场与仿真对比）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（平台类型、能源与结构综述）",
            "evidence synthesis（现场与仿真证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="AIAA/ASME 样式（编号制，工程主流）",
    reporting_standards={
        "wave_and_wind_load": "波浪/风荷载须遵循 API RP 2A / ISO 19901",
        "structural_design": "结构设计与疲劳须遵循 DNV-OS-E301 / DNV-RP-C203",
        "mooring": "系泊系统设计须遵循 API RP 2SK / DNV-OS-E302",
        "wave_energy": "波浪能装置须遵循 WAMITSY/OMG 报告口径",
        "renewable": "海上风电须遵循 IEC 61400 / DNV-ST-0119",
    },
    conventions=(
        "采用 SI 单位，水深单位：m；浪高单位：m",
        "结构应力单位：MPa；力单位：kN 或 MN",
        "荷载组合须明示标准组合/极限组合与分项系数",
        "波浪与流场数据须注明站点、时段、统计窗口",
        "性能指标（AEP/WP）须注明统计基准与年份",
    ),
    key_venues=(
        "Ocean Engineering",
        "Applied Ocean Research",
        "Renewable Energy",
        "IEEE Journal of Oceanic Engineering",
        "Marine Structures",
        "Energy Conversion and Management",
    ),
    units_and_formulas_notes=(
        "波浪参数：H_s（有义波高 m）、T_e（能量周期 s）、频谱 Pierson-Moskowitz/JONSWAP",
        "Morison 方程：F = ½ ρ C_D D V|V| + ρ C_M V̇（体积加速度项）",
        "系泊载荷：F_mooring = k·Δx + c·v + F_pre（弹簧-阻尼-预张力）",
        "风电：AEP = ∫ P(v)·f(v) dv（年发电量 kWh）",
        "能量转换效率 η = E_out / E_in",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("OrcaFlex（系泊与平台）", "AQUA / WAMIT / Nemoh（水面体与频域）", "ANSYS Mechanical / ABAQUS（结构）", "SESAM（水动力）", "OpenFOAM（CFD）", "SWAN（波浪谱）", "HAWC2（风电载荷）", "FAST（整机仿真）", "MATLAB / Python（数据处理与 ML）", "Simulink（控制）", "动态荷载试件与疲劳试验台", "波浪水池与水力模型", "GNSS/RTK 位移监测", "加速度计与应变仪（HBM）", "ROV 与水下相机", "波浪浮标（Waveminder）", "海上风电整机（Vestas/Siemens Gamesa）", "浮式风电平台（半潜式/SPAR）", "海上打桩与安装船", "水下机器人（Underwater Vehicle）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "IEEE Xplore", "ScienceDirect", "CNKI"),
)
