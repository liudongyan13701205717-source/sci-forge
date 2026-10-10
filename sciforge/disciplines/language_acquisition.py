"""语言习得学科论文支持：第二语言习得、认知机制、教学理论与语料分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="language_acquisition",
    aliases=(
        "language_acquisition",
        "语言习得",
        "Second Language Acquisition",
        "SLA",
        "Language Learning",
        "Foreign Language Acquisition",
        "Applied Linguistics",
        "Bilingualism",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（绪论）",
            "methodology（研究方法）",
            "results（结果）",
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
    citation_style="APA",
    reporting_standards={
        "k1": "CEFR 欧洲语言共同参考框架",
        "k2": "GB/T 33062 语言能力分级标准",
        "k3": "ACTFL 第二语言能力量表",
    },
    conventions=(
        "语料标注须遵循CLAN/CHAT编码规范",
        "实验设计须注明变量类型（自变量/因变量/控制变量）",
        "统计检验须报告效应量（如η²、Cohen's d）",
        "学习者水平须采用CEFR或ACTFL分级",
        "引用语言数据须注明来源与版权",
    ),
    key_venues=(
        "Studies in Second Language Acquisition",
        "Applied Linguistics",
        "Language Learning",
        "The Modern Language Journal",
        "中国应用语言学",
    ),
    units_and_formulas_notes=(
        "频率以词/分钟（wpm）表示",
        "反应时间以毫秒（ms）表示",
        "皮尔逊相关系数r：-1到1",
        "效应量η²：0到1",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("CLAN", "CHAT", "L2Speech", "Praat", "ELAN", "Annodex", "AntConc", "Lauda", "Sketch Engine", "Corpus of Contemporary American English", "BYU Speech", "TalkBank", "LinguaLab", "VoiceBase", "SpeechRecognizer", "iSpeak", "Anki", "iLearn", "Rosetta Stone", "FLEx（Field Linguistics Explorer）"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
