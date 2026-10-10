"""戏剧学科论文支持：戏剧表演、导演与舞台艺术研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="drama",
    aliases=(
        "drama", "戏剧", "戏剧艺术",
        "theatre", "剧场",
        "theatrical arts", "舞台艺术",
        "stage performance", "舞台表演",
        "dramatic literature", "戏剧文学",
        "playwriting", "剧本写作",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（戏剧问题与理论背景）",
            "methodology（文本分析、表演分析、观众研究）",
            "results（表演效果与艺术分析）",
            "discussion（戏剧理论与实践启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "work analysis（作品分析）",
            "performance analysis（表演分析）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（戏剧理论综述）",
            "major works（重要作品分析）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "performance": "表演分析须注明时间、场景与演员",
        "analysis": "文本分析须注明分析方法与理论框架",
        "audience": "观众研究须注明样本量与方法",
    },
    conventions=(
        "作品首次出现给出中文译名与原名",
        "演员名称使用通用译名并注明原名",
        "舞台术语须使用行业标准",
        "引用剧照须注明版权与来源",
        "表演时间用 分:秒 表示",
    ),
    key_venues=(
        "Theatre Research International",
        "Theatre Journal",
        "Modern Drama",
        "Performance Research",
        "TDR-The Drama Review",
        "Journal of Dramatic Theory and Criticism",
    ),
    units_and_formulas_notes=(
        "时间用 分:秒 表示",
        "舞台术语须使用行业标准",
        "引用剧照须注明版权与来源",
        "观众研究注明样本量与方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Final Draft", "Celtx", "QLab", "Storyboard Pro", "Vectorworks Spotlight", "GrandMA3", "ETC Eos", "Blender", "Unreal Engine", "Ableton Live", "Sibelius", "Logic Pro", "Max/MSP", "Movie Magic Scheduling", "StudioBinder", "Wwise", "Trezor", "Acting Studio", "Gorilla Film", "Dramatron"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
