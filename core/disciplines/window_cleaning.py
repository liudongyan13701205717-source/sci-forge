"""高空外墙清洗学科论文支持：清洗作业安全规范、效率评估与作业标准研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="window_cleaning",
    aliases=(
        "window cleaning",
        "外墙清洗",
        "玻璃清洗",
        "高空清洗作业",
        "window cleaning management",
        "facade cleaning",
        "外墙清洗管理",
        "玻璃幕墙清洗",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（行业背景与问题）",
            "literature review（安全与效率研究综述）",
            "data and methods（数据来源与方法）",
            "findings（效率与安全风险发现）",
            "discussion（管理启示）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "building profile（建筑概况描述）",
            "cleaning method and process（清洗方法与流程）",
            "safety and efficiency analysis（安全与效率分析）",
            "recommendations（改进建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "cleaning technology overview（清洗技术综述）",
            "safety regulations（安全规范综述）",
            "cost and productivity（成本与产能综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "safety protocols": "作业流程须完整报告安全装备、坠落防护方案与应急救援预案",
        "building characteristics": "建筑高度、外立面材质、面积须准确报告",
        "productivity metrics": "生产效率须标注单位（㎡/小时·人）与作业条件",
        "environmental impact": "清洁剂成分与环境影响须符合 GB 15618 标准",
    },
    conventions=(
        "建筑高度单位 m；清洗面积单位 ㎡",
        "清洗频次按 GB/T 24996-2010 或企业标准标注（月/季/年）",
        "作业方式区分吊板/蜘蛛人、升降平台、擦窗机（RBD）、无人机",
        "清洁剂稀释比须标注（如 1:50）",
        "安全事故率单位 起/百万工时",
    ),
    key_venues=(
        "Journal of Occupational Safety and Health",
        "SAFETY Science",
        "Construction Management and Economics",
        "Building and Environment",
        "Journal of Industrial Safety",
    ),
    units_and_formulas_notes=(
        "作业效率 = 清洗面积 /（作业人数×作业时间）（㎡/人·小时）",
        "作业成本 =（人工成本+设备折旧+材料+管理费）/清洗面积（元/㎡）",
        "坠落防护系数 = 安全带承载力 / 人体体重（须≥15）",
        "清洁剂残留检测限参照 GB/T 19815（表面活性剂 mg/kg）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("建筑吊板系统（Rope Access System）", "电动升降平台（Scissor Lift）", "擦窗机（Rapid Building Machine / RBD）", "蜘蛛人安全绳索系统（Fall Arrest System）", "安全带与安全绳（CE/GB 认证）", "无人机外墙清洗系统（如 DJI Mavic + 清洗附件）", "高压水枪清洗系统（压力 100-200 bar）", "双绞盘卷扬机（双轴卷扬机）", "建筑外立面清洁评估软件", "激光测距仪（如 Bosch GCM 系列）", "风速仪（Wind Meter，作业前风速检测）", "气象观测站（作业气象条件监测）", "清洁剂残留检测试剂盒", "水质硬度测试笔（pH/电导率/硬度）", "作业管理 SaaS 平台（排班与进度跟踪）", "Python 数据分析（pandas）", "LaTeX 学术排版", "EndNote 文献管理", "Google Maps 作业区域规划", "CAD 外立面图纸设计（AutoCAD）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
