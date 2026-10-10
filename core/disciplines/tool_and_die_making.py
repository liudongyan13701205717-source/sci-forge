"""模具制造学科论文支持：模具设计/制造工艺体裁、Journal of Materials Processing Technology 样式与模具记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="tool_and_die_making",
    aliases=("tool_and_die_making", "模具制造", "模具设计", "冲压模具", "注塑模具",
             "die design", "mold making", "模具热处理", "模具钢"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与模具设计问题）",
            "methods（仿真/设计/工艺方法）",
            "results（试验验证与性能评估）",
            "discussion（优化方向与工程应用）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（模具案例与需求）",
            "design and analysis（设计与仿真）",
            "results（加工与试模）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="Elsevier 样式（数字编号，期刊名称全拼）",
    reporting_standards={
        "simulation_parameters": "有限元分析网格划分策略与接触定义须明确",
        "material_properties": "材料力学性能参数须报告（含来源）",
        "dimensional_accuracy": "试模件尺寸精度以 IT 公差等级报告",
        "reproducibility": "试验条件（温度、速度、压力）须记录",
    },
    conventions=(
        "材料牌号用国标/ISO 标注（如 Cr12MoV / AISI D2）",
        "尺寸单位统一用 mm，公差用 ±0.01 mm 等格式",
        "硬度用 HRC 或 HV 表示，注明测试标准",
        "模具寿命以冲次/型次为单位",
        "仿真结果附网格收敛性验证",
    ),
    key_venues=(
        "Journal of Materials Processing Technology",
        "CIRP Annals",
        "Journal of Manufacturing Processes",
        "International Journal of Advanced Manufacturing Technology",
        "Die Casting Engineering",
    ),
    units_and_formulas_notes=(
        "尺寸单位 mm，公差 ±0.001~0.1 mm",
        "硬度单位 HRC 或 HV",
        "模具寿命单位：次（冲压次数/注射次数）",
        "公式用 amsmath 排版；有限元网格数量与单元类型须注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("UG NX", "AutoCAD", "SolidWorks", "Pro/E (Creo)", "Moldflow", "Dynaform", "AutoForm", "HyperWorks", "DEFORM-3D", "CATIA V5", "CAXA", "Siemens CAM", "Mastercam", "PowerMill", "五轴数控加工中心", "线切割机床", "电火花机床", "激光切割机", "硬度计", "三坐标测量机"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
