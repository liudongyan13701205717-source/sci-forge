"""仿生学学科论文支持：仿生学/仿生设计体裁、APA 引用样式与仿生学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bionics",
    aliases=(
        "bionics",
        "biomimetics",
        "biomimetics",
        "bioinspired_engineering",
        "biologically_inspired_design",
        "仿生学",
        "仿生设计",
        "仿生工程",
        "生物启发工程",
        "仿生机理",
        "仿生制造",
    ),
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
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Bruker Skyscan 1272（Micro-CT）", "Zeiss Xradia 610（Micro-CT）", "Zeiss Axio Observer 7（荧光显微镜）", "Olympus VS170（体视显微镜）", "Leica STEMI 2000 M", "JEOL JSM-6510LV（SEM）", "Thermo iRAM One（Raman 光谱）", "Correlated Solutions VIC-3D（DIC）", "IDT 6022 同步相机", "Stratasys Fortus 450（FDM 3D 打印）", "UP Vatool Pro（DLP 光固化）", "Formlabs Form 3+", "Asiga MAX S20", "Carbon DMM Pro（多材料喷射）", "Artec Leo（3D 扫描）", "Shining 3D FreeScan UE Pro", "Fusion 360", "nTopology（点阵与生成式设计）", "Grasshopper（Rhinoceros 参数化）", "Altair Inspire（拓扑优化）", "Altair OptiStruct", "SimScale", "MATLAB", "Python（NumPy / SciPy）", "Bruker Dimension Icon AFM"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "Zenodo", "DOAJ"),
)