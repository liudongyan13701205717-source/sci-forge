"""食品科学论文支持：食品化学、食品安全、食品加工、营养学、感官评价。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_science",
    aliases=("food_science", "food_technology", "食品科学", "食品工程"),
    paper_types={
        "research": ("abstract", "introduction", "materials and methods", "results and discussion", "conclusions", "references"),
        "review": ("abstract", "introduction", "classification", "mechanisms", "applications", "future trends", "conclusions", "references"),
        "sensory": ("abstract", "introduction", "panel description", "methodology", "results", "discussion", "conclusions", "references"),
    },
    citation_style="ACS style（上标编号），如 ¹ 或 [1]",
    reporting_standards={
        "safety": "安全性须报告微生物指标（菌落总数/大肠菌群/致病菌）、重金属与农残",
        "sensory": "感官评价须报告评价方法（QDA/TC/9点标度）、评价员人数与培训情况",
        "processing": "加工须报告工艺参数（温度/时间/压力/pH）与设备规格",
        "nutrition": "营养须报告分析方法（国标/AOAC）、检测值与允许误差",
    },
    conventions=(
        "食品添加剂用 INN（国际非专有名称）或 E 编号",
        "微生物用标准培养基与计数方法（平板计数/MPN/PCR）",
        "仪器分析须报告色谱/质谱条件（柱温/流动相/检测波长）",
        "感官描述词用标准词典（如 Sensory Wheel）",
        "所有实验至少三次独立重复",
    ),
    key_venues=(
        "Food Chemistry",
        "Journal of Agricultural and Food Chemistry",
        "Food Research International",
        "LWT - Food Science and Technology",
        "Journal of Food Science",
    ),
    units_and_formulas_notes=(
        "浓度用 mg/kg（ppm）或 mg/L",
        "水分活度 aw 无量纲（0-1）",
        "质构用 N（硬度）和 mm（弹性）",
        "色泽用 L*a*b* 值；色差用 ΔE",
        "微生物用 CFU/g 或 CFU/mL",
    ),
    contribution_forms=("论文", "专利"),
    tools=("HPLC", "质构仪", "SPSS", "Origin"),
    category="工学",
    databases=("OpenAlex", "Crossref", "PubMed", "CNKI"),
    paper_capable=True,
)
