"""酒精与药物滥用咨询学科论文支持：咨询、成瘾治疗与干预研究体裁及 APA 记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="alcohol_and_drug_abuse_counselling",
    aliases=(
        "alcohol and drug abuse counselling",
        "酒精与药物滥用咨询",
        "addiction counselling",
        "substance abuse counselling",
        "药物滥用咨询",
        "addiction therapy",
        "成瘾咨询",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题、动机与目标）",
            "methods（干预方案、采样与评估工具）",
            "results（疗效、复发率与随访结果）",
            "discussion（与循证实践对比与局限）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "case presentation",
            "assessment",
            "intervention",
            "outcomes and discussion",
            "references",
        ),
    },
    citation_style="APA 7 样式（DSM-5-TR/ICD-11 分类须准确引用）",
    reporting_standards={
        "intervention_report": "干预方案须遵循 SAMHSA 或 WHO 循证实践标准",
        "outcome_measures": "疗效评估须给出工具信度（如 AUDIT-C、CCI）、随访时长与流失率",
        "ethics": "研究伦理与知情同意须披露，涉及青少年/孕妇等敏感群体须注明额外保护",
        "cultural_context": "跨文化干预须注明文化适应与本地化情况",
    },
    conventions=(
        "干预方案须遵循 SAMHSA 或 WHO 循证实践标准（如 NIDA、SAMHSA TIPS）并准确引用版本",
        "疗效评估须给出工具信度（如 AUDIT、AUDIT-C、DAST）、随访时长与流失率",
        "研究伦理与知情同意须披露，涉及青少年/孕妇等敏感群体须注明额外保护",
        "跨文化干预须注明文化适应与本地化情况（如本土化干预方案与翻译验证）",
        "复发率须按 SAMHSA 或 WHO 定义报告（如 30 天/60 天/90 天）",
    ),
    key_venues=(
        "Addictive Behaviors",
        "Drug and Alcohol Dependence",
        "Journal of Studies on Alcohol and Drugs",
        "Substance Use & Misuse",
        "Addiction",
        "Journal of Substance Abuse Treatment",
        "Journal of Consulting and Clinical Psychology",
        "Clinical Psychology Review",
    ),
    units_and_formulas_notes=(
        "饮酒量按 AUDIT 或 NIAAA 定义（如 1 标准杯/日、每周饮酒次数）",
        "吸毒量按 WHO 或 SAMHSA 定义（如克/日、次/周、次/月）",
        "随访时长以天/周/月为单位，报告 30/60/90 天复发率",
        "疗效指数（如 effect size, Cohen's d）须按 APA 6/7 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "专利", "教案与教材", "报告", "数据集"),
    tools=("PHQ-9", "GAD-7", "AUDIT", "DAST", "SIPS", "MI Spirit", "MI Watch", "SMART Recovery", "SAMHSA", "NIDA", "NIDA Quickset", "Matrix Model", "Seeking Safety", "MAT", "Relapse Prevention", "Motivational Enhancement Therapy", "CBT", "DBT", "ACT", "MBI"),
    category="教育学",
    databases=("PubMed", "OpenAlex", "Crossref", "SAMHSA", "NIDA"),
)
