"""批发与零售学科论文支持：流通渠道、渠道管理与零售运营效率评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wholesale_and_retail_sales",
    aliases=(
        "wholesale and retail sale",
        "批发零售",
        "流通渠道",
        "渠道管理",
        "retail management",
        "distribution channel",
        "channel management",
        "批发与零售",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "literature review（渠道理论与零售前沿）",
            "data and methods（数据来源与研究方法）",
            "empirical results（实证结果与统计分析）",
            "discussion（机制讨论与管理启示）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "company background（企业背景描述）",
            "channel structure analysis（渠道结构分析）",
            "operational performance（运营绩效评估）",
            "strategy evaluation（策略评估与启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "retail evolution（零售业态演变综述）",
            "omni-channel strategies（全渠道策略综述）",
            "digital transformation（数字化转型综述）",
            "future research agenda",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "channel mapping": "渠道研究须明确标注批发层级、零售终端与消费者触达路径",
        "data vintage": "零售数据须标注数据采集时点、渠道范围与区域覆盖",
        "performance metrics": "运营绩效须区分财务指标（毛利率、周转率）与运营指标（坪效、人效）",
        "competitive context": "须说明市场竞争格局与同业对标基准",
    },
    conventions=(
        "批发层级用 W1/W2/... 表示，零售终端用 R1/R2/... 表示",
        "渠道长度（number of intermediaries）与渠道宽度（number of channels）须明确区分",
        "销售数据标注单位（万元/亿元）与时间粒度（日/周/月/年）",
        "全渠道（omni-channel）研究须说明线上线下数据融合方法与去重规则",
        "库存周转率计算须标注采用移动平均还是加权平均成本法",
    ),
    key_venues=(
        "Journal of Retailing",
        "Journal of Marketing Channels",
        "International Journal of Retail & Distribution Management",
        "Retail Research International",
        "Journal of Business & Industrial Marketing",
    ),
    units_and_formulas_notes=(
        "销售毛利率 =（销售收入-销售成本）/销售收入×100%",
        "库存周转率 = 销售成本 / 平均库存（次/年）",
        "坪效 = 销售面积 / 平均库存额（元/㎡·月）",
        "客户留存率 = 期末留存客户数 / 期初客户数×100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Salesforce 客户关系管理系统", "SAP ERP 企业资源计划", "Oracle Retail 零售管理系统", "SAP Ariba 供应链协同平台", "Coupa 采购与支出管理", "NetSuite 云计算 ERP", "Shopify 电商零售平台", "BigCommerce 电商零售平台", "WooCommerce 电商插件", "Tableau 数据可视化", "Power BI 商业智能分析", "QlikView 数据可视化平台", "Python 数据处理（pandas）", "R 语言统计分析", "Stata 计量软件", "SPSS 统计分析软件", "Excel 高级数据分析", "LaTeX 学术排版", "EndNote 文献管理", "Google Analytics 流量分析"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
