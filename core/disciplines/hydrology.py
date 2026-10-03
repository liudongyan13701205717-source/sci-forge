"""水文学学科论文支持：水文过程/水资源/水文模型体裁、AGU 引用样式与水文度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hydrology",
    aliases=("hydrology", "水文学", "水文科学", "水资源"),
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
        "modeling_study": (
            "abstract",
            "introduction",
            "model description（模型描述）",
            "calibration and validation（率定与验证）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "field_study": (
            "abstract",
            "introduction",
            "study area（研究区）",
            "data collection（数据采集）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="AGU 样式（作者-年份；WRR 遵循 AGU 规范）",
    reporting_standards={
        "observational": "观测研究遵循水文观测数据报告规范",
        "modeling": "水文模型研究遵循模型率定验证报告规范",
        "field_study": "野外研究遵循流域观测报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循数据描述符规范",
    },
    conventions=(
        "流域与站点信息须报告",
        "数据来源与质量控制须说明",
        "模型率定与验证期须区分",
        "不确定性分析须报告",
        "单位与基准期须一致",
    ),
    key_venues=(
        "Water Resources Research",
        "Journal of Hydrology",
        "Hydrological Processes",
        "Hydrology and Earth System Sciences",
        "Journal of Hydrometeorology",
        "Advances in Water Resources",
    ),
    units_and_formulas_notes=(
        "流量用 m³/s；径流深用 mm；水位用 m",
        "降水用 mm；蒸散发用 mm/d",
        "公式用 amsmath；水量平衡方程须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "时间序列注明时间步长与时段",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("HEC-RAS", "Python", "R", "水文传感器"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)