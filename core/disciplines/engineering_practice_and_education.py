"""工程实践与教育学科论文支持：工程教育、工程伦理与工程实践研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="engineering_practice_and_education",
    aliases=(
        "engineering_practice_and_education", "工程实践与教育",
        "engineering practice and education", "工程实践与教育",
        "engineering education", "工程教育",
        "engineering ethics", "工程伦理",
        "professional engineering", "职业工程",
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
        "Journal of Engineering Education",
        "International Journal of Engineering Education",
        "European Journal of Engineering Education",
        "IEEE Transactions on Education",
        "Engineering Studies",
        "Journal of Professional Issues in Engineering Education and Practice",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm 表示",
        "力用 N 表示",
        "应力用 MPa 表示",
        "温度用 °C 表示",
        "效率用 % 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "ANSYS", "Abaqus", "SolidWorks", "AutoCAD", "CATIA", "NX", "Creo", "Inventor", "Fusion 360", "LabVIEW", "Python (numpy, scipy)", "R (RStudio)", "Excel", "Origin", "Mathematica", "Maple", "Arduino IDE", "Lab Streaming Platform"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
