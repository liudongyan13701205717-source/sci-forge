"""电话销售学科论文支持：远程销售过程与转化分析的体裁、APA 7 引用样式与销售指标注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="telephone_selling",
    aliases=(
        "telephone_selling",
        "电话销售",
        "远程销售",
        "电销",
        "呼叫中心销售",
        "telesales",
        "outbound selling",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究假设）",
            "methods（样本、话术设计与实验安排）",
            "results（转化与沟通指标）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（企业与业务情境）",
            "process analysis（销售流程与话术分析）",
            "results（业绩与过程指标）",
            "discussion and implications",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与筛选方法）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份制，营销与运营管理研究主流规范）",
    reporting_standards={
        "experimental": "实验研究须报告被叫样本量、随机分组与话术版本",
        "privacy": "通话录音与个人数据处理须符合个人信息保护要求并取同意",
        "measurement": "转化率等指标须定义分子分母与统计窗口",
        "longitudinal": "追踪研究须报告周期长度与流失情况",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "通话录音与分析须匿名化客户身份与个人敏感信息",
        "转化率、接通率、成单率须统一口径并说明去重规则",
        "话术脚本须以附录或匿名化方式提供",
        "合规约束（拒访登记、骚扰限制、时段限制）须在方法节声明",
        "业绩指标须区分个人层与团队/座席层，控制班次差异"
    ),
    key_venues=(
        "Journal of Marketing Research",
        "Journal of Retailing and Consumer Services",
        "European Journal of Information Systems",
        "Journal of Interactive Marketing",
        "Journal of Business and Industrial Marketing",
    ),
    units_and_formulas_notes=(
        "通话时长用 min；话务量用 ACW/ASA（秒）与话务密度 Erlang",
        "转化率用百分比，须给出样本量与置信区间",
        "公式用 amsmath；Erlang C 排队公式与转化率公式须编号并被引用",
        "金额指标注明币种与统计口径（订单额/回款额）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Salesforce", "HubSpot", "Zendesk", "Freshdesk", "Zoho CRM", "Microsoft Dynamics 365", "Glean", "NICECX One", "Avaya", "Genesys", "Five9", "Aircall", "Talkdesk", "RingCentral", "Gong", "Qualified", "PowerDialer", "ClickCall", "SPSS", "Microsoft Excel"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
