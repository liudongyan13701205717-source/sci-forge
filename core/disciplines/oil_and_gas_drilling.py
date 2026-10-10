"""石油与天然气钻探学科论文支持：钻井工程/井下工艺体裁、SPE 引用样式与钻井记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="oil_and_gas_drilling",
    aliases=("oil_and_gas_drilling", "油气钻探", "钻井工程", "石油钻井", "oil drilling", "drilling engineering"),
    paper_types={
        "research": ("abstract", "introduction（背景与工程问题）", "methodology（钻井设计与实验）", "results（钻井性能）", "discussion（机理与推广）", "references"),
        "case_study": ("abstract", "introduction", "case description（井位与地质）", "analysis（井控与风险）", "results（完井与产出）", "discussion（经验与改进）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（技术综述）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="SPE 样式",
    reporting_standards={"well_report": "遵循 SPE 钻井报告规范", "safety_report": "遵循 API 53 规范", "systematic_review": "遵循 PRISMA 声明"},
    conventions=("井深用 m 并注明参考", "井压力用 MPa", "井下工具须注明 API 等级", "钻屑/泥浆须报告 API 密度", "完井方式须明确"),
    key_venues=("SPE Drilling & Completion", "Journal of Petroleum Science and Engineering", "International Journal of Offshore and Polar Engineering", "Journal of Applied Petroleum Science", "Petroleum Science"),
    units_and_formulas_notes=("深度用 m", "压力用 MPa", "流量用 L/s 或 m³/s", "钻压用 kN", "公式用 amsmath"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("钻井模拟器", "Wellhead/防喷器 BOP", "测井仪器", "Mud Logger", "MWD 随钻测量", "LWD 随钻测井", "Seismic 地震勘探", "Petrel 建模软件", "Landmark 地质建模", "Petrel 2D/3D 建模", "RockWorks", "Compass 3D", "Sedex Drilling Simulator", "SLB 完井软件", "API 5CT", "Mud 性能分析仪", "Mudlog 数据处理", "Python 数据分析", "MATLAB", "Petroleum Engineering 计算软件"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
