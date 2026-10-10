"""野生动植物管理学科论文支持：野外监测、栖息地保护与生态保护政策研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wildlife_ranger_studies",
    aliases=(
        "wildlife ranger studies",
        "野生动物巡护",
        "生态保护",
        "自然保护地管理",
        "wildlife patrol",
        "conservation area management",
        "自然保护",
        "野生动物保护",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "study area（研究区域与生态系统描述）",
            "methods（巡护与监测方法）",
            "results（监测结果与威胁评估）",
            "discussion（管理意义与对策）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "site description（保护地概况）",
            "ranger program description（巡护制度与人员配置）",
            "threat monitoring and response（威胁监测与应对）",
            "effectiveness assessment（成效评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "ranger practices overview（巡护实践综述）",
            "technology integration（技术装备综述）",
            "community involvement（社区参与综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "patrol records": "巡护日志须完整记录时间、路线、发现、处置与上报",
        "threat documentation": "盗猎/栖息地破坏等威胁须有影像/物证与空间定位记录",
        "population surveys": "种群调查须说明方法、样点密度与重复次数",
        "intervention reporting": "干预措施须报告实施时间、范围、资源投入与成效",
    },
    conventions=(
        "保护地等级参照 IUCN 保护地管理类别（Ia-VI）或国家标准",
        "物种保护等级引用 IUCN 红色名录与中国国家重点保护名录",
        "威胁类型分类引用 CITES 附录或国际自然保护联盟分类",
        "巡护区域面积单位 km²；巡护频次单位 次/月",
        "地理坐标使用 WGS84 系统，标注定位精度",
    ),
    key_venues=(
        "Biological Conservation",
        "Conservation Biology",
        "Nature Conservation",
        "Conservation Areas",
        "Journal of Nature Conservation",
    ),
    units_and_formulas_notes=(
        "巡护覆盖率 = 实际巡护面积 / 保护地总面积×100%",
        "物种发现率 = 记录物种数 / 预期物种数×100%",
        "盗猎案件发生率单位 起/km²·年",
        "社区补偿标准单位 元/户·年",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("红外触发相机（Reconyx、Bushnell）", "GPS 巡护系统（如 TrackUnit、WiiTrack）", "手持 GPS 定位仪（Garmin GPSMAP 66i）", "无人机巡查系统（DJI Mavic Enterprise）", "声学监测设备（Song Meter SM4）", "遥感卫星影像（Sentinel-2、Landsat 9）", "GIS 软件（ArcGIS Pro、QGIS）", "无人机航测相机（Sony α7R IV）", "电子围栏系统（虚拟围栏平台）", "动物诱捕器与陷阱（非致死型）", "DNA 样本采集工具（FTA 卡）", "PCR 基因检测实验室（Thermo Fisher PCR仪）", "Python 数据分析（pandas）", "R 语言统计分析", "LaTeX 学术排版", "EndNote 文献管理", "野外记录软件（如 iNaturalist）", "CITIZEN SCIENCE 平台（eBird、Mushroom Observer）", "巡护任务管理 SaaS（如 Ranger Connect）", "无人机热成像（DJI Zenmuse Thermal）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
