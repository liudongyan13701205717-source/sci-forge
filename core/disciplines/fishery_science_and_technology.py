"""渔业科学与技术学科论文支持：渔业工程装备、自动化养殖与水产机械。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fishery_science_and_technology",
    aliases=("fishery_science_and_technology", "渔业科学与技术", "fishery engineering",
             "aquaculture engineering", "fishery technology", "渔业工程",
             "aquatic machinery", "水产机械", "fishery automation"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714",
    reporting_standards={
        "mechanical": "机械设计须报告材料参数、载荷条件与安全系数",
        "hydrodynamic": "流体力学试验须报告雷诺数、流速分布与边界条件",
        "automation": "自动化系统须说明传感器型号、控制算法与通信协议",
    },
    conventions=(
        "流体力学参数用国际单位制（SI）",
        "转速用 r/min 表示",
        "功率用 kW 表示",
        "水流速度用 m/s 表示",
        "设备效率用百分比(%)表示",
    ),
    key_venues=(
        "Aquaculture Engineering",
        "Transactions of the ASABE",
        "Fisheries Control",
        "Aquaculture International",
        "渔业工程",
    ),
    units_and_formulas_notes=(
        "功率 P = η × ρ × g × Q × H，单位 W",
        "雷诺数 Re = ρvL/μ，无量纲",
        "流量 Q = A × v，单位 m³/s",
        "设备效率 η = 输出功率 / 输入功率 × 100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS", "COMSOL Multiphysics", "SolidWorks", "AutoCAD", "MATLAB/Simulink", "MATLAB", "Python (SciPy/NumPy)", "SPSS", "R (RStudio)", "Excel", "水质监测仪", "溶解氧仪", "饲料颗粒机", "增氧机", "温控设备", "自动投喂系统", "水质分析仪", "光谱分析仪", "显微镜", "电子天平"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)