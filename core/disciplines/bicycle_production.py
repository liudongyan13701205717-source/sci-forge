"""自行车制造（Bicycle Production）学科论文支持：整车设计、车架/传动/工艺/供应链管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bicycle_production",
    aliases=(
        "bicycle production", "bicycle manufacturing", "自行车制造", "自行车生产",
        "自行车装配", "bicycle assembly", "cycle manufacturing", "整车制造",
        "frame manufacturing", "车架制造", "bicycle industry", "自行车产业",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与应用场景）",
            "materials and methods（工艺路线、试验设计、测量方法）",
            "results（试验数据与工程指标）",
            "discussion（机理、局限与工程意义）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（工艺/材料/供应链综述）",
            "challenges and outlook",
            "references",
        ),
        "case_study": (
            "abstract",
            "背景（工厂/产线/车型）",
            "工艺与设备",
            "质量与效率指标",
            "讨论与改进建议",
            "references",
        ),
    },
    citation_style="APA 7 或 ISO 690；工程类亦可遵循 GB/T 7714",
    reporting_standards={
        "manufacturing_process": "工艺路线、设备型号、参数（温度/时间/压力）须完整报告",
        "materials_testing": "强度/硬度/疲劳试验须遵循 ISO/ASTM/GB 相应标准并给出设备",
        "cad_fea": "CAD/CAE 工具版本、网格尺度、边界条件与载荷须可复现",
        "quality": "抽样方案、缺陷分类（首件/过程/成品）与 Cpk/Ppk 指标须报告",
        "supply_chain": "供应链网络（一级/二级供应商）与产能口径须交代",
    },
    conventions=(
        "整车与零部件 BOM 编号与版本管理须交代",
        "材料牌号（如 6061-T6、T800 碳纤维）须显式标注",
        "受力/疲劳/刚度试验按 ISO 4210 系列报告（车架、把立、轮组、前叉等）",
        "整车几何参数（TT、Reach、Stack、Wheelbase 等）须按行业惯例给出",
        "工程图按 GB/T 与 ISO 标准绘制，比例与公差标注完整",
    ),
    key_venues=(
        "Journal of Bicycling Research",
        "International Journal of Vehicle Design",
        "Journal of Materials Processing Technology",
        "Chinese Journal of Mechanical Engineering",
        "Advances in Mechanical Engineering",
        "Journal of Materials in Cycling",
    ),
    units_and_formulas_notes=(
        "力学量按 ISO 3320 报告，含不确定度与有效位数",
        "整车几何参数以 mm 为单位，整车质量以 kg 为单位（±0.01 kg）",
        "功率/扭矩单位 kW/N·m；刚度 N/mm 或 N/m",
        "疲劳试验次数按 ISO 4210 分级（100k/500k/1000k 循环）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SolidWorks", "AutoCAD", "Siemens NX", "PTC Creo (Pro/ENGINEER)", "Dassault CATIA V5", "Autodesk Fusion 360", "Ansys Mechanical", "Ansys Fluent", "MSC Nastran", "Abaqus/Standard", "COMSOL Multiphysics", "OptiStruct", "Tecplot", "Altair HyperWorks", "Mastercam", "Siemens Teamcenter PLM", "SAP PLM", "Ultimaker Cura", "Stratasys Fortus (FDM/SLA)", "PrusaSlicer", "Fusion 360 Simulation", "3D 打印机（Ultimaker 5/Prusa MK4）", "CNC 加工中心（Haas VF / Mazak Variaxis）", "碳纤维热压罐（Hybrid Composites）", "真空袋模压设备", "激光切割机（Trumpf TruLaser / IPG YLS）", "电子焊接机（Jasic / Fronius）", "整车装配线 MES（Kingdee / SAP）", "扭矩扳手（Shimano TL-FC300）", "材料试验机（Instron 5944 / ZwickRoell）", "疲劳试验机（MTS 810 / Servo Hydraulic）", "万能材料试验机（SANS）", "测力/功率测试台（Power2max / Stages）", "风洞与骑行台（Roland R7 / Wahoo Kickr）", "SPC 软件（Minitab / SPC+ / QI Macros）", "SolidWorks Simulation", "LaTeX"),
    category="工学",
    databases=("OpenAlex", "Scopus", "IEEE Xplore", "CNKI"),
)
