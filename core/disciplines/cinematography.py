"""Cinematography 学科论文支持：电影摄影/影像制作体裁、电影学与运动科学分析规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cinematography",
    aliases=(
        "Cinematography", "cinematography", "cinematography studies",
        "film photography", "director of photography",
        "电影摄影", "摄影指导", "电影视觉", "摄影艺术", "电影灯光",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（影像研究问题与美学/技术视角）",
            "methodology（分析框架：镜头语法、光色学、影像计量）",
            "findings（镜头/光影/色彩/构图分析）",
            "discussion（与电影史/观众研究对话）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "film_description",
            "shot_analysis",
            "production_context",
            "references",
        ),
        "technique_review": (
            "abstract",
            "introduction",
            "equipment_review（相机/镜头/软件）",
            "workflow_test",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份；电影学论著亦常见 Chicago 风格）",
    reporting_standards={
        "shot_analysis": "镜头分析须注明镜号、时间码、焦距、光圈、快门与快门角",
        "camera_specs": "报告相机型号、传感器尺寸、动态范围、ISO 与色彩科学",
        "color_grading": "调色报告注明 LUT、色彩空间（ACES / Rec.709）与 HDR 范围",
        "lighting": "灯光设计报告色温 K、照度 lx 与布光方案（三点/环形/高对比等）",
        "audio_sync": "音视频同步报告采样率、时间码格式与同步方式",
    },
    conventions=(
        "影像描述给出时间码（HH:MM:SS:FF）、镜号、焦距（mm）、光圈（f）、快门（度或秒）",
        "色彩科学名词（ACES、DCI-P3、Rec.2020、sRGB）首次出现须给出全称与缩写",
        "景别/机位/运动术语（远景、广角、滑轨、斯坦尼康）使用行业中文标准或首次双语",
        "摄影器材报告品牌+型号+版本；虚拟制作报告 LED 屏参数与跟踪系统",
        "引用作品首次出现给出片名（英文原名+译名）、导演、年份、时长与发行方",
    ),
    key_venues=(
        "Camera Work",
        "Film & Video",
        "Screen",
        "Film History",
        "Cinema Journal",
        "Editing: A Journal of Film and Video",
    ),
    units_and_formulas_notes=(
        "曝光值用 EV；照度 lx；色温 K；帧率 fps；动态范围 dB",
        "焦距 mm；光圈 f/值；快门角（度）或秒",
        "分辨率以 MP 或 px 报告；色深 bit；位深 8/10/12-bit",
        "镜头数据文件（.mft / .mxf）引用标准（如 SMPTE ST 2110 / IMF）",
        "色度学参数（x, y, Y, ΔE）报告 CIE 标准",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Adobe Premiere Pro", "DaVinci Resolve", "Avid Media Composer", "Final Cut Pro", "Autodesk Maya", "Autodesk 3ds Max", "Houdini", "Nuke", "Motion 5", "ARRI Alexa Mini", "ARRI Alexa LF", "RED Komodo / V-RAPTOR", "Sony Venice", "Canon EOS C700", "Blackmagic URSA / URSA Mini Pro", "Panavision C-Series", "Cooke S7/i Prime 定焦镜头组", "Zeiss Supreme Prime", "Angenieux Optimo 变焦", "Teradek Bolt / Wireless Video Transmitter", "Teradek Sphere", "DJI Ronin 4D", "L-UXCUBE Light Meter", "Sekonic C-800", "Light Illusion LightGrid", "ARRI SkyPanel", "ARRI M-Series LED", "ARRI L-Series HMI", "ARRI L-Series Tungsten", "ARRI L-Series Fresnel", "ARRI L-Series SkyPanel Edge", "ARRi L-Series PAR Light", "Aputure 1200/600d 灯", "Mole-Richardson M-Series", "Astera Titan Tube", "LITECH 移动监控", "SmallHD Cine 700 监视器", "Blackmagic Video Assist", "Teradek Cube", "ARRI WAND 云台", "DJI Ronin 2", "Sachtler Fluid Head", "OConnor 摄影机云台", "ProSound Master / ProTools", "Logic Pro X", "Adobe Audition", "iZotope RX", "Unreal Engine 5（虚拟制作）", "Nuke 合成", "Trapcode / Element 3D", "Photoshop", "Lightroom", "Camera Raw", "DaVinci Resolve Fairlight", "CinemaDNG 后期工具"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "AFI Catalog", "A&C Index"),
)
