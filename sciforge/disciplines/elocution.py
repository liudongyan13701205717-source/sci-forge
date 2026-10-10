"""演讲术学科论文支持：演讲技巧、修辞学与口语表达研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="elocution",
    aliases=(
        "elocution", "演讲术", "演讲技巧",
        "public speaking", "公共演讲",
        "rhetoric", "修辞学",
        "oral expression", "口语表达",
        "speech communication", "演讲传播",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（演讲问题与背景）",
            "methodology（演讲分析、修辞研究、效果评估）",
            "results（演讲效果与修辞分析）",
            "discussion（演讲优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "speech analysis（演讲分析）",
            "results（效果评估）",
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
    citation_style="APA 7",
    reporting_standards={
        "analysis": "演讲分析须注明时间、场景与演讲者",
        "rhetoric": "修辞分析须注明方法与理论框架",
        "audience": "观众研究须注明样本量与方法",
    },
    conventions=(
        "演讲时间用 分:秒 表示",
        "修辞术语须使用行业标准",
        "引用演讲须注明版权与来源",
        "观众研究注明样本量与方法",
    ),
    key_venues=(
        "Quarterly Journal of Speech",
        "Communication Monographs",
        "Journal of Communication",
        "Rhetoric Society Quarterly",
        "Communication Education",
    ),
    units_and_formulas_notes=(
        "演讲时间用 分:秒 表示",
        "修辞术语须使用行业标准",
        "引用演讲须注明版权与来源",
        "观众研究注明样本量与方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Adobe Premiere Pro", "Final Cut Pro", "DaVinci Resolve", "Audacity", "Pro Tools", "Logic Pro", "Adobe Audition", "Cubase", "GarageBand", "PowerPoint", "Keynote", "Google Slides", "Canva", "Prezi", "Zoom", "Microsoft Teams", "OBS Studio", "Streamlabs OBS", "iMovie", "Filmora"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
