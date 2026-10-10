"""海洋工程建筑学科论文支持：海洋结构与海岸工程体裁、荷载与材料规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="marine_construction",
    aliases=("marine_construction", "海洋工程建筑", "海洋建筑", "海岸工程", "近海工程建筑",
             "Marine Construction", "Offshore Construction", "Coastal Engineering",
             "Ocean Engineering Construction", "港湾与航道工程"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与工程问题）",
            "methodology（建模、试验、现场监测）",
            "results（结构响应、水动力、耐久性）",
            "discussion（工程启示与适用边界）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工程概况与施工工况）",
            "analysis（荷载、响应与控制措施）",
            "results（监测与对比）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（结构、水动力与材料综述）",
            "evidence synthesis（同类工程证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="ASCE/BibTeX 样式（编号制，工程惯例）",
    reporting_standards={
        "wave_load": "波浪荷载须遵循 API RP 2A / JIP 220 报告",
        "wind_and_seismic": "风与地震荷载须遵循 GB 50009/GB 50011 或 ASCE 7",
        "corrosion": "海工钢结构腐蚀防护须遵循 NORSOK M-501 / ISO 12944",
        "fatigue": "疲劳寿命须遵循 DNV-RP-C203 / S-N 曲线报告",
        "geotechnical": "地基与桩基须遵循 JIP 30 / GB 50007 岩土工程规范",
    },
    conventions=(
        "采用 SI 单位，水深单位：m；浪高单位：m；周期单位：s",
        "结构应力用 MPa 报告，力用 kN 报告",
        "波浪与海流数据须注明站点、观测时段与统计窗口",
        "荷载组合须明示标准组合/极限组合与分项系数",
        "施工工况须报告船位、潮汐、气象窗口",
    ),
    key_venues=(
        "Ocean Engineering",
        "Coastal Engineering",
        "Marine Structures",
        "ASCE Journal of Structural Engineering",
        "Journal of Waterway Port Coastal and Ocean Engineering",
        "Applied Ocean Research",
    ),
    units_and_formulas_notes=(
        "波浪要素：H_s（有义波高 m）、T_e（能量周期 s）、波陡 H/L",
        "Morison 方程：F(t) = ½ ρ C_D D V|V| + ρ C_M π D²/4 (dV/dt - ε V̇)",
        "抗力系数 C_D、附加质量系数 C_M 须注明取值依据",
        "应力单位：MPa；模量单位：GPa",
        "腐蚀速率单位：mm/a（毫米每年）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("OrcaFlex（水动力与系泊）", "AQUA / WAMIT（水面体时域）", "ANSYS Mechanical（有限元）", "ABAQUS（结构非线性）", "SACS（Spar/Jack-Up 分析）", "SESAM（船舶与海工）", "SWAN（波浪谱）", "MIKE21/MIKE21 FM（水动力）", "Delft3D（潮流与泥沙）", "OpenFOAM（CFD）", "MATLAB（信号处理）", "Python（数据处理与 ML）", "应力应变仪（HBM/Vishay）", "动态载荷测量（Load Pin）", "波浪浮标（WaveRider）", "GNSS 与 RTK（位移监测）", "水下声呐与 ROV（潜水员作业）", "打桩锤与沉箱工艺装备", "水下机器人（ROV / Remus）", "有限元验证试块与疲劳试验台"),
    category="工学",
    databases=("OpenAlex", "Crossref", "ASCE Library", "ScienceDirect", "CNKI"),
)
