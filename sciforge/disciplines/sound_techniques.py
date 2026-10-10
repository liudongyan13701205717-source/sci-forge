"""音响工程学科论文支持：扩声系统/声学测量/信号处理体裁、IET 与 AES 样式与声压级记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sound_techniques",
    aliases=("sound_techniques", "音响工程", "Sound Techniques", "扩声工程", "录音技术", "音频工程", "acoustics engineering", "扩声设计", "音频处理"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="IET / AES 样式（编号引用，如 [1]）",
    reporting_standards={
        "measurement": "报告声压级、计权方式（dB(A)、dB(Z)）、时间计权与背景噪声水平",
        "system_setup": "扩声系统布置、扬声器功率/指向性、处理器链路与分频点须完整给出",
        "subjective_test": "听辨实验须报告听者人数、声压级控制、掩蔽条件与统计方法",
    },
    conventions=(
        "声压级统一标 dB SPL（20 µPa 参考）或 dB(A)，计权与时权标注齐全",
        "混响时间按 RT60 报告（T30 测量法），分频段给 125–4000 Hz 数据",
        "频响曲线标 dB / Hz 双对数刻度，带宽给 3 dB 或 6 dB 截止频率",
        "信号链以流程图给出，含设备型号、增益结构与延迟时间",
        "系统指标（SPL max、THD+N、动态范围）标测试条件与设备编号",
    ),
    key_venues=(
        "Journal of the Audio Engineering Society (JAES)",
        "Audio Engineering Society Convention Proceedings",
        "Archives of Acoustics",
        "Acta Acustica",
        "Applied Acoustics",
    ),
    units_and_formulas_notes=(
        "声压级 dB SPL（ref 20 µPa）；声强级 dB SIL（ref 10⁻¹² W/m²），不得混用",
        "混响时间 RT60 = 6.91·V / A（Sabine 公式，V 体积、A 吸声量）",
        "频谱密度 dB/Hz；信噪比 SNR = 20·log₁₀(P_sig / P_noise)",
        "声功率级 dB re 1 pW（ref 10⁻¹² W），房间声功率与声压级换算注明房间常数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SoundSystemDesigner", "L-Acoustics Sound Vision", "D&B ArrayCalc", "BASS ArrayCalc", "EASE 4.3", "LinguaAcustica ARA", "Room EQ Wizard", "Smaart 7", "Altoneq 扬声器建模", "iZotope RX", "REAPER", "Propellerhead Reason", "Antelope Orion Studio", "Audix iMic 传声器", "GRAS 2250 声级计", "B&K 2256 声分析仪", "SoundPlan 声学仿真", "Matlab Acoustics Toolbox", "Pyroomacoustics", "BASS Live"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
