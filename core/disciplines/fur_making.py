"""毛皮制造学科论文支持：皮革鞣制、毛皮染色、皮草服装工艺与质量控制。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fur_making",
    aliases=("fur_making", "fur", "毛皮制造", "皮草加工", "皮革鞣制", "毛皮染色", "皮草服装", "皮草工艺"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "tanning": "鞣制工艺须报告试剂种类、浓度与时间参数",
        "dyeing": "染色工艺须报告染料配方、温度与染色时间",
        "quality": "质量检验须报告检测方法与标准编号"
    },
    conventions=(
        "皮革/毛皮厚度须标注测量位置",
        "染色配方须注明染料批次与用量",
        "鞣制条件须完整记录（温度、pH、时间）",
        "成品规格须用标准化尺码标注",
        "毒性物质含量须报告检测方法与限值"
    ),
    key_venues=(
        "Journal of Leather Science",
        "Leather & Tanning",
        "Journal of Textile and Apparel Technology Management",
        "International Journal of Apparel and Fashion",
        "Textile Research Journal"
    ),
    units_and_formulas_notes=(
        "毛皮密度用 g/cm³",
        "鞣制剂浓度用 g/L",
        "染色温度用 °C",
        "强度用 N 或 MPa",
        "色牢度用级（1-5 级）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Fur Cutting Machine", "Fur Design Software", "Tanning Equipment", "Dye Machine", "Sewing Machine", "Stitching Machine", "Fur Press", "Fur Steamer", "Leather Cutter", "Fur Grading Machine", "Fur Dye Machine", "Fur Finishing Machine", "Fur Quality Tester", "Fur CAD System", "Fur Sewing Machine", "Fur Lasting Machine", "Fur Pressing Machine", "Fur Finishing Station", "Fur Cutting Platform", "Fur Processing Line"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
