"""废物管理学科论文支持：固废处置、资源化利用与生命周期评价的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="waste_management",
    aliases=("waste_management", "废物管理", "废弃物处理", "固废管理", "垃圾分类",
             "waste management", "solid waste", "waste disposal",
             "refuse management", "waste treatment"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "environmental implications（环境影响）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "site description（地点概况）",
            "waste generation and characterization（废物产生与特征）",
            "treatment process（处理工艺）",
            "performance evaluation（性能评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "waste generation trends（废物产生趋势综述）",
            "treatment technologies（处理技术综述）",
            "circular economy approaches（循环经济路径）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "generation_assessment": "废物产生量须按重量（t/d）或体积（m³/d）标注，注明统计口径与时间窗口",
        "treatment_process": "处理工艺须说明反应条件（温度、pH、停留时间等）与污染物去除率",
        "lifecycle_analysis": "生命周期评价须遵循 ISO 14040/14044，明确系统边界与功能单位",
    },
    conventions=(
        "废物分类按 GB/T 15768 或 EU 废物目录（2000/53/EC）执行",
        "处理效率以去除率（%）或转化率（%）表示",
        "排放限值以 mg/L 或 mg/m³ 为单位，标注监测标准编号",
        "能量回收以 MJ/kg 或 kWh/t 为单位",
        "温室气体排放以 CO₂ 当量（tCO₂e）标注",
    ),
    key_venues=(
        "Waste Management",
        "Journal of Environmental Management",
        "Resources, Conservation and Recycling",
        "Waste and Biomass Valorization",
        "Clean Technologies and Environmental Policy",
    ),
    units_and_formulas_notes=(
        "质量流量为 t/d 或 kg/s",
        "浓度为 mg/L 或 g/L",
        "能耗为 kWh/t 或 MJ/kg",
        "碳减排以 tCO₂e 为单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SimaPro", "GaBi", "OpenLCA", "ArcGIS Pro", "QGIS", "MATLAB", "Python", "R", "SPSS", "Microsoft Excel", "Tableau", "AnyLogic", "SolidWorks", "AutoCAD", "LaTeX", "AERMOD", "OpenRefine", "WEKA", "GeoMedia", "COMSOL Multiphysics"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
