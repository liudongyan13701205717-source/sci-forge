"""可持续性科学学科论文支持：指标/情景/转型体裁、Elsevier 引用样式与可持续度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sustainability_science",
    aliases=("sustainability_science", "可持续性科学", "可持续发展", "可持续"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "framework（分析框架）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "indicator_study": (
            "abstract",
            "introduction",
            "indicator framework（指标体系）",
            "data（数据）",
            "methods（计算方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "scenario_study": (
            "abstract",
            "introduction",
            "scenario design（情景设计）",
            "model（模型）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="Elsevier 样式（作者-年份；J Clean Prod 遵循 Elsevier 规范）",
    reporting_standards={
        "indicator": "指标研究遵循指标体系报告规范",
        "scenario": "情景研究遵循情景分析报告规范",
        "life_cycle": "生命周期评估遵循 ISO 14040/14044",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循可持续数据规范",
    },
    conventions=(
        "可持续维度（经济/社会/环境）须明确",
        "指标定义与数据来源须报告",
        "时间与空间尺度须说明",
        "不确定性须报告",
        "与 SDG 的关联须注明",
    ),
    key_venues=(
        "Journal of Cleaner Production",
        "Sustainability Science",
        "Sustainable Development",
        "Sustainability",
        "Ecological Economics",
        "Nature Sustainability",
    ),
    units_and_formulas_notes=(
        "指标用无量纲指数或 %；排放用 t CO₂e",
        "强度用 t CO₂e/万元 GDP",
        "公式用 amsmath；综合指数公式须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "报告", "数据集"),
    tools=("SimaPro（生命周期评估软件）", "R（指标综合与统计）", "SPSS", "GIS（QGIS/ArcGIS）",
           "openLCA", "Python（NumPy/Pandas）"),
    category="交叉学科",
    databases=("OpenAlex", "Crossref", "CNKI", "Semantic Scholar", "Zenodo"),
)