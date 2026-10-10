"""资源工程与提取冶金学学科论文支持：采矿、选矿与冶炼工艺。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="resources_engineering_and_extractive_metallurgy",
    aliases=(
        "resources_engineering_and_extractive_metallurgy",
        "资源工程与提取冶金",
        "mining engineering",
        "矿业工程",
        "选矿",
        "冶金",
        "metallurgy",
        "提取冶金",
        "extractive metallurgy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景）",
            "methodology（工艺方法）",
            "results（试验与结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（工艺分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（工艺评价）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "mineral_processing": "矿物试验流程、粒度分布、给料条件须完整",
        "metallurgical_trial": "热力学与动力学条件、试剂消耗须报告",
        "life_cycle": "ISO 14040 生命周期评价与系统边界定义",
    },
    conventions=(
        "矿物组成以重量百分数 wt% 报告并注矿物学名",
        "回收率与品位以标准公式定义并注明基准",
        "温度单位统一摄氏度并注明压力条件",
        "单位能耗以 t·dmt 或 kWh/t 给出",
        "试金分析与 XRD/SEM-EDS 须附原图或数据表",
    ),
    key_venues=(
        "Minerals Engineering",
        "International Journal of Mining Science and Technology",
        "Hydrometallurgy",
        "Mineral Processing Design and Operation",
        "Extractive Metallurgy International",
    ),
    units_and_formulas_notes=(
        "颗粒粒度 mm；品位%；回收率与精选率用标准冶金公式",
        "能耗以 kWh/t 或 GJ/t；单位以 SI 为单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("JAMAR Rock Breaker", "XRF Analyzer", "XRD diffractometer", "SEM-EDS", "Laser Particle Sizer", "Densimetric Analyzer", "Froth Flotation Column", "Magnetic Separator", "Pressure Leach Reactor", "Electrorefining Cell", "Bench Scale Roaster", "Audiopex Mill", "Fugro Trencher", "Geotechnical Core Logger", "MINEPLAN", "ROMSUMP", "Discrete Element Code", "ANSYS Mechanical", "COMSOL Multiphysics", "MATLAB"),
    category="工学",
    databases=("OpenAlex", "Crossref", "ScienceDirect"),
)
