"""招聘学科论文支持：人才选拔/招聘流程/人才获取体裁、APA 引用样式与招聘评估口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="recruitment",
    aliases=(
        "recruitment",
        "招聘",
        "人才选拔",
        "人才获取",
        "Recruitment",
        "Talent Acquisition",
        "选拔",
        "招聘流程",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（模型与数据）", "results（招聘结果与绩效）", "discussion（机理与管理意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（招聘过程分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；人力资源研究常用 APA）",
    reporting_standards={
        "k1": "招聘评估须遵循 SHRM 报告规范",
        "k2": "公平性评估须遵循 EEOC 规范",
        "k3": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "招聘渠道与筛选流程须说明",
        "评估量表与评分标准须报告",
        "公平性与多样性数据须报告",
        "成本与时间指标须给出计算口径",
        "统计量给出 M/SD 与 95% CI",
    ),
    key_venues=(
        "Human Resource Management Review",
        "Journal of Applied Psychology",
        "Personnel Psychology",
        "Human Resource Management Journal",
        "Journal of Management",
    ),
    units_and_formulas_notes=(
        "时间指标用天或周",
        "成本指标用货币单位",
        "转化率给出分子分母口径",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("LinkedIn Recruiter", "Indeed", "Glassdoor", "Greenhouse", "Lever", "Workday", "BambooHR", "HiBob", "SAP SuccessFactors", "Oracle HCM", "Ashby", "SmartRecruiters", "Beamery", "Gloat", "Eightfold", "Zoom Interview", "Microsoft Interview Management", "SPSS", "Excel", "Tableau"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
