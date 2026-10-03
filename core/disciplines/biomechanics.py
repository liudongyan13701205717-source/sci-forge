"""生物力学学科论文支持：生物力学/人体力学体裁、APA 引用样式与生物力学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biomechanics",
    aliases=("biomechanics", "生物力学", "人体力学", "运动生物力学", "biomechanics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与生物力学问题）",
            "methods（实验设计与测量）",
            "results（力学数据）",
            "discussion（力学机理）",
            "references",
        ),
        "computational_model": (
            "abstract",
            "introduction",
            "model（模型与材料参数）",
            "simulation（仿真与验证）",
            "discussion（与实验对比）",
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
    citation_style="APA 样式（作者-年份；J Biomech 遵循 Elsevier 规范）",
    reporting_standards={
        "experimental": "实验研究遵循运动科学报告规范",
        "computational": "计算模型遵循模型设定报告规范",
        "simulation": "仿真研究遵循仿真实验报告规范",
        "instrument_validation": "测量工具验证遵循验证报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "测量设备与采样频率须报告",
        "坐标系与关节角度定义须明确",
        "数据滤波（截止频率、阶数）须注明",
        "材料参数与边界条件须报告",
        "模型验证与敏感性分析须明确",
    ),
    key_venues=(
        "Journal of Biomechanics",
        "Journal of Applied Biomechanics",
        "Clinical Biomechanics",
        "Journal of the Mechanical Behavior of Biomedical Materials",
        "Annals of Biomedical Engineering",
        "Journal of Biomechanical Engineering",
    ),
    units_and_formulas_notes=(
        "力用 N；力矩用 N·m；应力用 MPa；应变无量纲",
        "公式用 amsmath；逆动力学与有限元计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "模型误差给出 RMSE 与验证指标",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "运动捕捉系统（Vicon）",
        "肌电图采集系统（EMG）",
        "MATLAB 运动学建模",
        "三维测力台",
    ),
    category="交叉学科",
    databases=("PubMed", "OpenAlex", "Crossref", "Zenodo"),
)