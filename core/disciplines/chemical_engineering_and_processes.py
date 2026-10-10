"""化学工程与工艺学科论文支持：反应器/分离/过程控制与流程优化的写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chemical_engineering_and_processes",
    aliases=(
        "chemical engineering and processes", "化学工程与工艺",
        "化学工程", "化工工艺", "process engineering",
        "chemical process engineering", "化学工艺流程",
        "reaction engineering", "反应工程",
        "separation engineering", "分离工程",
        "process design", "过程设计",
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
        "process case study": (
            "abstract",
            "introduction（背景与工艺描述）",
            "process design（流程设计与物料衡算）",
            "simulation（流程模拟）",
            "results（模拟/实验结果）",
            "optimization（优化）",
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
    citation_style="ACS 样式（编号）或 Elsevier（编号）",
    reporting_standards={
        "materials": "原料/催化剂给出规格、来源、纯度",
        "reaction_conditions": "温度、压力、停留时间、进料浓度给出",
        "simulation": "给出物性方法、模型文件与边界条件",
        "energy_balance": "能流/物流给出衡算表",
    },
    conventions=(
        "工艺流程图（PFD/P&ID）给出设备编号与流股编号",
        "物性方法注明（如 NRTL、UNIFAC、PC-SAFT）",
        "衡算表按稳态/非稳态标注",
        "单位统一使用 SI，反应条件给压力（bar/kPa）与温度（K 或 ℃）",
        "催化剂/反应条件给出空速（LHSV/WHSV）与接触时间",
        "流程图与图表使用矢量格式（EPS/SVG/PDF）",
    ),
    key_venues=(
        "AIChE Journal",
        "Chemical Engineering Science",
        "Industrial & Engineering Chemistry Research (I&EC Research)",
        "Chemical Engineering Research and Design (ChERD)",
        "Computers & Chemical Engineering",
        "Chemical Engineering Journal",
        "Processes (MDPI)",
        "化工学报 (The Chinese Journal of Chemical Engineering)",
    ),
    units_and_formulas_notes=(
        "温度 K 或 ℃；压力 bar 或 kPa；浓度 mol·m⁻³ 或 kmol·kmol⁻¹",
        "反应速率 mol·kg_cat⁻¹·h⁻¹；转化率 X（无量纲）",
        "选择性 S、产率 Y 给出百分数",
        "停留时间 τ（s 或 h）；空速 LHSV 或 WHSV（h⁻¹）",
        "传热系数 W·m⁻²·K⁻¹；压降 ΔP（kPa 或 Pa·m⁻¹）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Aspen Plus", "Aspen HYSYS", "Aspen AspenONE", "Aspen Custom Modeler", "Aspen Properties", "Aspen Reactor", "Aspen Separations", "COMSOL Multiphysics", "Ansys Fluent", "Ansys CFX", "Ansys Multiphysics", "OpenFOAM", "KAIKEN CFD", "CFD-Post", "ChemCAD", "ProMax", "gPROMS", "HYSYS Plus", "Plant Design System (PDS)", "Aspen Plus Dynamics", "Aspen HYSYS Process Engineering", "DWSIM", "SuperPro Designer", "SuperPro Studio", "SuperPro Studio Process Simulation", "PRO-II", "PRO-HEAT", "PRO-TAG", "PRO-MATHEWS", "MATHEWS (Metha)", "ModelBuilder (Metha)", "Process Modeller", "MatSim", "Chemical Engineering Design Tool (CEDT)", "ChemDraw", "AutoCAD", "AutoCAD Plant 3D", "Plant Simulation by Siemens", "WorleySpark", "Aveva PDMS (Plant Design Management System)", "Aveva P&ID", "Infor IIM", "Yokogawa Centum", "Honeywell Experion", "Emerson DeltaV DCS", "Siemens PCS 7 DCS", "MATLAB", "MATLAB Simulink", "Python (Pyomo, SciPy)", "Python (PyDAE, Pyomo)", "Python (PyAnsys)", "SciPy", "NumPy", "OriginLab", "Mathcad", "LabVIEW", "Agilent ChemStation", "Thermo Fisher Chromeleon CDS", "Beckman Coulter FlowS", "Malvern Mastersizer (粒度仪)", "Brookfield viscometer (粘度仪)", "Anton Paar rheometer", "Sartorius analytical balance (分析天平)", "Mettler Toledo 天平", "Sartorius pH meter", "梅特勒-托利多 pH 计", "XRD 粉末衍射仪 (Rigaku SmartLab)", "ICP-OES 电感耦合等离子体质谱", "GC 气相色谱", "HPLC 高效液相色谱", "Furnace 反应釜/流化床", "Reactor: CSTR 搅拌反应釜", "Reactor: PFR 管式反应器", "Reactor: fluidized bed 流化床反应器", "Reactor: fixed bed 固定床反应器", "Lab Packed Column 填料柱", "Column: structured packing (规整填料)", "Column: random packing (散装填料)", "Drying: fluid bed dryer", "Distillation: pilot scale column", "Extraction: counter-current mixer-settler", "Membrane: NF/RO 纳滤/反渗透", "Membrane: UF 超滤", "Membrane: MF 微滤", "Membrane: gas separation membrane", "Catalyst: zeolite (分子筛)", "Catalyst: zeolite HZSM-5", "Catalyst: activated carbon (活性炭)", "Catalyst: zeolite NaA", "Catalyst: zeolite NaX", "Catalyst: zeolite ZSM-5", "Analytical: NMR spectroscopy", "Analytical: FTIR", "Analytical: DSC 差示扫描量热", "Analytical: TG 热重", "Analytical: BET 比表面 (Micromeritics ASAP 2460)", "Analytical: mercury porosimetry", "Analytical: ICP-MS", "Analytical: XPS 表面分析", "Optimization: CiteSpace", "Optimization: MATLAB Optimize", "Optimization: Python (OptiMo)", "Optimization: Python (pyDOE2)", "Statistical: Minitab", "Statistical: JMP", "Statistical: SAS", "Statistical: SPSS", "LaTeX 排版", "Zotero 文献管理", "EndNote 文献管理", "Matlab toolbox: HYSYS-Matlab", "GraphPad Prism 绘图", "Adobe Illustrator"),
    category="工学",
    databases=("Crossref", "OpenAlex", "Web of Science", "Scopus", "CNKI", "Aspen Properties"),
)
