"""Switchboard operating 学科论文支持：配电操作/继电保护/电气安全/SCADA。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="switchboard_operating",
    aliases=(
        "switchboard_operating", "Switchboard operating",
        "配电操作", "开关柜操作", "变电操作",
        "电气操作",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与操作问题）",
            "methods（操作方案与安全规程）",
            "results（操作效率与安全数据）",
            "discussion（讨论与改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景与设备参数）",
            "analysis（操作流程与风险分析）",
            "results（操作成效与安全评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（操作理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（作者编号；电气工程期刊规范）",
    reporting_standards={
        "operation_procedure": "操作规程须报告步骤、安全要点与应急措施",
        "protection_setting": "继电保护定值须报告整定依据、计算过程与动作时间",
        "safety_assessment": "安全评估须报告风险等级、防护措施与检测记录",
        "fault_analysis": "故障分析须报告故障类型、动作序列与原因",
    },
    conventions=(
        "电气设备编号须按规范标注（如 1# 主变、2# 出线）",
        "操作票须按顺序编号并记录操作时间",
        "继电保护定值须注明计算依据与版本",
        "电压用 kV；电流用 A；功率用 kW 或 MW",
        "接地电阻用 Ω；绝缘电阻用 MΩ",
    ),
    key_venues=(
        "IEEE Transactions on Power Delivery",
        "IEEE Transactions on Power Systems",
        "Electric Power Systems Research",
        "电力系统自动化",
        "高电压技术",
    ),
    units_and_formulas_notes=(
        "电压用 kV；电流用 A；功率用 kW/MW",
        "接地电阻用 Ω；绝缘电阻用 MΩ",
        "短路电流用 kA；操作时间用 s",
        "继电保护动作时间用 ms",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("配电柜（开关柜）", "低压断路器（ABB/施耐德）", "高压开关柜（KYN28）", "继电保护装置（继电保护屏）", "SCADA 系统（监视控制与数据采集）", "PLC 可编程控制器（西门子 S7-1200）", "DCS 分布式控制系统", "变频器（VFD，ABB/施耐德）", "电能质量分析仪（Fluke）", "绝缘电阻测试仪", "接地电阻测试仪", "红外测温仪（热成像仪）", "高压验电器", "示波器（Tektronix）", "钳形万用表", "开关柜操作与联锁系统", "电气柜温度监测系统", "智能配电网自动化终端（FTU）", "电力监控系统（SCADA/EMS）", "继电保护测试仪"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
