"""家具工艺学科论文支持：木材加工、家具设计、传统工艺与材料创新。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="furniture_crafts",
    aliases=("furniture_crafts", "furniture", "家具工艺", "木作", "家具设计", "传统木作", "木工", "家具制造"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "material": "木材性能须报告树种、测试方法与标准编号",
        "craftsmanship": "传统工艺须记录工具、步骤与制作时长",
        "durability": "耐久性测试须报告载荷条件与测试次数"
    },
    conventions=(
        "木材尺寸须用 mm 标注",
        "木材含水率须报告（%）",
        "树种须用拉丁学名与中文名",
        "接合方式须用专业术语描述",
        "涂层须注明涂料种类与涂覆次数"
    ),
    key_venues=(
        "Journal of Wood Science and Technology",
        "Wood Science and Technology",
        "International Journal of Sustainable Engineering",
        "Heritage",
        "Journal of Materials in Civil Engineering"
    ),
    units_and_formulas_notes=(
        "木材含水率用 %",
        "密度用 g/cm³",
        "硬度用 Shore 或 MPa",
        "强度用 N 或 MPa",
        "含水率测试用烘箱法或 NCC 标准"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Furniture CAD Software", "3D Modeling Software", "Wood Drying Equipment", "Cutting Machine", "Sawing Machine", "Drilling Machine", "Sanding Machine", "Gluing Machine", "Painting Equipment", "Measuring Instrument", "3D Printing", "Laser Cutting Machine", "Wood Moisture Tester", "Wood Density Meter", "Wood Hardness Tester", "Wood Strength Tester", "Wood Quality Tester", "Wood Grading Machine", "Wood Processing Equipment", "Wood Finishing Machine"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
