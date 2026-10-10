"""营养与饮食学科论文支持：临床营养治疗/膳食咨询体裁、Vancouver 引用样式与饮食行为注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nutrition_and_dietetics",
    aliases=(
        "nutrition_and_dietetics",
        "营养与饮食",
        "Nutrition and Dietetics",
        "Clinical Dietetics",
        "Dietitian Practice",
        "Clinical Nutrition Therapy",
        "Food and Nutrition",
        "Dietary Counselling",
        "临床营养",
    ),
    paper_types={
        "research": ("abstract", "introduction（临床营养问题）", "methods（对象、膳食方案与结局测量）", "results（营养与临床结局）", "discussion（临床实践含义）", "references"),
        "intervention": ("abstract", "introduction（干预目标）", "trial design（注册号）", "dietary protocol", "outcomes", "adherence", "references"),
        "review": ("abstract", "introduction", "search strategy（检索策略）", "evidence grading（证据等级）", "findings", "limitations", "references"),
    },
    citation_style="AMA 或 Vancouver（营养期刊主流样式）",
    reporting_standards={
        "trial": "CONSORT 与临床试验注册号",
        "diet": "膳食评估方法（24h 回顾/FFQ）版本与信效度",
        "biomarkers": "生化指标测定方法与变异系数",
        "counselling": "饮食咨询记录遵循 SBAR 格式",
    },
    conventions=(
        "营养素单位统一（g、mg、µg；维生素用 µg RE 或 IU 注明）",
        "食物成分表来源与版本写明",
        "临床营养评估按 ASPEN 或中华营养学会标准",
        "能量与营养素摄入给均值±标准差",
        "指南推荐引用具体条目",
    ),
    key_venues=(
        "Clinical Nutrition",
        "American Journal of Clinical Nutrition",
        "Nutrition in Clinical Practice",
        "European Journal of Clinical Nutrition",
        "Asia Pacific Journal of Clinical Nutrition",
    ),
    units_and_formulas_notes=(
        "能量 kcal 或 MJ；蛋白质 g/kg 体重",
        "微量元素 µg/day",
        "血糖 mmol/L 或 mg/dL（注明换算）",
        "营养风险筛查用 NRS-2002 或 MUST",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ESHA Professional", "NutritionData USDA", "Cronometer", "MyFitnessPal", "Lifesum", "Python", "R", "SPSS", "SAS", "Stata", "Microsoft Excel", "Tableau", "EndNote", "Mendeley", "Zotero", "中国食物成分表 CNFD", "膳食频率问卷 FFQ", "24 小时膳食回顾", "饮食记录软件", "BIA 生物电阻抗人体成分分析仪"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
