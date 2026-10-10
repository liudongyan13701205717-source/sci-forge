"""建筑翻新（Building renovation）：既有建筑改造、节能与结构加固研究方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="building_renovation",
    aliases=("building_renovation", "建筑翻新", "Building renovation",
             "building retrofit", "建筑改造", "adaptive reuse", "适应性再利用",
             "existing building upgrading", "既有建筑升级"),
    paper_types={
        "research": (
            "abstract",
            "introduction（既有建筑背景与改造目标）",
            "methodology（改造方案、结构检测、能耗仿真方法）",
            "results（结构安全、能耗节约、舒适度改善指标）",
            "cost-benefit analysis（改造成本与收益对比）",
            "conclusion",
            "references",
        ),
    },
    citation_style="Elsevier 样式（Energy and Buildings 系）",
    reporting_standards={
        "base_year": "改造前后能耗给基准年与统计口径（电/热/气分项或综合 kWh/m²·yr）",
        "structural_survey": "结构检测（回弹、超声、钻芯）给样本量、标准（GB 50291）与结果统计",
        "simulation": "改造方案能耗仿真给 EnergyPlus/DesignBuilder 版本、围护结构 U 值前后对比",
        "cost": "改造成本按分项（围护、设备、结构、室内）拆分；回收期（payback period）写明",
    },
    conventions=(
        "既有建筑年代、结构体系、层高与现状缺陷在首段交代；图纸按编号引用",
        "能耗结果给基准建筑对比；改造前后 U 值、窗墙比、气密性（n50）逐项列表",
        "结构加固方案给计算书摘要（承载力提升率 %）；材料与工艺说明施工关键工序",
    ),
    key_venues=(
        "Energy and Buildings",
        "Building & Environment",
        "Journal of Building Engineering",
        "Building and Environment（改造专题）",
        "Habitat International（适应性再利用方向）",
        "Construction and Building Materials",
    ),
    units_and_formulas_notes=(
        "能耗 kWh/m²·yr（电/热/气分项）；U 值 W/m²K；气密性 n50 次/h",
        "结构检测给 fcu（回弹）、σ₀（钻芯强度）；加固前后承载力提升率 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "Revit", "ArchiCAD", "EnergyPlus", "DesignBuilder", "TRNSYS", "Ladybug Tools", "Grasshopper", "Rhino", "SketchUp", "D5 Render", "Lumion", "Navisworks", "Tekla Structures", "ANSYS Mechanical", "STAAD.Pro", "Mid Civil (MIDAS)", "SAP2000", "ETABS", "OpenSees", "QGIS", "Blender", "Fusion 360", "BIM Track"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "ScienceDirect"),
)
