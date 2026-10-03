"""农学论文支持：田间试验、作物模型、土壤与养分管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="agriculture",
    aliases=("agriculture", "agronomy", "crop", "soil", "farming", "农学", "作物", "土壤"),
    paper_types={
        "research": ("abstract", "introduction", "materials and methods（田间/温室设计）",
                     "results", "discussion", "conclusions", "references"),
        "field_trial": ("abstract", "introduction", "site description（土壤/气候）",
                        "experimental design", "results", "yield analysis", "references"),
        "review": ("abstract", "introduction", "scope", "findings", "research gaps", "references"),
    },
    citation_style="Elsevier numbered 或 ASA-CSSA-SSSA style",
    reporting_standards={
        "trial": "田间试验设计（随机区组/裂区）、重复数与小区面积须给出",
        "soil": "土壤类型、pH、有机质、前茬与基础肥力须报告",
        "climate": "试验季气象数据（降水/积温）须给出（来源写明）",
        "yield": "产量按标准含水率折算；统计用 ANOVA+多重比较（LSD/Tukey）",
        "inputs": "肥料/农药用量（有效成分）与施用时期须列表",
    },
    conventions=(
        "品种名给正式登记名；转基因材料注明转化事件",
        "农艺性状给测定方法（如 SPAD、LAI）与仪器型号",
        "产量图按年份/处理分组；显著性字母标注法一致",
        "单位用 SI（kg/ha、t/ha、mm）；养分按 N-P2O5-K2O 折算",
    ),
    key_venues=(
        "Field Crops Research",
        "Agronomy Journal",
        "Plant and Soil",
        "European Journal of Agronomy",
        "Nature Plants",
    ),
    units_and_formulas_notes=(
        "产量 t/ha 或 kg/ha；养分利用率（NUE/PFP）公式须给出",
        "水分利用效率 WUE = 产量/蒸散量；单位 kg/m³",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("R", "DSSAT", "ArcGIS", "SPSS", "Origin"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
