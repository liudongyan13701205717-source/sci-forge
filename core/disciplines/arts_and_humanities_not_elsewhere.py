"""Arts and humanities not elsewhere 学科论文支持：文学、语言学、文化批评等未另列人文学科，偏语料与文本分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="arts_and_humanities_not_elsewhere",
    aliases=(
        "arts_and_humanities_not_elsewhere",
        "arts and humanities not elsewhere",
        "文学研究",
        "文学与批评",
        "literary studies",
        "literary and linguistic computing",
        "语料库语言学",
        "corpus linguistics",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "corpus and method（语料来源、切分与分析工具）",
            "analysis",
            "interpretation",
            "conclusion",
            "references",
        ),
        "theoretical": (
            "abstract",
            "introduction",
            "conceptual development",
            "argument",
            "critique of alternatives",
            "conclusion",
            "references",
        ),
        "close_reading": (
            "abstract",
            "introduction",
            "contextual background",
            "close reading / analysis",
            "theoretical framing",
            "conclusion",
            "references",
        ),
    },
    citation_style="MLA 9th（文学）；Chicago 17th Notes-Bibliography（历史/艺术史）",
    reporting_standards={
        "corpus": "语料库版本、语种、文本量与来源逐条标注",
        "quotation": "直接引文须与所依据版本校对；引用异文处说明版本",
        "annotation": "注释体系（脚注/尾注/方括号）须全文一致",
        "digital_tool": "使用分词、标注、语料检索工具时报告工具与参数",
        "version": "研究依赖的电子书版本、修订日期须标注",
    },
    conventions=(
        "文学批评须区分「文本内部」与「文本外部」证据；理论术语首次出现给出出处",
        "直接引文与释义须区分；转述不得改动原文语义与语气",
        "异文、校勘记、版本差异须在首次出现处标明版本依据",
        "语言学术语用拉丁字母斜体（term, lang-xx）；中文术语用书名号《》或引号",
        "图表按正文引用顺序编号；数字人文图表须附可复算的数据表",
        "结论段须明确本文主张、贡献与局限",
    ),
    key_venues=(
        "PMLA (Publications of the Modern Language Association)",
        "New Literary History",
        "boundary 2",
        "Representations",
        "Modern Philology",
        "Comparative Literature",
        "New Media & Society",
    ),
    units_and_formulas_notes=(
        "频率报告 per million words 或 per 1,000 tokens；共现用 PMI/log-likelihood",
        "统计测试用 chi-square、Fisher exact 或 log-likelihood；报告 P 值与 df",
        "情感/主题分析用 F1、Cohen's κ 报告一致性",
        "数字人文可视化须标注坐标轴、比例、缺失值处理",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "MAXQDA", "ATLAS.ti", "ELAN", "AntConc", "Sketch Engine", "LIWC-22", "Coh-Metrix", "Voyant Tools", "gensim", "BERTopic", "MALLET", "spaCy", "Stanza (CMU)", "YAKE", "R (quanteda, tm)", "Python (nltk, pandas)", "Zotero", "EndNote", "Project Gutenberg", "Perseus Digital Library", "Internet Archive", "Google Books Ngram Viewer"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "JSTOR", "Project MUSE", "LILAC", "PhilPapers"),
)
