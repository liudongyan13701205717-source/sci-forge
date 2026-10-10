"""第一语言研究学科论文支持：母语习得、语料库语言学与第一语言处理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="first_language_studies",
    aliases=("first_language_studies", "第一语言研究", "母语研究", "L1 studies",
             "first language acquisition", "native language", "语言习得",
             "corpus linguistics", "母语语言学"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="MLA 9",
    reporting_standards={
        "corpus": "语料库规模、抽样方法与标注规范须完整说明",
        "annotation": "标注协议须报告标注者间信度（Cohen's κ / ICC）",
        "elicitation": "数据采集任务须描述指令、环境与参与者的知情同意",
    },
    conventions=(
        "语料库词频用次/千词（frel）表示",
        "标注者间信度用 Cohen's κ 表示",
        "语音参数用 Hz、ms 表示",
        "语料库分层用 tokens/word types 表示",
        "时间序列数据用秒或毫秒表示",
    ),
    key_venues=(
        "Journal of Chinese Linguistics",
        "Applied Linguistics",
        "Bilingualism: Language and Cognition",
        "International Journal of Corpus Linguistics",
        "语言研究",
    ),
    units_and_formulas_notes=(
        "相对词频 frel = 出现次数 / 语料总词数 × 1000",
        "标注者间信度 Cohen's κ 取值 [-1, 1]",
        "基础音高 F0 用 Hz 表示",
        "音节时长用 ms 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN (annotation)", "Praat (phonetics)", "FLEx (Field Linguistics Explorer)", "AntConc (corpus analysis)", "Sketch Engine", "R (tidytext, tidyverse)", "Python (NLTK, spaCy)", "NVivo", "Atlas.ti", "SPSS", "Excel", "CHILDES", "CLARIN", "Leipzig Corpora Collection", "BCC (Bangor Corpus Collection)", "WordNet", "Open Web Corpora", "语音记录仪", "Pragmatica", "LDC (Linguistic Data Consortium)"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)