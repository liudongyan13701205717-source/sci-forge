"""自尊技能学科论文支持：自尊量表与技能型干预（认知重构/元认知训练）体裁、APA 引用样式与心理测量学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="selfesteem_skills",
    aliases=("selfesteem_skills", "self-esteem skills", "自尊技能", "自尊训练",
             "self-esteem training", "self-worth", "self-worth skills"),
    paper_types={
        "research": (
            "abstract",
            "introduction（自尊构念与技能型干预动机）",
            "methods（技能模块与实施流程）",
            "results（前测/后测与随访）",
            "discussion（技能机制与迁移性）",
            "references",
        ),
        "intervention_study": (
            "abstract",
            "introduction",
            "intervention design（技能课程结构）",
            "methods（被试、随机化与盲法）",
            "results（效应量与异质性分析）",
            "discussion（推广性与局限）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（自尊发展谱系）",
            "evidence synthesis（技能型干预证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份，临床与教育心理学主流）",
    reporting_standards={
        "intervention": "技能型干预遵循 CONSORT 或 SPIRIT 声明并注册临床试验",
        "measurement": "自尊量表（Rosenberg、Coopersmith）须报告信度与 CFA 拟合",
        "systematic_review": "系统综述遵循 PRISMA 与 Cochrane 手册",
    },
    conventions=(
        "区分状态性自尊（state）与特质性自尊（trait）并分别报告",
        "技能模块须明确认知重构、正念、行为激活等核心成分",
        "干预依从性须报告（完成率、缺席、脱落）",
        "报告效应量（d、g）与随访时间点（1/3/6/12 个月）",
        "被试特征、共病与人口学变量须完整披露",
    ),
    key_venues=(
        "Journal of Adolescence",
        "Clinical Psychology Review",
        "Journal of Counseling Psychology",
        "Psychological Bulletin",
        "Journal of Child and Family Studies",
    ),
    units_and_formulas_notes=(
        "量表分用 Likert 1-4 或 1-5；Rosenberg 10 项报告总分与因子分",
        "效应量用 Cohen's d、Hedges' g；95% CI 用 bootstrapping",
        "随访数据用混合效应模型（lme4/mixedModels）处理缺失",
        "样本量按 power ≥ .80 与 α = .05 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "RStudio", "Microsoft Excel", "Qualtrics", "NVivo", "Mplus", "SmartPLS", "JASP", "Jamovi", "Stata", "Python（pandas/NumPy）", "REDCap", "Google Forms", "SurveyMonkey", "RevMan", "IDLab", "PsychoPy", "OpenSesame", "OSF"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
