"""未另分类服务学科论文支持：服务产业管理/服务质量/服务运营体裁、Chicago 引用样式与管理学研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="services_not_elsewhere_classified",
    aliases=("services_not_elsewhere_classified", "services not elsewhere classified",
             "未另分类服务", "其他服务", "未另分类服务业", "general services",
             "miscellaneous services"),
    paper_types={
        "research": (
            "abstract",
            "introduction（服务问题与管理情境）",
            "methods（数据、模型与情境）",
            "results（服务绩效与服务创新结果）",
            "discussion（管理启示与理论贡献）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（服务企业/服务流程案例）",
            "analysis（框架化分析）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（服务管理理论谱系）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago Notes and Bibliography 样式（17th，服务管理学主流）",
    reporting_standards={
        "primary_data": "一手数据须报告样本、抽样、量表与信度（Cronbach's α、CR）",
        "service_quality": "服务质量研究遵循 SERVQUAL/SERVPERF 与 PRISMA 系统综述规范",
        "causal_inference": "因果推断报告识别策略（IV、DID、RD、PSM）与稳健性检验",
    },
    conventions=(
        "服务构念（服务质量、服务创新、服务主导逻辑）须显式界定并引用出处",
        "服务触点（customer contact points）与服务流程须图示化",
        "报告服务绩效指标（响应时间、可靠性、客户满意度、净推荐值 NPS）",
        "问卷量表须报告 Cronbach's α ≥ .70 与验证性因子分析拟合指数",
        "报告样本、行业与地理背景；跨国样本须报告汇率与通胀调整",
    ),
    key_venues=(
        "Journal of Service Research",
        "Journal of Service Management",
        "International Journal of Service Industry Management",
        "European Journal of Operational Research",
        "Management Science",
    ),
    units_and_formulas_notes=(
        "服务质量量表用 SERVQUAL 五维度；7 点 Likert",
        "效应量用 Cohen's d、η²p、Cohen's f²；95% CI 报告",
        "服务效率用 SERVQUAL 差值项（感知-期望）；NPS 报告 -100 至 100 整数",
        "回归与 SEM 用 amsmath；报告 R²、ΔR² 与路径系数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "RStudio", "Microsoft Excel", "Qualtrics", "NVivo", "Mplus", "LISREL", "AMOS", "SmartPLS", "JASP", "Jamovi", "Stata", "Python（pandas/NumPy）", "Salesforce", "Freshdesk", "Zendesk", "Microsoft Dynamics 365", "SAP Service Cloud", "Qualtrics XM"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
