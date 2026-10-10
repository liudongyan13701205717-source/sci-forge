"""咨询学科论文支持：心理咨询/心理健康服务体裁、APA 引用样式与咨询研究约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="counselling",
    aliases=(
        "咨询", "心理咨询", "辅导", "Counselling",
        "Counseling", "Psychological Counselling", "心理健康辅导",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "case_study": (
            "案例摘要",
            "来访者背景",
            "评估与诊断",
            "咨询过程",
            "结果与讨论",
            "伦理讨论",
        ),
        "systematic_review": (
            "摘要",
            "引言",
            "方法",
            "结果",
            "讨论",
            "参考文献",
        ),
    },
    citation_style="APA 第 7 版",
    reporting_standards={
        "diagnosis": "临床诊断须依据 DSM-5 或 ICD-11",
        "ethical_standards": "须遵循咨询伦理准则（如 ACA/AACCP 伦理守则）",
        "outcome_measures": "咨询效果须使用标准化量表评估（如 PHQ-9、GAD-7）",
        "competence": "咨询师资格须说明（注册咨询心理学家等）",
    },
    conventions=(
        "来访者信息须完全脱敏，使用化名或代号",
        "量表引用须注明版本、信度系数与常模来源",
        "咨询流派须明确标注（如 CBT、人本主义、精神动力等）",
        "知情同意与保密原则须在方法部分说明",
        "研究须通过伦理委员会审查并标注审查编号",
    ),
    key_venues=(
        "Journal of Counseling Psychology",
        "The Counseling Psychologist",
        "British Journal of Guidance and Counselling",
        "Counselling and Psychotherapy Research",
        "Journal of Counseling and Development",
        "中国临床心理学杂志",
    ),
    units_and_formulas_notes=(
        "量表评分报告原始分与标准分",
        "效应量报告 Cohen's d 或 Hedges' g",
        "显著性水平设定 α=0.05",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Mental Health Care Platform (MHCP)", "MindSpot（心理健康平台）", "CogniFit（认知训练软件）", "CBT Coach by Mind（认知行为治疗教练）", "SAPAS（心理治疗评估系统）", "Mood Meter by Yeale（情绪管理工具）", "PsyTrack Pro（心理跟踪系统）", "TherapyNotes（咨询记录系统）", "Counseling Outcomes（咨询效果评估）", "SPSS", "R（统计分析）", "SAS", "NVivo（质性分析）", "ATLAS.ti", "Q-Global Assessment（心理评估工具）", "Mental Health Toolkit (MHT)", "Psychotherapy Data Analyzed System (PDAS)", "Clinical Outcomes in Psychotherapy (COP)", "Google Workspace（远程咨询工具）", "Zoom（远程咨询平台）"),
    category="教育学",
    databases=("PubMed", "PsycINFO", "Scopus", "OpenAlex", "中国知网"),
)
