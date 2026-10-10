"""垃圾收运学科论文支持：垃圾收集系统、车辆路径优化与清运作业设计注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="refuse_collection",
    aliases=(
        "refuse_collection",
        "垃圾收运",
        "垃圾收集",
        "清运作业",
        "Refuse Collection",
        "Waste Collection",
        "Municipal Solid Waste Collection",
        "Vehicle Routing"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与清运问题）",
            "methodology（路径优化/收运调度方法）",
            "results（算法/运营结果）",
            "discussion（工程与成本意义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域与收运现状）",
            "analysis（路径与运力分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（VRP/收运系统基础）",
            "evidence synthesis（方法与城市对比）",
            "future directions",
            "references"
        ),
    },
    citation_style="Elsevier 样式（Waste Management 遵循编号制）",
    reporting_standards={
        "vehicle_routing": "车辆路径须报告起点/终点、装载率、总里程与计算时间",
        "scheduling": "收运频次与班次安排须报告居民响应率与投诉率",
        "experimental": "实地试验须注明采样日、称重方法与垃圾组成"
    },
    conventions=(
        "垃圾量单位 t/d；车辆容积 m³；载重 kg 或 t",
        "车辆路径须注明车型与额定载荷",
        "转运站与末端处理设施须明确类型",
        "对比研究须在同一区域或同一收运周期比较",
        "算法报告须给出计算时间与最优性指标"
    ),
    key_venues=(
        "Waste Management",
        "Journal of Environmental Management",
        "Waste Management & Research",
        "Resources Conservation and Recycling",
        "Journal of Cleaner Production"
    ),
    units_and_formulas_notes=(
        "垃圾量：t/d 或 kg/h；车辆容积：m³；载重：kg",
        "收集效率 = 实际收集量/预测生成量（%）",
        "单位运距成本：CNY/(t·km)",
        "装载率 = 实际载重/额定载重（%）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("OR-Tools", "OptRoute", "ArcGIS Network Analyst", "QGIS", "AnyLogic", "VRPy", "Open-VRP", "Gurobi", "CPLEX", "MATLAB", "Tableau", "Google Maps API", "Fleet Management System", "GPS Tracker", "RFID Reader", "Smart Bin Sensor", "Truck Scale", "Load Sensor", "Waste Weighing Station", "Waste Composition Analyzer"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
