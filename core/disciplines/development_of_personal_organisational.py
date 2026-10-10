"""个人组织技能发展学科论文支持：时间管理、组织行为与自我调节研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="development_of_personal_organisational",
    aliases=(
        "development_of_personal_organisational", "个人组织技能发展",
        "personal organizational skills", "个人组织能力",
        "time management", "时间管理",
        "self-regulation", "自我调节",
        "goal setting", "目标设定",
        "organizational behavior", "组织行为技能",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（技能发展问题与理论背景）",
            "method（参与者、干预方案、测量工具）",
            "results（技能发展效果）",
            "discussion（机制探讨与实践启示）",
            "references",
        ),
        "intervention_study": (
            "abstract",
            "introduction",
            "intervention design（干预方案设计）",
            "results（技能提升与行为改变）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical framework（理论框架）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "intervention": "干预方案须描述内容、时长、频率与实施方式",
        "measurement": "技能评估工具须注明信效度",
        "statistics": "统计检验须注明效应量与置信区间",
        "ethics": "涉及人体验证须声明 IRB 批准",
    },
    conventions=(
        "技能定义须明确（行为指标、评估标准）",
        "干预方案须注明干预频率与持续时间",
        "评估工具须注明版本与信效度",
        "行为指标须给出基线数据与后测数据",
        "统计检验注明 α=0.05 与效应量",
    ),
    key_venues=(
        "Journal of Applied Psychology",
        "Personnel Psychology",
        "Academy of Management Review",
        "Journal of Vocational Behavior",
        "Career Development International",
        "Employee Relations",
    ),
    units_and_formulas_notes=(
        "时间用小时/分钟表示",
        "任务完成度用 % 表示",
        "量表评分用 Likert 5/7 级表示",
        "统计检验注明效应量（d/η²）与 95% CI",
        "样本量须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Excel", "Google Forms", "Qualtrics", "SurveyMonkey", "Trello", "Asana", "Notion", "Todoist", "Microsoft Planner", "Time Tracking Software", "MindMap Software", "Gantt Software", "Power BI", "Tableau", "NVivo", "Miro", "Canva"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "PsycINFO"),
)
