"""公交与教练车驾驶：客运安全行车技术、驾驶行为与运输组织研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bus_and_coach_driving",
    aliases=("Bus and coach driving", "公交客车驾驶", "公交驾驶", "coach driving",
             "客运驾驶", "road transport safety", "道路运输安全", "public transport driving"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与研究缺口）",
            "literature review（既有研究与理论脉络）",
            "methodology（数据来源、抽样与分析方法）",
            "results",
            "discussion（与既有研究对话）",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7th（交通科学系）",
    reporting_standards={
        "accident_data": "事故数据给来源（数据库、时间窗口、覆盖区域）与判定口径",
        "simulation": "驾驶行为仿真给模型版本、参数取值与敏感性说明",
        "field_data": "车载数据（速度、加速度、制动）给采样频率与缺失值处理",
        "safety_metrics": "安全指标（事故率、暴露量）统一口径并标注单位",
    },
    conventions=(
        "安全结果区分致死/重伤/轻伤等级；暴露量（行驶里程）与时间窗口一致",
        "单位制统一 SI；速度 km/h、距离 m、质量 t",
        "驾驶员特征（驾龄、培训）在方法部分交代；统计方法给显著性水平",
    ),
    key_venues=(
        "Accident Analysis & Prevention",
        "Transportation Research Part F: Traffic Psychology and Behaviour",
        "Safety Science",
        "Journal of Safety Research",
        "Transportation Research Part A: Policy and Practice",
        "IET Intelligent Transport Systems",
    ),
    units_and_formulas_notes=(
        "速度 km/h；减速度 m/s²；视距 m；制动距离按路面附着系数换算",
        "事故率 起/百万车公里；暴露量给行驶里程与运营天数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PTV Videopacket", "Kistler Driver Monitor", "MATLAB", "Simulink", "CarSim", "VISSIM", "SUMO", "Python (pandas/NumPy/scikit-learn)", "R", "SPSS", "Stata", "OmniPro (Omnet++)", "TransCAD", "GT-SUITE", "AnyLogic", "DSPACE (Vector)", "VBOX (dSPACE measurement)", "LabVIEW", "MATLAB/Simulink", "CARsim AD", "MATSim"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
