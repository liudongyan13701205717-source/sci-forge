"""Street cleaning 学科论文支持：环卫作业/城市卫生/路径优化/环境监测。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="street_cleaning",
    aliases=(
        "street_cleaning", "Street cleaning", "环卫", "道路清洁",
        "城市环卫", "街道清扫", "环卫作业",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methods（作业方案与监测方法）",
            "results（清洁效率与环境指标）",
            "discussion（讨论与优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域与现状）",
            "analysis（问题分析）",
            "results（整治成效）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；括号式）",
    reporting_standards={
        "route_optimization": "路径优化须报告目标函数、约束条件与求解算法",
        "environmental_monitoring": "环境监测须报告监测点位、频次、仪器型号与校准方式",
        "efficiency_evaluation": "效率评价须报告评价指标体系与权重确定方法",
        "performance_assessment": "绩效考核须报告考核周期、数据收集方式与统计口径",
    },
    conventions=(
        "道路等级（快速路/主干路/次干路/支路）须注明",
        "清扫作业频次与时间窗口须报告",
        "环境监测数据须注明采样时间与气象条件",
        "成本分析须注明计价单位（元/km·次）与统计口径",
        "GIS 数据须注明坐标系与精度",
    ),
    key_venues=(
        "Waste Management",
        "Journal of Environmental Management",
        "Environmental Science & Technology",
        "城市与环境研究",
        "环境工程学报",
    ),
    units_and_formulas_notes=(
        "道路长度用 km；面积用 km²",
        "PM2.5 用 μg/m³；噪声用 dB(A)",
        "清扫频次用 次/天或 次/周",
        "成本用 元/km·次或 元/km²·年",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("环卫 GIS 路径优化系统", "GPS 车辆定位系统", "智能垃圾箱（传感器）", "无人机道路巡检系统", "扬尘在线监测仪（PM2.5）", "道路油污检测仪", "真空吸污车", "高压冲洗车", "环卫作业电子围栏系统", "车载视频监控系统", "水质在线监测仪", "环卫绩效考核管理系统", "智慧环卫大数据平台", "道路环境综合评价软件", "城市精细化管理平台（一网统管）", "环卫车辆油耗监测系统", "道路积尘负荷仪", "环卫作业监管平台（RFID 打卡）", "空气质量自动监测站", "智能垃圾分类回收系统"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
