"""清烟筒学科论文支持：职业安全、烟道维护与烟尘测量的写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chimney_sweeping",
    aliases=(
        "chimney sweeping", "清烟筒", "烟筒清理",
        "chimney sweep", "烟囱清理工",
        "chimney cleaning", "烟囱清洁",
        "flue cleaning", "烟道清理",
        "soot removal", "积碳清理",
        "ventilation maintenance", "通风维护",
        "smokestack maintenance", "烟囱维护",
        "wood stove maintenance", "壁炉维护",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "case study": (
            "abstract",
            "background",
            "case description",
            "results",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "state of the art",
            "challenges and future",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "observation": "观察记录遵循观察报告规范",
        "measurement": "测量结果遵循测量报告规范（含仪器精度与不确定度）",
        "safety": "涉及职业安全须遵循 GB/T 16483 与 ANSI/CSA 标准",
        "sustainability": "涉及能耗/排放须遵循 ISO 14064 或 GHG Protocol",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
    },
    conventions=(
        "测量仪器型号/精度须注明",
        "职业安全指标遵循 GB/T 16483 与 ANSI/CSA Z415",
        "烟尘排放指标给出口径（如 mg/m³、mg/L）",
        "维护/清理频次按周期/次数记录",
        "引用清洁/维护案例须注明设备与燃烧介质",
    ),
    key_venues=(
        "Journal of the Air & Waste Management Association",
        "Atmospheric Environment",
        "Fuel",
        "Energy and Buildings",
        "Building and Environment",
        "Combustion and Flame",
        "Fuel Processing Technology",
        "中国环境科学",
    ),
    units_and_formulas_notes=(
        "烟尘排放 mg/m³；颗粒物 µg/m³；温度 ℃",
        "烟道长度以 m 计；直径以 mm 计",
        "维护频次以次/年、次/月记录",
        "能耗给 kWh/年 或 MJ/kg",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Chimney Rod Kit 烟囱杆套装", "Chimney Sweep Brush Set 烟囱清洁刷组", "Flue Liner Inspection Tool 烟道衬检测工具", "Industrial Endoscope 工业内窥镜", "Chimney Camera Inspection 烟囱内窥镜", "Kidde 烟感探测器", "Kidde N2630 烟感探测器", "Kidde N3403 烟感探测器", "Kidde COM300 一氧化碳探测器", "GASMET 手持式 CO 检测仪", "Smiths Group SM-A1 烟尘分析仪", "TEOM 5500i 颗粒物监测仪", "TEOM 1400a 颗粒物监测仪", "PMS5003 颗粒物计数器", "PMS3003 颗粒物计数器", "PMS4003 颗粒物计数器", "PMS5003S 颗粒物计数器", "FLIR E8 红外热像仪", "FLIR E9 红外热像仪", "FLIR E10 红外热像仪", "FLIR Ex-PRO20 红外热像仪", "FLIR Ex-PRO25 红外热像仪", "Flir C5 红外热像仪", "Flir C6 红外热像仪", "Flir C8 红外热像仪", "Flir C2 红外热像仪", "Gorilla 145 工业吸尘器", "Nilfisk 95GSC 工业吸尘器", "Nilfisk 99 GSC 工业吸尘器", "Nilfisk AT 20-21 工业吸尘器", "Nilfisk AC3000 工业吸尘器", "Nilfisk SC50 工业吸尘器", "Nilfisk SC55 工业吸尘器", "Nilfisk AC4000 工业吸尘器", "Nilfisk AC6100 工业吸尘器", "Nilfisk AC8100 工业吸尘器", "Nilfisk SC70 工业吸尘器", "Nilfisk SC75 工业吸尘器", "Nilfisk AC5000 工业吸尘器", "Nilfisk AC6500 工业吸尘器", "Nilfisk SC55E 工业吸尘器", "Nilfisk SC70E 工业吸尘器", "Nilfisk SC75E 工业吸尘器", "Nilfisk SC50E 工业吸尘器", "Nilfisk AT30 工业吸尘器", "Nilfisk AT35 工业吸尘器", "Nilfisk AT40 工业吸尘器", "Nilfisk AC5500 工业吸尘器", "Nilfisk AC6000 工业吸尘器", "Nilfisk AC7000 工业吸尘器"),
    category="工学",
    databases=("Crossref", "OpenAlex", "Web of Science", "Scopus", "CNKI"),
)
