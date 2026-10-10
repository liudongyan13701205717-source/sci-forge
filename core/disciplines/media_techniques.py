"""Media techniques 学科论文支持：媒体技术制作体裁、行业标准与技术规格注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="media_techniques",
    aliases=("media_techniques", "媒体技术", "media production", "broadcast technology", "film production", "media engineering", "media technology", "media art", "broadcasting"),
    paper_types={
        "research": ("abstract", "introduction（媒体技术背景与动机）", "methodology（制作方法与技术流程）", "results（制作成果与性能评估）", "discussion（应用分析与创新点）", "references"),
        "case_study": ("abstract", "introduction", "case description（制作案例描述）", "analysis（技术分析与制作流程）", "results（成果展示）", "discussion（经验总结）", "references"),
        "review": ("abstract", "introduction", "technology overview（技术综述）", "evidence synthesis（实践证据整合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "audio": "音频制作遵循 ITU-R BS.1770 响度标准",
        "video": "视频制作遵循 SMPTE 色彩标准与 ITU-R BT.709/BT.2020",
        "broadcast": "广播制作遵循 ATSC 或 DVB 编码标准",
        "digital_media": "数字媒体遵循 ISO 14496（MPEG）系列标准",
        "accessibility": "无障碍制作遵循 WCAG 2.1 标准",
    },
    conventions=(
        "技术参数（分辨率、帧率、采样率、码率）须完整列出",
        "制作软件版本须注明",
        "设备型号与规格须给出",
        "制作流程须以分镜表或流程图呈现",
        "色彩管理须说明色彩空间与伽马值",
    ),
    key_venues=(
        "Journal of Broadcasting & Electronic Media",
        "New Media & Society",
        "Journal of the Audio Engineering Society",
        "IEEE Transactions on Broadcasting",
        "Journal of Film and Video",
        "Cinema Journal",
    ),
    units_and_formulas_notes=(
        "视频分辨率用像素；帧率用 fps；色彩空间注明（sRGB/Rec.709/Rec.2020）",
        "音频采样率用 kHz；位深用 bit；响度用 LUFS",
        "码率用 Mbps；压缩编码格式须注明",
        "时长用 HH:MM:SS 格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe Premiere Pro", "Adobe After Effects", "Adobe Audition", "Adobe Photoshop", "Adobe Illustrator", "Avid Media Composer", "DaVinci Resolve", "Final Cut Pro", "Pro Tools", "Cinema 4D", "Blender", "Unreal Engine", "Maya", "Cinema Camera (Sony/Fuji/Canon)", "Microphone (Neumann/Rode/Shure)", "Camera Lens (Canon/Zeiss/Sigma)", "Lighting Equipment (LED/Fluorescent)", "Audio Interface (Focusrite/PreSonus)", "Streaming Software (OBS/Streamlabs)", "Motion Capture System (OptiTrack/Qualisys)"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
