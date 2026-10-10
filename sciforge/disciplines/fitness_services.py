"""健身服务学科论文支持：健身服务管理、服务质量与客户体验研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fitness_services",
    aliases=("fitness_services", "健身服务", "fitness management",
             "sports service management", "health club management",
             "健身房管理", "体育服务管理", "fitness industry",
             "sports business"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "service": "服务质量评估须报告量表来源、信效度系数与样本特征",
        "survey": "问卷调查须说明抽样方法、问卷设计与数据收集流程",
        "satisfaction": "满意度分析须注明评估维度与统计方法",
    },
    conventions=(
        "Likert 量表用 5 级或 7 级表示",
        "服务满意度用均值与标准差表示",
        "会员流失率用百分比(%)表示",
        "客单价用元/次或元/月表示",
        "NPS (净推荐值) 用 [-100, 100] 表示",
    ),
    key_venues=(
        "Journal of Sport and Exercise Psychology",
        "Journal of Sport Management",
        "Sport Management Review",
        "International Journal of Sport and Fitness",
        "体育科学",
    ),
    units_and_formulas_notes=(
        "客户满意度 = Σ(重要性×满意度)/Σ重要性 × 100%",
        "净推荐值 NPS = 推荐者占比% - 贬损者占比%",
        "会员留存率 = (期末会员数 - 新会员数) / 期初会员数 × 100%",
        "客单价 = 总收入 / 交易次数，单位 元/次",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "Excel", "NVivo", "Atlas.ti", "Qualtrics", "SurveyMonkey", "Google Forms", "健身管理系统", "客户关系管理系统 (CRM)", "会员管理系统", "预约管理系统", "服务评价系统", "Tableau", "Power BI", "Kinovea (运动分析)", "视频分析系统", "客户满意度评估系统", "SERVQUAL 评估工具", "健身课程管理系统"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)