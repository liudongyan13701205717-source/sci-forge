"""Demonstration techniques 学科论文支持：示威/抗议技术研究体裁、社会运动分析工具与数据采集规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="demonstration_techniques",
    aliases=(
        "demonstration_techniques", "示威技术", "抗议技术研究",
        "demonstration studies", "protest techniques", "social movement studies",
        "demonstration strategy", "示威策略", "抗议策略",
        "demonstration organization", "mass action studies",
        "crowd dynamics", "示威活动组织",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与示威场景）",
            "data and methods（数据采集与研究方法）",
            "results（示威行为模式与效果分析）",
            "discussion（政策与社会意义）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context（案例背景）",
            "analysis（示威过程与策略分析）",
            "outcome（结果与影响评估）",
            "references",
        ),
        "theory": (
            "abstract",
            "introduction",
            "theoretical_framework（理论框架）",
            "model（行为模型或分析框架）",
            "application（应用与检验）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "data_collection": "社交媒体数据采集须声明抓取范围、时间跨度与平台",
        "analysis": "数据分析须区分定量方法（统计分析）与定性方法（文本/内容分析）",
        "network": "网络分析须声明节点/边定义、算法选择与参数设定",
        "ethics": "伦理审查与知情同意须声明；涉及敏感数据须注明脱敏处理",
    },
    conventions=(
        "示威活动描述须明确时间、地点、参与规模与组织形式",
        "数据分析须区分定量方法（统计分析）与定性方法（文本/内容分析）",
        "社交媒体数据采集须声明抓取范围、时间跨度与平台",
        "网络分析须声明节点/边定义、算法选择与参数设定",
        "伦理审查与知情同意须声明；涉及敏感数据须注明脱敏处理",
    ),
    key_venues=(
        "Social Movement Studies",
        "Journal of Social Issues",
        "Socio-Economic Review",
        "Journal of Contemporary History",
        "European Journal of Political Research",
        "Social Science History",
        "Theory and Society",
        "Mobilization",
    ),
    units_and_formulas_notes=(
        "参与规模用 人数；时间跨度用 天/周/月",
        "网络分析指标（中心度、聚类系数）须注明计算方法和参数",
        "文本分析须注明语料范围与主题模型参数",
        "统计显著性用 α=0.05；95% 置信区间须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "R (RStudio)", "Python (pandas, networkx)", "Stata", "IBM SPSS Statistics", "Tableau", "Power BI", "Qualtrics", "SurveyMonkey", "ArcGIS", "QGIS", "Gephi", "UCINET", "OpenRefine", "Google Trends", "Twitter API", "YouTube Data API", "Media Cloud", "Amazon Mechanical Turk"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
