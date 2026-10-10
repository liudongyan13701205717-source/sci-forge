"""谈话治疗学科论文支持：心理治疗/认知行为疗法体裁、APA 引用样式与临床写作约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="conversational_therapy",
    aliases=(
        "谈话治疗", "对话治疗", "心理治疗", "Conversational therapy",
        "Conversational Therapy", "Psychotherapy", "Talk therapy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "case_report": (
            "摘要",
            "案例介绍",
            "评估与诊断",
            "治疗过程",
            "结果与讨论",
            "参考文献",
        ),
        "review": (
            "摘要",
            "引言",
            "文献综述",
            "整合与讨论",
            "结论",
            "参考文献",
        ),
    },
    citation_style="APA 第 7 版",
    reporting_standards={
        "diagnosis": "临床诊断须依据 DSM-5 或 ICD-11 标准，注明诊断版本",
        "treatment_protocol": "治疗方案须明确治疗流派、周期与频率",
        "outcome_measures": "疗效评估须报告标准化量表（如 PHQ-9、GAD-7）与效应量",
        "ethics": "涉及真实个案须获得知情同意，脱敏处理",
    },
    conventions=(
        "临床术语首次出现时给出中英文对照",
        "心理量表引用须注明版本、信度系数与常模来源",
        "个案报告须说明知情同意与脱敏处理情况",
        "疗效数据报告效应量（Cohen's d 或 Hedges' g）与置信区间",
        "引用量表须说明中文版是否经过标准化修订",
    ),
    key_venues=(
        "Journal of Consulting and Clinical Psychology",
        "British Journal of Clinical Psychology",
        "Psychotherapy Research",
        "Behaviour Research and Therapy",
        "Journal of Clinical Psychology",
        "中国临床心理学杂志",
    ),
    units_and_formulas_notes=(
        "量表评分报告原始分、标准分与 T 分数",
        "效应量报告 Cohen's d 或 Hedges' g",
        "显著性水平设定 α=0.05，多重比较校正须说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SAPAS（SAGE Adaptive Psychotherapy Assessment System）", "CBT Coach by Mind", "Mood Meter by Yeale", "PsyTrack Pro", "SPSS", "R", "SAS", "NVivo", "ATLAS.ti", "TherapyNotes", "Counseling Outcomes", "Mental Health Care Platform (MHCP)", "MindSpot", "CogniFit", "Psychometrics Software (PSI)", "Q-Global Assessment", "Mental Health Toolkit (MHT)", "PsyTrack for Therapists", "Clinical Outcomes in Psychotherapy (COP)", "Psychotherapy Data Analyzed System (PDAS)"),
    category="医学",
    databases=("PubMed", "PsycINFO", "Scopus", "OpenAlex", "中国知网"),
)
