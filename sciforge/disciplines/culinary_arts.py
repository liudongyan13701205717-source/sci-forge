"""Culinary arts 学科论文支持：烹饪技术/美食科学体裁、美食学报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="culinary_arts",
    aliases=(
        "culinary_arts",
        "culinary arts",
        "烹饪艺术",
        "烹饪技术",
        "烹饪科学",
        "cuisine",
        "美食学",
        "cookery",
        "culinary science",
        "gastronomy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与动机）",
            "materials and methods（原料与工艺方法）",
            "results（实验结果与感官评价）",
            "discussion（讨论与对比）",
            "conclusion",
            "references",
        ),
        "technique_study": (
            "abstract",
            "introduction（技法溯源）",
            "technique description（技法步骤与参数）",
            "evaluation（成品质构与感官评价）",
            "applications（应用场景）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "literature review（技法与科学综述）",
            "trends and challenges（趋势与挑战）",
            "references",
        ),
    },
    citation_style="APA 第7版（教育/营养类遵循 APA 规范）",
    reporting_standards={
        "technique": "技法参数（温度/时间/比例）须精确到最小刻度",
        "sensory": "感官评价遵循感官评价报告规范（评分标准、评价员培训、重复次数）",
        "measurement": "测量工具精度须声明（温度计精度、电子秤精度）",
        "reproducibility": "配方须给出精确克重而非体积量度，确保可重复",
    },
    conventions=(
        "配方中原料按功能分类排列（结构/风味/装饰）；精确到克",
        "温度统一使用摄氏度，必要时括注华氏度",
        "时间参数给出精确到分钟的区间（如 2:30-2:45 min）",
        "感官评价采用标准评分量表（1-9分），报告均值±标准差",
        "术语使用烹饪行业规范用语（如 乳化/凝胶化/焦化）",
    ),
    key_venues=(
        "Journal of Culinary Science & Technology",
        "Culinary Science Today",
        "International Journal of Gastronomy and Food Science",
        "Food Research International",
        "L'Art Culinaire",
        "Culinary Arts Research Quarterly",
    ),
    units_and_formulas_notes=(
        "重量用 g/kg；温度用 °C；时间用 min/h",
        "浓度用 %（重量比）或 Brix 度",
        "配方以百分比（% Baker's Math）或绝对克重标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Anova Sous-vide Precision Cooker", "ThermaPro 数字温度计", "KitchenAid Artisan Stand Mixer", "Vitamix Professional Series 5200", "ChefSteps 烹饪工具平台", "NutriCheck 营养分析软件", "MarketMan 库存管理系统", "BlueCart 库存管理系统", "Square POS 收银系统", "Toast POS 收银系统", "MenuEngineering.com 菜单工程软件", "7shifts KDS 厨房显示系统", "SafeStack 食品安全软件", "Atago 手持式 pH 计", "Atago 手持折射仪", "PolyScience 控温设备", "FLIR 热成像仪", "Brix 糖度计", "ThermoDol 温度探针", "KitchenIQ 配方管理软件", "Tasty 食谱管理 App"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "Scopus", "Web of Science"),
)
