"""Mechanical trades 学科论文支持：机械操作与制造工艺体裁、ASME/ISO 规范与设备记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mechanical_trades",
    aliases=("mechanical_trades", "机械工", "机械操作", "mechanical operations", "mechanical processing", "金属加工", "装配工", "设备维修", "mechanical maintenance"),
    paper_types={
        "research": ("abstract", "introduction（工艺背景与问题）", "methods（操作工艺与参数）", "results（加工质量与效率数据）", "discussion（工艺优化与工程应用）", "references"),
        "case_study": ("abstract", "introduction", "case description（设备与工况描述）", "analysis（故障诊断与工艺分析）", "results（维修/改造结果）", "discussion（改进建议）", "references"),
        "review": ("abstract", "introduction", "technique overview（技术综述）", "practice synthesis（实践经验总结）", "future directions", "references"),
    },
    citation_style="ASME 样式（工业实践遵循 ASME 规范）",
    reporting_standards={
        "machining": "机加工遵循 ISO 286 公差配合标准",
        "welding": "焊接工艺遵循 ASME Section IX",
        "assembly": "装配作业遵循 ISO 13679 机械装配通用规则",
        "maintenance": "设备维护遵循 ISO 14224 设备维护管理",
        "quality_control": "质量控制遵循 ISO 9001 质量管理体系",
    },
    conventions=(
        "工艺参数（切削速度、进给量、吃刀深度）须完整列出",
        "设备型号与规格须注明",
        "安全操作规程须符合职业健康安全标准",
        "加工精度与表面粗糙度须给出实测值",
        "工艺流程图须标注关键控制点",
    ),
    key_venues=(
        "Journal of Manufacturing Technology",
        "International Journal of Advanced Manufacturing Technology",
        "CIRP Annals – Manufacturing Technology",
        "Production Engineering",
        "Journal of Materials Processing Technology",
    ),
    units_and_formulas_notes=(
        "切削速度用 m/min；进给量用 mm/r；吃刀深度用 mm",
        "表面粗糙度用 Ra 值表示",
        "焊接参数用电流 A、电压 V 表示",
        "工具寿命用切削长度 m 或时间 h 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CNC Lathe", "Milling Machine", "Welding Machine", "Grinding Machine", "Drilling Machine", "Lathe", "Boring Machine", "Shaping Machine", "Broaching Machine", "Forging Press", "Rolling Machine", "Casting Machine", "Sanding Machine", "Tapping Machine", "Honing Machine", "Laser Cutting Machine", "Plasma Cutting Machine", "EDM (Electrical Discharge Machining)", "3D Printer", "Caliper / Micrometer / Dial Indicator"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
