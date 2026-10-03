"""声学学科论文支持：声学/超声体裁、AIP 引用样式与声学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="acoustics",
    aliases=("acoustics", "声学", "声学工程", "acoustical engineering", "超声",
             "ultrasonics", "建筑声学", "architectural acoustics", "心理声学", "psychoacoustics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与声学问题）",
            "theory（波动方程与边界条件）",
            "methods（解析/数值/实验方法）",
            "results（声场、传递损失或频谱）",
            "discussion（与理论/文献对比）",
            "conclusion",
            "references",
        ),
        "experimental": (
            "abstract",
            "introduction",
            "experimental setup（声源、传声器与消声室/混响室）",
            "measurements（校准与测量方法）",
            "results（声压级、指向性或吸声系数）",
            "discussion（不确定度与物理解释）",
            "references",
        ),
        "computational": (
            "abstract",
            "introduction",
            "model（几何与声学边界）",
            "numerical method（FEM/BEM/射线法）",
            "results（声场分布与频率响应）",
            "validation（与测量对比）",
            "references",
        ),
    },
    citation_style="AIP 样式（作者-年份；JASA 遵循 AIP 规范）",
    reporting_standards={
        "sound_levels": "声压级用 dB SPL 并注明参考值（20 \\mu Pa）",
        "frequency_analysis": "频谱分析须说明窗函数、FFT 参数与频率分辨率",
        "calibration": "测量系统校准方法与标准（IEC/ISO）须报告",
        "boundary_conditions": "声学边界（刚性/吸收/阻抗）须定义",
        "uncertainty": "测量不确定度与重复性须报告",
    },
    conventions=(
        "声压 p 与声压级 L_p 定义（L_p = 20 log10(p/p_0)）须给出",
        "频率用 Hz，倍频程/1/3 倍频程带须注明标准",
        "吸声系数 \\alpha 与传递损失 TL 定义须给出",
        "指向性图标注角度与频率",
        "心理声学量（响度、音调）注明所用模型（如 Moore 模型）",
    ),
    key_venues=(
        "Journal of the Acoustical Society of America (JASA)",
        "Journal of Sound and Vibration",
        "Applied Acoustics",
        "Ultrasonics",
        "IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control",
        "Noise Control Engineering Journal",
    ),
    units_and_formulas_notes=(
        "声压用 Pa，声压级用 dB（参考 20 \\mu Pa），声强级参考 10^-12 W/m^2",
        "空气中声速 c ≈ 343 m/s（20°C）须注明温度依赖",
        "公式用 amsmath；波动方程与 Helmholtz 方程记号统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出频率范围与误差估计",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("MATLAB", "Python (NumPy/SciPy)", "COMSOL", "Simulink", "Origin"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar", "Zenodo"),
)