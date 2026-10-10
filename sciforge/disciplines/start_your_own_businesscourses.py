"""创业学学科论文支持：创业教育/商业模式/小企业创业体裁、APA 引用样式与创业学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="start_your_own_businesscourses",
    aliases=("start_your_own_businesscourses", "创业学", "创业教育",
             "自主创业课程", "entrepreneurship", "business model design"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7th（管理学主流）",
    reporting_standards={
        "startup_study": "初创企业研究遵循 SEED 早期企业数据集规范",
        "entrepreneurship_education": "创业教育评估遵循 EPI（Entrepreneurship Education Policy Indicator）",
        "case_study": "创业案例报告遵循 Harvard Business School Case Study 规范",
    },
    conventions=(
        "商业模式描述须使用 BMC（Business Model Canvas）或 Lean Canvas 框架",
        "初创企业样本须报告年龄、行业、地域与融资阶段",
        "财务数据以万元或等值货币报告，注明会计年度与币种",
        "创业教育评估须区分前测-后测设计与准实验设计",
        "术语首次出现给出中文全称与英文对照（如 MVP = 最小可行产品）",
    ),
    key_venues=(
        "Journal of Business Venturing",
        "Entrepreneurship Theory and Practice",
        "Small Business Economics",
        "Venture Capital Journal",
        "管理世界（Journal of Management World）",
    ),
    units_and_formulas_notes=(
        "营收/成本以万元或等值货币报告，注明会计年度与币种",
        "客户指标以 CAC、LTV、LTV/CAC 报告",
        "增长指标以月/季度活跃用户与留存率报告",
        "公式用 amsmath；财务比率换算须明确分子分母口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("LeanStack 精益画布", "Business Model Canvas", "Miro 协作白板", "Notion", "Trello 看板", "Asana 项目管理", "Figma 原型", "Canva 图像设计", "Google Workspace", "Microsoft Office 365", "QuickBooks 财务", "Xero 财务", "Stripe 支付", "Shopify 电商", "Salesforce CRM", "HubSpot CRM", "Mailchimp 邮件营销", "Google Analytics 分析", "Mixpanel 产品分析", "SurveyMonkey 调研"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "EBSCO"),
)
