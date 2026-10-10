"""其他工程学学科论文支持：未被细类归入的工程设计与系统建模研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_engineering",
    aliases=(
        "other_engineering", "其他工程学",
        "other engineering", "其他工程学",
        "engineering not elsewhere classified", "工程学未另分类",
        "systems engineering", "系统工程",
        "industrial engineering", "工业工程",
        "process engineering", "过程工程",
        "reliability engineering", "可靠性工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程问题与背景）",
            "methodology（设计、建模与实验方法）",
            "results（性能与验证结果）",
            "discussion（工程意义与局限）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工程系统与工况）",
            "analysis（仿真与现场对比）",
            "results（指标达成与验证）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与方法综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "k1": "实验须报告仪器型号、量程、校准状态与测量不确定度",
        "k2": "仿真须报告求解器、网格独立性验证与收敛判据",
        "k3": "性能对比须给出基线与置信区间",
    },
    conventions=(
        "符号首次出现须定义全称与量纲",
        "实验结果用 M ± SD 报告",
        "性能指标统一口径并注明测试工况",
        "图表须使用 SI 单位且坐标轴标注完整",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "IEEE Transactions on Industrial Electronics",
        "Mechanical Systems and Signal Processing",
        "IEEE Transactions on Automation Science and Engineering",
        "Computers & Chemical Engineering",
        "Reliability Engineering & System Safety",
        "《机械工程学报》",
    ),
    units_and_formulas_notes=(
        "一律使用 SI 单位并附括号注释",
        "功率用 W 或 kW 表示并注明名义/额定口径",
        "温度用 °C 或 K 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "Python (numpy, scipy)", "SolidWorks", "AutoCAD", "ANSYS Mechanical", "COMSOL Multiphysics", "Abaqus", "NASTRAN", "CATIA", "Creo Parametric", "Siemens NX", "Autodesk Revit", "LabVIEW", "Arduino IDE", "Raspberry Pi", "KiCad", "LTspice", "OnScale", "EndNote"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
