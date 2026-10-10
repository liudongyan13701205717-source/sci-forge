"""暖通行业学科论文支持：供暖与暖通工程体裁、ASHRAE 样式与热工记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="heating_trades",
    aliases=("heating_trades", "暖通", "暖通空调", "供暖工程", "供暖安装", "供暖维修", "供暖技术", "供暖设备", "供暖工程"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ASHRAE 样式",
    reporting_standards={
        "simulation": "模拟研究规范",
        "experimental": "实验研究规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "温度用 ℃/K；压力用 Pa/kPa/MPa",
        "供暖热负荷须报告",
        "系统效率须报告",
        "参数敏感性须报告",
        "单位换算须一致",
    ),
    key_venues=(
        "Building and Environment",
        "Energy and Buildings",
        "Applied Energy",
        "ASHRAE Journal",
        "Journal of Energy Engineering",
    ),
    units_and_formulas_notes=(
        "温度用 ℃/K；压力用 Pa/kPa/MPa",
        "公式用 amsmath；热工公式须编号",
        "行内公式避免复杂分式",
        "数值结果给出均值±SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD MEP", "Revit MEP", "HAP", "Carrier HAIL", "Carrier Design System", "Trane Trace", "EES", "CoolProp", "EnergyPlus", "DesignBuilder", "SketchUp", "SolidWorks", "CATIA", "NX", "Creo", "Solid Edge", "Teamcenter", "DIALux", "Relux", "Radiance"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
