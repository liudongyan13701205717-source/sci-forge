"""动物生产学科论文支持：肉品/乳品/蛋品/毛发畜产品体裁、Elsevier 样式与畜产品注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="animal_production",
    aliases=("animal production", "动物生产学", "畜产品科学",
             "animal products science", "肉类科学", "meat science",
             "乳品科学", "dairy science", "家禽科学", "poultry science",
             "蛋品科学", "egg science", "羊毛与皮毛", "wool and hide",
             "畜禽产品", "livestock products", "动物源食品",
             "animal-derived foods", "畜产品质量与安全"),
    paper_types={
        "research": (
            "abstract",
            "introduction（产品问题与质量假设）",
            "materials and methods（样本、加工、处理与检测）",
            "results（理化、微生物、感官与安全指标）",
            "discussion（工艺与品质关联）",
            "limitations",
            "references",
        ),
        "process_optimization": (
            "abstract",
            "introduction",
            "methods（因子、水平、试验设计与验证）",
            "results（响应面、优化与验证试验）",
            "discussion（工艺窗口与量产性）",
            "references",
        ),
        "sensory_study": (
            "abstract",
            "introduction",
            "methods（评价小组、量表与样品制备）",
            "results（感官评分与差异检验）",
            "discussion（与理化指标的对应）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按产品类别综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Elsevier/Vancouver 样式（编号制；Meat Sci. 遵循 Elsevier 规范）",
    reporting_standards={
        "sample": "样本来源、日龄、性别、屠宰与取样时间须报告",
        "processing": "加工条件（温度、时间、pH、添加剂）须完整",
        "analysis": "分析方法（GB/ISO/ASTM）与仪器条件须报告",
        "sensory": "感官评价小组（人数、培训与量表）须报告",
        "safety": "微生物与安全指标须给出检测方法与阈值",
    },
    conventions=(
        "畜产品指标按部位（如肌肉部位、熟化度）或产品形态（粉/液/半固体）区分报告",
        "感官评价按 ISO 6564/ISO 8589 报告并给出量表定义",
        "水分活度（a_w）与 pH 须报告测试方法与平衡温度",
        "脂肪酸与脂质按百分比与绝对值分别报告并给出来源",
        "缩写首次出现给出全称（如 a_w = water activity）",
    ),
    key_venues=(
        "Meat Science",
        "Journal of Dairy Science",
        "LWT - Food Science and Technology",
        "Journal of Food Science",
        "Food Chemistry",
        "Journal of Food Composition and Analysis",
        "Food Quality and Safety",
    ),
    units_and_formulas_notes=(
        "蛋白质、脂肪、水分、灰分以 g/100g 报告",
        "水分活度以 a_w 报告；pH 精确到 0.01",
        "脂肪酸以占总脂肪酸百分比与绝对值（g/100g）分别报告",
        "感官评分以百分制或 Likert 量表报告并给出锚点定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Foss MilkoScan FT3", "Dairycomp Lactron", "Foss PA 205", "Foss NIRSystems 6500", "Shimadzu GC-2030", "Shimadzu UV-1800", "Stable Micro Systems TA.XT Plus", "Instron 5944", "Warner-Bratzler Shear Tester", "Konica Minolta CR-410", "Aqualab CX-2", "Mettler Toledo", "Hanna Instruments", "FIZZ", "Ovo-Ball", "Labconco FreeZone", "R", "SPSS", "SAS", "GC-MS"),
    category="农学",
    databases=("Crossref", "OpenAlex", "CNKI", "PubMed"),
)
