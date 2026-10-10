"""未分类外语言学科论文支持：既非特定语言分支、亦未细分的通用语言文献。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="languages_not_elsewhere_classified",
    aliases=(
        "languages_not_elsewhere_classified",
        "未分类外语言",
        "Languages NEC",
        "Languages Not Elsewhere Classified",
        "语言杂类",
        "泛语言研究",
        "General Language Studies",
        "Language Miscellany",
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
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 或学科规范",
    reporting_standards={
        "k1": "语料与实验条件完整披露",
        "k2": "被试/语言标注（语种、口音、语域）",
        "k3": "跨语言泛化须说明证据边界",
    },
    conventions=(
        "首次出现给 ISO 639-3 与语系归属",
        "术语区分描述与解释层面",
        "例词统一排版（原文/转写/释义）",
        "数据表给出样本量与来源",
        "参考文献按字母序或引用序统一",
    ),
    key_venues=(
        "Linguistic Typology",
        "Journal of Historical Linguistics",
        "Annual Review of Linguistics",
        "Language Problems and Language Planning",
        "语言学论丛",
    ),
    units_and_formulas_notes=(
        "频率以每千词或百分数给出",
        "语料量注明语料库与检索式",
        "时间单位用秒或分钟",
        "比例给分母与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN", "FLAME", "Praat", "AntConc", "Sketch Engine", "COWS", "CQPweb", "LaTeX", "Zotero", "Mendeley", "Glossa", "CLDF Tools", "R", "JASP", "SPSS", "NVivo", "MAXQDA", "Attacat", "Wiktionary", "Wordfreq"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
