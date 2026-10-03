"""石油工程学科论文支持：油气藏/钻井/采油体裁、SPE 引用样式与石油工程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="petroleum_engineering",
    aliases=("petroleum_engineering", "石油工程", "石油", "油气藏工程",
             "钻井工程", "采油工程"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与油气问题）",
            "methods（实验、建模与参数）",
            "results（岩心/油藏数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "reservoir_study": (
            "abstract",
            "introduction",
            "reservoir description（油藏描述）",
            "modeling（数值模拟）",
            "history matching（历史拟合）",
            "prediction（预测与方案）",
            "references",
        ),
        "field_case": (
            "abstract",
            "introduction",
            "field background（油田背景）",
            "methodology（工艺/方案）",
            "results（现场数据与效果）",
            "lessons learned（经验教训）",
            "references",
        ),
    },
    citation_style="SPE 样式（编号制；SPE 期刊遵循 SPE 规范）",
    reporting_standards={
        "experimental": "岩心/流体实验遵循 SPE 实验报告规范",
        "reservoir_simulation": "油藏数值模拟遵循 SPE 模拟研究规范",
        "field_case": "现场案例遵循 SPE 案例报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "economic_evaluation": "经济评价遵循 SPE 经济评价规范",
    },
    conventions=(
        "油藏单位制（油田单位或 SI）须统一并注明",
        "孔隙度/渗透率/饱和度符号须规范",
        "流体性质（PVT）数据须完整报告",
        "模拟网格与边界条件须说明",
        "产量/压力数据给出时间基准",
    ),
    key_venues=(
        "SPE Journal",
        "Journal of Petroleum Technology",
        "SPE Reservoir Evaluation & Engineering",
        "SPE Drilling & Completion",
        "Journal of Petroleum Science and Engineering",
        "SPE Production & Operations",
    ),
    units_and_formulas_notes=(
        "渗透率用 mD；压力用 psi 或 MPa（注明单位制）",
        "公式用 amsmath；达西方程与物质平衡须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "采收率用 %；储量用 MMbbl 或 10⁴ t",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("ECLIPSE 油藏模拟器", "Python", "SeisSpace", "Petrel"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Zenodo", "CNKI"),
)