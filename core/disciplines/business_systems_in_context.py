"""信息系统学科论文支持：企业信息系统、业务系统与 IT 治理体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="business_systems_in_context",
    aliases=(
        "business_systems_in_context",
        "信息系统",
        "管理信息系统",
        "企业信息系统",
        "业务系统",
        "Business Systems in Context",
        "Information Systems",
        "Management Information Systems",
        "Enterprise Systems",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与贡献）",
            "literature review",
            "theoretical framework",
            "methodology（案例/实验/调查/数据分析）",
            "findings",
            "discussion",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（企业案例背景）",
            "research design",
            "findings",
            "implications（理论与实践启示）",
            "conclusion",
            "references",
        ),
        "survey_study": (
            "abstract",
            "introduction",
            "theoretical framework",
            "research design",
            "data collection",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7；MIS 领域遵循 MIS Quarterly 与 ISR 编辑规范",
    reporting_standards={
        "case_study": "案例须说明资料来源、访谈对象、数据编码与信度",
        "survey": "调查须报告样本量、抽样、回复率与共同方法偏差控制",
        "experiment": "实验须报告随机化、盲法、样本量与效应量",
        "data_analysis": "数据分析须说明数据源、构造、缺失处理与稳健性",
    },
    conventions=(
        "系统架构须用统一图形语言（UML/BPMN 等）描述",
        "案例研究须说明资料来源、访谈与三角验证路径",
        "实证研究须报告测量量表信效度与共同方法偏差检验",
        "IT 投资-绩效关系须控制规模、行业与时间因素",
    ),
    key_venues=(
        "Information Systems Research",
        "MIS Quarterly",
        "Journal of Management Information Systems",
        "Information & Management",
        "International Journal of Information Management",
        "Journal of the Association for Information Systems",
        "Communications of the ACM",
        "IEEE Transactions on Knowledge and Data Engineering",
        "计算机学报",
        "管理世界",
    ),
    units_and_formulas_notes=(
        "系统响应时间以毫秒（ms）为单位",
        "吞吐量以每秒事务数（TPS）或每秒查询数（QPS）报告",
        "调查量表须报告 Cronbach α 与组合信度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ERwin", "Microsoft Visio", "Lucidchart", "Draw.io", "StarUML", "Modelio", "Archi", "BPMN.io", "Jira", "ServiceNow", "Salesforce", "SAP S/4HANA", "Oracle E-Business Suite", "Amazon Web Services (AWS)", "Microsoft Azure", "Kubernetes", "Docker", "GitHub", "GitLab", "Prometheus", "Grafana", "Datadog", "New Relic", "Tableau", "Microsoft Power BI"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "IEEE Xplore", "ACM DL"),
)
