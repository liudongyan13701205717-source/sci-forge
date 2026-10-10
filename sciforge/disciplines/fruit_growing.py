"""果树栽培学科论文支持：果树栽培、修剪、病虫害防治与果园管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fruit_growing",
    aliases=("fruit_growing", "fruit tree", "果树栽培", "果树种植", "果园管理", "果树修剪", "果树病虫害", "果树育种"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methods（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA（作者-年份）",
    reporting_standards={
        "variety": "品种须用标准化名称与编号",
        "pruning": "修剪须遵循标准化修剪规范",
        "disease": "病害防治须遵循标准化用药规范",
        "harvest": "采收须遵循标准化采收规范"
    },
    conventions=(
        "品种用标准化名称（附学名）",
        "修剪方式用标准化术语（疏枝、短截等）",
        "产量用 kg/ha 或 t/ha",
        "树体参数用标准术语（树冠、株高）",
        "病虫害须用标准化学名"
    ),
    key_venues=(
        "Journal of Horticultural Science and Biotechnology",
        "HortScience",
        "Journal of Plant Research",
        "Acta Horticulturae",
        "果树学报"
    ),
    units_and_formulas_notes=(
        "产量用 kg/ha 或 t/ha",
        "株高用 m",
        "树冠直径用 m",
        "株距用 m",
        "施肥量用 kg/ha"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GIS software", "Remote sensing software", "Drone", "Fruit grower's knife", "Pruning shear", "Ladder", "Fruit tree grafting tool", "Fertilizer applicator", "Sprayer", "Soil moisture sensor", "Weather station", "Pest monitoring trap", "Pollen collector", "Insecticide applicator", "Fruit harvester", "Irrigation system", "Mulching machine", "Compost pile builder", "Seedling nursery system", "Bee hive system"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
