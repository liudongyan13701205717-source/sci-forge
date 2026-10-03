"""药学论文支持：药代动力学、制剂开发、药物相互作用。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pharmacy",
    aliases=("pharmacy", "pharmacology", "pharmaceutics", "drug", "药学", "药理学", "制剂"),
    paper_types={
        "research": ("abstract", "introduction", "materials and methods", "results",
                     "discussion", "conclusions", "references"),
        "pk_study": ("abstract", "introduction", "study design", "analytical method",
                     "results（Cmax/AUC/t½）", "discussion", "references"),
        "formulation": ("abstract", "introduction", "formulation design", "characterization",
                        "stability", "in vitro release", "references"),
    },
    citation_style="ACS 或 Vancouver",
    reporting_standards={
        "bioanalytical": "LC-MS/MS 方法验证须符合 FDA/EMA 指南（线性/精密度/回收率）",
        "pk": "非房室/房室模型选择须说明；Cmax、AUC0-t、AUC0-∞、t½、CL 给几何均值±CV",
        "ethics": "临床试验注册号与伦理批件须写明（ICH-GCP）",
        "stability": "稳定性条件（温度/湿度/光照）与取样时间点须列表",
        "interaction": "药物相互作用给机制（CYP450 酶）与临床意义分级",
    },
    conventions=(
        "药物名首现用通用名（INN），后续可缩写；浓度单位统一（ng/mL、µM）",
        "给药方案表（剂量/途径/频次/疗程）必须出现",
        "溶出曲线给 f2 相似因子；处方组成用百分比或 mg/片",
        "剂量换算（人与动物）注明依据（体表面积法）",
    ),
    key_venues=(
        "British Journal of Pharmacology",
        "Journal of Pharmaceutical Sciences",
        "Molecular Pharmaceutics",
        "European Journal of Pharmaceutical Sciences",
        "Pharmaceutical Research",
    ),
    units_and_formulas_notes=(
        "AUC 单位 ng·h/mL；清除率 L/h；分布容积 L/kg",
        "溶出度 %；溶解度 mg/mL（注明温度与 pH）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("ChemDraw", "HPLC", "AutoDock", "溶出仪"),
    category="医学",
    databases=("PubMed", "Crossref", "PubChem", "CNKI"),
)
