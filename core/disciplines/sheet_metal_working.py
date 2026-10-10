"""钣金加工学科论文支持：钣金成型/激光切割/冲压工艺/工艺规划体裁、IEEE 引用样式与制造业注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sheet_metal_working",
    aliases=("sheet_metal_working", "钣金加工", "钣金制造", "金属成型",
             "sheet metal fabrication", "钣金成型", "钣金工艺"),
    paper_types={
        "research": (
            "abstract",
            "introduction（钣金成型问题与工艺背景）",
            "methods（材料、工艺参数与仿真）",
            "results（几何精度、力学性能与工艺窗口）",
            "discussion（工艺改进与推广）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（钣金件/产线案例）",
            "analysis（工艺参数与设计评估）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（钣金成型理论谱系）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（作者编号；IEEE Transactions 系列遵循 IEEE 规范）",
    reporting_standards={
        "simulation": "成形仿真遵循 ABAQUS/LS-DYNA 报告规范（网格、边界、接触）",
        "process_control": "工艺控制遵循 ISO 9001 与 ASTM E 系列检测标准",
        "metrology": "几何精度检测遵循 GD&T（ISO 1101）与三维测量报告规范",
    },
    conventions=(
        "板材材料按牌号（Q235、DC01、SUS304 等）与厚度报告",
        "成形工艺按工序编号（下料-展开-折弯-焊接-表面处理）",
        "工艺参数（折弯角、折弯半径、压力、速度）须完整披露",
        "仿真须报告网格尺寸、单元类型与收敛判据",
        "几何精度用 GD&T 特征符号；公差用 ISO 2768 或 GB/T 1184",
    ),
    key_venues=(
        "Journal of Manufacturing Systems",
        "International Journal of Machine Tools and Manufacture",
        "Journal of Materials Processing Technology",
        "The International Journal of Advanced Manufacturing Technology",
        "CIRP Annals",
    ),
    units_and_formulas_notes=(
        "板材厚度用 mm；折弯角用 °；折弯半径用 mm",
        "屈服强度 σs 用 MPa；抗拉强度 σb 用 MPa；延伸率用 %",
        "激光切割功率用 kW；频率用 kHz；切割速度用 m/min",
        "网格单元尺寸（mm）、时间步长（s）与收敛判据（如 10⁻⁶）须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SolidWorks", "Rhinoceros", "Grasshopper", "Fusion 360", "AutoCAD Inventor", "CATIA", "Siemens NX", "Mastercam", "GibbsCAM", "FeatureCAM", "Delcam PowerMILL", "SheetCAM", "Fiber Laser Cutting Machine", "Press Brake", "CNC Punch Press", "Waterjet Cutting Machine", "TIG Welding Machine", "MIG Welding Machine", "Faro Laser Tracker"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
