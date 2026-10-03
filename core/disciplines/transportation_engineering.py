"""交通工程学科论文支持：交通规划/道路/安全体裁、TRB 引用样式与交通记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="transportation_engineering",
    aliases=("transportation_engineering", "交通工程", "交通", "交通运输",
             "交通规划", "交通安全"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与交通问题）",
            "methods（数据、建模与参数）",
            "results（流量/安全数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "traffic_study": (
            "abstract",
            "introduction",
            "study area（研究区域）",
            "data collection（数据采集）",
            "analysis（分析）",
            "results and recommendations（结果与建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="TRB 样式（作者-年份；Transportation Research Record 遵循 TRB 规范）",
    reporting_standards={
        "traffic_study": "交通调查遵循 TRB/ITE 手册规程",
        "safety_analysis": "安全分析遵循 Highway Safety Manual（HSM）",
        "survey": "出行调查遵循 TRB 调查方法规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "simulation": "交通仿真遵循 TRB 仿真指南",
    },
    conventions=(
        "交通量/通行能力单位须规范（pcu/h 等）",
        "数据来源与采集时段须说明",
        "服务水平（LOS）分级标准须注明",
        "事故统计口径与暴露量须明确",
        "模型标定与验证指标须报告",
    ),
    key_venues=(
        "Transportation Research Record",
        "Transportation Research Part A/B/C/D/E",
        "Accident Analysis & Prevention",
        "Journal of Transport Geography",
        "Journal of Transportation Engineering",
        "Transportation",
    ),
    units_and_formulas_notes=(
        "流量用 veh/h 或 pcu/h；速度用 km/h",
        "公式用 amsmath；通行能力与延误方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "事故率用 次/百万车公里",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("VISSIM", "Python", "MATLAB", "TransCAD"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Zenodo", "CNKI"),
)