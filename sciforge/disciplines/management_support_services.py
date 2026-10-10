"""管理支持服务学科论文支持：行政、HR、财务与采购支持服务研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="management_support_services",
    aliases=(
        "management_support_services",
        "管理支持服务",
        "行政支持",
        "人力资源支持",
        "Management Support",
        "Administrative Support",
        "Business Support Services",
        "后台支持服务",
        "BPO 服务",
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
    citation_style="APA 7 样式（商业服务与运营通用）",
    reporting_standards={
        "service_design": "服务设计遵循 SD 报告规范",
        "survey": "客户满意度调查遵循 AAPOR 规范",
        "case_study": "案例研究遵循案例研究报告规范",
    },
    conventions=(
        "服务绩效指标须报告 KPI 定义与测量口径",
        "外包/BPO 案例须明确 SLA 与服务范围",
        "成本效益须报告 ROI 或成本节约比",
        "服务质量须报告 SERVQUAL 或类似量表",
        "供应商评估须报告权重与评分方法",
    ),
    key_venues=(
        "Journal of Service Research",
        "Journal of Business and Industrial Marketing",
        "Human Resource Management Review",
        "SOP Journal",
        "European Management Journal",
        "管理世界",
    ),
    units_and_formulas_notes=(
        "服务成本以货币单位报告并说明汇率",
        "客户满意度以 5/7 分制报告并附样本量",
        "SLA 达成率以百分比报告",
        "处理时长以小时/分钟报告并附置信区间",
        "人力成本以每人月薪报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Workday HCM", "SAP SuccessFactors", "Oracle HCM", "Sage Intacct", "NetSuite", "QuickBooks Online", "Xero", "Asana", "Trello", "Jira", "Monday.com", "ClickUp", "Toggl", "Harvest", "Time Doctor", "Expensify", "Concur", "Coupa", "Stampli", "SharePoint"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
