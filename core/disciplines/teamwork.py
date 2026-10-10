"""团队合作学科论文支持：协作过程/团队效能的体裁、APA 7 引用样式与协作分析注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teamwork",
    aliases=(
        "teamwork",
        "团队合作",
        "协作",
        "团队效能",
        "团队协作",
        "group collaboration",
        "team effectiveness",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、理论框架与研究问题）",
            "methods（设计、样本与协作数据采集）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（团队与协作情境）",
            "data and analysis（协作轨迹分析）",
            "findings（发现）",
            "discussion and implications",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与筛选方法）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份制，组织行为与协作研究主流规范）",
    reporting_standards={
        "empirical": "实证研究须报告团队数、成员数与团队层面的分析单位",
        "measurement": "团队量表须区分个体层与团队层施测，报告层级信度",
        "ethics": "组织内协作数据使用须取得雇主知情同意与数据保护批准",
        "longitudinal": "追踪研究须报告波次、间隔与流失率",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "团队层指标须说明聚合依据与组内一致性（ICC）",
        "成员角色与构成（专业背景、职级、远程/线下）须报告",
        "协作沟通数据须匿名化成员身份并标注工具来源",
        "社会影响效应须控制团队规模与任务时长",
        "Tuckman/团队拓扑等模型引用须给出提出者与年份"
    ),
    key_venues=(
        "Journal of Applied Psychology",
        "Academy of Management Journal",
        "Journal of Management Studies",
        "Human Relations",
        "Journal of Business and Psychology",
    ),
    units_and_formulas_notes=(
        "效能指标须给出单位：任务完成时长（min）、交付吞吐（件/周）",
        "公式用 amsmath；ICC 与效应量公式须编号并被引用",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "远程协作强度用消息数/时长报告，须标注时间窗"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Teams", "Slack", "Miro", "Mural", "Lucidchart", "draw.io", "Trello", "Asana", "Jira", "Notion", "Microsoft Viva Insights", "Google Workspace", "Zoom", "Loom", "Qualtrics", "SPSS", "R", "NVivo", "Basecamp", "ClickUp"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
