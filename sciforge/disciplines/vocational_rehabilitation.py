"""职业康复学科论文支持：职业康复评估/干预研究体裁、Vancouver 引用与康复度量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vocational_rehabilitation",
    aliases=("vocational rehabilitation", "职业康复", "职业康复医学",
             "rehabilitation medicine", "康复治疗", "disability rehabilitation",
             "职业功能恢复", "workplace rehabilitation"),
    paper_types={
        "research": (
            "structured abstract",
            "introduction（康复问题与研究假设）",
            "methods（设计、对象、评估工具、干预方案）",
            "results（康复效果与功能恢复）",
            "discussion（康复外推性与临床意义）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction",
            "patient presentation（患者描述）",
            "assessment and intervention（评估与干预）",
            "results（康复效果与反思）",
            "discussion",
            "references",
        ),
        "systematic_review": (
            "structured abstract",
            "introduction",
            "methods（PICO、检索、纳排、偏倚评估）",
            "results（森林图、GRADE 证据等级）",
            "discussion",
            "references",
        ),
    },
    citation_style="Vancouver（J Rehabil Med 体例，按引用顺序编号）",
    reporting_standards={
        "case_report": "CARE",
        "cohort": "STROBE",
        "systematic_review": "PRISMA",
        "randomized_trial": "CONSORT",
        "functional": "ICF 框架报告规范",
    },
    conventions=(
        "伦理规范：知情同意、保密原则、患者权益保护",
        "康复评估须遵循 ICF 框架（身体/活动/参与）",
        "干预方案须给具体步骤、频次与执行者资质",
        "效果指标须预先定义（如就业能力、生活质量）",
        "研究须通过伦理委员会审查",
    ),
    key_venues=(
        "Journal of Rehabilitation Medicine",
        "Archives of Physical Medicine and Rehabilitation",
        "Disability and Rehabilitation",
        "Journal of Vocational Rehabilitation",
        "Clinical Rehabilitation",
    ),
    units_and_formulas_notes=(
        "康复量表给标准化分数（0-100 或 0-5）并注明刻度",
        "就业能力给 % 就业或 FTE 就业率",
        "康复时长给 周或 个月",
        "效果量给 Cohen's d 或 η² 并注明 95% CI",
        "生活质量给 QoL 得分并注明评估工具",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "MATLAB", "职业康复评估系统", "职业康复训练系统", "职业康复测评系统", "职业康复心理辅导系统", "职业康复职业适应系统", "职业康复职业恢复系统", "职业康复职业再就业系统", "职业康复职业培训系统", "职业康复职业咨询系统", "职业康复职业辅导系统", "职业康复职业评估系统", "职业康复职业反馈系统", "职业康复职业报告系统", "职业康复职业管理系统", "职业康复职业监测系统", "职业康复职业适应测评", "职业康复职业功能测评"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
