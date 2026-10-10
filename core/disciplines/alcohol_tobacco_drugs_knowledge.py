"""酒精烟草药物知识学科论文支持：预防教育、健康素养与流行病学体裁及 WHO 记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="alcohol_tobacco_drugs_knowledge",
    aliases=(
        "alcohol tobacco drugs knowledge",
        "酒精烟草药物知识",
        "substance use education",
        "tobacco prevention education",
        "drug education",
        "药物滥用预防教育",
        "成瘾预防",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题、动机与目标）",
            "methods（教育干预、采样与评估工具）",
            "results（健康知识、态度与行为变化）",
            "discussion（与循证实践对比与局限）",
            "conclusion",
            "references",
        ),
        "epidemiological_report": (
            "背景",
            "方法",
            "结果",
            "讨论",
            "结论",
            "参考文献",
        ),
    },
    citation_style="APA 7 或 Vancouver 样式（WHO/ICD-11 分类须准确引用）",
    reporting_standards={
        "educational_intervention": "教育干预须遵循 WHO 循证实践标准（如 MPOWER、TIPS）并准确引用版本",
        "outcome_measures": "健康知识评估须给出工具信度（如 KAP 量表）、样本量与流失率",
        "epidemiology": "流行病学研究须遵循 STROBE 或 TREND 报告标准",
        "cultural_context": "跨文化预防须注明文化适应与本地化情况",
    },
    conventions=(
        "教育干预须遵循 WHO 循证实践标准（如 MPOWER、TIPS、I-CHANGE）并准确引用版本",
        "健康知识评估须给出工具信度（如 KAP 量表）、样本量与流失率",
        "流行病学研究须遵循 STROBE 或 TREND 报告标准，按 WHO GATS 或 ICD-11 分类",
        "跨文化预防须注明文化适应与本地化情况（如本土化干预方案与翻译验证）",
        "预防干预效果须按 WHO 或 SAMHSA 定义报告（如 30/60/90 天/1 年）",
    ),
    key_venues=(
        "Drug and Alcohol Dependence",
        "Addictive Behaviors",
        "Drug and Alcohol Review",
        "Journal of Studies on Alcohol and Drugs",
        "Preventive Medicine",
        "Addictive Behaviors Supplement",
        "中国药物依赖性杂志",
        "中国临床心理学杂志",
    ),
    units_and_formulas_notes=(
        "饮酒量按 AUDIT 或 NIAAA 定义（如 1 标准杯/日、每周饮酒次数）",
        "吸毒量按 WHO 或 SAMHSA 定义（如克/日、次/周、次/月）",
        "健康知识评估按 KAP 量表（Knowledge, Attitude, Practice）报告",
        "流行病学数据按 WHO GATS 或 ICD-11 分类",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "专利", "教案与教材", "报告", "数据集"),
    tools=("WHO FCTC", "WHO MPOWER", "WHO GATS", "WHO Tobacco Atlas", "WHO World Health Report", "WHO World Health Survey", "SAMHSA", "NIDA", "WHO Substance Use Disorder", "WHO Mental Health", "WHO Substance Abuse", "WHO Tobacco", "WHO Alcohol", "WHO Drugs", "WHO Prevention", "KAP", "AUDIT", "WHO 60-60", "WHO Health", "WHO Health Promotion"),
    category="教育学",
    databases=("WHO", "OpenAlex", "Crossref", "PubMed", "SAMHSA", "NIDA"),
)
