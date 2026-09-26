"""高性能计算学科论文支持：并行计算/超算体裁、ACM 引用样式与 HPC 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="high_performance_computing",
    aliases=("high_performance_computing", "高性能计算", "HPC", "并行计算",
             "超级计算"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "method（方法）",
            "implementation（实现）",
            "evaluation（评估）",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "architecture（架构）",
            "parallelization（并行化）",
            "optimization（优化）",
            "evaluation（评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；SC 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验遵循 HPC 论文评估规范",
        "benchmark": "基准测试遵循 TOP500/标准基准报告规范",
        "reproducibility": "可复现性遵循 HPC 可复现性清单",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_study": "案例研究遵循系统案例报告规范",
    },
    conventions=(
        "硬件平台与规模须报告",
        "并行策略与通信模式须说明",
        "强/弱扩展性须报告",
        "对比基线须公平（同硬件）",
        "能耗与效率须报告",
    ),
    key_venues=(
        "SC",
        "ICS",
        "PPoPP",
        "IEEE Transactions on Parallel and Distributed Systems",
        "Journal of Parallel and Distributed Computing",
        "Parallel Computing",
    ),
    units_and_formulas_notes=(
        "性能用 FLOPS/TFLOPS；时间用 s；效率用 %",
        "公式用 amsmath；并行算法须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Python（NumPy）", "MATLAB", "CUDA", "OpenMPI"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)