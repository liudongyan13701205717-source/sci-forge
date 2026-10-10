"""给排水学科论文支持：市政给水与排水系统工程设计的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="water_supply_and_sewerage",
    aliases=("water_supply_and_sewerage", "给排水", "给排水工程", "市政给排水", "供水与排污",
             "water supply and sewerage", "water and wastewater",
             "municipal water", "civil engineering water", "sewerage"),
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
            "project description（项目概况）",
            "demand forecast（用水需求预测）",
            "system design（系统设计）",
            "hydraulic verification（水力验证）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "water supply systems（给水系统综述）",
            "wastewater collection systems（污水收集系统综述）",
            "treatment and reuse（处理与回用综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "hydraulic_modeling": "管网水力模型须验证压力、流量与水质指标，标注模型验证方法",
        "wastewater_collection": "污水收集系统须标注管径、坡度、设计流速与过流能力",
        "environmental_assessment": "环境影响评估须包含生态流量计算与排放水质达标分析",
    },
    conventions=(
        "管径以 mm 为单位，坡度以 % 或 1:N 表示",
        "流速以 m/s 标注，最小/最大流速按 GB 50014 执行",
        "用水量预测以 m³/d 为单位，标注预测方法与置信区间",
        "污水处理标准按 GB 18918 或行业排放标准标注",
        "管网图按 GB/T 13734 绘制，标注管径、材质与埋深",
    ),
    key_venues=(
        "Water Research",
        "Environmental Engineering Science",
        "Journal of Environmental Engineering",
        "Water Science and Technology",
        "Environmental Science & Technology",
    ),
    units_and_formulas_notes=(
        "管径：mm",
        "坡度：% 或 1:N",
        "流速：m/s",
        "流量：m³/d",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("EPANET", "WaterGEMS", "SewerGEMS", "Bentley Hammer", "MATLAB", "Python", "R", "SPSS", "Microsoft Excel", "Tableau", "ArcGIS Pro", "QGIS", "AutoCAD", "SolidWorks", "COMSOL Multiphysics", "SWMM", "Visual MINTEQ", "LaTeX", "OpenRefine", "GeoMedia"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
