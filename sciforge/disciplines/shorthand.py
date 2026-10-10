"""速记学科论文支持：速记符号体系、口述实录转录与速记教育研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="shorthand",
    aliases=(
        "shorthand",
        "速记",
        "速记学",
        "stenography",
        "stenography theory",
        "court reporting",
        "速记理论",
        "法庭记录",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（速记体系/应用场景）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份）",
    reporting_standards={
        "empirical": "速度测试须报告样本量、语速（words per minute, wpm）与准确率",
        "comparative": "不同速记体系对比须说明测试协议与评判标准",
        "historical": "速记符号史研究须给出文献考据",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "记录速度以 wpm 表示，附准确率（% correct）",
        "速记符号书写须符合所属体系规范（Steno/Memphis/Gabelsberger）",
        "转录误差须按词错率（WER）报告",
        "图表须标注测量条件与置信区间",
        "术语首次出现须给出中英文对照",
    ),
    key_venues=(
        "Journal of the Stenographic Institute",
        "National Court Reporters Association Bulletin",
        "Journal of Communication Disorders",
        "Speech, Language and Hearing",
        "语言文字应用",
    ),
    units_and_formulas_notes=(
        "记录速度：wpm（每分钟词数），基准速记 225 wpm",
        "准确率：correct strokes / total strokes × 100%",
        "词错率：WER = (S + D + I) / N，S=替换、D=删除、I=插入",
        "反应时：ms，采用 stopwatch 或键位记录",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Stenograph Advantage", "EdgeWriter", "Luminant", "Stenograph Mac Stenograph", "Mentor", "MacStroke", "Vosk", "Whisper (OpenAI)", "Audacity", "Adobe Audition", "Microsoft Word (Transcription)", "ZoomText", "Dragon NaturallySpeaking", "Otter.ai", "Rev.ai", "Google Docs Voice Typing", "Adobe InDesign", "LaTeX", "Python (pandas)", "Endnote"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus"),
)
