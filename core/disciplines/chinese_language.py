"""中国语言学科论文支持：语音/语法/方言体裁、APA 引用样式与语言学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chinese_language",
    aliases=("chinese_language", "中国语言学", "汉语语言学", "汉语言文字学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "data（语料）",
            "analysis（分析）",
            "discussion（讨论）",
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
        "fieldwork_study": (
            "abstract",
            "introduction",
            "field sites（调查点）",
            "informants（发音人）",
            "data（语料）",
            "analysis（分析）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；中国语文类期刊遵循 APA 规范）",
    reporting_standards={
        "corpus": "语料库研究遵循语料库报告规范",
        "fieldwork": "田野调查遵循方言调查报告规范",
        "experimental": "实验研究遵循实验报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "语料来源与规模须说明",
        "音标用 IPA 标注",
        "方言点与发音人须交代",
        "转写规范须说明",
        "统计检验须报告",
    ),
    key_venues=(
        "中国语文",
        "语言研究",
        "当代语言学",
        "Journal of Chinese Linguistics",
        "Language and Linguistics",
        "方言",
    ),
    units_and_formulas_notes=(
        "音标用 IPA 国际音标",
        "语料量用 词/字/句 计数",
        "统计量给出 M/SD/SE/CI",
        "样本量须报告",
        "时间用统一格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=(
        "CCL/BCC 语料库检索工具",
        "语料标注软件",
        "Praat 语音分析",
        "LaTeX 排版",
    ),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)