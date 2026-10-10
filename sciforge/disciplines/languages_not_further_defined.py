"""进一步未定义语言学科论文支持：既未细分也未归类的语言类工作。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="languages_not_further_defined",
    aliases=(
        "languages_not_further_defined",
        "未细分语言",
        "Languages Not Further Defined",
        "未定义语言",
        "Undefined Languages",
        "语言未分类",
        "Generic Language Work",
        "Undifferentiated Language Studies",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题提出）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（个案描述）",
            "analysis（分析）",
            "results（结论）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（背景综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 或通用学术体例",
    reporting_standards={
        "k1": "语料来源与标注完整披露",
        "k2": "被试与语言身份说明（语种、口音）",
        "k3": "分类归属不清晰时须明确范围限定",
    },
    conventions=(
        "涉及具体语言时给 ISO 639-3",
        "术语与例词排版统一",
        "数据表给样本量与检索式",
        "文献体例全稿统一",
        "讨论区分实证与理论层次",
    ),
    key_venues=(
        "Linguistic Inquiry",
        "Studies in Language",
        "Journal of Language Research",
        "Language Research",
        "世界汉语教学",
    ),
    units_and_formulas_notes=(
        "频率以每千词或百分数给出",
        "语料规模以词/句/时长标注",
        "时值以秒或百分比给出",
        "比例给分母与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN", "FLAME", "Praat", "AntConc", "Sketch Engine", "COWS", "CQPweb", "LaTeX", "Zotero", "Glossa", "CLDF Tools", "R", "JASP", "SPSS", "NVivo", "MAXQDA", "Attacat", "Wordfreq", "CLAN", "Audacity"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
