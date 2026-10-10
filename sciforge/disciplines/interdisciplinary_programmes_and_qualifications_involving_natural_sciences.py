"""自然科学类跨学科项目与学位：研究、案例、综述体裁，Chicago 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interdisciplinary_programmes_and_qualifications_involving_natural_sciences",
    aliases=(
        "interdisciplinary_programmes_and_qualifications_involving_natural_sciences",
        "自然科学类跨学科项目与学位",
        "Natural Sciences Interdisciplinary Programmes",
        "Science Interdisciplinary Degree",
        "Cross-disciplinary Natural Science",
        "自然科学学位",
        "科学跨学科项目",
        "理学跨学科",
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
    citation_style="Chicago（脚注 + 参考列表）",
    reporting_standards={
        "k1": "ICMJE（医学期刊编辑委员会）",
        "k2": "PRISMA（系统综述）",
        "k3": "SI 单位规范",
    },
    conventions=(
        "实验重复次数与统计方法须说明",
        "试剂/仪器型号须完整列出",
        "误差分析采用 ±1 SD 或 95% CI",
        "图表单位使用 SI 标准",
        "数据可用性声明须附",
    ),
    key_venues=(
        "Nature",
        "Science",
        "Physical Review Letters",
        "Journal of the American Chemical Society",
        "Nature Reviews",
    ),
    units_and_formulas_notes=(
        "SI 单位优先，必要时标注传统单位",
        "统计量报告 mean ± SD 或 median (IQR)",
        "P 值与效应量须同时给出",
        "物理量须给出量纲与不确定度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Mathematica", "Python（NumPy）", "R", "OriginLab", "Origin", "Jupyter Notebook", "Gaussian", "VESTA", "Materials Studio", "ANSYS", "COMSOL Multiphysics", "Zemax", "LabVIEW", "GraphPad Prism", "GraphPad", "ImageJ", "Zen Software", "EndNote", "Reference Manager"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
