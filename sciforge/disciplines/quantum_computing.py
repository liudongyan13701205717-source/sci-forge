"""量子计算论文支持：算法与复杂度、硬件实验、误差分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="quantum_computing",
    aliases=("quantum computing", "quantum", "qubit", "量子计算", "量子信息",
             "量子算法", "vqe", "qaoa"),
    paper_types={
        "algorithm": ("abstract", "introduction", "preliminaries", "algorithm description",
                      "analysis（复杂度/资源估计）", "numerical experiments", "conclusion", "references"),
        "hardware": ("abstract", "introduction", "device architecture", "control and calibration",
                     "results（保真度）", "error analysis", "references"),
        "theory": ("abstract", "introduction", "formalism", "theorems and proofs",
                   "discussion", "open problems", "references"),
    },
    citation_style="REVTeX（APS）或 ACM",
    reporting_standards={
        "gates": "门保真度给 randomized benchmarking（RB）结果与误差棒；两比特门单独报告",
        "device": "量子比特数、拓扑（heavy-hex/格点）、相干时间 T1/T2 须列全",
        "simulation": "经典模拟给状态向量/张量网络方法与规模限制；随机种子固定",
        "resources": "资源估计（T-count/T-depth/电路深度）注明假设（全连通/all-to-all）",
        "noise": "噪声模型（去极化/退相位）与误差缓解方法（ZNE/PEC）须描述",
    },
    conventions=(
        "狄拉克记号一致；密度矩阵 ρ 与纯态 |ψ⟩ 区分使用",
        "量子线路图用标准门符号；测量基说明（计算基/泡利基）",
        "保真度定义（态/门/过程）首次出现处说明",
        "结果图给 shot 数与统计误差；暗计数与读出误差处理说明",
    ),
    key_venues=(
        "Quantum",
        "npj Quantum Information",
        "Physical Review X",
        "Physical Review A",
        "PRX Quantum",
    ),
    units_and_formulas_notes=(
        "相干时间 µs/ms；门时间 ns；保真度 %（附置信区间）",
        "保极化/交叉熵基准（XEB）注明 circuit 参数",
    ),
)
