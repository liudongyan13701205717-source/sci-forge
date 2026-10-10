"""草药学学科论文支持：药用植物与植物化学体裁、Vancouver 引用样式与草药记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="herbology",
    aliases=("herbology", "植物药", "草药学", "药草学", "药用植物", "药用植物学", "药草", "草药研究", "药用植物研究"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver（作者-序号）",
    reporting_standards={
        "ethnobotanical": "民族植物学规范",
        "chemical": "化学研究规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "植物名称须给出学名",
        "采集/处理须报告",
        "成分分析须报告",
        "生物活性须报告",
        "分类须遵循最新分类",
    ),
    key_venues=(
        "Journal of Ethnopharmacology",
        "Phytotaxa",
        "Phytochemistry",
        "Plant Diversity",
        "Phytochemical Reviews",
    ),
    units_and_formulas_notes=(
        "剂量用 mg/g",
        "公式用 amsmath；化学公式须编号",
        "行内公式避免复杂分式",
        "数值结果给出均值±SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Python (SciPy)", "HPLC", "GC-MS", "LC-MS", "NMR", "UV-Vis", "FTIR", "TLC", "Ethnobotanical Database", "TCM Database", "iNaturalist", "GBIF", "PlantNet", "Flora of China", "Flora of North America", "Flora of Japan", "World Checklist of Vascular Plants", "Phytochemistry Software"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
