"""翻译学学科论文支持：翻译/口译/批评体裁、MLA 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="translation_studies",
    aliases=("translation_studies", "翻译学", "翻译研究", "口译研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "analysis（分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "translation_analysis": (
            "abstract",
            "introduction",
            "source text（源文本）",
            "translation（译文）",
            "analysis（分析）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
        "corpus_study": (
            "abstract",
            "introduction",
            "corpus（语料库）",
            "method（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="MLA 样式（作者-页码；Translation Studies 遵循 MLA 规范）",
    reporting_standards={
        "translation": "翻译分析遵循翻译分析报告规范",
        "corpus": "语料库研究遵循语料库报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "源文本与译文版本须注明",
        "译文给出原文页码",
        "翻译策略须明确",
        "语料库规模须说明",
        "理论框架须明确",
    ),
    key_venues=(
        "Translation Studies",
        "The Translator",
        "Target",
        "Perspectives",
        "Meta",
        "Babel",
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "译文给出原文页码",
        "语料量用 词/字 计数",
        "版本与版次须注明",
        "时间用统一格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "译文"),
    tools=(
        "SDL Trados 翻译记忆",
        "OmegaT 翻译记忆与术语管理",
        "ParaCrawl 语料对齐",
        "AntConc 语料检索与搭配分析",
        "LaTeX 译文排版",
    ),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)