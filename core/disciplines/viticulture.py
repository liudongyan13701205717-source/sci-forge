"""葡萄栽培学科论文支持：葡萄品种/栽培/酿造研究体裁、Vancouver 引用与农业度量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="viticulture",
    aliases=("viticulture", "葡萄栽培", "葡萄种植", "vine cultivation",
             "葡萄品种", "vineyard", "葡萄园", "葡萄育种"),
    paper_types={
        "research": (
            "structured abstract",
            "introduction（栽培问题与研究假设）",
            "methods（栽培设计、品种、处理、结局指标）",
            "results（生长、产量与品质分析）",
            "discussion（栽培外推性与生产意义）",
            "references",
        ),
        "variety_trial": (
            "abstract",
            "introduction",
            "materials and methods（品种与材料）",
            "results（生长与品质表现）",
            "discussion（品种适应性与选择建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver（Vitis Science/Agriculture 体例）",
    reporting_standards={
        "variety_trial": "品种试验报告规范",
        "systematic_review": "PRISMA",
        "field_study": "田野研究报告规范",
    },
    conventions=(
        "品种名称须遵循 VIVC 国际葡萄品种目录规范",
        "砧木与接穗须注明品种与亲本来源",
        "栽培制度须给整枝方式、密植与架式",
        "品质指标须给采样时间与方法",
        "气候数据须给积温与降雨量并注明测站",
    ),
    key_venues=(
        "American Journal of Enology and Viticulture",
        "Vitis Journal",
        "Journal of the Science of Food and Agriculture",
        "Acta Horticulturae",
        "European Journal of Agronomy",
    ),
    units_and_formulas_notes=(
        "产量给 kg/ha 或 t/ha",
        "糖度给 °Brix；酸度给 g/L",
        "单穗重给 g；果粒数给 粒/穗",
        "积温给 °C·d（≥10°C 活动积温）",
        "产量变化给 % 并与对照比较",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "MATLAB", "葡萄园土壤分析仪", "葡萄园气象站", "葡萄园无人机", "葡萄园传感器网络", "葡萄园灌溉控制器", "葡萄园自动化设备", "葡萄园机器人", "葡萄园土壤硬度仪", "葡萄园土壤水分仪", "葡萄园温度记录仪", "葡萄园湿度记录仪", "葡萄园光照仪", "葡萄园风速仪", "葡萄园雨量计", "葡萄园植物生长分析仪", "葡萄园果实品质分析仪", "葡萄园病虫害监测仪"),
    category="农学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
