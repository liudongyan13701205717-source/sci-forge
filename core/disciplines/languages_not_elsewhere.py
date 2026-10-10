"""未分类语言学科论文支持：语言学分外未归类的语言相关工作。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="languages_not_elsewhere",
    aliases=(
        "languages_not_elsewhere",
        "未分类语言",
        "Languages not elsewhere classified",
        "其他语言",
        "Unclassified Languages",
        "语言杂项",
        "Miscellaneous Languages",
        "非主流语言研究",
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
    citation_style="APA 7 或学科惯例体例",
    reporting_standards={
        "k1": "语言身份（ISO 639-3 代码）须标注",
        "k2": "濒危等级与语料来源透明披露",
        "k3": "母语者/学习者的数据区分注明",
    },
    conventions=(
        "首次出现给 ISO 代码与族群名称",
        "语言例词给原文、转写、释义三列",
        "避免刻板印象与殖民视角表述",
        "语料稀缺时须说明限制",
        "文献体例统一，勿混用",
    ),
    key_venues=(
        "Language Documentation and Conservation",
        "Journal of Endangered Languages",
        "Documental Journal of Linguistics",
        "Linguistic Discovery",
        "民族语言研究",
    ),
    units_and_formulas_notes=(
        "词表规模给词条数",
        "语音参数用 Hz 或 dB",
        "语料量以词/句/小时标注",
        "比例与频次给口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN", "FLAME", "Praat", "Audacity", "LingList", "Glottolog", "PHLARD", "ELDP Toolkit", "CldfTools", "CLDFTemplate", "FieldWorks Language Explorer", "SIL FieldWorks", "OpenCorpora", "AntConc", "Sketch Engine", "LaTeX", "Zotero", "Glossbazaar", "Wiktionary API", "R"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
