"""火山学学科论文支持：喷发/监测/岩石学体裁、AGU 引用样式与火山度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="volcanology",
    aliases=("volcanology", "火山学", "火山地质", "火山监测"),
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
        "field_study": (
            "abstract",
            "introduction",
            "geological setting（地质背景）",
            "field observations（野外观察）",
            "analyses（分析）",
            "discussion（讨论）",
            "references",
        ),
        "monitoring_study": (
            "abstract",
            "introduction",
            "monitoring network（监测网络）",
            "data（监测数据）",
            "analysis（分析）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="AGU 样式（作者-年份；JGR-Solid Earth 遵循 AGU 规范）",
    reporting_standards={
        "observational": "观测研究遵循火山监测数据报告规范",
        "field_study": "野外研究遵循地质观察报告规范",
        "modeling": "喷发建模研究遵循模型报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "hazard": "火山危险性遵循危险性评估报告规范",
    },
    conventions=(
        "火山与喷发事件须明确标识",
        "监测手段（地震/形变/气体）须报告",
        "样品与分析方法须说明",
        "喷发规模（VEI）须注明",
        "时间序列须注明时间分辨率",
    ),
    key_venues=(
        "Journal of Volcanology and Geothermal Research",
        "Bulletin of Volcanology",
        "Journal of Geophysical Research: Solid Earth",
        "Geophysical Research Letters",
        "Volcanica",
        "Geology",
    ),
    units_and_formulas_notes=(
        "喷发物用 km³ 或 m³；温度用 °C",
        "形变用 mm；气体通量用 t/d",
        "公式用 amsmath；喷发动力学公式须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "坐标用经纬度并注明基准",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("GIS", "MATLAB", "地震监测仪", "气体监测仪"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)