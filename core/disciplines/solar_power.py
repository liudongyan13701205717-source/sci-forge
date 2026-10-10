"""太阳能发电学科论文支持：光伏电站/并网运行/性能评估体裁、IEEE 样式与电力记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="solar_power",
    aliases=(
        "solar_power",
        "太阳能发电",
        "光伏电站",
        "光伏发电",
        "并网光伏",
        "solar power",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusion（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="IEEE 样式（作者-编号）",
    reporting_standards={
        "experimental": "实验遵循光伏并网实验报告规范",
        "case_study": "案例研究遵循光伏电站案例报告规范",
        "benchmark": "基准测试遵循光伏并网基准报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "光伏电站位置与规模须报告",
        "并网方式与功率须说明",
        "光伏组件与逆变器参数须注明",
        "统计处理须说明",
        "单位须与国际单位一致",
    ),
    key_venues=(
        "Solar Energy",
        "Solar Energy Materials and Solar Cells",
        "Renewable Energy",
        "IEEE Transactions on Sustainable Energy",
        "IEEE Transactions on Power Systems",
    ),
    units_and_formulas_notes=(
        "辐照度用 W/m²；效率用 %",
        "功率用 W/kW；能量用 Wh/kWh",
        "公式用 amsmath；电力参数须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PVsyst", "SAM", "HelioScope", "Solar Pathfinder", "Heliodas", "PV WIZARD", "PV*SOL", "OpenSolar", "PVCase", "SolarGIS", "HelioCAM", "MATLAB", "Python", "R", "ETAP", "DIgSILENT PowerFactory", "HOMER Pro", "PV*SOL Compact", "PV*SOL Professional", "PV*SOL Light"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
