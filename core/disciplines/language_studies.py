"""语言学研究论文支持：语音、语法、语义与语用研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="language_studies",
    aliases=(
        "language_studies",
        "语言学研究",
        "Linguistics",
        "语言学",
        "Theoretical Linguistics",
        "理论语言学",
        "Empirical Linguistics",
        "实证语言学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题提出）",
            "methodology（方法与数据）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（语言事实描述）",
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
    citation_style="Linguistics 引用体例（作者-年份）或 Chicago",
    reporting_standards={
        "k1": "语料/被试描述（人数、语种、口音、采样条件）",
        "k2": "实验设计与判断实验的评分方案、评判者信度",
        "k3": "生成理论给出显式标记式与预测",
    },
    conventions=(
        "国际音标（IPA）与音素/音位区分；正字法与音标并存",
        "术语区分音位（phoneme）与音素（phone），例词给原文",
        "例句编号统一并给双语注释",
        "数据披露语料量、时段与被试数",
        "讨论区分描述性发现与理论推论",
    ),
    key_venues=(
        "Language",
        "Linguistic Inquiry",
        "Journal of Linguistics",
        "Natural Language & Linguistic Theory",
        "Chinese Journal of Linguistics",
    ),
    units_and_formulas_notes=(
        "频率给每千词或百分比并注明语料基数",
        "被试人数与实验试次需给出",
        "统计检验给出 t/χ²/α 值与效应量",
        "音高以 Hz 或 semitone 为单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Praat", "ELAN", "FLAMES", "PANNZER", "SondR", "OpenFEST", "PraatScript", "ELAN Corpus Tool", "AntConc", "Sketch Engine", "COCA", "BNC CQP", "CLAN", "ChildLang", "Glossa", "R", "JASP", "PsychoPy", "E-Prime", "Audacity"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
