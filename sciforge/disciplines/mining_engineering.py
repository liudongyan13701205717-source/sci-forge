"""采矿工程学科论文支持：采矿方法/岩石力学/选矿体裁、SME 引用样式与采矿记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mining_engineering",
    aliases=("mining_engineering", "采矿工程", "采矿", "选矿", "岩石力学",
             "矿山安全"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与采矿问题）",
            "methods（实验、建模与参数）",
            "results（岩体/工艺数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "mine_design": (
            "abstract",
            "introduction",
            "geology and resources（地质与资源）",
            "mining method selection（采矿方法选择）",
            "design（开拓/采准/回采设计）",
            "economic analysis（经济分析）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="SME 样式（作者-年份；SME 期刊遵循 SME 规范）",
    reporting_standards={
        "experimental": "岩石力学实验遵循 ISRM 建议方法",
        "geotechnical": "岩土工程遵循 ISRM/ISSMGE 规范",
        "safety": "矿山安全遵循 MSHA 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "economic_evaluation": "经济评价遵循 SME 经济评价规范",
    },
    conventions=(
        "矿体产状与储量分级（JORC/储量规范）须注明",
        "岩石力学参数（强度、模量）须报告试验方法",
        "采矿方法术语须统一",
        "安全系数与支护设计准则须明确",
        "品位/回收率单位须规范",
    ),
    key_venues=(
        "Mining Engineering",
        "International Journal of Mining Science and Technology",
        "Minerals Engineering",
        "International Journal of Rock Mechanics and Mining Sciences",
        "Journal of the Southern African Institute of Mining and Metallurgy",
        "Mining, Metallurgy & Exploration",
    ),
    units_and_formulas_notes=(
        "应力用 MPa；深度用 m；品位用 % 或 g/t",
        "公式用 amsmath；强度准则与稳定性方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "储量用 Mt；回收率用 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("ANSYS", "3D MineDesign", "Python", "FLAC3D"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Zenodo", "CNKI"),
)