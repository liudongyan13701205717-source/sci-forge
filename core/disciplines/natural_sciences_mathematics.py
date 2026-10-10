"""自然科学与数学学科论文支持：综合理科数学研究体裁、学术引用规范与理科数学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="natural_sciences_mathematics",
    aliases=("natural_sciences_mathematics", "自然科学与数学", "理科数学",
             "科学与数学", "自然科学", "理科综合", "自然科学研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（理论/实验/计算方法）",
            "results（推导/实验结果）",
            "discussion（结论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（研究系统或现象）",
            "analysis（数学/物理建模）",
            "results（求解/验证结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论基础综述）",
            "evidence synthesis（现有方法证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式（理科常用）",
    reporting_standards={
        "experimental": "实验遵循科学报告规范",
        "mathematical": "数学证明遵循数学论文规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "statistical": "统计分析遵循 ASA 统计声明",
        "reproducibility": "可复现性遵循科学可复现性指南",
    },
    conventions=(
        "实验条件与参数须完整报告",
        "数学符号与公式须定义",
        "定理/引理/推论须分层编号",
        "数据/代码可用性须说明",
        "样本量与统计方法须报告",
    ),
    key_venues=(
        "Nature",
        "Science",
        "Physical Review Letters",
        "Journal of Mathematical Physics",
        "Proceedings of the National Academy of Sciences",
    ),
    units_and_formulas_notes=(
        "SI 单位",
        "公式用 amsmath；方程须编号",
        "定理/引理/推论编号",
        "数值结果给出均值 ± 标准差与样本量",
        "变量定义须完整",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python（NumPy/SciPy）", "R", "Mathematica", "Maple", "SageMath", "Julia", "Octave", "SymPy", "Jupyter Notebook", "LaTeX", "Wolfram Alpha", "Desmos", "Pandas", "scikit-learn", "Matplotlib", "OriginLab", "Excel", "Git/GitHub", "Coq（定理证明）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "万方"),
)
