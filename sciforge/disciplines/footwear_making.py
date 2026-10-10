"""鞋类制造学科论文支持：皮革工程、鞋类设计、生产工艺与材料研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="footwear_making",
    aliases=("footwear_making", "footwear", "鞋类制造", "鞋类设计", "皮革工程", "鞋材研究", "鞋底工艺", "皮革加工"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "material": "材料性能须报告测试方法、标准编号与重复次数",
        "manufacturing": "生产工艺须报告参数、设备型号与批次信息",
        "wearing_test": "穿着测试须报告模拟条件、次数与磨损程度"
    },
    conventions=(
        "皮革厚度用 mm，鞋底硬度用 Shore A",
        "材料成分须用标准化测试方法测定",
        "鞋类型号须用标准化尺码标注",
        "生产工艺须注明设备型号与参数",
        "测试数据须报告均值±标准差"
    ),
    key_venues=(
        "Journal of Leather Science",
        "Leather & Tanning",
        "Footwear Science",
        "Journal of Industrial Textiles",
        "Materials & Design"
    ),
    units_and_formulas_notes=(
        "硬度用 Shore A",
        "厚度用 mm",
        "强度用 N 或 MPa",
        "磨耗用 mg 或 mm³",
        "拉伸强度用 N/mm²"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Footsize", "Vectorworks Footwear", "Rhino 3D", "SolidWorks", "Gerber Cutter", "Brother Embroidery", "Usha sewing machine", "Grotto Lasting", "Dainic Gluing", "Shoe Steamer", "Pressure Test Machine", "Color Difference Meter", "Abrasion Tester", "Material Tester", "Hot Press Machine", "Leather Dye Machine", "Footwear CAD System", "Pattern Cutting Machine", "3D Foot Scanner", "Leather Analyzer"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
