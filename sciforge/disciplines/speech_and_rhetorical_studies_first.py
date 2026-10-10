"""修辞与演讲学科论文支持：古典修辞学/演说批评/说服研究体裁、MLA 与修辞学术惯例。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="speech_and_rhetorical_studies_first",
    aliases=(
        "speech_and_rhetorical_studies_first",
        "修辞与演讲研究",
        "Speech and Rhetorical Studies",
        "修辞学",
        "演讲学",
        "修辞批评",
        "rhetoric",
        "public speaking",
        "言语修辞",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例）",
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
    citation_style="MLA 9（作者-页码）或芝加哥样式（视期刊）",
    reporting_standards={
        "rhetorical_criticism": "分析路径（如修辞三角、论辩图式、语篇体裁学）须声明，论证结构逐节对应",
        "experimental_study": "说服效果实验须报告被试来源、材料版本、随机化方案与效应量",
        "corpus_study": "语料规模、抽样策略、编码本与一致性（κ）须报告",
    },
    conventions=(
        "引用演说或文本用首次出现后（作者 年份 页码），后续简化为（作者 页码）",
        "修辞格分类沿用古典三分：ethos/pathos/logos，或语篇层面的 kairos/ethos 等术语须给出英文与中文并列",
        "术语译名保持稳定：ethos（信誉）、pathos（情感）、logos（论据）、kairos（时机）、stasis（争议焦点）",
        "直接引语超过 40 词用块引（缩进、不计引号）",
        "历史演说按发表版本引用（含演讲者、场合、日期、场合说明），并注明录音/文本来源",
    ),
    key_venues=(
        "Quarterly Journal of Speech",
        "Rhetoric Review",
        "Philosophy & Rhetoric",
        "Rhetoric",
        "Southern Communication Journal",
    ),
    units_and_formulas_notes=(
        "被试数与效应量按 APA 7 报告：t/F/χ² 标 df，η² 或 ω² 为效应量",
        "说服态度的量表用 Likert 5/7 点，均分给 M (SD)",
        "语料频次以 per 1,000 words 归一化",
        "时间码用于视频演说引用：mm:ss（首次出现处标注）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "MaxQDA", "Transana", "Otter.ai 转写", "Elan", "Audacity 音频编辑", "LabanPro", "XMind 思维导图", "OBS Studio", "Sketch Engine 语料库", "AntConc", "LancsBox", "Noosa", "SPSS", "R", "LaTeX", "EndNote", "Zotero", "Microsoft Word"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
