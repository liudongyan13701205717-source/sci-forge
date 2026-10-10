"""戏剧学学科论文支持：戏剧史、剧本文本、导演学与表演实践研究体裁、MLA 引用样式与演出记录注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="theatre",
    aliases=(
        "theatre",
        "Theatre",
        "戏剧学",
        "戏剧研究",
        "剧本文学",
        "导演学",
        "Drama and Theatre",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题背景与研究动机）",
            "methodology（文本分析、田野方法与访谈设计）",
            "results（发现与分析结论）",
            "discussion（理论阐释与实践对话）",
            "conclusions",
            "references",
        ),
        "literary_analysis": (
            "abstract",
            "introduction（作品背景与文本脉络）",
            "textual analysis（剧本结构与人物分析）",
            "interpretation（阐释路径与理论视角）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "artwork description（作品基本信息与演出背景）",
            "process documentation（创作过程记录）",
            "analysis（演出效果评估）",
            "discussion",
            "references",
        ),
    },
    citation_style="MLA 样式（艺术学领域以 MLA 为常见；剧本引用遵循 Stage 32 格式）",
    reporting_standards={
        "script_citation": "剧本引用须注明版本（出版年份或剧团本）与页码或场/幕编号",
        "performance_citation": "演出引用须包含剧团、导演、演出时间与地点",
        "fieldwork": "田野/排练记录须注明访谈对象、时间、地点与知情同意情况",
        "visual_documentation": "照片与视频记录须注明拍摄者、时间与使用许可",
    },
    conventions=(
        "剧本场次编号采用 场:幕:分 格式（如 2:3:1），与原文一致",
        "演出引用首版演出优先标注",
        "理论建构须结合具体演出案例，避免脱离实践的抽象化论述",
        "排练记录保留时间线与关键节点，访谈引语须经受访者确认",
        "术语首现给出中英对照",
    ),
    key_venues=(
        "Theatre Research International",
        "Theatre Journal",
        "New Theatre Quarterly",
        "Performance Research",
        "戏剧艺术",
    ),
    units_and_formulas_notes=(
        "演出时长以分钟（min）为单位，分幕长度须注明",
        "舞台尺寸以米（m）为单位，灯光角度以度（°）为单位",
        "音视频记录时长以秒（s）为单位，音频采样率以 kHz 计",
        "文献引用页码与场/幕编号并给出",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Final Draft", "Dramatica", "Stage 32", "Adobe Premiere Pro", "DaVinci Resolve", "Final Cut Pro", "Avid Media Composer", "ProTools", "Logic Pro", "Sibelius", "Adobe Photoshop", "Adobe After Effects", "Blender", "Unreal Engine", "OBS Studio", "ARRI Alexa 摄影机", "RED Cinema Camera", "ETC ION 舞台灯光控制台", "EndNote", "Zotero"),
    category="艺术学",
    databases=("OpenAlex", "Crossref"),
)
