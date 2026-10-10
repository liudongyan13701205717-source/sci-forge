"""木材加工与车削学科论文支持：木工机械加工与车削工艺体裁、APA 引用样式与加工记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wood_machining_and_turning",
    aliases=("wood machining and turning", "木材加工与车削", "木工车削", "木材机械加工", "木工加工",
             "wood machining", "wood turning", "woodworking machinery"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与加工问题）",
            "materials and methods（材料、机床与参数）",
            "results（加工质量、刀具磨损与效率）",
            "discussion（切削机理与工艺意义）",
            "references",
        ),
        "process_study": (
            "abstract",
            "introduction",
            "materials and methods（工艺参数与工序）",
            "results（质量与效率数据）",
            "discussion（工艺优化建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；木材与制造期刊多用 APA/Elsevier）",
    reporting_standards={
        "machining_trial": "切削试验须报告刀具、转速、进给与切深",
        "surface_quality": "表面质量须报告粗糙度参数（Ra/Rz）与测量方法",
        "tool_wear": "刀具磨损须报告测量方法与磨损判据",
        "statistical": "须报告重复数、统计方法与显著性",
    },
    conventions=(
        "木材树种须给出学名与含水率",
        "切削参数（转速、进给、切深）须量化",
        "表面粗糙度用 μm（Ra/Rz）报告",
        "刀具材质与几何角度须注明",
        "含水率用 % 并说明测定方法",
    ),
    key_venues=(
        "Wood Science and Technology",
        "Holzforschung",
        "European Journal of Wood and Wood Products",
        "BioResources",
        "Journal of Wood Science",
        "Forest Products Journal",
    ),
    units_and_formulas_notes=(
        "转速用 rpm；进给用 m/min 或 mm/min",
        "切深用 mm；粗糙度用 μm (Ra/Rz)",
        "含水率用 %；密度用 kg/m³",
        "切削力用 N；功率用 kW",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("数控木工车床 (CNC lathe)", "木工车床 (wood lathe)", "带锯机 (band saw)", "台锯 (table saw)", "CNC 雕刻机 (CNC router)", "平刨床 (planer)", "铣床 (milling machine)", "砂光机 (sander)", "钻床 (drill press)", "仿形车床 (copy lathe)", "WoodWop (CAD/CAM)", "AlphaCAM", "AutoCAD", "SolidWorks", "激光雕刻机 (laser engraver)", "含水率测定仪 (moisture meter)", "木材硬度计", "表面粗糙度仪", "车刀 (turning tools)", "除尘系统 (dust collection)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
