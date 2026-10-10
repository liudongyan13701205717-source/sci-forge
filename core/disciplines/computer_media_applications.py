"""计算机媒体应用学科论文支持：多媒体/视听/桌面发布体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_media_applications",
    aliases=("computer media applications", "计算机媒体应用", "多媒体",
             "multimedia", "数字媒体", "digital media", "视听技术",
             "audiovisual techniques", "桌面发布", "desktop publishing"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "related work",
            "method",
            "implementation",
            "evaluation",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "background and motivation",
            "design and implementation",
            "evaluation",
            "user study",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method",
            "taxonomy",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份）",
    reporting_standards={
        "experimental": "评估须报告输出设备与编码参数",
        "benchmark": "媒体质量指标须同格式同码率对比",
        "user_study": "用户研究须报告样本量、招募与激励",
        "reproducibility": "工程文件与导出设置须公开",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "音视频/图文输出规格（分辨率、码率、色彩空间）须声明",
        "媒体质量指标（PSNR/SSIM/VMAF）须定义一致",
        "对比须在相同格式与播放环境下进行",
        "工程文件与导出设置须记录",
        "版权/许可须声明",
    ),
    key_venues=(
        "ACM Multimedia",
        "IEEE Transactions on Multimedia",
        "IEEE Transactions on Circuits and Systems for Video Technology",
        "EuroMedia",
        "ACM Multimedia Systems (MM)",
        "Human-Computer Interaction International (HCII)",
        "ACM Transactions on Applied Perception",
        "Journal of Imaging",
    ),
    units_and_formulas_notes=(
        "分辨率用 px；帧率用 fps；码率用 kbps",
        "音频采样率用 kHz；位深用 bit",
        "压缩比用 ×；质量指标 PSNR 用 dB",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe Premiere Pro", "Adobe After Effects", "Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "DaVinci Resolve", "Kdenlive", "Shotcut", "FFmpeg", "Audacity", "Ableton Live", "Pro Tools", "Logic Pro", "GIMP", "Affinity Photo", "Affinity Designer", "Figma", "Canva", "Blender", "Lightroom", "Cinema 4D", "Minecraft", "Houdini", "Substance Painter", "Webflow", "Framer", "Sora", "Midjourney", "Stable Diffusion"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)
