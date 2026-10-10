"""餐饮服务学科论文支持：餐饮运营、服务流程优化与顾客行为研究的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="waiting_and_bar_service",
    aliases=("waiting_and_bar_service", "餐饮服务", "酒吧服务", "餐饮服务与管理",
             "waiter", "bartender", "food and beverage service",
             "hospitality service", "餐饮管理", "酒店餐饮"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "literature review（文献综述）",
            "methods（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions and implications（结论与启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（案例背景）",
            "case description（案例描述）",
            "analysis（分析）",
            "findings（发现）",
            "management implications（管理启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "industry trends（行业趋势）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "case_description": "案例研究须包含服务流程、员工配置、运营时段与客群特征描述",
        "data_collection": "满意度调查须说明样本量、抽样方法、量表来源与信效度指标（如 Cronbach's α）",
        "ethics": "涉及顾客隐私的数据须获得知情同意并进行匿名化处理",
    },
    conventions=(
        "服务流程使用 BPMN（业务流程模型与标记法）或流程图表示",
        "财务数据以人民币（CNY）标注，汇率换算时标注日期与来源",
        "员工绩效评估采用 KPI 或 OKR 框架，给出指标定义与权重",
        "满意度量表采用 Likert 5 级或 7 级评分，并标注量表来源",
        "案例描述须注明时间、地点、经营业态与客群画像",
    ),
    key_venues=(
        "International Journal of Hospitality Management",
        "Cornell Hospitality Quarterly",
        "International Journal of Contemporary Hospitality Management",
        "Tourism Management",
        "Service Industries Journal",
    ),
    units_and_formulas_notes=(
        "营收单位为人民币（元）或美元（USD），换算标注汇率日期",
        "时间指标以小时（h）或分钟（min）为单位",
        "客流量以人次/日或人次/周为单位",
        "满意度评分为 1-5 或 1-7 级 Likert 标度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Toast POS", "OpenTable", "Microsoft Excel", "SPSS", "NVivo", "AMOS", "SmartPLS", "Qualtrics", "Google Forms", "Tableau", "OpenRefine", "LaTeX", "Figma", "SketchUp", "AutoCAD", "Revit", "Python", "R", "Minitab", "Wine-Logix"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
