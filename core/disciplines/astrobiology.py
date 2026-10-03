"""天体生物学学科论文支持：天体生物学/地外生命体裁、APA 引用样式与天体生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="astrobiology",
    aliases=("astrobiology", "天体生物学", "地外生命", "宜居性研究", "astrobiology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与天体生物学问题）",
            "methods（实验与观测方法）",
            "results（宜居性与生命信号数据）",
            "discussion（生命起源与分布）",
            "references",
        ),
        "observational_study": (
            "abstract",
            "introduction",
            "methods（观测与仪器）",
            "results（光谱与遥感数据）",
            "discussion（与理论对比）",
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
    citation_style="APA 样式（作者-年份；Astrobiology 遵循 Liebert 规范）",
    reporting_standards={
        "observational": "观测研究遵循仪器与数据处理报告规范",
        "laboratory": "实验室研究遵循实验报告规范",
        "computational": "计算模型遵循模型设定报告规范",
        "field_study": "野外研究遵循采样与污染控制报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "仪器校准与数据处理流程须报告",
        "污染控制与灭菌措施须注明",
        "生命信号判定标准须明确",
        "行星环境参数（温度、辐射等）须报告",
        "不确定性传播须明确",
    ),
    key_venues=(
        "Astrobiology",
        "Nature Astronomy",
        "Icarus",
        "The Planetary Science Journal",
        "Origins of Life and Evolution of Biospheres",
        "Journal of Geophysical Research: Planets",
    ),
    units_and_formulas_notes=(
        "辐射用 Gy/W·m⁻²；温度用 K；距离用 AU/pc",
        "公式用 amsmath；宜居带与辐射计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "观测误差给出置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=(
        "光谱分析软件（PyAstronomy）",
        "望远镜数据处理管线（JWST 观测数据）",
        "Python 科学计算",
        "GIS 行星表面制图",
    ),
    category="交叉学科",
    databases=("arXiv", "OpenAlex", "Crossref", "PubMed"),
)