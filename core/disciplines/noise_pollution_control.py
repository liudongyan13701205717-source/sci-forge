"""噪声污染控制学科论文支持：声环境评价/降噪措施/振动控制体裁、ISO 引用样式与声学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="noise_pollution_control",
    aliases=("noise_pollution_control", "噪声污染控制", "noise control",
             "声学", "acoustics", "声环境", "sound environment",
             "振动控制", "vibration control"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与噪声问题）",
            "methodology（测量与仿真方法）",
            "results（声压级与频谱数据）",
            "discussion（机理与控制措施）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例场景与源）",
            "analysis（传播路径与受体）",
            "results（噪声影响与整改）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（声学与心理声学理论）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ISO 样式（作者-年份，ANSI/ISO 引用规范）",
    reporting_standards={
        "measurement": "声压级测量遵循 ISO 1996 系列",
        "prediction": "噪声预测遵循 ISO 9613 系列",
        "regulatory": "限值遵循 GB 3096-2008 声环境质量标准",
        "lab": "实验室条件遵循 ISO 3741",
        "data": "数据集遵循 ISO 9612 报告规范",
    },
    conventions=(
        "声压级单位 dB(A)，加权须注明",
        "频率用 Hz 或 kHz，倍频程须标明",
        "距离用 m，衰减用 dB",
        "公式用 amsmath；显示公式编号",
        "样本量与持续时间须标注",
    ),
    key_venues=(
        "Applied Acoustics",
        "Journal of Sound and Vibration",
        "Noise Control Engineering",
        "建筑声学",
        "噪声与振动控制",
        "Sound & Vibration",
    ),
    units_and_formulas_notes=(
        "声压级 dB(A)；频率 Hz/kHz",
        "功率谱密度 dB/Hz",
        "距离 m；衰减 dB/m",
        "统计用 amsmath；显示公式编号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CadnaA", "SoundPLAN", "ARCMID", "LMS Test.Lab", "Artemis SOL", "COMSOL Multiphysics", "ANSYS Acoustics", "MATLAB", "Python (NumPy, SciPy)", "R", "B&K PULSE", "SPLN", "FLAC3D", "Actran", "AVLfire", "ODEON", "B&K Sound Level Meter", "Brüel & Kjær", "Sound Level Calibrator", "Spectrum Analyzer"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
