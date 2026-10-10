"""影视制作学科论文支持：影视制作流程、技术工艺与产业研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="film_and_video_production",
    aliases=(
        "film_and_video_production", "影视制作", "影视生产",
        "film production", "video production",
        "电影制作", "电视制作", "影视工业", "影视项目管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（影视制作问题与产业背景）",
            "methodology（制作流程、技术分析、产业调研）",
            "results（制作效果与产业数据）",
            "discussion（与影视工业、技术传播对话）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（影片/项目案例）",
            "analysis（制作流程与技术分析）",
            "results（案例发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（影视制作技术综述）",
            "evidence synthesis（现有研究与缺口）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份；影视产业论著亦常见注-书目）",
    reporting_standards={
        "production": "制作报告须注明预算、周期与人员配置",
        "equipment": "设备参数须注明型号、规格与版本",
        "workflow": "制作流程须注明环节、格式与交付标准",
        "safety": "现场安全须注明风险评估与措施",
    },
    conventions=(
        "预算用统一币种并注明年份",
        "设备参数注明品牌+型号+版本",
        "时间用拍摄天数或工时表示",
        "分辨率与编码注明标准",
        "人员配置注明角色与工时",
    ),
    key_venues=(
        "Screen",
        "Cinema Journal",
        "Journal of Film and Video",
        "Film History",
        "Film Production Magazine",
    ),
    units_and_formulas_notes=(
        "预算用元或美元；工时 h",
        "分辨率 px；帧率 fps；位深 bit",
        "编码率 Mbps；文件体积 GB",
        "照度 lx；色温 K",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("ARRI Alexa Mini", "RED Komodo", "Sony Venice", "Blackmagic URSA Mini Pro", "Canon EOS C700", "DJI Ronin 4D", "Cooke S7/i Prime 定焦镜头组", "Zeiss Supreme Prime", "ARRI SkyPanel", "Aputure 1200d", "Sachtler Fluid Head", "DJI Ronin 2", "SmallHD Cine 700 监视器", "L-UXCUBE Light Meter", "Adobe Premiere Pro", "DaVinci Resolve", "Unreal Engine 5", "ProSound Master / ProTools", "FFmpeg", "Endnote"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
