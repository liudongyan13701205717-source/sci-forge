"""家具制造学科论文支持：现代家具生产工艺、自动化制造与质量检测。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="furniture_making",
    aliases=("furniture_making", "furniture manufacturing", "家具制造", "家具生产", "木工机械", "家具工程", "板式家具", "家具自动化"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "production": "生产工艺须报告设备型号、加工参数与良品率",
        "quality": "质量检验须报告检测项目、标准与合格判定",
        "durability": "耐久性测试须遵循国标或 ISO 家具测试标准"
    },
    conventions=(
        "家具尺寸须用 mm 标注",
        "木材含水率须控制在 8-12%",
        "板材等级须用标准化等级标注",
        "涂层须注明涂料类型与涂覆厚度",
        "测试数据须报告均值与置信区间"
    ),
    key_venues=(
        "Journal of Wood Science and Technology",
        "Wood Science and Technology",
        "Journal of Materials in Civil Engineering",
        "Heritage",
        "International Journal of Sustainable Engineering"
    ),
    units_and_formulas_notes=(
        "板材厚度用 mm",
        "含水率用 %",
        "抗压强度用 MPa",
        "弯曲强度用 MPa",
        "甲醛释放量用 mg/m³"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Furniture CAD System", "3D Design Software", "Wood Cutting Machine", "Wood Pressing Machine", "Wood Sawing Machine", "Wood Drilling Machine", "Wood Sanding Machine", "Wood Gluing Machine", "Wood Painting Machine", "Wood Measuring Tool", "Wood Inspection Tool", "Wood Quality Tester", "Wood Finishing Machine", "Wood Processing Robot", "Wood CNC Machine", "Wood Laser Cutting", "Wood 3D Printing", "Wood Joinery Tool", "Wood Furniture Testing Machine", "Wood Assembly Equipment"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
