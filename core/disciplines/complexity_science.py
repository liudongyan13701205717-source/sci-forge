"""复杂性科学学科论文支持：复杂性科学/复杂系统体裁、APA 引用样式与复杂性科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="complexity_science",
    aliases=("complexity_science", "复杂性科学", "复杂系统", "复杂性研究", "complex systems"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与复杂性问题）",
            "methods（模型与数据）",
            "results（涌现与动力学数据）",
            "discussion（普适规律）",
            "references",
        ),
        "computational_model": (
            "abstract",
            "introduction",
            "model（模型架构与规则）",
            "simulation（仿真与相变分析）",
            "discussion（与实证对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Complexity 遵循 APA 规范）",
    reporting_standards={
        "computational": "计算模型遵循模型设定报告规范",
        "simulation": "仿真研究遵循仿真实验报告规范",
        "empirical": "实证研究遵循数据来源报告规范",
        "network_analysis": "网络分析遵循网络研究报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "模型规则与参数设定须可复现",
        "涌现指标（序参量、标度指数等）须定义",
        "仿真运行次数与初始条件须报告",
        "相变与临界现象判定标准须明确",
        "随机种子与敏感性分析须报告",
    ),
    key_venues=(
        "Complexity",
        "Chaos, Solitons & Fractals",
        "Physica A",
        "Journal of Complex Networks",
        "Advances in Complex Systems",
        "Scientific Reports",
    ),
    units_and_formulas_notes=(
        "标度指数无量纲；时间步用 t",
        "公式用 amsmath；标度律与熵计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与运行次数",
        "相变点给出临界值与误差估计",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=(
        "Python 计算建模（NumPy/SciPy）",
        "MATLAB 数值计算",
        "Agent-Based 建模平台（NetLogo）",
        "元胞自动机仿真",
    ),
    category="交叉学科",
    databases=("arXiv", "OpenAlex", "Crossref", "Zenodo"),
)