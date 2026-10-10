"""水技术与工程学科论文支持：水资源工程、水力计算与水利设施的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="water_technology_and_engineering",
    aliases=("water_technology_and_engineering", "水技术", "水工程", "水科技工程", "水利技术",
             "water technology", "water engineering", "water resources engineering",
             "hydropower engineering", "water resources"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "engineering implications（工程意义）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "project description（工程概况）",
            "hydraulic design（水力设计）",
            "structural design（结构设计）",
            "environmental impact（环境影响评价）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "water resources development（水资源开发综述）",
            "engineering technologies（工程技术综述）",
            "policy and management（政策与管理综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "project_design": "工程设计须包含水力计算、结构计算与环境影响评价的完整报告",
        "monitoring_data": "监测数据须标注传感器位置、精度等级与采样频率",
        "safety_assessment": "安全评估须给出设计标准、安全系数与风险分析",
    },
    conventions=(
        "流量以 m³/s 或 m³/d 为单位",
        "扬程以 m 为单位，功率以 kW 或 MW 为单位",
        "水头损失以 mH₂O 为单位",
        "安全系数按 GB 50011 或行业规范取值",
        "水文资料标注数据来源、时段与整编方法",
    ),
    key_venues=(
        "Journal of Hydraulic Engineering",
        "Water Resources Research",
        "Journal of Water Resources Planning and Management",
        "Environmental Engineering Science",
        "Water Science and Technology",
    ),
    units_and_formulas_notes=(
        "流量：m³/s",
        "扬程：m",
        "功率：kW 或 MW",
        "流速：m/s",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("HEC-RAS", "MIKE11", "MIKE21", "EPANET", "MATLAB", "Python", "R", "SPSS", "Microsoft Excel", "Tableau", "ArcGIS Pro", "QGIS", "AutoCAD", "SolidWorks", "COMSOL Multiphysics", "Visual MINTEQ", "LaTeX", "OpenRefine", "GeoMedia", "SWMM"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
