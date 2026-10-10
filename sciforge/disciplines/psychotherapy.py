"""心理治疗学科论文支持：疗效研究/质性体裁、APA 引用样式与治疗方案注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="psychotherapy",
    aliases=(
        "psychotherapy",
        "心理治疗",
        "Psychotherapy",
        "心理干预",
        "Psychotherapeutic intervention",
        "Cognitive behavioral therapy",
        "CBT",
        "精神分析治疗",
        "Psychoanalytic therapy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与临床问题）",
            "methodology（研究设计与样本）",
            "results（疗效与统计结果）",
            "discussion（临床意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（治疗案例描述）",
            "analysis（过程与机制分析）",
            "results（疗效结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（治疗理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；治疗手册研究遵循 APA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "qualitative": "质性研究遵循 COREQ 指南",
        "treatment_manual": "治疗手册须遵循 APA 手册报告规范",
        "implementation": "实施研究遵循 STARI 规范",
    },
    conventions=(
        "治疗流派与手册版本须注明",
        "会谈片段作为研究材料须获书面同意",
        "治疗设置（频次、时长、疗程数）须说明",
        "标准化治疗流程与偏离须记录",
        "疗效与脱落率须报告",
    ),
    key_venues=(
        "Psychotherapy Research",
        "Psychotherapy",
        "Behavior Therapy",
        "Journal of Consulting and Clinical Psychology",
        "Cognitive Therapy and Research",
    ),
    units_and_formulas_notes=(
        "量表分数无量纲，须报告量表名称与版本",
        "疗程数与频次以周计",
        "公式用 amsmath；效应量与置信区间须报告",
        "治疗联盟须报告标准化量表分数",
        "样本量与流失率须说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("CBT", "DBT", "EMDR", "ACT", "Schema Therapy", "Psychodynamic Psychotherapy", "CBT for Insomnia", "CBT for Depression", "CBT for Anxiety", "CBT for Eating Disorders", "Psychodynamic Interpersonal Therapy", "Psychodynamic Supportive Therapy", "Therapy Manually System", "Therapy Outcome Measures", "Treatment Alliance Inventory", "PHQ-9", "GAD-7", "HAM-D", "SCL-90", "Recording System"),
    category="理学",
    databases=("OpenAlex", "Crossref", "PubMed", "CNKI"),
)
