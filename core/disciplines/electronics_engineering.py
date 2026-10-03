"""电子工程学科论文支持：电路/器件/集成电路体裁、IEEE 引用样式与电子记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electronics_engineering",
    aliases=("electronics_engineering", "电子工程", "电子", "集成电路",
             "电路设计", "电子器件"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与电子问题）",
            "methods（电路/器件设计与工艺）",
            "results（特性曲线与性能）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "circuit_design": (
            "abstract",
            "introduction",
            "architecture（架构与指标）",
            "circuit implementation（电路实现）",
            "measurement results（流片/实测结果）",
            "comparison（与同类工作对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号制；IEEE 期刊遵循 IEEE 规范）",
    reporting_standards={
        "experimental": "实验研究遵循 IEEE 实验报告规范",
        "circuit_design": "电路设计遵循 IEEE 电路与系统报告规范",
        "reliability": "器件可靠性遵循 JEDEC 可靠性试验标准",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "simulation": "仿真研究遵循 IEEE 仿真报告规范",
    },
    conventions=(
        "器件参数（阈值电压、跨导等）符号须规范",
        "工艺节点与器件尺寸须注明",
        "版图/原理图术语须统一",
        "测量条件（温度、电源电压）须报告",
        "功耗与面积等指标须给出",
    ),
    key_venues=(
        "IEEE Journal of Solid-State Circuits",
        "IEEE Transactions on Electron Devices",
        "IEEE Transactions on Circuits and Systems I",
        "IEEE Electron Device Letters",
        "Electronics Letters",
        "Solid-State Electronics",
    ),
    units_and_formulas_notes=(
        "电压用 V/mV；电流用 A/mA/µA；频率用 Hz/GHz",
        "公式用 amsmath；传递函数与噪声方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "噪声/带宽分析给出具体数值与单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利", "软件与代码"),
    tools=("KiCad", "Altium Designer", "LTspice", "MATLAB"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)