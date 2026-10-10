"""休闲与旅游学科论文支持：目的地营销、游客行为、旅游经济与服务研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="leisure_and_tourism",
    aliases=(
        "leisure_and_tourism",
        "休闲与旅游",
        "旅游管理",
        "tourism management",
        "leisure studies",
        "休闲研究",
        "旅游业",
        "tourism industry",
        "travel and hospitality",
    ),
    paper_types={
        "research": (
            "abstract（摘要）",
            "introduction（引言）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references（参考文献）",
        ),
        "case_study": (
            "abstract（摘要）",
            "introduction（引言）",
            "case description（案例背景）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references（参考文献）",
        ),
        "review": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references（参考文献）",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "问卷研究须报告样本量、抽样方法与响应率",
        "k2": "游客满意度须引用 SERVQUAL 或标准化量表",
        "k3": "空间分析须声明坐标系与时间窗口",
    },
    conventions=(
        "游客量单位人次或万人，注明统计口径",
        "满意度用 Likert 5/7 级量表",
        "景区等级用 AAAAA-A 级标注",
        "货币单位 USD 或 CNY，注明年份",
        "季节指数的季度划分遵循国家统计",
    ),
    key_venues=(
        "Annals of Tourism Research",
        "Tourism Management",
        "Journal of Travel Research",
        "Annals of Tourism Research",
        "旅游学刊",
    ),
    units_and_formulas_notes=(
        "游客接待量单位 万人次",
        "满意度用均值与标准差报告",
        "重游意愿以 5 级或 7 级量表计分",
        "季节性指数以 % 表示，年总为 100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "Google Earth Pro", "SPSS", "Stata", "R", "Python pandas", "AMOS", "Lisrel", "MaxDiff", "SimSTAT3", "NVivo", "ATLAS.ti", "Amadeus GDS", "Sabre GDS", "Google Analytics", "Amplitude", "Mixpanel", "Qualtrics", "问卷星"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
