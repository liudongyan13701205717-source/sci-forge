"""动物饲养学科论文支持：畜禽舍/饲喂/环境/福利/精准养殖体裁、Elsevier 样式与养殖管理注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="animal_husbandry",
    aliases=("animal husbandry", "动物饲养学", "畜禽饲养学",
             "livestock husbandry", "畜禽饲养管理", "animal care and handling",
             "动物福利", "animal welfare", "饲养营养", "feeding and nutrition",
             "精准养殖", "precision livestock farming",
             "畜牧舍", "livestock housing", "家禽管理", "poultry management",
             "猪只管理", "swine management", "水禽与特种养殖"),
    paper_types={
        "research": (
            "abstract",
            "introduction（饲养管理问题与假设）",
            "materials and methods（品种、群体、舍型、饲料与采样）",
            "results（生产性能、健康、福利与环境指标）",
            "discussion（管理干预与经济效益）",
            "limitations",
            "references",
        ),
        "feeding_trial": (
            "abstract",
            "introduction",
            "methods（舍/栏次划分、饲料配方、饲喂策略与对照）",
            "results（生长、饲料转化、粪便与福利）",
            "discussion",
            "references",
        ),
        "welfare_study": (
            "abstract",
            "introduction",
            "methods（观察设计、评分表与观察者培训）",
            "results（福利评分与行为记录）",
            "discussion（阈值与管理改进）",
            "references",
        ),
        "environmental": (
            "abstract",
            "introduction",
            "methods（采样点、仪器与监测频率）",
            "results（温湿度、气体与颗粒物分布）",
            "discussion（通风方案与减排潜力）",
            "references",
        ),
    },
    citation_style="Elsevier/Vancouver 样式（编号制；Livestock Sci. 遵循 Elsevier 规范）",
    reporting_standards={
        "group": "群体、性别、日龄/月龄与初始体重须完整报告",
        "housing": "舍型、密度、通风与光照（时长、强度）须报告",
        "feeding": "饲料配方（能量、蛋白、氨基酸、微量元素）与饲喂策略须完整",
        "welfare": "福利评分表与观察者培训须报告",
        "environment": "舍内温湿度、CO2/NH3/PM 须报告采样点与频率",
    },
    conventions=(
        "动物来源、品种与日龄（或初始体重）须以统一方式报告",
        "饲料配方按干物质（DM）或粗蛋白（CP）水平报告并给出原料来源",
        "福利评分须给出评分表版本与观察者培训记录",
        "环境参数以均值 ± SD 报告并注明采样点与时间分辨率",
        "缩写首次出现给出全称（如 CP = crude protein）",
    ),
    key_venues=(
        "Animal Feed Science and Technology",
        "Livestock Science",
        "Computers and Electronics in Agriculture",
        "Journal of Applied Animal Welfare Science",
        "Animal Welfare",
        "Poultry Science",
        "World's Poultry Science Journal",
    ),
    units_and_formulas_notes=(
        "体重用 kg；体长用 cm；饲养密度用 头/㎡ 或 只/㎡",
        "温度用 °C、湿度用 %RH；CO2 与 NH3 用 ppm 或 mg/m^3",
        "饲料转化按干物质计（kg DM/kg gain）",
        "光照用 lx 与日时长 h/d；通风用换气次数次/h",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Dairycomp DFM", "Bovision Dairy Manager", "DeLaval PROXIMITY", "DeLaval FEEDSTAR", "MooMonitor", "COW-Log", "ViviFarm", "Allflex eID", "Allflex TracTags", "AgroNerd", "InGroom", "PoultryTools", "Foss Kjeltec", "Foss FIBEX", "Foss Foodscan F/4010", "Karl Heidenreich", "R", "SPSS", "SAS", "Bovisync"),
    category="农学",
    databases=("Crossref", "OpenAlex", "CNKI", "Sciencedirect"),
)
