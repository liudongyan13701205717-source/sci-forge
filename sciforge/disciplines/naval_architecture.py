"""船舶与海洋工程学科论文支持：船舶设计/水动力/结构体裁、SNAME 引用样式与船舶记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="naval_architecture",
    aliases=("naval_architecture", "船舶与海洋工程", "船舶工程", "船舶设计",
             "水动力", "海洋工程"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与船舶问题）",
            "methods（建模、试验与参数）",
            "results（水动力/结构数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "ship_design": (
            "abstract",
            "introduction",
            "design requirements（设计需求与船级社规范）",
            "preliminary design（总体设计）",
            "detailed design（结构/系统设计）",
            "verification（校核与试验）",
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
    citation_style="SNAME 样式（作者-年份；SNAME 期刊遵循 SNAME 规范）",
    reporting_standards={
        "experimental": "船模试验遵循 ITTC 规程",
        "seakeeping": "耐波性试验遵循 ITTC 耐波性规程",
        "structural": "结构强度遵循 ABS/DNV 船级社规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "simulation": "CFD/水动力仿真遵循 ITTC 验证与确认规程",
    },
    conventions=(
        "船型主尺度（LOA、LBP、B、D、T）须完整报告",
        "船级社规范与版本须引用",
        "模型缩尺比与试验条件须说明",
        "阻力/推进性能换算方法须明确",
        "结构材料与许用应力准则须注明",
    ),
    key_venues=(
        "Journal of Ship Research",
        "Ocean Engineering",
        "Marine Structures",
        "Journal of Marine Science and Technology",
        "Ships and Offshore Structures",
        "International Shipbuilding Progress",
    ),
    units_and_formulas_notes=(
        "排水量用 t；航速用 kn；功率用 kW",
        "公式用 amsmath；阻力/推进方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "傅汝德数/雷诺数等无量纲数须定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("Nauticalics Nautilus", "MATLAB", "OpenFOAM", "AVEVA Marine"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)