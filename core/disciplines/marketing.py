"""市场营销学科论文支持：消费者/品牌/渠道体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="marketing",
    aliases=("marketing", "市场营销", "营销学", "消费者行为", "品牌管理",
             "Marketing", "Consumer Behavior", "Brand Management", "品牌营销", "数字营销"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究动机）",
            "theory and hypotheses（理论与假设）",
            "study design（研究设计）",
            "data（数据与样本）",
            "results（结果与统计分析）",
            "discussion（讨论与实务启示）",
            "references",
        ),
        "experimental_study": (
            "abstract",
            "introduction",
            "study 1（研究一）",
            "study 2（研究二）",
            "general discussion（总体讨论）",
            "references",
        ),
        "field_study": (
            "abstract",
            "introduction",
            "field setting（现场设置）",
            "data（数据）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份制，Journal of Marketing 遵循）",
    reporting_standards={
        "experimental": "实验研究须遵循实验报告规范与预注册",
        "survey": "调查须遵循 AAPOR 报告规范（SSG/SGA）",
        "field_study": "现场研究须遵循现场实验报告规范",
        "qualitative": "质性研究须遵循 COREQ/SRQR",
        "meta_analysis": "元分析须遵循 PRISMA 声明",
    },
    conventions=(
        "理论与假设须明确",
        "刺激材料与操纵检验须报告",
        "构念测量须注明信效度",
        "样本与招募须说明",
        "效应量与显著性须报告",
    ),
    key_venues=(
        "Journal of Marketing",
        "Journal of Marketing Research",
        "Journal of Consumer Research",
        "Marketing Science",
        "Journal of the Academy of Marketing Science",
        "Journal of Consumer Psychology",
    ),
    units_and_formulas_notes=(
        "均值 M、标准差 SD、标准误 SE 须报告",
        "效应量：Cohen's d、η²、Cohen's f",
        "信度：Cronbach's α；效度：AVE、CR",
        "相关性：Pearson r、Spearman ρ",
        "金额单位：统一币种并注明年份与汇率",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R（lavaan/tidyverse）", "Python（pandas/scikit-learn）", "Tableau（销售与漏斗可视化）", "AMOS", "Mplus", "Stata", "NVivo（质性分析）", "SurveyMonkey / Typeform", "Qualtrics", "在线调研平台（问卷星）", "A/B 测试（Optimizely）", "CRM 数据（Salesforce/HubSpot）", "Marketing Mix Modeling（Nintex）", "文本挖掘（NLP/LLM）", "网络爬虫（Scrapy）", "大数据分析平台（Google Analytics）", "广告平台 API（Meta/Google Ads）", "定价与优化（Monte Carlo）", "客户旅程分析（Salesforce Journey Builder）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "Google Scholar"),
)
