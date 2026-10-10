"""Defence studies (British English) 学科论文支持：防务研究/防务政策研究体裁、防务分析工具与军事学规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="defence_studies",
    aliases=(
        "defence_studies", "防务研究", "防务政策研究", "国防研究（英式）",
        "defence studies", "defence policy", "security studies",
        "military strategy", "national security studies", "military affairs",
        "armed forces studies", "military research",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与国防问题）",
            "methods（研究设计与数据来源）",
            "results（防务政策与预算数据）",
            "discussion（政策意义）",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy_background（政策背景）",
            "analysis（政策选项评估）",
            "recommendations（政策建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main_developments（按主题综述）",
            "outlook",
            "references",
        ),
        "training": (
            "abstract",
            "introduction",
            "curriculum（课程设计与教学目标）",
            "assessment（考核标准与评估）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份；Defence Stud 遵循 Chicago 规范）",
    reporting_standards={
        "policy_analysis": "政策分析遵循政策评估报告规范",
        "case_study": "案例研究遵循案例研究报告规范",
        "historical": "国防史研究遵循史料来源报告规范",
        "analytical": "防务分析遵循模型设定报告规范",
        "comparative": "比较国防研究遵循比较研究报告规范",
    },
    conventions=(
        "防务政策术语与机构名称须规范",
        "国防预算与军费数据来源须注明",
        "政策时间线与决策过程须明确",
        "涉密信息处理与脱密声明须注明",
        "评估标准（效能、成本、风险）须明确",
    ),
    key_venues=(
        "Defence Studies",
        "Journal of Strategic Studies",
        "International Affairs",
        "Strategic Studies Quarterly",
        "Armed Forces & Society",
        "Defence and Peace Economics",
        "Journal of Military Ethics",
        "Security Studies",
    ),
    units_and_formulas_notes=(
        "军费用本币/美元并注明年份；占比用 %GDP",
        "公式用 amsmath；预算与效能计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "汇率与通胀调整须注明基准年",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "R (RStudio)", "Python (pandas, networkx)", "Stata", "ArcGIS", "QGIS", "Vensim", "AnyLogic", "NetLogo", "Gephi", "UCINET", "Tableau", "Power BI", "SIPRI Database", "IISS Military Balance", "GlobalData Defense", "Wind Financial Terminal", "Statista", "RAND Corporation Tools"),
    category="军事学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
