"""语言、传播与文化学科论文支持：跨文化交际、传播学与社会文化研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="language_communication_and_culture",
    aliases=(
        "language_communication_and_culture",
        "语言传播与文化",
        "跨文化交际",
        "Communication and Culture",
        "Intercultural Communication",
        "跨文化研究",
        "语言与社会",
        "Communications Studies",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题提出）",
            "methodology（方法与语料）",
            "results（发现）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（跨文化分析）",
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
    citation_style="APA 7 或《中国社会科学》引注规范",
    reporting_standards={
        "k1": "语料标注与抽样（时段、来源、编码表）须披露",
        "k2": "受访者身份匿名化与伦理审查声明",
        "k3": "跨文化结论避免单语预设，注明语境差异",
    },
    conventions=(
        "跨文化术语首次出现给中英对照与语用注释",
        "引语保留原文并给直译，避免翻译腔掩盖异质性",
        "图表区分量化指标与叙事材料的呈现方式",
        "避免文化本质主义表述，采用协商/流动视角",
        "参考文献按引用顺序或字母序统一，勿混用体例",
    ),
    key_venues=(
        "Journal of Intercultural Communication",
        "Intercultural Communication Studies",
        "跨文本",
        "语言教学与研究",
        "Foreign Language Teaching and Research",
    ),
    units_and_formulas_notes=(
        "访谈频次与时长给出单位（人次/分钟）",
        "语料库检索用命中率（hits per 100k words）",
        "问卷量表注明题项数与 Likert 刻度",
        "无公式；比例与均值注明口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN", "FLAME", "AntConc", "Sketch Engine", "NVivo", "Atlas.ti", "MAXQDA", "SPSS", "R", "NVivo Transcription", "Otter.ai", "Qualtrics", "SurveyMonkey", "Privolet", "iHIT", "DiscourseKit", "LAUDATUM", "CLAN", "Praat", "Gephi"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
