"""汽车工程学科论文支持：整车/动力/底盘体裁、SAE 引用样式与汽车工程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="automotive_engineering",
    aliases=("automotive_engineering", "汽车工程", "汽车", "车辆工程",
             "整车开发", "汽车动力"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与汽车问题）",
            "methods（建模、试验与参数）",
            "results（性能与验证数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "vehicle_development": (
            "abstract",
            "introduction",
            "targets（整车目标与法规）",
            "design（系统设计）",
            "testing（试验验证）",
            "results（达标情况）",
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
    citation_style="SAE 样式（编号制；SAE 期刊遵循 SAE 规范）",
    reporting_standards={
        "experimental": "整车/零部件试验遵循 SAE J 系列试验标准",
        "crash_testing": "碰撞试验遵循 FMVSS/NCAP 规程",
        "emissions": "排放测试遵循 UNECE/EPA 规程",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "simulation": "仿真研究遵循 SAE 仿真报告规范",
    },
    conventions=(
        "整车参数（质量、尺寸、轴距）须完整报告",
        "动力总成（发动机/电机）参数须注明",
        "试验工况（NEDC、WLTP、CLTC）须明确",
        "安全与排放法规版本须引用",
        "控制策略与标定参数须说明",
    ),
    key_venues=(
        "SAE International Journal of Vehicles and Machines",
        "IEEE Transactions on Vehicular Technology",
        "International Journal of Automotive Technology",
        "Vehicle System Dynamics",
        "Proceedings of the Institution of Mechanical Engineers, Part D",
        "SAE International Journal of Connected and Automated Vehicles",
    ),
    units_and_formulas_notes=(
        "功率用 kW；扭矩用 N·m；油耗用 L/100km",
        "公式用 amsmath；动力学与能耗方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "加速度用 m/s²；车速用 km/h",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("CATIA", "ANSYS", "MSC Adams/CarSim", "MATLAB/Simulink"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)