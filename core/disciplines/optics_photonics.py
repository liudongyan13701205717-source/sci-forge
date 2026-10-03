"""光学与光子学论文支持：光学系统设计、激光实验、光场表征。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="optics_photonics",
    aliases=("optics", "photonics", "laser", "光学", "光子学", "激光", "光通信"),
    paper_types={
        "research": ("abstract", "introduction", "principle/design", "methods（实验装置）",
                     "results", "discussion", "conclusions", "references"),
        "experiment": ("abstract", "introduction", "setup（光路图）", "characterization",
                       "results", "uncertainty analysis", "references"),
        "theory": ("abstract", "introduction", "formalism", "derivations", "numerical validation",
                   "discussion", "references"),
    },
    citation_style="OSA/Optica style（编号）",
    reporting_standards={
        "setup": "光路图必须出现（元件型号/焦距/波长）；激光参数（功率/脉宽/重频）须列全",
        "measurement": "探测器型号与带宽、噪声水平与积分时间须报告",
        "uncertainty": "测量不确定度按 GUM 或 Monte Carlo 传播",
        "simulation": "FDTD/FEM 网格收敛验证；材料光学常数来源（Palik/RefractiveIndex.info）",
        "reproducibility": "样品制备与表征（SEM/AFM/XRD）参数给全",
    },
    conventions=(
        "波长以 nm（可见/近红外）或 µm（中远红外）；单位在图轴注明",
        "光路图元件用标准符号；偏振态给庞加莱球或琼斯矢量",
        "光谱图给分辨率与积分时间；效率给绝对值与测量方法",
        "无量纲数（菲涅耳数/光学厚度）定义首次出现处给出",
    ),
    key_venues=(
        "Optica",
        "Nature Photonics",
        "Light: Science & Applications",
        "Optics Letters",
        "Physical Review Applied",
    ),
    units_and_formulas_notes=(
        "功率 mW/W；能量密度 mJ/cm²；强度 W/cm²（注明峰值/平均）",
        "损耗 dB；品质因数 Q=λ/Δλ；消光比 dB",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("LaTeX", "COMSOL", "MATLAB", "Zemax", "光谱仪"),
    category="理学",
    databases=("Crossref", "OpenAlex", "arXiv", "CNKI", "万方"),
)
