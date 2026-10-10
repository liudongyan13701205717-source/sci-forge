"""零售业学科论文支持：顾客行为、渠道策略与运营效率。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="retailing",
    aliases=(
        "retailing",
        "零售学",
        "retail",
        "零售",
        "零售管理",
        "零售消费者行为",
        "e-retailing",
        "omnichannel",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与情境）",
            "methodology（方法与数据来源）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（企业/门店案例）",
            "analysis（战略/运营分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与文献综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "survey": "SAE/CONSORT; 抽样、问卷回收率、量表信效度须报告",
        "experiment": "店头 A/B 试验须报告分流、时长、显著性检验",
        "big_data": "POS/交易日志口径与去重规则须定义",
    },
    conventions=(
        "消费者行为量表 Cronbach's α≥0.7；主成分/因子分析须说明",
        "财务指标 ROA、ROE、坪效、客单价口径须定义",
        "样本来源、时间跨度与门店数量须报告",
        "变量名与操作化定义须列出",
    ),
    key_venues=(
        "Journal of Retailing",
        "Journal of Marketing",
        "Journal of Retailing and Consumer Services",
        "International Journal of Retail & Distribution Management",
        "Journal of Business Research",
    ),
    units_and_formulas_notes=(
        "销售额单位元/月或万元；坪效元/㎡/月",
        "NPS、CSAT 采用百分制或 5 点量表并给出分布",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R with tidyverse", "NVivo", "Python Pandas", "Tableau", "Power BI", "Google Analytics", "Yammer POS System", "SAP POS", "Salesforce Commerce Cloud", "Shopify Analytics", "Snowflake Data Warehouse", "Tableau Prep", "Qualtrics Survey", "MRO Consumer Insight Panel", "Kantar Worldpanel", "Nielsen Retail Audit", "Amplitude Product Analytics", "Google BigQuery"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "EBSCO"),
)
