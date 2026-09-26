"""运动机能学学科论文支持：运动机能学/人体运动体裁、APA 引用样式与运动机能学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="kinesiology",
    aliases=("kinesiology", "运动机能学", "人体运动学", "动作科学", "human movement science"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与运动机能学问题）",
            "methods（研究设计与参与者）",
            "results（运动学与动力学数据）",
            "discussion（机理与应用意义）",
            "references",
        ),
        "biomechanical_study": (
            "abstract",
            "introduction",
            "methods（动作捕捉与力学模型）",
            "results（关节角度/力矩数据）",
            "discussion（与既往研究对比）",
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
    citation_style="APA 样式（作者-年份；J Appl Biomech 遵循 APA 规范）",
    reporting_standards={
        "observational": "观察性研究遵循 STROBE 声明",
        "biomechanical": "生物力学研究遵循 ISB 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "laboratory_study": "实验室研究遵循运动科学报告规范",
        "instrument_validation": "测量工具验证遵循 COSMIN 指南",
    },
    conventions=(
        "关节角度/力矩定义与坐标系须注明",
        "动作捕捉标记方案与采样频率须报告",
        "数据滤波（截止频率、阶数）须明确",
        "参与者特征与纳入标准须报告",
        "统计显著性阈值与效应量须明确",
    ),
    key_venues=(
        "Journal of Applied Biomechanics",
        "Journal of Motor Behavior",
        "Human Movement Science",
        "Journal of Biomechanics",
        "Medicine & Science in Sports & Exercise",
        "Research Quarterly for Exercise and Sport",
    ),
    units_and_formulas_notes=(
        "角度用 deg/rad；力矩用 N·m；角速度用 rad/s",
        "公式用 amsmath；逆动力学与关节力矩计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "效应量给出 Cohen's d 或 η² 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "Vicon 光学运动捕捉系统",
        "表面肌电图（EMG）采集系统",
        "测力台（Kistler）",
        "R 语言运动学数据分析",
        "OpenSim 肌骨建模",
    ),
    category="教育学",
    databases=("CNKI", "万方", "OpenAlex", "PubMed"),
)