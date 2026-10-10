"""职业技能学科论文支持：技能形成与职业培训研究、APA 引用样式与技能测量注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="work_skills",
    aliases=("work_skills", "职业技能", "职场技能形成", "work skills", "skills formation", "vocational skills"),
    paper_types={
        "research": (
            "abstract",
            "introduction（技能问题背景）",
            "literature review（技能研究综述）",
            "methods（方法与设计）",
            "results（结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "training_evaluation": (
            "abstract",
            "introduction",
            "training design（培训设计）",
            "implementation（实施）",
            "evaluation（评估）",
            "outcomes（结果）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and search（范围与检索）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="APA 第 7 版样式（作者-年份）",
    reporting_standards={
        "skills_assessment": "技能评估须报告工具、方法与信效度",
        "training_design": "培训设计须遵循 ADDIE/柯氏四级评估等模型",
        "skills_formation": "技能形成须明确阶段、条件与情境",
        "ethics": "研究伦理审批与知情同意须给出",
        "statistics": "统计检验与样本量须报告",
    },
    conventions=(
        "技能形成与技能掌握术语区分（formation vs mastery）",
        "技能分类遵循通用技能/专业技能/可迁移技能框架",
        "技能评估工具信效度须报告",
        "培训情境描述完整（行业、岗位、培训类型）",
        "技能迁移须明确条件与情境"
    ),
    key_venues=(
        "Journal of Vocational Behavior",
        "Journal of Vocational and Technical Education",
        "Vocational Behavior Research Journal",
        "Human Resource Development International",
        "Journal of Workplace Learning"
    ),
    units_and_formulas_notes=(
        "技能水平用李克特量表（1-5 或 1-7）",
        "培训时长用小时/周表示",
        "样本量 n 与置信区间须给出",
        "p 值用 <0.05/<0.01/<0.001 表示显著性"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Qualtrics", "SPSS", "R (lme4)", "Stata", "MPlus", "AMOS", "NVivo", "MAXQDA", "Tableau", "Power BI", "Excel", "Skills Matrix 建模工具", "Simian (VET 培训管理系统)", "T2 技能平台", "Eightfold AI Talent Intelligence", "Degreed", "Cornerstone OnDemand", "Docebo", "360Learning", "Workday Skills Cloud"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
