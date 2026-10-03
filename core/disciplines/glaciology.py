"""冰川学学科论文支持：冰川/冰盖/冰芯体裁、AGU 引用样式与冰体度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="glaciology",
    aliases=("glaciology", "冰川学", "冰川", "冰盖"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "observational_study": (
            "abstract",
            "introduction",
            "study area（研究区）",
            "data（观测数据）",
            "methods（分析方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "modeling_study": (
            "abstract",
            "introduction",
            "model description（模型描述）",
            "forcing（强迫数据）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="AGU 样式（作者-年份；JGR-Earth Surface 遵循 AGU 规范）",
    reporting_standards={
        "observational": "观测研究遵循冰川观测数据报告规范",
        "modeling": "冰盖模式研究遵循模式评估报告规范",
        "field_study": "野外研究遵循冰川测量报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循数据描述符规范",
    },
    conventions=(
        "冰川与冰盖须明确标识",
        "观测手段（遥感/地面/冰芯）须报告",
        "质量平衡定义须一致",
        "模式配置与强迫数据须说明",
        "不确定性须报告",
    ),
    key_venues=(
        "Journal of Glaciology",
        "Journal of Geophysical Research: Earth Surface",
        "The Cryosphere",
        "Annals of Glaciology",
        "Geophysical Research Letters",
        "Nature Geoscience（冰川方向）",
    ),
    units_and_formulas_notes=(
        "质量平衡用 m w.e./a；流速用 m/a",
        "厚度用 m；面积用 km²",
        "公式用 amsmath；冰流方程须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "时间注明观测时段与基准期",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("R（统计与栅格分析）", "Python（xarray/rasterio/NumPy）", "卫星遥感（Sentinel-1/2、Landsat）",
           "航空激光雷达冰厚测量系统", "冰芯连续流分析系统（CFA）", "差分 GPS 表面位移监测"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Zenodo", "Semantic Scholar"),
)