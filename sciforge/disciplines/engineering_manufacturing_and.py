"""工程制造学科论文支持：制造工艺、制造系统与先进制造研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="engineering_manufacturing_and",
    aliases=(
        "engineering_manufacturing_and", "工程制造", "制造工程",
        "engineering manufacturing", "工程制造",
        "manufacturing engineering", "制造工程",
        "manufacturing systems", "制造系统",
        "advanced manufacturing", "先进制造",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（制造问题与背景）",
            "methodology（设计方法、实验条件、测试）",
            "results（制造效果与性能评估）",
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
        "Journal of Manufacturing Systems",
        "International Journal of Machine Tools and Manufacture",
        "Journal of Materials Processing Technology",
        "CIRP Annals - Manufacturing Technology",
        "Robotics and Computer-Integrated Manufacturing",
        "Journal of Manufacturing Processes",
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
    tools=("MATLAB", "Simulink", "ANSYS", "Abaqus", "SolidWorks", "AutoCAD", "CATIA", "NX", "Creo", "Inventor", "Fusion 360", "LabVIEW", "Python (numpy, scipy)", "R (RStudio)", "Excel", "Origin", "Mathematica", "Maple", "Mastercam", "Siemens TIA Portal"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
