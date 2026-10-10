"""养鱼业学科论文支持：养殖模式、水质调控与饲料管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fish_farming",
    aliases=("fish_farming", "养鱼业", "aquaculture", "fish farming technology",
             "aquaculture practices", "水产养殖", "fish pond management", "鱼类养殖",
             "aquaculture engineering"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="CSE (Council of Science Editors)",
    reporting_standards={
        "experiment": "养殖试验须报告水温、溶解氧、pH、氨氮等环境参数范围",
        "feeding": "饲料试验须说明配方、投喂率、频次与饲料系数计算方式",
        "growth": "生长试验须报告初始体重、测定频次与统计方法",
    },
    conventions=(
        "饲料系数用 FCR = 饲料量/增重 表示",
        "存活率用 SR = 存活数/初始数 × 100% 表示",
        "生长速度用 SGR = (ln W_t - ln W_0)/t × 100 表示",
        "水质参数须注明采样时间与测量仪器",
        "养殖密度用尾/单位面积或尾/单位体积表示",
    ),
    key_venues=(
        "Aquaculture Engineering",
        "Aquaculture Research",
        "Aquaculture International",
        "Journal of Applied Ichthyology",
        "水产养殖学报",
    ),
    units_and_formulas_notes=(
        "饲料系数 FCR = 投喂量(kg) / 体重增量(kg)，无量纲",
        "特定生长率 SGR = ln(W_t) - ln(W_0)) / t) × 100 (%/d)",
        "存活率 SR = 期末存活数 / 初始投放数 × 100%",
        "水温用 °C 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("YSI ProDSS 多参数水质仪", "溶解氧自动监测仪", "自动水质监测系统", "水质分析仪", "自动投喂系统", "增氧机 (罗茨风机)", "体视显微镜", "电子天平", "SPSS", "R (RStudio)", "Excel", "Python (Pandas/NumPy)", "MATLAB", "AutoCAD", "GIS (ArcGIS)", "水质采样器", "环境因子记录仪", "光谱分析仪", "显微摄影系统", "鱼类体尺测量仪"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)