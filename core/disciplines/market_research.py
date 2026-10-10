"""市场研究学科论文支持：问卷、实验、访谈与消费者行为体裁、APA 与社会科学统计注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="market_research",
    aliases=("market_research", "市场研究", "市场调研", "消费者研究", "消费者行为研究",
             "Market Research", "Consumer Research", "Consumer Behavior", "市场调查研究",
             "商业洞察"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究动机）",
            "theory and hypotheses（理论与假设）",
            "study design（研究设计：问卷/实验/访谈）",
            "data collection（数据采集与样本）",
            "results（结果与统计分析）",
            "discussion（讨论与实务启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（企业/品牌/产品描述）",
            "analysis（方法、发现与决策）",
            "results（关键指标）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（方法与理论综述）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（社科主流，作者-年份制）",
    reporting_standards={
        "survey": "问卷调查须遵循 AAPOR 报告规范（SSG/SGA）",
        "experiment": "实验研究须遵循实验报告规范与预注册",
        "qualitative": "质性研究须遵循 COREQ/SRQR",
        "meta_analysis": "元分析须遵循 PRISMA 声明",
        "ethics": "涉消费者隐私须遵循 GDPR/所在国个人信息保护法",
    },
    conventions=(
        "样本量须报告 N、抽样方法与响应率",
        "量表与信度须报告 Cronbach's α",
        "构念测量须注明效度与因子结构",
        "统计检验须报告 p、效应量与置信区间",
        "问卷与访谈提纲须附在附录",
    ),
    key_venues=(
        "Journal of Marketing Research",
        "Journal of Consumer Research",
        "Marketing Science",
        "Journal of Marketing",
        "Journal of Business Research",
        "European Journal of Marketing",
    ),
    units_and_formulas_notes=(
        "均值 M、标准差 SD、标准误 SE 须报告",
        "效应量：Cohen's d、η²、Cohen's f",
        "相关性：Pearson r、Spearman ρ",
        "信度：Cronbach's α；效度：AVE、CR",
        "金额单位：统一币种并注明年份与汇率",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "AMOS", "Mplus", "R（lavaan/tidyverse）", "Python（pandas/scikit-learn）", "Stata", "NVivo（质性分析）", "MAXQDA", "SurveyMonkey / Typeform", "Qualtrics", "在线调研平台（问卷星/WJX）", "焦点小组工具（Zoom/Teams）", "眼动仪（Tobii）", "行为实验室", "大数据与文本挖掘（Kaggle）", "网络爬虫（Scrapy/BeautifulSoup）", "A/B 测试平台（Optimizely）", "CRM 数据（Salesforce/HubSpot）", "统计可视化（Tableau/Power BI）", "AI 辅助分析（LLM/ChatGPT）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "Google Scholar"),
)
