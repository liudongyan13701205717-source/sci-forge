"""空调制冷学科论文支持：HVAC 系统设计、能耗与 CFD 体裁及 ASHRAE 记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="airconditioning_programmes",
    aliases=(
        "air conditioning",
        "空调",
        "HVAC",
        "HVAC&R",
        "refrigeration engineering",
        "制冷工程",
        "thermal comfort",
        "air conditioning system design",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与目标）",
            "methods（CFD/能耗模拟或实验方法、边界条件与网格/仪器）",
            "results（温湿度、能耗、COP/EER 与节能量）",
            "discussion（与 ASHRAE/ISO 标准对比）",
            "conclusion",
            "references",
        ),
        "design_report": (
            "背景与需求",
            "系统方案与选型",
            "设计与计算",
            "性能验证",
            "结论与建议",
            "参考文献",
        ),
    },
    citation_style="ISO/ASHRAE/GB 参考样式（技术附件按 ASHRAE Handbook 或 ISO 标准编号引用）",
    reporting_standards={
        "cfd_validation": "CFD 结果须披露几何、边界条件、网格密度与验证方法（网格无关性）",
        "energy_comparison": "能耗与制冷系数须注明测试工况（ARI/ISO/AHRI）与参考基准",
        "instrument_accuracy": "实验须披露设备型号、传感器精度与不确定度预算",
    },
    conventions=(
        "温湿度须遵循 ASHRAE Handbook 或 ISO 4512 定义条件（如 27°C/19°C 或 24°C/22°C）",
        "能耗与制冷系数须注明测试工况（如 ARI 210/223 或 ISO 5151）与参考基准",
        "CFD/能耗模型须披露边界条件、网格密度与验证方法（如网格无关性验证）",
        "数据以 SI 单位为主，温度用摄氏度、压力用 kPa、体积流量用 m³/h",
        "符号与缩写首次出现须给出全称与来源标准（如 COP、EER、IPLV）",
    ),
    key_venues=(
        "ASHRAE Journal",
        "Journal of Building Performance Simulation",
        "Applied Thermal Engineering",
        "HVAC&R Research",
        "Building and Environment",
        "Energy and Buildings",
        "International Journal of Refrigeration",
        "Energy",
    ),
    units_and_formulas_notes=(
        "温度用摄氏度（°C），湿度用相对湿度（%RH）或含湿量（g/kg）",
        "压力用 kPa（绝对）或 mmHg（真空），流量用 m³/h",
        "能耗用 kWh，制冷系数用 COP/EER/IPLV，按 ASHRAE 或 ISO 标准定义",
        "温度、压力、湿度同时出现时须在文中或图中同时给出单位与参考标准",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Carrier HAP", "Trane Trace", "Daikin VRV Selector", "Carrier FieldServe", "Trane TRACE 3D", "EnergyPlus", "OpenStudio", "DesignBuilder", "COMSOL Multiphysics", "ANSYS Fluent", "FDS", "QGIS", "ArcGIS", "Python", "MATLAB", "R", "C++", "QPlus", "ASHRAE Climate Files", "ASHRAE Handbook"),
    category="工学",
    databases=("ASHRAE", "ISO", "OpenAlex", "Crossref"),
)
