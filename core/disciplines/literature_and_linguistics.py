"""文学与语言学学科论文支持：文学批评、语言学与跨学科研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="literature_and_linguistics",
    aliases=(
        "literature_and_linguistics",
        "文学与语言学",
        "literature",
        "linguistics",
        "中文",
        "语言学",
        "文学",
        "corpus linguistics",
        "textual analysis",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
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
    citation_style="MLA 9",
    reporting_standards={
        "k1": "文学研究采用主题分析框架",
        "k2": "语言学实验须报告样本量与统计显著性",
        "k3": "跨学科研究注明理论来源与适用边界",
    },
    conventions=(
        "引用文学作品使用 MLA 格式",
        "术语首次出现标注英文与释义",
        "语料库分析注明语料规模与抽样方法",
        "文体分析须说明语料与计量指标",
        "翻译研究注明对译版本与底本",
    ),
    key_venues=(
        "PMLA",
        "Poetics",
        "Language",
        "Lingua",
        "Journal of Literary Studies",
    ),
    units_and_formulas_notes=(
        "语料库计数以词元(token)与词形(lemma)区分",
        "统计检验报告效应量与置信区间",
        "文本计量指标注明算法版本",
        "引用页码遵循版本文本",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ANTCONC", "LCM", "RStudio", "LaTeX", "Sketch Engine", "CLARIN", "Praat", "ELAN", "ProxLab", "Voyants Tools", "StanzaNLP", "Stanford CoreNLP", "SpaCy", "Wmatrix", "LEXICAL DATABASE (COCA)", "NOVA (Narrative Corpus)", "Mental Timeline Database", "František Štěpánek's STARDIC", "Wordsmith Tools", "UAMCO"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
