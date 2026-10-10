"""表演与导演学科论文支持：戏剧研究、导演学、表演方法派与田野记录注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="acting_and_directing",
    aliases=(
        "acting_and_directing",
        "表演与导演",
        "表演艺术",
        "导演学",
        "戏剧表演",
        "Acting",
        "Directing",
        "Drama and Theatre",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题背景与研究动机）",
            "methodology（田野方法、访谈设计、排练观察与文本分析方法）",
            "results（排练记录、演出分析或访谈发现）",
            "discussion（理论阐释与实践对话）",
            "conclusion",
            "references",
        ),
        "literary_analysis": (
            "abstract",
            "introduction（作品背景与文本脉络）",
            "textual analysis（剧本结构与人物关系分析）",
            "directorial reading（导演阐释路径）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "artwork description（作品基本信息与演出背景）",
            "process documentation（创作过程记录）",
            "performance analysis（演出效果评估）",
            "discussion",
            "references",
        ),
    },
    citation_style="APA 或 MLA 样式（艺术学领域以 MLA 为常见；剧本引用遵循 Stage 32 格式）",
    reporting_standards={
        "fieldwork": "田野/排练记录须注明访谈对象身份、时间、地点与知情同意情况",
        "work_citation": "演出作品引用须包含剧团、导演、演出时间与地点",
        "script_quotation": "剧本引用须注明版本（剧本出版年份/剧团本）与页码或场/幕编号",
        "visual_documentation": "照片与视频记录须注明拍摄者、时间与使用许可",
    },
    conventions=(
        "剧本引用遵循行业标准（如 Stage 32 或 Dramatica 格式），场/幕编号须与原文一致",
        "演出引用须包含剧团、导演、演出时间与地点，首版演出优先标注",
        "理论建构应结合具体演出案例分析，避免脱离实践的抽象化论述",
        "排练记录应保留时间线与关键节点，访谈引语须经受访者确认",
    ),
    key_venues=(
        "Theatre Research International",
        "Theatre Journal",
        "New Theatre Quarterly",
        "Performance Research",
        "戏剧艺术",
        "Theatre Communication and Culture",
    ),
    units_and_formulas_notes=(
        "演出时长以分钟（min）为单位，分幕长度须注明",
        "舞台尺寸以米（m）为单位，灯光角度以度（°）为单位",
        "剧本场次编号采用 场:幕:分 格式（如 2:3:1），与剧本原文一致",
        "音视频记录时长以秒（s）为单位，采样率须注明（音频采样率以 kHz 计）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Final Cut Pro", "Adobe Premiere Pro", "DaVinci Resolve", "Avid Media Composer", "ProTools", "Adobe After Effects", "Adobe Photoshop", "Final Draft", "Storyboarder（Toontoon）", "ARRI Alexa 摄影机", "RED Cinema Camera", "Blackmagic 摄影机", "ETC ION 舞台灯光控制台", "Sibelius", "Logic Pro", "OBS Studio", "Blender", "Unreal Engine", "ScreenFlow", "Adobe Audition"),
    category="艺术学",
    databases=("OpenAlex",),
)
