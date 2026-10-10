"""水污染控制学科论文支持：水污染监测、治理工艺与水体修复的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="water_pollution_control",
    aliases=("water_pollution_control", "水污染控制", "水污染治理", "污水处理", "水体修复",
             "water pollution control", "water treatment", "wastewater treatment",
             "water remediation", "aquatic pollution"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "environmental impact（环境影响）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "site description（研究区概况）",
            "pollution status（污染现状）",
            "treatment design（治理方案设计）",
            "performance evaluation（处理效果评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "pollution sources and pathways（污染源与途径综述）",
            "treatment technologies（治理技术综述）",
            "policy and regulation（政策法规综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "pollutant_monitoring": "污染物浓度须标注检测标准编号、方法编号与检出限",
        "treatment_performance": "处理工艺评估须给出进水/出水浓度、去除率与污染物负荷",
        "mass_balance": "质量平衡须包含输入、输出与损耗项，闭合误差控制在 5% 以内",
    },
    conventions=(
        "COD、BOD₅、SS 等常规指标按 HJ（环境保护行业标准）方法检测",
        "去除率 = (C_进水 - C_出水) / C_进水 × 100%",
        "水力停留时间（HRT）以 h 或 min 为单位",
        "污泥产量以 kgDS/m³ 或含水率 % 为单位",
        "排放标准按 GB 18918（城镇污水处理厂）或行业排放标准标注",
    ),
    key_venues=(
        "Water Research",
        "Environmental Science & Technology",
        "Science of the Total Environment",
        "Journal of Hazardous Materials",
        "Chemosphere",
    ),
    units_and_formulas_notes=(
        "污染物浓度单位为 mg/L 或 g/L",
        "流量单位为 m³/d 或 m³/h",
        "COD 去除率以 % 表示",
        "能耗为 kWh/m³",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python", "R", "SPSS", "Microsoft Excel", "Tableau", "AnyLogic", "Visual MINTEQ", "EPANET", "SWMM", "ArcGIS Pro", "QGIS", "AutoCAD", "SolidWorks", "LaTeX", "OpenRefine", "COMSOL Multiphysics", "WEKA", "GeoMedia", "Minitab"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
