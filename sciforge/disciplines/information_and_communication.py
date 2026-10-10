"""信息与通信学科论文支持：通信系统、信息传输与传播理论的跨学科研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_and_communication",
    aliases=(
        "information_and_communication",
        "信息与通信",
        "信息通信",
        "通信工程",
        "信息传输",
        "information and communication systems",
        "communication theory",
        "信息通信工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（通信工程）或 GB 样式（国内期刊）",
    reporting_standards={
        "system_design": "系统设计须报告频谱效率、BER 与吞吐率",
        "experimental": "实验须注明硬件平台、参数与可复现性配置",
        "simulation": "仿真须注明工具版本、信道模型与收敛条件",
        "field_trial": "现场试验须注明测试时长、地理分布与干扰条件",
    },
    conventions=(
        "误码率（BER）须注明调制方式与编码",
        "频谱效率单位统一为 bit/s/Hz",
        "天线参数须注明增益、方向图与极化方式",
        "信道模型须注明（Rayleigh/Rician/3GPP）",
        "仿真须注明随机种子与样本数",
    ),
    key_venues=(
        "IEEE Transactions on Communications",
        "IEEE Transactions on Information Theory",
        "IEEE Transactions on Wireless Communications",
        "Journal of Communications and Networks",
        "通信学报",
    ),
    units_and_formulas_notes=(
        "带宽单位用 Hz/kHz/MHz/GHz，须注明频段",
        "误码率须注明 10⁻⁵~10⁻⁹ 量级",
        "香农容量 C = B log₂(1 + S/N) 须注明 S/N 计算口径",
        "延迟用 ms/μs，须注明单向/往返",
        "统计量须给 95% CI，仿真须给样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB（通信仿真）", "Python（numpy/scipy）", "GNU Radio（软件定义无线电）", "NS-3（网络仿真）", "OPNET（网络建模）", "CST（电磁仿真）", "ANSYS HFSS（高频电磁）", "Mathematica（解析推导）", "Spike（通信协议栈）", "Xilinx（FPGA 实现）", "National Instruments（数据采集）", "Keysight（网络分析仪）", "Rohde & Schwarz（频谱分析）", "Python（scipy.signal）", "ECharts（结果可视化）", "Docker（可复现性）", "GSL（科学计算库）", "Python（scikit-learn 检测算法）", "MATLAB Simulink", "Wireshark（协议分析）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
