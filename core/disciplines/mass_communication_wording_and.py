"""大众传播与写作学科论文支持：传播、媒介、文本与话语分析体裁、APA 与社科统计注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mass_communication_wording_and",
    aliases=("mass_communication_wording_and", "大众传播与写作", "大众传播", "传播学",
             "Mass Communication", "Communication Studies", "Media Studies", "媒介研究",
             "新闻与传播"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究动机）",
            "literature review（文献综述）",
            "theory and hypotheses（理论与假设）",
            "study design（研究设计：内容/问卷/实验/民族志）",
            "data（数据与样本）",
            "results（结果与统计分析）",
            "discussion（讨论与实务启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（媒介/事件/机构描述）",
            "analysis（分析与理论对话）",
            "results（关键发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（传播理论综述）",
            "evidence synthesis（跨研究证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（传播学主流，芝加哥风格备选）",
    reporting_standards={
        "survey": "调查须遵循 AAPOR 报告规范",
        "experiment": "实验研究须遵循实验报告规范与预注册",
        "qualitative": "质性研究须遵循 COREQ/SRQR",
        "content_analysis": "内容分析须遵循 Krippendorff 编码信度报告",
        "ethics": "涉受众隐私须遵循 GDPR/所在国个人信息保护法",
    },
    conventions=(
        "样本量须报告 N、抽样方法与响应率",
        "量表与信度须报告 Cronbach's α",
        "统计检验须报告 p、效应量与置信区间",
        "引用文本须注明作者、年份、媒介与页码",
        "编码信度须报告 Cohen's κ 或 Krippendorff's α",
    ),
    key_venues=(
        "Journal of Communication",
        "Communication Studies",
        "New Media & Society",
        "Journal of Communication Inquiry",
        "Public Opinion Quarterly",
        "International Journal of Communication",
    ),
    units_and_formulas_notes=(
        "均值 M、标准差 SD、标准误 SE 须报告",
        "效应量：Cohen's d、η²、Cohen's f",
        "编码信度：Cohen's κ、Krippendorff's α",
        "传播指标：覆盖率、接触率、到达率、传播深度",
        "金额单位：统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("SPSS", "R（lavaan/tidyverse）", "Python（pandas/scikit-learn）", "NVivo（质性分析）", "MAXQDA", "Tableau / Power BI", "Mplus", "AMOS", "Stata", "在线调研平台（Qualtrics/Typeform）", "SurveyMonkey / 问卷星", "内容分析工具（NVivo/ATLAS.ti）", "文本分析工具（R/Python/LLM）", "网络爬虫（Scrapy/BeautifulSoup）", "社交媒体分析（Brandwatch/Meltwater）", "受众研究工具（Nielsen/Kantar）", "眼动仪（Tobii）", "采访录音与转录（Otter.AI/Adobe Podcast）", "写作与编辑工具（Grammarly/Trinket）", "文献管理（Zotero/Mendeley）"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "ProQuest"),
)
