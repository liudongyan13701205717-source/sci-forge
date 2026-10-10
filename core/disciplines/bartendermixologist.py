"""Bartender/Mixologist 学科论文支持：调制酒/鸡尾酒工艺体裁、APA 引用样式与调酒行业记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bartendermixologist",
    aliases=(
        "bartendermixologist",
        "bartender",
        "mixologist",
        "调酒师",
        "调酒工艺",
        "鸡尾酒调制",
        "Bar & Beverage Service",
        "Bartending",
        "Mixology",
        "调酒与酒吧管理",
        "酒类调制",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与工艺/产品问题）",
            "literature review（文献综述）",
            "materials and methods（配方、原料与实验方法）",
            "results（感官评价与理化指标）",
            "discussion（讨论与工艺优化）",
            "conclusion（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景）",
            "recipe and preparation（配方与工艺）",
            "sensory evaluation（感官评价）",
            "discussion（反思与改进）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（行业/工艺综述）",
            "outlook（趋势展望）",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；Food Chemistry 遵循 Elsevier 规范）",
    reporting_standards={
        "sensory_analysis": "感官评价遵循 ISO 8586 与 ISO 13299 报告规范",
        "case_study": "案例研究遵循 SAGER 案例报告规范",
        "experimental": "配方实验遵循预注册与可复现性规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "配方须同时给出英制与公制用量（oz/mL、°F/°C），并标注精度（如 ±0.5 mL）",
        "所有原料须注明品牌、酒精度（ABV%）、产地、年份（如适用），避免仅写品类",
        "感官评价须报告评价员人数、评价维度（外观、香气、口感、余味）与统计方法",
        "涉及酒精成分与酒精含量的建议须标注法规依据（如美国 TTB、欧盟 2008/12/EC）",
        "禁止以「更好喝」「更健康」等主观断言替代可核验指标",
    ),
    key_venues=(
        "Journal of Food Science",
        "Food Chemistry",
        "Journal of Agricultural and Food Chemistry",
        "Leavening",
        "Alcohol and Alcoholism",
        "Alcohol Science & Research",
        "Food Science and Technology International",
        "British Journal of Nutrition",
    ),
    units_and_formulas_notes=(
        "液体用量优先用 mL，其次 oz；温度用 °C，体积比用 %（v/v）",
        "酒精含量用 ABV%（体积分数）；pH 无量纲；Brix 用 °Brix",
        "配方中的糖/盐浓度用 g/100 mL 或 g/L 表达，避免仅写「少许」",
        "蒸馏/浸泡时长须给出具体的时间与温度，避免「隔夜」等模糊表达",
        "感官评分使用 ISO 标准化的量表（1-9 分或 1-10 分），并注明量表类型",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Boston Shaker (Cocktail Shaker)", "Hawthorne Strainer", "Julep Strainer", "Fine Mesh Strainer", "Jigger (2 oz)", "Bar Spoon", "Cocktail Muddler", "Cocktail Glasses", "Bartesian One", "Hoshino Shu Kiyoshizake", "Suntory Whisky", "Maker's Mark Bourbon", "Jameson Irish Whiskey", "Hendrick's Gin", "Beefeater London Dry Gin", "Tanqueray London Dry Gin", "Bombay Sapphire Gin", "Absolut Vodka", "Grey Goose Vodka", "Cîroc Vodka", "Ketel One Vodka", "Cointreau Liqueur", "Grand Marnier", "Disaronno Amaretto", "Glenfiddich 12", "Johnnie Walker Black Label", "Glenmorangie 10", "Highland Park 12", "The Macallan 12", "Luxardo Maraschino", "Monin Syrups", "Torani Syrups"),
    category="管理学",
    databases=("OpenAlex", "CNKI", "万方", "PubMed"),
)
