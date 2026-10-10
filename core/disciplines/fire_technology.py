"""消防技术学科论文支持：火灾动力学、灭火系统、防火设计与火灾科学体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fire_technology",
    aliases=(
        "fire_technology", "消防技术", "消防工程",
        "fire engineering", "fire science",
        "火灾科学", "防火工程", "灭火技术", "消防安全",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（火灾问题与安全背景）",
            "methodology（实验设计、数值模拟、火灾模型）",
            "results（火灾动力学与灭火效果数据）",
            "discussion（火灾机理与安全意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（火灾事故案例描述）",
            "analysis（火灾蔓延、烟气与灭火分析）",
            "results（案例发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（消防技术研究综述）",
            "evidence synthesis（现有研究与缺口）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式；火灾科学论文亦常见 ASCE 或 ISO 引用规范",
    reporting_standards={
        "experimental": "火灾实验遵循 ISO 13931 火灾测试标准",
        "simulation": "数值模拟须注明 CFD 模型、网格与湍流模型",
        "fire_safety": "防火设计遵循 GB 50016 建筑设计防火规范",
        "material_testing": "材料燃烧性能遵循 GB 8624 标准",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "温度用 °C 或 K；热释放速率用 kW",
        "烟气浓度用 ppm 或 mg/m³",
        "燃烧性能按 GB 8624 或 ASTM 分类",
        "时间用 min 或 s 注明",
        "火焰传播速度用 m/s 表示",
    ),
    key_venues=(
        "Fire Safety Journal",
        "Journal of Fire Sciences",
        "Combustion and Flame",
        "Fire Technology",
        "Building and Environment",
        "Fire Prevention and Fire Protection Engineering",
    ),
    units_and_formulas_notes=(
        "温度 °C 或 K；热释放速率 kW",
        "烟气浓度 ppm 或 mg/m³；能见度 m",
        "燃烧速率 g/(m²·s)；热导率 W/(m·K)",
        "火焰传播速度 m/s；热通量 kW/m²",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("FDS（Fire Dynamics Simulator）", "ANSYS Fluent", "OpenFOAM", "SolidWorks", "AutoCAD", "Revit", "Rhino 3D", "MATLAB", "Python", "R", "Excel", "Tableau", "Endnote", "Zotero", "Minitab", "JMP", "OriginPro", "Thermal Imaging Camera", "Gas Analyzer", "Smoke Chamber"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
