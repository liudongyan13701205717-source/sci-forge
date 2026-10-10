"""影视剪辑学科论文支持：影像剪辑技术、叙事节奏与后期工艺体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="film_and_tv_editing",
    aliases=(
        "film_and_tv_editing", "影视剪辑", "影视后期",
        "film editing", "video editing",
        "电视剪辑", "影像后期", "剪辑工艺", "影视制作后期",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（剪辑技术与叙事问题）",
            "methodology（剪辑参数、叙事分析、影像计量）",
            "results（剪辑效果与叙事分析）",
            "discussion（与电影美学、观众研究对话）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（影片/节目案例）",
            "analysis（剪辑节奏、镜头语法与叙事）",
            "results（案例发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（剪辑理论与实践综述）",
            "evidence synthesis（现有研究与缺口）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份；影视学论著亦常见注-书目）",
    reporting_standards={
        "editing": "剪辑参数须注明时间码、帧率与分辨率",
        "color": "调色报告须注明 LUT、色彩空间与 HDR 范围",
        "audio": "音频剪辑须注明采样率、位深与混音参数",
        "workflow": "工作流程须注明软件版本、格式与编码",
    },
    conventions=(
        "时间码用 HH:MM:SS:FF 格式",
        "帧率用 fps 表示",
        "分辨率用 px 表示",
        "位深用 bit 表示",
        "剪辑工具注明软件名称与版本",
    ),
    key_venues=(
        "Screen",
        "Cinema Journal",
        "Film Quarterly",
        "Journal of Film and Video",
        "Editing: A Journal of Film and Video",
    ),
    units_and_formulas_notes=(
        "时间码 HH:MM:SS:FF；帧率 fps",
        "分辨率 px；位深 bit",
        "采样率 kHz；音频电平 dB",
        "文件体积 GB；编码率 Mbps",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Premiere Pro", "DaVinci Resolve", "Avid Media Composer", "Final Cut Pro", "Adobe After Effects", "DaVinci Resolve Fairlight", "Adobe Audition", "ProTools", "Logic Pro X", "FFmpeg", "DaVinci Resolve Fusion", "Nuke", "Unreal Engine 5", "Blender", "Cinema 4D", "Adobe Photoshop", "Adobe Lightroom", "Apple Motion", "Endnote", "Zotero"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
