"""营养学科论文支持：膳食干预、营养流行病学、生物标志物体裁、Vancouver 引用样式与营养素单位注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nutrition",
    aliases=(
        "nutrition",
        "营养学",
        "Nutrition",
        "Dietetics",
        "Clinical Nutrition",
        "Public Health Nutrition",
        "Nutritional Epidemiology",
        "Dietary Intervention",
        "膳食研究",
    ),
    paper_types={
        "research": ("abstract", "introduction（膳食问题与假设）", "subjects and methods（对象与膳食评估方法）", "results（营养素摄入与临床结局）", "discussion（营养意义）", "references"),
        "intervention": ("abstract", "introduction（干预目标）", "trial design（注册号）", "dietary protocol", "outcomes", "adherence", "references"),
        "review": ("abstract", "introduction", "search strategy（检索策略）", "evidence grading（证据等级）", "findings", "limitations", "references"),
    },
    citation_style="AMA 或 Vancouver（营养期刊主流样式）",
    reporting_standards={
        "trial": "CONSORT 与临床试验注册号（ChiCTR/ClinicalTrials.gov）",
        "diet": "膳食评估方法（24h 回顾/FFQ）版本与信效度",
        "biomarkers": "生化指标测定方法、实验室与批间变异",
        "intake": "能量与营养素摄入均值±标准差；能量摄入异常者处理",
    },
    conventions=(
        "营养素单位统一（g、mg、µg；维生素用 µg RE 或 IU 注明）",
        "食物成分表来源（中国食物成分表/USDA FDC）版本写明",
        "人群描述给年龄/性别/BMI/活动水平",
        "膳食依从性给量化指标",
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
        "能量 kcal 或 MJ；蛋白质 g/kg 体重",
        "微量元素 µg/day",
        "血糖 mmol/L 或 mg/dL（注明换算）",
        "血脂给口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ESHA Dietary Analysis", "NutritionData USDA", "Cronometer", "MyFitnessPal", "Python", "R", "SPSS", "SAS", "Stata", "Microsoft Excel", "Tableau", "EndNote", "Mendeley", "Zotero", "中国食物成分表 CNFD", "膳食频率问卷 FFQ", "24 小时膳食回顾", "Lifesum", "Yazio", "NutritionistPro"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Google Scholar", "Web of Science"),
)
