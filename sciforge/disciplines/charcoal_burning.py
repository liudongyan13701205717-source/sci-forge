"""烧炭学科论文支持：木炭生产/炭化工艺/生物质能源/烟气排放体裁与引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="charcoal_burning",
    aliases=(
        "charcoal burning",
        "charcoal production",
        "wood charcoal",
        "charcoalization",
        "biochar",
        "烧炭",
        "木炭生产",
        "木炭制造",
        "木材炭化",
        "炭化工艺",
        "生物炭",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（能源需求与生物质来源）",
            "materials and methods（木材、炭化制度与测试方法）",
            "results（炭化产物、热值与排放数据）",
            "discussion（工艺优化与环境影响）",
            "conclusions",
            "references",
        ),
        "process": (
            "abstract",
            "introduction",
            "charcoalization process（炭化工艺与设备）",
            "product characterization（木炭物性与热值）",
            "emissions and by-products（烟气与副产物）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "taxonomy（按窑型/木材/用途分类）",
            "state of the art",
            "challenges and outlook",
            "references",
        ),
    },
    citation_style="Fuel 样式（Elsevier 编号）；生物炭引用 Bioresource Technology",
    reporting_standards={
        "feedstock": "木材品种须标注拉丁学名与初始含水率",
        "process": "炭化工艺须报告最高温度、保温时间、升温速率与炉内气氛",
        "product": "木炭须报告固定碳含量、挥发分与灰分（GB/T 21713）",
        "yield": "收炭率须注明（干基 %）；炭化产物须分馏（焦油/木醋液/木炭）",
        "emissions": "烟气排放须报告 CO/焦油含量与排放时段",
    },
    conventions=(
        "木材品种须标注拉丁学名与初始含水率",
        "炭化工艺须报告最高温度、保温时间、升温速率与炉内气氛",
        "木炭须报告固定碳含量、挥发分与灰分（GB/T 21713）",
        "收炭率须注明（干基 %）；炭化产物须分馏（焦油/木醋液/木炭）",
        "烟气排放须报告 CO/焦油含量与排放时段",
    ),
    key_venues=(
        "Bioresource Technology",
        "Fuel",
        "Industrial & Engineering Chemistry Research",
        "Biomass and Bioenergy",
        "Wood Science and Technology",
        "Waste Management",
    ),
    units_and_formulas_notes=(
        "温度用 ℃；升温速率用 ℃/min；保温时间用 min/h",
        "固定碳、挥发分、灰分用 %（干基或干燥无灰基须注明）",
        "热值用 kJ/g 或 kJ/kg；收炭率用 %（干基）",
        "烟气组分用体积分数 %；排放时段须标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Protimeter 木材水分仪", "Mettler TGA 热重分析仪", "NDIR 红外气体分析仪", "K 型热电偶", "PID 温度控制器", "木炭炭化窑", "生物质炭化炉", "Leco 固定碳分析仪", "Leco CHN 分析仪", "灰分测定仪", "挥发分测定仪", "氧弹量热仪", "烟尘仪", "Extech 烟气分析仪", "SCADA 炭化控制系统", "木炭分级筛", "木炭包装线", "热解反应炉", "木醋液蒸馏塔", "木炭灰分测定仪"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
