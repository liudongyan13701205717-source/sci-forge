"""Custodian/caretaker 学科论文支持：设施养护/物业运维/建筑环境性能体裁、设施管理报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="custodiancaretaker",
    aliases=(
        "custodiancaretaker",
        "custodian/caretaker",
        "custodian and caretaker",
        "custodial services",
        "养护管理",
        "物业运维",
        "facilities upkeep",
        "building caretaking",
        "facility management operations",
        "custodial operations",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "materials and methods（对象、设备与方法）",
            "results（结果与性能数据）",
            "discussion（讨论）",
            "conclusions",
            "references",
        ),
        "performance_study": (
            "abstract",
            "introduction",
            "facility profile（设施概况）",
            "measurement protocol（测量规程）",
            "performance results（性能结果）",
            "maintenance implications（养护启示）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction（案例背景）",
            "incident description（事件/作业描述）",
            "measures taken（处置措施）",
            "outcomes and follow-up（结果与跟踪）",
            "references",
        ),
    },
    citation_style="IEEE 样式（工程设备与仪器类）；管理类成果遵 APA 第7版",
    reporting_standards={
        "measurement": "环境参数测量须报告仪器型号、校准有效期、量程与精度、测点位置",
        "protocol": "作业规程须遵循厂商与维护手册规定，偏离须记录理由",
        "safety": "涉高风险作业（高空、电气、密闭空间）须报告安全评估与防护措施",
        "energy": "能耗统计须注明计量口径、基准期与天气/使用强度归一化方法",
        "maintenance": "维保记录须可追溯至工单编号、执行人与验收结果",
    },
    conventions=(
        "环境参数统一单位：照度 lx、噪声 dB(A)、温度 °C、相对湿度 %RH、CO₂ ppm、PM2.5 μg/m³",
        "设备引用须给出厂商 + 型号 + 序列号，软件平台给出版本号",
        "工单、巡检与维保记录编号规则全文一致，可追溯",
        "能耗与费用数据须注明口径（含/不含公摊、是否分摊人力）",
        "测点位置与样本量须报告，重复测量给出均值±标准差",
        "安全与合规条款须引用现行标准全称、编号与年份（如 GB/T、ISO 41001）",
    ),
    key_venues=(
        "Facilities Management",
        "Journal of Facilities Management",
        "Building and Environment",
        "Energy and Buildings",
        "Indoor and Outdoor Built Environment",
        "International Journal of Building Physics and Environment",
        "物业管理学刊",
    ),
    units_and_formulas_notes=(
        "照度 lx；噪声 dB(A)；温度 °C；相对湿度 %RH；CO₂ ppm；PM2.5 μg/m³",
        "能耗以 kWh 计量，单位面积能耗 W/m² 或 kWh/m²·a 并注明建筑面积口径",
        "压差用 Pa；风量用 m³/h；功率因数无量纲",
        "寿命类数据用小时或次数，须注明测试工况",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("IBM Maximo", "FM:Systems", "planful (planfulFM)", "Infor EAM", "UpKeep", "FieldPulse", "Fiix FM", "ServiceChannel", "Autodesk Revit", "Navisworks", "EcoStruxure Building Operation (Schneider Electric)", "Honeywell Building Enterprise", "Siemens Desigo", "Johnson Controls Metasys", "Tridium Niagara", "Energy Star Portfolio Manager", "Fluke Ti40 Pro", "Aranet4", "Protimeter DampMeter", "Sekonic C800", "DustTrak (TSI)", "Extech 407755", "Dräger X-am 5000", "Fluke 87V MAX"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "Scopus", "Web of Science", "Google Scholar"),
)
