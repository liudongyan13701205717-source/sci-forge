"""广播电视设备维修学科论文支持：故障诊断与信号修复的体裁、IEEE 引用样式与测试注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="television_and_radio_repairing",
    aliases=(
        "television_and_radio_repairing",
        "广播电视设备维修",
        "接收机维修",
        "射频故障诊断",
        "音视频设备维修",
        "AV equipment repair",
        "RF fault diagnosis",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与故障问题）",
            "methods（诊断方法与测试仪器配置）",
            "results（测试与修复结果）",
            "discussion（机理分析与讨论）",
            "references",
        ),
        "technical_report": (
            "abstract",
            "introduction",
            "fault description（故障现象与复现条件）",
            "diagnosis（诊断路径与测量数据）",
            "repair and verification（修复与验证）",
            "prevention measures（预防措施）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "evidence synthesis（故障类型统计与处置比较）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号制，电子与电气工程主流规范）",
    reporting_standards={
        "safety": "音视频与信息设备安全遵循 IEC 60065",
        "emc": "广播/电视接收设备电磁兼容遵循 EN 55013 / EN 55022",
        "signal_quality": "视频与射频质量评价遵循 ITU-R BT.500",
        "repair_documentation": "维修技术文件遵循企业维修档案规范与可追溯要求",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "故障模式须给出编号、复现条件与发生频次",
        "波形与频谱须标注通道、比例、触发条件与测量点位置",
        "替换元件须给出型号、参数与批次一致性说明",
        "测试结果须注明仪器型号、量程与校准有效期",
        "高压部位测试须声明断电、放电与个人防护步骤"
    ),
    key_venues=(
        "IEEE Transactions on Consumer Electronics",
        "IEEE Transactions on Industrial Electronics",
        "Electronics Letters",
        "IET Electric Power Applications",
        "Journal of Low Power Electronics and Applications",
    ),
    units_and_formulas_notes=(
        "功率用 dBm/dBW；音频电平用 dBFS 或 dBμV",
        "频率用 Hz/kHz/MHz/GHz；场强用 dB(μV/m)",
        "公式用 amsmath；增益、噪声系数与信噪比公式须编号并被引用",
        "频谱结果须标注采样率、窗口函数与分辨率带宽"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Keysight 示波器", "Tektronix 示波器", "频谱分析仪", "矢量网络分析仪", "信号发生器", "任意波形发生器", "数字万用表", "逻辑分析仪", "视频分析测试仪", "场强仪", "卫星综合测试仪", "功率计", "热风返修台", "恒温电烙铁", "静电手腕带", "LabVIEW", "Proteus", "KiCad", "Altium Designer", "Oscillogram"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
