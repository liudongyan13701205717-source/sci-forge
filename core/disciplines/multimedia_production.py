"""多媒体制作学科论文支持：交互式多媒体内容设计与评估体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="multimedia_production",
    aliases=(
        "multimedia_production", "多媒体制作", "Multimedia production",
        "多媒体设计", "交互式内容", "Multimedia design",
        "digital media production", "数字媒体制作",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（设计/评估方法）",
            "results（用户与内容数据）",
            "discussion（发现与局限）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（作品/项目）",
            "analysis（设计分析）",
            "results（用户反馈）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（工具/平台综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "可用性评估须报告任务完成率与 SUS 分数",
        "k2": "交互设计研究须报告用户样本与任务设计",
        "k3": "多媒体作品分析须报告平台、时长与分发渠道",
    },
    conventions=(
        "多媒体作品描述须给出平台与格式",
        "视频时长用 mm:ss 记法",
        "图表编号须给出分辨率与帧率",
        "用户研究须报告样本与任务成功率",
        "引用作品须给出作者、年份与 URL",
    ),
    key_venues=(
        "IEEE Transactions on Multimedia",
        "Journal of New Media",
        "International Journal of Human-Computer Studies",
        "Journal of Communication",
        "《电声技术》",
    ),
    units_and_formulas_notes=(
        "视频分辨率用 像素×像素；帧率用 fps",
        "音频用 kHz 采样率与 bit 深度",
        "文件大小用 MB/GB；带宽用 Mbps",
        "响应时间用 ms；加载时间用 s",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Adobe Premiere Pro", "Adobe After Effects", "Adobe Photoshop", "Adobe Illustrator", "DaVinci Resolve", "Final Cut Pro", "Avid Media Composer", "Unreal Engine", "Unity", "Blender", "Maya", "Adobe Audition", "Pro Tools", "Logic Pro", "Minecraft Education", "Canva", "InDesign", "Figma", "EndNote", "Qualtrics"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
