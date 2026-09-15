"""营养学论文支持：膳食干预、营养流行病学、生物标志物。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nutrition",
    aliases=("nutrition", "diet", "dietetics", "营养学", "膳食", "食品科学"),
    paper_types={
        "research": ("abstract", "introduction", "subjects and methods", "results",
                     "discussion", "conclusions", "references"),
        "intervention": ("abstract", "introduction", "trial design（注册号）", "dietary protocol",
                         "outcomes", "adherence", "references"),
        "review": ("abstract", "introduction", "search strategy", "evidence grading",
                   "findings", "limitations", "references"),
    },
    citation_style="AMA 或 Vancouver（营养期刊主流）",
    reporting_standards={
        "trial": "临床试验注册号（ChiCTR/ClinicalTrials.gov）与 CONSORT 声明必须附",
        "diet": "膳食评估方法（24h 回顾/FFQ）版本与信效度须引用",
        "biomarkers": "生化指标给测定方法、实验室与批间/批内变异系数",
        "intake": "能量与营养素摄入给均值±标准差；能量摄入异常者（±界限）处理说明",
        "outcomes": "主要结局与次要结局事先声明；多重比较校正",
    },
    conventions=(
        "营养素单位统一（g、mg、µg；维生素用 µg RE 或 IU 注明）",
        "食物成分表来源（中国食物成分表/USDA FDC）版本写明",
        "人群描述给年龄/性别/BMI/活动水平；膳食依从性给量化指标",
        "指南推荐引用（DRIs/膳食指南）具体条目",
    ),
    key_venues=(
        "American Journal of Clinical Nutrition",
        "The Journal of Nutrition",
        "Nutrition Reviews",
        "British Journal of Nutrition",
        "European Journal of Clinical Nutrition",
    ),
    units_and_formulas_notes=(
        "能量 kcal 或 MJ；蛋白质 g/kg 体重；微量元素 µg/day",
        "血糖 mmol/L 或 mg/dL（注明换算）；血脂给口径",
    ),
)
