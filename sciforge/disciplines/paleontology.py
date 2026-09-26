"""古生物学学科论文支持：化石/系统发育/地层体裁、Paleontological Society 引用样式与地质记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="paleontology",
    aliases=("paleontology", "古生物学", "化石", "古生态"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "geological setting（地质背景）",
            "materials and methods（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "taxonomic_description": (
            "abstract",
            "introduction",
            "systematic paleontology（系统古生物学）",
            "description（描述）",
            "comparison（比较）",
            "discussion（讨论）",
            "references",
        ),
        "phylogenetic_study": (
            "abstract",
            "introduction",
            "taxon sampling（分类单元取样）",
            "character matrix（性状矩阵）",
            "analysis（系统发育分析）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="Paleontological Society 样式（作者-年份；J Paleontol 遵循古生物学会规范）",
    reporting_standards={
        "taxonomic": "分类描述遵循国际命名法规（ICZN/ICBN）",
        "phylogenetic": "系统发育研究遵循矩阵与分析报告规范",
        "observational": "观察研究遵循化石描述报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循形态数据规范",
    },
    conventions=(
        "化石产地与地层须报告",
        "标本编号与存放机构须注明",
        "命名须符合命名法规",
        "系统发育分析参数须说明",
        "地层年代须注明定年方法",
    ),
    key_venues=(
        "Journal of Paleontology",
        "Paleobiology",
        "Palaeontology",
        "Journal of Vertebrate Paleontology",
        "Palaeogeography, Palaeoclimatology, Palaeoecology",
        "Proceedings of the Royal Society B（古生物方向）",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm 或 cm；年代用 Ma",
        "地层用阶/统并注明国际年代地层表",
        "公式用 amsmath；分支图与矩阵须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "坐标用经纬度并注明基准",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("GIS", "CT 扫描", "古生物标本数字化", "MATLAB"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)