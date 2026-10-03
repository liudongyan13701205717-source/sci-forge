"""操作系统学科论文支持：内核/调度/存储体裁、ACM 引用样式与系统记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="operating_systems",
    aliases=("operating_systems", "操作系统", "OS", "内核"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "design（系统设计）",
            "implementation（实现）",
            "evaluation（评估）",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "architecture（架构）",
            "scheduling（调度）",
            "memory management（内存管理）",
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
    citation_style="ACM 样式（作者-年份；SOSP/OSDI 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验遵循系统论文评估规范",
        "benchmark": "基准测试遵循标准基准（如 SPEC）报告规范",
        "reproducibility": "可复现性遵循系统论文可复现性清单",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_study": "案例研究遵循系统案例报告规范",
    },
    conventions=(
        "内核版本与硬件平台须报告",
        "调度/内存策略参数须说明",
        "测量方法（perf、trace）须透明",
        "对比基线须公平（同配置）",
        "可扩展性实验须报告",
    ),
    key_venues=(
        "SOSP",
        "OSDI",
        "USENIX ATC",
        "ACM Transactions on Computer Systems",
        "IEEE Transactions on Computers",
        "Operating Systems Review",
    ),
    units_and_formulas_notes=(
        "延迟用 ms/μs；吞吐量用 ops/s；内存用 MB/GB",
        "公式用 amsmath；调度算法伪代码须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Linux", "C 编译器（GCC/Clang）", "QEMU"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)