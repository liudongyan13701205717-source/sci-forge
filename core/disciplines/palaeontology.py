"""古生物学（英式拼写）学科论文支持：化石描述、系统发育与地层体裁、命名法规与国际年代地层表注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="palaeontology",
    aliases=(
        "palaeontology",
        "古生物学",
        "Palaeontology",
        "化石生物学",
        "化石",
        "古生态",
        "Palaeobiology",
        "化石研究",
        "palaeobiology"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（标本案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references"
        ),
    },
    citation_style="Paleontological Society 样式（作者-年份）",
    reporting_standards={
        "k1": "新属新种描述遵循国际命名法规（ICZN/ICBN/ICNP）",
        "k2": "系统发育研究遵循矩阵与分析报告规范",
        "k3": "数据论文遵循形态与化石记录数据规范，综述遵循 PRISMA"
    },
    conventions=(
        "化石产地、层位与标本编号须完整著录",
        "标本存放机构与馆藏号须注明",
        "系统发育分析须报告矩阵、权重、模型与统计支持值",
        "地层年代须注明定年方法与国际年代地层表对应关系",
        "测量数据须报告样品数、均值、标准差与样本量"
    ),
    key_venues=(
        "Journal of Paleontology",
        "Paleobiology",
        "Palaeontology",
        "Journal of Vertebrate Paleontology",
        "Palaeogeography, Palaeoclimatology, Palaeoecology"
    ),
    units_and_formulas_notes=(
        "尺寸以 mm 或 cm 报告，年代以 Ma 报告",
        "地层年代须对应国际年代地层表并注明基准",
        "坐标须注明经纬度与基准（如 WGS84）",
        "系统发育支持值须报告（aLRT/UF-bootstrap/后验概率）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("PhyloSuite", "T-REX", "MESQUITE", "PAUP*", "MrBayes", "RAxML", "MEGA", "MorphoTools", "geomorph", "MorphoDig", "TimeTree", "PaleobioDB", "GeoMap.org", "GPlates", "CT 扫描（微焦点 X 射线）", "3D 建模（Meshlab）", "QGIS", "R", "EndNote", "Microsoft Excel"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
