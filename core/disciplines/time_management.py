"""时间管理学科论文支持：个人效率/团队调度体裁、Journal of Management 引用样式与项目管理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="time_management",
    aliases=("time_management", "时间管理", "时间效率", "个人效率", "日程管理",
             "time management", "schedule optimization", "时间规划", "生产力管理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与时间管理问题）",
            "literature review（理论综述）",
            "methods（实验设计或调查方法）",
            "results（数据分析与发现）",
            "discussion（理论贡献与实践启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（组织/个人案例）",
            "analysis（流程分析与改进建议）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "scale_validation": "使用量表须经信效度检验（Cronbach's α≥0.7）",
        "sampling": "抽样方法与样本量须报告",
        "ethical_approval": "涉及人类受试者须声明伦理审批",
        "data_analyses": "统计检验方法与显著性水平须注明",
    },
    conventions=(
        "时间单位统一用分钟或小时",
        "效率指标定义须明确（如单位时间任务完成数）",
        "量表条目与计分方式须清晰说明",
        "干预措施（如番茄工作法）须标准化描述",
        "数据报告遵循 APA 7 格式（均值±SD, t/F, p 值）",
    ),
    key_venues=(
        "Journal of Management",
        "Personality and Social Psychology Bulletin",
        "Organizational Behavior and Human Decision Processes",
        "Academy of Management Journal",
        "Journal of Business and Psychology",
    ),
    units_and_formulas_notes=(
        "时间单位：小时（h）、分钟（min）、秒（s）",
        "效率用任务数/时间（tasks/h）表示",
        "统计检验：t 检验、ANOVA、卡方检验",
        "公式用 amsmath 排版；回归系数与效应量（Cohen's d）须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Excel", "SPSS", "R", "Python", "MATLAB", "NVivo", "AMOS", "Mplus", "Harvestr 时间追踪器", "RescueTime", "Toggl Track", "Clockify", "Microsoft Project", "Jira", "Trello", "Asana", "Google Calendar", "Notion", "SurveyMonkey", "Qualtrics"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
