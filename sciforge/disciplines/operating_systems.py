"""操作系统学科论文支持：内核/调度/存储体裁、ACM 引用样式与系统记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="operating_systems",
    aliases=("operating_systems", "操作系统", "OS", "内核", "Operating System", "Kernels", "系统编程", "System Programming"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ACM 样式",
    reporting_standards={"k1": "系统论文评估规范", "k2": "基准测试报告规范", "k3": "可复现性检查清单"},
    conventions=("内核版本与硬件平台须报告", "调度/内存策略参数须说明", "测量方法须透明", "对比基线须公平"),
    key_venues=("SOSP", "OSDI", "USENIX ATC", "ACM Transactions on Computer Systems", "IEEE Transactions on Computers"),
    units_and_formulas_notes=("延迟用ms/μs", "吞吐量用ops/s", "内存用MB/GB", "复杂度用O(·)记法"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Linux Kernel", "QEMU", "GCC", "Clang", "CMake", "perf", "strace", "LTTng", "Systemtap", "eBPF", "Valgrind", "GDB", "Bochs", "Muen OS", "FreeBSD", "Zircon", "Rust (no_std)", "Zephyr RTOS", "LynxOS", "SystemC"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
