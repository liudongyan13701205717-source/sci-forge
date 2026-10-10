"""导演学科论文支持：电影/戏剧导演理论与创作研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="directing",
    aliases=(
        "directing", "导演", "导演艺术",
        "film directing", "电影导演",
        "theatre directing", "戏剧导演",
        "screen direction", "屏幕导演",
        "stage direction", "舞台导演",
        "directorial studies", "导演研究",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（导演问题与理论背景）",
            "methodology（文本分析、导演访谈、作品分析）",
            "results（导演手法与效果分析）",
            "discussion（导演理论与实践启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "work analysis（作品分析）",
            "directorial approach（导演手法分析）",
            "evaluation（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（导演理论综述）",
            "major directors（重要导演分析）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "film_analysis": "镜头/景别/剪辑术语须标准化",
        "interview": "访谈对象、方法与时间须注明",
        "analysis": "分析方法须明确（形式主义/作者论/精神分析等）",
        "ethics": "访谈须获得知情同意",
    },
    conventions=(
        "电影/戏剧作品首次出现给出中文译名与原名",
        "导演名称使用通用译名并注明原名",
        "镜头术语（长镜头、特写、全景）须使用行业标准",
        "影像分析须标注时间码",
        "引用影像/剧照须注明版权与来源",
    ),
    key_venues=(
        "Screen",
        "Journal of Film and Video",
        "Camera Obscura",
        "Sight and Sound",
        "Cinema Journal",
        "Film Quarterly",
    ),
    units_and_formulas_notes=(
        "时间用 分:秒 表示",
        "镜头术语须使用行业标准",
        "影像分析须标注时间码",
        "引用须注明版权与来源",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Final Draft", "Celtx", "StudioBinder", "ShotPro", "Shot Designer", "Storyboard Pro", "Frame.io", "Movie Magic Scheduling", "Movie Magic Budgeting", "DaVinci Resolve", "Adobe Premiere Pro", "Avid Media Composer", "Blender", "Unreal Engine", "QLab", "Ableton Live", "Logic Pro", "Sibelius", "GrandMA3", "Dramatron"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
