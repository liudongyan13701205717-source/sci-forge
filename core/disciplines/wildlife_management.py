"""野生动物管理学科论文支持：种群动态监测、栖息地保护与生态评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wildlife_management",
    aliases=(
        "wildlife management",
        "野生动物管理",
        "野生动物保护",
        "种群管理",
        "wildlife conservation",
        "population management",
        "habitat management",
        "野生动物保育",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "study area（研究区域描述）",
            "methods（调查/监测方法）",
            "results（种群动态与栖息地评估结果）",
            "discussion（生态意义与管理建议）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "site description（样地/保护区描述）",
            "management actions（管理措施描述）",
            "monitoring and evaluation（监测与评估）",
            "effectiveness assessment（有效性评价）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical framework（种群生物学理论综述）",
            "management strategies（管理策略综述）",
            "human-wildlife conflict（人兽冲突综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "species identification": "物种鉴定须基于形态学或分子标记证据，标注鉴定方法与置信度",
        "sampling protocol": "调查方法须详述样线/样方/陷阱/红外相机等方案与参数",
        "statistical analysis": "种群估算须说明采用 CAPTURE/Program MARK 等模型及拟合结果",
        "ethical approval": "涉及动物采样须获得动物伦理委员会批准并标注批准号",
    },
    conventions=(
        "物种名首次出现时标注中文名与拉丁名（学名），后续使用学名",
        "种群密度单位统一使用 ind/km²（个/平方公里）",
        "栖息地分类参照 IUCN 或本地保护地分类标准",
        "保护等级引用 IUCN 红色名录或中国国家重点保护名录",
        "地理坐标使用 WGS84 坐标系统，标注精度（GPS/相机定位精度）",
    ),
    key_venues=(
        "Biological Conservation",
        "Conservation Biology",
        "Journal of Wildlife Management",
        "Oryx",
        "Mammal Research",
    ),
    units_and_formulas_notes=(
        "种群密度单位 ind/km²；种群增长率单位 /年",
        "栖息地面积单位 km² 或公顷（ha）；景观破碎化指数（Shannon 指数）",
        "红外相机有效工作距离单位 m；触发灵敏度单位 秒",
        "物种丰富度用 Shannon-Wiener 指数（H'）或 Simpson 指数（D）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("红外触发相机（如 Reconyx、Bushnell）", "GPS 定位颈圈/项圈（卫星追踪器，如 Telonics、Lotek）", "声学监测设备（Acoustic Monitoring，如 Song Meter）", "无人机遥感（DJI Phantom/Inspire）", "遥感卫星（Sentinel-2、Landsat）", "GIS 软件（ArcGIS Pro、QGIS）", "遥感影像处理软件（ENVI、Erdas Imagine）", "种群分析软件（CAPTURE、Program MARK）", "栖息地适宜性模型（MaxEnt）", "分子标记实验室（PCR、电泳仪）", "DNA 提取仪（如 Qiagen QIAamp）", "基因测序仪（Illumina MiSeq）", "无人机航测相机（如 Sony α7R IV）", "样方调查工具（卷尺、罗盘、GPS 手持机）", "Python 数据分析（pandas、scipy）", "R 语言统计分析", "LaTeX 学术排版", "EndNote 文献管理", "Field Notes 野外记录", "CITIZEN SCIENCE 平台（如 eBird）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
