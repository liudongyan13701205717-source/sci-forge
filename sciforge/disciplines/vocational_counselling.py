"""职业辅导学科论文支持：职业评估/咨询/干预研究体裁、APA 7 引用与心理度量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vocational_counselling",
    aliases=("vocational counselling", "职业辅导", "职业咨询", "career counselling",
             "职业指导", "career guidance", "职业心理", "vocational psychology"),
    paper_types={
        "research": (
            "structured abstract",
            "introduction（职业问题与研究假设）",
            "methods（设计、对象、测评工具、干预）",
            "results（测评结果与干预效果）",
            "discussion（职业外推性与实践意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "client presentation（来访者描述）",
            "assessment and intervention（评估与干预）",
            "results（干预效果与反思）",
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
    citation_style="APA 7（心理学/教育学常用）",
    reporting_standards={
        "research": "心理测量报告规范（SPPM 报告标准）",
        "case_study": "CASE 案例报告规范",
        "systematic_review": "PRISMA",
        "intervention": "CONSORT 或 TIDieR",
    },
    conventions=(
        "伦理规范：知情同意、保密原则、来访者权益保护",
        "测评工具须给信度、效度与标准化依据",
        "干预方案须给具体步骤、频次与执行者资质",
        "效果指标须预先定义（如职业认同感、求职效能感）",
        "研究须通过伦理委员会审查",
    ),
    key_venues=(
        "Journal of Counseling Psychology",
        "Journal of Vocational Behavior",
        "Career Development International",
        "Journal of Career Assessment",
        "Frontiers in Psychology",
    ),
    units_and_formulas_notes=(
        "心理测评给标准化分数（T 分或 Z 分）并注明常模",
        "效度给内容效度、效标效度与结构效度",
        "信度给 Cronbach's α 或 ICC",
        "效应量给 Cohen's d 或 η² 并注明 95% CI",
        "样本量给功效分析参数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "MATLAB", "职业测评系统", "职业心理测评系统", "职业兴趣测评系统", "职业能力测评系统", "职业性格测评系统", "职业认知测评系统", "职业动机测评系统", "职业价值观测评系统", "职业适应力测评系统", "职业幸福感测评系统", "职业倦怠测评系统", "职业压力测评系统", "职业满意度测评系统", "职业认同感测评系统", "求职效能感测评系统", "职业规划测评系统", "职业决策系统"),
    category="教育学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
