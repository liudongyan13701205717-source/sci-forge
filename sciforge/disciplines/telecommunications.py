"""电信工程学科论文支持：通信系统/网络/信号体裁、IEEE 引用样式与通信记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="telecommunications",
    aliases=("telecommunications", "电信", "通信工程", "通信", "无线通信",
             "通信网络"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与通信问题）",
            "system model（系统模型与假设）",
            "methods（方案设计与分析）",
            "results（性能仿真/实测）",
            "conclusions",
            "references",
        ),
        "protocol_design": (
            "abstract",
            "introduction",
            "protocol design（协议设计）",
            "analysis（理论分析）",
            "simulation/implementation（仿真/实现）",
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
        "simulation": "仿真研究遵循 IEEE 仿真报告规范",
        "field_trial": "外场试验遵循 ITU 试验报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "standardization": "标准化研究遵循 ITU/3GPP 规范引用",
    },
    conventions=(
        "信道模型与参数（衰落、路径损耗）须说明",
        "调制/编码方案与参数须明确",
        "仿真场景与流量模型须可复现",
        "性能指标（吞吐、时延、误码率）定义须一致",
        "标准引用（3GPP、ITU）须给出版本号",
    ),
    key_venues=(
        "IEEE Transactions on Communications",
        "IEEE Transactions on Wireless Communications",
        "IEEE Communications Magazine",
        "IEEE/ACM Transactions on Networking",
        "Computer Networks",
        "IEEE Transactions on Vehicular Technology",
    ),
    units_and_formulas_notes=(
        "速率用 bps/Mbps/Gbps；带宽用 Hz/MHz",
        "公式用 amsmath；信噪比与容量公式须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "误码率/误帧率给出置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("MATLAB/Simulink", "HFSS", "CST Studio Suite", "Python", "OPNET"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)