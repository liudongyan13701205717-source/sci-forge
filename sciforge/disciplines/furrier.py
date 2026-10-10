"""毛皮工艺学科论文支持：毛皮鞣制、染色、服装加工与皮毛质量控制。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="furrier",
    aliases=("furrier", "fur craft", "毛皮工艺", "皮草工艺", "皮毛加工", "毛皮设计", "皮草服装", "皮毛鞣制"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "tanning": "鞣制工艺须报告鞣剂种类、浓度与工艺时间",
        "dyeing": "染色工艺须报告染料配方、浴比与染色时间",
        "quality": "皮毛质量须报告等级标准与检测项目"
    },
    conventions=(
        "毛皮等级须用标准化等级描述",
        "染色配方须注明染料名称、浓度与浴比",
        "鞣制剂须注明化学成分与用量",
        "成品须注明皮毛来源与产地",
        "毒性物质须报告检测方法与限值"
    ),
    key_venues=(
        "Journal of Leather Science",
        "Leather & Tanning",
        "Journal of Textile and Apparel Technology Management",
        "International Journal of Apparel and Fashion",
        "Textile Research Journal"
    ),
    units_and_formulas_notes=(
        "皮毛密度用 g/cm³",
        "鞣制剂用量用 g/m²",
        "染色温度用 °C",
        "色牢度用级（1-5 级）",
        "强度用 N 或 MPa"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Fur Tanning Equipment", "Fur Dye Machine", "Fur Cutting Machine", "Fur Sewing Machine", "Fur Press Machine", "Fur Steamer", "Fur Grading Equipment", "Fur Quality Tester", "Fur Finishing Station", "Fur CAD System", "Fur Design Software", "Fur Processing Line", "Fur Cutting Platform", "Fur Lasting Equipment", "Fur Dyeing Machine", "Fur Finishing Machine", "Fur Inspecting Tool", "Fur Grading Machine", "Fur Quality Control System", "Fur Production Software"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
