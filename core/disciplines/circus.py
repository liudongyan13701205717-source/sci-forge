"""Circus 学科论文支持：马戏艺术/技艺研究/表演科学体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="circus",
    aliases=(
        "Circus", "circus", "circus arts", "circus performance",
        "circus studies", "contemporary circus",
        "马戏", "马戏艺术", "马戏技艺", "马戏表演研究", "现代马戏",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（技艺/演出语境与研究问题）",
            "methodology（田野观察、运动分析、观众研究）",
            "findings（技艺结构、身体力学、观众互动）",
            "discussion（与表演研究/舞蹈学/运动科学对话）",
            "conclusion",
            "references",
        ),
        "movement_analysis": (
            "abstract",
            "introduction",
            "skills_description",
            "biomechanics_setup",
            "results",
            "discussion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "performance_description",
            "analysis",
            "references",
        ),
    },
    citation_style="APA 7 样式（表演艺术论著亦常见 Chicago 风格）",
    reporting_standards={
        "skills": "技巧描述采用业内通用术语；动作分阶段拆解",
        "biomechanics": "运动学量报告采样率、标记点、坐标系统与关节中心估计方法",
        "safety": "高空/旋转/道具类技巧报告防护装置、教练/安全人员配置与场地参数",
        "fieldwork": "驻场/排练田野遵循 IRB 伦理审查与知情同意",
        "choreography": "群舞/编排分析采用 Laban/Bartenieff/RST 等标准编码",
    },
    conventions=(
        "技巧名称首次出现给出正式名称（若为行业黑话，附中文译名与源语言）",
        "动作时间以秒/拍报告；运动学量单位 mm/s、deg、deg/s 一致",
        "道具/装置参数（质量 kg、长度 m、扭矩 N·m）首次出现定义",
        "影像资料引用给出时间码、机位与录制规格",
        "引用剧目首次出现给出团体、演出年份、场地、时长",
    ),
    key_venues=(
        "Performance Research",
        "Research in Drama, Theater and Performance",
        "Society for Theatre Research Bulletin",
        "Contemporary Dance Research",
        "Journal of Circus Arts",
        "Theatre Research International",
    ),
    units_and_formulas_notes=(
        "动作时间秒；采样率 Hz；关节角度 deg",
        "力/扭矩 N、N·m；功率 W；速度 m/s；角速度 rad/s",
        "道具质量 kg、线密度 kg/m、转动惯量 kg·m²",
        "视频分析帧率 fps；同步以 NTP/PTP 时间戳",
        "统计报告均值±SD 或中位数（IQR），效应量给出 Cohen's d",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Vicon 光学运动捕捉系统", "OptiTrack 光学动捕", "Xsens MVN 惯性动捕", "Noitom Perception Neuron", "IMU 惯性运动捕捉", "Kistler 力板/测力台", "AMTI 测力台", "Biodex 等速肌力", "MyotonPRO 肌硬度", "Delsys 表面 EMG", "NEMeT 无线 EMG", "Adobe Premiere Pro", "DaVinci Resolve", "Final Cut Pro", "After Effects", "Motion 5", "Labanotation（舞谱）", "Benesh Movement Notation", "Eshkol-Wachman Movement Notation", "Kinetisys Notation Studio", "Adobe Acrobat Pro", "iZotope RX", "Pro Tools", "Logic Pro X", "Photoshop", "Illustrator", "Unreal Engine 5", "Unity", "R 统计软件", "SPSS Statistics", "JASP", "NVivo 质性分析"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "Arts & Humanities Citation Index"),
)
