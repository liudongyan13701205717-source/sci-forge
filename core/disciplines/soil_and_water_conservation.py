"""水土保持学科论文支持：侵蚀模型/防治工程/水文监测体裁、SSSA 样式与水土记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="soil_and_water_conservation",
    aliases=(
        "soil_and_water_conservation",
        "水土保持",
        "土壤侵蚀",
        "水土流失防治",
        "水土保持工程",
        "soil conservation",
    ),
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
        "experimental_study": (
            "abstract",
            "introduction",
            "experimental design（实验设计）",
            "treatments（处理）",
            "measurements（测定）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="SSSA 样式（作者-年份；SSSAJ 遵循美国土壤学会规范）",
    reporting_standards={
        "experimental": "实验遵循水土保持实验报告规范",
        "field_study": "野外研究遵循水土保持调查报告规范",
        "observational": "观察研究遵循水土保持观测报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "研究区地理位置与地形须报告",
        "采样点与采样深度须说明",
        "侵蚀模型与参数须注明",
        "统计处理须说明",
        "单位须与国际单位一致",
    ),
    key_venues=(
        "Soil and Tillage Research",
        "Catena",
        "Journal of Hydrology",
        "Agricultural Water Management",
        "Land Degradation & Development",
    ),
    units_and_formulas_notes=(
        "土壤侵蚀模数用 t/(hm²·a)",
        "坡度用 %；坡长用 m",
        "公式用 amsmath；侵蚀方程须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "HEC-HMS", "HEC-RAS", "SWAT", "WEAP", "TOPMODEL", "MODFLOW", "SWAT-CUP", "RUSLE", "WEPP", "GSSHA", "LISFLOOD", "NAM", "HBV", "ENVI", "MATLAB", "Python", "R", "SPSS"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
