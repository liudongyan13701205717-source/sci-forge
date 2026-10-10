"""航空器维修学科论文支持：可靠性、故障分析与结构健康监测体裁及 FMEA/FRACAS 记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aircraft_maintenance",
    aliases=(
        "aircraft maintenance",
        "航空维修",
        "aviation maintenance engineering",
        "airframe maintenance",
        "aircraft reliability engineering",
        "机务维修",
        "航空器维修工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（可靠性问题、故障背景与目标）",
            "methods（数据分析/故障诊断/维护策略方法）",
            "results（故障率、MTBF、维护成本、寿命估计）",
            "discussion（与维护策略对比与改进）",
            "conclusion",
            "references",
        ),
        "reliability_report": (
            "背景与问题",
            "可靠性评估",
            "故障分析",
            "维护策略",
            "结论与建议",
            "参考文献",
        ),
    },
    citation_style="IEEE 或 ASME 样式（技术附件按 EASA AD/CS 或 SAE/ASTM 编号引用）",
    reporting_standards={
        "reliability_metric": "可靠性指标（MTBF、MTTR、MTBSI）须注明数据来源、时间窗口与置信区间",
        "failure_analysis": "故障分析须按 FMEA/FTA 或 FRACAS 报告失效模式、后果与根因",
        "maintenance_traceability": "维护决策须关联 EASA AD、CMM/CDR 与工单记录",
        "safety_analysis": "涉及安全的关键系统须按 RAM 或 FMEA 给出危害等级",
    },
    conventions=(
        "可靠性指标（MTBF、MTTR、MTBSI）须给出数据来源、时间窗口与置信区间",
        "故障分析须遵循 FMEA/FTA 或 FRACAS 标准分类，失效模式与后果须按危害等级（H/M/L）标注",
        "维护决策须关联 EASA AD、CMM/CDR 与工单记录，形成可追溯的证据链",
        "涉及安全关键系统的可靠性评估须按 RAM（可靠性、可用性、可维护性、安全性）四要素报告",
        "维护与检测数据须注明来源（如 AMOS、TRAX、LIDO）与采样策略",
    ),
    key_venues=(
        "Reliability Engineering & System Safety",
        "Journal of Quality in Maintenance Engineering",
        "Journal of Maintenance Engineering",
        "Aerospace Science and Technology",
        "Engineering Failure Analysis",
        "Mechanical Systems and Signal Processing",
        "航空学报",
        "Journal of Engineering Maintenance",
    ),
    units_and_formulas_notes=(
        "时间单位以 h 为主（MTBF/MTTR），累计量用件数（failures）与小时（hours）",
        "MTBF 须按 ISO 14224 或 SAE ARP4761 报告（分母为累计运行小时）",
        "MTTR 按 MTTR = 总维修时间 / 维修次数 报告，须说明是平均修理时间还是中位修理时间",
        "可靠性用百分比或指数（如 R(t) = exp(-t/MTBF)）",
        "维修成本以 USD 或 CNY 为单位并明确币种与年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AMOS", "TRAX", "LIDO", "Python", "MATLAB", "R", "C++", "CATIA", "SolidWorks", "ANSYS", "NASTRAN", "Abaqus", "Simulink", "ParaView", "SimScale", "COMSOL Multiphysics", "FEniCS", "Code_Aster", "FreeCAD", "ANSYS Mechanical", "MATLAB Simulink"),
    category="工学",
    databases=("EASA AD", "EASA CS", "arXiv", "OpenAlex", "Crossref"),
)
