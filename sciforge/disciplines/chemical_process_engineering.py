"""化学工程过程设计学科论文支持：过程集成、过程强化与过程安全的写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chemical_process_engineering",
    aliases=(
        "chemical process engineering", "化学过程工程",
        "化工过程", "process engineering",
        "process integration", "过程集成",
        "process intensification", "过程强化",
        "process safety", "过程安全",
        "反应工程", "反应工程与传递",
        "reactor engineering", "反应器工程",
        "separation processes", "分离过程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods",
            "results and discussion",
            "conclusion",
            "references",
        ),
        "process study": (
            "abstract",
            "introduction（背景与工艺描述）",
            "process simulation（流程模拟）",
            "results",
            "economic evaluation",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "state of the art",
            "challenges and future",
            "references",
        ),
    },
    citation_style="ACS 样式（编号）",
    reporting_standards={
        "simulation": "给出物性方法、模型文件与边界条件",
        "materials": "原料/催化剂给出规格、来源、纯度",
        "reaction_conditions": "温度、压力、停留时间、进料浓度给出",
        "energy_balance": "能流/物流给出衡算表",
    },
    conventions=(
        "工艺流程图（PFD/P&ID）给出设备编号与流股编号",
        "物性方法注明（如 NRTL、UNIFAC、PC-SAFT）",
        "单位统一使用 SI，反应条件给压力（bar/kPa）与温度（K 或 ℃）",
        "催化剂/反应条件给出空速与接触时间",
        "流程图使用矢量格式",
        "催化剂给出口径、孔结构与表面积数据",
    ),
    key_venues=(
        "AIChE Journal",
        "Chemical Engineering Science",
        "Industrial & Engineering Chemistry Research",
        "Chemical Engineering and Processing",
        "Chemical Engineering Research and Design",
        "Chemical Engineering Journal",
        "Applied Catalysis A: General",
        "Separation and Purification Technology",
    ),
    units_and_formulas_notes=(
        "温度 K 或 ℃；压力 bar 或 kPa；浓度 mol·m⁻³",
        "反应速率 mol·kg_cat⁻¹·h⁻¹；转化率 X（无量纲）",
        "选择性 S、产率 Y 给百分数",
        "停留时间 τ（s 或 h）；空速 LHSV 或 WHSV（h⁻¹）",
        "传热系数 W·m⁻²·K⁻¹；压降 ΔP（kPa 或 Pa·m⁻¹）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Aspen Plus", "Aspen HYSYS", "Aspen AspenONE", "Aspen Custom Modeler", "Aspen Properties", "Aspen Reactor", "Aspen Separations", "COMSOL Multiphysics", "Ansys Fluent", "Ansys CFX", "Ansys Engineering Simulation", "OpenFOAM", "KAIKEN CFD", "CFD-Post", "ChemCAD", "ProMax", "gPROMS", "HYSYS Plus", "Plant Design System (PDS)", "Aspen Plus Dynamics", "Aspen HYSYS Process Engineering", "DWSIM", "SuperPro Designer", "SuperPro Studio", "PRO-II", "PRO-HEAT", "PRO-TAG", "MATHEWS (Metha)", "ModelBuilder (Metha)", "ChemDraw", "AutoCAD", "AutoCAD Plant 3D", "Plant Simulation (Siemens)", "Aveva PDMS", "Aveva P&ID", "Infor IIM", "Yokogawa Centum", "Honeywell Experion", "Emerson DeltaV DCS", "Siemens PCS 7 DCS", "MATLAB", "MATLAB Simulink", "Python (Pyomo, SciPy)", "SciPy", "NumPy", "OriginLab", "Mathcad", "LabVIEW", "Agilent ChemStation", "Thermo Fisher Chromeleon CDS", "Beckman Coulter FlowS", "Malvern Mastersizer", "Brookfield 粘度仪", "Anton Paar 流变仪", "Sartorius 分析天平", "Mettler Toledo 天平", "Sartorius pH 计", "Mettler Toledo pH 计", "Rigaku SmartLab XRD", "ICP-MS 电感耦合等离子体质谱", "GC 气相色谱", "HPLC 高效液相色谱", "CSTR 搅拌反应釜", "PFR 管式反应器", "fluidized bed 流化床反应器", "fixed bed 固定床反应器", "Lab Packed Column 填料柱", "distillation pilot column", "Counter-current mixer-settler 萃取设备", "Membrane: NF/RO 纳滤/反渗透", "Membrane: UF 超滤", "Membrane: MF 微滤", "Gas separation membrane 气体分离膜", "Catalyst: zeolite HZSM-5", "Catalyst: activated carbon", "Catalyst: zeolite NaA", "Catalyst: zeolite NaX", "Catalyst: ZSM-5", "Analytical: NMR spectroscopy", "Analytical: FTIR", "Analytical: DSC 差示扫描量热", "Analytical: TG 热重", "Analytical: BET (Micromeritics ASAP 2460)", "Analytical: ICP-MS", "Analytical: XPS 表面分析", "Statistical: Minitab", "Statistical: JMP", "Statistical: SAS", "Statistical: SPSS", "Python (pyDOE2)", "LaTeX 排版", "Zotero 文献管理", "EndNote 文献管理", "GraphPad Prism 绘图", "Adobe Illustrator"),
    category="工学",
    databases=("Crossref", "OpenAlex", "Web of Science", "Scopus", "CNKI", "Aspen Properties"),
)
