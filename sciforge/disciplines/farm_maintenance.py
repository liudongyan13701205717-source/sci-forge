"""农场维护学科论文支持：农业设施、设备维护与农场运营研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="farm_maintenance",
    aliases=(
        "farm_maintenance", "农场维护", "农业设施维护",
        "farm maintenance", "农场维护",
        "agricultural facility maintenance", "农业设施维护",
        "farm operation", "农场运营",
        "equipment maintenance", "设备维护",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（维护问题与背景）",
            "methodology（维护方法、实验条件、效果评估）",
            "results（维护效果与可靠性评估）",
            "discussion（维护优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "maintenance process（维护过程）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（方法对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "maintenance": "维护步骤须完整描述",
        "testing": "测试方法须注明（标准、仪器、环境）",
        "safety": "安全规程须声明",
    },
    conventions=(
        "维护周期用 月 或 年 表示",
        "故障率用 % 表示",
        "维修时间用 h 表示",
        "成本用 元 表示",
        "统计检验注明效应量与置信区间",
    ),
    key_venues=(
        "Journal of Agricultural Engineering",
        "Applied Engineering in Agriculture",
        "Transactions of the ASABE",
        "Journal of Food Engineering",
        "Biosystems Engineering",
        "Computers and Electronics in Agriculture",
    ),
    units_and_formulas_notes=(
        "维护周期用 月 或 年 表示",
        "故障率用 % 表示",
        "维修时间用 h 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "CMMS Software", "Preventive Maintenance Software", "Predictive Maintenance Software", "Equipment Monitoring System", "IoT Sensors", "Drone Survey", "GPS Tracking System", "Fleet Management Software", "Inventory Management Software", "Work Order Management Software", "Maintenance Scheduling Software", "Reliability Analysis Software", "Failure Analysis Software", "Thermal Imaging Camera", "Vibration Analyzer"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
