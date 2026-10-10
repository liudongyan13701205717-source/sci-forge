"""视听技术与媒体制作 (Audio-Visual Techniques and Media Production) 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="audiovisual_techniques_and_media_production",
    aliases=(
        "Audio-visual techniques and media production",
        "视听技术与媒体制作", "视听技术",
        "media production", "数字媒体制作", "digital media production",
        "影视制作", "film production", "广播制作", "broadcast production",
        "audio post-production", "video post-production",
        "post-production", "后期制作", "视听技术与艺术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "methodology",
            "production design",
            "case study",
            "discussion",
            "conclusions",
            "references",
        ),
        "process_report": (
            "abstract",
            "project overview",
            "pre-production",
            "production",
            "post-production",
            "post-mortem",
        ),
        "critique": (
            "abstract",
            "work description",
            "formal analysis",
            "context and interpretation",
            "conclusions",
        ),
    },
    citation_style="APA 7（人文学科）或 IEEE 样式（工程向）",
    reporting_standards={
        "workflow": "完整披露前期、拍摄、后期、发行的关键决策",
        "measurement": "音视频测量遵循 EBU / SMPTE / ITU 标准",
        "loudness": "广播响度 EBU R128 (-23 LUFS)",
        "versioning": "工程文件版本须可追溯，最终交付格式须声明",
        "copyright": "素材版权与使用许可须完整披露",
    },
    conventions=(
        "帧率 fps、分辨率、色域按行业标准明确标注",
        "响度单位 LUFS，参考电平 -20 dBFS = 0 dBu",
        "色彩管理遵循 Rec.709 或 Rec.2020",
        "剪辑术语遵循 HDS (High Definition Stereophonic) 标准",
        "字幕遵循 GB/T 35641 与字幕规范",
        "作品分类按《中国广播电视行业标准》",
    ),
    key_venues=(
        "Journal of the Audio Engineering Society",
        "Signal Processing: Image and Video",
        "IEEE Transactions on Broadcasting",
        "IEEE Transactions on Circuits and Systems for Video Technology",
        "Journal of Media Psychology",
        "Convergence",
        "Film Quarterly",
        "Screen",
        "中国广播电视学刊",
        "电影艺术",
        "当代电影",
    ),
    units_and_formulas_notes=(
        "音频 dBFS/LUFS；视频 fps/Hz；分辨率 px",
        "色域 %DCI-P3；亮度 nit；对比比",
        "网络带宽 Mbps；文件 MB/GB",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe Premiere Pro", "Adobe After Effects", "Adobe Photoshop", "Adobe Illustrator", "Adobe Audition", "Adobe Lightroom", "DaVinci Resolve", "Final Cut Pro", "Blackmagic Fusion", "Cinema 4D", "Autodesk Maya", "Autodesk 3ds Max", "Blender", "Houdini", "Unreal Engine", "Unity", "Substance Painter", "Substance Designer", "ZBrush", "Nuke (NukeX)", "Flame (Autodesk)", "Mocha (Pixel)", "Boris FX", "Red Giant", "Pro Tools", "Logic Pro", "Cubase", "Reaper", "Nuendo", "Studio One", "Serato", "Traktor", "djay", "Rekordbox", "DJI Mavic", "DJI Inspire", "DJI Ronin", "DJI Pocket", "DJI Osmo", "ARRI ALEXA", "Sony VENICE", "RED KOMODO", "Blackmagic Pocket Cinema Camera", "Canon EOS C", "Panasonic Lumix", "Sony Alpha", "Canon EOS R", "Fujifilm X", "Sennheiser MKH", "Neumann U87", "Zoom F6", "Zaxcom", "Sound Devices", "Tascam", "Genelec", "Neumann KH", "Yamaha (Studio Monitors)", "Focusrite", "SSL (Silk / Duality)", "Allen & Heath", "DiGiCo", "Soundcraft", "Mackie"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore", "ArtBase"),
)
