"""未再细分服务学科论文支持：泛服务运营/服务创新/服务生态体裁、Chicago 引用样式与运营管理注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="services_not_further_defined",
    aliases=("services_not_further_defined", "services not further defined",
             "未再细分服务", "其他未细分服务", "miscellaneous services",
             "general services industry"),
    paper_types={
        "research": (
            "abstract",
            "introduction（服务问题与运营情境）",
            "methods（建模、仿真与实验）",
            "results（服务运营与绩效结果）",
            "discussion（管理启示与理论贡献）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（服务场景/组织案例）",
            "analysis（理论框架构建）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（服务运营管理理论谱系）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago Notes and Bibliography 样式（17th，运营管理学主流）",
    reporting_standards={
        "simulation": "服务仿真遵循离散事件仿真报告规范（报告队列、服务率、利用率）",
        "operations": "运营研究遵循 QUEUEING/OR 报告规范（含参数敏感性与稳健性）",
        "systematic_review": "系统综述遵循 PRISMA 并注册 PROSPERO",
    },
    conventions=(
        "服务流程须图示化（流程图、服务蓝图、泳道图）",
        "报告服务绩效指标（等待时间、周转时间、产能利用率、服务水平）",
        "仿真须报告随机种子、重复次数与 95% CI",
        "运营优化问题须明确目标函数与约束集合，最优性用证明/次优界限报告",
        "跨行业案例须报告行业背景、样本量与情境变量",
    ),
    key_venues=(
        "Journal of Business Research",
        "Academy of Management Review",
        "Strategic Management Journal",
        "Marketing Science",
        "Organization Science",
    ),
    units_and_formulas_notes=(
        "服务时间、等待时间、周期时间用分钟或小时；吞吐量用单位/小时",
        "队列模型记法 M/M/c、M/G/1 等须完整（到达/服务分布/服务台）",
        "利用率 ρ、到达率 λ、服务率 μ 用 SI 或每小时单位统一报告",
        "蒙特卡洛仿真随机种子、重复次数 n ≥ 30 与 95% CI 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "RStudio", "Microsoft Excel", "Qualtrics", "NVivo", "Mplus", "LISREL", "AMOS", "SmartPLS", "JASP", "Jamovi", "Stata", "Python（pandas/NumPy）", "ServiceNow", "Freshdesk", "Zendesk", "Microsoft Dynamics 365", "Kustomer", "Help Scout"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
