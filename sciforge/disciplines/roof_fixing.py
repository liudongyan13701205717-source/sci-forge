"""屋顶施工学科论文支持：屋面材料、防水系统与施工检测。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="roof_fixing",
    aliases=(
        "roof_fixing",
        "屋顶施工",
        "屋面工程",
        "roofing",
        "防水工程",
        "屋面防水",
        "屋面板",
        "roof installation",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景）",
            "methodology（材料与试验方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（屋面案例）",
            "analysis（构造与施工分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（材料与规范综述）",
            "evidence synthesis（工程证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 或 GB/T 7714",
    reporting_standards={
        "material_test": "ASTM、EN 或 GB/T 方法须注明编号",
        "waterproofing": "渗漏检测时长与压力须符合 JGJ 或 ISO 规范",
        "thermal": "传热系数 U 值与热工模拟须给出参数",
    },
    conventions=(
        "屋面坡度以角度 ° 或百分比 % 表示",
        "材料抗拉/抗压强度 MPa；渗透率 mPa·s",
        "构造层次须按材料名称与厚度分层列出",
        "防水等级与设防年限须报告",
        "热工性能以 U 值 W/(m²·K) 报告",
    ),
    key_venues=(
        "Construction and Building Materials",
        "Building and Environment",
        "Journal of Building Engineering",
        "建筑材料学报",
        "防水技术",
    ),
    units_and_formulas_notes=(
        "防水层渗透性以 mPa·s 或渗透深度 mm 报告",
        "抗风揭能力以 kN/m² 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Waterproofing Membrane Analyzer", "Penetration Tester", "Tensile Testing Machine", "Thermal Imager", "Blower Door Test", "Hydrostatic Pressure Tester", "UV Accelerated Weather Tester", "Salt Spray Tester", "Flexometer Bending Tester", "Impact Tester", "Fire Resistance Tester", "Adhesion Tester", "Thermal Conductivity Tester", "Moisture Content Analyzer", "GPR Ground Penetrating Radar", "Spectrometer", "SEM-EDS", "3D Scanning Laser", "Building Envelope Simulation PHK", "ANSYS Structural"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
