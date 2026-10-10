"""视听技术与媒体 (Audio-Visual Techniques and Media) 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="audiovisual_techniques_and_media",
    aliases=(
        "Audio-visual techniques and media",
        "视听技术与媒体", "视听技术与媒体制作",
        "audio-visual media", "audiovisual media",
        "数字媒体", "digital media", "new media",
        "新媒体", "数字影像", "media production",
        "影视制作", "digital post-production",
        "audio-visual and multimedia",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "methodology",
            "production workflow",
            "results / case studies",
            "discussion",
            "conclusions",
            "references",
        ),
        "critique": (
            "abstract",
            "introduction",
            "text / visual analysis",
            "media context",
            "conclusions",
        ),
        "review": (
            "abstract",
            "historical overview",
            "current state",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（人文学科）",
    reporting_standards={
        "workflow": "制作流程须按前期-拍摄-后期-发行完整披露",
        "measurement": "音视频测量须遵循 EBU / SMPTE / ITU 标准",
        "loudness": "广播响度遵循 EBU R128 (-23 LUFS)",
        "copyright": "作品版权、授权范围与使用许可须声明",
        "reproducibility": "脚本、工程文件、素材来源须可追溯",
    },
    conventions=(
        "帧率 fps、分辨率、色域按行业标准明确标注",
        "音频响度单位 LUFS，参考电平 -20 dBFS = 0 dBu",
        "色彩管理遵循 Rec.709 (HDTV) 或 Rec.2020 (UHD)",
        "作品分类按《中国广播电视行业标准》与行业习惯",
        "引用影视作品的日期、时长、发行机构须完整",
        "字幕字体、时长、位置遵循 GB/T 35641",
    ),
    key_venues=(
        "Journal of Media Psychology",
        "Convergence: The International Journal of Research into New Media",
        "Journal of Digital Media and Convergence",
        "New Media & Society",
        "Journal of Communication",
        "Film Quarterly",
        "Screen",
        "Media, Culture & Society",
        "中国广播电视学刊",
        "电影艺术",
        "当代电影",
    ),
    units_and_formulas_notes=(
        "音频 dBFS/LUFS；视频 fps/Hz；分辨率 px",
        "色域 %DCI-P3；亮度 nit；对比比",
        "网络带宽 Mbps；文件大小 MB/GB",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Adobe Premiere Pro", "Adobe After Effects", "Adobe Photoshop", "Adobe Illustrator", "Adobe Audition", "Adobe Lightroom", "DaVinci Resolve", "Final Cut Pro", "Blackmagic Fusion", "Cinema 4D", "Autodesk Maya", "Autodesk 3ds Max", "Blender", "Houdini", "Unreal Engine", "Unity", "Substance Painter", "Substance Designer", "ZBrush", "Nuke (NukeX)", "Flame (Autodesk)", "Mocha (Pixel)", "Boris FX", "Red Giant", "Pro Tools", "Logic Pro", "Cubase", "Reaper", "Nuendo", "Studio One", "Serato", "Traktor", "djay", "Rekordbox", "DJI Mavic", "DJI Inspire", "DJI Ronin", "DJI Pocket", "DJI Osmo", "ARRI ALEXA", "Sony VENICE", "RED KOMODO", "Blackmagic Pocket Cinema Camera", "Canon EOS C", "Panasonic Lumix", "Sony Alpha", "Canon EOS R", "Fujifilm X", "Sennheiser MKH", "Neumann U87", "Zoom F6", "Zaxcom", "Sound Devices", "Tascam", "Genelec", "Neumann KH", "Yamaha (Studio Monitors)", "Focusrite", "SSL (Silk / Duality)", "Allen & Heath", "DiGiCo", "Soundcraft", "Mackie"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore", "ArtBase", "Museum of Modern Art"),
)
