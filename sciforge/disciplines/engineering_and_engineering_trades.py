"""工程与工程技术学科论文支持：工程技术、应用工程与工程实践研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="engineering_and_engineering_trades",
    aliases=(
        "engineering_and_engineering_trades", "工程与工程技术",
        "engineering and engineering trades", "工程与工程技术",
        "engineering technology", "工程技术",
        "applied engineering", "应用工程",
        "engineering practice", "工程实践",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程问题与背景）",
            "methodology（设计方法、实验条件、测试）",
            "results（工程效果与性能评估）",
            "discussion（技术改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "implementation（实现过程）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（技术对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "design": "设计参数须完整（尺寸、材料、载荷等）",
        "testing": "测试方法须注明（标准、仪器、环境）",
        "safety": "安全规程须声明",
    },
    conventions=(
        "尺寸用 mm 表示",
        "力用 N 表示",
        "应力用 MPa 表示",
        "温度用 °C 表示",
        "效率用 % 表示",
    ),
    key_venues=(
        "Journal of Engineering Design",
        "Engineering Structures",
        "Journal of Mechanical Design",
        "IEEE Transactions on Engineering Management",
        "Engineering Applications of Artificial Intelligence",
        "Advanced Engineering Informatics",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm 表示",
        "力用 N 表示",
        "应力用 MPa 表示",
        "温度用 °C 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "ANSYS", "Abaqus", "SolidWorks", "AutoCAD", "CATIA", "NX", "Creo", "Inventor", "Fusion 360", "LabVIEW", "Python (numpy, scipy)", "R (RStudio)", "Excel", "Origin", "Mathematica", "Maple", "Solid Edge", "Rhino"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
