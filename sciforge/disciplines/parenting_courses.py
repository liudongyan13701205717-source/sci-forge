"""育儿课程学科论文支持：家长教育、儿童教养与家庭支持课程研究体裁、课程干预效应量报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="parenting_courses",
    aliases=(
        "parenting_courses",
        "育儿课程",
        "Parenting Courses",
        "家长教育",
        "Parent Education",
        "Parenting Programs",
        "儿童教养研究",
        "家庭支持课程",
        "parent education program"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references"
        ),
    },
    citation_style="APA 第7版",
    reporting_standards={
        "k1": "课程评估研究遵循教育干预研究规范",
        "k2": "家长报告问卷须报告信度与效度",
        "k3": "质性研究遵循 COREQ/SRQR 报告规范"
    },
    conventions=(
        "家长与儿童数据须匿名化并脱敏处理",
        "涉及未成年人研究须报告伦理批准与监护人同意",
        "课程效果评估须报告对照组与效应量",
        "教养量表须报告信效度与使用版本",
        "结论须区分短期课程效果与长期结果"
    ),
    key_venues=(
        "Parenting: Children and Adolescents",
        "Family Relations",
        "Journal of Marriage and Family",
        "Journal of Child and Family Studies",
        "Early Child Development and Care"
    ),
    units_and_formulas_notes=(
        "儿童年龄以月龄或岁报告并注明是否校正胎龄",
        "课程频次以周次数与课时数报告",
        "效应量须报告 Cohen's d 与 95% 置信区间",
        "家长报告须注明自评与教师报告来源"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Strengthening Families Program (SFP)", "Triple P（Parenting Program）", "Incredible Years (IY)", "Parents as Teachers (PAT)", "Nurse-Family Partnership (NFP)", "Parenting Styles Questionnaire", "HOME（家庭环境评定量表）", "Child Behavior Checklist (CBCL)", "Strengths and Difficulties Questionnaire (SDQ)", "BITSEA（婴幼儿社交情感评估）", "Early Developmental Inventory (EDI)", "Parenting Scale (PS)", "Parental Beliefs Scale", "家长访谈提纲", "Zoom", "Google Forms", "NVivo", "MAXQDA", "SPSS", "R"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
