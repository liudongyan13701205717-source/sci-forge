"""仓储学科论文支持：库存优化、拣货路径与仓库布局仿真的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="warehousing",
    aliases=("warehousing", "仓储", "仓储管理", "仓库管理", "物流仓储",
             "warehouse management", "WMS", "storage management",
             "inventory control", "warehouse optimization"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "literature review（文献综述）",
            "problem formulation（问题建模）",
            "methodology（方法）",
            "simulation results（仿真结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "warehouse setting（仓库概况）",
            "problem statement（问题描述）",
            "solution implementation（方案实施）",
            "performance evaluation（绩效评估）",
            "lessons learned",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "warehouse technologies（仓储技术综述）",
            "optimization methods（优化方法综述）",
            "industry benchmarks（行业基准）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_description": "案例须包含仓库面积、货品种类、日均吞吐量与 WMS 系统配置",
        "data_collection": "吞吐量数据须标注时间窗口、计量单位与异常值处理策略",
        "simulation": "仿真研究须说明模型参数、边界条件、验证结果与敏感性分析",
    },
    conventions=(
        "库存水平以件、吨或立方米为单位，明确计量基准",
        "周转率 = 年出库量 / 平均库存，单位：次/年",
        "拣货路径优化采用 TSP（旅行商问题）或 VRP（车辆路径问题）模型",
        "仓库布局图按 1:100 或 1:200 比例绘制，标注区域功能与通道宽度",
        "KPI 须给出基准值、目标值与计算周期",
    ),
    key_venues=(
        "Journal of Operations Management",
        "International Journal of Production Economics",
        "European Journal of Operational Research",
        "Journal of Supply Chain Management",
        "Omega",
    ),
    units_and_formulas_notes=(
        "面积为 m²；体积为 m³",
        "库存周转率：次/年",
        "拣货效率：行/小时或件/小时",
        "存储空间利用率：百分比",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SAP EWM", "Manhattan Associates", "Oracle WMS", "Microsoft Dynamics 365 Supply Chain", "FlexSim", "AnyLogic", "Arena Simulation", "Plant Simulation", "AutoCAD", "Revit", "MATLAB", "Python", "R", "Microsoft Excel", "Tableau", "SPSS", "OpenRefine", "LaTeX", "QGIS", "SolidWorks"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
