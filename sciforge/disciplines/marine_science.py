"""海洋科学学科论文支持：物理/化学/生物/地质海洋体裁、海洋采样与统计规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="marine_science",
    aliases=("marine_science", "海洋科学", "海洋科学学", "海洋学", "物理海洋学",
             "Marine Science", "Ocean Science", "Oceanography", "物理海洋学", "化学海洋学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、气候与科学问题）",
            "study area（研究海域与生境）",
            "materials and methods（航次、站位、仪器、数据处理）",
            "results（观测、模式或统计结果）",
            "discussion（机制、气候与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域或事件描述）",
            "analysis（过程与驱动）",
            "results（关键指标）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（物理/化学/生物/地质综述）",
            "evidence synthesis（多源证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 / GSA 样式（物理海洋与地球科学常用）",
    reporting_standards={
        "sampling": "海洋采样须遵循 GOOS/ICES 采样与航次规范",
        "CTD": "CTD 剖面须报告深度、盐度、温度、溶解氧、荧光",
        "chemistry": "化学分析须遵循 ASTM/EPA/ISO 水质规范",
        "data_processing": "数据处理须报告插值、平均、滤波与不确定性",
        "climate_model": "模式结果须遵循 CMIP6 报告规范",
    },
    conventions=(
        "坐标采用 WGS84 十进制度，深度采用米（m）",
        "海洋变量须给出单位：温度（℃）、盐度（PSU）、pH（SW）",
        "观测时间须以 UTC 报告并注明航次与船名",
        "气候/变化研究须给出统计显著性与置信区间",
        "模式与观测对比须给出 RMSE/bias 等检验指标",
    ),
    key_venues=(
        "Journal of Geophysical Research: Oceans",
        "Deep-Sea Research Part I",
        "Marine Chemistry",
        "Progress in Oceanography",
        "Ocean Science",
        "Climate Dynamics",
    ),
    units_and_formulas_notes=(
        "温度单位：℃；盐度：PSU；密度：kg/m³",
        "流量：Sv（1 Sv = 10⁶ m³/s）",
        "湍流动能 ε 单位：m²/s³；涡黏度 ν_T 单位：m²/s",
        "溶解氧 DO 单位：μmol/kg 或 mg/L",
        "pH 单位：无量纲（SW 标尺）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("CTD 剖面仪（Sea-Bird SBE 9119）", "Argo 浮标", "水下滑翔机（Slocum Glider）", "波浪浮标与气象浮标", "声学多普勒流速剖面仪（ADCP，Riverdee）", "回声探深仪（Sub-Bottom Profiler）", "水样采集瓶（Niskin Riser）", "溶解氧传感器（Aqua TROLL）", "光谱仪/荧光仪（Wet Labs）", "质谱仪（ICP-MS、HRMS）", "激光粒度仪", "稳定同位素质谱（IRMS）", "卫星遥感（SeaWiFS/Modis/Aqua）", "全球海洋环流模式（MITgcm/MITgcm）", "区域海洋模式（ROMS/Mom6）", "气候模式（CESM/CMIP6）", "MATLAB（数据处理）", "Python（xarray/netCDF4）", "NetCDF 与 CF 规范", "海洋观测船（破冰船/调查船）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Argo Data", "NOAA"),
)
