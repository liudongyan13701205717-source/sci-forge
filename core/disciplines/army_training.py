"""军事训练学科论文支持：训练方案、演习评估、模拟仿真与训练效益分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="army_training",
    aliases=(
        "army training",
        "军事训练",
        "部队训练",
        "军队训练",
        "military training",
        "combat training",
        "military education and training",
        "训练效益评估",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methodology",
            "case analysis",
            "findings",
            "training implications",
            "references",
        ),
        "evaluation": (
            "abstract",
            "introduction",
            "exercise or training description",
            "assessment framework",
            "data collection",
            "results",
            "recommendations",
            "references",
        ),
        "simulation_study": (
            "abstract",
            "introduction",
            "scenario design",
            "simulation model",
            "experiments",
            "results",
            "conclusions",
            "references",
        ),
    },
    citation_style="APA 7 或 GJB/GB 标准引用式（军事领域常混用）",
    reporting_standards={
        "simulation": "仿真模型给参数、初值与验证（validity/verification）说明",
        "evaluation": "评估指标给定义、权重与评分规则",
        "survey": "问卷与访谈给样本量、信度与保密处理",
        "classification": "涉密内容须做脱密处理并注明密级",
    },
    conventions=(
        "训练科目按《军事训练与考核大纲》条款引用",
        "演习方案给时间线、兵力编成与想定条件",
        "指标给权重与计分方法，禁止只给定性结论",
        "涉密信息脱密、脱坐标、脱番号后再写入正文",
    ),
    key_venues=(
        "Journal of Military, Strategic, and Defense Systems",
        "Defence Studies",
        "Armed Forces & Society",
        "Military Psychology",
        "Human Factors",
        "Journal of Defense Studies",
        "军事理论",
    ),
    units_and_formulas_notes=(
        "命中率/达成率 %；时长 min 或 h",
        "仿真步长 s；兵力以人/装备单位计",
        "评估等级按大纲给定量区间与定名",
        "体能指标：负重 kg、跑速 km/h、心率 bpm；训练强度按 METs 计",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Virtual Battlespace 4", "ARTEMIS", "Mission Rehearsal Systems", "Google Earth Pro", "QGIS", "ArcGIS Online", "MATLAB", "Simulink", "ANSYS", "Unity", "Unreal Engine", "AutoCAD", "Microsoft Visio", "NVivo", "SPSS", "Qualtrics", "Google My Maps", "Google Slides", "Matrikon", "Microsoft Word"),
    category="军事学",
    databases=("OpenAlex", "Crossref", "DOAJ", "CNKI"),
)
