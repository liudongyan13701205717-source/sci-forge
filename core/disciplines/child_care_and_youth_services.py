"""儿童保育与青少年服务学科论文支持：儿童福利、青年发展与服务评估规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="child_care_and_youth_services",
    aliases=(
        "child care and youth services", "儿童保育与青少年服务",
        "儿童与青少年服务", "青少年服务",
        "child and youth services", "youth services",
        "youth development", "青少年发展",
        "儿童福利", "儿童权益保护",
        "child welfare", "child protection",
        "child safeguarding", "儿童保护",
        "social work children", "儿童社会工作",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methodology",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "case study": (
            "abstract",
            "background",
            "case description",
            "analysis",
            "conclusion",
            "references",
        ),
        "program evaluation": (
            "abstract",
            "program description",
            "evaluation framework",
            "results",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "observation": "观察记录遵循观察报告规范",
        "intervention": "干预研究遵循 PRECIS-2 报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethical": "涉及儿童数据遵循伦理审查与知情同意规范",
    },
    conventions=(
        "涉及儿童数据须匿名化或化名处理",
        "干预/服务方案明确目标群体、实施路径与评估指标",
        "引用儿童权益须注明法律与政策依据",
        "评估量表须注明版本、来源与信度效度",
        "伦理审查编号须在文首声明",
    ),
    key_venues=(
        "Children and Youth Services Review",
        "Child Abuse & Neglect",
        "Journal of Child and Family Studies",
        "Youth Services Quarterly",
        "Journal of Adolescent Research",
        "Journal of Child Abuse and Neglect",
        "Child & Youth Care Forum",
        "儿童与青少年服务研究",
    ),
    units_and_formulas_notes=(
        "年龄用月龄/周岁表示；干预组别须明确",
        "服务频次/时长以次、小时/周记录",
        "量表得分给出原始分、标准化分与百分位",
        "统计检验与效应量须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Bayley IV 婴儿发育量表", "Bayley Scales of Infant Development III", "Denver II Developmental Screening Test", "Gesell Developmental Schedules", "ASQ-3 (Ages & Stages Questionnaires)", "DDST-II Developmental Screening Test", "MacArthur-Bates CDI", "M-CHAT-R/F 自闭症筛查", "Vineland Adaptive Behavior Scales", "Pediatric Symptom Checklist (PSC-17)", "Strengths and Difficulties Questionnaire (SDQ)", "Child Behavior Checklist (CBCL)", "Youth Self-Report (YSR)", "Parenting Behavior Inventory (PBI)", "Parenting Scale (PS)", "Home Environment Scale (HOME)", "Family Environment Scale (FES)", "Family Adaption and Cohesion Tool (FACES III)", "Family Assessment Device (FAD)", "Childhood Trauma Questionnaire (CTQ)", "Child Abuse Potential Inventory (CAP)", "Child Abuse Potential Inventory (CATI)", "Child Protection Questionnaire (CPQ)", "Child Youth Mental Health Assessment (CYHMS)", "Child Youth Mental Health Assessment Center", "Kidography (儿童观察记录)", "Kidography Developmental Assessment", "Kidography Digital Assessment (KDA)", "Child Trends Database", "CDC Youth Risk Behavior Surveillance System (YRBSS)", "Child Protective Services (CPS) 报告系统", "Youth Bulging Surveillance System", "Youth Bullying Prevention Network", "Youth Suicide Prevention Database", "Youth Violence Surveillance System", "Youth Bullying and Suicide Prevention Database", "Youth Suicide Risk Assessment (SASQ)", "Youth Risk Behavior Surveillance (YRBS)", "Youth Suicide and Self-Injury Risk Assessment (SIRS)", "Youth Bullying Prevention Database", "Child Trends Research Center", "Youth Bullying Prevention Research Center", "Youth Bullying and Suicide Prevention Research Center", "Kidography Digital Assessment"),
    category="教育学",
    databases=("ERIC", "PubMed", "CNKI", "万方", "OpenAlex", "Web of Science"),
)
