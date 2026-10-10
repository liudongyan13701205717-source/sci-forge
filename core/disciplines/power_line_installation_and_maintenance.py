"""电力线路安装与维护学科论文支持：输电线路设计、施工、状态检修与安全运行。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="power_line_installation_and_maintenance",
    aliases=(
        "power line installation and maintenance", "电力线路安装与维护",
        "transmission line", "输电线路",
        "line maintenance", "线路检修",
        "power distribution", "配电线路",
        "condition-based maintenance", "状态检修",
        "insulator string", "耐张塔与绝缘子",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（运行问题与工程背景）",
            "methodology（测量方法、建模与试验）",
            "results（性能数据与对比）",
            "discussion（工程适用性与建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（线路区段与工况）",
            "analysis（缺陷诊断与处置工艺）",
            "results（处理后性能恢复）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（线路结构与状态评估理论）",
            "evidence synthesis（缺陷类型与失效证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "k1": "试验须符合 GB/T 2900 与 IEC 60870 系列术语口径",
        "k2": "状态检修须报告缺陷分级依据（Q/GDW 状态检修规程）",
        "k3": "带电作业须报告安全工器具检验周期与绝缘电阻值",
    },
    conventions=(
        "电压等级须明确标注（如 110 kV、220 kV、500 kV）",
        "线路参数以正序/零序区分并注明单位长度口径",
        "试验数据须注明试验日期、气象条件与仪器校准状态",
        "缺陷照片须标注缺陷位置、编号与拍摄角度",
        "带电作业须报告等电位转移与电位差安全裕度",
    ),
    key_venues=(
        "IEEE Transactions on Power Delivery",
        "Electric Power Systems Research",
        "High Voltages (MDPI)",
        "IEEE Transactions on Dielectrics and Electrical Insulation",
        "Proceedings of the CSEE",
    ),
    units_and_formulas_notes=(
        "绝缘电阻以 MΩ 表示，试验电压按 GB/T 11022 规定",
        "泄漏电流以 mA 为单位并注明污秽等级（如 II 级）",
        "风荷载按 vmax 与基本风速 m/s 口径并注明重现期",
        "对地距离以 m 表示并注明最大弧垂工况",
        "温度系数与热稳定电流以 A·√min 口径注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ETAP PowerStation", "Digsilent DIgSILENT PowerFactory", "PSCAD/EMTDC", "ANSYS Maxwell", "COMSOL Multiphysics", "MATLAB Simulink", "Python (pandas, PyTorch)", "MATLAB (Power Systems Toolbox)", "PowerWorld Simulator", "FLARE 无人机机巢巡检系统", "DJI M350 RTK 巡检无人机", "DLT105 高压数字绝缘电阻测试仪", "OMICRON MICOM 2555 继电保护测试仪", "OMICRON CMC376 电缆故障测试仪", "Fluke 8508A 数字兆欧表", "Hilger uds 红外热像仪", "Matsusada 局部放电检测仪", "Fluke RT-3000B 同步相量测量", "QGIS（线路 GIS）", "AutoCAD 电气制图"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
