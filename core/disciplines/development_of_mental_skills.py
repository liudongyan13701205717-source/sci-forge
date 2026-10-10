"""心智技能发展学科论文支持：认知技能习得、元认知与工作记忆研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="development_of_mental_skills",
    aliases=(
        "development_of_mental_skills", "心智技能发展",
        "cognitive skill development", "认知技能发展",
        "metacognitive development", "元认知发展",
        "working memory development", "工作记忆发展",
        "executive function development", "执行功能发展",
        "problem solving", "问题解决技能",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（认知技能问题与理论背景）",
            "method（参与者、任务、训练方案、测量）",
            "results（训练效果与迁移）",
            "discussion（认知机制与实践启示）",
            "references",
        ),
        "intervention": (
            "abstract",
            "introduction",
            "training program（训练方案设计）",
            "results（认知改善与迁移效果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical synthesis（理论综合）",
            "evidence evaluation（证据评估）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "training": "训练方案须描述任务、时长、频率与练习量",
        "transfer": "迁移测试须区分近迁移与远迁移",
        "measurement": "认知任务须注明标准化与信效度",
        "ethics": "涉及儿童/老年人研究须声明伦理审批",
    },
    conventions=(
        "认知任务定义须明确（任务类型、难度、测量指标）",
        "训练方案须注明练习次数、间隔时间与反馈条件",
        "认知评估工具须注明版本与标准化年龄范围",
        "效应量须报告 Cohen's d 或 η²",
        "迁移效果须区分近迁移与远迁移任务",
    ),
    key_venues=(
        "Journal of Experimental Psychology: Learning, Memory, and Cognition",
        "Cognitive Development",
        "Developmental Psychology",
        "Psychonomic Bulletin & Review",
        "Mind, Brain, and Education",
        "Cortex",
    ),
    units_and_formulas_notes=(
        "反应时间用 ms 表示",
        "工作记忆容量用 n-back 或 span 单位表示",
        "效应量用 Cohen's d 或 η²",
        "认知评分用标准分或百分位表示",
        "统计检验注明 α=0.05 与多重比较校正方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("PsychoPy", "OpenSesame", "E-Prime", "MATLAB", "SPSS", "R (RStudio)", "JASP", "Excel", "CogniFit", "Lumosity", "BrainHQ", "n-back Task Software", "Corsi Block-Tapping", "Dual N-Back", "Flanker Task", "Stroop Task", "Go/No-Go Task", "Digit Span", "Wechsler Intelligence Scales", "Nback Task"),
    category="理学",
    databases=("PubMed", "OpenAlex", "Crossref", "PsycINFO"),
)
