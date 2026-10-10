"""外语学科论文支持：语言习得、二语习得、语言测试、语言政策与教学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="foreign_languages",
    aliases=("foreign_languages", "foreign language", "外语", "二语习得", "语言教学", "语言测试", "应用语言学", "第二语言"),
    paper_types={
        "research": ("abstract", "introduction（研究背景与动机）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "experiment": "实验须报告样本量、设计类型与统计检验方法",
        "survey": "问卷调查须报告信效度与回收率",
        "teaching": "教学实验须报告课时、教材与干预措施",
        "test": "语言测试须报告信度、效度与区分度"
    },
    conventions=(
        "语种与方言须明确标注",
        "学习者水平用 CEFR 分级描述",
        "语料须注明来源与收集方法",
        "引文须区分直接引文与间接引文",
        "术语须统一中英文对应关系"
    ),
    key_venues=(
        "The Modern Language Journal",
        "Foreign Language Annals",
        "TESOL Quarterly",
        "Applied Linguistics",
        "Studies in Second Language Acquisition"
    ),
    units_and_formulas_notes=(
        "语言水平用 CEFR（A1-C2）",
        "反应时用 ms（毫秒）",
        "准确率用 %（百分比）",
        "词汇量用词目数（type-token）",
        "语速用 wpm（每分钟词数）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Duolingo", "Rosetta Stone", "Anki", "Memrise", "Grammarly", "iWriter", "AntConc", "Linguistic Analysis Web Server", "Corpus Builder", "Praat", "ELAN", "EXMARaLDA", "LaBSS", "Learner Corpus", "BNC", "COCA", "WordNet", "Google Ngram", "Sketch Engine", "LIFT"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
