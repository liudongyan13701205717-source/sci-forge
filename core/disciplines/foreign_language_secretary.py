"""外语秘书学科论文支持：商务英语、翻译技能、行政办公与跨语言沟通。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="foreign_language_secretary",
    aliases=("foreign_language_secretary", "foreign language secretary", "外语秘书", "商务英语", "翻译", "行政办公", "商务秘书", "跨语言沟通"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "translation": "翻译研究须报告源语言、目标语言与翻译策略",
        "linguistic": "语言分析须报告语料来源与标注方法",
        "skill_assessment": "技能评估须报告评分标准与评分者信度"
    },
    conventions=(
        "语种须明确标注（含代码，如 EN-ZH）",
        "语言水平须用标准化量表描述（如 CEFR、HSK）",
        "语料须注明来源与收集方法",
        "翻译术语须统一译法",
        "统计数据须报告样本量与信效度"
    ),
    key_venues=(
        "The Modern Language Journal",
        "Translation Studies",
        "Intercultural Communication Studies",
        "Business English Quarterly",
        "Journal of Second Language Writing"
    ),
    units_and_formulas_notes=(
        "语言水平用 CEFR（A1-C2）或 HSK 分级",
        "正确率用 %",
        "反应时用 ms",
        "词频用次/千词",
        "评分用分制（如 1-5 级）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Microsoft Office", "Google Workspace", "Adobe Acrobat", "Grammarly", "DeepL Translator", "Trados Studio", "MemoQ", "SDL Trados", "Skype for Business", "Zoom", "Teams", "Outlook", "Baidu Translate", "Youdao Dictionary", "Pleco", "WordReference", "ECDICT", "LanguageTool", "AntConc", "Corpus Tool"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
