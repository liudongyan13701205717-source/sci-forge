"""制鞋与维修学科论文支持：鞋类设计、材料工艺与修复技术体裁及鞋类工程学规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="shoemaking_and_repairing",
    aliases=(
        "shoemaking_and_repairing",
        "制鞋",
        "制鞋与维修",
        "鞋类设计",
        "鞋类工程",
        "Shoemaking",
        "Footwear Design",
        "Shoe Repair",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（设计/实验方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工艺/修复案例）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份）",
    reporting_standards={
        "experimental": "材料试验须报告样品数量、加载速率、环境温湿度与标准号（ASTM/ISO/GB）",
        "design": "鞋楦设计须给出脚型测量方法与误差来源",
        "case": "修复案例须披露材质识别、工艺步骤与前后对比照片",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "鞋码采用 ISO 9409 或国家制（EU/US/UK/JP）并标注换算公式",
        "力学性能测试按 ASTM D6256（鞋帮）、D2633（弯曲）执行",
        "磨损试验采用 ASTM F2413 或 ISO 20344 标准",
        "所有材料成分以质量百分比（wt%）报告",
        "图表须标注测试条件与置信区间",
    ),
    key_venues=(
        "Footwear Science",
        "International Journal of Clothing Science and Technology",
        "Journal of Industrial Textiles",
        "Textile Research Journal",
        "中国皮革杂志",
    ),
    units_and_formulas_notes=(
        "弯曲刚度 J·mm 或 N·m；撕裂强度 N/mm",
        "耐磨次数以 Martindale 循环数计（ISO 12947）",
        "鞋楦尺寸以 mm 计；脚长 = 最长脚趾到脚跟距离",
        "重量以 g 计；密度以 g/cm³ 计",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CLO 3D", "FootScan", "AMASS 3D Scanner", "C-Tact Flex Analyzer", "ZwickRoell Z010", "Instron 5965", "Tinius Olsen Impact Tester", "Wearometer 6-Load", "Pleione 3D Body Scanner", "Adobe Substance Painter", "Grasshopper", "MATLAB", "Python（NumPy/Pandas）", "OpenFOAM", "ABAQUS", "SolidWorks", "Rhino 3D", "Adobe Illustrator", "Photoshop", "Autodesk Fusion 360"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ScienceDirect", "Scopus"),
)
