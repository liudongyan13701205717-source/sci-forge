"""水文工程学科论文支持：水文学/水资源/水力学体裁、IAHR/ASCE 引用样式与水文记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hydrology_engineering",
    aliases=("hydrology_engineering", "水文工程", "水文学", "水文", "水资源",
             "水力学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与水文问题）",
            "methods（数据、建模与参数）",
            "results（径流/水位数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "hydrological_modeling": (
            "abstract",
            "introduction",
            "study area and data（研究区与数据）",
            "model description（模型描述）",
            "calibration and validation（率定与验证）",
            "results（模拟结果）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="IAHR/ASCE 样式（作者-年份；Journal of Hydrology 遵循其规范）",
    reporting_standards={
        "experimental": "水力学试验遵循 IAHR 试验规程",
        "hydrological_modeling": "水文建模遵循 IAHS 建模报告规范",
        "flood_risk": "洪水风险遵循 EU Floods Directive 报告框架",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "uncertainty": "不确定性分析遵循 IAHS 不确定性报告规范",
    },
    conventions=(
        "流域面积与水文分区须说明",
        "数据序列长度与来源须报告",
        "模型率定/验证指标（NSE、R²）须给出",
        "重现期与频率分析假定须明确",
        "单位换算（mm、m³/s）须规范",
    ),
    key_venues=(
        "Journal of Hydrology",
        "Water Resources Research",
        "Journal of Hydraulic Engineering",
        "Hydrological Processes",
        "Journal of Hydrologic Engineering",
        "Journal of Hydrology and Hydromechanics",
    ),
    units_and_formulas_notes=(
        "径流用 m³/s 或 mm；水位用 m",
        "公式用 amsmath；水量平衡与洪水方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "NSE、KGE 等评价指标须定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("HEC-RAS", "SWAT", "MATLAB", "Python（NumPy/SciPy）", "水文测验仪器"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "Zenodo"),
)