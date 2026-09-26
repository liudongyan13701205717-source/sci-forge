"""环境科学学科论文支持：污染/生态风险/环境管理体裁、ACS 引用样式与环境度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="environmental_science",
    aliases=("environmental_science", "环境科学", "环境工程", "污染控制"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "materials and methods（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "field_study": (
            "abstract",
            "introduction",
            "study area（研究区）",
            "sampling（采样设计）",
            "analyses（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "risk_assessment": (
            "abstract",
            "introduction",
            "exposure assessment（暴露评估）",
            "hazard assessment（危害评估）",
            "risk characterization（风险表征）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="ACS 样式（编号制；EST 遵循 ACS 规范）",
    reporting_standards={
        "experimental": "实验遵循环境实验报告规范",
        "field_study": "野外研究遵循环境监测报告规范",
        "risk_assessment": "风险评估遵循暴露评估报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循环境数据规范",
    },
    conventions=(
        "采样与分析方法须附标准编号",
        "检出限与质量控制须报告",
        "环境标准（GB/EPA 等）须注明",
        "统计处理须说明",
        "单位须与国际单位一致",
    ),
    key_venues=(
        "Environmental Science & Technology",
        "Water Research",
        "Environmental Pollution",
        "Journal of Hazardous Materials",
        "Science of the Total Environment",
        "Environmental Science and Pollution Research",
    ),
    units_and_formulas_notes=(
        "浓度用 mg/L 或 μg/m³；负荷用 t/a",
        "风险用无量纲指数或概率",
        "公式用 amsmath；风险计算式须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "温度用 °C；pH 无量纲",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集", "报告"),
    tools=("R（统计与空间分析）", "SPSS", "GIS（QGIS/ArcGIS）", "环境监测仪器（气体传感器、水质分析仪）",
           "GC-MS / ICP-MS 分析系统", "Python（NumPy/Pandas）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Zenodo", "Semantic Scholar"),
)