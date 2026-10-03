"""微电子学学科论文支持：器件/工艺/集成电路体裁、IEEE 引用样式与微电子记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="microelectronics",
    aliases=("microelectronics", "微电子学", "微电子", "集成电路", "半导体器件",
             "芯片"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与微电子问题）",
            "methods（工艺、器件与参数）",
            "results（电学特性数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "device_characterization": (
            "abstract",
            "introduction",
            "device structure（器件结构）",
            "fabrication（制备工艺）",
            "measurement（测试方法）",
            "results and analysis（结果与分析）",
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
        "experimental": "器件测试遵循 IEEE 半导体测试规范",
        "process": "工艺研究遵循 SEMI 标准",
        "reliability": "可靠性遵循 JEDEC 标准",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "simulation": "TCAD 仿真遵循 IEEE 仿真报告规范",
    },
    conventions=(
        "器件尺寸与工艺节点须注明",
        "电学参数（阈值电压、迁移率）定义须一致",
        "测试条件（温度、偏置）须报告",
        "工艺步骤与材料须完整描述",
        "可靠性试验条件须按 JEDEC 说明",
    ),
    key_venues=(
        "IEEE Transactions on Electron Devices",
        "IEEE Electron Device Letters",
        "IEEE Journal of Solid-State Circuits",
        "IEEE Transactions on Semiconductor Manufacturing",
        "Solid-State Electronics",
        "Microelectronics Reliability",
    ),
    units_and_formulas_notes=(
        "电压用 V；电流用 A/μA；尺寸用 nm/μm",
        "公式用 amsmath；器件方程（MOS、BJT）须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "迁移率用 cm²/V·s；掺杂浓度用 cm⁻³",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利", "软件与代码"),
    tools=("Cadence Virtuoso", "Synopsys Design Compiler", "TCAD", "MATLAB",
           "Python（NumPy/SciPy）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "万方"),
)