"""工业排放控制学科论文支持：工业废水/废气/固废排放的治理工艺、达标核算与环境影响评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="industrial_discharge_control",
    aliases=(
        "industrial_discharge_control",
        "工业排放控制",
        "工业废水治理",
        "工业废气控制",
        "工业固体废弃物处理",
        "industrial wastewater treatment",
        "industrial air emission control",
        "industrial solid waste management",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ACS 样式（化工/环境类期刊）或 GB 规范样式（国内环评报告）",
    reporting_standards={
        "emission_compliance": "达标核算须按 HJ 91—2019 等排污单位核算导则与最新国标限值执行",
        "impact_assessment": "环境影响评估须按 HJ 2.1—2011 导则报告全要素数据",
        "treatment_performance": "治理设施效率报告须给进出口浓度、去除率与运行参数",
        "life_cycle": "全生命周期评估须按 ISO 14040/14044 规范执行",
    },
    conventions=(
        "废水/废气浓度单位统一为 mg/L、mg/m³ 或 ppm，须注明测定方法",
        "去除率、达标率须用同一口径核算并给出原始数据",
        "排放标准须明确引用 GB 8978、GB 16297、行业专项标准最新版本",
        "污染物负荷用 t/a，统计年须标注",
        "治理工艺名称须用行业规范术语",
    ),
    key_venues=(
        "Water Research",
        "Journal of Hazardous Materials",
        "Environmental Science & Technology",
        "Journal of Environmental Management",
        "中国环境科学",
    ),
    units_and_formulas_notes=(
        "流量单位统一为 m³/d 或 m³/h，须注明平均/峰值口径",
        "去除率公式为 (C_in - C_out) / C_in × 100%，须给进出口值",
        "污染物当量与总量指标须按国家总量控制名录核算",
        "成本核算须给处理量、电耗、药剂耗量与元/吨口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("EPA SCREEN3", "EPA BETA9", "EPA CMAQ", "NOAA WRF", "COMSOL Multiphysics", "ANSYS Fluent", "MATLAB", "R（环境统计建模）", "Python（scipy 数据处理）", "EPA BenMAP-3", "QGIS", "ArcGIS", "EPA AP-42 排放因子库", "EPA EDGAR", "MARPOL 船载排放核算", "EPA CalMet/CALPUFF", "EPA AERMOD", "IPCC 排放因子默认值", "EPA AirToxScreen", "HJ 系列国标核算软件"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
