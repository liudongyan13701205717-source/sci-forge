"""市场营销与广告学科论文支持：广告创意、媒介、传播与消费者反应体裁、APA 与媒介计量注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="marketing_and_advertising",
    aliases=("marketing_and_advertising", "市场营销与广告", "营销与广告", "广告学",
             "Marketing and Advertising", "Advertising", "Marketing and Communication",
             "品牌传播", "整合营销传播"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究动机）",
            "theory and hypotheses（理论与假设）",
            "study design（研究设计：创意/媒介/现场）",
            "data（数据与样本）",
            "results（结果与统计分析）",
            "discussion（讨论与实务启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（品牌/广告/媒介描述）",
            "analysis（策略、执行与效果）",
            "results（关键指标与回报）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（创意、媒介与传播综述）",
            "evidence synthesis（跨研究证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（社科主流，广告学常用）",
    reporting_standards={
        "experimental": "实验研究须遵循实验报告规范与预注册",
        "survey": "调查须遵循 AAPOR 报告规范（SSG/SGA）",
        "field_study": "现场与媒介研究须遵循现场实验报告规范",
        "qualitative": "质性研究须遵循 COREQ/SRQR",
        "ethics": "涉媒介数据与消费者隐私须遵循 GDPR/所在国隐私法规",
    },
    conventions=(
        "样本量须报告 N、抽样方法与响应率",
        "广告刺激材料须附完整文本或截图",
        "量表与信度须报告 Cronbach's α",
        "统计检验须报告 p、效应量与置信区间",
        "媒介指标须注明曝光、点击、转化定义与统计窗口",
    ),
    key_venues=(
        "Journal of Advertising",
        "Journal of Advertising Research",
        "Journal of Marketing",
        "Journal of Consumer Research",
        "Journal of Advertising & Society",
        "International Journal of Advertising",
    ),
    units_and_formulas_notes=(
        "媒介指标：曝光量（Impressions）、点击率 CTR、转化率 CVR",
        "ROI = (净收入 - 广告支出) / 广告支出",
        "CPM = (广告成本 / 展示数) × 1000",
        "CAC = 广告成本 / 新客数；LTV = 客户终身价值",
        "均值 M、标准差 SD 须报告；效应量：Cohen's d",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R（lavaan/tidyverse）", "Python（pandas/scikit-learn）", "Tableau / Power BI", "AMOS", "NVivo（质性分析）", "Qualtrics", "SurveyMonkey / Typeform", "Google Analytics", "Google Ads / Meta Ads", "广告创意工具（Adobe Creative Cloud）", "视频制作（Premiere Pro/Final Cut）", "3D 建模（Cinema 4D/Blender）", "眼动仪（Tobii）", "A/B 测试（Optimizely）", "媒介计划工具（MediaMath）", "广告技术（AdTech）平台", "文本与情感分析（NLP/LLM）", "CRM 数据（Salesforce/HubSpot）", "品牌追踪（Kantar/GfK）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "Google Scholar"),
)
