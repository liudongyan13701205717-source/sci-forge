"""工程类跨学科项目与学位：研究、案例、综述体裁，IEEE 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interdisciplinary_programmes_and_qualifications_involving_engineering",
    aliases=(
        "interdisciplinary_programmes_and_qualifications_involving_engineering",
        "工程类跨学科项目与学位",
        "Engineering Interdisciplinary Programmes",
        "Cross-disciplinary Engineering",
        "Engineering Interdisciplinarity",
        "Engineering Degree Programme",
        "工程学跨学科",
        "工程学位项目",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（案例分析）",
            "results（发现）",
            "discussion（启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="IEEE（数字编号）",
    reporting_standards={
        "k1": "CONSORT（临床对照试验）",
        "k2": "PRISMA（系统综述）",
        "k3": "IEEE 报告规范",
    },
    conventions=(
        "设备型号与参数须完整列出",
        "实验环境与校准数据须报告",
        "误差分析与不确定度须给出",
        "图表单位符合 SI 标准",
        "代码与数据可用性声明须附",
    ),
    key_venues=(
        "Nature Reviews Engineering",
        "IEEE Transactions on Engineering Management",
        "Journal of Industrial Engineering",
        "Engineering Applications of Artificial Intelligence",
        "International Journal of Engineering Education",
    ),
    units_and_formulas_notes=(
        "SI 单位统一（kg、m、s、K、A、mol、cd）",
        "温度同时标注摄氏度与开尔文时须显式换算",
        "压力须区分绝对压力与表压",
        "统计量报告 M/SD/95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Simulink", "ANSYS", "COMSOL Multiphysics", "SolidWorks", "AutoCAD", "Revit", "LabVIEW", "Arduino IDE", "ROS", "TensorFlow", "PyTorch", "OpenFOAM", "LTspice", "Keil µVision", "OriginLab", "Mathematica", "Jupyter Notebook", "GitHub Codespaces", "GitLab"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
