"""电气工程学科论文支持：电力系统/电机/电力电子体裁、IEEE 引用样式与电气记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electrical_engineering",
    aliases=("electrical_engineering", "电气工程", "电气", "电力系统",
             "电力电子", "电机"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与电气问题）",
            "methods（建模、控制与实验）",
            "results（波形、效率与验证）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "power_system_study": (
            "abstract",
            "introduction",
            "system model（系统建模与数据）",
            "methodology（潮流/稳定/保护分析）",
            "case studies（算例与场景）",
            "conclusions",
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
        "power_system_study": "电力系统研究遵循 IEEE 399 工业电力系统手册",
        "safety": "电气安全遵循 IEEE C2 国家电气安全规范（NESC）",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "simulation": "仿真研究遵循 IEEE 仿真报告规范",
    },
    conventions=(
        "电压/电流/功率符号与单位（V、A、W、VA）须规范",
        "相量/复数表示须明确（幅值-相角或实部-虚部）",
        "电力系统基准值（base）与标幺值须说明",
        "控制框图与传递函数须完整给出",
        "仿真软件与求解器参数须报告",
    ),
    key_venues=(
        "IEEE Transactions on Power Systems",
        "IEEE Transactions on Power Delivery",
        "IEEE Transactions on Industry Applications",
        "IET Generation, Transmission & Distribution",
        "Electric Power Systems Research",
        "IEEE Transactions on Power Electronics",
    ),
    units_and_formulas_notes=(
        "电压用 V/kV；电流用 A/kA；功率用 W/MW",
        "公式用 amsmath；潮流/稳定方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "暂态分析给出时间常数与稳定裕度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("MATLAB/Simulink", "PSCAD", "PSIM", "LTspice"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)