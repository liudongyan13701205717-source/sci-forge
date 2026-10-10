"""手语翻译学科论文支持：口译研究范式、聋人文化翻译伦理与语料库研究方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sign_language_interpreting",
    aliases=(
        "sign_language_interpreting",
        "手语翻译",
        "手语口译",
        "sign language interpreting",
        "SLI",
        "Sign Language Interpreting",
        "Deaf Studies",
        "聋人研究",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（语料库/实验/访谈方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（场景/译员案例）",
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
        "corpus": "语料库研究须报告语料规模、领域分布、标注方案与信度（κ 值）",
        "experimental": "口译实验须说明任务设计、被试分组与盲法",
        "ethics": "涉及聋人参与者的研究须遵循 SILI 伦理准则（知情同意、社区参与）",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "手语术语遵循 ISO 24610 术语标准与所属国家手语规范",
        "翻译方向标明：SL→SP（手语→口语）或 SP→SL（口语→手语）",
        "视频数据须说明录制设备、帧率、分辨率与参与者身份匿名化方式",
        "错误分析按词错率（WER）、句错率（SER）与语义等价度分层报告",
        "引用聋人研究文献须优先使用聋人学者第一人称表述",
    ),
    key_venues=(
        "Interverbing: International Journal of Sign Language Interpretation",
        "Across Linguistic Communities: Theories, Approaches and Methods of Translation",
        "Sign Language & Translation Studies",
        "Journal of Deaf Studies and Deaf Education",
        "手语研究",
    ),
    units_and_formulas_notes=(
        "口译速度以 words per second (wps) 计；双语切换以 Hz 报告",
        "错误率：CER = (S + D + I) / N，含替换/删除/插入",
        "视频帧率以 fps 标注；动作识别采用 pose landmarks (COCO/Wrist keypoints)",
        "参与者报告以年龄/手语熟练度/职业年限三元组表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN", "FLAME", "SignNote", "SignPuddle", "Praat", "Nvivo", "Adobe Premiere Pro", "DaVinci Resolve", "OpenPose", "MediaPipe", "Otter.ai", "Rev.ai", "Zoom", "OBS Studio", "iMovie", "LaTeX", "Endnote", "Canva", "Adobe InDesign", "Photoshop"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus", "LanguageSci"),
)
