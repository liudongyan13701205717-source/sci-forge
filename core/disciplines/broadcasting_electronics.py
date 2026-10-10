"""广播电视与电子技术学科：射频/天线/信号处理研究方法、测试仪器与标准约束。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="broadcasting_electronics",
    aliases=("broadcasting_electronics", "广播电视电子", "Broadcasting electronics",
             "broadcast engineering", "广播电视工程", "电子与传播技术", "broadcast technology",
             "电视工程技术", "radio broadcasting"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "system model and theory（系统模型、链路预算与理论分析）",
            "design / experimental setup（系统实现、硬件平台与测试条件）",
            "results（性能指标：SNR、BER、SFDR、噪声系数等）",
            "comparison and discussion（与现有标准/方案的对比）",
            "conclusion",
            "references",
        ),
    },
    citation_style="IEEE 样式（数字编号 [1]，作者-年份可选）",
    reporting_standards={
        "measurements": "给出测试仪器型号、带宽、采样率与校准条件；可复现",
        "standards": "对标标准写明版本（如 DVB-T2、MPEG-2/4/7、ATSC 3.0、H.265/266）",
        "simulation": "仿真参数（时长、随机种子、调制方式）须与实验结果分开标注",
        "metrics": "指标定义统一（信噪比、误差向量误差 EVM、频谱占用比等）并给测量方法",
    },
    conventions=(
        "射频/微波电路须给版图面积、功耗与工作温度范围；指标附测量方法",
        "频谱与调制分析区分单载波与多载波（OFDM）口径，采样率与奈奎斯特条件显式写明",
        "系统级结果与器件级结果分开呈现；仿真与实测结果分别标注，不混排",
    ),
    key_venues=(
        "IEEE Transactions on Broadcasting",
        "IEEE Transactions on Circuits and Systems I: Regular Papers",
        "IEEE Transactions on Antennas and Propagation",
        "IEEE Journal of Solid-State Circuits",
        "Signal, Image and Video Processing (Springer)",
        "Proceedings of the IEEE International Symposium on Circuits and Systems (ISCAS)",
    ),
    units_and_formulas_notes=(
        "射频指标用 dB/dBm/dBi 表示（增益、EIRP、天线增益）；时基统一为 ns/μs/ms",
        "频谱图给分辨率带宽（RBW）与视频带宽（VBW）；误码率曲线标注仿真/实测点",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "GNU Radio", "SDR (USRP / HackRF / BladeRF)", "Vector Network Analyzer (R&S ZNA)", "Spectrum Analyzer (R&S FSW)", "Oscilloscope (Keysight InfiniiVision)", "LTspice", "ADS (Advanced Design System)", "CST Studio Suite", "HFSS", "Ansys AEDT", "Python (NumPy/SciPy/MNE)", "FFTW", "OpenCV", "ffmpeg", "MPEG codec (x264/x265)", "OBS Studio", "VLC Media Player", "GStreamer", "FFmpeg graph", "MediaInfo", "Jamf (media QA)", "HDMI test equipment (Tektronix)", "SMPTE color bars generator"),
    category="工学",
    databases=("OpenAlex", "Crossref", "IEEE Xplore", "arXiv"),
)
