"""国防研究学科论文支持：国防研究/防务政策体裁、Chicago 引用样式与国防研究记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="defense_studies",
    aliases=("defense_studies", "国防研究", "防务研究", "国防政策", "defence studies"),
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
            "policy background（政策背景）",
            "analysis（政策选项评估）",
            "recommendations（政策建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份；Defense Stud 遵循 Chicago 规范）",
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
        "Defense Studies",
        "Journal of Defense Resources Management",
        "Defence and Peace Economics",
        "Armed Forces & Society",
        "The RUSI Journal",
        "Military Balance (IISS)",
    ),
    units_and_formulas_notes=(
        "军费用本币/美元并注明年份；占比用 %GDP",
        "公式用 amsmath；预算与效能计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "汇率与通胀调整须注明基准年",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "报告"),
    tools=(
        "政策文本分析工具（NVivo）",
        "GIS 空间分析（ArcGIS）",
        "兵棋推演软件",
        "系统动力学模型（Vensim）",
    ),
    category="军事学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)