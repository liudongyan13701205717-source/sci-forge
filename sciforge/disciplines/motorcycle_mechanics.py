"""摩托车维修学科论文支持：摩托车故障诊断与修理工艺体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="motorcycle_mechanics",
    aliases=(
        "motorcycle_mechanics", "摩托车维修", "Motorcycle mechanics",
        "motorcycle repair", "摩托车修理", "二轮机修",
        "机车维修", "motorcycle engineering",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（测试方法）",
            "results（试验结果）",
            "discussion（分析与建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（故障描述）",
            "analysis（诊断过程）",
            "results（修复结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（工艺综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "故障诊断研究须报告样本量与故障类型分布",
        "k2": "改装试验须报告测试工况与仪表参数",
        "k3": "维修工艺研究须报告工艺步骤与验收标准",
    },
    conventions=(
        "故障类型使用标准故障树术语",
        "扭矩值给出牛顿·米并注明拧紧顺序",
        "发动机数据须区分冷机与热机",
        "改装前后数据须给出对照组",
        "引用厂修手册须给出年份与版本",
    ),
    key_venues=(
        "SAE International Journal of Fuels and Lubricants",
        "SAE Technical Papers",
        "Journal of Automotive Engineering",
        "Automotive Engineering International",
        "《摩托车技术》",
    ),
    units_and_formulas_notes=(
        "力矩用 N·m；压力用 bar",
        "转速用 rpm；功率用 kW 或 PS",
        "温度用 °C；燃油标号须明确",
        "油耗用 L/100km；排放用 g/km 或 ppm",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Autel MaxiSys", "LAUNCH X431", "Snap-on Verus Tech 3", "OBDLink EX", "NI ScanXEL", "Tech2 Live", "Autel IM608", "Snap-on Command Elite", "Motorola SDR3", "KohTek KT270", "Snap-on GDS3", "TechForce Pro 5800", "Kestrel 5500", "Fluke 87V", "Snap-on T700", "Snap-on P2500", "EndNote", "MATLAB", "SolidWorks", "Microsoft Excel"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
