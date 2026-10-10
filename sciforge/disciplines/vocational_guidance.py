"""职业指导学科论文支持：职业指导/教育干预研究体裁、APA 7 引用与教育度量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vocational_guidance",
    aliases=("vocational guidance", "职业指导", "职业规划", "career guidance",
             "职业教育指导", "职业发展方向", "career planning", "employment guidance"),
    paper_types={
        "research": (
            "structured abstract",
            "introduction（指导问题与研究假设）",
            "methods（设计、对象、指导内容、效果评估）",
            "results（指导效果与就业结果）",
            "discussion（指导外推性与教育意义）",
            "references",
        ),
        "program_evaluation": (
            "abstract",
            "introduction",
            "program description（项目描述）",
            "implementation（实施过程）",
            "results（项目效果）",
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
    citation_style="APA 7（教育学常用）",
    reporting_standards={
        "research": "教育研究报告规范（ERIC 标准）",
        "program_evaluation": "CIPP 模型",
        "systematic_review": "PRISMA",
        "intervention": "CONSORT 或 TIDieR",
    },
    conventions=(
        "伦理规范：知情同意、保密原则、学生权益保护",
        "指导内容须给具体方案、频次与执行者资质",
        "效果指标须预先定义（如就业率、职业满意度）",
        "测评工具须给信度、效度与标准化依据",
        "研究须通过伦理委员会审查",
    ),
    key_venues=(
        "Journal of Career Development",
        "Review of Educational Research",
        "Educational Researcher",
        "Journal of Vocational and Technical Education",
        "Career Development Quarterly",
    ),
    units_and_formulas_notes=(
        "就业率给 % 并注明统计口径",
        "职业满意度给 Likert 5 点量表得分",
        "指导时长给 小时或 学时",
        "效果量给 Cohen's d 或 η² 并注明 95% CI",
        "样本量给功效分析参数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "MATLAB", "职业指导系统", "职业规划系统", "职业测评系统", "职业心理测评系统", "职业兴趣测评系统", "职业能力测评系统", "职业性格测评系统", "职业认知测评系统", "职业动机测评系统", "职业价值观测评系统", "职业适应力测评系统", "职业幸福感测评系统", "职业倦怠测评系统", "职业压力测评系统", "职业满意度测评系统", "职业认同感测评系统", "求职效能感测评系统"),
    category="教育学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
