"""管理与行政学科论文支持：公共部门治理、政策执行与组织管理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="management_and_administration",
    aliases=(
        "management_and_administration",
        "管理与行政",
        "公共管理",
        "行政管理",
        "Business Administration",
        "Public Administration",
        "Government Management",
        "政府管理",
        "行政研究",
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
    citation_style="APA 7 样式（公共管理与行政管理通用）",
    reporting_standards={
        "policy_analysis": "政策研究遵循 Policy Research 报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "qualitative": "质性研究遵循 COREQ 规范",
    },
    conventions=(
        "公共部门案例须明确制度语境与政策背景",
        "政策评估须报告效果量与置信区间",
        "绩效指标须注明来源与测量口径",
        "组织层级与岗位须标准化编码",
        "术语须遵循公共行政标准词汇（如 OMB、OECD 术语表）",
    ),
    key_venues=(
        "Journal of Public Administration Research and Theory",
        "Public Administration Review",
        "Journal of Policy Analysis and Management",
        "Administration & Society",
        "Public Administration",
        "中国行政管理",
    ),
    units_and_formulas_notes=(
        "财政数据以标准货币单位报告并说明汇率",
        "组织绩效用标准化比率报告",
        "政策效果量报告 Cohen's d 或边际效应",
        "样本量与置信水平须报告",
        "时间以年/季度为单位并附政策生效日期",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SAP SuccessFactors", "Workday HCM", "Oracle HCM", "ADP Workforce Now", "Microsoft Dynamics 365", "NetSuite", "Salesforce", "Power BI", "Power Automate", "Power Apps", "SharePoint", "Microsoft Teams", "Planner", "Outlook", "Excel", "PowerPoint", "Visio", "OneNote", "Loop", "Viva Insights"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
