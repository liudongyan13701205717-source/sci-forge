"""邮件运营学科论文支持：邮政/快递系统的路由、配送与运营优化研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mail_operations",
    aliases=(
        "mail_operations",
        "邮件运营",
        "邮政运营",
        "快递运营",
        "物流运营",
        "Mail Operations",
        "Postal Operations",
        "快递路由优化",
        "分拣配送",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
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
    citation_style="APA 7 样式（物流与运营研究通用）",
    reporting_standards={
        "simulation": "离散事件仿真遵循 M&S 报告规范",
        "optimization": "优化模型遵循运筹学报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
    },
    conventions=(
        "路由/调度问题须报告实例规模",
        "仿真研究须报告随机种子与置信区间",
        "对比方法须包含基线（启发式或精确法）",
        "实验平台与硬件须明确",
        "术语须遵循 ISO 物流与运输词汇",
    ),
    key_venues=(
        "Transportation Science",
        "European Journal of Operational Research",
        "Journal of Operations Management",
        "Omega: Journal of Decision Sciences",
        "International Journal of Production Economics",
        "European Journal of Operational Research",
    ),
    units_and_formulas_notes=(
        "时间以秒/分钟为单位并标注 SI",
        "路径长度以公里/米为单位",
        "成本单位统一为货币并说明汇率",
        "吞吐率单位明确（件/小时）",
        "统计量给出均值、标准差与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SAP TM", "SAP EWM", "Oracle Transportation Management", "IBM Sterling Order Management", "QGIS", "ArcGIS", "PostGIS", "AnyLogic", "FlexSim", "Arena", "Python（pandas 与 scikit-learn）", "R（统计与可视化）", "Tableau", "Power BI", "Apache Spark", "Kafka", "Docker", "Kubernetes", "Jenkins", "Splunk"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
