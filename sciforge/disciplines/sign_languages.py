"""手语学科论文支持：手语语言学、形态句法结构与聋人社区语言政策研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sign_languages",
    aliases=(
        "sign_languages",
        "手语",
        "sign languages",
        "手语语言学",
        "Sign Linguistics",
        "Sign Language",
        "ASL",
        "BSL",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（语料库/构拟/实验方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（语言/社区案例）",
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
        "corpus": "语料库研究须说明采集协议、参与者知情同意与视频存储",
        "descriptive": "描述性研究须给出音标/词素标注方案与双标注一致性",
        "typology": "类型学研究须报告样本覆盖的语言数量与代表语言",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "手语术语遵循 ISO 24610 与所属国家手语词典规范",
        "手语形态标注须包含空间指向、非手工特征（口形/眉眼/身体位移）",
        "示例符号须使用手语音标系统（如 SFSL、Bamboo 手语文字系统）",
        "双语社区研究须说明参与者的语言背景与熟练度",
        "视频示例须标注帧率、时长与动作起止点",
    ),
    key_venues=(
        "Sign Language & Translation Studies",
        "Phonology",
        "Journal of Deaf Studies and Deaf Education",
        "Lingua",
        "手语研究",
    ),
    units_and_formulas_notes=(
        "手语词时长以 ms 计；语速以 words per minute (wpm) 计",
        "空间位置标注采用三维坐标系（x, y, z），单位 cm",
        "非手工特征采用 Likert 5 级量表或分类编码",
        "语料标注一致性用 Cohen's κ 报告（κ > 0.8 为优）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN", "FLAME", "Praat", "3D Slicer", "Bamboo Notepad", "SFSL", "RStudio", "Python", "LingPy", "PHYLIP", "CLAN (CHILDES)", "Prosign", "SignBabble", "Adobe Premiere Pro", "DaVinci Resolve", "OBS Studio", "iMovie", "LaTeX", "Endnote", "Adobe InDesign"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus", "LanguageSci"),
)
