"""计算机体系结构学科论文支持：微架构/存储/并行体裁、ACM 引用样式与性能记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_architecture",
    aliases=("computer architecture", "计算机体系结构", "微架构",
             "处理器设计", "computer architecture and organization", "并行计算",
             "并行架构", "存储系统", "存储体系结构", "memory architecture",
             "处理器微架构"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work",
            "design",
            "implementation",
            "evaluation",
            "references",
        ),
        "microarchitecture": (
            "abstract",
            "introduction",
            "background",
            "design",
            "implementation",
            "evaluation（含 SPEC/MLPerf 对比）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method",
            "taxonomy",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；ISCA/MICRO 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "评估须报告微架构参数、仿真器与工艺节点",
        "benchmark": "基准测试遵循 SPEC/MLPerf 等标准负载报告规范",
        "simulation": "周期精确/事件驱动仿真须说明参数与配置",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性清单：仿真器版本、负载、种子均须记录",
    },
    conventions=(
        "微架构参数（流水线/缓存/分支预测）须报告",
        "仿真器与工艺节点须说明",
        "性能与功耗须同时报告",
        "基准套件（SPEC/MLPerf 等）须明确",
        "对比设计须公平（同工艺同负载）",
    ),
    key_venues=(
        "International Symposium on Computer Architecture (ISCA)",
        "IEEE/ACM International Symposium on Microarchitecture (MICRO)",
        "International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS)",
        "IEEE International Symposium on High-Performance Computer Architecture (HPCA)",
        "ACM Transactions on Architecture and Code Optimization",
        "IEEE Computer Architecture Letters",
    ),
    units_and_formulas_notes=(
        "性能用 IPC 或周期数；频率用 GHz；功耗用 W",
        "面积用 mm²；工艺用 nm",
        "公式用 amsmath；加速比公式须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "能效用 perf/W 或 perf/mm²",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Verilog", "VHDL", "SystemVerilog", "Chisel", "Vivado", "Quartus", "Xcelium", "VCS", "ModelSim", "Icarus Verilog", "GTKWave", "OpenROAD", "OpenSTA", "OpenLane", "GEM5", "Intel Pin", "Perf", "SPEC CPU", "MLPerf", "ROSE", "LLVM", "Sphinx"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)
