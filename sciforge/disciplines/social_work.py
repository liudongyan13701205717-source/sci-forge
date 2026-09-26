"""社会工作学科论文支持：干预/个案/社区体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_work",
    aliases=("social_work", "社会工作", "社会福利", "社会服务"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "theory（理论框架）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "intervention_study": (
            "abstract",
            "introduction",
            "intervention design（干预设计）",
            "participants（参与者）",
            "measures（测量）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case presentation（个案呈现）",
            "intervention（干预过程）",
            "evaluation（评估）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Social Work 遵循 APA 规范）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "case_study": "个案研究遵循案例研究报告规范",
        "randomized_trial": "随机对照试验遵循 CONSORT 声明",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "伦理审批与知情同意须报告",
        "干预手册化与保真度须说明",
        "测量工具须注明信效度",
        "样本流失须报告",
        "实践启示须讨论",
    ),
    key_venues=(
        "Social Work",
        "Social Work Research",
        "Journal of Social Work Education",
        "British Journal of Social Work",
        "Research on Social Work Practice",
        "Child & Family Social Work",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量用 Cohen's d 或 η²",
        "量表分数给出范围与信度",
        "样本量须报告",
        "百分比给出基数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告"),
    tools=("SPSS", "NVivo（质性编码）", "心理测量与量表分析软件", "Stata", "AMOS（结构方程模型）"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)