"""视听技术 (Audio-Visual Techniques) 学科论文支持：摄录、灯光、录音、监视、广播。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="audiovisual_techniques_and",
    aliases=(
        "Audio-visual techniques and", "视听技术",
        "audio-visual techniques", "audiovisual techniques",
        "视听技术及其制作", "视听技术",
        "broadcast engineering", "广播工程",
        "audio recording", "audiovisual production engineering",
        "摄录技术", "灯光与照明技术", "现场录音",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "technical design",
            "experiment / test setup",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "project overview",
            "system architecture",
            "workflow",
            "evaluation",
        ),
        "review": (
            "abstract",
            "technical evolution",
            "current state",
            "open questions",
            "references",
        ),
    },
    citation_style="IEEE 样式（工程技术）",
    reporting_standards={
        "measurement": "音视频测量须遵循 EBU / SMPTE / ITU 标准",
        "loudness": "响度遵循 EBU R128 / ATSC A85（-23 LUFS 广播）",
        "color": "色度学遵循 Rec.2020 / Rec.709；色温 K",
        "latency": "端到端延迟须报告（ms）",
        "safety": "现场电气与安全符合 GB / CE / FCC",
    },
    conventions=(
        "音频电平用 dBFS；响度用 LUFS；动态范围 dB",
        "帧率用 fps（24/25/30/50/60）；分辨率 1920×1080/3840×2160",
        "色彩空间与色域明确（Rec.709 / Rec.2020 / DCI-P3）",
        "信号流向图按 SMPTE 标准绘制（SDI/HDMI/NDI）",
        "现场设备按 IEC 60307 标识",
        "参考电平 -20 dBFS = 0 dBu (AES3)",
    ),
    key_venues=(
        "Journal of the Audio Engineering Society (JAES)",
        "Signal Processing: Image and Video",
        "IEEE Transactions on Broadcasting",
        "IEEE Transactions on Circuits and Systems for Video Technology",
        "Broadcast Engineering",
        "中国广播",
        "电视技术",
        "电声技术",
        "中国有线电视",
        "Journal of the Acoustical Society of America",
    ),
    units_and_formulas_notes=(
        "音频电平 dBFS/dBU；响度 LUFS",
        "视频帧率 fps；分辨率 1920×1080；刷新率 Hz",
        "色温 K；照度 lx；色彩 gamut %DCI",
        "网络带宽 Gbps；延迟 ms",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ARRI ALEXA", "ARRI LF", "Sony VENICE", "RED KOMODO", "Blackmagic Pocket Cinema Camera", "Canon EOS C", "DJI Ronin", "DJI Inspire", "DJI Pocket", "Sennheiser MKH 416", "Sennheiser MKH 8040", "Neumann KU 100", "DPA 4099", "Shure SM7B", "Neumann U87", "AKG C414", "Zoom F6", "Zoom H6", "Tascam Model 62", "Sound Devices MixPre-6 II", "Zaxcom Livetrak", "Pro Tools", "Nuendo", "Reaper", "Logic Pro", "Cubase", "Studio One", "Ableton Live", "Focusrite Scarlett", "SSL Duality", "RME Fireface", "Genelec", "Neumann KH", "Yamaha MG", "Mackie", "Behringer", "Allen & Heath dLive", "DiGiCo SD12", "Soundcraft Vi", "Native Instruments Komplete", "Arturia", "Serato", "Traktor", "Rekordbox"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "IEEE Xplore", "CNKI", "Zenodo", "arXiv"),
)
