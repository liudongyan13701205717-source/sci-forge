"""口译与翻译项目学科论文支持：口译、同声传译与翻译技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interpretation_programmes",
    aliases=("interpretation programmes", "口译", "同声传译", "译员培训", "翻译", "翻译学", "口译教育", "翻译技术"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题定位）", "methodology（语料与实验设计）", "results（质量评估与发现）", "discussion（理论与应用）", "references"),
        "case_study": ("abstract", "introduction", "case description（场景、文本与译员）", "analysis（翻译错误分析与质量评估）", "results（错误类型与影响）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（翻译理论与口译理论）", "evidence synthesis（译例与实验证据）", "future directions", "references"),
    },
    citation_style="翻译学引注（GB/T 7714 中文稿或 Chicago 17 英文稿）",
    reporting_standards={
        "k1": "语料给来源、时长或字数与标注方案",
        "k2": "译员或机器译文实验给样本与盲评设计",
        "k3": "质量评估框架明确（MQM 或 DIME-Q 等）",
    },
    conventions=(
        "术语首次出现给双语对照",
        "引文给原译对照并标页码",
        "译例按错误类型分类",
        "口译时长、停顿与填充词单独统计",
        "研究设计区分口译、笔译与机器翻译"
    ),
    key_venues=(
        "Meta: Transactions des Langues et Traducteurs",
        "Target: International Journal of Translation Studies",
        "Babel: Journal of the International Federation of Translation Associations",
        "Traduer: Revue de Linguistique et de Didactique",
        "Journal of Translation, Interpreting and Cross-Cultural Studies"
    ),
    units_and_formulas_notes=(
        "MT 质量用 BLEU、COMET 或 chrF",
        "口译质量用 MQM 错误严重度加权",
        "时长以秒或分钟并给停顿比例",
        "译员样本以人数、次数与语种标注"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("RWS Trados Studio", "SDL Trados", "DeepL", "Google Translate", "Phrase", "Smartcat", "Crowdin", "MemoQ", "OmegaT", "iTranslate", "Rev", "Otter.ai", "Temi", "OpenAI Whisper", "Zoom Transcription", "Adobe Audition", "Audacity", "Grammarly", "DeepL Write", "Wordfast"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
