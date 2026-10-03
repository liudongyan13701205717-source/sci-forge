"""仿生学学科论文支持：仿生学/仿生设计体裁、APA 引用样式与仿生学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bionics",
    aliases=("bionics", "仿生学", "仿生设计", "生物启发工程", "biomimetics"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与仿生问题）",
            "methods（仿生原理与实现）",
            "results（性能数据）",
            "discussion（仿生机理）",
            "references",
        ),
        "design_study": (
            "abstract",
            "introduction",
            "design（仿生设计与原理）",
            "fabrication（制备与表征）",
            "discussion（与生物原型对比）",
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
    citation_style="APA 样式（作者-年份；Bioinspir Biomim 遵循 IOP 规范）",
    reporting_standards={
        "design": "仿生设计遵循设计报告规范",
        "experimental": "实验研究遵循实验报告规范",
        "computational": "计算模型遵循模型设定报告规范",
        "fabrication": "制备表征遵循材料表征报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "生物原型与仿生映射须明确",
        "制备工艺与参数须可复现",
        "性能测试方法与条件须报告",
        "与生物原型/对照的性能对比须给出",
        "局限性（尺度效应等）须讨论",
    ),
    key_venues=(
        "Bioinspiration & Biomimetics",
        "Advanced Functional Materials",
        "ACS Applied Materials & Interfaces",
        "Journal of the Royal Society Interface",
        "Soft Robotics",
        "Nature Materials",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm/μm；力用 N；刚度用 N/m",
        "公式用 amsmath；仿生结构与力学计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "性能对比给出提升百分比与显著性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("生物力学分析软件", "三维扫描与 3D 打印设备", "运动捕捉系统（Vicon）"),
    category="交叉学科",
    databases=("OpenAlex", "Crossref", "arXiv", "Zenodo"),
)