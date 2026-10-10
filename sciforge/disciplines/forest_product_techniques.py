"""林产加工与经营学科论文支持：木材加工、竹藤编织、林产品利用与森林经营。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forest_product_techniques",
    aliases=("forest_product_techniques", "forest product technology", "林产加工", "木材加工", "竹编", "藤编", "林产利用", "林产品利用"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methods（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA（作者-年份）",
    reporting_standards={
        "timber": "木材加工须遵循标准化工艺流程",
        "bamboo": "竹编须遵循传统工艺规范",
        "processing": "林产品加工须遵循食品安全标准",
        "quality": "产品质量须遵循标准化检测规范"
    },
    conventions=(
        "树种用拉丁学名（首次出现时附中文名）",
        "加工参数须用标准术语（温度、压力、时间）",
        "尺寸用 mm 或 cm",
        "密度用 kg/m³",
        "含水率用 %（百分比）"
    ),
    key_venues=(
        "Wood Science and Technology",
        "Journal of Wood Science",
        "Holzforschung",
        "Wood Fiber Science",
        "Journal of Bamboo and Rattan"
    ),
    units_and_formulas_notes=(
        "密度用 kg/m³",
        "含水率用 %（百分比）",
        "硬度用 N 或 J/cm²",
        "强度用 MPa",
        "尺寸用 mm"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Wood lathe", "Table saw", "Planer", "Jointer", "Drill press", "Bandsaw", "Moulder", "Spindle moulder", "Edge bander", "Cabinetmaker's bench", "Wood planer", "Wood lathe machine", "CNC router", "Laser cutter", "Wood chisel", "Hand plane", "Spokeshave", "Wood marking gauge", "Woodworking clamp", "Bamboo splitting machine"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
