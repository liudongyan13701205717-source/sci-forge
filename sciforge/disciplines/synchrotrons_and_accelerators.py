"""Synchrotrons And Accelerators 学科论文支持：粒子束学、加速器光学与同步辐射源研究论文体裁、NAPS/APA 引用样式与束流动力学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="synchrotrons_and_accelerators",
    aliases=(
        "synchrotrons_and_accelerators",
        "Synchrotrons And Accelerators",
        "同步辐射与加速器",
        "beam physics",
        "accelerator physics",
        "storage ring",
        "free electron laser",
        "bunch dynamics",
        "accelerator science",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与束流/装置问题）",
            "methods（设备、束流条件与实验方法）",
            "results（束流参数与物理测量结果）",
            "discussion（机制与仪器适用性）",
            "acknowledgements（装置与用户时支持）",
            "references",
        ),
        "technical_note": (
            "abstract",
            "introduction",
            "device description（设备/装置描述）",
            "commissioning results（试运行结果）",
            "performance benchmark（性能基准）",
            "outlook",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview（装置与理论演进）",
            "state of the art（当前技术水平与开放问题）",
            "future directions",
            "references",
        ),
    },
    citation_style="NAPS（加速器物理作者-字母编号）；物理与工程类遵循 APS/IEEE 样式",
    reporting_standards={
        "beam_optics": "束流动力学须报告完整参数集：β/α/μ、emittance、energy spread、time-of-flight 谱",
        "simulation": "数值模拟须报告代码版本、时间步长、粒子数、网格分辨率与守恒量守恒性",
        "measurement": "测量不确定度须按 GUM 分解（Type A/B）合并为扩展不确定度（k=2）",
        "rf_design": "RF 腔体设计须报告 shunt impedance、Q_o/Q_ext、field profile 与热负载",
        "safety": "涉及电离辐射的装置须报告剂量率、屏蔽厚度与辐射安全合规声明",
    },
    conventions=(
        "束流动力学记法：相位空间相空间坐标 (x, x')、Courant–Snyder 参数 β、α、μ；β 函数取最大/最小值位置须注明",
        "能量记法：粒子动能用 T=γmc²-mc²，动量用 p=γmv；电子伏特单位统一 eV/keV/MeV/GeV，避免混用",
        "时间与同步：RF 频率 f_RF、桶宽度 RF buckets 数、时基（lab frame 或 co-moving frame）须显式声明",
        "同步辐射：光子能量用 eV/keV、通量用 photons/s/mrad²/0.1%BW、极化用水平/垂直分量",
        "符号与量纲：符号在首次出现处定义；SI 单位优先，磁场用 T，长度用 mm/cm/m，时间用 ns/ps",
        "装置名缩写首次出现须写全称（如 LCLS-II、ESRF-EBS、SPring-8/BL22UW、Diamond/B19）",
    ),
    key_venues=(
        "Physics of Fluids (Accelerator Science and Technology) / Accelerator Science and Technology (AST)",
        "Physics Review ST - Accelerators and Beams (Phys. Rev. Accel. Beams)",
        "Nuclear Instruments and Methods in Physics Research A",
        "IEEE Transactions on Nuclear Science",
        "Journal of Synchrotron Radiation",
        "Physical Review Letters",
    ),
    units_and_formulas_notes=(
        "运动方程与 Lorentz 力：dp/dt = e(E + v × B)；偏转半径 ρ = p/(eB) = 3.336·p[GeV/c]/B[T]",
        "Lattice 方程：Frenkel–Serret 参考轨道、Twiss 参数 β、α、μ；相空间 emittance ε = γ⟨x²x'² - x x'⟩",
        "RF 方程：dE/dt = eV sin(φ_s)；同步相 φ_s、桶宽度 ΔE=4√(2h|e|Vβ²Ecosφ_s/f_RF/T_0)，粒子质量 m、能量 E",
        "同步辐射功率 P = C_p γ⁴ I / (2π)·ρ²；C_p = 88.5 W/(GeV/c)²/m，能量 100 MeV 以上须显式声明",
        "公式用 amsmath；显式公式仅在正文引用时编号；行内公式避免复杂分式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("CERN Accelerator Toolkit (AT)", "MAD-X", "SixTrack", "astra", "Wakefield", "OPAL", "POTRAK", "GPT-3", "PyGADGET-NG", "ZoltraK", "Gafchrom 剂量胶片", "CERES", "TangDyn / GANSSS", "CST Particle Studio", "ANSYS HFSS", "GIDL / EMD", "Dedalus", "Emittance Measurement Camera (EMC)", "Laser Wire Scanner / Wire Scanner", "CERN Beam Dynamics Python (CERN-BDP)"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv"),
)
