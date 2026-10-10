"""商务信函学科论文支持：商务沟通、公文写作、商务信函与跨文化商务文体。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="business_correspondence",
    aliases=(
        "business_correspondence",
        "商务信函",
        "商务沟通",
        "商务写作",
        "商务公文",
        "Business Correspondence",
        "Business Communication",
        "Business Writing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与研究动机）",
            "literature review",
            "methodology（语料分析/内容分析/实证调查）",
            "findings",
            "discussion",
            "conclusion",
            "references",
        ),
        "corpus_analysis": (
            "abstract",
            "introduction",
            "corpus description（语料说明）",
            "methodology",
            "findings",
            "discussion",
            "conclusion",
            "references",
        ),
        "pedagogical": (
            "abstract",
            "introduction",
            "instructional design（教学设计）",
            "implementation",
            "evaluation",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7 或 MLA 9；商务文体引用可参考 AMA Style",
    reporting_standards={
        "corpus_analysis": "语料研究须说明采集范围、编码规则与信度",
        "instructional": "教学实验须报告样本量、教学阶段与前后测对比",
        "translation": "译文须保留原文版式与术语口径",
    },
    conventions=(
        "商务文体引用须给出文件编号、日期与签发机构",
        "跨语言对比须说明语料来源与编码一致性",
        "教学设计须给出教学目标、活动序列与评估指标",
        "术语使用须遵循领域行业标准（如 ISO、GB、行业规范）",
    ),
    key_venues=(
        "Journal of Business Communication",
        "Business Communication Quarterly",
        "Journal of Business Writing",
        "Business Horizons",
        "Journal of Management Communication",
        "Journal of Applied Corporate Finance",
        "Journal of Corporate Finance",
        "Journal of Business Ethics",
    ),
    units_and_formulas_notes=(
        "文体引用须给出文件编号、日期与签发机构",
        "语料样本量须给出具体字符/词/句数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Microsoft Word", "Google Docs", "WPS Office", "Microsoft Outlook", "Gmail", "Grammarly", "DeepL Translator", "有道词典", "百度翻译", "Adobe Acrobat Pro", "LaTeX", "Microsoft Word Mail Merge", "DocuSign", "PandaDoc", "Canva", "石墨文档", "飞书文档", "Typora", "Grammarly Business", "Microsoft VBA", "Python（python-docx）", "AntConc（语料分析）", "LancsBox", "Sketch Engine"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "JSTOR"),
)
